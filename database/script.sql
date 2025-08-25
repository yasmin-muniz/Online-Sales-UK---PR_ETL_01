-- drop table Orders;

CREATE TABLE Orders (
    InvoiceNo VARCHAR(20) NOT NULL,
    StockCode VARCHAR(20) NOT NULL,
    Description VARCHAR(255),
    Quantity INT,
    InvoiceDate DATETIME,
    UnitPrice DECIMAL(10,2),
    CustomerID INT,
    Country VARCHAR(100),
	TotalPrice DECIMAL(10,2)
);


CREATE LOGIN PR_ETL_01
WITH PASSWORD = 'ETL123';
 
CREATE USER PR_ETL_01 FOR LOGIN PR_ETL_01; 

ALTER ROLE db_datareader ADD MEMBER PR_ETL_01;
ALTER ROLE db_datawriter ADD MEMBER PR_ETL_01;



select * from Orders (nolock)

select count(*) from Orders (nolock)

 