# "CHECK FIRST"

# Overview:
The focus of this project is to use Machine Learning and Deep Learning models to determine the risk of common health diseases. We choose COPD (Chronic Obstructive Pulmonary Disease) and Dementia as two common diseases to analyze. 

# Installation:
The Jupyter Lab Notebook `Analysis.ipynb` can be accessed by making sure the required packages and programs are installed.
1. Install the latest verion of Python.
2. Install the latest version of Anaconda.
3. Install the hvplot package.
4. Install the scikit-learn packages.
5. Install tensorflow package.
6. Install the joblib package.
7. Install the pickle package.

The final models are also deployed for testing on [streamlit](https://check-first.streamlit.app/)

# HYPOTHESIS: Risk Analysis with "CHECK FIRST"
"Check First" is an app created specifically to analyze health-related risk behaviors, chronic health conditions, and the use of preventive services connected to the risk for COPD(Chronic Obstructive Pulmonary Disease) and Dementia.

# EXPLAINED DISEASE 1
## COPD (Chronic Obstructive Pulmonary Disease)
Chronic obstructive pulmonary disease (COPD) is a lung disease that makes it hard to breathe. Two main forms of COPD: Chronic bronchitis, which involves a long-term cough with mucus and Emphysema, which involves damage to the lungs over time. Most people with COPD have a combination of both conditions.

### Risk factors:
Smoking 
Exposure to certain gases or fumes in the workplace
Exposure to heavy amounts of secondhand smoke and pollution
Frequent use of a cooking fire without proper ventilation 

### Symptoms :
Cough, with or without mucus
Fatigue
Frequent respiratory infections
Shortness of breath (dyspnea) that gets worse with mild activity
Trouble catching one's breath
Wheezing

# Explained DISEASE 2
## Dementia
Dementia is a general term for loss of memory, language, problem-solving, and other thinking abilities that are severe enough to interfere with daily life. Alzheimer's is the most common cause of dementia.

### Causes 
Depression.
Medication side effects.
Excess use of alcohol.
Thyroid problems.
Vitamin deficiencies.

### Symptoms
Short-term memory.
Keeping track of a purse or wallet.
Paying bills.
Planning and preparing meals.
Remembering appointments.
Traveling out of the neighborhood.

# Datasets Used:
1. For COPD, we used BRFSS (Behavioral Risk Factor Surveillance System) Dataset 
2. For Dementia, we used NHAMCS (National Hospital Ambulatory Medical Care Survey) Dataset

# DATA CLEANUP & MODEL TRAINING:

## BRFSS Dataset (Behavioral Risk Factor Surveillance System)
The Behavioral Risk Factor Surveillance System (BRFSS) is a health survey that collects data on behavioral risk factors. It is administered by the Centers for Disease Control and Prevention and conducted in all 50 states and US territories by participating individual state health departments. It gives communities, states, and federal agencies and information they need to plan public health programmes and other activities at local, state, and national levels.

## Preprocessing of BRFSS Dataset
We preprocessed and cleaned the BRFSS Dataset. From 304 unique variables, We hand-picked 19 variables that relates to lifestyle factors of a person that can be contributed to being at risk with any form of COPD (Chronic Obstructive Pulmonary Disease). The data was from BRFSS dataset that was collected from CDC. Data preprocessing was done using pandas. We selected the relevant columns and dropped the rest to feature values to their labels. Remapping and reseting index leads to complete data cleaning. Most of the data cleaning was made sure that the values of the data are understandable. Then, we seperated the Label & features as required to train the model. Continued to split the datasets into training and testing sets so that we have data that the model has not seen  to evaluate its performance. Last step before training the model is to standardize the data for model to work efficiently.


## DESCRIBED EXPLORATION :
### Model 1
1st Model: Support Vector Machine algorithm, C-Support Vector Classification.
- Support vector machines (SVMs) is a set of supervised learning methods used for classification, regression and outliers detection. SVM is a powerful supervised algorithm that works best on smaller datasets but on complex ones. Support Vector Machine can be used for both regression and classification tasks, but generally, they work best in classification problems and keep on being the go-to method for a high-performing algorithm with a little tuning. 
- It took almost 4 hours for model to get trained.

### Model 2
2nd ml model: k-nearest neighbors algorithm, k-nearest neighbors vote.
- The KNN algorithm uses a majority voting mechanism. It collects data from a training data set, and uses this data later to make predictions for new records. K Nearest Neighbour is a simple algorithm that stores all the available cases and classifies the new data or case based on a similarity measure.
- It took almost 2 hours for model to get trained.

### Model 3
3rd model: ensemble-based methods for classification, Gradient Boosting Classifier.
- The module sklearn.ensemble provides methods for both classification and regression via gradient boosted decision trees. This algorithm builds an addictive model in a forward stage-wise fashion; it allows for the optimization of arbitrary differentiable loss functions. K Nearest Neighbour is a simple algorithm that stores all the available cases and classifies the new data or case based on a similarity measure
- It took almost 40 minutes for model to get trained.

### Model 4
4th model: Naive Bayes algorithm, Gaussian Naive Bayes Classifier.
- Naive Bayes is a probabilistic machine learning algorithm that can be used in several classification tasks. Typical applications of Naive Bayes are classification of documents, filtering spam, prediction and so on. Any modifications in the value of one feature do not directly impact the value of any other feature of the algorithm. The main advantage of the Naïve Bayes algorithm is that it is a simple yet powerful algorithm.
- It took almost 10 mins for model to get trained.

## NHAMC Dataset (National Hospital Ambulatory Medical Care Survey)
The National Hospital Ambulatory Medical Care Survey (NHAMCS) is a program conducted by the U.S. Centers for Disease Control and Prevention (CDC) to collect data on the use of hospital emergency and outpatient services in the United States. It provides valuable insights into healthcare utilization, patient demographics, and the reasons for medical visits, aiding in healthcare policy and planning.

## Preprocessing of NHAMCS Dataset
This dataset was the most difficult to process. The original dataset had 955 features, which we narrowed down to 32. Since there are over 3000 diagnosis in the data, after encoding we ended up with a features dataset with 3447 columns. We then continued by selecting the relevant columns for the target and features, split the data into training and testing sets, and standardized the data for training.

Model 1
### 1st Model: Support Vector Machine algorithm, C-Support Vector Classification.
- As mentioned in the C.O.P.D. section.

### Model 2
2nd ml model: k-nearest neighbors algorithm, k-nearest neighbors vote.
- As mentioned in the C.O.P.D. section.

### Model 3
3rd model: ensemble-based methods for classification, Gradient Boosting Classifier.
- As mentioned in the C.O.P.D. section.

Model 4
4th Model: Deep Learning, Neural Network
- In TensorFlow, a Sequential Neural Network model is a linear stack of layers where data flows sequentially from one layer to the next, making it easy to create feedforward neural networks for tasks like classification by simply adding layers in order. Each layer in a Sequential model can consist of various types of neurons, such as densely connected (fully connected) layers, dropout layers, etc., allowing for flexible model designs.


# Model Evaluation
We used testing data that was separated using Train_Test_Split to make predictions. We then compared the predictions to their true-truths to calculate the accuracy, precision, and recall through the classification report. 


# Model Summary:
It was great learning to train each model. Each model gave minor differences but we are looking for higher recall. As we are not wanting to risk not capturing the set of people who might be at the risk of COPD (Chronic Obstructive Pulmonary Disease) with our model. For predicting COPD we choose the Guassian Naive Bayes model and tried optimizing by dropping a number of features which improves the model but in minimal. The final scores were Precision: 27%, Recall: 56% and Accuracy: 84%. For predicting Dementia we used the neural network model without dropout layers or regularizers. The final scores were Precision: 26%, Recall: 17% and Accuracy: 98%.

# Discussion
From all the Models mentioned for predicting COPD, Model 4 Naive Bayes algorithm, Gaussian Naive Bayes Classifier took just 10mins to get trained and also gave higher recall with 57%. Considering a medical point of view, higher recall is more important than precision. Higher recall ensures to capture everyone and not leave behind the ones who might have copd. It is better to count the ones even with minimum risk, even if the final test reports are negative/positive. It is better for a model to predict than not predicting. On the other hand, for predicting Dementia, the Neural Network model before optimizing performed the best. Although the Gradient Boosting model with resampled data had the highest recall, in practice it was too sensitive. Optimizing the neural network model by adding dropout layers and regulizers significantly increased the precision score, but also damaged the recall score severly, making it unusuable. 

# Postmortem
Working on New modules was interesting. Data cleaning was bit challenging as to make sure not to drop the data that might be important at the later stage. It is important to read the documentation provided with the data to understand it well. By doing so, this ensures the data is interpreted correctly ask the right questions to be used for making predictions. Future models could be extended by making the different features as labels such as Diabetes, Asthma and so on.


## Collaborators
Emily Blackstein </br>
Harshita Panchal </br>
Andy Vu </br>
Amar Sen

## Resources
- [2021 BRFSS Survey Data and Documentation](https://www.cdc.gov/brfss/annual_data/annual_2021.html)
- [NHAMCS Datasets and Documentation](https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm)
