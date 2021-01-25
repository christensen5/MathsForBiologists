#!/usr/bin/env python
# coding: utf-8

# 1. **Island Model** Assume that a species lives in a habitat that consists of many islands close to a mainland. The species occupies both the mainland and the islands, but, although it is present on the mainland at all times, it frequently goes extinct on the islands. Islands can be recolonized by migrants from the mainland. The following model keeps track of the fraction of islands occupied: Denote the fraction of islands occupied at time $t$ by $p(t)$. Assume that each island experiences a constant risk of extinction and that vacant islands (the fraction $1-p$) are colonized from the mainland at a constant rate. Then
# 
#     $$
#         \frac{dp}{dt}=c(1-p)-ep
#     $$
# 
#      where $c$ and $e$ are positive constants.
# 
#     <br/>
#     
#     1. The gain from colonization is $f (p) = c(1 - p)$ and the loss from extinction is $g(p) = ep$. Graph (without graph visualisers) $f(p)$ and $g(p)$ for $0 \le p \le 1$ in the same coordinate system. Explain why the two graphs intersect whenever $e$ and $c$ are both positive. Compute the point of intersection and interpret its biological meaning.
#     
#      <br/>
#      
#     2. The parameter $c$ measures how quickly a vacant island becomes colonized from the mainland. The closer the islands, the larger is the value of $c$. Use your graph in (a) to explain what happens to the point of intersection of the two lines as c increases. Interpret your result in biological terms.

# 2. **Biotic Diversity** (Adapted from Valentine, 1985.) Walker and Valentine (1984) suggested a model for species diversity which assumes that species extinction rates are independent of diversity but speciation rates are regulated by competition. Denoting the number of species at time $t$ by $S(t)$, the speciation rate by $b$, and the extinction rate by $a$, they used the model
# 
#     $$
#         \frac{dS}{dt} = S\left[b\left(1-\frac{S}{K}\right)-a \right]
#     $$
#       
#     where $K$ denotes the number of "niches", or potential places for species in the ecosystem.
#     
#     <br/>
#     
#     1. Find possible equilibria ($dS/dt = 0$) under the condition $a < b$.
#     
#     <br/>
#     
#     2. Use your result in (a) to explain the following statement by Valentine (1985):
#     
#         "In this situation, ecosystems are never 'full', with all potential niches occupied by species so long as the extinction rate is above zero."
#     
#     <br/>
#     
#     3. What happens when $a \ge b$?

# 3. Find a point on the curve
#     
#     $$
#         y = 1 - 3x^3
#     $$
#     
#      whose tangent line is parallel to the line $y = -x$. Is there more than one such point? If so, find all other points with this property.

# 4. Find a point on the curve
# 
#     $$
#         y = 2x^3 - 4x + 1
#     $$
#     
#     whose tangent line is parallel to the line $y-2x = 1$. Is there more than one such point? If so, find all other points with this property.

# 5. In the following, use the product and quotient rules to find the derivative with respect to the independent variable.
# 
#     <br/>
#     
#     1. $f(x) = (2x^3 - 1)(3 + 2x^2)$
#     
#     <br/>
#     
#     2. $h(s) = (4 - 3s^2 + 4s^3)^2$
#     
#     <br/>
#     
#     3. $f(x) =\sqrt{3x}(x^2 - 1)$
#     
#     <br/>
#     
#     4. $g(t) = 4(3t^2 - 1)(2t + 1)$
#     
#     <br/>
#     
#     5. $f(x) = 3(x^2 + 2)(4x^2 - 5x^4) - 3$
#     
#     <br/>
#     
#     6. $g(x) = \displaystyle\frac{1 - 4x^3}{1 - x}$
#     
#     <br/>
#     
#     7. $h(x) = \displaystyle\frac{1 + 2x^2 - 4x^4}{3x^3 - 5x^5}$
#     
#     <br/>
#     
#     8. $f(t) =\displaystyle\frac{3 - t^2}{(t + 1)^2}$
#     
#     <br/>
#     
#     9. $h(s) = \displaystyle\frac{2s^3 - 4s^2 + 5s - 7}{(s^2 - 3)^2}$
#     
#     <br/>
#     
#     10. $g(s) = \displaystyle\frac{s^{1/7} - s^{2/7}}{s^{3/7} + s^{4/7}}$
#     

