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
dtype: object

           OrderID    Quantity        Price   TotalPrice
count    40.000000   40.000000    40.000000    40.000000
mean   1020.500000    5.450000   106.457500   139.325000
std      11.690452   15.903475   201.091854   206.567228
min    1001.000000    1.000000     0.800000    15.000000
25%    1010.750000    1.000000    18.000000    34.250000
50%    1020.500000    1.000000    43.500000    72.500000
75%    1030.250000    2.250000   112.500000   136.250000
max    1040.000000  100.000000  1200.000000  1200.000000