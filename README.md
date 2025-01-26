# API Documentation

## **Base URL:**

`http://127.0.0.1:8000/api/`

---

## **Authentication**

### **Login**

**POST** `/token/`\
Request Body (JSON):

```json
{
    "username": "test@example.com",
    "password": "strongpassword123"
}
```

Response:

- Returns an authentication token upon successful login.

---

### **Register**

**POST** `/users/`\
Request Body (JSON):

```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "strongpassword123",
    "password2": "strongpassword123",
    "bio": "Hello, I'm a new user",
    "birth_date": "1990-01-01"
}
```

Response:

- Creates a new user account.

---

## **Todos**

### **Get All Todos**

**GET** `/samples/`\
Response:

- Returns a list of all todos stored in the MongoDB collection.

---

### **Add Todo**

**POST** `/samples/`\
Request Body (JSON):

```json
{
    "name": "Test Sample",
    "description": "This is a test",
    "project": "p1",
    "status": "pending",
    "assigned_users": ["64b0c2f6d6fc1f2a3b4e7d1c"]
}
```

Response:

- Creates a new todo and stores it in the MongoDB collection.

---

### **Get Single Todo**

**GET** `/samples/{id}/`\
Response:

- Returns details of a specific todo from MongoDB by its `_id`.

---

### **Update Todos**

Use appropriate HTTP methods (e.g., `PUT` or `PATCH`) on the endpoint `/samples/{id}/` to update an existing todo.\
Request Body:

```json
{
    "name": "Updated Sample",
    "status": "completed"
}
```

Response:

- Updates the specified fields of the todo in the MongoDB collection.

---

### **Notes:**

- Ensure to include the token in the `Authorization` header for authenticated routes:\
  `Authorization: Bearer <your_token>`.
- Replace `{id}` with the specific todo `_id` (MongoDB ObjectID) for detailed or update operations.

