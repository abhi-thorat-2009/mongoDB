# MongoDB Installation and Python Connection Guide

This guide helps you install **MongoDB**, set up a **Python environment**, and connect to **MongoDB** using **PyMongo**.

## Prerequisites

- Python (>= 3.6)
- MongoDB (either locally or MongoDB Atlas)

---

## Step 1: Install MongoDB

### 1.1. **Install MongoDB Locally**

#### Windows:

1. Download the installer from the [MongoDB download page](https://www.mongodb.com/try/download/community).
2. Run the installer and follow the setup instructions:
   - **Install MongoDB as a Service** (recommended).
   - **Data directory path**: Set up `C:\data\db` (default).
3. After installation, start MongoDB using the following command in the **Command Prompt**:
   ```bash
   mongod
   ```
4. Open a new **Command Prompt** window and enter `mongo` to access the MongoDB shell.

#### macOS:

1. If you have **Homebrew** installed, you can run the following command:
   ```bash
   brew tap mongodb/brew
   brew install mongodb-community@5.0
   ```
2. Start MongoDB using:
   ```bash
   brew services start mongodb/brew/mongodb-community
   ```

#### Linux:

Follow the specific installation instructions for your Linux distribution from the [MongoDB installation documentation](https://docs.mongodb.com/manual/installation/).

---

### 1.2. **Using MongoDB Atlas (Cloud Database)**

1. Sign up for **MongoDB Atlas**: [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. Create a **new cluster** and follow the setup instructions.
3. Get the **connection string** from the **Connect** button in the MongoDB Atlas dashboard.
4. Ensure your **IP address** is whitelisted and create a **MongoDB user** for access.

---

## Step 2: Install Python and PyMongo

### 2.1. **Install Python**

Ensure that **Python 3.6+** is installed on your system. If not, you can download it from [python.org](https://www.python.org/downloads/).

### 2.2. **Install PyMongo**

To interact with MongoDB from Python, you’ll need the **PyMongo** package. Install it via **pip**:
```bash
pip install pymongo
```

---

## Step 3: Connect to MongoDB from Python

### 3.1. **Connect to MongoDB Locally**

```python
from pymongo import MongoClient

# Connect to the local MongoDB instance (default URI)
client = MongoClient("mongodb://localhost:27017/")

# Access the database
db = client['superstore_db']  # Replace with your database name

# Access the collection
collection = db['orders']  # Replace with your collection name

# Fetch a single document to test the connection
document = collection.find_one()
print(document)
```



