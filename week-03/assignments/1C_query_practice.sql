select products.ProductID, products.ProductName, products.UnitPrice
from northwind.products
order by UnitPrice asc;

select products.ProductID, products.ProductName, products.UnitsInStock
from northwind.products
where UnitsInStock >= 100 
order by UnitsInStock desc;

select products.ProductID, products.ProductName, products.UnitsInStock, products.UnitPrice
from northwind.products
where UnitsInStock >= 100 
order by UnitPrice desc, ProductName asc;

select count(distinct CustomerID) as CustomerCount
from northwind.orders;
 
select orders.ShipCountry, count(distinct CustomerID) as CustomerCount
from northwind.orders
group by orders.ShipCountry
order by CustomerCount desc;

select ProductID, ProductName, UnitsInStock, UnitsOnOrder
from northwind.products
where UnitsInStock <= 25 or UnitsOnOrder > 1;

select title, count(distinct EmployeeID) as EmployeeCount
from northwind.employees
group by Title;

-- What employees have a monthly salary that is between $2000 and $2500? Write a query that orders them by job title.
select EmployeeID, FirstName, LastName, Salary
from northwind.employees
where Salary > 2000 and Salary < 2500; 