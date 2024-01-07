# Kidney-Disease-Classification-MLflow-DVC

Welcome to Kidney-Diseases-Classification-DVC-MLflow, an end-to-end deep-learning project focused on kidney disease classification. This project incorporates the power of Flask, VGG16, MLflow, and DVC, placing a strong emphasis on the model's performance and the modularity of the project.

## Pretrained Model Details

The classification model utilizes the VGG16 architecture, a powerful convolutional neural network (CNN) that has proven effective in image classification tasks. VGG16 was originally proposed by the Visual Geometry Group at the University of Oxford. It consists of 16 weight layers and has been pre-trained on large-scale image datasets.

## Project Highlights

- **VGG16 Model Integration:** This project leverages the VGG16 model for accurate kidney diseases classification. The VGG16 architecture's ability to capture intricate features in medical images makes it an ideal choice for this classification task.

- **Modularity:** Designed with modularity in mind, Kidney-Diseases-Classification-DVC-MLflow provides a flexible and adaptable architecture. Easily customize and extend the project to suit your specific image classification needs.

- **MLflow Integration:** MLflow is seamlessly integrated into the project to track experiments, log parameters, and save models. This facilitates reproducibility and allows for efficient model management.

- **DVC Integration:** DVC (Data Version Control) is employed to handle data versioning, ensuring reproducibility and efficient management of large datasets.

- **Flask for Deployment:** The Flask web framework is utilized for deploying the kidney diseases classification model, providing an easy-to-use interface for end-users.


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Yashmori09/Kidney-Diseases-Classification-DVC-MLflow.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
python -m venv <folder path> <virtual env name>
```

```bash
<virtual env name>\Scripts\activate.bat
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```






## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=<Enter your URI> \
MLFLOW_TRACKING_USERNAME=<Enter your username> \
MLFLOW_TRACKING_PASSWORD=<enter your password> \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=<Enter your URI> 

export MLFLOW_TRACKING_USERNAME=MLFLOW_TRACKING_USERNAME=<Enter your username>  

export MLFLOW_TRACKING_PASSWORD=MLFLOW_TRACKING_PASSWORD=<enter your password>

```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

