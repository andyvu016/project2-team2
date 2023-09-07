# Health Risk Analysis: C.O.P.D and Dementia

# Name of the Project - "CHECK FIRST"

# Overview:
Focus of this project is to use Machine Learning and Deep Learning models to determine the risk of common health diseases. We choose the COPD and Dimentia as the disease to analyse the risk in human.

# Installation:
1. Install the latest verion of Python.
2. Install the latest version of Anaconda here.
3. Installing Anaconda includes the Pandas package.
4. To install the scikit-learn packages, run the following command in your terminal.
5. Installing TensorFlow includes the Keras package.


* HYPOTHESIS :
# Risk Analysis with "CHECK FIRST"
"Check First" is an app created specifically to analyse the health-related risk behaviors, chronic health conditions, and use of preventive services. We are  analyzing risk for COPD(Chronic Obstructive Pulmonary Disease) and Dimentia.


# EXPLAINED DISEASE_1
### COPD (Chronic Obstructive Pulmonary Disease)
Chronic obstructive pulmonary disease (COPD) is a lung disease and makes it hard to breathe. Two main forms of COPD:Chronic bronchitis, which involves a long-term cough with mucus and Emphysema, which involves damage to the lungs over time. Most people with COPD have a combination of both conditions.

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

# Explained DISEASE_2
Dementia is a general term for loss of memory, language, problem-solving and other thinking abilities that are severe enough to interfere with daily life. Alzheimer's is the most common cause of dementia.

### Causes 
Depression.
Medication side effects.
Excess use of alcohol.
Thyroid problems.
Vitamin deficiencies.

### Symptons
Short-term memory.
Keeping track of a purse or wallet.
Paying bills.
Planning and preparing meals.
Remembering appointments.
Traveling out of the neighborhood.

# Datasets Used:
1. For COPD , we used BRFSS Dataset 
2. For Dimentia, we used NHAMCS Analysis



# DATA CLEANUP & MODEL TRAINING :

### BRFSS Dataset (Behavioral Risk Factor Surveillance System)
The Behavioral Risk Factor Surveillance System (BRFSS) is a health survey that collects data on behavioral risk factors. It is administered by the Centers for Disease Control and Prevention and conducted in all 50 states and US territories by participating individual state health departments. It gives communities, states, and federal agencies and information they need to plan public health programmes and other activities at local, state, and national levels.

### Preprocessing of BRFSS Dataset
I preprocessed and cleaned the BRFSS Dataset. From 304 unique variables, I hand-picked 19 variables that relates to lifestyle factors of a person that can be contributed to being at risk with any form of COPD (Chronic Obstructive Pulmonary Disease). The data was from BRFSS dataset that was collected from CDC. Data preprocessing was done using pandas. We selected the relevant columns and dropped the rest to feature values to their labels. Remapping and reseting index leads to complete data cleaning. Most of the data cleaning was made sure that the values of the data are understandable. Then, we seperated the Label & features as required to train the model. Continued to split the datasets into training and testing sets so that we have data that the model has not seen  to evaluate its performance. Last step before training the model is to standardize the data for model to work efficiently.


# DESCRIBED EXPLORATION :

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

# Model Evaluation
We did Use Testing Data that was separated using Train_Test_Split to make predictions. Compared the predictions to their true-truths to calculate the accuracy, precision and recall through the classification report. 

# Model Summary :
It was great learning to train each model. Each model gave minor difference but we are looking for higher recall. As we are not wanting to risk the set of people who might be at the risk of COPD (Chronic Obstructive Pulmonary Disease). We choose the 4th model and tried optimizing by dropping number of features which improves the model but in minimal.

# Discussion
From all the Models mentioned above, Model 4 Naive Bayes algorithm, Gaussian Naive Bayes Classifier took just 10mins to get trained and also gave higher recall with 57%. Considering a medical point of view, higher recall is more important than precision. Higher recall ensures to capture everyone and not leave behind the ones who might have copd. It is better to count the ones even with minimum risk, even if the final test reports are negative/positive. It is better for a model to predict than not predicting.

Model 1
### 1st Model: Support Vector Machine algorithm, C-Support Vector Classification.
- Support vector machines (SVMs) is a set of supervised learning methods used for classification, regression and outliers detection. SVM is a powerful supervised algorithm that works best on smaller datasets but on complex ones. Support Vector Machine can be used for both regression and classification tasks, but generally, they work best in classification problems and keep on being the go-to method for a high-performing algorithm with a little tuning.
- 
### Model 2
2nd ml model: k-nearest neighbors algorithm, k-nearest neighbors vote.
- The KNN algorithm uses a majority voting mechanism. It collects data from a training data set, and uses this data later to make predictions for new records. K Nearest Neighbour is a simple algorithm that stores all the available cases and classifies the new data or case based on a similarity measure.

### Model 3
3rd model: ensemble-based methods for classification, Gradient Boosting Classifier.
- The module sklearn.ensemble provides methods for both classification and regression via gradient boosted decision trees. This algorithm builds an addictive model in a forward stage-wise fashion; it allows for the optimization of arbitrary differentiable loss functions. K Nearest Neighbour is a simple algorithm that stores all the available cases and classifies the new data or case based on a similarity measure

Model 4
4th Model : Deep Learning , Neural Network




# Postmortem
Working on New modules was interesting. Data cleaning was bit challenging as to make sure not to drop the data that might be important at the later stage. Future model would be extended by different features as labels like Diabetes, Asthma and so on.


## Collaborators
Emily Blackstein </br>
Harshita Panchal </br>
Andy Vu </br>
Amar Sen

## Resources
- [2021 BRFSS Survey Data and Documentation](https://www.cdc.gov/brfss/annual_data/annual_2021.html)
- [NHAMCS Datasets and Documentation](https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm)
