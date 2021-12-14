#!/usr/bin/env python
# coding: utf-8

# In[24]:


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as plticker

# Create figure and add axes
#fig = plt.figure(figsize=(5, 5))
#ax = fig.add_subplot(111)

fig, ax = plt.subplots(figsize=(5, 5)) 

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


#loc = plticker.MultipleLocator(base=3.0) # this locator puts ticks at regular intervals
#ax.xaxis.set_major_locator(loc)
#loc = plticker.MultipleLocator(base=2.0) # this locator puts ticks at regular intervals
#ax.yaxis.set_major_locator(loc)

x = np.linspace(-3, 3, 100)
y = x**3
ax.plot(x, y, color='b', linewidth=2.5, label=('$f(x) = x^3$'))

ylim = ax.get_ylim()
xlim = ax.get_xlim()

ax.tick_params(axis='both', which='major', labelsize=13)


ax.legend(fontsize=13)
# Add legend

#ax.legend(bbox_to_anchor=(1.05, 0.3),loc='lower left', 
#          frameon=False, labelspacing=0.2, fontsize=13)

plt.tight_layout()
plt.savefig('xcube.png')


# In[25]:


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as plticker

# Create figure and add axes
#fig = plt.figure(figsize=(5, 5))
#ax = fig.add_subplot(111)

fig, ax = plt.subplots(figsize=(5, 5)) 

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


#loc = plticker.MultipleLocator(base=3.0) # this locator puts ticks at regular intervals
#ax.xaxis.set_major_locator(loc)
#loc = plticker.MultipleLocator(base=2.0) # this locator puts ticks at regular intervals
#ax.yaxis.set_major_locator(loc)

x = np.linspace(-3, 3, 100)
y = x**3-(3/2)*x**2-6*x+3
ax.plot(x, y, color='b', linewidth=2.5, label=('$f\,(x)$'))

x = np.linspace(-3, 3, 100)
y = 3*x**2-3*x-6
ax.plot(x, y, color='g', linewidth=2.5, label=('$f\,\'(x)$'))

ylim = ax.get_ylim()
xlim = ax.get_xlim()

ax.tick_params(axis='both', which='major', labelsize=13)


ax.legend(fontsize=15)
# Add legend

#ax.legend(bbox_to_anchor=(1.05, 0.3),loc='lower left', 
#          frameon=False, labelspacing=0.2, fontsize=13)

plt.tight_layout()
plt.savefig('func_diff.png')


# In[31]:


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as plticker

# Create figure and add axes
#fig = plt.figure(figsize=(5, 5))
#ax = fig.add_subplot(111)

fig, ax = plt.subplots(figsize=(5, 5)) 

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


#loc = plticker.MultipleLocator(base=3.0) # this locator puts ticks at regular intervals
#ax.xaxis.set_major_locator(loc)
#loc = plticker.MultipleLocator(base=2.0) # this locator puts ticks at regular intervals
#ax.yaxis.set_major_locator(loc)

x = np.linspace(-3, 3, 100)
y = x**3-(3/2)*x**2-6*x+3
ax.plot(x, y, color='b', linewidth=2.5, label=('$f\,(x)$'))

x = np.linspace(-3, 3, 100)
y = 6*x-3
ax.plot(x, y, color='orange', linewidth=2.5, label=('$f\,\'\'(x)$'))

ylim = ax.get_ylim()
xlim = ax.get_xlim()

ax.tick_params(axis='both', which='major', labelsize=13)


ax.legend(fontsize=15)
# Add legend

#ax.legend(bbox_to_anchor=(1.05, 0.3),loc='lower left', 
#          frameon=False, labelspacing=0.2, fontsize=13)

plt.tight_layout()
plt.savefig('plot_concav.png')


# In[37]:


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as plticker

# Create figure and add axes
#fig = plt.figure(figsize=(5, 5))
#ax = fig.add_subplot(111)

fig, ax = plt.subplots(figsize=(5, 5)) 

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


