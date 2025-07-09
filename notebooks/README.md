# Model Card

Guava (Psidium guajava) is a key crop in South Asia, especially in Bangladesh. Rich in vitamin C and fiber, it supports regional economies and nutrition. Unfortunately, guava production is threatened by diseases that reduce yields. This dataset is designed to aid the development of machine learning models for early disease detection in guava fruit, helping to protect harvests and reduce economic losses.

**The aim of this project is to develop a machine learning model for early disease detection in guava fruit, helping to protect harvests and reduce economic losses.** The model takes in images of guava fruits and classifies them into three categories: Anthracnose, Fruit Flies, or Healthy fruits. This classification can help farmers identify diseases early and take appropriate action to minimize crop losses. 

<details>
<summary>Model card explanation</summary>
    Model cards are a succinct approach for documenting the creation, use, and shortcomings of a model. The idea is to write a documentation such that a non-expert can understand the model card's contents. For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf.
</details>


## Model Details

[@Miguel-mmf](https://github.com/Miguel-mmf) created the model using PyTorch and a custom CNN architecture. The project utilizes Python programming language along with PyTorch, Scikit-Learn, and other machine learning libraries to develop an image classification model for guava disease detection. The model is designed to classify guava fruit images into three categories: Anthracnose, Fruit Flies, and Healthy fruits.

## Intended Use

This model is being used as a proof of concept for the first project in the Machine Learning programme at the Federal University of Rio Grande do Norte's [PPGEEC](https://sigaa.ufrn.br/sigaa/public/programa/portal.jsf?id=103).


## Training Data

The dataset used in this project is based on the Guava Fruit Disease Dataset downloaded from: https://www.kaggle.com/datasets/asadullahgalib/guava-disease-dataset/data?select=GuavaDiseaseDataset.

Original dataset from Mendeley Data:
> Amin, Md Al; Mahmud, Md Iqbal; Rahman, Asadullah Bin; Parvin, Mst Aktarina; Mamun, Md Abdulla Al (2024), "Guava Fruit Disease Dataset", Mendeley Data, V1, doi: 10.17632/bkdkc4n835.1

### Dataset Summary

The dataset includes 473 annotated images of guava fruits, categorized into three classes. Images underwent preprocessing steps such as unsharp masking and CLAHE. The preprocessed images are augmented to increase to 3,784 image data. The three classes are:

* **Anthracnose**: A fungal disease that causes dark spots on guava fruits
* **Fruit Flies**: Pest infestation that damages the fruit
* **Healthy fruits**: Normal, disease-free guava fruits

Images were collected from guava orchards in Rajshahi and Pabna, Bangladesh, during the fruit-ripening season in July when disease vulnerability is highest. A plant pathologist verified the images for accuracy in classification. Each image was preprocessed to a consistent size of 512 x 512 pixels in RGB format, suitable for deep learning and image processing applications.


## Evaluating Data

The dataset under study is split into Train, Validation, and Test during the preprocessing stage. The data is divided into training (69.95%), validation (19.95%), and test (10.10%) sets to ensure proper model evaluation and avoid overfitting.


## Metrics

In order to follow the performance of machine learning experiments, the project marked certain stage outputs of the data pipeline as metrics. The metrics adopted are: 
* [**Accuracy**](https://scikit-learn.org/stable/modules/model_evaluation.html)
<p align="center">
$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$
</p>
where TP = True Positives, TN = True Negatives, FP = False Positives, and FN = False Negatives.

* [**f1**](https://scikit-learn.org/stable/modules/model_evaluation.html)
<p align="center">
$\text{F1} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$
</p>

* [**Precision**](https://scikit-learn.org/stable/modules/model_evaluation.html)
<p align="center">
$\text{Precision} = \frac{TP}{TP + FP}$
</p>

* [**Recall**](https://scikit-learn.org/stable/modules/model_evaluation.html)
<p align="center">
$\text{Recall} = \frac{TP}{TP + FN}$
</p>

The follow results will be shown:

| Dataset | Threshold | Accuracy | F1 Score | Precision | Recall |
|-----------|-----------|----------|----------|-----------|--------|
| Train     |   0.05    |  0.9000  |  0.7757  |   0.7524  | 0.8005 |
| Test      |   0.05    |  0.9058  |  0.8241  |   0.8367  | 0.8119 |

**Threshold explanation:**  
The threshold value determines the cutoff for classifying predictions as positive or negative. Different thresholds can impact the balance between precision and recall. The chosen threshold (0.05) was selected based on the evaluation of metrics for each threshold value, aiming to achieve a good trade-off between accuracy, precision, recall, and F1 score.


## Ethical Considerations

When developing machine learning models for agricultural applications, it's important to consider that this dataset represents only one specific geographic region (Bangladesh) and specific conditions. The model's performance may vary when applied to different regions, climates, or guava varieties. We acknowledge that this is not a comprehensive representation of all possible guava disease scenarios.


## Caveats and Recommendations

It should be noted that the model trained in this project was used only for validation. It is important to note that some issues related to dataset imbalances exist, and adequate techniques need to be adopted in order to balance it. The model should be tested with additional data from different geographic regions and under various environmental conditions before deployment in real-world agricultural settings.



<div align="center">
<img src="https://avatars.githubusercontent.com/u/69444221?v=4" alt="Miguel-mmf" width="80" style="border-radius: 50%; display: block; margin: 0 auto;"/>

**Miguel Marques**  
[GitHub](https://github.com/Miguel-mmf) • [LinkedIn](https://www.linkedin.com/in/miguelmf08) • [Gmail](miguel.ferreira@estudante.cear.ufpb.br) • [Gmail](miguel.ferreira.111@ufrn.edu.br)
</div>
