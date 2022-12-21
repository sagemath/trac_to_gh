# Issue 3896: [with spkg, patch - needs review] Upgrade Cython to 0.9.8.1

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-08-19 04:32:02

Assignee: mabshoff

Lots of new features, including c-speed access to NumPy arrays, a memory leak fix in some cpdef calls, and others. 

Builds and passes all tests with the attached patch. 


---

Comment by robertwb created at 2008-08-19 04:33:41

http://cython.org/cython-0.9.8.1.spkg


---

Comment by mabshoff created at 2008-08-22 20:15:46

Hi Robert,

I am curious about a couple changes:

 * the spkg contains a copy of cython-0.9.8.1.1 which I deleted. That brings the size of the spkg down to 2.1MB from about 4MB.
 * hg status also shows a bunch of deleted files from the repo.
 * Why the rename of ZZ_pX_eis_shift to ZZ_pX_eis_shift_p? Otherwise the patch just seems to remove unneeded variables and declarations.

I am currently building and doctesting with the new Cython.spkg.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-22 20:32:20

This Cython update breaks the Sage library for me:

```
Building sage/matrix/misc.c because it depends on sage/matrix/misc.pyx.
python2.5 `which cython` --embed-positions --incref-local-binop -I/scratch/mabshoff/release-cycle/sage-3.1.2.alpha0/devel/sage-main -o sage/matrix/misc.c sage/matrix/misc.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...
import  sage.structure.element

cdef class RealNumber(sage.structure.element.RingElement)  # forward decl

cdef class RealField(sage.rings.ring.Field):
    cdef object __weakref__
               ^
------------------------------------------------------------

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha0/devel/sage-main/sage/rings/real_mpfr.pxd:18:16: '__weakref__' redeclared 
sage: Error running cython.
sage: There was an error installing modified sage library code.
```


Cheers,

Michael


---

Comment by robertwb created at 2008-08-22 22:46:39

I know I was able to build the entire 3.0.6 with the new Cython, and I thought I tried a -ba with 3.1.1, but I was pretty tired at the time (trying to get ready for my SciPy talk and official release of 0.9.8.1.1) The extra .1 is only important for the distutils package--some files were missing in that (but present in the spkg). 

In any case, tonight I will verify that 3.1.1 builds entirely (the error above is a another redefinition bug, delete that line if you want to get testing) and will make sure the spkg is clean (i.e. no extra builds in there). 

The deleted files probably because we moved some stuff up a level (I believe that's what you were seeing). ZZ_pX_eis_shift ->  ZZ_pX_eis_shift_p was due to a conflict in naming (ZZ_pX_eis_shift is an NTL function in decl.pxi, and then the p-adic numbers also implements a function of the same name). 

As you probably noticed, the new Cython is more strict about having multiple functions/attributes of the same name, which helps eliminate some subtle bugs and confusion (e.g. when a cdef class had the same named attribute as on of its superclasses sometimes the wrong one would get picked up, or gcc would complain or you'd have odd things like two local variables with the same name and different types in a local scope...) This should be the only change needed to the sage codebase.


---

Comment by robertwb created at 2008-08-22 22:46:39

Changing status from new to assigned.


---

Comment by robertwb created at 2008-08-22 22:46:39

Changing assignee from mabshoff to robertwb.


---

Comment by mabshoff created at 2008-08-22 23:27:42

Thanks Robert,

I would also suggest moving the Cython content into a src directory and having an spkg-install script that deletes the old Cython directory in $SAGE_LOCAL/lib/python. When I up- and then downgraded the old Cython did not get wiped out, so I had to delete the old/new Cython manually.

Keep up the good work :)

Cheers,

Michael


---

Attachment

This replaces the older patch.


---

Comment by robertwb created at 2008-08-23 16:47:05

I updated the patch to fix the issues introduced by 3.1.1. Also, a polished spkg is up at http://sage.math.washington.edu/home/robertwb/cython/cython-0.9.8.1.1.spkg


---

Comment by mabshoff created at 2008-08-23 18:03:58

The new spkg looks good to me. I did some more cleanup fixes, i.e. make spkg-install executable, add the "Releases" section to SPKG.txt. I am currently doing a `-ba` with the new patch applied.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-23 19:38:10

The patch looks good, Sage compiles and passes doctests with the patch applied. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-23 19:38:25

Resolution: fixed


---

Comment by mabshoff created at 2008-08-23 19:38:25

Merged in Sage 3.1.2.alpha1
