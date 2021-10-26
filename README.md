# Solver of first order ODE via numerical methods
## made by Konstantin Smirnov (B20-06 at Innopolis University)

The application plots charts of solutions of the first order ODE via numerical methods and LTE's and GTE's:
* Euler's
* Improved Euler's
* Runge-Kutta

GUI is made by:
* PyQT
* MAtplotlib

![Image of GUI](https://github.com/Skvayzer/DE-numerical-solutions/blob/master/images/GUI.png)

UML class diagram:
![Image of UML](https://github.com/Skvayzer/DE-numerical-solutions/blob/master/images/UML.png)

The app solves Initial Value Problem (IVP):
![Image of IVP](https://github.com/Skvayzer/DE-numerical-solutions/blob/master/images/IVP.png)

x ∈ [x0, X], N - number of grid steps

Next let's consider this example (Variant 24):
![Image of MyVariant](https://github.com/Skvayzer/DE-numerical-solutions/blob/master/images/example.png)

Analytical solution:
![Image of AnalyticalSolution](https://github.com/Skvayzer/DE-numerical-solutions/blob/master/images/analytical_solution.png)


![Image of GUI](https://github.com/Skvayzer/DE-numerical-solutions/blob/master/images/GUI.png)
![Image of GTEs](https://github.com/Skvayzer/DE-numerical-solutions/blob/master/images/GTEs.png)

As we can see from these charts, the best approximation gives the Runge-Kutta method and the worst gives the Euler's.
Also in this example there's a point of discontinuity: x=0
In this case numerical methods don't work, because they either overflow in infinity or step over the point of discontinuity and lose precision.
![Image of discontinuity_break1](https://github.com/Skvayzer/DE-numerical-solutions/blob/master/images/discontinuity_method_break.png)
![Image of discontinuity_break2](https://github.com/Skvayzer/DE-numerical-solutions/blob/master/images/discontinuity_gte_break.png)

Also there's a warning of grid step h= (X - x0)/N becomes larges than 1. In this case methods lose precision.
