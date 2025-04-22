# STT_Lab9

CS 203: Software Tools & Techniques for AI

IIT Gandhinagar

Sem-II - 2024-25

________________________________________________________________

Lab Assignment 9 


Total: 10 Marks
Submission deadline: Sunday, 13/04/2025 11:59:59 PM

Submission guidelines:
Implement the code in the jupyter notebook and share it during submission.
Add all screenshots of the results in a pdf file and share.
The deadline will not be extended at any cost.
Late submissions will be penalized 20% per day.

Note: Submitting this assignment solution confirms that you will follow the IITGN's honor code. We shall strictly penalize the submissions containing plagiarized text/code.
________________________________________________________________

Objective

This assignment will introduce students to CI/CD for Machine Learning using MLRun, a powerful orchestration and automation framework for deploying ML pipelines. Students will learn to create a function, deploy it using Kubernetes/Nuclio, and set up a simple retraining pipeline. 
Dataset Preparation

Get the breast cancer dataset using “from sklearn.datasets import load_breast_cancer”.


Installation guide
Features to Implement
Create a mlrun project:
Use mlrun new_project. [10%]

Create the following Python script:

Data_prep.py: This fetches data using sklearn.datasets import load_breast_cancer. (Add screenshot of the code)[10 %]

Trainer.py: Split the data into train test (10% test data). Train a model using the training data. Use Random forest classifier. Wrap the model with apply_mlrun from mlrun.frameworks.sklearn. (Add screenshot of the code)[10 %]

serving.py: Create a model class that will inherit from mlrun.serving.V2ModelServer, enabling automatic support for model lifecycle methods like load() and predict(). (Add screenshot of the code)[10 %]

workflow.py: Create a Python script that defines an MLRun pipeline using the @dsl.pipeline decorator. It should include the following steps:
Data Ingestion(Add screenshot of the code) [3 %]

Model Training: Experiment with different hyperparamters(n_estimators: [10, 100, 200], max_depth=[2, 5, 10]). Keep max accuracy as selector. (Add screenshot of the code)[4 %]

Model Deployment: Deploy the model into the base kubernetes image(mlrun/mlrun) using mlrun.deploy_function (Add screenshot of the code)[3 %]

Run the workflow using project.run:

Add the screenshot of the workflow graph [10 %]

Add the screenshot of the Data_prep artifact and take the screenshot of the dataframe. [10 %]

Add the screenshot of the confusion-matrix artifact of train.py [10 %]

Add the screenshot of feature importance artifact. [10 %]

Code Quality:
Maintain clean, modular, and readable code. [10 %]







*****Best of Luck*****
