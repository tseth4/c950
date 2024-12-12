# **WGUPS Routing Program - C950**
**By Tristan Setha**

## **Overview**
The WGUPS (Western Governors University Parcel Service) Routing Program is a Python-based solution designed to optimize package deliveries for a busy parcel service. It uses an adjacency matrix for route distance calculations, a custom-built hash table for efficient data storage, and the Nearest Neighbor Algorithm for routing optimization. 

---

## **Features**
- **Routing Optimization:** Implements the Nearest Neighbor Algorithm to minimize travel distance while adhering to delivery deadlines.
- **Custom Hash Table:** Efficiently stores package data with O(1) average lookup and update times.
- **Adjacency Matrix:** Represents the distance between all delivery points for efficient route calculations.
- **Dynamic Updates:** Handles real-time changes, such as updated delivery addresses, with minimal disruption.
- **User-Friendly Interface:** Provides real-time delivery status updates and allows users to query package details.
- **Reporting Capabilities:** Generates detailed delivery logs and screenshots at specified time intervals.
- **Scalability:** Adaptable to handle larger datasets and growing package volumes.

---

## **Algorithm Details**
### **Nearest Neighbor Algorithm**
The program uses the **Nearest Neighbor Algorithm**, a greedy approach, to minimize delivery distances by visiting the closest undelivered package at each step. This method balances simplicity with efficiency, ensuring all packages are delivered on time.

**Pseudocode:**
```python
INPUT: 
Adjacency matrix of distances (distance_matrix), 
HashMap of packages (packages), Truck capacity (max_capacity)

OUTPUT:
Packages with info, delivery time, and a boolean displaying if delivered on time

INITIALIZE undelivered_packages = all packages
FOR each undelivered_packages:
    ASSIGN up to 16 packages to Truck1
    ASSIGN up to 16 packages to Truck2

SET current_time = 8:00 AM

WHILE undelivered_packages exist:
    FOR each truck:
        IF truck has packages:
            FIND nearest neighbor for the next package using adjacency_matrix
            DELIVER the package
            UPDATE package status to "delivered"
            RECORD delivery time for the package
            UPDATE truck location
            UPDATE current_time
        IF current_time == 10:20 AM:
            UPDATE package #9 with the new address

RETURN all package data
PRINT all package information
```

---

## **Big-O Complexity**
- **Hash Table Operations:** O(1) (average)
- **Adjacency Matrix Distance Lookups:** O(1)
- **Nearest Neighbor Algorithm:** O(n)
- **Overall Algorithm Complexity:** O(n²)

## **Data Structures**
### **Custom Hash Table**
- **Purpose:** Stores package data for quick access and dynamic updates.
- **Operations:** O(1) average time complexity for insertion, deletion, and lookups.
- **Key:** Package ID (unique and immutable) for efficient delivery management.
- **Stored Values:** Delivery address, deadline, city, ZIP code, weight, status, and delivery time.

### **Adjacency Matrix**
- **Purpose:** Represents distances between all delivery locations for efficient route calculations.
- **Implementation:** A 2D matrix where each cell contains the distance between two locations.
- **Strengths:** Allows O(1) access to any distance but uses more memory compared to adjacency lists.

---

## **Programming Environment**
- **Software:**
  - Visual Studio Code
  - Python 3.12.4
  - macOS Sequoia 15.1
- **Hardware:**
  - MacBook Air (Apple M1 Chip, 16GB RAM)
  - External Dell Monitor



---

## **Key Strengths of the Program**
- **Simplicity:** The Nearest Neighbor Algorithm is easy to implement and understand, making it suitable for small datasets.
- **Efficiency:** Custom hash tables and adjacency matrices provide rapid data access and support real-time updates.
- **Scalability:** Handles edge cases dynamically and is adaptable for larger datasets with additional optimization techniques.

---

## **Limitations and Future Enhancements**
- **Hash Table Weakness:** Collisions may require resolution strategies like chaining or open addressing.
- **Adjacency Matrix Weakness:** Memory usage increases significantly for larger datasets.

**Future Enhancements:**
- Use advanced algorithms like Christofides or genetic algorithms for more complex scenarios.
- Replace adjacency matrix with adjacency lists for memory efficiency in sparse graphs.
- Add data visualization for real-time truck routing and delivery status.

---

## **Screenshots**
1. **8:35 a.m. - 9:25 a.m.**
![9 AM](screenshots/0900_deliveries2.png)

2. **9:35 a.m. - 10:25 a.m.**
![10 AM](screenshots/1000_deliveries2.png)

3. **12:03 p.m. - 1:12 p.m.**
![12:30 AM](screenshots/1230_deliveries2.png)

4. **Total Mileage**
![Total miles](screenshots/miles.png)

---

## **References**
1. MathWorks. (2019). *What Is the Genetic Algorithm?* [MathWorks](https://www.mathworks.com/help/gads/what-is-the-genetic-algorithm.html)
2. GeeksforGeeks. (2014). *Binary Heap - GeeksforGeeks.* [GeeksforGeeks](https://www.geeksforgeeks.org/binary-heap/)