#loc = plticker.MultipleLocator(base=3.0) # this locator puts ticks at regular intervals
#ax.xaxis.set_major_locator(loc)
#loc = plticker.MultipleLocator(base=2.0) # this locator puts ticks at regular intervals
#ax.yaxis.set_major_locator(loc)

x = np.linspace(-3, 4, 100)

y = (3/2)*x**4-2*x**3-6*x**2+2
ax.plot(x, y, color='b', linewidth=2.5, label=('$f\,(x)$'))

y = 6*x**3-6*x**2-12*x
ax.plot(x, y, color='g', linewidth=2.5, label=('$f\,\'(x)$'))

y = 18*x**2-12*x-12
ax.plot(x, y, color='orange', linewidth=2.5, label=('$f\,\'\'(x)$'))

#ylim = ax.get_ylim()
#xlim = ax.get_xlim()
ax.set_ylim(-50,50)

ax.tick_params(axis='both', which='major', labelsize=13)


ax.legend(fontsize=15)
# Add legend

#ax.legend(bbox_to_anchor=(1.05, 0.3),loc='lower left', 
#          frameon=False, labelspacing=0.2, fontsize=13)

plt.tight_layout()
plt.savefig('plot_extrema.png')


# In[51]:


import matplotlib.pyplot as plt
import numpy as np
    
dens = np.linspace(0,4)

fig, ax = plt.subplots(figsize=(6, 4))


ax.plot(dens,2*dens**2/(1+dens**2))
    
ax.set_xlabel('$N$',fontsize = 16)
ax.set_ylabel('$f\,(N)$',fontsize = 16)

ax.set_yticks([])
ax.set_yticklabels([])

ax.set_xticks([np.sqrt(1/3)])
ax.set_xticklabels([r'$\sqrt{\frac{1}{3ah}}$'],fontsize=16)

ax.axvline(np.sqrt(1/3), ls='--', color='black', lw=0.5)

ax.set_ylim(0, 2)
ax.set_xlim(0, 4)

fig.tight_layout()
fig.savefig('hollingIII.png')


# In[57]:


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as plticker

# Create figure and add axes
#fig = plt.figure(figsize=(5, 5))
#ax = fig.add_subplot(111)

fig, ax = plt.subplots(figsize=(5, 5)) 

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


#loc = plticker.MultipleLocator(base=3.0) # this locator puts ticks at regular intervals
#ax.xaxis.set_major_locator(loc)
#loc = plticker.MultipleLocator(base=2.0) # this locator puts ticks at regular intervals
#ax.yaxis.set_major_locator(loc)

x = np.linspace(-3, 3, 100)
y = np.exp(x)
ax.plot(x, y, color='b', linewidth=2.5, label=('$e^x$'))

y = 1+x
ax.plot(x, y, color='orange', linewidth=2.5, label=('$1+x$'))


ax.tick_params(axis='both', which='major', labelsize=13)


ax.legend(fontsize=15)
ax.set_ylim(-2,10)
# Add legend

#ax.legend(bbox_to_anchor=(1.05, 0.3),loc='lower left', 
#          frameon=False, labelspacing=0.2, fontsize=13)

plt.tight_layout()
plt.savefig('exp_linapp.png')


# # 07 - Analysing change, continuously (Part 2)

# In many different contexts we may be interested in finding the maximum or minimum values a given function may assume. This process is referred to as *optimization*.  
#   
# In Ecology, some of the most common uses for optimization methods are:
# 
# 1 - *Statistical estimation and inference*: optimizing the likelihood of a model and its parameters being true, for a given set of observations.
# 
# 2 - *Resources management*: finding a balance between different wildlife and economic priorities (market, legal, natural constraints)
# 
# 3 - *Optimality theory*: how can the behavioural or life-history trade-offs result in optimal strategies for different organisms

