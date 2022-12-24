# Issue 2326: compiled sparse and dense graph datastructures

archive/issues_002326.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  jason\n\nImplement compiled base classes for graphs, which will be faster than Python based NetworkX classes (especially when accessed from Cython).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2326\n\n",
    "created_at": "2008-02-27T00:00:40Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "compiled sparse and dense graph datastructures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2326",
    "user": "rlm"
}
```
Assignee: rlm

CC:  jason

Implement compiled base classes for graphs, which will be faster than Python based NetworkX classes (especially when accessed from Cython).

Issue created by migration from https://trac.sagemath.org/ticket/2326





---

archive/issue_comments_015481.json:
```json
{
    "body": "The patches on this ticket will depend on those in #2307.",
    "created_at": "2008-02-27T00:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2326#issuecomment-15481",
    "user": "rlm"
}
```

The patches on this ticket will depend on those in #2307.



---

archive/issue_comments_015482.json:
```json
{
    "body": "Don't know what's up with the HTML preview on the second patch, but...",
    "created_at": "2008-02-27T01:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2326#issuecomment-15482",
    "user": "rlm"
}
```

Don't know what's up with the HTML preview on the second patch, but...



---

archive/issue_comments_015483.json:
```json
{
    "body": "For the results of `sage -t -valgrind` on the new code, see\n\nsparse_graph:\n\nhttp://sage.math.washington.edu/home/rlmill/.sage/valgrind/sage-memcheck.12219\n\ndense_graph:\n\nhttp://sage.math.washington.edu/home/rlmill/.sage/valgrind/sage-memcheck.18970\n\nThey certainly look clean to me :)",
    "created_at": "2008-02-28T19:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2326#issuecomment-15483",
    "user": "rlm"
}
```

For the results of `sage -t -valgrind` on the new code, see

sparse_graph:

http://sage.math.washington.edu/home/rlmill/.sage/valgrind/sage-memcheck.12219

dense_graph:

http://sage.math.washington.edu/home/rlmill/.sage/valgrind/sage-memcheck.18970

They certainly look clean to me :)



---

archive/issue_comments_015484.json:
```json
{
    "body": "Alternatively,\n\nsparse_graph:\n\nhttp://sage.math.washington.edu/home/rlmill/sage-memcheck.12219\n\ndense_graph:\n\nhttp://sage.math.washington.edu/home/rlmill/sage-memcheck.18970",
    "created_at": "2008-02-28T20:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2326#issuecomment-15484",
    "user": "rlm"
}
```

Alternatively,

sparse_graph:

http://sage.math.washington.edu/home/rlmill/sage-memcheck.12219

dense_graph:

http://sage.math.washington.edu/home/rlmill/sage-memcheck.18970



---

archive/issue_comments_015485.json:
```json
{
    "body": "Attachment [2326-final.patch](tarball://root/attachments/some-uuid/ticket2326/2326-final.patch) by jason created at 2008-03-01 10:24:41\n\nSorry for the caps, but I just wanted to make sure mabshoff saw it :)  It looks good to me.",
    "created_at": "2008-03-01T10:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2326#issuecomment-15485",
    "user": "jason"
}
```

Attachment [2326-final.patch](tarball://root/attachments/some-uuid/ticket2326/2326-final.patch) by jason created at 2008-03-01 10:24:41

Sorry for the caps, but I just wanted to make sure mabshoff saw it :)  It looks good to me.



---

archive/issue_comments_015486.json:
```json
{
    "body": "Merged 2326-final.patch in Sage 2.10.3.rc1",
    "created_at": "2008-03-01T23:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2326#issuecomment-15486",
    "user": "mabshoff"
}
```

Merged 2326-final.patch in Sage 2.10.3.rc1



---

archive/issue_comments_015487.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-01T23:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2326#issuecomment-15487",
    "user": "mabshoff"
}
```

Resolution: fixed
