# Issue 2299: [with patch, needs review] add zero_matrix constructor.

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-02-25 08:10:33

Assignee: malb

CC:  ncalexan

Keywords: zero matrix identity one

This adds the `zero_matrix` convenience constructor, just like `identity_matrix`.


---

Comment by malb created at 2008-02-25 11:29:23

Changing assignee from malb to was.


---

Comment by malb created at 2008-02-25 11:29:23

Changing component from commutative algebra to linear algebra.


---

Attachment

You replaced "n x n" by "$n \times n$" which reads nicer if typesetted. However, it is harder to comprehend from the command line (`foo?`).

I am not sure that we need `identity_matrix` and `zero_matrix` (i.e. the functional versions of `MS(0)` and `MS(1)`) but that is a matter of taste.


---

Comment by ncalexan created at 2008-02-25 18:07:24

I really want `identity_matrix` and `zero_matrix` because I often don't want to name the matrix space in advance.  `MS(0)` requires me to create said space first.

As for latex in docstrings... I don't care either way.  I think it should be latex but I parse simple latex from tex without trouble.


---

Comment by was created at 2008-02-25 18:09:50

Just a quick remark.  You can make a zero matrix using the matrix function:


```
sage: matrix(ZZ, 2,3)
[0 0 0]
[0 0 0]
```


I don't think that's a good reason not to add zero_matrix and identity_matrix
functions though, both of which I would like to have too.


---

Comment by ncalexan created at 2008-02-25 18:17:43

I think zero_ and identity_ declare programmer intent nicely.  Will someone say positive or negative and this either goes to the bit-bucket or gets applied?


---

Comment by was created at 2008-02-25 18:42:07

REFEREE REPORT:

I definitely think these functions should go in, but with TWO caveats. 

1. I think the zero_matrix should have an option to be nonsquare though.  Please post another patch that adds that, so, e.g.,


```
sage: zero_matrix(ZZ, 2,3)
[0 0 0]
[0 0 0]
```


works. 

2. There should be a sparse option for both zero_matrix and
identity_matrix.


```
sage: zero_matrix(ZZ, 2,3, sparse=True).parent()
Full MatrixSpace of 2 by 3 sparse matrices over Integer Ring
```


 -- William


---

Attachment


---

Comment by ncalexan created at 2008-02-25 19:14:48

`2299-ncalexan-zero-matrix-2.patch` should apply without the previous patch, and should address the referee's comments.

I generated this patch using hg diff between two revisions, not hg export.  Let me know if it's not okay.


---

Comment by mhansen created at 2008-02-27 22:08:00

Works for me in 2.10.3.alpha0.  Note that only the last patch should be apply and that it is a "raw" patch.


---

Attachment


---

Comment by mhansen created at 2008-02-27 22:16:39

I just realized this conflicts with #874.  #874 should be applied first, and then 2299.patch should be applied.


---

Comment by mabshoff created at 2008-02-28 00:48:29

Resolution: fixed


---

Comment by mabshoff created at 2008-02-28 00:48:29

Merged 2299.patch in Sage 2.10.3.rc0