# ## Extreme values of functions  
#   
# For a given function $f(x)$ that is **continuous** in an interval $a \le x \le b$, there will always be a global maximum and a global minimum, points at which the function assumes its maximum and minimum values in the interval.  
# ```{image} extrema.png  
#   
# ```
#   
# A function $f(x)$ presents a *local maximum* value if for a given vicinity of the point $x_0$, $f(x_0)$ is greater than all the other $f(x)$ for $x$ in this vicinity. The analogous definition can be made for a *local minimum* value when $f(x_0)$ is smaller than all the other $f(x)$ in the vicinity. Local minima and local maxima constitue the *local extrema* for $f(x)$, and with the set of all extrema we can find the global maximum and the global minimum.  
#   
# An important result is that, if the function $f$ has a local extremum at a given point $x=c$ in that interval ($a<c<b$) and the derivative of the function exists at that point (in other words, if $f'(c)$ is well defined), then we will have:  
#   
# $f'(c)=0$  
#     
#   
# `````{warning}  
# 
# ````{panels}  
#   
# ```{image} ./xcube.png  
# 
# ```  
# 
# ---  
#   
# Note, however, that the contrary is not always true. If $f'(c)=0$, not necessarily $f(c)$ will be an extremum point. On the left plot, $f(x)=x^3 \implies f'(x)=2x^2$, thus $f'(0)=0$ but there is no extremum at $x=0$ .
#       
# ```` 
# `````  
#   
# Thus the points $x=c$, for which $f'(c)$, will constitute **candidates** for local extrema, and will have to be evaluated under other sets of conditions. Also important to have in mind that point for which the derivative is not definided (kinks or discontinuities) may also constitute local extrema (see on the first figure).  
#   
#   
# In general, when searching for local extrema, we have to adopt the following rules:  
# 
# - Do not assume points $x$ for which $f'(x) = 0$ are extrema. They are candidates.
# - Check points where derivative is not defined.
# - Check endpoints of domain.
#   
#   

