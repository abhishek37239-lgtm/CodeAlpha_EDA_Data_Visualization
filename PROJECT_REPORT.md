# Project Report: Sales Data EDA and Visualization

**Internship:** CodeAlpha – Data Analytics
**Tasks:** Task 2 (Exploratory Data Analysis) and Task 3 (Data Visualization)
**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, VS Code

---

## 1. Introduction
This project explores a sales dataset to understand product performance, customer ratings and sales trends. It covers two internship tasks: Exploratory Data Analysis (Task 2) and Data Visualization (Task 3). No machine learning is used.

## 2. Dataset Description
- **File:** `sales_data.csv` (a sample dataset created for learning)
- **Size:** 61 rows and 9 columns (60 unique orders after cleaning)
- **Columns:** order_id, date, product, category, region, units_sold, unit_price, revenue, rating
- **Products:** Laptop, Smartphone, Tablet, Smartwatch, Headphones, Keyboard
- **Period:** January to December 2025

## 3. Methodology
1. Loaded the CSV file with Pandas.
2. Inspected the first 5 rows, shape, column names and data types.
3. Generated a statistical summary with `describe()`.
4. Checked for missing values and duplicate rows.
5. Cleaned the data: removed 1 duplicate row and filled 1 missing rating with the median.
6. Converted the date column to a date type and created a month column.
7. Calculated total revenue, total units sold and average rating.
8. Grouped the data by product, month, region and category.
9. Detected anomalies with the IQR (interquartile range) method.
10. Created 6 charts and saved them in the `charts` folder.

## 4. Key Results
| Metric | Value |
|--------|-------|
| Total revenue | Rs. 22,044,500 |
| Total units sold | 1,530 |
| Average rating | 4.00 / 5 |
| Rows after cleaning | 60 |

### Product Performance
| Product | Revenue (Rs.) | Units Sold | Avg Rating |
|---------|---------------|------------|------------|
| Laptop | 12,100,000 | 220 | 4.68 |
| Tablet | 4,248,000 | 236 | 4.18 |
| Smartphone | 2,882,000 | 131 | 4.19 |
| Smartwatch | 1,470,000 | 210 | 4.07 |
| Keyboard | 732,000 | 488 | 3.53 |
| Headphones | 612,500 | 245 | 3.74 |

## 5. Visualizations
| Chart | Type | File |
|-------|------|------|
| Revenue by Product | Bar chart | `charts/revenue_by_product.png` |
| Units Sold by Product | Bar chart | `charts/units_sold_by_product.png` |
| Average Rating by Product | Bar chart | `charts/average_rating_by_product.png` |
| Revenue Distribution | Histogram | `charts/revenue_distribution.png` |
| Units Sold vs Rating | Scatter plot | `charts/units_vs_rating.png` |
| Revenue Trend Over Time | Line chart | `charts/revenue_trend.png` |

## 6. Insights
1. Laptops earn the most revenue (about 55% of the total).
2. Keyboards sell the most units (488) but earn little revenue because of their low price.
3. Laptops have the best average rating (4.68); Keyboards have the lowest (3.53).
4. Units sold and rating are almost unrelated (correlation -0.11).
5. Electronics generate about 94% of total revenue; Accessories about 6%.
6. January 2025 is the best month (Rs. 7,167,000) and September the weakest (Rs. 693,000).
7. One bulk order of 120 laptops (Rs. 6,600,000) in January inflates both the January total and the South region.
8. The IQR method flagged 5 high-revenue orders, all Laptops.
9. The revenue distribution is right-skewed: most orders are small and a few are very large.

## 7. Data Quality Notes
- 1 duplicate row was found and removed.
- 1 missing rating was found and filled with the median rating.
- The dataset is synthetic. It is meant for demonstrating the analysis workflow, not for making real business decisions.

## 8. Conclusion
The project completes Task 2 by loading, inspecting, cleaning and analysing the data and reporting key metrics, trends and anomalies. It completes Task 3 by presenting the findings in six clear charts. The main finding is that revenue depends on high-priced products like Laptops, while low-priced products like Keyboards drive sales volume but not revenue.

## 9. How to Run
```bash
pip install -r requirements.txt
python analysis.py
```