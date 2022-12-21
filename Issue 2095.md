# Issue 2095: Simplification sometimes is wrong in Sage

Issue created by migration from Trac.

Original creator: moretti

Original creation time: 2008-02-08 01:36:44

Assignee: was


```
sage: plot(arcsin(sin(x)))
```


plots a straight line.


```
sage: x/x
1
```




```
sage: assume(x<0)
sage: sqrt(x)^2
x
```




---

Comment by was created at 2008-02-08 04:02:16

Which is "sometimes wrong"?  The first two examples look fine to me.  For the third, we're totally screwed -- or -- we just don't understand Maxima, since it's just the
native behavior of Maxima:


```

sage: !maxima
Maxima 5.13.0 http://maxima.sourceforge.net
Using Lisp CLISP 2.41 (2006-10-13)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) assume(x<0);
(%o1)                               [x < 0]
(%i2) sqrt(x)^2;
(%o2)                                  x

```



---

Comment by moretti created at 2008-02-08 21:27:54

These are examples pointed out by Peter Jipsen... the second one I think is okay. The first one could be problematic, but Robert pointed out that it works fine if you use fast_eval. For the third, I think we are screwed. There is the command


```
domain:real;
real

domain:complex;
complex
```


in maxima, however the *only* effect that this seems to have on Maxima is if domain is real, sqrt(x^2) returns abs(x).

Perhaps this should be changed to an enhancement. Assume() is currently only there as a workaround to Maxima's interactive behavior; it would be nice if Sage were smarter about assumptions on symbolic variables.


---

Comment by gfurnish created at 2008-03-16 20:10:34

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-16 20:10:34

Changing assignee from was to gfurnish.


---

Comment by was created at 2008-03-16 20:56:08

We're being stupid.  Clearly `sqrt(x)^2` should equal x NO MATTER what x is.  Period.  No matter what you assume about x it has to be the case the "sqrt(x)" is
something that when squared gives x. That's the definition of "square root".


---

Comment by was created at 2008-03-16 20:56:08

Resolution: invalid
