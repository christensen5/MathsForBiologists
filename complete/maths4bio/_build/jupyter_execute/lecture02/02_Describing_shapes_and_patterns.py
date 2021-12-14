#!/usr/bin/env python
# coding: utf-8

# In[13]:


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
fig, ax = plt.subplots(figsize=(6, 4.5))
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


# In[14]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#xt=np.linspace(0,15*np.pi,num=500)
xt=np.linspace(0,50,num=1000)
##
fig, ax = plt.subplots(figsize=(12, 3))

y1=0.62*np.cos(0.52*xt) + 1.09*np.sin(0.52*xt)
y2=3.75 + 4.33*np.cos(0.26*xt) + 2.5*np.sin(0.26*xt)

ax.plot(xt, y1+y2, color='g', lw=2)
ax.tick_params(axis='both', labelsize= 15)
ax.set_xlabel('$t$', fontsize = 16)
ax.set_ylabel('$f\,(t)$', fontsize = 16)

ax.set_xlim(0,50)
fig.tight_layout()
fig.savefig('comp_signal.png')

fig, ax = plt.subplots(figsize=(12, 3))

ax.plot(xt, y1, color='b', lw=2)
ax.tick_params(axis='both', labelsize= 15)
ax.set_xlabel('$t$', fontsize = 16)
ax.set_ylabel('$y_1\,(t)$', fontsize = 16)

ax.set_xlim(0,50)
fig.tight_layout()
fig.savefig('y1_signal.png')

fig, ax = plt.subplots(figsize=(12, 3))

ax.plot(xt, y2, color='y', lw=2)
ax.tick_params(axis='both', labelsize= 15)
ax.set_xlabel('$t$', fontsize = 16)
ax.set_ylabel('$y_2\,(t)$', fontsize = 16)

ax.set_xlim(0,50)
fig.tight_layout()
fig.savefig('y2_signal.png')


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


# # 02   - Describing shapes and patterns
#   

# ## Measuring angles  
#   
#   
# An **angle** is a primitive geometrical element, such as the *point*, the *curve* or the *plane*. It is defined as the figure formed by two line segments that extend from a common point.  
#     
# <br />
#     
# ```{image} angle.png  
# 
# ```  
#   
# <br/>
# <br />
#       
# The two most common units for measuring angles are the *degree* and the *radian*.  
#   
#   
# `````{tabbed} Degrees 
# 
# ````{panels}  
#   
# ```{image} ./degree.png  
# 
# ```  
# 
# ---  
#   
# If we divide a full rotation by 360 equal parts, each of these parts is called a *degree* (noted as $1^{\circ}$). Thus, the degree corresponds to $1/360$ of one full rotation. Each degree can also be divided in 60 equal parts called *minutes* ($1^{\circ} = 60'$) and each minute further divided in 60 *seconds* ($1' = 60''$).  
#   
# +++  
# In the figure, one degree (shown in red) and eighty nine degrees (shown in blue).
# 
#   
# ````  
# `````  
#   
# `````{tabbed} Radians  
# 
# ````{panels}  
#   
# ```{image} ./Circle_radians.gif  
# 
# ```  
# 
# ---  
#   
# One *radian* is the angle comprised in a circunference when the size of the arc is equal to the radius of the circunference. If $C$ is the size of the arc and $R$ the radius of the circunference, the corresponding angle in radians $\phi$ will be given by:  
#   
# $$ \phi = \frac{C}{R} $$
#   
# Thus, if we are considering the arc for the full circunference, $C = 2\pi R$, and we will have:  
#   
# $$\phi = \frac{2\pi R}{R} = 2\pi, $$  
#   
# and the angle for a full rotation corresponds to $2\pi$ radians.  
#   
# ```{tip}  
# When the angle is written in radians, the unit (radians or rad) is frequently omitted.
# 
# ```
#   
# ````  
# `````  
#   
# For a given angle, transforming between units of degrees and radians can be simply done with:  
#   
# $$\frac{360^{\circ}}{\theta} = \frac{2\pi}{\phi},$$  
#   
# where $\theta$ is the angle measured in degrees and $\phi$, measured in radians. In this lecture, we will consider the angles measured in radians (independent of the symbol used for the variable), unless stated otherwise. 
#   
# ```{admonition} Example  
# If $\theta = 90^{\circ}$, then using the previous expression we have $\phi = \displaystyle\frac{\pi}{2}$. Since $\theta$ and $\phi are directly proportional, we also have:  
#   
#   $$\theta = 180^{\circ} \longrightarrow \phi = 2 \cdot \frac{\pi}{2} = \pi $$  
#   $$\theta = 270^{\circ} \longrightarrow \phi = 3 \cdot \frac{\pi}{2} = \frac{3\pi}{2} $$  
#   $$\theta = 360^{\circ} \longrightarrow \phi = 4 \cdot \frac{\pi}{2} = 2\pi $$
#   
# ```

