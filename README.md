**Customer company:** Acme Corp - a fast-growing startup developing innovative supply chain management software.

## Description of the Task

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


## Overview of API's

Tools: Django, DRF, PostgreSQL, JWT Authentication, Gunicorn, Swagger, Docker, Render, Postman

Applications: Supply (to manage products), Account (custom user account with jwt authentication and email activation)

Main API endpoints:
admin, supply, account

Authentication:
JWT tokens

Containerization: docker, render.yml

Documentation: Swagger

Deploy of backend and database: Render server

## Screenshots
Project structuere
<div style="text-align: left;">
    <img src="/screenshots/Screenshot2024-06-12at17.22.41.png" alt="Screenshot 1" width="200"/>
</div>


### Admin panel
![Screenshot 3](/screenshots/Screenshot2024-06-12at16.58.35.png)
![Screenshot 2](/screenshots/Screenshot2024-06-12at16.58.39.png)
![Screenshot 2](/screenshots/Screenshot2024-06-12at16.58.24.png)
![Screenshot 2](/screenshots/Screenshot2024-06-12at16.56.56.png)
![Screenshot 2](/screenshots/Screenshot2024-06-12at16.56.42.png)

### Endpoints
![Screenshot 2](/screenshots/Screenshot2024-06-12at14.59.04.png)
![Screenshot 2](/screenshots/Screenshot2024-06-12at14.58.03.png)
![Screenshot 2](/screenshots/Screenshot2024-06-12at14.55.44.png)
![Screenshot 2](/screenshots/Screenshot2024-06-12at14.55.37.png)
![Screenshot 2](/screenshots/Screenshot2024-06-12at14.55.02.png)
![Screenshot 2](/screenshots/Screenshot2024-06-12at18.20.26.png)


### Swager Documentation
![Screenshot 2](/screenshots/Screenshot2024-06-12at19.11.49.png)
![Screenshot 2](/screenshots/Screenshot2024-06-12at19.12.19.png)
![Screenshot 2](/screenshots/Screenshot2024-06-12at19.12.36.png)


## Video presentation of project

[Video link](https://drive.google.com/drive/folders/1BR_qLzhz5P1JVFfpLAKOqZHvO-NuY4hR)

## Server

[Server link](https://acme-corp.onrender.com)
