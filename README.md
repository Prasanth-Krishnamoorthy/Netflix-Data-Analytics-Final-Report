# Netflix Movies & TV Shows — Data Analytics Project

## Project Overview
This project analyzes the Netflix Movies and TV Shows catalog to identify content distribution patterns, release-year trends, rating patterns, country representation, and genre/category trends. It combines data cleaning, exploratory data analysis (EDA), and an interactive Power BI dashboard.

## Problem Statement
Streaming platforms manage large catalogs of movies and TV shows. Exploring this catalog can help stakeholders understand the balance of content types, content-rating distribution, release-year patterns, country representation, and frequently listed genres. This project uses the Netflix titles dataset to summarize these patterns and communicate them through visualizations and a dashboard.

## Dataset Information
- **Dataset:** Netflix Movies and TV Shows
- **Source:** Kaggle — https://www.kaggle.com/datasets/shivamb/netflix-shows
- **Rows:** 8,807 titles (loaded dataset)
- **Columns:** 12
- **Fields:** `show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, `description

## Project Workflow
1. Data cleaning and preprocessing
2. Exploratory Data Analysis (EDA)
3. Visual analysis of content types, release years, ratings, countries, and genres
4. Power BI dashboard design and KPI presentation
5. Business insights and conclusions

## Data Cleaning & Preprocessing
The cleaning workflow reviewed:
- Missing values in fields such as director, cast, country, rating, date added, duration, and description.
- Duplicate records.
- Data type consistency (for example, `release_year` as numeric and `date_added` as a date where possible).
- Whitespace and formatting inconsistencies.
- Duration field consistency (movie duration in minutes versus TV show seasons).

Missing categorical details were represented as `Unknown` where appropriate rather than inventing values. Dates or descriptive fields with unavailable information were left blank or documented. Cleaning decisions should be checked against the final cleaned workbook before reuse.

## Exploratory Data Analysis
The analysis produced five visualizations:
1. Movies vs. TV Shows
2. Content release-year trend
3. Rating distribution
4. Top 10 countries
5. Top 10 genres/categories

### Key Findings (from the executed EDA)
- Total titles: **8,807**
- Movies: **6,131** (about **69.6%**)
- TV Shows: **2,676** (about **30.4%**)
- Peak release year in the catalog: **2018**
- Most common rating: **TV-MA**
- Top country by title count: **United States**
- Most frequent genre/category: **International Movies**

Country and genre fields may contain multiple comma-separated values per title; their analysis can count a title under multiple categories.

## Dashboard
The Power BI dashboard includes KPI cards and visualizations for:
- Ratings by title count
- Genre/category by title count
- Country distribution map
- Movies vs. TV Shows
- Release-year trend

Dashboard screenshot: [`dashboard/netflix_dashboard.png`](dashboard/netflix_dashboard.png)

> Note: This repository includes the screenshot of the dashboard. The editable Power BI `.pbix` file is not included unless separately added.

## Business Insights
- **Catalog mix:** Movies make up roughly 69.6% of records, while TV Shows account for roughly 30.4%. The catalog is movie-heavy.
- **Release-year pattern:** 2018 is the highest-count release year in this dataset. Release-year counts describe titles represented in this dataset, not Netflix's historical acquisitions in that year.
- **Audience rating:** TV-MA is the most common rating, suggesting mature-rated titles are well represented.
- **Geographic representation:** The United States is the leading country by title count in the country analysis. Multi-country entries can be counted for more than one country.
- **Genre/category mix:** International Movies is the most frequent category in the EDA genre breakdown. Multi-category titles can contribute to more than one category.

## Tools & Technologies
- Microsoft Excel
- Python
- Pandas
- Matplotlib
- Google Colab
- Microsoft Power BI

## Project Structure
```text
Netflix_Data_Analytics_Final_Project/
├── README.md
├── dashboard/
│   └── netflix_dashboard.png
├── analysis/
│   └── netflix_eda.py
└── reports/
    └── final_project_report.md
```

## How to Run the EDA Script
1. Install dependencies:
   ```bash
   pip install pandas matplotlib openpyxl
   ```
2. Place the Netflix Excel workbook in the project folder (or update the path in `analysis/netflix_eda.py`).
3. Run:
   ```bash
   python analysis/netflix_eda.py
   ```
4. The script saves chart images in `charts/` and prints the main summary.

## Conclusion
This project demonstrates a data analytics workflow from data cleaning and exploration to dashboard storytelling. It summarizes the Netflix catalog and presents patterns in content type, release years, ratings, country, and genre through visual analytics.

## Internship Task
**Task 4:** Final Project — Data Analytics  
**Project:** Netflix Movies & TV Shows Analysis
