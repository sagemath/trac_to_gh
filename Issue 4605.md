# Issue 4605: Update Cython to 0.10.2 (latest stable upstream)

archive/issues_004605.json:
```json
{
    "body": "Assignee: @robertwb\n\nCython 0.10.2 fixes a important bug that resolves an issue so that #4206 can be merged.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4605\n\n",
    "created_at": "2008-11-24T20:49:40Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Update Cython to 0.10.2 (latest stable upstream)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4605",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @robertwb

Cython 0.10.2 fixes a important bug that resolves an issue so that #4206 can be merged.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4605





---

archive/issue_comments_034448.json:
```json
{
    "body": "See http://sage.math.washington.edu/home/robertwb/cython/cython-0.10.2.spkg",
    "created_at": "2008-11-25T22:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34448",
    "user": "https://github.com/robertwb"
}
```

See http://sage.math.washington.edu/home/robertwb/cython/cython-0.10.2.spkg



---

archive/issue_comments_034449.json:
```json
{
    "body": "Thanks Robert,\n\nI am doing a full -ba followed by a full test run. The spkg itself looks good, the only thing we should add in the long term is a version change history in SPKG.txt. For now I don't care too much about that.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T22:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34449",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Thanks Robert,

I am doing a full -ba followed by a full test run. The spkg itself looks good, the only thing we should add in the long term is a version change history in SPKG.txt. For now I don't care too much about that.

Cheers,

Michael



---

archive/issue_comments_034450.json:
```json
{
    "body": "I get the following failure:\n\n```\npython2.5 `which cython` --embed-positions --incref-local-binop -I/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main -o sage/rings/real_rqdf.cpp sage/rings/real_rqdf.pyx\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\ncdef extern from \"qd/qd_real.h\":\n\n    ctypedef struct qd \"qd_real\":\n        # Members\n        double *x\n        qd _pi\n          ^\n------------------------------------------------------------\n\n/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:21:11: Struct cannot contain itself as a member.\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\n    ctypedef struct qd \"qd_real\":\n        # Members\n        double *x\n        qd _pi\n        qd _log2\n          ^\n------------------------------------------------------------\n\n/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:22:11: Struct cannot contain itself as a member.\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ctypedef struct qd \"qd_real\":\n        # Members\n        double *x\n        qd _pi\n        qd _log2\n        qd _nan\n          ^\n------------------------------------------------------------\n\n/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:23:11: Struct cannot contain itself as a member.\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n    ctypedef struct qd \"qd_real\":\n        # Members\n        double *x\n        qd _pi\n        qd _log2\n        qd _nan\n          ^\n------------------------------------------------------------\n\n/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:23:11: Struct cannot contain itself as a member.\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        # Members\n        double *x\n        qd _pi\n        qd _log2\n        qd _nan\n        qd _e\n          ^\n------------------------------------------------------------\n\n/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:24:11: Struct cannot contain itself as a member.\n\nError converting Pyrex file to C:\n\n\nError running command, exited with status 256.\nsage: There was an error installing modified sage library code.  \n\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T23:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34450",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I get the following failure:

```
python2.5 `which cython` --embed-positions --incref-local-binop -I/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main -o sage/rings/real_rqdf.cpp sage/rings/real_rqdf.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...
cdef extern from "qd/qd_real.h":

    ctypedef struct qd "qd_real":
        # Members
        double *x
        qd _pi
          ^
------------------------------------------------------------

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:21:11: Struct cannot contain itself as a member.

Error converting Pyrex file to C:
------------------------------------------------------------
...

    ctypedef struct qd "qd_real":
        # Members
        double *x
        qd _pi
        qd _log2
          ^
------------------------------------------------------------

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:22:11: Struct cannot contain itself as a member.

Error converting Pyrex file to C:
------------------------------------------------------------
...
    ctypedef struct qd "qd_real":
        # Members
        double *x
        qd _pi
        qd _log2
        qd _nan
          ^
------------------------------------------------------------

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:23:11: Struct cannot contain itself as a member.
Error converting Pyrex file to C:
------------------------------------------------------------
...
    ctypedef struct qd "qd_real":
        # Members
        double *x
        qd _pi
        qd _log2
        qd _nan
          ^
------------------------------------------------------------

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:23:11: Struct cannot contain itself as a member.

Error converting Pyrex file to C:
------------------------------------------------------------
...
        # Members
        double *x
        qd _pi
        qd _log2
        qd _nan
        qd _e
          ^
------------------------------------------------------------

/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage-main/sage/rings/real_rqdf.pxd:24:11: Struct cannot contain itself as a member.

Error converting Pyrex file to C:


Error running command, exited with status 256.
sage: There was an error installing modified sage library code.  

```


Cheers,

Michael



---

archive/issue_comments_034451.json:
```json
{
    "body": "I am actually surprised that the issue pops up with a stable release :p\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T23:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34451",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am actually surprised that the issue pops up with a stable release :p

Cheers,

Michael



---

archive/issue_comments_034452.json:
```json
{
    "body": "This was to catch a gcc compiler error. Surely that typedef is wrong...",
    "created_at": "2008-11-25T23:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34452",
    "user": "https://github.com/robertwb"
}
```

This was to catch a gcc compiler error. Surely that typedef is wrong...



---

archive/issue_comments_034453.json:
```json
{
    "body": "Replying to [comment:5 robertwb]:\n> This was to catch a gcc compiler error. Surely that typedef is wrong...\n\nWasn't this the \"recursive\" definition issue the other day on the Cython-dev list?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-26T00:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34453",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 robertwb]:
> This was to catch a gcc compiler error. Surely that typedef is wrong...

Wasn't this the "recursive" definition issue the other day on the Cython-dev list?

Cheers,

Michael



---

archive/issue_comments_034454.json:
```json
{
    "body": "Yes. A struct can contain a pointer to itself (which was the error on cython-devel), but it can't actually contain itself. Before gcc would choke on such a definition.",
    "created_at": "2008-11-26T00:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34454",
    "user": "https://github.com/robertwb"
}
```

Yes. A struct can contain a pointer to itself (which was the error on cython-devel), but it can't actually contain itself. Before gcc would choke on such a definition.



---

archive/issue_comments_034455.json:
```json
{
    "body": "Oh, it's a C++ class pretending to be a struct. \n\nI had thought it was safe because it moved a gcc compile error into a Cython compile error, but of course extern declarations don't actually get produced and may (as in this case) be fake structs. I'll fix this. \n\nA new spkg is up, though as before my own sage -ba is still in progress.",
    "created_at": "2008-11-26T00:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34455",
    "user": "https://github.com/robertwb"
}
```

Oh, it's a C++ class pretending to be a struct. 

I had thought it was safe because it moved a gcc compile error into a Cython compile error, but of course extern declarations don't actually get produced and may (as in this case) be fake structs. I'll fix this. 

A new spkg is up, though as before my own sage -ba is still in progress.



---

archive/issue_comments_034456.json:
```json
{
    "body": "Replying to [comment:8 robertwb]:\n> Oh, it's a C++ class pretending to be a struct. \n> \n> I had thought it was safe because it moved a gcc compile error into a Cython compile error, but of course extern declarations don't actually get produced and may (as in this case) be fake structs. I'll fix this. \n\nCool.\n\n> A new spkg is up, though as before my own sage -ba is still in progress. \n\nUsing eight CPUs I got passed the Cython phase, so things should be loooking good. If the tests pass this will turn into a positive revivew.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-26T01:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34456",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:8 robertwb]:
> Oh, it's a C++ class pretending to be a struct. 
> 
> I had thought it was safe because it moved a gcc compile error into a Cython compile error, but of course extern declarations don't actually get produced and may (as in this case) be fake structs. I'll fix this. 

Cool.

> A new spkg is up, though as before my own sage -ba is still in progress. 

Using eight CPUs I got passed the Cython phase, so things should be loooking good. If the tests pass this will turn into a positive revivew.

Cheers,

Michael



---

archive/issue_comments_034457.json:
```json
{
    "body": "Thanks. Sage -ba just succeeded on my machine too.",
    "created_at": "2008-11-26T01:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34457",
    "user": "https://github.com/robertwb"
}
```

Thanks. Sage -ba just succeeded on my machine too.



---

archive/issue_comments_034458.json:
```json
{
    "body": "Positive review, but I am running doctests to be 100% certain. Thanks for the quick fix.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-26T01:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34458",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review, but I am running doctests to be 100% certain. Thanks for the quick fix.

Cheers,

Michael



---

archive/issue_comments_034459.json:
```json
{
    "body": "Thanks for the quick review and bug catch :).",
    "created_at": "2008-11-26T01:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34459",
    "user": "https://github.com/robertwb"
}
```

Thanks for the quick review and bug catch :).



---

archive/issue_comments_034460.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-26T07:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34460",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034461.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha1",
    "created_at": "2008-11-26T07:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34461",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha1



---

archive/issue_comments_034462.json:
```json
{
    "body": "Thanks for getting this in!",
    "created_at": "2008-11-26T16:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4605#issuecomment-34462",
    "user": "https://github.com/jasongrout"
}
```

Thanks for getting this in!
