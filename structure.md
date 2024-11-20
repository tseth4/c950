```
project_root/
│
├── data/
│   ├── distances.csv           # Distance matrix (raw data from CSV)
│   ├── packages.csv            # Package data (raw data from CSV)
│
├── src/
│   ├── __init__.py             # Makes src a Python package
│   ├── main.py                 # Entry point for the program
│   ├── data_loader.py          # Handles loading data from CSV files
│   ├── routing.py              # Implements routing algorithms (e.g., Nearest Neighbor)
│   ├── time_tracker.py         # Handles time calculations and updates
│   ├── utils.py                # Utility functions (e.g., distance calculations)
│
├── data_structures/
│   ├── __init__.py             # Makes data_structures a Python package
│   ├── adjacency_matrix.py     # Defines the AdjacencyMatrix class
│   ├── hash_table.py           # Defines the HashTable class for packages
│   ├── priority_queue.py       # (Optional) Defines a PriorityQueue class for deadlines
│
├── models/
│   ├── __init__.py             # Makes models a Python package
│   ├── package.py              # Defines the Package class
│   ├── truck.py                # Defines the Truck class
│
├── tests/
│   ├── test_routing.py         # Unit tests for routing algorithms
│   ├── test_data_loader.py     # Unit tests for data loading
│   ├── test_time_tracker.py    # Unit tests for time calculations
│   ├── test_adjacency_matrix.py # Unit tests for AdjacencyMatrix
│   ├── test_hash_table.py      # Unit tests for HashTable
│
├── outputs/
│   ├── delivery_log.txt        # Final delivery report
│   ├── debug_log.txt           # Debugging logs (optional)
│
├── requirements.txt            # Dependencies (e.g., pandas)
├── README.md                   # Overview of the project
```