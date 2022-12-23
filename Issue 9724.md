# Issue 9724: Sage allows creation of variables with empty name

Issue created by migration from https://trac.sagemath.org/ticket/9724

Original creator: logix

Original creation time: 2010-08-11 09:47:33

Assignee: burcin

CC:  schilly

Keywords: variable empty name

Sage allows you to create a variable with an empty name.  While this at first appears not to cause any problems, one thing it does break is reset():

```
sage: var(' ')
(, )
sage: whos
Variable   Type          Data/Info
----------------------------------
           Expression    
sage: reset()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (437, 0))

---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/usr/local/sage/local/lib/python2.6/site-packages/sage/all_cmdline.pyc in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/misc/reset.so in sage.misc.reset.reset (sage/misc/reset.c:838)()

IndexError: string index out of range
sage: del globals()['']
sage: reset()
```

Sage also allows the creation of variables with other illegal names (e.g. '1a' or '1'), but for these at least reset() still works.  There are two ways to fix this, the first is to disallow the creation of such variables via var(), but then all illegal cases would have to be taken care of, and it wouldn't help if you created illegal variables manually by inserting them into globals() (but I would argue that if you do this, you're on your own anyway).  The second way to fix the behaviour above would be to make reset() able to delete empty variables too.  This however is only viable if these variables don't break anything else, other than the case mentioned above.


---

Comment by leif created at 2010-08-16 22:45:49

Perhaps one could add a warning message giving a hint in other cases, too.

From `#sage-devel` (IRC):

```
<cousteau> weird, I can't make the notebook display the same that real LaTeX
 I have a variable which I called {m}:   var('{m}')   In real LaTeX, it nicely displays as an m, but in the notebook it keeps the braces
 same for a variable called \mu\Omega
 does the notebook just get the latex() of the variables? or does it do something else?
 var('sui', latex_name="s_{u,i}")   :'( I shoild read the manual first
```



---

Comment by vbraun created at 2011-06-18 05:17:18

Fixed in the patch on #7496:


```
sage: var(' ')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/vbraun/opt/sage-4.7.1.alpha2/devel/sage-main/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/calculus/var.so in sage.calculus.var.var (sage/calculus/var.c:687)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/symbolic/ring.so in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6276)()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/symbolic/ring.so in sage.symbolic.ring.SymbolicRing.var (sage/symbolic/ring.cpp:6048)()

ValueError: The name "" is not a valid Python identifier.
```



---

Comment by vbraun created at 2011-06-18 05:17:18

Changing keywords from "variable empty name" to "sd31".


---

Comment by vbraun created at 2011-06-18 05:17:18

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-06-24 00:29:43

Apparently this means this should be closed.  Probably proper form is to let the release manager change the milestone, right, Jeroen?  :)

I'm assuming that Mariah's comment on #7496 means she checked this out, so I'm putting her and Volker as reviewers for closing this.


---

Comment by kcrisman created at 2011-06-24 00:29:43

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-06-24 03:10:05

It does work.  This is not mentioned in the patch for #7496, though, so I'm adding a doctest there.


---

Comment by jdemeyer created at 2011-06-24 15:03:14

Replying to [comment:3 kcrisman]:
> Probably proper form is to let the release manager change the milestone, right, Jeroen?  :)
No, it is easier if you change the milestone to "sage-duplicate/invalid/wontfix" and set to "positive_review".  This gives me the best overview on [http://trac.sagemath.org/sage_trac/report/40](http://trac.sagemath.org/sage_trac/report/40).  I will then close the ticket.


---

Comment by jdemeyer created at 2011-06-24 15:03:14

Resolution: duplicate
