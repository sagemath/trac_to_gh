# Issue 2915: bug in symbolic integration or "stupid bug in the sage/maxima interface"?

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-14 05:27:46

Assignee: was

I tried the first integral inthe Axiom book in Sage and get a big boom!

```
sage: var('a,b')
sage: integrate(1/(x^3 *(a+b*x)^(1/3)), x)
Traceback (most recent call last):
...
TypeError: 
Is  a  
Computation failed due to a bug in Maxima -- NOTE: Maxima had to be restarted.
```


Trying maxima interactively shows it is just prompting for
whether or not a is positive.  Specifying which makes this work fine:

```
sage: var('a,b')
sage: assume(a>0)
sage: integrate(1/(x^3 *(a+b*x)^(1/3)), x)
2*b^2*arctan((2*(b*x + a)^(1/3) + a^(1/3))/(sqrt(3)*a^(1/3)))/(3*sqrt(3)*a^(7/3)) - b^2*log((b*x + a)^(2/3) + a^(1/3)*(b*x + a)^(1/3) + a^(2/3))/(9*a^(7/3)) + 2*b^2*log((b*x + a)^(1/3) - a^(1/3))/(9*a^(7/3)) + (4*b^2*(b*x + a)^(5/3) - 7*a*b^2*(b*x + a)^(2/3))/(6*a^2*(b*x + a)^2 - 12*a^3*(b*x + a) + 6*a^4)
```



---

Comment by mhansen created at 2008-04-14 20:44:44

Changing status from new to assigned.


---

Comment by mhansen created at 2008-04-14 20:44:44

Changing assignee from was to mhansen.


---

Attachment


---

Attachment

REFEREE REPORT:

   * Excellent!
 
   * I've reformatted the doctest a little and added computing the actual integral, since it's a good example to have in our system.


---

Comment by mabshoff created at 2008-04-15 00:55:21

Resolution: fixed


---

Comment by mabshoff created at 2008-04-15 00:55:21

Merged both patches in Sage 3.0.alpha5
