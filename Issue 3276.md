# Issue 3276: [with patch] more generic assumptions in calculus

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-05-23 08:13:34

Assignee: gfurnish

For example: 


```
sage: var('n,m')
(n, m)
sage: assume(n, m, 'integer')
sage: sin(n*m*pi)
0
sage: forget()
sage: sin(n*m*pi)
sin(pi*m*n)
```



---

Attachment


---

Comment by mhansen created at 2008-05-23 08:22:10

Excellent work Robert -- this is really nice.  The code applies, passes, tests, and is well documented.


---

Comment by gfurnish created at 2008-05-23 17:03:17

I'm giving this a negative review - see the email I'm writing to sage-devel on how introducing more maxima-isms without serious consideration is bad. There is nothing wrong with the code (so it is probably safe to use as a patch if someone needs this feature now), but introducing code to deprecate it two weeks or three weeks later is not good practice in my opinion.


---

Comment by robertwb created at 2008-05-23 18:58:13

This is a feature that people have requested from me personally many times, so I think it's worthy of inclusion. I am skeptical that the new symbolics can be a drop-in replacement for maxima in two or three weeks (would be happy to be proven wrong) so I think that it has value. Also, the exposed interface, though it passes strings to maxima, is not tied to the way maxima does things and could easily be used in the new symbolics (if not, they are not a drop-in replacement). 

Would it be better if there was a smaller, limited set of options (e.g. "integer", "even", "odd", "rational", ...) that we will be sure to want to support in the future.


---

Comment by gfurnish created at 2008-05-23 19:16:03

Drop in replacement for Maxima? doubtful.  Drop in replacement for sage.calculus? almost certainly.  Part of that is changing how assumptions work.  Like it or not assumptions are tied to the maxima way of doing things.  What makes you think I'm going to choose an assumption model that is 100% compatible with the Maxima way?  You can declare variables to be in ZZ instead of having to assume it, so immediately your method becomes very inefficient.  Also your patch has horrible error checking.  It allows for declaring a variable to be analytic or increasing.  This should almost certainly be handled better, even if your making an argument that this should go in now.  I am not going to waste time implementing complicated features in symbolics because people wern't willing to design them properly.


---

Comment by robertwb created at 2008-05-23 19:49:40

To summarize, you don't want this feature because it is at odds with the way you are handling it in your symbolics package (which is a perfectly valid argument).


---

Comment by gfurnish created at 2008-05-23 20:29:44

Basically yes.


---

Comment by gfurnish created at 2008-06-18 21:26:49

After discussion at dev1 we have decided that we should merge this but only the assume function should be considered "public" in that it will be supported after the symbolics rewrite.  The other support classes/methods will probably go away.


---

Comment by mabshoff created at 2008-06-25 09:15:16

Resolution: fixed


---

Comment by mabshoff created at 2008-06-25 09:15:16

Merged in Sage 3.0.4.alpha1
