MongoDB Installation and Python Connection Setup
Prerequisites
Python (version 3.6 or higher)
MongoDB (either locally or via MongoDB Atlas)
Step 1: Install MongoDB
1.1. Install MongoDB Locally
On Windows:
Download the MongoDB installer from the official MongoDB website.
Choose the version appropriate for your operating system (Windows).
Run the installer and follow the instructions:
Install MongoDB as a Service (this is recommended).
Set up the MongoDB data directory (default path: C:\data\db).
Once installation is complete, you can start MongoDB by running the following command in Command Prompt:
bash
Copy
Edit
mongod
You can now access MongoDB by running the MongoDB shell in another terminal window:
bash
Copy
Edit
mongo
On macOS:
If you have Homebrew installed, you can install MongoDB using the following command:
bash
Copy
Edit
brew tap mongodb/brew
brew install mongodb-community@5.0
Start MongoDB using the command:
bash
Copy
Edit
brew services start mongodb/brew/mongodb-community
On Linux:
Follow the MongoDB installation instructions specific to your Linux distribution, available at the MongoDB installation documentation.
