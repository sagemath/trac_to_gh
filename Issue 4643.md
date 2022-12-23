# Issue 4643: build system uses leftover .so files

archive/issues_004643.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  robertwb\n\nAs it stands, if you remove a Cython extension from `module_list.py`, and remove all associated files in the sage library, everything builds fine. However, the `.so` files are still there. In particular, if you try to load a pickled object from a class that was defined in that `.pyx` file, it still loads just fine -- in fact, it loads the `.so` and uses that code. \n\nUnfortunately, I don't see an easy fix for this offhand. The problem is that we don't manage the `.so` files ourselves -- we leave that to distutils. If someone has a good idea for how to fix this, I'm happy to help implement it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4643\n\n",
    "created_at": "2008-11-28T08:29:39Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "title": "build system uses leftover .so files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4643",
    "user": "craigcitro"
}
```
Assignee: mabshoff

CC:  robertwb

As it stands, if you remove a Cython extension from `module_list.py`, and remove all associated files in the sage library, everything builds fine. However, the `.so` files are still there. In particular, if you try to load a pickled object from a class that was defined in that `.pyx` file, it still loads just fine -- in fact, it loads the `.so` and uses that code. 

Unfortunately, I don't see an easy fix for this offhand. The problem is that we don't manage the `.so` files ourselves -- we leave that to distutils. If someone has a good idea for how to fix this, I'm happy to help implement it.

Issue created by migration from https://trac.sagemath.org/ticket/4643





---

archive/issue_comments_034952.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-19T14:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4643#issuecomment-34952",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_034953.json:
```json
{
    "body": "Fixed by #16431.",
    "created_at": "2014-08-19T14:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4643#issuecomment-34953",
    "user": "jdemeyer"
}
```

Fixed by #16431.



---

archive/issue_comments_034954.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-08-19T14:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4643#issuecomment-34954",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_034955.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-08-20T20:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4643#issuecomment-34955",
    "user": "vbraun"
}
```

Resolution: fixed
