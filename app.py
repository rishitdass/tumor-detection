import tensorflow as tf
from tensorflow import keras
import PIL
import streamlit as st
import cv2
import numpy as np



model = keras.models.load_model("E:/Programming/Projects/Brain Tumor Detection/braintumorModel.h5")

st.title("Brain Tumor Detection")
st.header("Please upload your image here")

file=st.file_uploader(" ",type=['jpg','jpeg','png'])


if file is not None:
    image=PIL.Image.open(file).convert('RGB')
    st.image(image,use_column_width=True)

    file_arr = np.array(image)
    file_arr=cv2.resize(file_arr,(180,180))
    file_arr=file_arr/255

    file_arr = np.expand_dims(file_arr, axis=0)

    outcome=np.argmax(model.predict(file_arr))
    names=['glioma tumor','meningioma tumor','no tumor','pituitary tumor']
    st.write("Predicted class:", names[outcome])