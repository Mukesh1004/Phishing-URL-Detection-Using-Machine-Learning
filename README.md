# Phishing URL Detection Using Machine Learning

## Problem
Classify URLs as phishing or legitimate using structural URL features. This corresponds to Problem 02 in the supplied capstone PDF.

## Dataset
This package contains a **synthetic educational dataset** (`dataset.csv`) with 3,000 records. It was created for a prototype and should not be represented as a real-world external dataset.

## Features
URL, URLLength, SubdomainCount, SpecialCharCount, DigitRatio, DomainLength, HTTPS, HasIP, URLDepth, HyphenCount, DotCount, Label.

## Label
- `0` = Phishing
- `1` = Legitimate

## Model
Decision Tree Classifier (`max_depth=8`) is used for the Streamlit prototype. Logistic Regression is also evaluated in the notebook.

## How to run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Notebook
Open `phishing_url_detection.ipynb` to reproduce data loading, cleaning, EDA, training and evaluation.

## Important limitation
The synthetic dataset is highly structured, which can produce unusually high validation scores. These results demonstrate the workflow but are not evidence of production-level phishing detection accuracy.
