### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
Postgres is an open-source, object-relational database management system (DBMS). 
It is a system that allows users to efficiently store, manage, and retrieve data.

- What is the difference between SQL and PostgreSQL?
SQL is a language used to interact with databases and PostgreSQL is a data management system.

- In `psql`, how do you connect to a database?
psql -U your_username -d your_database_name -h your_host -p your_port


- What is the difference between `HAVING` and `WHERE`?
WHERE can filter rows based on one or more conditions using comparison operators. 
HAVING is used in SELECT statements with GROUP BY to filter the results of aggregate functions based on a condition.

- What is the difference between an `INNER` and `OUTER` join?
An INNER JOIN returns only the rows that have matching values in both tables based on the specified join condition.
An OUTER JOIN returns all the rows from one table, even if there are no matches in the other table based on the join condition.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
A LEFT OUTER JOIN returns all the rows from the left table (the table mentioned before the join keyword) and the matching rows from the right table (the table mentioned after the join keyword).
A RIGHT OUTER JOIN returns all the rows from the right table and the matching rows from the left table.

- What is an ORM? What do they do?
ORM stands for "Object-Relational Mapping." It is a programming technique and architectural pattern used to convert data between incompatible systems—particularly, between object-oriented programming languages and relational databases.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
 AJAX is used for making asynchronous HTTP requests from the client-side, enabling dynamic interactions with the server without page reloads. On the other hand, requests is used on the server-side to perform HTTP requests and handle responses, making it suitable for tasks that require server-side processing and interaction with external APIs or services.

- What is CSRF? What is the purpose of the CSRF token?
CSRF stands for Cross-Site Request Forgery, which is a type of security vulnerability that allows an attacker to trick a user's web browser into making unintended and potentially harmful actions on a web application on which the user is authenticated. This occurs when an authorized user unknowingly submits a request that they did not intend to make, leading to unauthorized actions being performed on their behalf.

- What is the purpose of `form.hidden_tag()`?
The purpose of form.hidden_tag() is to include the CSRF token in the HTML form rendered by Flask, ensuring that the form submission is secure and protected against CSRF attacks.
