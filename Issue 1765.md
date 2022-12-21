# Issue 1765: allow list of variables as second input to solve command (very easy to implement)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-13 05:24:26

Assignee: was

CC:  dfdeshom


```
sage: var("s,i,b,m,g");
sage: sys = [ m*(1-s) - b*s*i, b*s*i-g*i ];
sage: equilibria = solve(sys,s,i);
[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]

> solve's
> syntax seems assymetric as used here.  Shouldn't the second argument
> be a sequence of variables?

You mean like this:

sage: solve(sys, [s, i])              # this is not implemented
[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]

That seems like a really good idea.
Note that right now at least you can do the following
(note the *) and it will work:

sage: solve(sys, *[s, i])
[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]

```


This would be very easy to implement. 


---

Attachment


---

Comment by AlexGhitza created at 2008-03-13 12:39:50

The patch doesn't actually do what the description asks for; more precisely, instead of the desired behavior


```
sage: solve(sys, [s, i])              # this is not implemented
[[s == 1, i == 0], [s == g/b, i == (b - g)*m/(b*g)]]
```


this still throws a ValueError.


---

Attachment


---

Comment by dfdeshom created at 2008-03-13 15:06:33

Should be corrected now so ` solve(sys, [s, i]) ` should now work. The correct changes are in 1765.hg, not the patch file (wish there was a way to delete files...)


---

Attachment

use instead of the above


---

Comment by AlexGhitza created at 2008-03-15 17:42:52

I applied this to sage-2.10.3 and it looks good.  Since we tend to like patches rather than bundles, I've uploaded a patch that has the changes from the bundle.


---

Comment by mabshoff created at 2008-03-16 01:07:14

Merged 1765.hg in Sage 2.10.4.rc0. Credit-wise it was the cleanest solution, but I am sure that Didier will post Mercurial patches in the future.


---

Comment by mabshoff created at 2008-03-16 01:07:14

Resolution: fixed
