INSERT INTO customers VALUES
(1,'Arun','Chennai'),
(2,'Priya','Coimbatore'),
(3,'Karthik','Madurai');

INSERT INTO products VALUES
(101,'Laptop','Electronics',50000),
(102,'Mouse','Electronics',500),
(103,'Keyboard','Electronics',1000),
(104,'Headphones','Electronics',2000);

INSERT INTO orders VALUES
(1001,1,'2026-01-10'),
(1002,2,'2026-01-15'),
(1003,3,'2026-02-05');

INSERT INTO order_items VALUES
(1,1001,101,1),
(2,1001,102,2),
(3,1002,103,1),
(4,1003,104,2),
(5,1003,102,3);
