/*
Write a query to find the price of the cheapest item that Northwind sells. Then write a
second query to find the name of the product that has that price
*/
select p.ProductID, p.ProductName, p.UnitPrice
from northwind.products as p 
where p.UnitPrice = (
	select min(UnitPrice)
    from northwind.products
    );

/*
Write a query to find the average price of all items that Northwind sells.
(Bonus: Once you have written a working query, try asking Claude or ChatGPT for help
using the ROUND function to round the average price to the nearest cent.)
*/
select avg(UnitPrice)
from northwind.products;

-- Chat using round function
select round(avg(UnitPrice), 2) as AvgUnitPrice
from northwind.products;

/*
Write a query to find the price of the most expensive item that Northwind sells. Then
write a second query to find the name of the product with that price, plus the name of
the supplier for that product.
*/
select p.ProductName, p.UnitPrice, su.CompanyName
from northwind.products as p, northwind.suppliers as su
where p.UnitPrice = (
	select max(UnitPrice)
    from northwind.products
    );

/*
Write a query to find total monthly payroll (the sum of all the employees’ monthly
salaries)
*/
select round(sum(Salary), 2) as AllEmployeeMonthly
from northwind.employees;

/*
Write a query to identify the highest salary and the lowest salary amounts which any
employee makes. (Just the amounts, not the specific employees!)
*/
select min(Salary) as MinEmployeeSal, max(Salary) as MaxEmployeeSal
from northwind.employees;

/*
Write a query to find the name and supplier ID of each supplier and the number of
items they supply. Hint: Join is your friend here
*/
select su.SupplierID, su.CompanyName, p.UnitsInStock
from northwind.suppliers as su
join northwind.products as p
	on su.SupplierID = p.SupplierID
where p.UnitsInStock in (
	select p.UnitsInStock
    from northwind.products
    group by UnitsInStock
    having count(*) = 1
    );
    
/*
Write a query to find the list of all category names and the average price for items in
each category.
*/

SELECT c.CategoryName, AVG(p.UnitPrice) AS AvgUnitPrice
FROM northwind.categories AS c
JOIN northwind.products AS p
  ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;

/*
Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
is the name of each supplier and the number of items they supply.
*/
SELECT s.CompanyName AS SupplierName, COUNT(p.ProductID) AS ItemCount
FROM northwind.suppliers AS s
JOIN northwind.products AS p
    ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

/*
Write a query to list products currently in inventory by the product id, product name,
and inventory value (calculated by multiplying unit price by the number of units on
hand). Sort the results in descending order by value. If two or more have the same
value, order by product name. If a product is not in stock, leave it off the list.
*/
select 
	products.ProductID,
    products.ProductName,
    products.UnitPrice * products.UnitsInStock as InventoryValue
from 
	northwind.products
where UnitsInStock > 0
order by InventoryValue desc, ProductName asc;
