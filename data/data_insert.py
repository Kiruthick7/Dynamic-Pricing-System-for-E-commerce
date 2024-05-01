import pandas as pd
from sqlalchemy import create_engine

def insert_data_into_tables(username, password, hostname, dbname,range):
    # Create engine to connect to the database
    engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{hostname}/{dbname}")

    # Insert data into "sales2" table
    sales2_data = pd.DataFrame({
        "sno_id": list(range(1, range+1)),
        "product_id": [f"101-{i}" for i in range(1, range+1)],
        "product_price": [10.5 + (i * 0.5) for i in range(range)],
        "product_quantity": [100 + (i * 10) for i in range(range)],
        "customer_id": [f"101-{i}" for i in range(1, range+1)],
        "order_id": [f"2001-{i}" for i in range(1, range+1)],
        "order_timestamp": pd.date_range("2024-04-10 08:30:00", periods=range, freq="h")
    })
    sales2_data.set_index("sno_id", inplace=True)
    sales2_data.to_sql(name="sales2", con=engine, if_exists="replace", index=True)

    # Insert data into "data_for_optimization" table
    data_for_optimization = pd.DataFrame({
        "sno_id": list(range(1, range+1)),
        "product_id": [f"101-{i}" for i in range(1, range+1)],
        "arxikiTimi": [10.0 + (i * 0.5) for i in range(range)],
        "telikiTimi": [9.5 + (i * 0.5) for i in range(range)]
    })
    data_for_optimization.set_index("sno_id", inplace=True)
    data_for_optimization.to_sql(name="data_for_optimization", con=engine, if_exists="replace", index=True)

# Example usage:
username = "root"
password = ""
hostname = "127.0.0.1"
dbname = "products"
range = 1200

insert_data_into_tables(username, password, hostname, dbname)

# import pandas as pd
# from sqlalchemy import create_engine

# # Credentials to connect to the database
# username = "root"
# password = "Sep032020!"
# hostname = "127.0.0.1"
# dbname = "products"

# # Create engine to connect to the database
# engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{hostname}/{dbname}")

# # # Create table "sales2" in the database
# # engine.execute("CREATE TABLE IF NOT EXISTS sales2 ("
# #                 "sno_id INT PRIMARY KEY, "
# #                 "product_id VARCHAR(255), "
# #                 "product_price FLOAT, "
# #                 "product_quantity INT, "
# #                 "customer_id VARCHAR(255), "
# #                 "order_id VARCHAR(255), "
# #                 "order_timestamp DATETIME"
# #                 ")")

# # Insert data into "sales2" table
# sales2_data = pd.DataFrame({
#     "sno_id": list(range(1, 1501)),
#     "product_id": [f"101-{i}" for i in range(1, 1501)],
#     "product_price": [10.5 + (i * 0.5) for i in range(1500)],
#     "product_quantity": [100 + (i * 10) for i in range(1500)],
#     "customer_id": [f"101-{i}" for i in range(1, 1501)],
#     "order_id": [f"2001-{i}" for i in range(1, 1501)],
#     "order_timestamp": pd.date_range("2024-04-10 08:30:00", periods=1500, freq="h")
# })
# sales2_data.set_index("sno_id", inplace=True)
# sales2_data.to_sql(name="sales2", con=engine, if_exists="replace", index=True)

# # # create table sales
# # engine.execute("CREATE TABLE IF NOT EXISTS sales ("
# #                 "sno_id INT PRIMARY KEY, "
# #                 "product_id VARCHAR(255), "
# #                 "product_price FLOAT, "
# #                 "product_quantity INT, "
# #                 "customer_id VARCHAR(255), "
# #                 "order_id VARCHAR(255), "
# #                 "order_timestamp DATETIME"
# #                 ")")

# # # Create table "products_2000_sales" in the database
# # engine.execute("CREATE TABLE IF NOT EXISTS products_2000_sales ("
# #                 "sno_id INT PRIMARY KEY, "
# #                 "product_id VARCHAR(255), "
# #                 "product_quantity INT"
# #                 ")")

# # # Create table "week_data" in the database
# # engine.execute("CREATE TABLE IF NOT EXISTS week_data ("
# #                 "sno_id INT PRIMARY KEY, "
# #                 "product_id VARCHAR(255), "
# #                 "week INT, "
# #                 "product_quantity INT, "
# #                 "product_price FLOAT, "
# #                 "product_cost FLOAT, "
# #                 "product_max_bound FLOAT"
# #                 ")")

