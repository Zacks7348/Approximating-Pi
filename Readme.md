# Approximating pi Using Randomly Generated Points

1. Lets plot a circle with r=1 and a square with side length equal to r at the origin. If we look at the first quadrant we see that the edges of the square lie on x=1 and y=1.
2. Now we can generate n random points (x,y) where x and y are randomly generated values in the range [0,1).
3. If we plot these points they will all lie somewhere in the first quadrant within the area of the square we created earlier.
4. We now want to find how many of these points we created lie within the area of the circle we drew earlier with r=1. If d is the distance between a point and the origin, we can tell if a point lies inside the circle if d <= 1, where d is calculated by the square root of (x^2 + y^2)
5. Now we can look at 2 equal ratios. Lets create some variables
    - Ac = Area of circle
    - As = Area of square
    - N = total number of points
    - c = number of points inside the circle 
 
6. Now lets look at two equal ratios  
(Ac/As) = (c/N)  
We know the following:  
Ac = pi * r^2  
As = (r+1)^2  
Since we know r=1, we can subsitute these formulas into the first ratio and plug 1 in for r and get the resulting equality  
pi/4 = c/N  
We can then solve for pi  
pi = 4c/N  

as N approaches infinity we should see our approximated value of pi approach the true value of pi
