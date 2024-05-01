import pandas as pd
from sqlalchemy import create_engine

# Credentials to connect to the database
username = "root"
password = ""
hostname = "127.0.0.1"
dbname = "products"

# Create engine to connect to the database
engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{hostname}/{dbname}")

# Insert data into "sales" table with product_id column
sales_data = pd.DataFrame({
    "sno_id": [1, 2, 3, 4, 5],  # Add serial numbers here
    "product_id": [1, 2, 3, 4, 5],  # Add product_id column
    "product_price": [10.5, 20.0, 15.75, 12.0, 18.5],
    "product_quantity": [100, 150, 80, 120, 90],
    "customer_id": [101, 102, 103, 104, 105],
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "order_timestamp": ["2024-04-10 08:30:00", "2024-04-11 12:45:00", "2024-04-12 15:20:00",
                        "2024-04-13 09:10:00", "2024-04-14 14:30:00"]
})

# Specify the "product_id" as the index
sales_data.set_index("product_id", inplace=True)

# Write the DataFrame to the "sales" table in the MySQL database
sales_data.to_sql(name="sales", con=engine, if_exists="replace", index=True)
