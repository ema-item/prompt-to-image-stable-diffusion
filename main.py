from diffusers import StableDiffusionPipeline, DiffusionPipeline
import matplotlib.pyplot as plt
import gradio as gr
import torch, gc
################################################ SD1.5
pipe_sd1_5  = StableDiffusionPipeline.from_pretrained(
    "sd-legacy/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)
################################################# SDXL
gc.collect()
torch.cuda.empty_cache()

pipe_sdxl = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16"
)

refiner = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-refiner-1.0",
    text_encoder_2=pipe_sdxl.text_encoder_2,
    vae=pipe_sdxl.vae,
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16",
)
################################################
def generate_image(prompt, negative_propt="", CFG=8.0, width=512, height=512, sd1_5_model=True):
    gc.collect()
    torch.cuda.empty_cache()

    if sd1_5_model == True:
        pipe_sd1_5.to("cuda", device_map="auto")
        image = pipe_sd1_5(prompt, negative_prompt=negative_propt, guidance_scale=CFG, height=height, width=width).images[0]
        model_name = "Stable Diffusion v1-5"

    else:
        pipe_sdxl.to("cuda", device_map="auto")
        refiner.to("cuda", device_map="auto")

        n_steps = 40
        high_noise_frac = 0.5

        image = pipe_sdxl(prompt=prompt, num_inference_steps=n_steps, guidance_scale=CFG, denoising_end=high_noise_frac, output_type="latent", height=height, width=width).images
        image = refiner(prompt=prompt, num_inference_steps=n_steps, denoising_start=high_noise_frac, image=image,).images[0]
        model_name = "Stable Diffusion XL 1.0"


    cfg_value = f"CFG: {CFG}"

    return image, model_name, cfg_value, width, height

###########################
with gr.Blocks() as demo:
    gr.Markdown('# Text-to-Image with Stable Diffusion🎨✨')

    with gr.Row(equal_height=True):
        with gr.Column():
            use_sd1_5 = gr.State(value=True)

            prompt = gr.Textbox(lines=1, label='Prompt', placeholder="Enter a prompt here...",
                                info="Describe what you want to see in the image.\n example: A futuristic city at sunset")

            N_prompt = gr.Textbox(lines=1, label='Negative Prompt', placeholder="Enter the negative prompt here...",
                                  info="Describe what you want to avoid in the image.\n example: blurry, distorted, extra limbs")

            CFG = gr.Slider(value=8.0, label='Classifier-Free Guidance(CFG)', minimum=0, maximum=50, step=0.5,
                           info = """
**CFG (Classifier-Free Guidance):**
Controls how closely the image generation should follow your prompt.

- **1–4 (Low):** More creative or random outputs, less focused on prompt.
- **5–12 (Medium):** Balanced results, good prompt adherence.
- **13–20+ (High):** Very strict to prompt, may lose diversity.

💡 *Typical values: 7.0 – 12.0*
""")
            with gr.Row():
                width = gr.Slider(value=512, label='Width', minimum=256, maximum=704, step=64)
                height = gr.Slider(value=512, label='Height', minimum=256, maximum=704, step=64)

            with gr.Row():
                button_sd1_5 = gr.Button("SD1.5 model", variant='secondary')
                button_sdx_l = gr.Button("SDXL model", variant='secondary')

        with gr.Column():
            image = gr.Image(height=450)
            button_gen = gr.Button("Generate", variant='primary')

            with gr.Row():
                model_info=gr.Textbox(lines=1, label='Model', interactive=False)
                cfg_imfo=gr.Textbox(lines=1, label='CFG Value', interactive=False)

            with gr.Row():
                width_info=gr.Textbox(lines=1, label='Width', interactive=False)
                height_imfo=gr.Textbox(lines=1, label='Height', interactive=False)

    button_sd1_5.click(fn=lambda: True,  outputs=use_sd1_5)
    button_sdx_l.click(fn=lambda: False, outputs=use_sd1_5)

    button_gen.click(
        fn=generate_image,
        inputs=[prompt, N_prompt, CFG, width, height, use_sd1_5],
        outputs=[image, model_info, cfg_imfo, width_info, height_imfo]
    )

demo.launch()