# 6. **Logistic Growth**
# 
#     <br/>
#     
#     1. Find the derivative of the logistic growth curve
#     
#         $$
#             N(t)=\frac{K}{1+\left(\frac{K}{N(0)}-1\right)e^{-rt}}
#         $$
#         
#         where $r$ and $K$ are positive constants and $N(0)$ is the population size at time $0$.
#         
#         <br/>
#             
#     2. Show that $N(t)$ satisfies the equation
#     
#         $$
#             \frac{dN}{dt}=rN\left(1-\frac{N}{K}\right)
#         $$
#         
#         [*Hint:* Use the function $N(t)$ given in (a) for the right-hand side, and simplify until you obtain the derivative of N(t) that you computed in A.]
#         
#         <br/>
#         
#     3. What happens to the *per-capita* rate of growth $\frac{1}{N}\frac{dN}{dt}$ as you increase N? What biological principle and what type of interaction is your model describing?

# 7. In the following, find the derivative with respect to the independent variable.
#     
#     <br/>
#     
#     1. $f(x) = \mbox{sin}(e^{2x} + x)$
#     
#     <br/>
#     
#     2. $h(x) = \mbox{exp}[x^2 - 2 \mbox{cos}\, x]$
#     
#     <br/>
#     
#     3. $f(x) =\displaystyle\frac{x-2^{−x}}
# {1+x2^{−x}}$
#     
#     <br/>
#     
#     4. $g(t) = \mbox{log}\left(\displaystyle\frac{1 - t}{1 + 2t}\right)$
#     
#     <br/>
#     
#     5. $f(t) = \mbox{sin}(\mbox{ln}(3t))$
#     
#     <br/>
#     
#     6. $g(x) = \mbox{ln}(\mbox{cos}(1 - x))$
#     
#     <br/>
#     
#     7. $h(x) = \displaystyle\frac{\sqrt{x^2 - 1}}{2+\sqrt{x^2+1}}$ 
#     
#     <br/>
#     
#     8. $f(t) =\sqrt[3]{t^2+\sqrt{1-t}}$
#     
#     <br/>
#     

# 8. The functional responses of some predators are sigmoidal; that is, the number of prey attacked per predator as a function of prey density has a sigmoidal shape. If we denote the prey density by $N$, the predator density by $P$, the time available for searching for prey by $T$, and the handling time of each prey item per predator by $T_h$, then the number of prey encounters per predator as a function of $N$, $T$, and $T_h$ can be expressed as
# 
#     $$
#         f (N, T, T_h) = \frac{b^2N^2T}{1 + cN + bT_hN^2}
#     $$
#     
#     where $b$ and $c$ are positive constants.
#     
#     <br/>
#     
#     1. Calculate the first-order partial derivative of $f(N, T, T_h)$ with respect to the prey density $N$. If $N$ increases, what happens to $f(N, T, T_h)$?
#      
#     <br/>
#     
#     2. Calculate the first-order partial derivative of $f(N, T, T_h)$ with respect to the the time $T$ available for search. If $T$ increases, what happens to $f(N, T, T_h)$?
#      
#     <br/>
#     
#     3. Calculate the first-order partial derivative of $f(N, T, T_h)$ with respect to the handling time $T_h$. If $T_h$ increases, what happens to $f(N, T, T_h)$?
#     
#     [*Hint:* The function $f(N, T, T_h)$ will be an increasing (decreasing) function of the independent variable if the first-order partial derivative of $f$ with respect to this variable is positive (negative).]