# # # Create table "nn_data" in the database
# # engine.execute("CREATE TABLE IF NOT EXISTS nn_data ("
# #                 "sno_id INT PRIMARY KEY, "
# #                 "week INT, "
# #                 "product_id VARCHAR(255), "
# #                 "product_cost FLOAT, "
# #                 "product_max_bound FLOAT, "
# #                 "P1 FLOAT, "
# #                 "Q1 INT, "
# #                 "P2 FLOAT, "
# #                 "Q2 INT, "
# #                 "P3 FLOAT, "
# #                 "Q3 INT"
# #                 ")")

# # # Create table "data_for_optimization" in the database
# # engine.execute("CREATE TABLE IF NOT EXISTS data_for_optimization ("
# #                 "sno_id INT PRIMARY KEY, "
# #                 "product_id VARCHAR(255), "
# #                 "arxikiTimi FLOAT, "
# #                 "telikiTimi FLOAT"
# #                 ")")


# # # Insert data into "sales" table
# # # Create sales data with some products purchased more than 2000 times
# # sales_data = pd.DataFrame({
# #     "sno_id": list(range(1, 2001)),
# #     "product_id": [f"101-{i}" for i in range(1, 2001)],
# #     "product_price": [10.5 + (i * 0.5) for i in range(2000)],
# #     "product_quantity": [100 + (i * 10) if i < 10 else 2000 + (i * 10) for i in range(2000)],
# #     "customer_id": [f"101-{i}" for i in range(1, 2001)],
# #     "order_id": [f"2001-{i}" for i in range(1, 2001)],
# #     "order_timestamp": pd.date_range("2024-04-10 08:30:00", periods=2000, freq="h")
# # })
# # sales_data.set_index("sno_id", inplace=True)

# # # Write the modified sales data to the "sales" table in the database
# # sales_data.to_sql(name="sales", con=engine, if_exists="replace", index=True)

# # # # Insert data into "products_2000_sales" table
# # # products_2000_sales_data = pd.DataFrame({
# # #     "sno_id": list(range(1, 2001)),
# # #     "product_id": [f"101-{i}" for i in range(1, 2001)],
# # #     "product_quantity": [2000 + (i * 100) for i in range(2000)]
# # # })
# # # products_2000_sales_data.set_index("sno_id", inplace=True)
# # # products_2000_sales_data.to_sql(name="products_2000_sales", con=engine, if_exists="replace", index=True)

# # # Insert data into "week_data" table
# # week_data = pd.DataFrame({
# #     "sno_id": list(range(1, 2001)),
# #     "product_id": [f"101-{i}" for i in range(1, 2001)],
# #     "week": [1 + (i // 35) for i in range(2000)],
# #     "product_quantity": [100 + (i * 10) for i in range(2000)],
# #     "product_price": [10.5 + (i * 0.5) for i in range(2000)],
# #     "product_cost": [8.4 + (i * 0.4) for i in range(2000)],
# #     "product_max_bound": [12.6 + (i * 0.6) for i in range(2000)]
# # })
# # week_data.set_index("sno_id", inplace=True)
# # week_data.to_sql(name="week_data", con=engine, if_exists="replace", index=True)

# # # Insert data into "nn_data" table
# # nn_data = pd.DataFrame({
# #     "sno_id": list(range(1, 2001)),
# #     "week": [1 + (i // 35) for i in range(2000)],
# #     "product_id": [f"101-{i}" for i in range(1, 2001)],
# #     "product_cost": [8.4 + (i * 0.4) for i in range(2000)],
# #     "product_max_bound": [12.6 + (i * 0.6) for i in range(2000)],
# #     "P1": [10.5 + (i * 0.5) for i in range(2000)],
# #     "Q1": [100 + (i * 10) for i in range(2000)],
# #     "P2": [10.5 + (i * 0.5) for i in range(2000)],
# #     "Q2": [100 + (i * 10) for i in range(2000)],
# #     "P3": [10.5 + (i * 0.5) for i in range(2000)],
# #     "Q3": [100 + (i * 10) for i in range(2000)]
# # })
# # nn_data.set_index("sno_id", inplace=True)
# # nn_data.to_sql(name="nn_data", con=engine, if_exists="replace", index=True)

# # Insert data into "data_for_optimization" table
# data_for_optimization = pd.DataFrame({
#     "sno_id": list(range(1, 1501)),
#     "product_id": [f"101-{i}" for i in range(1, 1501)],
#     "arxikiTimi": [10.0 + (i * 0.5) for i in range(1500)],
#     "telikiTimi": [9.5 + (i * 0.5) for i in range(1500)]
# })
# data_for_optimization.set_index("sno_id", inplace=True)
# data_for_optimization.to_sql(name="data_for_optimization", con=engine, if_exists="replace", index=True)

