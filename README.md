# Benchmarking Bias in Text-to-Image Models with Prompt Engineering

### Abhika Mishra and Grace Brigham


This is the repository for our CSE582 (Ethics in AI) course project.

## Image Generation

To generate images you need to run generate.py, you can do so with this command:

```
python --lightning --prompt 1 --num_images 50
```
You can specify which of the three models you want to run with one of the following: 
- ```--lightning```, run the SDXL-Lightning model
- ```--sdxl```, run the SDXL model
- ```--sdv4```, run the Stable Diffusion v1.4 model
  
You can specify which of the three prompts you want to run with one of the following:
- ```--prompt 1```, for base/neutral prompt
- ```--prompt 2```, for first engineered prompt - controlling for gender
- ```--prompt 3```, for second engineered prompt, representing diverse populations

NOTE: You will need access to a gpu in order to generate images.

## Image Tagging
You can access the raw tags data in `labels.csv` without running any code.

If you would like to run the tagging script, create an AWS account and set up Rekognition following [these steps](https://docs.aws.amazon.com/rekognition/latest/dg/getting-started.html).

The images generated for this project can be accessed in or download from [this Google Drive folder](https://drive.google.com/drive/folders/1lqd6F8RKPBKlyaighcXda_LLpxVEqyK2?usp=sharing). To run the Rekognition script on them, download the folder `582_Images` and place it in the root folder of this repository.

If you would like to run the script on images you have generated, create a folder called `582_Images` folder that follows the same structure and naming conventions as the one in [the Google Drive](https://drive.google.com/drive/folders/1lqd6F8RKPBKlyaighcXda_LLpxVEqyK2?usp=sharing).

In your AWS environment, run the following command:

```bash
python rekognition.py
```

The resulting tags will be stored in `labels.csv`.
