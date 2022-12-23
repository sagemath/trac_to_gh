# Issue 1686: arpack -- illegal instruction when built on Pentium 4 using gfortran

Issue created by migration from https://trac.sagemath.org/ticket/1686

Original creator: was

Original creation time: 2008-01-04 23:54:22

Assignee: jkantor

The file

```
SAGE_ROOT/devel/sage/sage/numerical/tests.py
```


contains this doctest:


```
sage: from scipy import sparse
sage: import arpack

#Test arpack
#This matrix is the finite difference approximation to
# the eigenvalue problem
#d^2f/dx^2=\lambda f, on [0,\pi], which boundary values 0
# The lowest eigenvalue calulated should be close to 1
sage: import scipy
sage: n=scipy.zeros((3,500))
sage: n[0,:]=-1
sage: n[1,:]=2
sage: n[2,:]=-1
sage: A=sparse.spdiags(n,[-1,0,1],int(500),int(500))
sage: e,v=arpack.speigs.ARPACK_eigs(A.matvec,500,6,which='SM')
sage: e[0]*float(501/pi)**2
0.999............
```


The line 

```
sage: e,v=arpack.speigs.ARPACK_eigs(A.matvec,500,6,which='SM')
```

crashes on at least one Pentium 4 machine with Sage built using gfortran.

If any sage developers replicate this on their personal hardware, please
email sage-devel.  We have removed the above doctest until this gets fixed. 
(See attached patch.)


---

Attachment

patch by William to disable the doctest for now


---

Comment by mabshoff created at 2008-01-05 00:14:42

I merged trac-1686-disable.patch into Sage 2.9.2.rc1 - but this ticket will remain open for now until we find a real solution.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-16 01:38:50

Changing assignee from jkantor to mabshoff.


---

Comment by mabshoff created at 2008-07-16 01:38:50

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-16 01:38:50

My assumption is that #2303 fixed this issue, too. So we should apply the reverse of the doctest patch and close this ticket.

There is no actual patch to review yet, just consider the reversing of the above doctest patch.

Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-11 05:46:50

Verbal positive review by William. I applied the reverse of the above patch and committed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-11 05:47:05

Merged in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-11 05:47:05

Resolution: fixed
