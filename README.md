# CodeAlpha_EDA_Data_Visualization

Exploratory Data Analysis (EDA) and Data Visualization on a sales dataset, built for the **CodeAlpha Data Analytics Internship** (Task 2 and Task 3).

## Objective
Explore a sales dataset, clean it, calculate key business metrics, find trends and anomalies, and present the results with clear charts.

## Tasks Covered
| Task | Description | Where in the project |
|------|-------------|----------------------|
| Task 2 | Exploratory Data Analysis | Terminal output of `analysis.py` |
| Task 3 | Data Visualization | 6 charts saved in `charts/` |

## Technologies
Python 3, Pandas, NumPy, Matplotlib, Seaborn

## Project Structure
```
CodeAlpha_EDA_Data_Visualization/
├── sales_data.csv        # Sample sales dataset (61 rows, 9 columns)
├── analysis.py           # Main EDA + visualization script
├── requirements.txt      # Required Python libraries
├── README.md             # Project documentation
├── PROJECT_REPORT.md     # Detailed project report
└── charts/               # Auto-generated charts (PNG)
```

## Dataset Columns
`order_id`, `date`, `product`, `category`, `region`, `units_sold`, `unit_price`, `revenue`, `rating`

The dataset is a realistic sample created for learning. It intentionally includes one duplicate row, one missing rating and one very large bulk order, so the data-cleaning and anomaly steps can be demonstrated.

## EDA Steps
- Load CSV, show first 5 rows, shape, column names, data types
- Statistical summary, missing values, duplicate rows
- Data cleaning (remove duplicates, fill missing ratings with median)
- Total revenue, total units sold, average rating
- Revenue, units sold and average rating by product
- Monthly trend, region and category analysis
- Correlation between units sold and rating
- Anomaly detection using the IQR method

## Visualizations
1. Revenue by Product – bar chart
2. Units Sold by Product – bar chart
3. Average Rating by Product – bar chart
4. Revenue Distribution – histogram
5. Units Sold vs Rating – scatter plot
6. Monthly Revenue Trend – line chart

## How to Run
```bash
pip install -r requirements.txt
python analysis.py
```
Charts are saved automatically in the `charts/` folder and the analysis is printed in the terminal.

## Key Insights
- Laptops generate about 55% of total revenue.
- Keyboards sell the most units but earn very little revenue (low price).
- Laptops have the best average rating; Keyboards the lowest.
- A single bulk laptop order in January 2025 distorts monthly and regional totals.
- Units sold and rating show almost no relationship.

## Author
Data Analytics Intern, CodeAlpha