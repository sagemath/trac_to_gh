# Issue 7165: an other bug in plot, real_part, imaginary_part and sqrt.

Issue created by migration from Trac.

Original creator: fmaltey

Original creation time: 2009-10-09 17:33:18

Assignee: was

CC:  kcrisman

I use sage 4.1.2alpha4. This plot is right with this version :

`parametric_plot([real(exp(i*m)),imaginary(exp(i*m))],m,0,7)`

I apply the patch 7122 by copy/paste in emacs and run sage -br.
Now this plot is also right, it draw a half-circle :

`parametric_plot([real(m+sqrt(m<sup>2-1)),imaginary(m+sqrt(m</sup>2-1))],m,-5,5)` 

I also get it by this function :

```
def solve2pplot (eq) : return [real(eq.rhs()),imaginary(eq.rhs())]
res = solve(z^2+2*m*z+1,z)
parametric_plot (solve2pplot (res[0]), m, -5,5)
```


Now I solve this 4 degree equation. The solve is right with sqrt at 2 levels.

But I get an error in the parametric_plot :


```
res = solve(z^4+2*m*z^2+1,z)
parametric_plot (solve2pplot (res[0]), m, -5,5)
```


The local `solve2pplot(res[0])` generates a long formula.

real axe and imaginary axe are right. 

But sage doesn't plot the quarter-circle between axes at position 1=(1,0) and i=(0,1) and claims `failed to evaluate function at 40 points`. So the plot is a line between the 2 axes.






---

Comment by fmaltey created at 2009-10-25 12:10:20

I browse the two previous expressions real(...) and imaginary(...), and test real(sqrt(...)).

Theses calculus are right and remain real. 

```
real(sqrt(m)) ; real(sqrt(I*m)) ; real(sqrt(I*m+1)) # are right 
```


But this one is the shorter that contains complex expressions :

```
real(sqrt(sqrt(m)+i+1))
```


The outer sqrt(...) assume that the inner sqrt is obvious ; so sqrt(m)+i+1 remains, even if it's a complex expression.
Then plot fails with this internal complex computation.


```
plot (real(sqrt(m)+i+1),m,-3,3) # fails with a system error
plot (real(m+i+1),m,-3,3) # is a pretty line
```



---

Comment by jason created at 2010-01-01 18:28:33

The `plot (real(sqrt(m)+i+1),m,-3,3)` now works, probably as a result of #7614.  However, I don't think the original question is addressed.


---

Comment by vdelecroix created at 2019-04-19 09:15:52

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2019-04-19 09:15:52

Now this does work

```
m = SR.var('m')
parametric_plot([real(exp(i*m)),imaginary(exp(i*m))], (m,0,7))
```



---

Comment by chapoton created at 2019-04-24 11:50:01

This needs a doctest.


---

Comment by chapoton created at 2020-01-04 20:13:18

Here is a tiny doctest. After that, I think one can close this old ticket.
----
New commits:


---

Comment by tscrim created at 2020-01-04 21:02:12

LGTM.


---

Comment by tscrim created at 2020-01-04 21:02:12

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2020-01-09 23:44:40

Resolution: fixed
