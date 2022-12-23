# Issue 9582: Term order discrepancy in random test on OS X

Issue created by migration from https://trac.sagemath.org/ticket/9582

Original creator: mpatel

Original creation time: 2010-07-23 07:47:16

Assignee: mvngu

CC:  cwitty ddrake jhpalmieri burcin

Reported by John Palmieri on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/8c77081af31fc7ef#8c77081af31fc7ef):

```
a 64 bit Mac OS X 10.6.4 box: one failure:

sage -t -long "devel/sage/sage/symbolic/random_tests.py"
**********************************************************************
File "/Applications/sage_builds/sage-4.5.2.alpha0/devel/sage/sage/
symbolic/random_tests.py", line 236:
    sage: random_expr(50, nvars=3, coeff_generator=CDF.random_element)
Expected:
    factorial(floor((-0.314177274493 + 0.144437996366*I)/cosh(-v1^2*e/
v3) + cos((-0.708874026302 - 0.954135400334*I)*v3) -
zetaderiv(-0.228070288671 + 0.33842966472*I, 0.520184609653 -
0.734276246499*I)))^(-arccoth(-abs(((-0.804514286089 -
0.0293247734576*I)*v1 + (-0.804514286089 - 0.0293247734576*I)*v3 -
1.0)*elliptic_ec((-0.0263902659909 +
0.153261789843*I)*arccot(pi*catalan)))))
Got:
    factorial(floor((-0.314177274493 + 0.144437996366*I)/cosh(-v1^2*e/
v3) - zetaderiv(-0.228070288671 + 0.33842966472*I, 0.520184609653 -
0.734276246499*I) + cos((-0.708874026302 - 0.954135400334*I)*v3)))^(-
arccoth(-abs(((-0.804514286089 - 0.0293247734576*I)*v1 +
(-0.804514286089 - 0.0293247734576*I)*v3 -
1.0)*elliptic_ec((-0.0263902659909 +
0.153261789843*I)*arccot(pi*catalan)))))
**********************************************************************

Looks like a discrepancy in the order terms are printed.
```


Acccording to Dan Drake:

```
I'm seeing that on bsd.math too. This is related to #9514, which was
supposed to fix this, but evidently doesn't, on OS X at least.
```


Related: #9514.


---

Comment by cwitty created at 2010-07-23 09:12:22

Unlikely that this has anything to do with #9514.  The symptom of #9514 was getting totally different terms, and the cause was that it made a list of all known symbolic functions [sin, cos, factorial, ...], and randomly picked the third element (say) from the list -- but on different systems, the third element might be factorial, or it might be cos.

If it's producing mathematically equal terms that only print differently, which seems to be the case here, the cause is probably some system dependency in the pynac simplification or printing routines.


---

Comment by mpatel created at 2010-07-27 02:54:25

Evaluating `cos(x) + zeta(x)` in Sage 4.5.2.alpha0 gives

 * `zeta(x) + cos(x)` on sage.math.
 * `cos(x) + zeta(x)` on bsd.math.

Is this representative of the underlying problem?


---

Comment by mpatel created at 2010-07-28 08:18:59

I compiled [GiNaC](http://www.ginac.de/Download.html) (and [CLN](http://www.ginac.de/CLN/)) on bsd and sage.math.  Evaluating `cos(x) + zeta(x);` in GiNaC's `ginsh` shell gives the same results as in [comment:2 comment 2].  I don't know if this is useful information.


---

Comment by kcrisman created at 2010-07-28 16:20:12

On Sage 4.4.4 on OS X 10.6:

```
sage: cos(x)+zeta(x)
cos(x) + zeta(x)
sage: zeta(x)+cos(x)
cos(x) + zeta(x)
sage: version()
'Sage Version 4.4.4, Release Date: 2010-06-23'
```

So this may have been a problem for a while?


---

Comment by jhpalmieri created at 2010-07-28 16:21:39

Maybe so.  Maybe it was just exposed with new tests?


---

Attachment


---

Comment by cwitty created at 2010-07-28 21:01:09

Changing status from new to needs_review.


---

Comment by cwitty created at 2010-07-28 21:01:09

If we decide that the actual problem (different printing across platforms) is not a regression, and doesn't have to be fixed in this release, then I've attached a patch that works around the problem (by modifying the doctest to produce an output that prints the same on my Linux box and on bsd.math).

If you do apply my patch, then either this ticket should not be closed, or another one should be opened about the printing order issue.


---

Comment by mpatel created at 2010-07-29 06:03:42

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-29 06:03:42

Replying to [comment:6 cwitty]:
> If we decide that the actual problem (different printing across platforms) is not a regression, and doesn't have to be fixed in this release, then I've attached a patch that works around the problem (by modifying the doctest to produce an output that prints the same on my Linux box and on bsd.math).

This seems reasonable.  Are there any objections?  The workaround patch works for me on bsd, sage, and t2.math. 

> If you do apply my patch, then either this ticket should not be closed, or another one should be opened about the printing order issue.

I'll give this ticket a positive review, merge it in 4.5.2.rc0, close it, and open a new one for the printing order problem.


---

Comment by mpatel created at 2010-07-29 06:03:52

Resolution: fixed


---

Comment by mpatel created at 2010-07-29 06:16:46

Replying to [comment:6 cwitty]:

> If you do apply my patch, then either this ticket should not be closed, or another one should be opened about the printing order issue.

I've opened #9632.


---

Comment by mpatel created at 2010-07-29 07:41:06

Burcin, since we haven't released 4.5.2.rc0 yet, I'm happy to make changes to it, e.g., merging a different patch.  Just let us know within a day or so.  I apologize for not giving you more time to examine this ticket.


---

Comment by mpatel created at 2010-08-01 09:53:09

I've "qfinished" 4.5.2.rc0, and we will release it soon.  Shall we continue at #9632?


---

Comment by burcin created at 2010-08-01 10:08:51

Yes, I couldn't see any quick fix which wouldn't effect performance. Ordering of the terms is already a big performance bottleneck in Python. I'd like to fix things properly once instead of adding kludges all around, but I don't have time to do that right now.

I've been sidetracked by other pynac problems since. Sorry for keeping quiet all this time and thanks for your efforts.