# ## Monotonicity and concavity  
#   
# 
# 
# Imagine a function $f(x)$ defined in a given interval $a \le x \le b$. For every $x_1$ and $x_2$ in this interval, if $x_{2} > x_{1}$ implies that $f(x_{2}) > f(x_{1})$ then the function is **increasing** in this interval. If on the other hand, $x_{2} > x_{1}$ implies that $f(x_{2}) < f(x_{1})$ then the function is **decreasing** in this interval.  This can be graphically shown as:  
#   
# ```{image} incr_decr.png  
# ```  
#   
# 
#   
# ```{note}  
# Since we are using the stric inequalities ("$>$" or "$<$") it can be added that the function is **monotonic**, or monotonically increasing or decreasing. If we had $x_{2} > x_{1}$ implying that $f(x_{2}) \ge f(x_{1})$ (or $f(x_{2}) \le f(x_{1})$), the function would be *non-decreasing* (or *non-increasing*).  
#   
# ```
#   
# Now suppose that $f$ is well-behaved in a given interval $a \le x \le b$ (in mathematical terms, we say: $f$ is continuous and differentiable in $(a,b)$), then an important results is that
# 
# $$\mbox{If }\ f'(x) > 0\ \mbox{ for}\ a \le x \le b \implies f(x)\ \mbox{is increasing for}\ a \le x \le b$$
# 
# $$\mbox{If }\ f'(x) < 0\ \mbox{ for}\ a \le x \le b \implies f(x)\ \mbox{is decreasing for}\ a \le x \le b$$  
#   
#   
# In other words, if the derivative of function $f$ is positive (negative) for every point $x$ in a given interval then the function is increasing (decreasing) in this interval.  
#   
# ````{admonition} Example  
# Let us calculate the intervals where the function $f(x) = x^{3} - \displaystyle\frac{3}{2}x^{2} - 6x + 3$ is increasing and decreasing. Since $f(x)$ is continuos and differentiable for all real values of $x$ (remember that all polynomial functions are well-behved), we can use the first derivative test:  
#   
# $$f'(x) = 3x^{2}-3x-6 = 3(x^{2}-x-2) = 3(x+1)(x-2)$$  
#   
# and we see that $f'(x)$ has roots in $x=-1$ and $x=2$. Since $f'(x)$ is a polynomial of degree 2 with the coefficient of the leading term positive, it is *concave up*. From this, we can conclude that:  
#   
# $$x<-1\ \mbox{or}\ x>2 \implies f'(x) > 0 \implies f(x)\ \mbox{is}\ increasing$$  
# $$-1<x<2 \implies f'(x) < 0 \implies f(x)\ \mbox{is}\ decreasing$$  
#   
# The following plot shows the function $f(x)$ and its derivative. Compare the intervals where the derivative is positive (negative) with the intervals where the function $f(x)$ is increasing (decreasing).  
#   
# ```{image} func_diff.png  
# ```  
# 
# ````  
#   
# When we discussed polynomials of degree 2, depending on the sign of the coefficient of the leading term, we had the two cases:  
#   
# ```{image}  concav.png  
# ```
#   
# Let us now generalise the notion of concavity for any arbitrary function. Suppose $f(x)$ is differentiable in a given interval $a \le x \le b$ (in other words, the derivative $f'(x)$ is well-defined for every point in this interval). Then we have the following results:  
#   
# $$\mbox{If }\ f'(x)\ \mbox{is increasing for}\ a \le x \le b \implies f(x)\ \mbox{is}\ concave\ up$$
# 
# $$\mbox{If }\ f'(x)\ \mbox{is decreasing for}\ a \le x \le b \implies f(x)\ \mbox{is}\ concave\ down$$  
#   
# This means that if for a given function $f(x)$ the slopes of the tangent lines are increasing in a given interval of $x$, in this interval the function should resemble an "upwards U-shape". If on the other hand, the slopes of the tangent lines are decreasing in this interval, the function should resemble a "downwards U-shape". This can be visualised on the plots below.  
#   
# ```{image}  slopes_inc_dec.png  
# ```
#   
# If the function $f$ is twice differentiable in $a \le x \le b$ ($f''(x)$ is well-define for $a \le x \le b$), we can use the last two results to find a general criterium for concavity. This will be given by:  
#   
# $$\mbox{If }\ f''(x) > 0\ \mbox{ for}\ a \le x \le b \implies f'(x)\ \mbox{is increasing for}\ a \le x \le b \implies f(x)\ \mbox{is}\ concave\ up$$
# 
# $$\mbox{If }\ f''(x) < 0\ \mbox{ for}\ a \le x \le b \implies f'(x)\ \mbox{is decreasing for}\ a \le x \le b \implies f(x)\ \mbox{is}\ concave\ down$$  
#   
#   
# ````{admonition} Example  
# Let us analyse the function $f(x) = x^{3}-\displaystyle\frac{3}{2}x^{2}-6x+3$ again. We have:  
#   
# $$\begin{align} 
# f'(x) = 3x^{2}-3x-6 \\
# f''(x) = 6x -3 \end{align}$$  
#   
# The function f''(x) has a root in $x=\displaystyle\frac{1}{2}$. Since its slope is positive, we have:  
#   
# $$x<\displaystyle\frac{1}{2} \implies f''(x) < 0 \implies f(x)\ \mbox{is}\ concave\ down$$  
# $$x>\displaystyle\frac{1}{2} \implies f''(x) > 0 \implies f(x)\ \mbox{is}\ concave\ up$$  
#   
# On the plots below, compare the intervals where the second derivative is positive (negative) with the intervals where the function $f(x)$ is concave up (concave down).  
#   
# ```{image}  plot_concav.png  
# ```  
# 
# ````