# ## Trigonometric circle  
#   
#   
# We obtain the trigonometric circle by superimposing a circle of radius $1$ to the cartesian system of coordinates:   
# 
# ```{image} trig_circ.png
# ```  
# 
#   
# The projections on the $x$ and $y$-axes have special meanings, if we consider the angle $\theta$ between the line segment in the radial direction and the $x$-axis.  
#   
# From the geometric relations on the right triangle (triangle in which one internal angle is a right angle):  
#   
# ````{panels}  
#   
# ```{image} ./right_trig.png
# 
# ```  
# 
# ---  
#   
# The larger side of the triangle, opposing the right angle, is called *hypothenuse*, while the other two smaller side are called *catheti*. We define the *sine* and *cosine* of the angle $\alpha$ as the ratios of the opposing and adjacent catheti, respectively, with the hypothenuse:  
#   
# $$\mbox{sin}(\alpha) = \frac{a}{c}$$  
# $$\mbox{cos}(\alpha) = \frac{b}{c}$$
#   
# ````  
#   
# Back to the trigonometric circle, it is possible to construct a right triangle where the hypothenuse corresponds to the radius of the superimposed circle. In this case, since this radius equals to $1$, we have:  
#   
# $$\mbox{sin}(\theta) = y$$  
# $$\mbox{cos}(\theta) = x.$$  
#   
# In other words, the projections of the end of the radial line segment on the $y$ and $x$-axes correspond to the sine and cosine of the angle $\theta$. Sine and cosine for this angle can be obtained by the projections even if $\theta > \displaystyle\frac{\pi}{2}$.  
#   
# ### Trigonometric identities  
#   
#   With the aid of the projections on the trigonometric circle, some trigonometric identities become imediately clear. Consider $\theta > 0$ for counterclockwise angle measurements starting from the $x$-axis and $\theta < 0$ for clockwise measurements. We have:  
#     
# $$\mbox{sin}(0) = 0,\ \ \ \mbox{sin}\left(\frac{\pi}{2}\right) = 1,\ \ \ \mbox{sin}(\pi) = 0,\ \ \ \mbox{sin}\left(\frac{3\pi}{2}\right) = -1,\ \ \ \mbox{sin}(2\pi) = 0$$  
# $$\mbox{cos}(0) = 1,\ \ \ \mbox{cos}\left(\frac{\pi}{2}\right) = 0,\ \ \ \mbox{cos}(\pi) = -1,\ \ \ \mbox{cos}\left(\frac{3\pi}{2}\right) = 0,\ \ \ \mbox{cos}(2\pi) = 1$$
#   
# From the fact that a full rotation brings you back to the same point:  
#   
# $$\mbox{sin}(\theta) = \mbox{sin}(\theta + 2\pi)$$  
# $$\mbox{cos}(\theta) = \mbox{cos}(\theta + 2\pi)$$  
#   
# or from Pythagoras' theorem on the right triangle in the trigonometric circle:  
#   
# $$\begin{align}
# [\mbox{sin}(\theta)]^2 + [\mbox{cos}(\theta)]^2 =& 1^2 \\
# \mbox{sin}^2(\theta) + \mbox{cos}^2(\theta) =& 1
# \end{align}$$  
#   
# ```{tip}
# The notation $\mbox{sin}^2(\theta)$ is frequently used to express the square of $\mbox{sin}(\theta)$, or:  
#   
# $$ \mbox{sin}^2(\theta) = [\mbox{sin}(\theta)]^2 = [\mbox{sin}(\theta)]\cdot[\mbox{sin}(\theta)],$$  
#   
# which is different from $\mbox{sin}(\theta^2)$.
# ```  
#   
#   
# Now watch this [video](https://web.microsoftstream.com/video/b3023026-7d45-4378-a8ee-c166a43eb2e7) for a different application of the same trigonometric construct.
#   
#   

