#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Codes for figures

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def multiple_formatter(denominator=2, number=np.pi, latex='\pi'):
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    def _multiple_formatter(x, pos):
        den = denominator
        num = np.int(np.rint(den*x/number))
        com = gcd(num,den)
        (num,den) = (int(num/com),int(den/com))
        if den==1:
            if num==0:
                return r'$0$'
            if num==1:
                return r'$%s$'%latex
            elif num==-1:
                return r'$-%s$'%latex
            else:
                return r'$%s%s$'%(num,latex)
        else:
            if num==1:
                return r'$\frac{%s}{%s}$'%(latex,den)
            elif num==-1:
                return r'$\frac{-%s}{%s}$'%(latex,den)
            else:
                return r'$\frac{%s%s}{%s}$'%(num,latex,den)
    return _multiple_formatter

class Multiple:
    def __init__(self, denominator=2, number=np.pi, latex='\pi'):
        self.denominator = denominator
        self.number = number
        self.latex = latex

    def locator(self):
        return plt.MultipleLocator(self.number / self.denominator)

    def formatter(self):
        return plt.FuncFormatter(multiple_formatter(self.denominator, self.number, self.latex))

xt=np.linspace(-4*np.pi,4*np.pi,num=500)
##
fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(xt, np.sin(xt), color='b', lw=2, label='$sin(x)$')
ax.plot(xt, np.cos(xt), color='g', lw=2, label='$cos(x)$')
ax.tick_params(axis='both', labelsize= 15)
ax.set_xlabel('$x$', fontsize = 16)
ax.legend(fontsize=14)

ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)

ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 12))
ax.xaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))

fig.tight_layout()
fig.savefig('sin_cos.png')

##
xt=np.linspace(-2*np.pi,2*np.pi,num=500)
fig, ax = plt.subplots(figsize=(4, 3))
y = np.tan(xt)
y[:-1][np.diff(y) < 0] = np.nan

ax.plot(xt,y, color ='r', lw=2)
ax.tick_params(axis='both', labelsize= 15)

ax.set_xlabel('$x$', fontsize = 16)
ax.set_ylabel("$tan(x)$", fontsize = 16)

plt.ylim(-10,10)
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)

ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 12))
ax.xaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))

fig.tight_layout()
fig.savefig('tan.png')


# In[3]:


from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return x**3

def htrans(c):
    x = np.linspace(-3,3)
    
    y = func(x+c) #constant c in the argument of the function
    
    plt.plot(x,y, label='$f\, (x+c)$')
    plt.title('Horizontal translation')
        
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(fontsize=12)
    
    plt.ylim(-8, 8) #remember to change the limits for better visualisation if necessary
    
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    
    

    plt.show()

def vtrans(c):
    x = np.linspace(-3,3)
    
    y = func(x)+c #constant c summing the whole function
    
    plt.plot(x,y,  label='$f\, (x)+c$')
    plt.title('Vertical translation')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(fontsize=12)
    
    plt.ylim(-8, 8) #remember to change the limits for better visualisation if necessary
        
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    
    plt.show()
    
# create a slider

interact(htrans, c=(-2.0,2.0))
interact(vtrans, c=(-2.0,2.0))


# In[6]:


from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return x**3-2*x

def hstetcom(c):
    x = np.linspace(-3,3)
    
    y = func(c*x) #constant c multiplying the argument of the function
    
    plt.plot(x,y, label='$f\, (cx)$')
    plt.title('Horizontal stretching/compression')
        
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(fontsize=12)
    
    plt.ylim(-4, 4) #remember to change the limits for better visualisation if necessary
    
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    
    

    plt.show()

def vstetcom(c):
    x = np.linspace(-3,3)
    
    y = c*func(x) #constant c multiplying the whole function
    
    plt.plot(x,y,  label='$c\, f\, (x)$')
    plt.title('Vertical stretching/compression')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(fontsize=12)
    
    plt.ylim(-4, 4) #remember to change the limits for better visualisation if necessary
        
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    
    plt.show()
    
# create a slider

interact(hstetcom, c=(0.1,2.0))
interact(vstetcom, c=(0.1,2.0))


# In[48]:


fig, ax = plt.subplots(1,2,figsize=(10, 5))

xt = np.linspace(-3,5)

