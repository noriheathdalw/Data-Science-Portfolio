# Ethical Life-Event Inference from Retail Transactions

This project explores whether changes in shopping behavior can signal life-stage transitions using public retail transaction data.

## Business problem
Retailers often want to understand how customer behavior changes over time. This project asks whether transaction patterns can be used to detect life-event-like behavior shifts in a privacy-aware way.

## Dataset
Public retail transaction data from the UCI Online Retail dataset.

## Objective
Build a predictive model that identifies customers whose shopping behavior is likely to change in the near future.

## Methods
- Data cleaning and transaction filtering
- Feature engineering at the customer level
- Logistic regression baseline model
- Comparison with a stronger classification model
- Model evaluation using AUC, precision, recall, and lift

## Key outputs
- Customer behavior feature set
- Predictive model for behavior-shift risk
- Business interpretation of the model
- Ethics and privacy discussion

## Why this matters
This project shows how retail analytics can support customer understanding, while also highlighting the risks of inferring sensitive personal information.

## Tech stack
Python, pandas, scikit-learn, matplotlib / seaborn, Jupyter Notebook

## Ethical note
This project is for educational and portfolio purposes only. It does not attempt to identify real individuals or infer sensitive traits in production.

## How to run
1. Install dependencies.
2. Download the dataset.
3. Run the notebook or pipeline script.
4. Review outputs in the `reports/` folder.
