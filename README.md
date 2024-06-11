# Task: Development of New API Features

**Customer company:** Acme Corp - A fast-growing startup developing innovative supply chain management software.

**Team:** The Acme Corp Back-End team consists of 8 people responsible for developing and supporting the server-side of the web application and API.

## Description of the Task

The Senior Back-End Developer at Acme Corp is looking for an intern to help with the development of new API features. As part of your test assignment, you will need to complete the following tasks:

### Tasks:

1. **Develop an API method to create a new product:**
   - Define a data model for a product, including fields such as name, description, price, category, and so on.
   - Create an API method (`POST /products`) that accepts a JSON object with product data and saves it to the database.
   - Return a JSON object with information about the created product.

2. **Develop an API method to get a list of products:**
   - Create an API method (`GET /products`) that returns a list of all products from the database.
   - Add the ability to filter products by category (use the `GET /products?category=` parameter).
   - Add the ability to sort products by price (use the `GET /products?sort=price` parameter).

3. **Develop an API method to get information about a specific product:**
   - Create an API method (`GET /products/:id`) that takes a product ID and returns information about it.
   - Handle a 404 error if the product with the specified ID is not found.

### Requirements:
- Experience in developing with Python or Java (of your choice)
- Knowledge of OOP
- Knowledge of SQL
- Experience working with APIs
- Ability to write clean and readable code

### Evaluation Criteria:
- Correctness of task completion
- Code quality
- Code readability
- API documentation
- Effective use of technologies
- Creative approach

### Possible Questions and Answers:

1. **Tell us about your experience in developing with Python/Java.**
   - I have experience in developing with Python/Java (specify language) for (specify number) years.
   - I have worked on such projects as (list projects).
   - I am familiar with the basic principles of OOP, such as encapsulation, inheritance, and polymorphism.

2. **How will you implement the API method to create a new product?**
   - I will create a data model for the product using appropriate libraries (ORM for Python/Java).
   - I will define an API method (`POST /products`) using the Flask/Spring Boot framework.
   - I will accept a JSON object with product data, deserialize it into a data model object, and save it to the database.
   - I will return a JSON object with information about the created product.

3. **How will you implement the API method to get a list of products?**
   - I will create an API method (`GET /products`) using the Flask/Spring Boot framework.
   - I will use an SQL query to get a list of products from the database.
   - I will process the query results and serialize them into a JSON object.
   - I will add the ability to filter products by category, using a WHERE clause in the SQL query.
   - I will add the ability to sort products by price, using an ORDER BY clause in the SQL query.

4. **How will you test your API?**
   - I will use Unit tests to test individual components of the API.
   - I will use Integration tests to test the interaction of different API methods.
   - I will use End-to-end tests to test the overall functionality of the API.

5. **How will you document your API?**
   - I will use OpenAPI Specification (Swagger) to generate API documentation.
   - The documentation will include descriptions of API methods, request and response formats, and error codes.

## Screenshots

![Screenshot 1](screenshots/screenshot1.png)
![Screenshot 2](screenshots/screenshot2.png)

## Video Description of Work

[Video link](https://drive.google.com/drive/folders/1BR_qLzhz5P1JVFfpLAKOqZHvO-NuY4hR)

## Commit Formatting

When making commits, use informative headers that describe the essence of the changes, for example:
- "Task description added"
- "Screenshots of completed work have been added"
- "Added link to video description of work"

## Result

After completing the assignment and posting the results on GitHub, provide a link to the repository for evaluation.
