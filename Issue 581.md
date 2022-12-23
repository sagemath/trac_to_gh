# Issue 581: apply LinBox's Changeset 2803 - this removes the workaround for #498 and fixes the problem itself

archive/issues_000581.json:
```json
{
    "body": "Assignee: mabshoff\n\nSee http://groups.google.com/group/linbox-use/t/513b47fcedb0f736 for details.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/581\n\n",
    "created_at": "2007-09-03T16:39:24Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "apply LinBox's Changeset 2803 - this removes the workaround for #498 and fixes the problem itself",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/581",
    "user": "mabshoff"
}
```
Assignee: mabshoff

See http://groups.google.com/group/linbox-use/t/513b47fcedb0f736 for details.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/581





---

archive/issue_comments_003004.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-03T16:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/581#issuecomment-3004",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003005.json:
```json
{
    "body": "The diff itself can be downloaded from http://linalg.org/projects/linalg/changeset/2803",
    "created_at": "2007-09-03T16:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/581#issuecomment-3005",
    "user": "mabshoff"
}
```

The diff itself can be downloaded from http://linalg.org/projects/linalg/changeset/2803



---

archive/issue_comments_003006.json:
```json
{
    "body": "By the way: The fix for #498 never made it into 2.8.3:\n\n```\nsage: M=Matrix(Integers(),20,20,L)\nsage: M.det()\nERROR in reconstruction ?\n\n0\nsage: M.rank()\n20\nsage:\n```\n\nWilliam, do you have a clue what happened to the fixed spkg? I certainly send you a link. The SPKG.txt also doesn't contain my change log entry.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-03T19:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/581#issuecomment-3006",
    "user": "mabshoff"
}
```

By the way: The fix for #498 never made it into 2.8.3:

```
sage: M=Matrix(Integers(),20,20,L)
sage: M.det()
ERROR in reconstruction ?

0
sage: M.rank()
20
sage:
```

William, do you have a clue what happened to the fixed spkg? I certainly send you a link. The SPKG.txt also doesn't contain my change log entry.

Cheers,

Michael



---

archive/issue_comments_003007.json:
```json
{
    "body": "A new spkg with ChangeSet 2803 applied can be found at \n\nhttp://fsmath.mathematik.uni-dortmund.de/~mabshoff/sage/linbox-20070903.spkg\n\nCheers,\n\nMichael",
    "created_at": "2007-09-03T19:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/581#issuecomment-3007",
    "user": "mabshoff"
}
```

A new spkg with ChangeSet 2803 applied can be found at 

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/sage/linbox-20070903.spkg

Cheers,

Michael



---

archive/issue_comments_003008.json:
```json
{
    "body": "applied and tested",
    "created_at": "2007-09-04T01:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/581#issuecomment-3008",
    "user": "was"
}
```

applied and tested



---

archive/issue_comments_003009.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-04T01:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/581#issuecomment-3009",
    "user": "was"
}
```

Resolution: fixed
