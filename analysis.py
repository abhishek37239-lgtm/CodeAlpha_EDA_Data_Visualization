"""
CodeAlpha Data Analytics Internship
Task 2: Exploratory Data Analysis (EDA)
Task 3: Data Visualization

Project : CodeAlpha_EDA_Data_Visualization
Dataset : sales_data.csv
Libraries: pandas, numpy, matplotlib, seaborn
"""

# ----------------------------------------------------------
# 1. IMPORT LIBRARIES
# ----------------------------------------------------------
import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")          # Save charts to files without opening windows
import matplotlib.pyplot as plt
import seaborn as sns

# Make the charts look clean and professional
sns.set_theme(style="whitegrid")

# Always work relative to this file, so the script runs from any folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "sales_data.csv")
CHARTS_DIR = os.path.join(BASE_DIR, "charts")

# Create the charts folder if it does not exist
os.makedirs(CHARTS_DIR, exist_ok=True)


def print_heading(title):
    """Print a neat section heading in the terminal."""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ----------------------------------------------------------
# 2. LOAD THE DATASET
# ----------------------------------------------------------
print_heading("TASK 2: EXPLORATORY DATA ANALYSIS (EDA)")

if not os.path.exists(CSV_PATH):
    raise FileNotFoundError(
        "sales_data.csv not found. Keep it in the same folder as analysis.py"
    )

df = pd.read_csv(CSV_PATH)
print("Dataset loaded successfully.")

# ----------------------------------------------------------
# 3. BASIC DATASET INFORMATION
# ----------------------------------------------------------
print_heading("1. FIRST 5 ROWS")
print(df.head())

print_heading("2. DATASET SHAPE")
print(f"Number of rows    : {df.shape[0]}")
print(f"Number of columns : {df.shape[1]}")

print_heading("3. COLUMN NAMES")
print(list(df.columns))

print_heading("4. DATA TYPES")
print(df.dtypes)

print_heading("5. STATISTICAL SUMMARY")
print(df.describe().round(2))

# ----------------------------------------------------------
# 4. DATA QUALITY CHECKS
# ----------------------------------------------------------
print_heading("6. MISSING VALUES")
missing = df.isnull().sum()
print(missing)

print_heading("7. DUPLICATE ROWS")
duplicate_count = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_count}")

# ----------------------------------------------------------
# 5. DATA CLEANING
# ----------------------------------------------------------
print_heading("8. DATA CLEANING")

# Remove duplicate rows
df = df.drop_duplicates()
print(f"Duplicate rows removed: {duplicate_count}")

# Fill missing ratings with the median rating (safe for beginners)
missing_ratings = df["rating"].isnull().sum()
if missing_ratings > 0:
    df["rating"] = df["rating"].fillna(df["rating"].median())
print(f"Missing ratings filled with median: {missing_ratings}")

# Convert the date column from text to a real date type
df["date"] = pd.to_datetime(df["date"])

# Create a month column to study monthly trends
df["month"] = df["date"].dt.to_period("M").astype(str)

print(f"Rows after cleaning: {len(df)}")

# ----------------------------------------------------------
# 6. KEY BUSINESS METRICS
# ----------------------------------------------------------
print_heading("9. KEY METRICS")
total_revenue = df["revenue"].sum()
total_units = df["units_sold"].sum()
average_rating = df["rating"].mean()

print(f"Total Revenue    : Rs. {total_revenue:,.0f}")
print(f"Total Units Sold : {total_units:,}")
print(f"Average Rating   : {average_rating:.2f} / 5")

# ----------------------------------------------------------
# 7. PRODUCT-WISE ANALYSIS
# ----------------------------------------------------------
revenue_by_product = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
units_by_product = df.groupby("product")["units_sold"].sum().sort_values(ascending=False)
rating_by_product = df.groupby("product")["rating"].mean().sort_values(ascending=False)

print_heading("10. REVENUE BY PRODUCT")
print(revenue_by_product.apply(lambda x: f"Rs. {x:,.0f}"))

print_heading("11. UNITS SOLD BY PRODUCT")
print(units_by_product)

print_heading("12. AVERAGE RATING BY PRODUCT")
print(rating_by_product.round(2))

# ----------------------------------------------------------
# 8. TRENDS, PATTERNS AND ANOMALIES
# ----------------------------------------------------------
print_heading("13. TRENDS, PATTERNS AND ANOMALIES")

# Monthly revenue
monthly_revenue = df.groupby("month")["revenue"].sum()
best_month = monthly_revenue.idxmax()
worst_month = monthly_revenue.idxmin()
print(f"Best month by revenue  : {best_month} (Rs. {monthly_revenue.max():,.0f})")
print(f"Lowest month by revenue: {worst_month} (Rs. {monthly_revenue.min():,.0f})")

# Revenue by region and category
revenue_by_region = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
revenue_by_category = df.groupby("category")["revenue"].sum().sort_values(ascending=False)
print("\nRevenue by region:")
print(revenue_by_region.apply(lambda x: f"Rs. {x:,.0f}"))
print("\nRevenue by category:")
print(revenue_by_category.apply(lambda x: f"Rs. {x:,.0f}"))

