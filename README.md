# Pandas_InfoAnalysis


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
Missing values:
OrderID         0
CustomerName    0
Product         0
Category        0
Quantity        0
Price           0
OrderDate       0
Shipped         0
Country         0
TotalPrice      0
dtype: int64

=== REVENUE BY CATEGORY ===
Category
Electronics    3146.0
Furniture      1993.0
Stationery      434.0
Name: TotalPrice, dtype: float64

=== TOP 5 ORDERS ===
   CustomerName        Product  TotalPrice
0    John Smith         Laptop      1200.0
6   Emily Davis  Standing Desk       450.0
7    James Park        Monitor       440.0
11    Raj Patel   File Cabinet       360.0
2      Ali Khan   Office Chair       300.0

=== SHIPPING STATUS ===
         count     sum
Shipped               
No          13  1879.0
Yes         27  3694.0

=== TOP 10 COUNTRIES BY REVENUE ===
Country
USA            1345.0
South Korea     586.0
UK              518.0
India           360.0
Canada          328.0
UAE             325.0
China           280.0
Germany         210.0
Mexico          160.0
Egypt           160.0
Name: TotalPrice, dtype: float64