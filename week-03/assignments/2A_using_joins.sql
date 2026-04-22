-- Create a single query to list the product id, product name, unit price and category name of all products. Order by category name and within that, by product name.
select products.ProductID, products.ProductName, products.UnitPrice, categories.CategoryName
from northwind.categories, northwind.products
order by categories.CategoryName, products.ProductName;

/*
Create a single query to list the product id, product name, unit price and supplier
name of all products that cost more than $75. Order by product name
*/
select products.ProductID, products.ProductName, products.UnitPrice, suppliers.CompanyName
from northwind.products, northwind.suppliers
where products.UnitPrice > 75
order by products.ProductName asc;

/*
Create a single query to list the product id, product name, unit price, category name,
and supplier name of every product. Order by product name
*/
select products.ProductID, products.ProductName, products.UnitPrice, categories.CategoryName, suppliers.CompanyName
from northwind.products, northwind.categories, northwind.suppliers
order by products.ProductName;

/*
Create a single query to list the order id, ship name, ship address, and shipping
company name of every order that shipped to Germany. Assign the shipping company
name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
shipped to
*/
SELECT sh.CompanyName AS Shipper, count(distinct o.ShipName) as ShipCount
FROM northwind.Orders AS o
JOIN northwind.Shippers AS sh
    ON o.ShipVia = sh.ShipperID
WHERE o.ShipCountry = 'Germany'
group by sh.CompanyName
ORDER BY sh.CompanyName;

-- Create a single query to list the order id, order date, ship name, ship address of all orders that included Sasquatch Ale
select o.OrderID, o.OrderDate, o.ShipName, o.ShipAddress
from northwind.orders as o
join northwind.`order details` as od
	on o.OrderID = od.OrderID
join northwind.products as p
	on od.ProductID = p.ProductID
where p.ProductName = "Sasquatch Ale";