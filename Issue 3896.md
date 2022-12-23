# Issue 3896: [with spkg, patch - needs review] Upgrade Cython to 0.9.8.1

archive/issues_003896.json:
```json
{
    "body": "Assignee: mabshoff\n\nLots of new features, including c-speed access to NumPy arrays, a memory leak fix in some cpdef calls, and others. \n\nBuilds and passes all tests with the attached patch. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3896\n\n",
    "created_at": "2008-08-19T04:32:02Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "[with spkg, patch - needs review] Upgrade Cython to 0.9.8.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3896",
    "user": "robertwb"
}
```
Assignee: mabshoff

Lots of new features, including c-speed access to NumPy arrays, a memory leak fix in some cpdef calls, and others. 

Builds and passes all tests with the attached patch. 

Issue created by migration from https://trac.sagemath.org/ticket/3896





---

archive/issue_comments_027847.json:
```json
{
    "body": "http://cython.org/cython-0.9.8.1.spkg",
    "created_at": "2008-08-19T04:33:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3896#issuecomment-27847",
    "user": "robertwb"
}
```

http://cython.org/cython-0.9.8.1.spkg



---

archive/issue_comments_027848.json:
```json
{
    "body": "Hi Robert,\n\nI am curious about a couple changes:\n\n* the spkg contains a copy of cython-0.9.8.1.1 which I deleted. That brings the size of the spkg down to 2.1MB from about 4MB.\n* hg status also shows a bunch of deleted files from the repo.\n* Why the rename of ZZ_pX_eis_shift to ZZ_pX_eis_shift_p? Otherwise the patch just seems to remove unneeded variables and declarations.\n\nI am currently building and doctesting with the new Cython.spkg.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-22T20:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3896#issuecomment-27848",
    "user": "mabshoff"
}
```

Hi Robert,

I am curious about a couple changes:

* the spkg contains a copy of cython-0.9.8.1.1 which I deleted. That brings the size of the spkg down to 2.1MB from about 4MB.
* hg status also shows a bunch of deleted files from the repo.
* Why the rename of ZZ_pX_eis_shift to ZZ_pX_eis_shift_p? Otherwise the patch just seems to remove unneeded variables and declarations.

I am currently building and doctesting with the new Cython.spkg.

Cheers,

Michael



---