# x-axis reflection
ax[0].plot(xt, (xt-1)**2, color ='r', lw=2, label = '$(x-1)^2$')
ax[0].plot(xt, -(xt-1)**2, color ='b', lw=2, label = '$-(x-1)^2$')
ax[0].tick_params(axis='both', labelsize= 12)

ax[0].set_xlabel('$x$', fontsize = 14)
ax[0].set_ylabel("$y$", fontsize = 14)

ax[0].set_title('x-axis reflection')

ax[0].set_ylim(-10,10)

ax[0].legend()

ax[0].axhline(0, color='black', lw=1)
ax[0].axvline(0, color='black', lw=1)

# y-axis reflection

xt = np.linspace(-4,4)

ax[1].plot(xt, (xt-1)**2, color ='r', lw=2, label = '$(x-1)^2$')
ax[1].plot(xt, (-xt-1)**2, color ='b', lw=2,  label = '$[(-x)-1]^2$')
ax[1].tick_params(axis='both', labelsize= 12)

ax[1].set_xlabel('$x$', fontsize = 14)
#ax[1].set_ylabel("$y$", fontsize = 14)

ax[1].set_title('y-axis reflection')

ax[1].set_ylim(-1,10)

ax[1].legend()

ax[1].axhline(0, color='black', lw=1)
ax[1].axvline(0, color='black', lw=1)

fig.tight_layout()
fig.savefig('reflection.png')


# In[91]:


import matplotlib.pyplot as plt
import numpy as np
    
time = np.linspace(0,15)
rat = 0.5 + ((1-0.5)/10)*time

fig, ax = plt.subplots(figsize=(6, 4))


ax.plot(time,rat)
    
ax.set_xlabel('$N_t$',fontsize = 16)
ax.set_ylabel(r'$\frac{N_t}{N_{t+1}}$',fontsize = 22)

ax.set_yticks([0.5,1])
ax.set_yticklabels(['$1/R$','1'],fontsize=14)

ax.set_xticks([0,10])
ax.set_xticklabels(['0','K'],fontsize=14)

ax.axhline(1, ls='--', color='black', lw=0.5)
ax.axvline(10, ls='--', color='black', lw=0.5)

ax.set_ylim(0, 1.5)
ax.set_xlim(0, 15)

fig.tight_layout()
fig.savefig('parent-offspring.png')


# In[89]:


import matplotlib.pyplot as plt
import numpy as np

lisg1=[]
lisg2=[]
lisg3=[]

n0g1=1
n0g2=1
n0g3=1

lisg1.append(n0g1)
lisg2.append(n0g2)
lisg3.append(n0g3)

vect = range(1,25)
for t in vect:
    n0g1=1.1*n0g1
    lisg1.append(n0g1)
    
    n0g2=1*n0g2
    lisg2.append(n0g2)
    
    n0g3=0.9*n0g3
    lisg3.append(n0g3)

fig, ax = plt.subplots(figsize=(6, 4))
time = range(25)

ax.scatter(time,lisg1,  label='$R>1$')
ax.scatter(time,lisg2,  label='$R=1$')
ax.scatter(time,lisg3,  label='$0<R<1$')
    
ax.set_xlabel('t',fontsize = 16)
ax.set_ylabel('$N_t$',fontsize = 16)

ax.tick_params(
    axis='both',          
    which='both',      
    bottom=False,      
    left=False,
    labelbottom=False,labelleft=False)



#plt.yticks([0,1],['0','K'],fontsize = 13)
#plt.axhline(1, ls='--', color='black', lw=0.5)

ax.set_ylim(0, 5)

ax.legend(fontsize=12)

fig.tight_layout()
fig.savefig('expgrowth.png')


# In[90]:


import matplotlib.pyplot as plt
import numpy as np

lisg1=[]
lisg2=[]
lisg3=[]

n0g1=0.1
n0g2=0.8
n0g3=1.4

lisg1.append(n0g1)
lisg2.append(n0g2)
lisg3.append(n0g3)

vect = range(1,16)
for t in vect:
    n0g1=1.5*n0g1/(1+((1.5-1)/1)*n0g1)
    n0g2=1.5*n0g2/(1+((1.5-1)/1)*n0g2)
    n0g3=1.5*n0g3/(1+((1.5-1)/1)*n0g3)
    
    lisg1.append(n0g1)
    lisg2.append(n0g2)
    lisg3.append(n0g3)
    
time = range(16)

fig, ax = plt.subplots(figsize=(6, 4))

ax.scatter(time,lisg1)
ax.scatter(time,lisg2)
ax.scatter(time,lisg3)
    
