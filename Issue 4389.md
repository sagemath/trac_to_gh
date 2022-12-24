# Issue 4389: [with patch, needs review] Sage 3.1.4: optional doctest failure in sage/groups/perm_gps/permgroup.py

archive/issues_004389.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t -long -optional devel/sage/sage/groups/perm_gps/permgroup.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/permgroup.py\", line 179:\n    sage: H.gens()                            # requires optional database_gap\nExpected:\n    ((1,2,3,4), (1,3))\nGot:\n    [(1,2,3,4), (1,3)]\n**********************************************************************\n```\n\nThe above is caused by changing the printing of permutations that went into Sage a while ago. The fix is obvious.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4389\n\n",
    "created_at": "2008-10-30T05:35:08Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] Sage 3.1.4: optional doctest failure in sage/groups/perm_gps/permgroup.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4389",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
sage -t -long -optional devel/sage/sage/groups/perm_gps/permgroup.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/permgroup.py", line 179:
    sage: H.gens()                            # requires optional database_gap
Expected:
    ((1,2,3,4), (1,3))
Got:
    [(1,2,3,4), (1,3)]
**********************************************************************
```

The above is caused by changing the printing of permutations that went into Sage a while ago. The fix is obvious.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4389





---

archive/issue_comments_032306.json:
```json
{
    "body": "Attachment [trac_4389.patch](tarball://root/attachments/some-uuid/ticket4389/trac_4389.patch) by mabshoff created at 2008-10-30 05:38:32",
    "created_at": "2008-10-30T05:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4389#issuecomment-32306",
    "user": "mabshoff"
}
```

Attachment [trac_4389.patch](tarball://root/attachments/some-uuid/ticket4389/trac_4389.patch) by mabshoff created at 2008-10-30 05:38:32



---

archive/issue_comments_032307.json:
```json
{
    "body": "+1",
    "created_at": "2008-10-30T05:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4389#issuecomment-32307",
    "user": "@mwhansen"
}
```

+1



---

archive/issue_comments_032308.json:
```json
{
    "body": "+1 here too",
    "created_at": "2008-10-30T05:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4389#issuecomment-32308",
    "user": "@dandrake"
}
```

+1 here too



---

archive/issue_comments_032309.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-30T05:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4389#issuecomment-32309",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_comments_032310.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-30T05:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4389#issuecomment-32310",
    "user": "mabshoff"
}
```

Resolution: fixed
