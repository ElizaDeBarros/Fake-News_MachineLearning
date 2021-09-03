# FinalProj_group4

As a group we decided to work on classifying Real News vs Fake News with data sourced from Kaggle.  
We did a couple of different Machine Learning models and settled on one that utilized the NLTK library,  SKLEARN and Python.  
We put the data through 4 models (Logistic Regression, Naive-Bayes, Decision Tree and Passive Aggressive Classifiers) all of which were at 94% accuracy or higher.

Shared Database setup with Postgresql.
Flask app reads in the tables on the database using classes.  There are two data webpages that flask jsonifies the tables to.
The app.js files makes a promise to the json URLs to create a dropdownlist of the different Headlines for the user.
When the webpage loads and on a user selection, 
the json takes the selected value and finds that in the jsonified data to get the method predictions.

The web page was written with html5, bootstrap and CSS. 
The page has a list of news that the user can select and verify what the different machine learning models are predicting.
A javascript code will get the results of the machine learning models and place them on the htlm. D3 is being used to parse data.