ax.set_xlabel('t',fontsize = 16)
ax.set_ylabel('$N_t$',fontsize = 16)

ax.tick_params(
    axis='x',          
    which='both',      
    bottom=False,      
    top=False,
    labelbottom=False)


ax.set_yticks([0,1])
ax.set_yticklabels(['0','K'],fontsize=12)
ax.axhline(1, ls='--', color='black', lw=0.5)

ax.set_ylim(0, 1.5)

fig.tight_layout()
fig.savefig('logistic.png')


# In[ ]:





# # 03   - Analysing change, one step at a time
#   

# Imagine a colony of wasps is founded by a queen with the following pattern of eggs laid:  
# 
# <br />  
#     
# | Days     |  Eggs  |
# |----------|:------:|
# | $0$      |  $100$ |
# | $1$      |  $135$ |
# | $2$      |  $170$ |
# | $3$      |  $205$ |
# | $4$      |  $240$ |  
#     
# 
# Since there is an additive pattern for the increase in the total number of eggs laid, with the number of eggs in any given day, we can determine the number of eggs the colony will have in the following day. If we index the days by a sequence of natural numbers *n*, we have for the above colony:  
#   
# $$a_{n+1} = a_{n} + 35,$$  
#   
# where $a_n$ represents the total amount of eggs in a given day $n$ and $a_{n+1}$ the same variable on the day following day $n$. The constant $35$ represents the daily increment (or decrement) on this total number. A sequence of number built with constant additive increments receives the name of *arithmetic progression*.  
#   
# The above expression defines an iterative process (also known as a *recursion*) with which we can construct the whole sequence starting from a single initial value. If we want to know how many eggs will have been laid on a given day $n$, this shall be given by the expression:  
#   
# $$a_n = 100 + 35n.$$  
#   
# Thus, the total amount of eggs laid on day $n=100$ is $a_{100} = 100 + 35 \cdot 100 = 3600$.  
#   
# <br />
# <br />
# Now imagine a single *Escherichia coli* cell put on a Petri dish with a favorable growth medium. If given the right conditions, *E. coli* cells divide, generating two other cells, in a time of approximately $30$ minutes. For our experiment, we would have:  
# 
# <br />  
#     
# | Minutes  |  # cells  |
# |----------|:------:|
# | $0$      |  $1$ |
# | $30$      |  $2$ |
# | $60$      |  $4$ |
# | $90$      |  $8$ |
# | $120$      |  $16$ |  
#   
#     
# If $t$ represents the number of reproduction intervals since the start of the experiment (assuming values $t=0, 1, 2, \ldots$), then we can construct the recursion:  
#   
# $$N_{t+1} = 2N_t,$$  
#   
# where $N_t$ represents the number of *E. coli* cells after $t$ intervals of reproduction (each interval corresponding to $30$ minutes) and $N_{t+1}$ represents the number of cells on the interval following $t$. See that this time the constant $2$ provides a multiplicative increment, so that the sequence formed by this multiplicative iteration is called *geometric progression*.  
#   
# If we want $N_t$ for a given interval $t$, we then have:  
#   
# $$N_t = 2^t,$$
#     
# leading to an exponential growth in discrete steps.  
#   
# In general, if we have a population growth described by a geometric progression, starting with a number of individuals $N_0$, the number of individuals on the subsequent generations can be described by the recursion:  
#   
# $$N_{t+1} = RN_t,$$  
#   
# where $t$ indicates the number of generations and $R$ is a positive constant ($R>0$).  
#   
# With this recursion, starting from $N_0$, we can obtain the full sequence by construction:  
#   
# $$\begin{align}  
# N_1 &= RN_0 \\
# N_2 &= RN_1 = R(RN_0) = R^2N_0 \\
# N_3 &= RN_2 = R(RN_1) = R[R(RN_0)] = R^3N_0 \\
#     &\vdots \end{align}$$  
#   
# From this process of construction, we can obtain what we call the *solution* of the above recursion, given by:  
#   
# $$N_t = N_0R^t.$$  
#   
# In problems of population dynamics, $R$ is called **growth constant** and its value determines the long-term behaviour of the function:  
#   
# ```{image} expgrowth.png
# ```

