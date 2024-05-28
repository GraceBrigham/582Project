# Benchmarking Bias in Text-to-Image Models with Prompt Engineering

### Abhika Mishra and Grace Brigham


This is the code and image repository for our CSE582 (Ethics in AI) course project.

## Image Generation

To generate images...

## Image Tagging
You can access the raw tags data in `labels.csv` without running any code.

If you would like to run the tagging script, create an AWS account and set up Rekognition following [these steps](https://docs.aws.amazon.com/rekognition/latest/dg/getting-started.html).

If you would like to run the script on images you have generated, replace the `582_Images` folder with your own that follows the same structure and naming conventions. Otherwise, you can leave the folder as is.

In your AWS environment, run the following command:

```bash
python rekognition.py
```

The resulting tags will be stored in `labels.csv`.