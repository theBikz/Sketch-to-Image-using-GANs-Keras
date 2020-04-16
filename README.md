# Sketch-to-Image-using-GANs-Keras-
Realistic Images are generated from Hand Drawn Sketches using conditional GANs. Implemented using Keras API. 

Shoe data used is edges2shoes dataset from pix2pix. They created it using UT Zappos50K data. 
Hat data is a data set created by myself.
I used both Colab and Jupyter Notebook. 

Code can be run on both CPU and GPU (GPU preferred)

For creating your own dataset, use the Data_Preperation.ipynb (Edit the path)

Creating_Data_for_Training.ipynb is for creating a .npz file of the dataset with training parameters.

Sketch2Shoes.ipynb is for training the shoes data and save the model.

Sketch2Hat.ipynb is for training the Hat data and save the model.

Generating_Images.ipynb is for Generate Realistic images from sketches using the model and save the Generated image.

Splitting_Data is for splitting the dataset to sketch and real image seperately. (refer the dataset image for understanding)
