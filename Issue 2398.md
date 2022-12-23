# Issue 2398: free modules over ZZ -- major bug

Issue created by migration from https://trac.sagemath.org/ticket/2398

Original creator: was

Original creation time: 2008-03-05 20:23:03

Assignee: was


```
m = lattice_polytope.read_palp_matrix(r"""4 9
...    0  0  0  0  0  0  0  0  0
...    0  3  0 -2  1 -2 -2  1 -2
...    0  0  3  2  2  5  0  0  3
...    0  0  0  0  0  0  0  0  0""")

sage: Ns = (ZZ^4).submodule(m.columns())
sage: Ns

Free module of degree 4 and rank 2 over Integer Ring
Echelon basis matrix:
[0 0 0 0]
[0 1 0 0]
```


What's with the 0 row above?!!?  That's insanely wrong.


---

Comment by was created at 2008-03-05 20:24:46

This was reported by Andrej Novoseltsov.


---

Comment by jason created at 2008-03-05 23:08:53

More interesting data points:


```
sage: (ZZ^4).submodule([(0, 0, 0, 0), (0, 0, 3, 0), (0, -2, 2, 0), (0, 1, 2, 0)])                         

Free module of degree 4 and rank 2 over Integer Ring
Echelon basis matrix:
[0 2 1 0]
[0 3 0 0]
sage: (ZZ^4).submodule([(0, 0, 3, 0), (0, -2, 2, 0), (0, 1, 2, 0), (0, -2, 5, 0)])

Free module of degree 4 and rank 2 over Integer Ring
Echelon basis matrix:
[0 0 0 0]
[0 1 2 0]
```



---

Comment by jason created at 2008-03-05 23:14:17

And more:


```
Does someone want to review the patch positively?  sage: (ZZ^3).span([(0, 0, 3), (0, -2, 2), (0, 1, 2), (0, -2, 5)])

Free module of degree 3 and rank 2 over Integer Ring
Echelon basis matrix:
[0 0 0]
[0 1 2]
sage: matrix([(0, 0, 3), (0, -2, 2), (0, 1, 2), (0, -2, 5)]).echelon_form()

[0 0 0]
[0 1 2]
[0 0 3]
[0 0 0]
```


I think the problem is the first row of the matrix is the zero row, which is clearly wrong.


---

Comment by jason created at 2008-03-05 23:28:56

Okay, I've traced it back to William's code.  He can take it from there:


```
sage: a=matrix([(0, 0, 3), (0, -2, 2), (0, 1, 2), (0, -2, 5)])
sage: import sage.matrix.matrix_integer_dense_hnf             
sage: sage.matrix.matrix_integer_dense_hnf.hnf(a)             

([0 0 0]
[0 1 2]
[0 0 3]
[0 0 0], [0, 1, 2])
```



---

Comment by jason created at 2008-03-05 23:30:00

Changing the title accordingly.  After fixing this, someone ought to check the first example works correctly.


---

Comment by was created at 2008-03-05 23:33:22

I'm changing this to a block -- it gives wrong answers, which is really serious!


---

Comment by was created at 2008-03-05 23:33:22

Changing priority from critical to blocker.


---

Comment by was created at 2008-03-06 02:47:35

this fixes the bug


---

Attachment

I've attached a patch that fixes the problem.  It was actually potentially fairly
serious, though something one wouldn't see much on "random" input.

The fix involves changing one line (the patch is longer, but only for cosmetic reasons and because of adding a doctest).

I ran the sanity check scripts and this code still works after the patch, by the way.  So that one tiny patch, which is clearly right, doesn't break things.


---

Comment by jason created at 2008-03-06 03:04:10

The patch fixes all of the above examples (and includes the minimal example as a doctest).  It looks good to me.


---

Comment by mabshoff created at 2008-03-07 04:26:23

Resolution: fixed


---

Comment by mabshoff created at 2008-03-07 04:26:23

Merged in Sage 2.10.3.rc3
