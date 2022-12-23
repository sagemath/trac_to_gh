# Issue 8633: remove more instances of 'texttt' from jsmath output

Issue created by migration from https://trac.sagemath.org/ticket/8633

Original creator: jhpalmieri

Original creation time: 2010-03-30 17:40:22

Assignee: tbd

Try this in the notebook with the "Typeset" box checked:

```
random_matrix(ZZ, 5, 5).eigenvalues()
```

You will see a box saying "Unknown control sequence '\texttt'".  The attached patch fixes this by replacing "\texttt" with "\hbox" before processing the LaTeX string with jsMath.

This was reported on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/b35dc4f890f48677?tvc=2).


---

Attachment

Works for me (I had another case of \texttt - thank you for providing such a timely patch!) and for the given code.

Is it ready for review? The patch does not add any doctests, but I am not sure if it is possible to test such an issue in doctests. At least it does not break any existing ones.


---

Comment by jhpalmieri created at 2010-04-01 01:55:32

Yes, it's ready for review.


---

Comment by jhpalmieri created at 2010-04-01 01:55:32

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-04-01 02:12:36

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 18:54:38

Merged "trac_8633-texttt.patch" in 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-16 18:54:38

Resolution: fixed


---

Comment by jason created at 2010-09-22 02:35:43

I get the same problem on 4.4.2 with


```
html.table([random_matrix(ZZ, 5, 5).eigenvalues()])
```


even though the example in this ticket does work.


---

Comment by jhpalmieri created at 2010-09-22 03:18:53

I think that the two calls to `latex` in sage/misc/html.py need to be changed from

```
latex(XXX)
```

to 

```
latex(XXX).replace('\\texttt','\\hbox')
```

Open another ticket, cc me, and post a patch.


---

Comment by jhpalmieri created at 2010-09-22 03:19:15

(Oh, and add a doctest in the patch.)