# ## Finding extrema  
#   
#   
# Back to our strategy for finding maxima or minima of functions, we first determine the set:  
#   
# - find all points $c$ for which $f'(c) = 0$ or all point $c$ where $f'(c)$ does not exist. These are called **critical points**.
# - find endpoints of domain of $f$.  
#   
# Additionally, if $f$ is twice differentiable (in some interval containing $c$):  
#   
# - If $f'(c) = 0$ and $f''(c) < 0 \implies c$ is a local maximum (since the function is concave down)
# - If $f'(c) = 0$ and $f''(c) > 0 \implies c$ is a local minimum (since the function is concave up)  
#   
# ````{admonition} Example  
# Let us analyse the function $f(x) = \displaystyle\frac{3}{2}x^{4}-2x^{3}-6x^{2}+2$, and find its local extrema. We have:  
#   
# $$\begin{align}
# f'(x)&= 6x^{3}-6x^{2}-12x=6x(x-2)(x+1) \\
# f''(x)&=18x^{2}-12x-12=6(3x^{2}-2x-2)\end{align}$$  
#   
# Since this is a polynomial function, the derivative is well-defined for all points. Also, for the critical points (roots of $f'(x)$) we have $x=0$, $x=-1$, and $x=2$. Calculating the value of the second derivative at the critical points:  
#   
# $$\begin{align}
# &x=0 \implies f''(0)=-12 \text{ (local maximum)} \\
# &x=-1 \implies f''(-1)=18 \text{ (local minimum)} \\
# &x=2 \implies f''(2)=36 \text{ (local minimum)}\end{align}$$  
#   
# Now we can check on the plot of $f(x)$ that we have successfully determined the local extrema.  
#   
# ```{image} plot_extrema.png  
# ```
# 
# ````

# ## Inflection points  
#   
#   
# As we saw before, given a function $f(x)$, for some values of $x$, there might be a change in the concavity of the function:  
#   
# ```{image} inflection.png  
# ```
#     
# The points $x$ for where the function changes its concavity are called **inflection points**. If $f$ is twice differentiable and $c$ is an inflection point, then $f''(c)=0$.  
#   
# ```{note}  
# Note again that the points $x=c$ where $f''(c)=0$ are only candidates for inflection points. See that if $f(x)=x^{4}$, $f''(x)=12x^{2}$. Then, $f''(0)=0$, but $x=0$ is not an inflection point of $f$.  
#   
# After calculating the candidate points $x=c$, if the concavities of the function (given by the sign of the second derivative) to the left and to the right of $c$ change, then $c$ is an inflection point.  
# 
# ```  
#   
# ````{admonition} Example  
# 
# Consider the Holling Type III functional response   
#   
# $$f(N)=\frac{aN^{2}}{1+ahN^{2}},$$  
#   
# where $f(N)$ is prey consumption rate per predator, $N$ is the prey population density, $a$ is the attack rate, and $h$ is handling time. Let us check if this function presents any inflection point. We have:  
#   
# $\begin{align}f'(N) 
# &= \frac{2aN(1+ahN^{2})-aN^{2}(2ahN)}{(1+ahN^{2})^{2}} \\
# &= \frac{2aN}{(1+ahN^{2})^{2}}\end{align}$  
#   
# <br />
#   
# $\begin{align}f''(N)
# &=\frac{2a(1+ahN^{2})^{2}-2aN[2(1+ahN^{2})\cdot2ahN]}{(1+ahN^{2})^{4}} \\
# &=\frac{2a(1+2ahN^{2}+a^{2}h^{2}N^{4})-2a[4ahN^{2}+4a^{2}h^{2}N^{4}]}{(1+ahN^{2})^{4}} \\
# &=\frac{2a(1-3ahN^{2})}{(1+ahN^{2})^{3}}\end{align}$  
#   
# See that the function $f''(N)$ has two roots: $N=-\sqrt{\displaystyle\frac{1}{3ah}}$ and $N=\sqrt{\displaystyle\frac{1}{3ah}}$. Since $N$ is a population density, it only makes sense to analyse $N \ge 0$. It is also possible to show that:
#   
# $$N<\sqrt{\displaystyle\frac{1}{3ah}} \implies f''(x) > 0$$  
# $$N>\sqrt{\displaystyle\frac{1}{3ah}} \implies f''(x) < 0$$  
#   
# This means that we have a change of concavity at the point $N=\sqrt{\displaystyle\frac{1}{3ah}}$ and thus this is and inflection point of this curve.  
#   
# Analyse how the function $f(N)$ changes with $N$.  
#   
# ```{image} hollingIII.png  
# ```
#   
# How does this function compares with the Holling type II functional response?
# 
# ````  
#   
# ```{tip}  
#   
# For the intervals where the function is concave up you can also think of it as representing "accelerated change" of that function (since the first derivative, the "velocity" is increasing), while the intervals where it is concave down represent "deccelerated change" of the function. Understanding this can be particularly important if you function has a specific biological meaning, as in the previous example.  
#   
# ```

