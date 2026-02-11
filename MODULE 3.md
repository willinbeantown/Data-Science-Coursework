# Module 3

## Data and Challanges in Managing Data

- A Key part of Data Science is **Data Transformation**

`Raw Data` --> `Information` --> `Knowledge`

- Almost everything in the universe can be seen as raw data.

- Volume of data create continues to grow exponentially over time, which can cause problems.

- Database Managment - Collecting raw data and organizaing its storage.


## Database Concepts

- A database is an **integrated collection** of logically related records or objects.

- A **Relational Database** serves a key purpose where data is orgized in buckets that contain other buckets, or data.

`Database` --> `File` --> `Record` --> `Field` --> `Character`

or 

`Table` --> `Record` --> `Field` --> `Value`

- **THESE ARE NEW TERMS!!**

### DBMS - **Database Management Systems

- A software tool for databases, Access, SQL, Oracle.

**DBMS Functions**

  - Create Databases

  - Query the Data

  - Maintenance

  - API

**DBMS Benefits**

  - Integration

  - Can reduce redundancy

  - Democratizes data

  - Manages data ingegrity

## Structure Query Language

- Developed under the name `SEQUEL` by IBM.

- This course will use MySQL (thru Anaconda)

### SQL Introduction

- Used to maintain, access and manage databases

- The schema, or relationship, between elements is a key thing to know about a database.

- A **Table** is a database object, and a **Record** is a Tuple, and the # of tuples is the **Cardinality**.

- The **Fields** are the *attributes* of a Table, and the # of attributes is called the **Degree**.

- In a Table the *index* is called the **Primary Key**, aka **Surrogate key** (surrogate in that it is a made up number)

- If a database uses something like SSN as a *Primary Key* it is known as a **Natural key** because it exists outside the database.

- A **Relational Database** is where there are relations between tables where a **Foriegn Key** in a table references the *Primary Key* in another table.

### SQL Usage

- The **Data Definition Language 'DDL'** is used to created databases, tables, and delete them.

An example to `create a database`

> CREATE DATABASE myschool;

> CREATE SCHEMA myschool;  <!--SCHEMA and DATABASE are interchangeable -->

- **GOOD PRACTICE** in SQL **reserved words** are ALL CAPITAL, and user defined terms are all lowercase.

An example to `create a table`

- First, design a table by defining what needs to be captured.

> CREATE TABLE 'myschool', 'employee' (
>   'id' INT NOT NULL, 
>   'name' VARCHAR(45) NOT NULL, 
>   'salary' VARCHAR(45) NOTNULL, 
>   PRIMARY KEY('id)
> );

- In SQL Databases are not *deleted* they are **DROPPED**.

### Syntax and Pitfalls

- Unlike Python, SQL calls need to end in a **semicolon, ;**

- "database", "table" == `database.table`

- SQL uses tuples, so between the `( )` should be **commas**

- SQL does need memory allocation to be considered, so `VARCHAR` should be set to an appropriate length to not take up too much space.

- In MySQL Workbench be aware of the diference between **`** and **'**.

## HELPFUL SQL CALLS

> CREATE DATABASE db_name;  <!--Can use SCHEMA-->

> DROP db_name;  <!--Drop, or 'delete', a DB-->

> INSERT INTO db_name.table_name (x, y, x);  <!--Don't forget the semicolon!!-->

- To comment out a line use **--**, to comment multiple lines use **/*..*/**