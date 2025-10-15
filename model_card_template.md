# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

RandomForestClassifier trained on U.S. census data to predict whether an individual's income exceeds $50K/year (>50K) or not (<=50K). Categorical features are one-hot encoded, and the target variable is binarized.

## Intended Use

Designed for demonstration of a scalable ML pipeline. Not intended for real-world financial, legal, or employment decisions.

## Training Data

80% of the census dataset was used for training, including features like age, workclass, education, marital-status, occupation, race, sex, native-country, hours-per-week, and others.

## Evaluation Data

20% of the census dataset held out for testing. Metrics were pcomputed overall and per categorical slice. 

## Metrics
Overall test performance: 
    - Precision: 0.742
    - Recall: 0.6384
    - F1 Score: 0.686

Full per-slice metrics are available in 'slice_output.txt'

## Ethical Considerations

The model uses demographic features including race, sex, and native country. Predictions may reflect biases in the training data. Avoid using this model for high-stakes decisions.

## Caveats and Recommendations

- Some slices have small sample sizes, leading to extreme metrics (0.0 or 1.0).
- Missing or unknown values are encoded as '?'.
- May not generalized to populations outside the dataset.
- Regular evaluations and fairness audits are recommended if applied to new data. 