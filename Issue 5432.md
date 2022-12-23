# Issue 5432: sage-combinat fixes: sage calls and qselect

archive/issues_005432.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat\n\nBug fixes:\n- Honor the SAGE_ROOT env variable to call sage\n- Removed config file handling which is now useless\n- Fixed missing default value for guards in qselect_backward_compatibility_patches\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5432\n\n",
    "created_at": "2009-03-03T23:28:24Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "sage-combinat fixes: sage calls and qselect",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5432",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat

Bug fixes:
- Honor the SAGE_ROOT env variable to call sage
- Removed config file handling which is now useless
- Fixed missing default value for guards in qselect_backward_compatibility_patches


Issue created by migration from https://trac.sagemath.org/ticket/5432





---

archive/issue_comments_042028.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-03T23:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5432#issuecomment-42028",
    "user": "nthiery"
}
```

Attachment



---

archive/issue_comments_042029.json:
```json
{
    "body": "Mike,\n\ncan you review this?\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T19:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5432#issuecomment-42029",
    "user": "mabshoff"
}
```

Mike,

can you review this?

Cheers,

Michael



---

archive/issue_comments_042030.json:
```json
{
    "body": "Well, no point of shipping 3.4 with a broken combinat script, so make this a blocker :)\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T22:36:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5432#issuecomment-42030",
    "user": "mabshoff"
}
```

Well, no point of shipping 3.4 with a broken combinat script, so make this a blocker :)

Cheers,

Michael



---

archive/issue_comments_042031.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-03-04T22:36:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5432#issuecomment-42031",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_042032.json:
```json
{
    "body": "Patch applies smootly and is working for me ! I'm giving it a +1.",
    "created_at": "2009-03-04T23:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5432#issuecomment-42032",
    "user": "hivert"
}
```

Patch applies smootly and is working for me ! I'm giving it a +1.



---

archive/issue_comments_042033.json:
```json
{
    "body": "Merged in Sage 3.4.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T23:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5432#issuecomment-42033",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.rc1.

Cheers,

Michael



---

archive/issue_comments_042034.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-04T23:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5432#issuecomment-42034",
    "user": "mabshoff"
}
```

Resolution: fixed
