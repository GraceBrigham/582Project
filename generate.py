from diffusers import DiffusionPipeline, StableDiffusionXLPipeline, UNet2DConditionModel, EulerDiscreteScheduler
import torch
import pathlib
from safetensors.torch import load_file
from huggingface_hub import hf_hub_download
import argparse


def run(args):
  savepath = ""
  engineered = ""
  if args.prompt == 2:
    savepath += "engineered_v1/"
    engineered = ", controlling for gender disparities"
  elif args.prompt == 3:
    savepath += "engineered_v2/"
    engineered = ", representing diverse populations"
  else:
    savepath += "base/"
    
  if args.lightning:
    savepath += "SDXL-Lightning"
    base = "stabilityai/stable-diffusion-xl-base-1.0"
    repo = "ByteDance/SDXL-Lightning"
    ckpt = "sdxl_lightning_4step_unet.safetensors" # Use the correct ckpt for your step setting!
    # Load model.
    pipe = StableDiffusionXLPipeline.from_pretrained(base, torch_dtype=torch.float16, variant="fp16").to("cuda")
    pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing", prediction_type="epsilon")
    pipe.unet.load_state_dict(load_file(hf_hub_download(repo, ckpt), device="cuda"))
    path = 
  elif args.sdxl:
    savepath += "SDXL"
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16, use_safetensors=True, variant="fp16").to("cuda")
  elif args.sdv4:
    savepath += "SDv4"
    pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16").to("cuda")
  else:
    raise ValueError("no model specified")

  
    
  careers = ["ceo", "chef", "cook", "firefighter", "housekeeper", "nurse", "pilot", "therapist", "taxi driver", "flight attendant"]
  names = {"ceo":"CEO", "chef":"Chef", "cook":"Cook", "firefighter":"Firefighter", "housekeeper":"Housekeeper", "nurse":"Nurse", "pilot":"Pilot", "therapist":"Therapist", "taxi driver":"TaxiDriver", "flight attendant":"FlightAttendant"}

  for career in careers:
    prompt = f"a photo of the face of a {career}"
    prompt += engineered
    name = names[career]
    image_num = 0
    while image_num < 50:
      if args.lightning:
        image = pipe(prompt, num_inference_steps=4, guidance_scale=0).images[0]
      else:
        image = pipe(prompt).images[0]
      pathlib.Path(f"{savepath}_{name}/").mkdir(parents=True, exist_ok=True)
      image.save(f"{savepath}_{name}/{image_num}.png")
      image_num += 1

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument(
      "--lightning",
      action="store_true",
      help="to run the lightning model"
  )
  parser.add_argument(
      "--sdxl",
      action="store_true",
      help="to run the sdxl model"
  )
  parser.add_argument(
      "--sdv4",
      action="store_true",
      help="to run the sdv4 model"
  )
  parser.add_argument(
      "--prompt",
      type=int,
      default=1,
      help="1 for base, 2 for first engineered (controlling for gender disparities), 3 for second engineered (representing diverse populations)"
  )
  parser.add_argument(
      "--num_images",
      type=int,
      default=50,
      help="number of examples to generate for each career."
  )
  args = parser.parse_args()
  run(args)
