# CodeAlpha Data Analytics Projects

This repository contains two projects completed as part of the **CodeAlpha Data Analytics Internship**. The projects demonstrate practical skills in **web scraping, exploratory data analysis (EDA), and data visualization** using Python.

---

# Project 1: Book Data Web Scraping using BeautifulSoup

## Project Overview
This project demonstrates web scraping using the **BeautifulSoup** library to extract book information from the **Books to Scrape** website. It collects details such as book titles, prices, availability, and ratings, and stores the extracted data in a structured CSV file for further data analysis, visualization, and machine learning tasks.

## Features
- Extracts book titles
- Extracts book prices
- Extracts availability status
- Extracts book ratings
- Stores the scraped data in CSV format

## Technologies Used
- Python
- BeautifulSoup
- Requests
- Pandas
- CSV

## Output
The scraped dataset is organized in CSV format and can be used for exploratory data analysis (EDA), data visualization, and other data science applications.

## Conclusion
This project successfully demonstrates web scraping using the BeautifulSoup library to extract book information from the Books to Scrape website. The collected data is stored in a structured CSV format and can be used for exploratory data analysis (EDA), data visualization, and machine learning applications. The project highlights the complete process of collecting, organizing, and preparing real-world data for further analysis while providing practical experience with Python, BeautifulSoup, Requests, and data handling techniques.

---

# Project 2: Amazon Review Sentiment Analysis

## Project Overview
This project analyzes Amazon customer reviews to understand customer sentiment using **Exploratory Data Analysis (EDA)** and **data visualization** techniques. It explores the dataset to identify trends, patterns, and insights through statistical analysis and visual representations, providing a strong foundation for text preprocessing and future machine learning-based sentiment analysis.

## Dataset
**Dataset:** Amazon Reviews (`train.csv`)

### Columns
- `label` – Sentiment (1 = Negative, 2 = Positive)
- `title` – Review title
- `text` – Review content

## Objectives
- Analyze customer review data.
- Perform Exploratory Data Analysis (EDA).
- Visualize the sentiment distribution and review length.
- Identify trends, patterns, and potential data issues.
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
The following visualizations were created using **Matplotlib** and **Seaborn**:
- Sentiment Distribution
- Review Length Distribution

## Insights
- The sentiment distribution shows the number of positive and negative reviews.
- The review length distribution helps understand how detailed customer reviews are.
- These visualizations reveal useful patterns in the dataset and support data-driven decision-making before model development.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn

## Project Structure

```text
amazon_review_
│── README.md
│── eda.py
│── visualization.py
│── train.csv
│── .gitignore
```

## Conclusion
This project successfully demonstrates exploratory data analysis and visualization of Amazon customer reviews. The insights gained from the analysis provide a clear understanding of customer sentiment and review characteristics, forming a strong foundation for text preprocessing and sentiment classification using machine learning.

---

# Overall Conclusion

These projects collectively demonstrate essential data analytics skills, including **web scraping, data collection, exploratory data analysis, and data visualization**. Using Python libraries such as **BeautifulSoup, Requests, Pandas, Matplotlib, and Seaborn**, the projects showcase the complete workflow from collecting raw data to extracting meaningful insights. Together, they provide a strong foundation for advanced analytics and machine learning applications while highlighting practical problem-solving and data-driven decision-making.