# ## Trigonometric functions  
#   
# Since sine and cosine are defined for any real value of a given angle $x$ ($x \in {\rm I\!R}$), we can define the functions:  
#   
# $$f(x) = \mbox{sin}(x)$$  
# $$f(x) = \mbox{cos}(x).$$  
#   
# Thus, the association of sine and cosine with pure geometric ratios gives place for a more generic definition of functions of real variables. The graphs of these functions are given by:  
#   
# ```{image} ./sin_cos.png
# 
# ```  
#   
# All the other known trigonometric relations can also be defined as functions in a similar way. Take for example the tangent of an angle $\theta$, which is:  
#   
# $$tan(\theta) = \displaystyle\frac{\mbox{sin}(\theta)}{\mbox{cos}(\theta)}.$$
# 
# If $x \in {\rm I\!R}$, than we can define a function  
#   
# $$ f(x) = \mbox{tan}(x) = \displaystyle\frac{\mbox{sin}(x)}{cos(x)}, \ \ \ (\mbox{for }\mbox{cos}(x) \ne 0).$$  
#   
# The graph from the tangent function will be given by:  
#   
# ```{image} ./tan.png
# 
# ```  
#   
# Note by the above graphs that the functions sine and cosine have patterns that repeat themselves every interval of $2\pi$, while the tangent repeats itself every interval of $\pi$. We say that these three functions are **periodic**.
# 
# 
# A function $f(x)$ is periodic if there is a positive constant $a$, so that:  
#   
# $$f(x + a) = f(x),$$  
#   
# for all values of $x$ for which the function f(x) is defined.  
#   
# If $a$ is the smallest number with this property, we call it the *period* of f(x).
# 
# ```{admonition} Example  
#   
# Since $\mbox{sin}(x + 2\pi) = \mbox{sin}(x)$ for any value of $x$ and since $2\pi$ is the smallest number for which this property holds, then sine is a periodic function with period $2\pi$. With the same reasoning, it can be shown that the tangent is periodic with period $\pi$.
# ```  
#   
# ### Amplitude and Period  
#   
#   
# From the basic functions $\mbox{sin}(x)$ or $\mbox{cos}(x)$ we can write a more general function $f(x)$ given by  
#   
# $$f(x) = A\mbox{sin}(\omega x),\ \ \ \ \ \ A, \omega \in {\rm I\!R}\ \ (A, \omega \ne 0)$$  
#   
# Since the sine ranges from $-1$ to $1$ (see the graph for $sin(x)$ for reference), by its definition, $f(x)$ will range from $-A$ to $A$. We call $A$ the **amplitude** of $f(x)$ and it gives the extent of the variation of the oscillation of the function.  
#   
# Being sine a periodic function, $f(x)$ will also be, possibly with a different period. The period $T$ of $f(x)$, as discussed before, will be determined by the equation $f(x + T) = f(x)$, that should be valid for every $x$. Thus:  
#   
# $$\begin{align}
#     f(x + T) &= f(x) \\
#     A\mbox{sin}(\omega(x+T)) &= A\mbox{sin}(\omega x) \\
#     \mbox{sin}(\omega(x+T)) &= \mbox{sin}(\omega x) \\
#     \mbox{sin}(\omega x+\omega T)) &= \mbox{sin}(\omega x) \\
#     \mbox{sin}(z+\omega T)) &= \mbox{sin}(z)\ \ \ \ \ \ (\mbox{where we change the variable to } z=\omega x)
#   \end{align}$$
#   
# But since we know that sine is periodic with period $2\pi$, we should have $|\omega|T = 2\pi$. Thus, the **period** of the function $f(x)$ will be:  
#   
# $$T = \frac{2\pi}{\omega}.$$  
#   
# The constant $\omega = \displaystyle\frac{2\pi}{T}$ is called **angular frequency** and measures the number of full rotations the function $f(x)$ oscillates in one interval of $T$.  
#   
# ```{admonition} Example  
#   
# The function $f(x) = 3.6\, \mbox{cos}\left(\displaystyle\frac{\pi}{3}x\right)$ has an amplitude $A=3.6$, an angular frequency $\omega = \displaystyle\frac{\pi}{3}$, and a period $T = \displaystyle\frac{2\pi}{\omega} = \displaystyle\frac{2 \pi}{\frac{\pi}{3}} = 6$.  
# ```