# ## Series expansions 
#   
# From the formal definition of a derivative  
#   
# $$f'(a)= \lim_{x \to a} \frac{f(x)-f(a)}{(x-a)} \xrightarrow{\text{$x$ very close to $a$}} f'(a) \approx \frac{f(x)-f(a)}{(x-a)},$$  
#   
# which means that if $x$ is sufficiently close to $a$, the average rate of change is sufficiently close to the value of the derivative at that point. From the previous approximation, we have:  
#   
# $$f(x) = f(a)+f'(a)(x-a),$$  
#   
# which provides a linear approximation of $f(x)$ around $a$ (see that if $\alpha= f(a)$ and $\beta=f'(a)$, both constants, then $f(x) = \alpha+\beta(x-a)$, which can easily be arranged on the form $y=mx+b$).  
#   
# `````{admonition} Example  
#   
# ````{panels}  
#   
# ```{image} ./exp_linapp.png
# 
# ```  
# 
# ---  
#   
# Say we have $f(x)=e^{x}$ and we want to use this linear expression to approximate the function close to $a=0$: 
# 
# $$f(x)=f(0)+f'(0)(x-0)=1+x,$$  
#   
# since $f'(x) = e^{x}$ and thus $f(0)=f'(0)=1$.  
#   
# The approximation is reasonable if $x$ very close to $0$, but fails when $x$ increasingly departs from $0$. 
#   
# ````  
#   
# `````

