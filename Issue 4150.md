# Issue 4150: [with patch, needs review and testing] migrate graphs to new refinement code

archive/issues_004150.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  jason\n\nThis moves the automorphism group and isomorphism functions for graphs over to the new framework. It should be tested on a few different architectures before getting merged.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4150\n\n",
    "created_at": "2008-09-19T07:42:32Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review and testing] migrate graphs to new refinement code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4150",
    "user": "rlm"
}
```
Assignee: rlm

CC:  jason

This moves the automorphism group and isomorphism functions for graphs over to the new framework. It should be tested on a few different architectures before getting merged.

Issue created by migration from https://trac.sagemath.org/ticket/4150





---

archive/issue_comments_030130.json:
```json
{
    "body": "Attachment [trac_4150-switchover-graphs.patch](tarball://root/attachments/some-uuid/ticket4150/trac_4150-switchover-graphs.patch) by rlm created at 2008-09-19 07:43:20",
    "created_at": "2008-09-19T07:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30130",
    "user": "rlm"
}
```

Attachment [trac_4150-switchover-graphs.patch](tarball://root/attachments/some-uuid/ticket4150/trac_4150-switchover-graphs.patch) by rlm created at 2008-09-19 07:43:20



---

archive/issue_comments_030131.json:
```json
{
    "body": "Dependends on #4115, if you're applying to 3.1.2.final",
    "created_at": "2008-09-19T07:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30131",
    "user": "rlm"
}
```

Dependends on #4115, if you're applying to 3.1.2.final



---

archive/issue_comments_030132.json:
```json
{
    "body": "Positive review for Robert's part.  He just needs to sign off on my small second patch.",
    "created_at": "2008-09-19T08:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30132",
    "user": "mhansen"
}
```

Positive review for Robert's part.  He just needs to sign off on my small second patch.



---

archive/issue_comments_030133.json:
```json
{
    "body": "+1",
    "created_at": "2008-09-19T08:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30133",
    "user": "rlm"
}
```

+1



---

archive/issue_comments_030134.json:
```json
{
    "body": "Note that the second patch depends on #4139 being applied.",
    "created_at": "2008-09-19T08:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30134",
    "user": "mhansen"
}
```

Note that the second patch depends on #4139 being applied.



---

archive/issue_comments_030135.json:
```json
{
    "body": "The first hunk from trac_4150-fixes.patch ought to be deleted since I ended up fixing that doctest failure at #4139.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-19T14:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30135",
    "user": "mabshoff"
}
```

The first hunk from trac_4150-fixes.patch ought to be deleted since I ended up fixing that doctest failure at #4139.

Cheers,

Michael



---

archive/issue_comments_030136.json:
```json
{
    "body": "Attachment [trac_4150-fixes.patch](tarball://root/attachments/some-uuid/ticket4150/trac_4150-fixes.patch) by rlm created at 2008-09-19 14:54:01\n\nPatch fixed.",
    "created_at": "2008-09-19T14:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30136",
    "user": "rlm"
}
```

Attachment [trac_4150-fixes.patch](tarball://root/attachments/some-uuid/ticket4150/trac_4150-fixes.patch) by rlm created at 2008-09-19 14:54:01

Patch fixed.



---

archive/issue_comments_030137.json:
```json
{
    "body": "Thanks, valgrinds clean and also works on Itanium with Python build with `-fwrapv`, which caused trouble with the old codebase, so what could go wrong :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-19T23:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30137",
    "user": "mabshoff"
}
```

Thanks, valgrinds clean and also works on Itanium with Python build with `-fwrapv`, which caused trouble with the old codebase, so what could go wrong :)

Cheers,

Michael



---

archive/issue_comments_030138.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-19T23:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30138",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030139.json:
```json
{
    "body": "Merged both patches in Sage 3.1.3.alpha0",
    "created_at": "2008-09-19T23:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4150#issuecomment-30139",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.1.3.alpha0
