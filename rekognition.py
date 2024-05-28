#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
import boto3
import pandas as pd
import os

def detect_labels_local_file(photo):
    print('Detected labels in ' + photo)
    client = boto3.client('rekognition')
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        
    labels = {}
    for label in response['Labels']:
        labels[label['Name']] = label['Confidence']
    return labels

def main():
    careers = [
        "CEO",
        "Chef",
        "Cook",
        "Firefighter",
        "FlightAttendant",
        "Housekeeper",
        "Nurse",
        "Pilot",
        "TaxiDriver",
        "Therapist"
    ]

    prompts = [
        "Base",
        "Engineered_v1",
        "Engineered_v2"
    ]

    models = [
        "SDv4",
        "SDXL",
        "SDXL-Lightning"
    ]
    labels_data = []
    for model in models:
        for career in careers:
            for prompt in prompts:
                folder_path = f'./582_Images/{model}/{career}/{model}_{career}_{prompt}'
                for filename in os.listdir(folder_path):
                    if filename != '.DS_Store':
                        image_path = os.path.join(folder_path, filename)
                        labels = detect_labels_local_file(image_path)

                        gender = None
                        if 'Man' in labels.keys():
                            gender = 'Man'
                        elif 'Woman' in labels.keys():
                            gender = 'Woman'

                        sex = None
                        if 'Male' in labels.keys():
                            sex = 'Male'
                        elif 'Female' in labels.keys():
                            sex = 'Female'

                        labels_data.append({
                            'Career': career,
                            'Prompt': prompt,
                            'Model': model,
                            'File Path': image_path,
                            'Sex': sex,
                            'Gender': gender,
                            'Labels': labels
                        })

            df = pd.DataFrame(labels_data)
            df.to_csv('intermediate_labels.csv', index=False)

        df = pd.DataFrame(labels_data)
        df.to_csv('labels.csv', index=False)
        

if __name__ == "__main__":
    main()

