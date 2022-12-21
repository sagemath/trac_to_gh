# Issue 1834: General linear group over ZZ hangs in __call__

Issue created by migration from Trac.

Original creator: kohel

Original creation time: 2008-01-18 16:42:33

Assignee: was

CC:  alexghitza

sage: G = GL(3,GF(101))
sage: G([[1,0,1],[0,1,0],[0,0,1]])

[1 0 1]
[0 1 0]
[0 0 1]

works fine, but

sage: G = GL(3,ZZ)
sage: G([[1,0,1],[0,1,0],[0,0,1]])

This should not try to find a solution to the word problem.




---

Comment by AlexGhitza created at 2008-08-29 13:37:59

This has been around for a while, and it's been bugging me.  I fixed it by writing methods !__call!__ and !__contains!__ for the class GeneralLinearGroup_generic, so that the GAP ones (which hang over ZZ) don't get used.  A pleasant side effect is that things are now faster for the cases that were working before (i.e. over finite fields):

before:

```
sage: G = GL(5, GF(next_prime(6*10^4)))                                    
sage: m = [[1,0,1,0,2],[0,1,0,1,1],[0,0,1,0,0],[0,0,0,1,1],[0,0,0,0,1]]                              
sage: timeit("G(m)")                                                                                     
25 loops, best of 3: 9.56 ms per loop
```


after:

```
sage: G = GL(5, GF(next_prime(6*10^4)))                                    
sage: m = [[1,0,1,0,2], [0,1,0,1,1], [0,0,1,0,0], [0,0,0,1,1], [0,0,0,0,1]]                              
sage: timeit("G(m)")                                                                                     
625 loops, best of 3: 459 µs per loop
```


The same issue comes up for all the matrix groups.  For the moment, I have only dealt with the really easy cases of GL and SL.  If this gets approved and merged, I will open a new ticket for the other classes of groups and deal with them in a similar way.


---

Comment by AlexGhitza created at 2008-09-01 09:15:04

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2008-09-01 10:03:12

Changing status from new to assigned.


---

Comment by cremona created at 2008-09-01 19:38:43

Changing component from algebraic geometry to linear algebra.


---

Comment by cremona created at 2008-09-01 19:38:43

Basically ok, but I would make the following changes to both cases (GL and SL):

Use a try: except: block to catch when coercion in the matrix space fails, with the error message "Cannot coerce ... to a matrix".  Then catch the non-invertible matrices in the GL case with the error message "... is not an invertible matrix", and similarly in the SL case with "... does not have determinant 1".

I think this alternative error handling will produce better output.

PS As this is not "algebraic geometry" I changed the Component to Linear Algebra


---

Attachment

Good idea.  I have made the changes and replaced the patch with a new one.


---

Comment by cremona created at 2008-09-02 08:37:33

Excellent.  These are much more helpful messages.

The new patch applies ok to 3.1.2.alpha3 (there was a little fuzz:

```
applying /home/john/1834-gl_z_call.patch
patching file sage/groups/matrix_gps/matrix_group.py
Hunk #1 succeeded at 13 with fuzz 1 (offset 3 lines).
```

but nothing serious).   All doctests in sage.groups.matrix_groups pass.  Publish!


---

Comment by mabshoff created at 2008-09-02 11:02:34

Merged in Sage 3.1.2.alpha4


---

Comment by mabshoff created at 2008-09-02 11:02:34

Resolution: fixed
