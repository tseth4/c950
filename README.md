# WGUPS
### By Tristan Setha
##### A.  Identify a named self-adjusting algorithm (e.g., nearest neighbor algorithm, greedy algorithm) that could be used to create your program to deliver the packages.

The Nearest Neighbor Algorithm will be used, which selects the nearest unvisited delivery location at each location to minimize  the distance based on the truck's current location.

##### B.  Identify a self-adjusting data structure, such as a hash table, that could be used with the algorithm identified in part A to store the package data.

A hash table can be used to store package data efficiently. Hash tables dynamically adjust their size as more elements are added, and each package is keyed by its unique package ID, enabling O(1) average lookup time.

1. In a hash table, each key is associated with a value. In this case, the package ID will map to an index where the package data is stored. Using a hash function provides direct access to update package information. Related components, such as deadlines and addresses, are grouped within each package entry in the hash table. The hash table allows dynamic updates to package data, enabling tracking of package status and live updates for delivery information.


##### C.  Write an overview of your program in which you do the following:


Explain the algorithm’s logic using pseudocode.
	Sort packages by deadline
```
INPUT: 
Adjacency matrix of distances (distance_matrix), 
HashMap of packages (packages), Truck capacity (max_capacity)

OUTPUT:
Packages with info, delivery time and a boolean displaying if delivered on time


INITIALIZE undelivered_packages = all packages
FOR each undelivered_packages:
    ASSIGN up to 16 packages to Truck1
    ASSIGN up to 16 packages to Truck2

SET current_time = 8:00 AM

WHILE undelivered_packages exist:
    FOR each truck:
        IF truck has packages:
            FIND nearest neighbor for the next package
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
##### 2.  Describe the programming environment you will use to create the Python application, including both the software and hardware you will use.
Software: Visual studio code, iTerm, Python 3.12.4, MacOS Sequoia 15.1
Hardware: Macbook Air, Apple M1 Chip, 16gb memory, Dell monitor

##### 3.  Evaluate the space-time complexity of each major segment of the program and the entire program using big-O notation.

Hashtable operation O(1)
Nearest Neighbor Algorithm O(n)
Algorithm: Search all packages with each package o(n^2)


##### 4.  Explain the capability of your solution to scale and adapt to a growing number of packages.

The solution can scale to handle more packages by implementing route optimization techniques, such as pre-computing routes using hash maps to group packages by delivery addresses. This method allows efficient management of large datasets and reduces redundant calculations.


##### 6.  Describe both the strengths and weaknesses of the self-adjusting data structure (e.g., the hash table).

Strengths: Hash tables provide O(1) average time complexity for lookups and updates, are dynamic for changes like status updates, and handle large datasets efficiently with proper hashing.
Weaknesses: Hash collisions may require additional logic to resolve conflicts.

##### 7.  Justify the choice of a key for efficient delivery management from the following components:
	
“For all items that might be stored in the hash table, every key is ideally unique so that the hash table's algorithms can efficiently search for a specific item by that key” (Lysecky, Vahid, & Olds, n.d.). In this situation, the package ID is the most suitable key as it is unique, immutable, and clearly identifies each package. In contrast, fields like delivery address or deadline are not unique and could lead to ambiguity.

