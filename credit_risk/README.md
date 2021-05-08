# Credit Risk

In this project I built and used several different machine learning models to predict credit risk using data typically seen in peer-to-peer lending services.

# Resampling

In the resampling notebook I fit the data to various models including a logistic regression model, Naive Random Oversampler and SMOTE to oversample the data, Cluster Centroids to undersample the data, and an over- and under-sampling combination utilizing SMOTEENN. The results of these models are summarized as follows: All the models except for the combination of over and under sampling and the logistic regression had the same balanced accuracy score of 0.9936781215845847. This was greater than the balanced accuracy score of the combination of over and under sampling and logistic regression. All the models had the same recall score of 0.99. All of the models except for the logistic regression had the same geometric mean score of 0.99, which was greater than the logistic regression.

# Ensemble Learning

In the Ensemble Learning notebook, I fit the data to two different models to predict loan risk. These models were the balanced random forest classifier and the random forest classifier. The results are summarized as follows: The Random Forest Classifier had the better balanced accuracy score of 1.0. Both models had a 1.0 recall. Both models had geometric mean scores of 1.0. The top three features are loan_status, total_rec_prncp, last_pymnt_amnt.
