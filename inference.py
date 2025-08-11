# inference.py
import os
import torch
from diffusers import StableDiffusionPipeline

MODEL = "runwayml/stable-diffusion-v1-5"   # or any model you chose (check its page & accept terms)
# If you used hf auth login, the pipeline can use that token automatically.

pipe = StableDiffusionPipeline.from_pretrained(MODEL, torch_dtype=torch.float16)
pipe = pipe.to("cuda")   # or "cpu" if no GPU (slow)

def generate(prompt, steps=30, guidance=7.5):
    out = pipe(prompt, num_inference_steps=steps, guidance_scale=guidance)
    return out.images[0]

if __name__ == "__main__":
    img = generate("A cyberpunk city at sunset, ultra-detailed")
    img.save("example.png")
