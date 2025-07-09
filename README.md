# Project overview

Guava (Psidium guajava) is a key crop in South Asia, especially in Bangladesh. Rich in vitamin C and fiber, it supports regional economies and nutrition. Unfortunately, guava production is threatened by diseases that reduce yields. This dataset is designed to aid the development of machine learning models for early disease detection in guava fruit, helping to protect harvests and reduce economic losses.

**The aim of this project is to develop a machine learning model for early disease detection in guava fruit, helping to protect harvests and reduce economic losses.** 

## Environment setup

To configure the virtual environment, follow the steps below:

1. Clone the repository
2. [Install UV](https://docs.astral.sh/uv/getting-started/installation/)
3. [Install dependencies using UV](https://docs.astral.sh/uv/concepts/projects/)


### **Requirements:**
- Python 3.12+
- UV


****
## Data

The dataset used in this project is based on the original csv was downloaded from: https://www.kaggle.com/datasets/asadullahgalib/guava-disease-dataset/data?select=GuavaDiseaseDataset.

Actual dataset from Mendeley Data:
> Amin, Md Al; Mahmud, Md Iqbal; Rahman, Asadullah Bin; Parvin, Mst Aktarina; Mamun, Md Abdulla Al (2024), “Guava Fruit Disease Dataset”, Mendeley Data, V1, doi: 10.17632/bkdkc4n835.1

### Dataset Summary

The dataset used for this project includes 473 annotated images of guava fruits, categorized into three classes. Images underwent preprocessing steps such as unsharp masking and CLAHE. The preprocessed images are augmented to increase in number to 3,784 image data. The three classes are:

* Anthracnose
* Fruit Flies
* Healthy fruits

Images were collected from guava orchards in Rajshahi and Pabna, Bangladesh, during the fruit-ripening season in July when disease vulnerability is highest. A plant pathologist verified the images for accuracy in classification. Each image was preprocessed to a consistent size of 512 x 512 pixels in RGB format, suitable for deep learning and image processing applications.


## Materials

* [Guava Fruit Disease Dataset](https://www.kaggle.com/datasets/asadullahgalib/guava-disease-dataset/data?select=GuavaDiseaseDataset)
* [Guava Disease Classification Using CNN](https://www.kaggle.com/code/sandeepnayak144/guava-disease-classification-using-cnn)

___
**Feel free to contribute and explore the project!**
