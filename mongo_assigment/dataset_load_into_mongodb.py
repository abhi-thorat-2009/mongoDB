import pandas as pd
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")  
db = client['superstore_db']  # Database name
collection = db['orders']  # Collection name

# Load the Superstore dataset from CSV using pandas  
data = pd.read_csv(r'C:\Users\SSK\Desktop\mongo_assigment\superstore.csv', encoding='windows-1252')

# Convert the DataFrame to a list of dictionaries (documents)
documents = data.to_dict(orient='records')

# Insert the documents into the MongoDB collection
collection.insert_many(documents)

print(f"Successfully loaded {len(documents)} records into MongoDB.")