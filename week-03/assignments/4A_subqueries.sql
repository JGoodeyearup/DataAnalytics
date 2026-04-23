-- What is the product name(s) of the most expensive products?
select p.ProductID, p.ProductName, p.UnitPrice
from northwind.products as p
where p.UnitPrice = (
	select max(UnitPrice)
    from northwind.products
group by p.ProductID, p.ProductName, p.UnitPrice
);

-- What is the product name(s) and categories of the least expensive products?
select p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
from northwind.products as p
join northwind.categories as c
	on p.CategoryID = c.CategoryID
where UnitPrice = (
	select min(UnitPrice)
    from northwind.products
group by p.ProductName, c.CategoryName
);

-- What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?
select o.OrderID, o.ShipName, o.ShipAddress
from northwind.orders as o
join northwind.shippers as sh
on o.ShipVia = sh.ShipperID
where sh.ShipperID = 3
group by o.OrderID, o.ShipName, o.ShipAddress;

-- What are the order ids of the orders that included "Sasquatch Ale"?
select od.OrderID, p.ProductName
from northwind.`order details` as od
join northwind.products as p
on od.ProductID = p.ProductID
where ProductName = "Sasquatch Ale";

-- What is the name of the employee that sold order 10266?
select e.EmployeeID, e.FirstName, e.LastName, o.OrderID
from northwind.employees as e,
	northwind.orders as o
where OrderID = 10266;

-- What is the name of the customer that bought order 10266?
select c.CustomerID, c.ContactName, o.OrderID
from northwind.customers as c,
	northwind.orders as o
where o.OrderID = 10266;