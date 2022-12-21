# Issue 7573: Sage crashes if insufficient data is provided for MIP

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-12-01 16:00:50

Assignee: jkantor

CC:  ncohen

This crashes Sage:


```
sage: g = graphs.PetersenGraph()
sage: p = MixedIntegerLinearProgram(maximization=True)
sage: b = p.new_variable()
sage: p.set_objective(sum([b[v] for v in g]))
sage: p.set_binary(b)
sage: p.solve(objective_only=True)
```



---

Comment by malb created at 2009-12-01 16:01:38

Changing status from new to needs_review.


---

Comment by malb created at 2009-12-01 16:01:38

The attached patch fixes the issue for me.


---

Comment by ncohen created at 2009-12-01 16:11:42

Changing status from needs_review to needs_info.


---

Comment by ncohen created at 2009-12-01 16:11:42

Hello !!!

This problem does not seem to exist on the version I am using, with patch #7270 and the new GLPK spkg installed... Did you test it on the current Sage version of both  ?

Nathann


---

Comment by malb created at 2009-12-01 17:15:51

The problem is not fixed in #7270 but I updated the patch to work with #7270.


---

Comment by malb created at 2009-12-01 17:15:51

Changing status from needs_info to needs_review.


---

Comment by ncohen created at 2009-12-01 17:30:32

I just tested your patch and it seems Coin behaves much better than GLPK : the new doctests fails for solver="Coin", as it peacefully returns an exception as it should. Could you add in your test solver="GLPK" to the p.solve() call ?

It sounds like wrapping solveCoin with _sig_on and sig_off is not needed, though it can not hurt to let it stay ;-)

Thank you very much for your help !!!!

Nathann


---

Comment by ncohen created at 2009-12-01 17:30:32

Changing status from needs_review to needs_work.


---

Comment by malb created at 2009-12-01 17:38:27

updated to fit #7270


---

Comment by malb created at 2009-12-01 17:38:51

Changing status from needs_work to needs_review.


---

Attachment

done


---

Comment by ncohen created at 2009-12-01 17:45:04

Applies fines, does its job... :-)


---

Comment by ncohen created at 2009-12-01 17:45:04

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-02 08:07:46

Resolution: fixed
