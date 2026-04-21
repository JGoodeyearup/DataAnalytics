SELECT products.ProductID, products.ProductName, products.UnitPrice
FROM northwind.products ORDER BY UnitPrice asc;

SELECT products.ProductID, products.ProductName, products.UnitPrice
FROM northwind.products
WHERE UnitPrice <= 7.50;

SELECT products.ProductID, products.ProductName, products.UnitsinStock, products.UnitsOnOrder
FROM northwind.products
WHERE UnitsInStock = 0 and UnitsOnOrder > 1; 

-- The products table describes the category it sells using the CategoryID primary key. To find the way products describe the type use these queries, and if all the seafood they offer.
SELECT products.ProductID, products.ProductName, categories.CategoryID, categories.CategoryName
From northwind.products, northwind.categories
WHERE categories.CategoryID = 8;

-- Same way we found out how to find what type was being represented in category, we're going to do the same thing but for the supplier.
SELECT products.ProductID, products.ProductName, suppliers.SupplierID, CompanyName
FROM northwind.products, northwind.suppliers
WHERE suppliers.SupplierID = 4;

-- There are 9 employees and only 1 of them have the manager title. Down below is how I found the info.
SELECT employees.EmployeeID, employees.LastName, employees.FirstName, employees.Title
FROM northwind.employees