# ## Sequences  
#   
# The two last problems are examples of *sequences* for which a formal definition is given as:  
#   
# $$\begin{align}
#     f\!:\ &{\rm I\!N} \rightarrow {\rm I\!R} \\
#        & n \rightarrow f(n),\end{align}$$  
#          
# in other words, a sequence is a function $f$ from the set of natural numbers to the set of real numbers. For each value of the independent variable $n$ (a natural number), the sequence determines its image $f(n)$.  
#   
# ```{admonition} Example  
# The sequence defined by the rule $f(n) = \displaystyle\frac{1}{n+1}$ defines the sequence of numbers (starting from $n=0$):  
#   
# $$1,\frac{1}{2},\frac{1}{3},\frac{1}{4},\frac{1}{5},\ldots,$$  
#   
# corresponding to the set of values $n=0,1,2,3,4,\ldots$.
# ```  
#   
#   
# 
# Sequences are usually written as ordered lists of numbers $a_0, a_1, a_2, a_3, \ldots$ where $a_n=f(n)$ and referred to with the notation $\{a_n\}$ (which is short for $\{a_n: n \in {\rm I\!N}\}$, making it explicit that $n$ is a natural number).  
#   
# As we have seen before, two forms of representation are possible:  
#   
# ````{panels}
# **Explicit description**
# ^^^
# $$a_n=f(n)$$  
#   
# ```{admonition} Examples  
# $$a_n = 100 + 35n$$  
# $$a_n = 100\cdot2^n$$  
# $$a_n = \frac{4n^2-1}{n^2}$$  
# $$a_n = \mbox{cos}\left(\displaystyle\frac{3\pi n}{2}\right)$$
# ```
# +++
# In this case, any term $a_n$ of arbitrary index $n$ can be obtained by direct calculation if we know the function $f(n)$. 
# ---
# 
# **Recursive description**
# ^^^
# $$a_{n+1}=g(a_n)$$  
#   
# ```{admonition} Examples  
# $$a_{n+1} = a_n + 35,\ \ \ \mbox{with}\ a_0 = 100$$  
# $$a_{n+1} = 2a_n,\ \ \ \mbox{with}\ a_0=100$$  
# $$a_{n+1} = \frac{3}{a_n},\ \ \ \mbox{with}\ a_0=2$$ 
# ```  
#   
# The recursive description is also called *difference equation*.
# +++
# Note that with the form $a_{n+1}=g(a_n)$ the following term $a_{n+1}$ can be determined only with the term one step back $a_n$, knowing the function $g$. In general, recursions can be dependent on several other backward terms. When it depends only on the immediate previous term it is called a **first-order** recursion. 
# ````

