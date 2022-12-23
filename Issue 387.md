# Issue 387: Inconsistencies with IntegerMod subtypes

Issue created by migration from https://trac.sagemath.org/ticket/387

Original creator: nbruin

Original creation time: 2007-06-12 20:56:32

Assignee: somebody

CC:  dmharvey@math.harvard.edu

The following bug was found by Thea Gegenberg. There seems to be in inconsistency in how elements in a ring Integers(D) for a bigger D are represented and there don't seem to be automatic coercions between the different representatives.

The culprits are IntegerMod_int, IntegerMod_int64 and IntegerMod_gmp (not illustrated here, but with bigger D similar errors arise wrt. gmp.)

This code illustrates the problem:


```
A=matrix([(70, 49, -20, -34, 57), (-49, -14, 95, 43, 85), (-95, -63, 68, 52, 12), (11,
-16, -50, 43, 76), (-55, 83, 55, 40, -14)])
D=A.determinant()
R=Integers(D)
MD=MatrixSpace(R,A.nrows(),A.ncols())
AD=MD(A)
# You would expect elements of R and entries of AD to be of exactly the same type.
# this is not the case, however:
print parent(AD.row(1)[1])
print parent(R(3))
# Indeed, the types of these are not the same:
print type(AD.row(1)[1])
print type(R(3))
# and this has consequences: You'd expect the following to work, but it gives an error:
R(3)*AD.row(1)
```



---

Comment by dmharvey created at 2007-08-28 18:51:12

Changing assignee from somebody to dmharvey.


---

Comment by mabshoff created at 2007-08-30 12:49:06

I think this issue can be closed:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.3.alpha2, Release Date: 2007-08-29                |
| Type notebook() for the GUI, and license() for information.        |
sage: A=matrix([(70, 49, -20, -34, 57), (-49, -14, 95, 43, 85), (-95, -63, 68, 52, 12), (11,
....: -16, -50, 43, 76), (-55, 83, 55, 40, -14)])
sage: D=A.determinant()
sage: R=Integers(D)
sage: MD=MatrixSpace(R,A.nrows(),A.ncols())
sage: AD=MD(A)
sage: # You would expect elements of R and entries of AD to be of exactly the same type.
sage: # this is not the case, however:
sage: print parent(AD.row(1)[1])
Ring of integers modulo 1240031145
sage: print parent(R(3))
Ring of integers modulo 1240031145
sage: # Indeed, the types of these are not the same:
sage: print type(AD.row(1)[1])
<type 'sage.rings.integer_mod.IntegerMod_int64'>
sage: print type(R(3))
<type 'sage.rings.integer_mod.IntegerMod_int64'>
sage: # and this has consequences: You'd expect the following to work, but it gives an error:
sage: R(3)*AD.row(1)
(1240030998, 1240031103, 285, 129, 255)
```

Cheers,

Reassigned to 2.8.3.

Michael


---

Comment by robertwb created at 2007-09-06 23:17:19

Is there a reason this is still open, looks good to me...


---

Comment by was created at 2007-09-07 04:20:02

Resolution: fixed
