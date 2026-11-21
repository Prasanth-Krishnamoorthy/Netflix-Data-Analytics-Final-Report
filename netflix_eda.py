"""
Netflix dataset EDA starter script
Run locally after installing: pandas matplotlib openpyxl

Usage:
  python analysis/netflix_eda.py
Set NETFLIX_FILE below to your local workbook path.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

NETFLIX_FILE = Path("Netflix.xlsx")  # Change to your Excel workbook path
OUTPUT_DIR = Path("charts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_excel(NETFLIX_FILE)
df.columns = [str(c).strip().lower() for c in df.columns]
df = df.replace("Missing", pd.NA)

def save_bar(series, title, xlabel, ylabel, filename, rotate=0):
    plt.figure(figsize=(9, 5))
    series.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotate, ha="right" if rotate else "center")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=160)
    plt.show()
    plt.close()

type_counts = df["type"].value_counts()
save_bar(type_counts, "Netflix Movies vs TV Shows", "Content Type", "Titles", "01_content_type.png")

release_counts = df["release_year"].dropna().astype(int).value_counts().sort_index()
plt.figure(figsize=(10, 5))
release_counts.plot(kind="line")
plt.title("Netflix Titles by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Titles")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "02_release_trend.png", dpi=160)
plt.show()
plt.close()

rating_counts = df["rating"].dropna().value_counts().head(15)
save_bar(rating_counts, "Top Content Ratings", "Rating", "Titles", "03_ratings.png", rotate=40)

countries = df["country"].dropna().astype(str).str.split(",").explode().str.strip()
countries = countries[countries.ne("") & countries.ne("Missing")]
country_counts = countries.value_counts().head(10)
save_bar(country_counts, "Top 10 Countries", "Country", "Title-country entries", "04_top_countries.png", rotate=40)

genres = df["listed_in"].dropna().astype(str).str.split(",").explode().str.strip()
genres = genres[genres.ne("") & genres.ne("Missing")]
genre_counts = genres.value_counts().head(10)
save_bar(genre_counts, "Top 10 Genres / Categories", "Category", "Title-category entries", "05_top_genres.png", rotate=40)

print("=" * 48)
print("NETFLIX EDA - SUMMARY")
print("=" * 48)
print(f"Total titles: {len(df):,}")
print(f"Movies: {type_counts.get('Movie', 0):,}")
print(f"TV Shows: {type_counts.get('TV Show', 0):,}")
if not df["rating"].dropna().empty:
    print("Most common rating:", df["rating"].mode().iloc[0])
if not release_counts.empty:
    print("Peak release year:", release_counts.idxmax())
if not country_counts.empty:
    print("Top country:", country_counts.index[0])
if not genre_counts.empty:
    print("Top genre/category:", genre_counts.index[0])
print("Charts saved in:", OUTPUT_DIR.resolve())
