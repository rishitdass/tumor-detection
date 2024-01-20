# tumor-detection
Tumor detection using Deep Leanring
# Tumor Detection Model

## Overview

This repository contains the code for a Tumor Detection Model using Convolutional Neural Networks (CNN). The model is trained on a dataset sourced from Kaggle, with the goal of accurately classifying tumors in medical images.

## Dataset

The dataset used for training can be found on Kaggle [here](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset). Download and use the dataset for training and testing your model.

## Model Summary

The model architecture involves the use of CNN layers for effective feature extraction. The training results indicate a promising accuracy of 93%. See key metrics below:
## Convolutional Neural Network (CNN) Workflow

The image below provides a visual representation of the key components and the flow of information through the layers of the CNN.

<img src="https://images.datacamp.com/image/upload/v1681492916/Architecture_of_the_CN_Ns_applied_to_digit_recognition_0d403dcf68.png" alt="CNN Workflow" width="600">



## Training Progress: Accuracy vs Validation Accuracy

Monitor the training progress of the Tumor Detection Model with the following plot illustrating the #*Training Accuracy and Validation Accuracy across epochs.*

<img src="https://github.com/rishitdass/tumor-detection/blob/81c8ae30101a8591a9d51e2115a8f6cfc4b6abec/Accuracy%20Plot.png" alt="Accuracy accros epochs" width="700">

Monitor the training progress of the Tumor Detection Model with the following plot illustrating the #*Training Loss and Validation Loss across epochs.*

<img src="https://github.com/rishitdass/tumor-detection/blob/1ad9516ef3fa5a982aae9ea3c0ff648b6e1b55ba/loss%20plot.png" alt="Loss across epochs" width="700">

## Model Evaluation

 Here's the classification report:

          precision    recall  f1-score   support

       0       0.88      0.95      0.91       307
       1       0.91      0.82      0.86       347
       2       0.96      0.95      0.96       402
       3       0.95      0.99      0.97       349

accuracy                           0.93      1405



## Model Prediction with Streamlit

Experience the live predictions of the Tumor Detection Model using the Streamlit web application. The screenshot below showcases the user interface where you can upload an image and witness the model's predictions.

<img src="https://github.com/rishitdass/tumor-detection/blob/5b2b36f1dc794a9816b4e8a83283c16eb918943b/streamlit%20screenshot.png" alt="Loss across epochs" width="700">

Explore the user-friendly interface and observe how the model predicts tumor presence based on the input image, providing valuable insights into its real-time performance.

## FINAL Thoughts

As i conclude the Tumor Detection Model project, here are some reflections on the journey. Delving into the world of CNNs and medical imaging has been both challenging and exhilarating.

Excitingly, the model has reached an impressive accuracy of 93%, and the addition of a Streamlit web app brings a touch of real-time magic to the experience.

I'm genuinely looking forward to showcasing the project and hearing your thoughts. Working on this has been a great experience, and I can't wait to discuss it further.

Cheers.