# ## Limits  
#   
#   
# In many applications, we are interested to know what is the *long-term behaviour* of a given sequence $\{a_n\}$. For example, is a given population tending towards a stable number of individuals as time passes? In other words, we want to know if there is a number $L$ for which the sequence tends to as $n$ increases. To represent this we use the followinf notation:  
#   
# $$\lim_{n\rightarrow \infty} a_n = L\ \ (\mbox{or simply}\ \lim a_n =L)$$  
#   
# If such a number exists, we say that the sequence $\{a_n\}$ is **convergent**.  
#   
# ```{admonition} Examples  
# 1. $a_n = \displaystyle\frac{1}{n+1}: \ \ \ \left\{1,\displaystyle\frac{1}{2},\displaystyle\frac{1}{3},\displaystyle\frac{1}{4},\displaystyle\frac{1}{5},\ldots\right\}$  
#     <br />
#     Note that each term is smaller than the previous and they are all positive. We can conclude that:  
#   
#     $$\lim a_n = 0.$$  
# 
# 2. $b_n = (-1)^n: \ \ \ \left\{1,-1,1,-1,1,-1,\ldots\right\}$  
#     <br />
#     The terms in this sequence are alternating between $1$ and $-1$, never convergeing for a specific value. Thus, the limit of sequence $\{b_n\}$ does not exist.  
#     <br />
# 3. $c_n = 2^n: \ \ \ \left\{1,2,4,8,16,32,\ldots\right\}$  
#     <br />
#     For this sequence, the terms are ever increasing. We frequently say that the sequence tends to infinity (or tends to $\infty$). However, $\infty$ represents an abstraction ("ever increasing"), not a specific number. Therefore, the limit for this sequence also does not exist.  
#     <br />
# 4. $d_n = \displaystyle\frac{n+2}{n+1}: \ \ \ \left\{2,\displaystyle\frac{3}{2},\displaystyle\frac{4}{3},\displaystyle\frac{5}{4},\displaystyle\frac{6}{5},\ldots\right\}$  
#     <br />
#     For this sequence, each term is smaller than the previous (look at the decimal forms of the fractions: $2, 1.5, 1.333\cdots, 1.25, 1.2 \ldots$) and they are greater than $1$. We can conclude that:  
#   
#     $$\lim a_n = 1.$$  
#   
# ```  
#   
# Although there is a formal way to *prove* that a sequence $\{a_n\}$ converges to a certain limit, in practice we use a set of rules to apply limits to sequences and composition of sequences.  
#   
# ```{tip}  
# Consider two sequences $\{a_n\}$ and $\{b_n\}$, and $C$ as a real constant. If these two sequences are convergent with  $\lim a_n = L$ and $\lim b_n = M$, we have:  
#   
# $$\lim (a_n + b_n) = \lim a_n + \lim b_n = L + M$$  
# $$\lim (Ca_n) = C\lim a_n = CL$$  
# $$\lim (a_nb_n) = (\lim a_n)(\lim b_n) = LM$$  
# $$\lim \left(\frac{a_n}{b_n}\right) = \frac{\lim a_n}{\lim b_n} = \frac{L}{M},\ \ (\mbox{if}\ M \ne 0)$$
#   
# In other other words, if you can decompose a given sequence into the sum, product or division of two other convergent sequences, the limit of this sequence will be the composition of the limits of the two others.
# ```  
#   
# ```{admonition} Examples  
# If $a_n = \displaystyle\frac{4n^2-1}{n^2}:$  
#   
# $$\lim\left(\displaystyle\frac{4n^2-1}{n^2}\right) = \lim\left(4-\displaystyle\frac{1}{n^2}\right) = \lim 4 - \left(\lim\displaystyle\frac{1}{n}\right)\left(\lim\displaystyle\frac{1}{n}\right) = 4,$$  
#   
# since as we know: $\ \lim 4 = 4\ $ and $\ \lim \displaystyle\frac{1}{n} = 0$.
# 
# ```  
#   
# For recursions, one way to find the limit is to find the solution (corresponding explicit description) and then calculate the limit of the sequence with the limit rules. However, finding the explicit form of a given sequence is not always possible.  
#   
# There is a procedure to find *candidates* for the long-term behaviour of a given sequence. We do this by calculating **fixed points**.  
#   
# Fixed points are specific values on a given sequence for which all subsequent values equal the first. That is, if $a$ is a fixed point of the sequence $\{a_n\}$, and if $a_0 = a$, then $a_1 = a$, $a_2 = a$, and all the other values will be $a$. Thus, given the recursion $a_{n+1} = g(a_n)$, if $a$ is a fixed point we will have:  
#   
# $$a = g(a)$$  
#   
# and the last equation provides a way of find possible values of $a$.  
#   
# ```{admonition} Example  
#   
# Consider the following recursion  
#   
# $$a_{n+1} = \sqrt{3a_n},\ \ \ a_0 = 2.$$  
#   
# To obtain the fixed points we calculate:  
#   
# $$\begin{align}
#   a &= \sqrt{3a} \\
#   a^2 &= 3a \ \ \longrightarrow a = 0\ \mbox{ or }\ a = 3 \end{align}$$  
#   
# Starting with $a_0 = 2$, we can use the recursion to construct the sequence as:  
#   
#   $$\left\{\sqrt{6},\sqrt{3\sqrt{6}},\sqrt{3\sqrt{3\sqrt{6}}},\sqrt{3\sqrt{3\sqrt{3\sqrt{6}}}},\ldots \right\}$$  
#     
# or also: $\{2.449\cdots,2.711\cdots,2.852\cdots,2.925\cdots, \ldots\}$. We see that starting with $a_0=2$, we have $a_n>2$ for all $n$, with increasing values. Since $a=3$ is a fixed point, we conclude that $\lim a_n = 3$.  
# ```  
#   
# ```{warning}  
#   
# Remember that fixed points are only **candidates** for long-term behaviour. See for example the recursion:  
#   
# $$a_{n+1} = \displaystyle\frac{3}{a_n}$$  
#   
# For the fixed points, we calculate:  
#   
# $$\begin{align}
#   a &= \displaystyle\frac{3}{a} \\
#   a^2 &= 3 \\
#   &\longrightarrow a = -\sqrt{3}\ \mbox{ or }\ a = \sqrt{3}. \end{align}$$  
#     
# Indeed, if we construct the sequence from the recursion starting with any of these two values, all the subsequent elements of the sequence will have the same value. However:  
#   
# $$\mbox{if } a_0 = 2 \ \mbox{the sequence will be given by: }\ \left\{2,\displaystyle\frac{3}{2},2,\displaystyle\frac{3}{2},\ldots \right\}$$  
#   
# or  
#   
# $$\mbox{If } a_0 = -3 \ \mbox{the sequence will be given by: }\ \left\{-3,-1,-3,-1,\ldots \right\}$$  
#   
# showing that for any initial value chosen (different from the fixed points), the sequence will oscillate between two values, without a clear tendency to any limit.
# ```
# 

