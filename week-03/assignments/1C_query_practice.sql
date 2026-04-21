USE northwind;
SELECT products.ProductID, products.ProductName, products.UnitPrice
FROM northwind.products ORDER BY UnitPrice asc;

USE northwind;
SELECT *
FROM products.UnitPrice
WHERE UnitsInStock >= 7.50

USE northwind;
SELECT *
fROM northwind.products
ORDER BY UnitPrice desc, ProductName asc;

