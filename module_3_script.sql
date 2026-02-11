-- create db
CREATE SCHEMA mystore;

-- create table in new db
CREATE TABLE mystore.inventory(
  item_no INT NOT NULL, 
  item_name VARCHAR(100) NOT NULL, 
  unit_price INT NOT NULL, 
  inventory INT NOT NULL, 
  PRIMARY KEY (item_no)
);

-- populate table
INSERT INTO mystore.inventory(item_no, item_name, unit_price, inventory) VALUES (2321, "Dell Laptop", 399.99, 100);