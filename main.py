import data as dt
import pso as ps
import neural_network as nn
# import data_insert as datainsert

# Insert Data
# datainsert.insert_data_into_tables() 
# directly call the file to insert data into the database

# Data preprocessing
dt.first_data_handle()
dt.products_with_sales()
dt.create_week_data()
dt.create_nn_data()
dt.pso_data()


# Test the neural network
nn.nn_testing()


# Optimize prices using particle swarm optimization
ps.optimize_prices()
