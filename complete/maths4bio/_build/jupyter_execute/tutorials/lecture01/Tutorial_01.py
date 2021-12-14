#!/usr/bin/env python
# coding: utf-8

# # Tutorial 01

# 1.  An autocatalytic reaction uses its resulting product for the formation of a new product, as in the reaction  
#   
#     $$A + X \rightarrow X$$  
#     
#     If we assume that this reaction occurs in a closed vessel, then the reaction rate is given by
#     
#     $$
#        R(x) = kx(a - x)
#     $$
#     
#     for $0 \le x \le a$, where $a$ is the initial concentration of $A$ and $x$ is the concentration of $X$.
#     
#     <br/>
#     
#     (a) Show that $R(x)$ is a polynomial and determine its degree.
#     <br/>
#     (b) Without using any graphic visualiser, graph $R(x)$ for $k = 2$ and $a = 6$. Find the value of $x$ at which the reaction rate is maximal.  
#     
#     <br/>
#       
# 2. Find the maximum/minimum value of the following polynomials  
#   
#     <br/>
#     
#     (a) $p(x) = x^2 - 2x - 3$
#     
#     (b) $p(x) = -x^2 - 6x + 8$
#     
#     (*Hint:* Calculate the roots and consider the symmetry of the parabola)  
#     
#     <br/>
#       
# 3. There is a function that is frequently used to describe the per capita growth rate of organisms when the rate depends on the concentration of some nutrient and becomes saturated for large enough nutrient concentrations. If we denote the concentration of the nutrient by $N$, then the per capita growth rate $r(N)$ is given by the *Monod growth function*
# 
#     $$
#         r(N)=\frac{aN}{k+N},\ \ \ N \ge 0
#     $$
#     
#     where $a$ and $k$ are positive constants.
#     
#     <br/>
#     
#     (a) Use Python or R to investigate the Monod growth function. Graph $r(N)$ for (i) $a = 5$ and $k = 1$, (ii) $a = 5$ and $k = 3$, and (iii) $a = 8$ and k = 1. Place all three graphs in the same coordinate system.
#     
#     (b) On the basis of the graphs in (a), describe in words what happens when you change $a$.
#     
#     (c) On the basis of the graphs in (a), describe in words what happens when you change $k$.  
#     
#     <br/>
#       
#       
# 4. The function 
# 
#     $$
#         f(x) = \frac{x^n}{b^n + x^n},\ \ \ x \ge 0
#     $$ 
#     
#     where $n$ is a positive integer and $b$ is a positive real number, is used in biochemistry to model reaction rates as a function of the concentration of some reactants    
#     
#     <br/>
#     
#     (a) Use Python or R to graph $f(x)$ for $n = 1, 2,\ \mbox{and}\ 3$ in the same coordinate system when $b = 2$.
#     
#     (b) Where do the three graphs in (a) intersect?
#     
#     (c) What happens to $f(x)$ as $x$ gets larger?
# 
#     (d) For an arbitrary positive value of $b$, show that $f (b) = 1/2$. On the basis of this demonstration and your answer in C. ,  explain why $b$ is called the half-saturation constant.  
#     
#     <br/>
#   
#   
# 5. The file [words_moby_dick.csv](https://imperialcollegelondon.box.com/s/940y521dq1owarx8pt4d4mu2d0f2cz85) contains data on the cumulative distribution of the number of times specific words occur in the text of the novel *Moby Dick*, by Herman Melville. Assume that this distribution is a power law of the form 
# 
#     $$
#         y = x^D
#     $$
#     
#     (a) Using the provided data, and R/Python, estimate the exponent of this power law. 
#     (*Hint:* If you plot this data in log-log scale, what should correspond to the exponent $D$?)
#     
#     (b) Can you think of a better way to estimate D?  
#     
#     <br/>
#   
#   
# 6. Assume that a population size at time $t$ is $N(t)$ and that
# 
#     $$
#         N(t) = 40 \cdot 2^t,\ \ \ t \ge 0
#     $$    
# 
#     (a) Find the population size at time t = 0.
# 
#     (b) Show that
# 
#     $$
#         N(t) = 40\, \mbox{e}^{t\, ln 2},\ \ \ t \ge 0
#     $$    
# 
#     (c) How long will it take until the population size reaches 1000?
#     
#    (*Hint*: Find $t$ so that $N(t) = 1000$.)  
#    
#    <br/>
#      
# 7. (*Adapted from Moss, 1980*) Hall (1964) investigated the change in population size of the zooplankton species *Daphnia galeata mendota* in Base Line Lake, Michigan. The population size $N(t)$ at time $t$ was modeled by the equation
# 
#     $$ 
#         N(t) = N_0\mbox{e}^{rt}
#     $$
#     
#     where $N_0$ denotes the population size at time $0$. The constant $r$ is called the **intrinsic rate of growth**.
#     
#     <br/>
#     
#     (a) Plot $N(t)$ as a function of $t$ if $N_0 = 100$ and $r = 2$. Compare your graph against the graph of $N(t)$ when $N_0 = 100$ and $r = 3$. Which population grows faster?
#     
#     (b) The constant $r$ is an important quantity because it describes how quickly the population changes. Suppose that you determine the size of the population at the beginning and at the end of a period of length $1$, and you find that at the beginning there were $200$ individuals and after one unit of time there were $250$ individuals. Determine $r$. (*Hint*: Consider the ratio $N(t+1)/N(t)$.)  
#     
#     <br/>
#       
# 8. Fish are indeterminate growers; that is, they grow throughout their lifetime. The growth of fish can be described by the von Bertalanffy function
# 
#     $$
#         L(x) = L_{\infty}(1-\textrm{e}^{-kx} )
#     $$
#     
#     for $x \ge 0$, where $L(x)$ is the length of the fish at age $x$ and $k$ and $L_{\infty}$ are positive
#     
#     <br/>
#     
#     (a) Using Python or R, graph $L(x)$ for $L_{\infty} = 20$, for (i) $k = 1$ and (ii) $k = 0.1$.
#     
#     (b) For $k = 1$, find $x$ so that the length is 90\% of $L_{\infty}$. Repeat for 99\% of $L_{\infty}$. Can the fish ever attain length $L_{\infty}$? Interpret the meaning of $L_{\infty}$.
#     
#     (c) Compare the graphs obtained in A. Which growth curve reaches 90\% of $L_{\infty}$ faster? Can you explain what happens to the curve of $L(x)$ when you vary $k$ (for fixed $L_{\infty}$)?  
#     
#     <br/>
#     
# 9. For the following pairs of functions, plot the ratio (quotient) between the two using R or Python. Based on the behaviour of the ratio when $x \rightarrow \infty$ (very large values of $x$), how does each of these functions compare to the other in the velocity that they grow?
# 
#     <br/>  
#     
#     (a) $ f(x) = e^x \quad \text{ and } \quad g(x) = x^2 $
# 
#     (b) $ f(x) = e^x \quad \text{ and } \quad g(x) = x^{20} $
#     
#     (c) $ f(x) = x \quad \text{ and } \quad g(x) = \log(x) $  
#     
#     <br/>
#       
# 10. A community measure that takes both species abundance and species richness into account is the Shannon diversity index $H$. To calculate $H$, the proportion $p_i$ of species $i$ in the community is used. Assume that the community consists of $S$ species. Then
# 
#     $$
#         H = -\sum_{i=1}^S p_i\, \textrm{ln}\, p_i = -( p_1 \textrm{ln}\, p_1 + p_2 \textrm{ln}\, p_2 + \cdots + p_S \textrm{ln}\, p_S )
#     $$
#     
#     <br/>
#     
#     (a) Assume that $S = 5$ and that all species are equally abundant; that is, $p_1 = p_2 = \cdots = p_5$. Compute $H$.
#     
#     (b) Assume that $S = 10$ and that all species are equally abundant; that is, $p_1 = p_2 = \cdots = p_{10}$. Compute $H$.
#     
#     (c) A measure of equitability (or evenness) of the species distribution can be measured by dividing the diversity index $H$ by $\textrm{ln}\, S$. Compute $H/\textrm{ln}\, S$ for $S = 5$ and $S = 10$.
