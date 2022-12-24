# Issue 3250: Parent does not have a cdef class default hash

archive/issues_003250.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  robertwb\n\nParent does has a default hash for python classes, but not for cython classes.  This leads to very subtle bugs where converting a python class to a cython class can result in coercion failing mysteriously.  Either coercion should be more descriptive with its error messages resulting from lack of a hash function or Parent should get a default cdef hash function.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3250\n\n",
    "created_at": "2008-05-18T02:33:23Z",
    "labels": [
        "coding theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Parent does not have a cdef class default hash",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3250",
    "user": "gfurnish"
}
```
Assignee: rlm

CC:  robertwb

Parent does has a default hash for python classes, but not for cython classes.  This leads to very subtle bugs where converting a python class to a cython class can result in coercion failing mysteriously.  Either coercion should be more descriptive with its error messages resulting from lack of a hash function or Parent should get a default cdef hash function.

Issue created by migration from https://trac.sagemath.org/ticket/3250





---

archive/issue_comments_022487.json:
```json
{
    "body": "Changing assignee from rlm to robertwb.",
    "created_at": "2008-05-18T02:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3250#issuecomment-22487",
    "user": "gfurnish"
}
```

Changing assignee from rlm to robertwb.



---

archive/issue_comments_022488.json:
```json
{
    "body": "Changing component from coding theory to coercion.",
    "created_at": "2008-05-18T02:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3250#issuecomment-22488",
    "user": "gfurnish"
}
```

Changing component from coding theory to coercion.



---

archive/issue_comments_022489.json:
```json
{
    "body": "Hashing/comparison is being addressed in the new coercion model.",
    "created_at": "2008-06-12T23:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3250#issuecomment-22489",
    "user": "robertwb"
}
```

Hashing/comparison is being addressed in the new coercion model.



---

archive/issue_comments_022490.json:
```json
{
    "body": "Hi Robert,\n\nI assume this has been addressed by now? If so please close this ticket as fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-10T13:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3250#issuecomment-22490",
    "user": "mabshoff"
}
```

Hi Robert,

I assume this has been addressed by now? If so please close this ticket as fixed.

Cheers,

Michael



---

archive/issue_comments_022491.json:
```json
{
    "body": "We didn't do as many changes to the comparison/hashing model as we had intended starting out, mainly because it just got to be too much on top of everything else... \n\nHowever, short of a specific example, this ticket is rather vague, and I have never run into this.",
    "created_at": "2008-12-11T07:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3250#issuecomment-22491",
    "user": "robertwb"
}
```

We didn't do as many changes to the comparison/hashing model as we had intended starting out, mainly because it just got to be too much on top of everything else... 

However, short of a specific example, this ticket is rather vague, and I have never run into this.



---

archive/issue_comments_022492.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2018-03-08T10:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3250#issuecomment-22492",
    "user": "jdemeyer"
}
```

Resolution: invalid