archive/issue_comments_027849.json:
```json
{
    "body": "This Cython update breaks the Sage library for me:\n\n```\nBuilding sage/matrix/misc.c because it depends on sage/matrix/misc.pyx.\npython2.5 `which cython` --embed-positions --incref-local-binop -I/scratch/mabshoff/release-cycle/sage-3.1.2.alpha0/devel/sage-main -o sage/matrix/misc.c sage/matrix/misc.pyx\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\nimport  sage.structure.element\n\ncdef class RealNumber(sage.structure.element.RingElement)  # forward decl\n\ncdef class RealField(sage.rings.ring.Field):\n    cdef object __weakref__\n               ^\n------------------------------------------------------------\n\n/scratch/mabshoff/release-cycle/sage-3.1.2.alpha0/devel/sage-main/sage/rings/real_mpfr.pxd:18:16: '__weakref__' redeclared \nsage: Error running cython.\nsage: There was an error installing modified sage library code.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-08-22T20:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3896#issuecomment-27849",
    "user": "mabshoff"
}
```

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

archive/issue_comments_027850.json:
```json
{
    "body": "I know I was able to build the entire 3.0.6 with the new Cython, and I thought I tried a -ba with 3.1.1, but I was pretty tired at the time (trying to get ready for my SciPy talk and official release of 0.9.8.1.1) The extra .1 is only important for the distutils package--some files were missing in that (but present in the spkg). \n\nIn any case, tonight I will verify that 3.1.1 builds entirely (the error above is a another redefinition bug, delete that line if you want to get testing) and will make sure the spkg is clean (i.e. no extra builds in there). \n\nThe deleted files probably because we moved some stuff up a level (I believe that's what you were seeing). ZZ_pX_eis_shift ->  ZZ_pX_eis_shift_p was due to a conflict in naming (ZZ_pX_eis_shift is an NTL function in decl.pxi, and then the p-adic numbers also implements a function of the same name). \n\nAs you probably noticed, the new Cython is more strict about having multiple functions/attributes of the same name, which helps eliminate some subtle bugs and confusion (e.g. when a cdef class had the same named attribute as on of its superclasses sometimes the wrong one would get picked up, or gcc would complain or you'd have odd things like two local variables with the same name and different types in a local scope...) This should be the only change needed to the sage codebase.",
    "created_at": "2008-08-22T22:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3896#issuecomment-27850",
    "user": "robertwb"
}
```

I know I was able to build the entire 3.0.6 with the new Cython, and I thought I tried a -ba with 3.1.1, but I was pretty tired at the time (trying to get ready for my SciPy talk and official release of 0.9.8.1.1) The extra .1 is only important for the distutils package--some files were missing in that (but present in the spkg). 

In any case, tonight I will verify that 3.1.1 builds entirely (the error above is a another redefinition bug, delete that line if you want to get testing) and will make sure the spkg is clean (i.e. no extra builds in there). 

The deleted files probably because we moved some stuff up a level (I believe that's what you were seeing). ZZ_pX_eis_shift ->  ZZ_pX_eis_shift_p was due to a conflict in naming (ZZ_pX_eis_shift is an NTL function in decl.pxi, and then the p-adic numbers also implements a function of the same name). 

As you probably noticed, the new Cython is more strict about having multiple functions/attributes of the same name, which helps eliminate some subtle bugs and confusion (e.g. when a cdef class had the same named attribute as on of its superclasses sometimes the wrong one would get picked up, or gcc would complain or you'd have odd things like two local variables with the same name and different types in a local scope...) This should be the only change needed to the sage codebase.



---

archive/issue_comments_027851.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-22T22:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3896#issuecomment-27851",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_027852.json:
```json
{
    "body": "Changing assignee from mabshoff to robertwb.",
    "created_at": "2008-08-22T22:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3896#issuecomment-27852",
    "user": "robertwb"
}
```

Changing assignee from mabshoff to robertwb.



---

archive/issue_comments_027853.json:
```json
{
    "body": "Thanks Robert,\n\nI would also suggest moving the Cython content into a src directory and having an spkg-install script that deletes the old Cython directory in $SAGE_LOCAL/lib/python. When I up- and then downgraded the old Cython did not get wiped out, so I had to delete the old/new Cython manually.\n\nKeep up the good work :)\n\nCheers,\n\nMichael",
    "created_at": "2008-08-22T23:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3896#issuecomment-27853",
    "user": "mabshoff"
}
```

Thanks Robert,

I would also suggest moving the Cython content into a src directory and having an spkg-install script that deletes the old Cython directory in $SAGE_LOCAL/lib/python. When I up- and then downgraded the old Cython did not get wiped out, so I had to delete the old/new Cython manually.

Keep up the good work :)

Cheers,

Michael



---

archive/issue_comments_027854.json:
```json
{
    "body": "Attachment\n\nThis replaces the older patch.",
    "created_at": "2008-08-23T16:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3896#issuecomment-27854",
    "user": "robertwb"
}
```

Attachment

This replaces the older patch.



---

archive/issue_comments_027855.json:
```json
{
    "body": "I updated the patch to fix the issues introduced by 3.1.1. Also, a polished spkg is up at http://sage.math.washington.edu/home/robertwb/cython/cython-0.9.8.1.1.spkg",
    "created_at": "2008-08-23T16:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3896#issuecomment-27855",
    "user": "robertwb"
}
```

I updated the patch to fix the issues introduced by 3.1.1. Also, a polished spkg is up at http://sage.math.washington.edu/home/robertwb/cython/cython-0.9.8.1.1.spkg



---

archive/issue_comments_027856.json:
```json
{
    "body": "The new spkg looks good to me. I did some more cleanup fixes, i.e. make spkg-install executable, add the \"Releases\" section to SPKG.txt. I am currently doing a `-ba` with the new patch applied.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-23T18:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3896#issuecomment-27856",
    "user": "mabshoff"
}
```

The new spkg looks good to me. I did some more cleanup fixes, i.e. make spkg-install executable, add the "Releases" section to SPKG.txt. I am currently doing a `-ba` with the new patch applied.

Cheers,

Michael



---

archive/issue_comments_027857.json:
```json
{
    "body": "The patch looks good, Sage compiles and passes doctests with the patch applied. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-23T19:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3896#issuecomment-27857",
    "user": "mabshoff"
}
```

The patch looks good, Sage compiles and passes doctests with the patch applied. Positive review.

Cheers,

Michael



---

archive/issue_comments_027858.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-23T19:38:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3896#issuecomment-27858",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027859.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-23T19:38:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3896#issuecomment-27859",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha1
