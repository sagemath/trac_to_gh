# Issue 7333: CBC spkg

Issue created by migration from https://trac.sagemath.org/ticket/7333

Original creator: ncohen

Original creation time: 2009-10-28 17:14:38

Assignee: tbd

Since the new version of sage.numerical.mip, which is now in the standard distribution of Sage, the old CBC spkg was not working anymore because of many changes in the structure of class MIP. This patch fixes this, by mainly changing some variables' names to the new ones, and Cythonizing part of the code when it was possible !

The spkg is available in two locations :
    * On sage.math at ~ncohen/cbc-2.3.p1.spkg
    * At http://www-sop.inria.fr/members/Nathann.Cohen/cbc-2.3.p1.spkg

Thank you for your help !!!!


---

Comment by ncohen created at 2009-10-28 17:15:00

Changing status from new to needs_review.


---

Comment by malb created at 2009-12-08 13:46:46

I get a bunch of `--optional` doctest errors if only CBC but not GLPK is installed. Most of them are fine (they point out that I need GLPK), but this one isn't:


```
    sage: p.get_values(x[3]) # optional - requires Glpk or COIN-OR/CBC
Expected:
    2.0
Got:
    0.0
```


Other than that, it looks fine. I have been using it over the last week or so and cannot report any problems.


---

Comment by malb created at 2009-12-08 13:46:46

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2009-12-08 14:18:21

I should have got rid of this before... :p

This is just caused by the fact that the problem that is optimized is symmetric in the two variables x[3] and y. CBC returnd x[3] set to two, and Coin returns the other one to 2, both being good answers :p

But I thought this had been updated... Did you test it on the last alpha version ?


---

Comment by malb created at 2009-12-08 14:26:48

Yes, alpha1.


---

Comment by ncohen created at 2009-12-08 14:28:31

Sorry, then I did not check on the good file. I can not find any occurrence of p.get_values(x[3]) in mip.pyx. Could you tell me which file contains it please ? :-)

I'll fix it immediately after !!!

Nathann


---

Comment by malb created at 2009-12-08 14:46:55

Line 477:


```
        EXAMPLE::

            sage: p = MixedIntegerLinearProgram()
            sage: x = p.new_variable()
            sage: y = p.new_variable(dim=2)
            sage: p.set_objective(x[3] + y[2][9] + x[5])
            sage: p.add_constraint(x[3] + y[2][9] + 2*x[5], max=2)
            sage: p.solve() # optional - requires Glpk or COIN-OR/CBC
            2.0
            sage: #
            sage: # Returns the optimal value of x[3]
>>>         sage: p.get_values(x[3]) # optional - requires Glpk or COIN-OR/CBC
            2.0
```



---

Comment by malb created at 2009-12-08 14:49:50

Ah, I was talking about vanilla alpha1, while you are probably talking about #7561. Thus it might be fixed already since #7561 is in rc0.


---

Comment by ncohen created at 2009-12-08 14:57:11

Yes, sorry for the misunderstanding :-)


---

Comment by malb created at 2009-12-08 16:49:24

Changing status from needs_work to needs_review.


---

Comment by malb created at 2009-12-08 16:49:35

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2009-12-08 16:51:14

Thank you ! :-)


---

Comment by mhansen created at 2009-12-09 02:54:50

Merged in with the optional packages.


---

Comment by mhansen created at 2009-12-09 02:54:50

Resolution: fixed
