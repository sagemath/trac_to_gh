# Issue 8125: problem with "text"

Issue created by migration from https://trac.sagemath.org/ticket/8125

Original creator: jhpalmieri

Original creation time: 2010-01-29 21:09:34

Assignee: was

In Sage 4.3.2.alpha0:

```
sage: text(r"$\left(2 a=b\right)$", (2,3))   # works fine 
sage: text(r"$(2 \, a=b)$", (2,3))   # works fine 
sage: text(r"$\left(2 \, a=b\right)$", (2,3))   # error! 
Traceback (click to the left of this block for traceback) 
... 
AttributeError: 'Kern' object has no attribute 'height' 
```




---

Comment by jhpalmieri created at 2010-01-30 01:25:15

This seems to be a bug in matplotlib; I just reported it to the matplotlib-devel mailing list, and I'll report any answers I get.

Meanwhile, this arises in "real life" as follows:

```
sage: var("y R") 
sage: a(y,R) = pi * (2*R - y) * y 
sage: latex(a(y,R))
{\left(2 \, R - y\right)} \pi y
```

Therefore 

```
sage: lbl = text(r"$\int \  " + latex(a(y,R)) + "$",(3,20)) 
```

won't work with matplotlib.  Should we get rid of the "\," in the latex output?


---

Comment by kcrisman created at 2010-07-27 17:35:39

Any response?


---

Comment by jhpalmieri created at 2010-07-27 17:45:45

No response at all.   From python:

```
>>> import pylab
>>> pylab.text(0.2, 0.2, r"$\left(2a = b\right)$")
<matplotlib.text.Text object at 0x1020aa450>
>>> pylab.savefig('a.png')
>>> pylab.text(0.2, 0.2, r"$(2a \, = b)$")
<matplotlib.text.Text object at 0x101e22a50>
>>> pylab.savefig('b.png')
>>> pylab.text(0.2, 0.2, r"$\left(2a \, = b\right)$")
<matplotlib.text.Text object at 0x1020b5750>
>>> pylab.savefig('c.png')
BOOM
```

Combining `\left(`, `\right)}]}, and {{{\,` seems to lead to problems.  So now what?  Do we get rid of the `\,`?


---

Comment by jhpalmieri created at 2010-10-21 04:50:01

Changing keywords from "" to "matplotlib".


---

Comment by jhpalmieri created at 2010-10-21 04:50:01

This is still an issue in Sage 4.6.alpha3: it has not been fixed in matplotlib 1.0.0.


---

Comment by mdboom created at 2011-03-23 23:48:47

Fixed by this pull request in matplotlib:

[https://github.com/matplotlib/matplotlib/pull/52](https://github.com/matplotlib/matplotlib/pull/52)

This will make it into the next matplotlib bugfix release.


---

Comment by mdboom created at 2011-03-23 23:48:47

Resolution: fixed


---

Comment by mhansen created at 2011-03-24 00:19:03

Changing status from closed to new.


---

Comment by mhansen created at 2011-03-24 00:19:03

Resolution changed from fixed to 


---

Comment by mhansen created at 2011-03-24 00:19:03

We keep tickets open until the fix has actually gone into a Sage release.


---

Comment by jhpalmieri created at 2012-03-21 21:16:20

This works now; it must be in matplotlib 1.1.0 (or earlier).  So this ticket can be closed.


---

Comment by jhpalmieri created at 2012-03-21 21:16:20

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2012-03-21 21:16:29

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-04-04 13:23:16

Resolution: worksforme
