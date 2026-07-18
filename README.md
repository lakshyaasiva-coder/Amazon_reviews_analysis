# Amazon Review Sentiment Analysis

## Project Overview
This project analyzes Amazon customer reviews to understand customer sentiment. Exploratory Data Analysis (EDA) and data visualization techniques are used to identify patterns and insights from the review dataset.

## Dataset
- Dataset: Amazon Reviews (`train.csv`)
- Columns:
  - `label` – Sentiment (1 = Negative, 2 = Positive)
  - `title` – Review title
  - `text` – Review content

## Objectives
- Analyze customer review data.
- Perform Exploratory Data Analysis (EDA).
- Visualize the sentiment distribution and review length.
- Prepare the dataset for future machine learning tasks.

## Questions Before Analysis
1. What is the distribution of positive and negative reviews?
2. Are most reviews short or long?
3. Is the dataset balanced?
4. Are there any missing or inconsistent values?
5. What insights can be obtained before model training?

## Exploratory Data Analysis (EDA)
- Loaded the dataset.
- Examined the dataset structure.
- Checked column names and data types.
- Analyzed sentiment distribution.
- Measured review lengths.

## Data Visualization
The following visualizations were created using Matplotlib and Seaborn:
- Sentiment Distribution
- Review Length Distribution

## Insights
- The sentiment distribution shows the number of positive and negative reviews.
- The review length distribution helps understand how detailed customer reviews are.
- These insights help prepare the dataset for preprocessing and sentiment analysis.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn

## Project Structure
```

```text
amazon_review_
│── README.md
│── eda.py
│── visualization.py
│── train.csv
│── .gitignore
```