# One way of trying to make the approximation better is to add terms of higher order of $x$. Suppose we want to approximate the function $f(x)$ at point $a$ by a given polynomial of degree $n$  
#   
# $$P(x)=a_{0}+a_{1}(x-a)+a_{2}(x-a)^{2}+\cdots+a_n(x-a)^{n}$$  
#   
# so that the derivatives of $f(x)$ and $P(x)$ are the same at $x=a$:
# 
# $$\begin{align}f(a)&=P(a) \\
# f'(a)&=P'(a)\\
# &\vdots \\
# f^{(n)}(a)&=P^{(n)}(a)\end{align}.$$  
#   
# But for the polynomial, we have:  
#   
# $$\begin{align}  
# P(a)&=a_{0} \\
# P'(a)&=1 \cdot a_{1} \\
# P''(a)&=2 \cdot 1 \cdot a_{2} \\
# P'''(a)&=3 \cdot 2 \cdot 1 \cdot a_{3} \\  
# P''''(a)&=4 \cdot 3 \cdot 2 \cdot 1 \cdot a_{4} \\
# &\vdots \\
# P^{(n)}(a)&= \underbrace{n(n-1)(n-2) \cdots 3 \cdot 2 \cdot 1}_{\displaystyle\text{$$n!$$}}\cdot a_{n} \end{align}$$  
#   
# where $n! = n\cdot(n-1)\cdot(n-2) \cdots 3 \cdot 2 \cdot 1$ is the factorial of $n$.  
#   
# Thus, by making derivatives of $f(x)$ and $P(x)$ equal at $x=a$, we obtain: 
#   
# $$f^{(n)}(a) = P^{(n)}(a) \implies f^{(n)}(a) = n!\, a_n \implies a_{n} = \frac{f^{(n)}(a)}{n!}$$  
#   
# The polynomial with these coefficients is called **Taylor polynomial** of degree $n$ at $x = a$:  
#   
# $$P(x)=f(a)+f'(a)(x-a)+\frac{f''(a)}{2!}(x-a)^{2}+\cdots+\frac{f^{(n)}(a)}{n!}(x-a)^{2}.$$  
#   
# ````{admonition} Example  
#   
# To find approximation of degree 3 for $f(x)=e^{x}$, at $x=0$, we have:  
#   
# $$f(0)=1 \\
# f'(0)=1 \\
# f''(0)=1 \\
# f'''(0)=1$$  
#   
# Thus, 
#   
# $$P_{3}(x)=1+(x-0)+\frac{1}{2!}(x-0)^2+\frac{1}{3!}(x-0)^3=1+x+\frac{x^2}{2}+\frac{x^3}{6}$$  
#   
# See how the approximation to the function $f(x)=e^{x}$  at $x=0$ gets increasingly better when more terms are added to the polynomial.  
#   
# ```{image} exp_series.gif  
# ```
#   
# ````  
#   
#   
# ```{admonition} Example  
# For the function $f(x)=\displaystyle\frac{1}{1-x}\ (x\neq1)$ at $x=0$, we have:  
#   
# $$f(x)=\frac{1}{1-x} \implies f(0)=1 \\
# f'(x)=\frac{1}{(1-x)^{2}} \implies f'(0)=1 \\
# f''(x)=\frac{2}{(1-x)^{3}} \implies f''(0)=2 \\
# f'''(x)=\frac{3\cdot2}{(1-x)^{4}} \implies f'''(0)=3! \\
# f^{(n)}(x)=\frac{n!}{(1-x)^{n+1}} \implies f^{(n)}(0)= n!$$  
#   
# Thus the Taylor polynomial of degree $n$ will be:  
#   
# $$\begin{align}P(x)
# &=1+1(x-0)+\frac{2}{2}(x-0)^{2}+\frac{3!}{3!}(x-0)^{3}+\cdots+\frac{n!}{n!}(x-0)^{n} \\
# &=1+x+x^{2}+x^{3}+\cdots+x^{n}\end{align}$$
# 
#   
# ```  
#   
# For some functions, the approximation $f(x)=P_n(x)$ at a given reference point $x=a$ can be made increasingly better by adding more terms to $P(x)$, so that in the limit $n\rightarrow \infty$ the Taylor polynomials (called **Taylor series** in this limit) for the functions $e^{x}$, $\mbox{sin}(x)$, $\mbox{cos}(x)$ converge exactly for all values of $x$. For other functions, such as $\mbox{ln}(1+x)$ and $\displaystyle\frac{1}{1-x}$, there is a restricted range of values of $x$ for which the approcximation can be made better by adding terms.  
#   
# We have the following approximations by Taylor series, with ranges in $x$, at $x = 0$:
# 
# $$e^x=1+x+\frac{x^2}{2}+\frac{x^3}{3!}+\cdots+\frac{x^n}{n!}+O_{n+1}(x),\ -\infty<x<\infty$$
# 
# $$\mbox{sin}(x)=x-\frac{x^3}{3}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots+(-1)^n\frac{x^{2n+1}}{(2n+1)!}+O_{2n+3}(x),\ -\infty<x<\infty$$
# 
# $$\mbox{cos}(x)=1-\frac{x^2}{2}+\frac{x^4}{4!}-\frac{x^6}{6!}+\cdots+(-1)^n\frac{x^{2n}}{(2n)!}+O_{2n+2}(x),\ -\infty<x<\infty$$
# 
# $$\mbox{ln}(1+x)=x-\frac{x^2}{2!}+\frac{x^3}{3!}-\frac{x^4}{4!}+\frac{x^5}{5!}+\cdots+(-1)^{n+1}\frac{x^n}{n!}+O_{n+1}(x),\ -1 < x \leq 1$$
# 
# $$\frac{1}{1-x}=1+x+x^2+x^3+\cdots+x^n+O_{n+1}(x),\ -1 \leq x < 1$$  
#   
# where the notation $O_{m}(x)$ represents the terms of order $n\ge m$ that belong to this (infinite) sum but are not explicitly shown.
