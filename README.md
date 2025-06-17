# 🎨 Text-to-Image Generator with Stable Diffusion (Gradio Interface)

This project provides a simple and interactive **Gradio web UI** for generating high-quality images from text prompts using **Stable Diffusion v1.5** and **Stable Diffusion XL 1.0**.

---

## 📷 Demo Preview

### 🔹 Stable Diffusion v1.5 (CFG=8)
![sd1_5](https://github.com/user-attachments/assets/88607794-367a-48f2-aae5-9056f0ab7e9b)

### 🔸 Stable Diffusion XL 1.0 (CFG=8)
![xl0_1](https://github.com/user-attachments/assets/58ca167f-3946-477c-afa3-762d5010ec12)
---

## 🚀 Features

-  Generate images from custom text prompts
-  Choose between two powerful models: **SD 1.5** or **SDXL 1.0**
-  Adjustable **CFG (Classifier-Free Guidance)** slider (0 to 50)
-  Negative prompt support to guide unwanted content
-  Fully interactive via a modern Gradio interface

---


## 🧪 Technologies Used

- [🤗 HuggingFace Diffusers](https://huggingface.co/docs/diffusers/index)
- [Gradio](https://gradio.app)
- PyTorch
- TorchVision
- CUDA (GPU recommended for full functionality)

---

## 🧠 Supported Models

| Model Name | Description |
|------------|-------------|
| **Stable Diffusion v1.5** | Lightweight and fast, great for general-purpose generations. |
| **Stable Diffusion XL 1.0** | More accurate, photorealistic images, but heavier on GPU usage. |

> ℹ️ **Default behavior:**  
> - If **no model** is explicitly selected, the app **automatically uses SD v1.5**  
> - The **default CFG value** is set to `8.0`, which is a balanced value for most prompts.

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/text-to-image-gradio.git
cd text-to-image-gradio

#Install dependencies (ideally in a virtual environment):
pip install -r requirements.txt

#Launch the app:
python app.py
```

## ✏️ Usage
Enter your prompt (e.g., A futuristic city at sunset)

Optionally, enter a negative prompt (e.g., blurry, distorted, extra limbs)

Adjust CFG scale between 0 – 50 (higher = stricter adherence to prompt)

Click on a model button (SD1.5 or SDXL) to select your model

Click Generate to create the image

## 🧪 Example Prompt 
Prompt:
A majestic cyberpunk city at night, glowing neon lights, futuristic buildings, flying cars, rainy street reflections, ultra-detailed, cinematic lighting

Negative Prompt (Optional):
blurry, distorted, low resolution, extra limbs, bad anatomy, deformed, oversaturated

CFG: 8.0


## ⚠️ Notes
Make sure you have CUDA-enabled GPU for inference (especially for SDXL)

On CPU-only environments like Hugging Face Spaces (without GPU), image generation will fail


## ✨ Credits
[StabilityAI - SD & SDXL Models]([https://gradio.app](https://huggingface.co/stabilityai))

[Hugging Face Diffusers]([https://gradio.app](https://github.com/huggingface/diffusers))

[Gradio Team]([https://gradio.app](https://github.com/gradio-app/gradio))
