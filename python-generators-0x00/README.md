## Overview
The `seed.py` script is designed to:
1. Set up a MySQL database named `ALX_prodev`.
2. Create a table `user_data` with the specified schema if it doesn't already exist.
3. Populate the `user_data` table with sample data from a CSV file (`user_data.csv`).

## Requirements

### Prerequisites
- MySQL server running on your system or accessible remotely.
- Python 3.x installed.
- Required Python package: `mysql-connector-python`.

### Table Schema
The `user_data` table is structured as follows:
- **`user_id`**: Primary key, `UUID` (indexed).
- **`name`**: `VARCHAR`, NOT NULL.
- **`email`**: `VARCHAR`, NOT NULL.
- **`age`**: `DECIMAL`, NOT NULL.

## Setup Instructions

### Step 1: Install Python Dependencies
Install the required Python package using pip:

```bash
pip install mysql-connector-python
```

### Step 2: Update Database Credentials
In the `seed.py` script, update the following placeholders with your MySQL credentials:

```python
host="localhost",
user="your_username",
password="your_password"
```

### Step 3: Provide the CSV File
Ensure the `user_data.csv` file is in the same directory as the script or provide its absolute path in the `csv_file_path` variable.

### Step 4: Run the Script
Run the `seed.py` script to set up the database, create the table, and populate it with data:

```bash
python seed.py
```

## Script Details

### Functions

1. **`connect_db()`**
   - Connects to the MySQL database server.

2. **`create_database(connection)`**
   - Creates the `ALX_prodev` database if it does not already exist.

3. **`connect_to_prodev()`**
   - Connects to the `ALX_prodev` database.

4. **`create_table(connection)`**
   - Creates the `user_data` table with the required schema if it does not exist.

5. **`insert_data(connection, data)`**
   - Inserts rows into the `user_data` table from the CSV file.

6. **`read_csv(file_path)`**
   - Reads and parses the `user_data.csv` file.

### CSV Data Requirements
The `user_data.csv` file should have the following column headers:
- `name`
- `email`
- `age`

Example:

```csv
name,email,age
John Doe,john.doe@example.com,30.5
Jane Smith,jane.smith@example.com,25.0
```

## Output
- Creates the `ALX_prodev` database (if it does not exist).
- Creates the `user_data` table with the required fields.
- Populates the table with the data from the CSV file.

### Example Success Message

```plaintext
Database setup and data insertion complete.
```

## Troubleshooting

### Common Issues
1. **Authentication Failure:**
   - Ensure your MySQL username and password are correct.

2. **MySQL Server Not Running:**
   - Start the MySQL server and ensure it's accessible.

3. **CSV File Issues:**
   - Ensure the CSV file exists and is formatted correctly.

4. **Dependencies Not Installed:**
   - Run `pip install mysql-connector-python` to install the required package.