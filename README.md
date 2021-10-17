# Fake News Machine Learning Project

This repository contains a code that classifies Real News vs Fake News with data sourced from Kaggle. It utilizes four Machine Learning models (Logistic Regression, Naive-Bayes, Decision Tree and Passive Aggressive Classifiers) all of which were at 94% accuracy or higher. The code is written in Python and uses NLTK and SKLEARN libraries.  

The Database was setup with Postgresql.
A Flask app reads in the tables on the database using classes.  There are two data webpages that flask jsonifies the tables to.
The app.js files makes a promise to the json URLs to create a dropdownlist of the different Headlines for the user.
When the webpage loads and on a user selection, the json takes the selected value and finds that in the jsonified data to get the method predictions.

The web page was written with html5, bootstrap and CSS. 
The page has a list of news that the user can select and verify what the different machine learning models are predicting.
A javascript code will get the results of the machine learning models and place them on the htlm. D3 is being used to parse data.
