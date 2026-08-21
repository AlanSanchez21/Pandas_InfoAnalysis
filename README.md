# Pandas InfoAnalysis
A Python data analysis project using pandas and matplotlib to explore and visualize a sample order dataset of 40 international transactions across three product categories.

## Necessary Installations
```bash
pip3 install pandas matplotlib
```
## Dataset
`order.csv` contains around 40 orders with the following columns: OrderID, CustomerName, Product, Category, Quantity, Price, OrderDate, Shipped, Country.

Another derived column `TotalPrice` is calculated at runtime. (Quantity * Price)

## Data Analysis 

### Dataset Overview
This dataset contains 40 orders across 10 columns. The average order total is $139.33, but the standard deviation of $206.57 is significantly higher than the mean, which indicates me that the data is right-skewed, however a small number of high-value orders are pulling the average up. The median order (50th percentile) is only $72.50, which is a more accurate picture of a typical order.

=== DATASET OVERVIEW ===
Shape: (40, 10)
OrderID           int64
CustomerName        str
Product             str
Category            str
Quantity          int64
Price           float64
OrderDate           str
Shipped             str
Country             str
TotalPrice      float64

           OrderID    Quantity        Price   TotalPrice
count    40.000000   40.000000    40.000000    40.000000
mean   1020.500000    5.450000   106.457500   139.325000
std      11.690452   15.903475   201.091854   206.567228
min    1001.000000    1.000000     0.800000    15.000000
25%    1010.750000    1.000000    18.000000    34.250000
50%    1020.500000    1.000000    43.500000    72.500000
75%    1030.250000    2.250000   112.500000   136.250000
max    1040.000000  100.000000  1200.000000  1200.000000

### Revenue
Electronics leads the total revenue with $3,146, followed by Furniture at $1,993 and Stationery at $434. 
Despite Stationery having the highest number of individual items sold, its low unit prices result in the lowest total revenue. This is a classic example of volume not equating to value.

=== REVENUE BY CATEGORY ===
Category
Electronics    3146.0
Furniture      1993.0
Stationery      434.0

### Top 5 Orders & Top 10 Countries by Revenue
#### Top 5 orders: 
The top order is John Smith's Laptop at $1,200 , a single item that represents 21% of Electronics revenue alone. 
Four of the top five orders are Furniture or Electronics, confirming that high-ticket categories drive disproportionate revenue. 

| === TOP 5 ORDERS === |
| CustomerName | Product | TotalPrice |
0    John Smith         Laptop      1200.0 |
6   Emily Davis  Standing Desk       450.0 |
7    James Park        Monitor       440.0 |
11    Raj Patel   File Cabinet       360.0 |
2      Ali Khan   Office Chair       300.0 |

This pattern shows that a small number of orders account for a large share of total sales.

#### Top 10 Countries By Revenue:
The USA leads at $1,345, mostly high-value Laptop order. 
South Korea ranks second at $586 despite only appearing twice in the dataset, which means its average order value is among the highest.

| === TOP 10 COUNTRIES BY REVENUE === |
| Country |
| USA | 1345.0 |
| South Korea | 586.0 |
| UK | 518.0 |
| India | 360.0 |
| Canada | 328.0 |
| UAE | 325.0 |
| China | 280.0 |
| Germany | 210.0 |
| Mexico | 160.0 |
| Egypt | 160.0 |

This suggests there is "market concentration risk" this happens when revenue from certain countries depend heavily on one or two large orders rather than a broad customer base. Increasing the risk that if one of them leave revenue will decrease drastically.

### Shipping Status
27 of 40 orders have been shipped, fulfilled revenue of $3,694. The missing 13 orders represent a potential revenue risk.

| Shipping Status| Count | Revenue (USD) |
|----------------|-------|---------------|
| No | 13 | 1879.0 |
| Yes | 27 | 3694.0 |

## File Structure
| File | Description |
|------|-------------|
| `main.py` | Main analysis script |
| `orders.csv` | Sample order dataset (40 rows) |
| `notebook.ipynb` | Jupyter notebook version |