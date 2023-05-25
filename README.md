# HistopathologyCancer_Classification

Build a breast cancer classifier on an IDC dataset that can accurately classify a histology image as benign or malignant using DENSENET.

## DATASET:
  IDC_regular dataset (the breast cancer histology image dataset) holds 9191 patches of size 50×50 extracted from 162 whole mount slide images of breast cancer specimens scanned at 40x. 
Of these, 4769 test negative and 4422 test positive with IDC.

## PREPROCESSING:
  Preprocessing such as Image resizing,Image normalization, and Data augmentation techniques applied to the images to increase the diversity of the training data and improve the generalization of the model.

## MODELS USED:
After splitting the dataset to train and test sets, 2 models were built on the histology dataset and their results are compared.
    - CNN model
    - DenseNet model (fine tuning)

## INFERENCE:
  - CNN model was trained to get the accuracy of 87% and densenet with fine tuning of 90% and densenet coded with 91% testing accuracy
  - And the image loaded from the dataset was predicted correctly to have IDC cancer or not.
  - CNN model has huge difference between training and testing accuracy, that is, tha model is overfitted.
  - But for the densenet models both training and testing accuracies are similar. Thus a best model is trained. And no overfitting occured.
  
## DEPLOYMENT:
The trained model was deployed using Streamlit, a Python web application framework. 
The user can upload an image and the model will make predictions on the uploaded image. The predicted class and probability are displayed to the user.

This project demonstrates the effectiveness of deep learning for the detection of IDC cancer in histopathological images. The developed model achieved high accuracy on the validation and test sets, indicating its potential for use in real-world scenarios.

* Detailed description of the project is given in the documentation

