# SQL GENERATOR
Webiste build with Reflex that generate a SQL Query from reading a CSV or Excel File

You got a CSV or Excel file with some data that you wanna insert/update/delete from your database. The webisite build in [Reflex](https://reflex.dev) read you CSV or Excel file and depends on you selection, generate the SQL Query to insert in the database.

### Example
We got this CSV or Excel file and we want to insert in the Fruits table:
| Item         | Price     | Stock      |
|--------------|-----------|------------|
| Juicy Apples | 1.99      | 7          |
| Bananas      | 1.89      | 5234       |
| Apples       | 1.79      | 524        |
| Orange       | 1.69      | 34         |
      ...           ...          ...

In the website you choose the INSERT option and returns X inserts of X rows of data that you have in the file:
```
INSERT INTO FRUITS (Item, Price, Stock) VALUES ('Juicy Apples', 1.99, 7)
INSERT INTO FRUITS (Item, Price, Stock) VALUES ('Bananas', 1.89, 5234)
INSERT INTO FRUITS (Item, Price, Stock) VALUES ('Apples', 1.79, 524)
INSERT INTO FRUITS (Item, Price, Stock) VALUES ('Orange', 1.69, 34)
```