# ## Modelling complex periodic phenomena  
#   
#   
# Watch this [video](https://web.microsoftstream.com/video/02f373a2-621b-4313-a18a-265f5fb65656) about periodic functions decomposition.

# ## Transformation on graphs  
#   
#   
# Starting from the elementary functions we have discussed  
#       
# $$ax+b,\ \ ax^2+bx+c,\ \ \sqrt{x},\ \ \mbox{e}^x,\ \ \mbox{log}(x),\ \ \mbox{sin}(x),\ \ \mbox{cos}(x)$$  
#   
# we can introduce several transformations to obtain new functions, by adding or multiplying constants to the argument (function variable) or to the whole function. These are the simplest cases of what is know as *function composition* with the resulting function called *composite function*.  
#   
# When working with mathematical models, this will help you to understand how the shape of a given function might change by changing one of the parameters, or how to construct a set of functions (that might be useful for your particular model) with small modifications of basic functions.  
#   
#   
# ### Translations  
#   
# A given function can be dislocated, either vertically or horiontally, by *adding* a constant $c$ to the whole function or to its argument. In general, starting from a function $f(x)$, translations are built following the rules:  
#   
# - **Horizontal** (Constant $c$ summed to the argument of the function)  
# 
#   $y = f(x + c)\ \ \ \  -  \left\{
# \begin{array}{ll}
#       c > 0 & \rightarrow \ \  \mbox{function moves to the left} \\
#       c < 0 & \rightarrow \ \  \mbox{function moves to the right} \\
# \end{array} 
# \right. $  
#   
# - **Vertical** (Constant $c$ summed to the whole function)  
# 
#   $y = f(x) + c\ \ \ \  -  \left\{
# \begin{array}{ll}
#       c > 0 & \rightarrow \ \  \mbox{function moves up} \\
#       c < 0 & \rightarrow \ \  \mbox{function moves down} \\
# \end{array} 
# \right. $  
#   
# ```{admonition} Example  
# If we start with the function $f(x) = x^3$, the function $y = f(x + 2) = (x+2)^3$ will represent a horizontal translation, while the function $y = f(x) + 2 = x^3+2$ will represent a vertical translation.  
# ```  
#   
# To see how this works, try to implement the following code in your own jupyter notebook. Try to use different functions $f(x)$ (defined in 'func(x)') to see how different graphs behave to horizontal and vertical translations.
#   
# ```{code}
# from ipywidgets import interact
# import matplotlib.pyplot as plt
# import numpy as np
# 
# def func(x):
#     return x**3
# 
# def htrans(c):
#     x = np.linspace(-3,3)
#     
#     y = func(x+c) #constant c in the argument of the function
#     
#     plt.plot(x,y, label='$f(x+c)$')
#     plt.title('Horizontal translation')
#     plt.legend(fontsize=12)
#     
#     plt.ylim(-8, 8) #remember to change the limits for better visualisation if necessary
#     
#     plt.axhline(0, color='black', lw=1)
#     plt.axvline(0, color='black', lw=1)
#     
#     
# 
#     plt.show()
# 
# def vtrans(c):
#     x = np.linspace(-3,3)
#     
#     y = func(x)+c #constant c summing the whole function
#     
#     plt.plot(x,y,  label='$f(x)+c$')
#     plt.title('Vertical translation')
#     
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.legend(fontsize=12)
#     
#     plt.ylim(-8, 8) #remember to change the limits for better visualisation if necessary
#         
#     plt.axhline(0, color='black', lw=1)
#     plt.axvline(0, color='black', lw=1)
#     
#     plt.show()
#     
# # create a slider
# 
# interact(htrans, c=(-2.0,2.0))
# interact(vtrans, c=(-2.0,2.0))
# ```  
#   
#   
# ### Stretching/ Compression  
#   
# A given function can also be stretched or compressed, either vertically or horiontally, by *multiplying* a constant $c$ to the whole function or to its argument. Starting from a function $f(x)$, stretchings/compressions are built following the rules:  
#   
# - **Horizontal** (Constant $c$ multiplied to the argument of the function)  
# 
#   $y = f(cx)\ \ \ \  -  \left\{
# \begin{array}{ll}
#       c > 1 & \rightarrow \ \  \mbox{function is horizontally compressed} \\
#       0 < c < 1 & \rightarrow \ \  \mbox{function is horizontally stretched} \\
# \end{array} 
# \right. $  
#   
# - **Vertical** (Constant $c$ multiplied to the whole function)  
# 
#   $y = cf(x)\ \ \ \  -  \left\{
# \begin{array}{ll}
#       c > 1 & \rightarrow \ \  \mbox{function is vertically stretched} \\
#       0 < c < 1 & \rightarrow \ \  \mbox{function is vertically compressed} \\
# \end{array} 
# \right. $  
#   
# ```{admonition} Example  
# For the function $f(x) = x^3-2x$, the function $y = f(2x) = (2x)^3-2(2x) = 8x^3-4x$ will represent a horizontal compression, while the function $y = 2f(x) = 2x^3 - 4x$ will represent a vertical stretching.  
# ```  
#   
# Now play with the code below to see how different graphs behave to horizontal and vertical stretching/compression.
#   
# ```{code}  
# from ipywidgets import interact
# import matplotlib.pyplot as plt
# import numpy as np
# 
# def func(x):
#     return x**3-2*x
# 
# def hstetcom(c):
#     x = np.linspace(-3,3)
#     
#     y = func(c*x) #constant c multiplying the argument of the function
#     
#     plt.plot(x,y, label='$f\, (cx)$')
#     plt.title('Horizontal stretching/compression')
#         
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.legend(fontsize=12)
#     
#     plt.ylim(-4, 4) #remember to change the limits for better visualisation if necessary
#     
#     plt.axhline(0, color='black', lw=1)
#     plt.axvline(0, color='black', lw=1)
#     
#     
# 
#     plt.show()
# 
# def vstetcom(c):
#     x = np.linspace(-3,3)
#     
#     y = c*func(x) #constant c multiplying the whole function
#     
#     plt.plot(x,y,  label='$c\, f\, (x)$')
#     plt.title('Vertical stretching/compression')
#     
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.legend(fontsize=12)
#     
#     plt.ylim(-4, 4) #remember to change the limits for better visualisation if necessary
#         
#     plt.axhline(0, color='black', lw=1)
#     plt.axvline(0, color='black', lw=1)
#     
#     plt.show()
#     
# # create a slider
# 
# interact(hstetcom, c=(0.1,3.0))
# interact(vstetcom, c=(0.1,3.0))
# ```  
#   
#   
# ### Reflection  
#   
# If the constant $c$ multiplying the whole function or its argument has the particular value $c = -1$, we will have a *reflection*. Reflections can be done in relation to the $x$ or $y$-axes and they are built, starting from a function $f(x)$, following the rules:  
#   
#   
# - **About the x-axis** - $y = -f(x)$  
#   
# - **About the y-axis** - $y = f(-x)$  
# 
# The figure below shows these two reflections using the function $f(x) = (x-1)^2$.  
#   
# ```{image} ./reflection.png
# 
# ```  
