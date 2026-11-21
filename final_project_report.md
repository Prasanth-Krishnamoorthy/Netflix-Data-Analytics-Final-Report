# Netflix Movies & TV Shows — Final Project Report

## 1. Problem Statement
A large streaming catalog is difficult to understand using raw tabular data alone. The purpose of this project is to analyze the Netflix Movies and TV Shows dataset and communicate useful patterns in content type, release year, ratings, countries, and genre/category distribution through data analysis and an interactive dashboard.

## 2. Dataset Information
- Dataset name: Netflix Movies and TV Shows
- Source: Kaggle (https://www.kaggle.com/datasets/shivamb/netflix-shows)
- Dataset size used: 8,807 records and 12 columns
- Attributes include title, content type, director, cast, country, date added, release year, rating, duration, genre/category, and description.

## 3. Data Cleaning and Preprocessing
The cleaning process reviewed missing values, duplicate records, data types, formatting, and consistency. Missing categorical details such as director, cast, country, and rating were represented as `Unknown` where suitable. Date and descriptive fields were not populated with fabricated values. Date and year fields were checked for appropriate data types, text formatting was standardized, and duration was reviewed because movies use minutes while TV shows use seasons.

## 4. Exploratory Data Analysis
The analysis covered:
- Content type distribution
- Release-year counts
- Rating counts
- Country title counts
- Genre/category counts

### Summary
| Metric | Result |
|---|---:|
| Total titles | 8,807 |
| Movies | 6,131 |
| TV Shows | 2,676 |
| Movie share | 69.6% |
| TV Show share | 30.4% |
| Peak release year | 2018 |
| Most common rating | TV-MA |
| Leading country | United States |
| Most frequent genre/category | International Movies |

Five charts were generated: content type, release trend, ratings, top countries, and top genres.

## 5. Dashboard
The Power BI dashboard presents KPI cards and charts for ratings, genres/categories, country distribution, Movies versus TV Shows, and release-year trends. The screenshot is included in the project `dashboard` folder. The Power BI editable file is not included in this package.

## 6. Key Business Insights
1. Movies account for about 69.6% of the titles, so movies form the larger share of this dataset.
2. The release-year distribution peaks in 2018. This is a pattern in the dataset and should not be interpreted as Netflix adding the most titles in 2018.
3. TV-MA is the most common rating in the dataset.
4. The United States leads the country analysis by title count.
5. International Movies is the most frequent category in the genre analysis.

Country and genre values can contain multiple comma-separated entries. A title can therefore be counted under more than one country or genre.

## 7. Tools Used
Excel, Python, Pandas, Matplotlib, Google Colab, Power BI.

## 8. Conclusion
The project turns the Netflix catalog into a more understandable summary through cleaning, exploratory analysis, and dashboard visualization. The results highlight the catalog's movie-heavy mix, rating distribution, release-year pattern, geographic representation, and category distribution.
