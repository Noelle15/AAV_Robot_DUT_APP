# AAV : Project of the robot
----- The project has been coded by Imène EL AINI and Noëlle VERMA -----

The project is to make algorithms that will enable to run through several predefined points in the shortest way possible.
In other words, starting from the first point, we have to run through all the other points and come back to the original point in the shortest way possible.

## Algorithms
To achieve the goal described above, we have to code three algorithm.

### Nearest
This algorithm resolves the problem by looking for the next closest point in the circuit. It is not the most efficient way to find the shortest circuit.

We decided to calculate the distance of all of the remaining points with the first point and to choose the nearest to be our next point. And then, we do the same with this new point and all of the remaining points.
All the tests pass for this algorithm.

### Better
This algorithm solves the problem better than the Nearest Algorithm but not as good as the Optimal Algorithm.
However, it is faster than the Optimal Algorithm.

We solved the problem by taking 3 points and permute their order to find the combination that is the shortest. Then, we move to the next group of 3 points and do the same. All of this is done until we reach the end of the list_of_points. This method enables to have a short circuit in a small amount of time. 

We were'nt able to achieve the ends of this algorithm because the the result is not better than the Nearest one.

### Optimal
This algorithm finds the shortest path by comparing the length of every possible circuit. It gives the best result but takes some time to run (around 7 seconds for a list of 10 points).
As far as the tests are concerned, they both work.

## Sources
To complete this work, we have used in particular the following websites :

https://docs.python.org/fr/2.7/ , to know more about the library of python and the functions available.

http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/notebooks/expose_TSP.html , to inspire us about the great algorithm and the way we can solve it by comparing 3 points.
