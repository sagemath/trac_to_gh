# Issue 6311: optional doctest failure -- supersingular_j

Issue created by migration from https://trac.sagemath.org/ticket/6311

Original creator: was

Original creation time: 2009-06-16 14:40:29

Assignee: tbd


```
sage -t -long --optional devel/sage/sage/modular/ssmod/ssmod.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/modular/ssmod/ssmod.py", line 571:
    sage: supersingular_j(GF(15073^2,'a'))  # optional -- requires database
Expected:
    10630*a + 6033
Got:
    4443*a + 13964
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_ssmod.py
	 [20.9 s]
```



---

Comment by chapoton created at 2013-09-21 12:02:54

This failure is still there in 5.12.beta4.

The results are related by the action of the Frobenius involution. So the problem is not too bad.


---

Comment by chapoton created at 2014-02-21 13:39:03

Now the doctest is

```
sage -t --optional=all src/sage/modular/ssmod/ssmod.py
```



---

Comment by chapoton created at 2015-03-24 20:31:46

what should we do here ? just change the doctest result ?


---

Comment by chapoton created at 2015-03-24 20:31:46

Changing status from new to needs_info.


---

Comment by jdemeyer created at 2015-03-24 22:40:01

Changing status from needs_info to needs_review.


---

Comment by jdemeyer created at 2015-03-24 22:40:01

Changing component from packages: optional to doctest framework.


---

Comment by jdemeyer created at 2015-03-24 22:40:01

New commits:


---

Comment by jdemeyer created at 2015-03-24 22:40:22

Remove `# optional` in #18049.


---

Comment by git created at 2015-03-24 23:36:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jdemeyer created at 2015-03-24 23:43:16

Changing component from doctest framework to number theory.


---

Comment by jdemeyer created at 2015-03-24 23:43:16

I think we can just close this as "duplicate" of #18049.


---

Comment by jdemeyer created at 2015-03-24 23:43:16

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-03-25 00:26:13

Resolution: duplicate
