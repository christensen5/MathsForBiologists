#!/usr/bin/env python
# coding: utf-8

# 1. Solve the following systems of linear equations
#     <br/>
#     
#     $$
#         \mbox{A.}  \ 
#         \begin{cases}
#             5x - y + 2z = 6 \\
#             x + 2y - z = -1 \\
#             3x + 2y - 2z = 1\\
#         \end{cases}
#     $$
#     
#     <br/>
#     
#     $$
#         \mbox{B.}  \ 
#         \begin{cases}
#             2x - y + 3z = 3 \\
#             2x + y + 4z = 4 \\
#             2x - 3y + 2z = 2\\
#         \end{cases}
#     $$

# 2. Three different species of insects are reared together in a laboratory cage. They are supplied with two different types of food each day. Each individual of species 1 consumes 3 units of food $A$ and 5 units of food $B$, each individual of species 2 consumes 2 units of food $A$ and 3 units of food $B$, and individual of species 3 consumes 1 unit of food $A$ and 2 units of food $B$. Each day, 500 units of food $A$ and 900 units of food $B$ are supplied. How many individuals of each species can be reared together? Is there more than one solution? What happens if we add 550 units of a third type of food, called $C$, and each individual of species 1 consumes 2 units of food $C$, each individual of species 2 consumes 4 units of food $C$, and each individual of species 3 consumes 1 unit of food $C$?

# 3. PRIMER

# 4. PRIMER

# 5. PRIMER

# 6. Write each system in matrix form
#    <br/>
#     
#     $$
#         \mbox{A.}  \ 
#         \begin{cases}
#             2x_2-x_1 = x_3 \\
#             4x_1 + x_3 = 7x_2 \\
#             x_2 - x_1 = x_3\\
#         \end{cases}
#     $$
#     
#     <br/>
#     
#     $$
#         \mbox{B.}  \ 
#         \begin{cases}
#             2x_1 - 3x_2 = 4 \\
#             -x_1 + x_2 = 3 \\
#             3x_1 = 4\\
#         \end{cases}
#     $$

# 7. Suppose that 
# 
#     <br/>
#     
#     $$
#         A = \begin{pmatrix}
#             2 & 4 \\
#             3 & 6 
#             \end{pmatrix}
#         \ \ \ \text{,}\ \ \
#         X = \begin{pmatrix}
#             x \\
#             y 
#             \end{pmatrix} \ \ \ \text{and}\ \ \
#             B = \begin{pmatrix}
#             b_1 \\
#             b_2 \\
#             \end{pmatrix}
#     $$
#     
#     <br/>
#     
#     1. Write $AX = B$ as a system of linear equations
#     
#     <br/>
#     
#     2. Show that if 
#     
#     <br/>
#     
#     $$
#         B = \begin{pmatrix}
#             3 \\
#             \frac92 \\
#             \end{pmatrix}
#     $$
#     
#     then $AX = B$ has infinitely many solutions. Graph the two straight lines associated with the corresponding system of linear equations, and explain why the system has infinitely many solutions.
#     
#     <br/>
#     
#     3. Find a column vector
#     
#     <br/>
#     
#     $$
#         B = \begin{pmatrix}
#             b_1 \\
#             b_2 \\
#             \end{pmatrix}
#     $$
#     
#     <br/>
#     
#     so that $AX = B$ has no solutions.

# 8. Assume that a population is divided into three age classes and that 80\% of the individuals age 0 and 10\% of the individuals age 1 survive until the end of the next breeding season. Assume further that individuals age 1 have an average of 1.6 female offspring and individuals age 2 have an average of 3.9 individual offspring. If, at time 0, the population consists of 1000 individuals age 0, 100 individuals age 1, and 20 individuals age 2, find the Leslie matrix and the age distribution at time 3.

# 9. Consider the following projection matrix representing a population with five age classes:
# 
#     <br/>
#     $$
#         P = \begin{pmatrix}
#         0 & 5 & 3 & 2 & 1 \\
#         0.9 & 0 & 0 & 0 & 0 \\
#         0 & 0.3 & 0 & 0 & 0 \\
#         0 & 0 & 0.1 & 0 & 0 \\
#         0 & 0 & 0 & 0.05 & 0 \\
#     \end{pmatrix}
#     $$
#     
#     <br/>
#     
#     1. Making use of Python or R code, begin with a population distributed as $(0,0,0,0,10)$ individuals, project the population $20$ time units, and plot the total number over time. Plot the logarithm of the total population over time.
#     
#     <br/>
#     
#     2. Repeat the above but begin with $(80,16,5,1,1)$ individuals. How do these results compare to the results in A. ?

# 10. In the problems below, find the eigenvalues $\lambda_1$ and $\lambda_2$ and corresponding eigenvectors $\mathbf{v_1}$ and $\mathbf{v_2}$ for each matrix $B$. Determine the equations of the lines through the origin in the direction of the eigenvectors $\mathbf{v_1}$ and $\mathbf{v_2}$, and graph the lines together with the eigenvectors $\mathbf{v_1}$ and $\mathbf{v_2}$ and the vectors $A\mathbf{v_1}$ and $A\mathbf{v_2}$.
# 
#     <br/>
#     
#     $$
#     \text{A.} \ \ B = \begin{pmatrix}
#     2 & 3\\
#     0 & -1
#     \end{pmatrix}
#     $$
# 
#     <br/>
# 
#     $$
#     \text{B.} \ \ B = \begin{pmatrix}
#     3 & 6\\
#     -1 & -4
#     \end{pmatrix}  
#     $$

# 11. Suppse that 
# 
#     <br/>
#     
#     $$
#     P = \begin{pmatrix}
#     0.5 & 2.3\\
#     a & 0
#     \end{pmatrix}
#     $$
#     
#     <br/>
#     
#     is the Leslie matrix of a population with two age classes. For which values of $a$ does this population grow?

# 12. Suppose that 
# 
#     <br/>
#     
#     $$
#     P = \begin{pmatrix}
#     0.5 & 2.0\\
#     0.1 & 0
#     \end{pmatrix}
#     $$
#     
#     <br/>
#     
#     is the Leslie matrix of a population with two age classes.
#     
#     1. If you were to manage this population, would you need to be concerned about its long-term survival?
#     
#     <br/>
#     
#     2. Suppose that you can improve either the fecundity or the survival of the zero-year-olds, but due to physiological and environmental constraints, the fecundity of zero-year-olds will not exceed 1.5 and the survival of zero-year-olds will not exceed 0.4. Investigate how the growth rate of the population is affected by changing either the survival or the fecundity of zero-year-olds, or both.What would be the maximum achievable growth rate?
#     
#     <br/>
#     
#     3. In real situations, what other factors might you need to consider when you decide on management strategies?
