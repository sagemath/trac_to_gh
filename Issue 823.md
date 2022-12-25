# Issue 823: make atlas standard in Sage

archive/issues_000823.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/823\n\n",
    "created_at": "2007-10-04T15:56:26Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "make atlas standard in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/823",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff



Issue created by migration from https://trac.sagemath.org/ticket/823





---

archive/issue_comments_005084.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-04T16:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/823#issuecomment-5084",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005085.json:
```json
{
    "body": "What needs to be done:\n\n* update to 3.8.0\n* use sage_fortran to build the f77 wrapper, the flag --no-f77 doesn't work properly\n* build a complete Lapack by using netlib.org's F77 Lapack\n\nGetting ATLAS into Sage will probably be a coding sprint project during SD6.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-27T06:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/823#issuecomment-5085",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

What needs to be done:

* update to 3.8.0
* use sage_fortran to build the f77 wrapper, the flag --no-f77 doesn't work properly
* build a complete Lapack by using netlib.org's F77 Lapack

Getting ATLAS into Sage will probably be a coding sprint project during SD6.

Cheers,

Michael



---

archive/issue_comments_005086.json:
```json
{
    "body": "new package that should resolve all these issues. \n\nhttp://sage.math.washington.edu/spkgs/atlas-3.8.spkg\n\nOne important point. For atlas to build a correct lapack, we must have already built an lapack and then merge with atlas libs to get a full one. On OSX we don't build lapack  so the above package will fail. To use the above on OSX first install this spkg \n\nhttp://sage.math.washington.edu/spkgs/lapack-20071123.spkg\n\nThis will build lapack even on OSX. Then atlas can be installed.\n\nAlso on OSX even with atlas installed, numpy and scipy build against the accelerate framework still.",
    "created_at": "2007-11-24T00:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/823#issuecomment-5086",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

new package that should resolve all these issues. 

http://sage.math.washington.edu/spkgs/atlas-3.8.spkg

One important point. For atlas to build a correct lapack, we must have already built an lapack and then merge with atlas libs to get a full one. On OSX we don't build lapack  so the above package will fail. To use the above on OSX first install this spkg 

http://sage.math.washington.edu/spkgs/lapack-20071123.spkg

This will build lapack even on OSX. Then atlas can be installed.

Also on OSX even with atlas installed, numpy and scipy build against the accelerate framework still.



---

archive/issue_comments_005087.json:
```json
{
    "body": "I just noticed that building the cvxopt package with this atlas causes a missing symbol error for the cvxopt package\n\n_g95_ioparm\n\nI'm mystified by this. Need to investigate.",
    "created_at": "2007-11-27T06:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/823#issuecomment-5087",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

I just noticed that building the cvxopt package with this atlas causes a missing symbol error for the cvxopt package

_g95_ioparm

I'm mystified by this. Need to investigate.



---

archive/issue_comments_005088.json:
```json
{
    "body": "Ignore the cvxopt package issue, it was a mistake on my part, I think atlas is ready to go.",
    "created_at": "2007-11-28T06:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/823#issuecomment-5088",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

Ignore the cvxopt package issue, it was a mistake on my part, I think atlas is ready to go.



---

archive/issue_comments_005089.json:
```json
{
    "body": "the atlas3.8 package didn't have mabshoff's patch so that the shared objects are copied by make install \n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/atlas-3.8.p1.spkg",
    "created_at": "2007-11-28T22:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/823#issuecomment-5089",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

the atlas3.8 package didn't have mabshoff's patch so that the shared objects are copied by make install 

http://sage.math.washington.edu/home/jkantor/spkgs/atlas-3.8.p1.spkg



---

archive/issue_comments_005090.json:
```json
{
    "body": "Problem: \n\nAtlas does not build shared libraries on OSX. \n\nTHis is because on OSX the atlas build script does \n\nld -melf_i386 -shared -soname libatlas.so -o libatlas.so \\\n        --whole-archive libatlas.a --no-whole-archive -lc -lm\nld: unknown flag: -melf_i386\n\n\nThis is a problem with atlas not knowing that on osx we don't want elf, \n\nprobably should be -dynamiclib or something.",
    "created_at": "2007-11-28T22:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/823#issuecomment-5090",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

Problem: 

Atlas does not build shared libraries on OSX. 

THis is because on OSX the atlas build script does 

ld -melf_i386 -shared -soname libatlas.so -o libatlas.so \
        --whole-archive libatlas.a --no-whole-archive -lc -lm
ld: unknown flag: -melf_i386


This is a problem with atlas not knowing that on osx we don't want elf, 

probably should be -dynamiclib or something.



---

archive/issue_comments_005091.json:
```json
{
    "body": "On OSX the ld options --whole_archive don't exist. \n\nThe following appears to produce a shared atlas from the static one\n\nld -dylib -o libatlas.dylib  -lm -lc -all_load libatlas.a\n\n(-L must be set appropriately)",
    "created_at": "2007-11-29T02:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/823#issuecomment-5091",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

On OSX the ld options --whole_archive don't exist. 

The following appears to produce a shared atlas from the static one

ld -dylib -o libatlas.dylib  -lm -lc -all_load libatlas.a

(-L must be set appropriately)



---

archive/issue_comments_005092.json:
```json
{
    "body": "New package\n\nhttp://sage.math.washington.edu/home/jkantor/atlas-3.8.p2.spkg\n\nThis package fixes problems with the shared libraries lapack creates on linux (the lapack.so doesn't not have the same symbols as lapack.a)\n\nIt also creates libatlas and libcblas shared on OSX using the trick in the previous comment, but I have not yet resolved how to make libf77blas or liblapack shared on OSX.  It might be best \nto not do this on OSX till we create the whole thing. Thoughts",
    "created_at": "2007-11-30T06:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/823#issuecomment-5092",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

New package

http://sage.math.washington.edu/home/jkantor/atlas-3.8.p2.spkg

This package fixes problems with the shared libraries lapack creates on linux (the lapack.so doesn't not have the same symbols as lapack.a)

It also creates libatlas and libcblas shared on OSX using the trick in the previous comment, but I have not yet resolved how to make libf77blas or liblapack shared on OSX.  It might be best 
to not do this on OSX till we create the whole thing. Thoughts



---

archive/issue_comments_005093.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-13T06:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/823#issuecomment-5093",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_000934.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-13T06:42:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/823",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/823#event-934"
}
```