# Correlation between units sold and rating
correlation = df["units_sold"].corr(df["rating"])
print(f"\nCorrelation between units sold and rating: {correlation:.2f}")

# Anomaly detection using the IQR method (simple statistics, no ML)
q1 = df["revenue"].quantile(0.25)
q3 = df["revenue"].quantile(0.75)
iqr = q3 - q1
upper_limit = q3 + 1.5 * iqr
outliers = df[df["revenue"] > upper_limit]

print(f"\nOutlier limit (Q3 + 1.5*IQR): Rs. {upper_limit:,.0f}")
print(f"High-revenue anomalies found: {len(outliers)}")
if len(outliers) > 0:
    print(outliers[["order_id", "date", "product", "units_sold", "revenue"]]
          .to_string(index=False))

# Share of the top product
top_product = revenue_by_product.idxmax()
top_share = revenue_by_product.max() / total_revenue * 100

# ----------------------------------------------------------
# 9. DATA VISUALIZATION
# ----------------------------------------------------------
print_heading("TASK 3: DATA VISUALIZATION")


def save_chart(filename):
    """Tidy the layout, save the chart as PNG and close the figure."""
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, filename), dpi=150)
    plt.close()
    print(f"Saved: charts/{filename}")


# Chart 1: Revenue by Product (Bar Chart)
plt.figure(figsize=(9, 5))
sns.barplot(x=revenue_by_product.index, y=revenue_by_product.values,
            hue=revenue_by_product.index, palette="Blues_r", legend=False)
plt.title("Revenue by Product", fontsize=14, fontweight="bold")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
save_chart("revenue_by_product.png")

# Chart 2: Units Sold by Product (Bar Chart)
plt.figure(figsize=(9, 5))
sns.barplot(x=units_by_product.index, y=units_by_product.values,
            hue=units_by_product.index, palette="Greens_r", legend=False)
plt.title("Units Sold by Product", fontsize=14, fontweight="bold")
plt.xlabel("Product")
plt.ylabel("Units Sold")
save_chart("units_sold_by_product.png")

# Chart 3: Average Rating by Product (Bar Chart)
plt.figure(figsize=(9, 5))
sns.barplot(x=rating_by_product.index, y=rating_by_product.values,
            hue=rating_by_product.index, palette="Oranges_r", legend=False)
plt.title("Average Rating by Product", fontsize=14, fontweight="bold")
plt.xlabel("Product")
plt.ylabel("Average Rating (out of 5)")
plt.ylim(0, 5)
save_chart("average_rating_by_product.png")

# Chart 4: Revenue Distribution (Histogram)
plt.figure(figsize=(9, 5))
sns.histplot(df["revenue"], bins=15, kde=True, color="steelblue")
plt.title("Revenue Distribution", fontsize=14, fontweight="bold")
plt.xlabel("Revenue per Order (Rs.)")
plt.ylabel("Number of Orders")
save_chart("revenue_distribution.png")

# Chart 5: Units Sold vs Rating (Scatter Plot)
plt.figure(figsize=(9, 5))
sns.scatterplot(data=df, x="units_sold", y="rating", hue="product",
                s=80, alpha=0.8)
plt.title("Units Sold vs Rating", fontsize=14, fontweight="bold")
plt.xlabel("Units Sold")
plt.ylabel("Rating")
plt.legend(title="Product", bbox_to_anchor=(1.02, 1), loc="upper left")
save_chart("units_vs_rating.png")

# Chart 6: Revenue Trend Over Time (Line Chart)
plt.figure(figsize=(10, 5))
plt.plot(monthly_revenue.index, monthly_revenue.values,
         marker="o", color="crimson", linewidth=2)
plt.title("Monthly Revenue Trend", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=45)
save_chart("revenue_trend.png")

# ----------------------------------------------------------
# 10. FINAL INSIGHTS
# ----------------------------------------------------------
print_heading("FINAL INSIGHTS")
print(f"1. Total revenue is Rs. {total_revenue:,.0f} from {total_units:,} units sold.")
print(f"2. '{top_product}' earns the highest revenue "
      f"({top_share:.1f}% of total revenue).")
print(f"3. '{units_by_product.idxmax()}' sells the most units "
      f"({units_by_product.max():,}), while '{revenue_by_product.idxmin()}' "
      f"earns the least revenue.")
print(f"4. '{rating_by_product.idxmax()}' has the best average rating "
      f"({rating_by_product.max():.2f}); '{rating_by_product.idxmin()}' has the "
      f"lowest ({rating_by_product.min():.2f}).")
print(f"5. {best_month} is the best month and {worst_month} the weakest "
      f"month for revenue.")
print(f"6. '{revenue_by_region.idxmax()}' is the top region and "
      f"'{revenue_by_category.idxmax()}' is the top category.")
print(f"7. Units sold and rating have a correlation of {correlation:.2f}.")
print(f"8. {len(outliers)} high-revenue anomaly order(s) found; they strongly "
      f"affect totals and monthly trends.")
print("9. Data quality: duplicates were removed and missing ratings were "
      "filled with the median.")
print("\nAnalysis complete. All 6 charts are saved in the 'charts' folder.")