# ## Discrete-time population models  
#   
# Sequences are generally used in many applications in Biology. Important examples are models for **seasonally breeding** populations.  
#   
#   
# ### Density-dependent population growth  
#   
# As we have seen before, the recursion relation for the exponential growth model is given by $N_{t+1} = RN_t$. Rearranging the terms of this equation we have:  
#   
# $$\displaystyle\frac{N_t}{N_{t+1}}=\frac{1}{R}.$$  
#   
# The left-hand term of the last equation is known as *parent-offspring ratio* as it denotes the ratio between the population size at time $t$ (parents) and the population size at the following time $t+1$ (offspring). Here we are considering a population that breeds without overlapping generations. Each generation breeds, dies, and is replaced by their offspring on the following generation.  
#   
# On the equation we also see that the parent-offspring ratio is equal to $\displaystyle\frac{1}{R}$, which is a constant. Therefore, we say that this growth is *density-independent* as the parent-offspring ratio does not depend on the density of individuals at any time step. Relating the parent-offspring ratio to the value of $R$ allows us to predict the behaviour of this population in terms of growth or decline:  
#   
# $$\begin{align}
# R>1 \ &- \ \mbox{there will be more offspring than parents (population grows)} \\
# R<1 \ &- \ \mbox{there will be more parents than offspring (population declines)} \\
# R=1 \ &- \ \mbox{there will be no change in population size} \end{align}$$
#   
# We know, however, than in real scenarios, that the growth factor of a given population should depend on the current size of that population, due to space or resources limitation. These are called *density-dependent* effects. One of the simplest methods to include density-dependent effects in this population model is to consider the parent-offspring ratio as a linear function of $N_t$, instead of a constant. Let us assume that the parent-offspring ratio show the following linear behaviour:  
#   
# ```{image} parent-offspring.png
# ```  
#   
# This means that the parent-offspring ratio is smaller than $1$ (population growth) for values of $N_t$ smaller than a given population threshold $K$, and greater than $1$ (population decline) if the population size is greater than this threshold. The graph above leads to the following expression:  
#   
# $$\begin{align}
# \displaystyle\frac{N_t}{N_{t+1}} = \frac{1}{R} + \frac{1-\frac{1}{R}}{K}N_t \\
# N_{t+1} = \frac{N_t}{\frac{1}{R} + \frac{1-\frac{1}{R}}{K}N_t}, \end{align}$$  
#   
# which leads, after rearranging the terms, to:  
#   
# $$N_{t+1} = \frac{RN_t}{1 + \frac{(R-1)}{K}N_t}.$$  
#   
# The previous expression is known as **Beverton-Holt recruitment curve** (or Beverton-Holt model) and it describes a type of population growth called *logistic growth*.  
#   
# The fixed points $\bar{N}$ for this recursion can be calculated as:  
#   
# $$\bar{N} = \frac{R\bar{N}}{1 + \frac{(R-1)}{K}\bar{N}}\ \longrightarrow \ \bar{N}\left(1 + \frac{(R-1)}{K}\bar{N}\right) = R\bar{N}$$  
#   
# From the last term we can show (try it as an exercise) that $\bar{N}=0$ and $\bar{N}=K$ are the two fixed points. Starting from different values for the initial population size $N_0$ it can be shown that the population tends to $K$ as time increases as:  
#   
# ```{image} logistic.png
# ```  
#   
# The constant $K$ is know as *carrying capacity* and represents the maximum population size a given population can reach at a given place, due to intra-specific competition for resources or space.  
#   
#   
# Watch this [video](https://www.youtube.com/watch?v=Kas0tIxDvrg) about application of growth models to epidemics.  
#   
#   
# ### Annual plants  
#   
#   
# Suppose a given population of plants produces, on average $f$ seeds per individual in the reproductive period. Seeds survive winter with a probability $\sigma$ and germinate on the next season with probability $\alpha$ (these seeds reach reproductive maturity on the same season). If $p_n$ is the plant population size on season $n$ and $p_{n+1}$ the population size on the season following $n$, we shall have:  
#   
# $$p_{n+1} = (\alpha\sigma f)p_n$$  
#   
# which correspond to the density-independent model since $R=\alpha\sigma f$ is a constant.  
#   
# Now suppose that some of the seeds that were produced on the previous season and survived the previous winter, but did not germinate on the current season, might have a second chance of germinating. They might do so on the following season, provided they survive the winter and germinate on the following season. From the average number of seeds produced last season $fp_{n-1}$, a number $\sigma fp_{n-1}$ of them survived last winter. From this number, a fraction $(1-\alpha)$ did not germinate this season (1 minus the probability of germinating). These seeds will have a second chance provided they survive next winter (with probability $\sigma$) and germinate on the next season (with probability $\alpha$). Thus, the number plant population size on the season following $n$ will be:  
#   
# $$\begin{align}
# p_{n+1} = \alpha\sigma fp_n + \alpha\sigma(1-\alpha)\sigma fp_{n-1} \\  
# p_{n+1} = (\alpha\sigma f)p_n + [\alpha(1-\alpha)\sigma^2 f]p_{n-1} \\  
# p_{n+1} = \beta p_n + \gamma p_{n-1}\end{align}$$  
#   
# where $\beta=\alpha\sigma f$ and $\gamma = \alpha(1-\alpha)\sigma^2 f$.  
#   
# The previous model is an example of a discrete population model with overlapping populations. Since the term $n+1$ depends not only on the term $n$ but also on $n-1$ this is called a *second-order difference equation* or *delay (or lagged) difference equation*.  
#   
#   
# ### Fibonacci sequence  
#   
#   
# The Fibonacci sequence is a sequence defined by the following rule: each number is equal to the sum of the previous two numbers (starting with $0$ and $1$). Thus the following sequence might be formed:  
#   
# $$\left\{ 0,1,1,2,3,5,8,13,21,\ldots \right\}. $$  
#   
# It can also be defined by the second-order difference equation:  
#   
# $$F_{n+1} = F_{n} + F_{n-1}.$$  
#   
# Although this is clearly not a convergent sequence (with sustained growth for each element), if we define a new sequence given by the ratio between successive elements of the Fibonacci sequence as $b_n = \displaystyle\frac{F_{n+1}}{F_n}$, it can be show that this sequence is convergent.  
#   
# Assuming that $\lim \displaystyle\frac{F_{n+1}}{F_n} = \lambda$, we have:  
#   
# $$\begin{align}
# F_{n+1} &= F_{n} + F_{n-1}\quad \mbox{(Fibonacci seq.)} \\  
# \displaystyle\frac{F_{n+1}}{F_{n}} &= 1 + \frac{F_{n-1}}{F_{n}}\quad \mbox{(divide both sides by}\ F_{n}\mbox{)} \\
# \lim \left(\displaystyle\frac{F_{n+1}}{F_{n}}\right) &= \lim\left(1 + \frac{F_{n-1}}{F_{n}}\right) \\
# \lambda &= 1 + \frac{1}{\lambda} \\
# \lambda^2 &- \lambda -1 = 0 \end{align}$$
#   
# The previous equation is solved finding the roots of the second-degree polynomial, which gives $\lambda = \displaystyle\frac{1+\sqrt{5}}{2}$ or $\lambda = \displaystyle\frac{1-\sqrt{5}}{2}$. Since the solution $\displaystyle\frac{1-\sqrt{5}}{2}$ is negative, it can be the limit of the ratio of Fibonacci terms (all of them positive). Hence we conclude:  
#   
# $$\lim \left(\displaystyle\frac{F_{n+1}}{F_{n}}\right) = \displaystyle\frac{1+\sqrt{5}}{2} \approx 1.618.$$  
#   
# The previous number is known as the *Golden ratio* and it has fascinated mathematicians, phylosophers, and artists since ancient times. Fibonacci numbers and the Golden ratio can be found in several interesting natural patterns, as you can see in this [video](https://www.youtube.com/watch?v=ahXIMUkSXX0).
