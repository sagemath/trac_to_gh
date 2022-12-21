# Issue 6677: [with patch, needs review] Sequence doesn't know how to typeset itself

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-08-06 11:49:04

Assignee: burcin

It seems that Sequence objects forgot how to typeset themselves somewhere between 3.4.2 and 4.1.

In 3.4.2:


```
sage: res = solve(x^2-2,x)
sage: latex(res)

\left[x  =  -\sqrt{ 2 }, 
 x  =  \sqrt{ 2 }\right]
```


In 4.1:


```
sage: latex(res)

\text{[
x == -sqrt(2),
x == sqrt(2)
]}
sage: latex(res[0])
x = -\sqrt{2}
```


Attached patch adds a `_latex_` method to `sage.structure.sequence.Sequence`.


---

Comment by burcin created at 2009-08-06 12:03:58

Changing status from new to assigned.


---

Comment by burcin created at 2009-08-06 12:03:58

Trac doesn't let me upload the patch. Here it is if anybody wants to review it in the meantime:

http://sage.math.washington.edu/home/burcin/trac_6677-sequence_latex.patch


---

Attachment


---

Comment by jhpalmieri created at 2009-08-20 21:06:03

Okay, I see why this used to work and doesn't anymore: we used to test elements when formatting for LaTeX using `isinstance(x, list)`, and sequences returned True for this.  Now we test using `type(x)` and looking it up in a dictionary, and there is no entry for "sage.structure.sequence.Sequence".  The patch here solves the problem for sequences and includes a doctest.  I have a trivial referee's patch (adds 'r' to the triple quotes at the beginning of the docstring, since there are backslashes in it).


---

Comment by jhpalmieri created at 2009-08-20 21:06:03

Changing priority from major to minor.


---

Attachment

apply on top of the other patch


---

Comment by mvngu created at 2009-08-25 04:29:52

Merged both patches.


---

Comment by mvngu created at 2009-08-25 04:29:52

Resolution: fixed
