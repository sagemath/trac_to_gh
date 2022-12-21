# Issue 9607: Doctest failure in latex.rst

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-27 07:00:47

Assignee: mvngu

CC:  ddrake jhpalmieri mvngu rbeezer

Seen on sage.math and bsd.math with Sage 4.5.2.alpha1:

```python
sage -t -long  devel/sage/doc/en/tutorial/latex.rst
**********************************************************************
File "/Users/mpatel/apps/sage-4.5.2.alpha1/devel/sage-main/doc/en/tutorial/latex
.rst", line 459:
    sage: latex.extra_preamble()
Expected:
    '\\usepackage{tikz}\n\\usepackage{tkz-graph}\n\\usepackage{tkz-berge}\n'
Got:
    '\\usepackage{tikz}\n'
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_11
***Test Failed*** 1 failures.
```


This may be caused by #9027.


---

Comment by rbeezer created at 2010-07-27 07:32:01

Almost certainly due to #9027.  I have two builds going and will investigate in the morning.


---

Comment by ddrake created at 2010-07-27 07:51:37

Ah, note that in latex.rst, it does `setup_latex_preamble()`. Here's that entire function:

```
latex.add_package_to_preamble_if_available("tikz")
latex.add_package_to_preamble_if_available("tkz-graph")
latex.add_package_to_preamble_if_available("tkz-berge")
```

So on sage.math, it looks like tkz-graph and tkz-berge are not getting added because they're not available.


---

Comment by mpatel created at 2010-07-27 08:11:05

It seems that none of the three packages is available on t2:

```python
Expected:
    '\\usepackage{tikz}\n\\usepackage{tkz-graph}\n\\usepackage{tkz-berge}\n'
Got:
    ''
```



---

Attachment

Patch marks the test as random, which I think is the right thing to do, not just an expedient.

There is no way to know what extra packages a system will have, and this block of code is meant more as an illustration than as a test.  So in particular, the line in question could even be removed, but then there would be less of the behavior documented.


---

Comment by rbeezer created at 2010-07-27 15:09:29

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-07-27 17:09:15

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-07-27 17:09:15

This looks good to me.

Sorry, I should have caught this when I reviewed the original ticket.


---

Comment by rbeezer created at 2010-07-27 17:50:52

> Sorry, I should have caught this when I reviewed the original ticket.

Well, I know better, it shouldn't have been there.  I have a latex-free system available at the moment, and I suspect #9074 could meet the same fate (I'll check shortly).

Thanks for the quick look at this one.

Rob


---

Comment by mpatel created at 2010-07-29 04:49:22

Resolution: fixed


---

Comment by mpatel created at 2010-07-29 05:36:21

I'll put the ticket number in the commit string before I make 4.5.2.rc0.


---

Attachment


---

Comment by rbeezer created at 2010-07-29 06:08:09

Replying to [comment:8 mpatel]:
> I'll put the ticket number in the commit string before I make 4.5.2.rc0.

Sorry!  New v2 patch has a real commit message, if it is not too late.


---

Comment by mpatel created at 2010-07-29 06:20:31

Replying to [comment:9 rbeezer]:
> Replying to [comment:8 mpatel]:
> > I'll put the ticket number in the commit string before I make 4.5.2.rc0.
> Sorry!  New v2 patch has a real commit message, if it is not too late.

No problem.  I'm merging V2, instead.
