# **Software Architecture Microservices with Flask**

**Instructor:** Jesus Salvador Lopez Ortega ([LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport))
  
## **Index**
- [**Software Architecture Microservices with Flask**](#software-architecture-microservices-with-flask)
  - [**Index**](#index)
  - [**Due Date**](#due-date)
  - [**Project Details**](#project-details)
    - [📘 Project Overview](#-project-overview)
    - [🚀 How to Run](#-how-to-run)
    - [🧩 Architecture Summary](#-architecture-summary)
    - [🗺️ Patterns Used](#️-patterns-used)
  - [**Class Activities**](#class-activities)
    - [✅ Objectives](#-objectives)
    - [📌 Activities](#-activities)
    - [🧠 Reflection Questions](#-reflection-questions)
  - [**Homework**](#homework)
    - [✅ Objectives](#-objectives-1)
    - [📌 Activities](#-activities-1)
    - [🧠 Reflection Questions](#-reflection-questions-1)
  - [**Contact**](#contact)

---

## **Due Date**
- **Start Date:** September 29, 2025
- <span style="color:gold"><b>Due date:</b> October 6, 2025 ⏰</span>

---

## **Project Details**

### 📘 Project Overview

This project is a software architecture practice based on microservices.
It includes three main components:

- **Users Service:** manages users, providing endpoints to create, list, and view user information.
- **Products Service:** manages products, providing endpoints to create, list, and view product data.
- **Gateway Service:** serves as a unified entry point to consume the data from the other services.

Each microservice runs independently with its own `Flask` server, local data files `(.json)`, and `HTML` templates for the views.

### 🚀 How to Run

> 💡 **Note:** This steps need to be run in different terminals for each microservice.

1. **Setup your virtual environment**

Windows:
```bash
.\setup_venv.ps1
```

Linux & macOs:
```bash
source setup_venv.sh
```

2. **Run the microservice** 

Windows:
```bash
.\products-services.ps1
```

Linux & macOs:
```bash
source products-services.sh
```

> 💡 **Note:** The different terminals need to be running at the same time.

1. **Access the endpoint**
- Open your browser and go to: 
  - `http://localhost:5000/` for the gateway
  - `http://localhost:5001/` for the users service
  - `http://localhost:5002/` for the products service
- You should see a rendered web application.

### 🧩 Architecture Summary

- **Language:** Python 3 (Flask framework).
- **Architecture:** RESTful microservices.
- **Main Components:**
  - **`users_services/:`** user management service.
  - **`products_services/:`** product management service.
  - **`gateway/:`** orchestrator and unified access point.
- **Communication:** HTTP (requests between microservices via Flask).
- **Data:** persisted in local `JSON` files (`users.json`, `products.json`).
- **Front-end:** HTML templates rendered with Flask (`Jinja2`).
- **Deployment:** local execution using `.sh` scripts (Linux/macOS) or `.ps1` scripts (Windows).

### 🗺️ Patterns Used

| Pattern                  | Purpose                                                                 |
|---------------------------|-------------------------------------------------------------------------|
| **Microservices**         | Splits the system into independent, loosely coupled services            |
| **Gateway**               | Provides a single entry point for clients, hiding service complexity    |
| **Repository**            | Encapsulates data access logic using JSON files as storage              |
| **Dependency Injection**  | Decouples components and makes services easier to test and extend       |
| **Model-View-Controller** | Separates concerns: Flask routes (controllers), templates (views), and JSON data (models) |
| **RESTful API**           | Standardizes communication between services through HTTP methods        |

---

## **Class Activities**

### ✅ Objectives
- Explore how independent microservices interact within the architecture.  
- Add new **users** and **products**, then verify data consistency through the Gateway.  
- Observe how the system responds when one microservice is unavailable.  
- Identify error messages or responses returned by the Gateway when a service is down.  
- Reflect on the importance of **fault tolerance** and **resilience** in distributed systems.  

### 📌 Activities
1. **Start all microservices** (Users, Products, Gateway).  
2. **Add users** via the Users Service and verify they appear in the Gateway.  
3. **Add products** via the Products Service and confirm they can be queried from the Gateway.  
4. **Stop one microservice** (e.g., Products Service) and attempt to access products through the Gateway.  
5. **Document observations**: what responses are returned, what still works, and what fails.  
6. **Restart the stopped service** and verify system recovery. 

### 🧠 Reflection Questions
- What did you notice when adding users and products separately versus through the Gateway?  
- How did the Gateway behave when one of the microservices was stopped?  
- Which parts of the system remained functional even when a service was unavailable?  
- What type of error messages or responses did you observe, and were they clear to the user?  
- How would you improve the system’s fault tolerance to handle unavailable services more gracefully?  
- Why is resilience an important consideration in a microservices architecture?  
- If this system were deployed in production, what strategies would you propose to ensure high availability?  

---

## **Homework**

### ✅ Objectives
- Understand the principles of microservice design.  
- Set up a new Flask-based microservice with routes and templates.  
- Implement a data model that allows **users to reference purchased products**.  
- Establish communication between the **Users Service** and the **Products Service**.  
- Practice **data persistence** using JSON files (or an equivalent simple store).  
- Integrate the new microservice with the **Gateway Service** for unified access.  
- Test the complete workflow:  
  1. Create users  
  2. Create products  
  3. Assign purchased products to users  
  4. Query user details including their product list  

### 📌 Activities

1. **Set up project structure** for the new microservice `purchases_service/`.  
2. **Define routes** for:
   - Creating a purchase (linking a user and a product).  
   - Listing purchases for a user.  
3. **Modify Users Service** to store a `purchased_products` field (list of product IDs).  
4. **Connect with Products Service** to validate product existence.  
5. **Update Gateway** to expose combined endpoints (users + products purchased).  
6. **Test end-to-end flow** with sample data.  

### 🧠 Reflection Questions

- What advantages did you observe in using a microservices architecture compared to a monolithic design?  
- What challenges did you face when connecting the Users Service with the Products Service?  
- How does the Gateway improve the overall usability of the system for clients?  
- If you were to replace the JSON files with a real database, what changes would be required in your services?  
- How could Dependency Injection make your microservice easier to test and maintain?  
- What trade-offs did you notice between simplicity (local JSON storage) and scalability (real databases, APIs)?  
- How would you handle failures if one of the microservices becomes unavailable?  
- In what scenarios would you recommend microservices over a monolithic application?  

---

## **Contact**

¿Any doubt? Check the support files or contact your instructor.

**Politécnica de Santa Rosa**

- **Carreer: ISW**
- **Assignature: Software Architectures**
- **Author:** Jesus Salvador Lopez Ortega ([LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport))
- **Last updated**: September 2025