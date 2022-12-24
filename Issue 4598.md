# Issue 4598: add sage/libs/gmp/__init__.py to MANIFEST.in

archive/issues_004598.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis causes build failures of the Sage library in Sage 3.2.1.alpha0.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4598\n\n",
    "created_at": "2008-11-23T21:20:17Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "add sage/libs/gmp/__init__.py to MANIFEST.in",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4598",
    "user": "mabshoff"
}
```
Assignee: mabshoff

This causes build failures of the Sage library in Sage 3.2.1.alpha0.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4598





---

archive/issue_comments_034475.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-23T21:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4598#issuecomment-34475",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034476.json:
```json
{
    "body": "Without the patch:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/spkg/standard/sage-3.2.1.alpha0$ hg status\n! sage/libs/gmp/__init__.py\n```\n\nWith the patch applied:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/spkg/standard/sage-3.2.1.alpha00$ hg stat\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/spkg/standard/sage-3.2.1.alpha00$ \n```\n",
    "created_at": "2008-11-25T11:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4598#issuecomment-34476",
    "user": "mabshoff"
}
```

Without the patch:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/spkg/standard/sage-3.2.1.alpha0$ hg status
! sage/libs/gmp/__init__.py
```

With the patch applied:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/spkg/standard/sage-3.2.1.alpha00$ hg stat
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/spkg/standard/sage-3.2.1.alpha00$ 
```




---

archive/issue_comments_034477.json:
```json
{
    "body": "Attachment [trac_4598.patch](tarball://root/attachments/some-uuid/ticket4598/trac_4598.patch) by mabshoff created at 2008-11-25 11:12:20",
    "created_at": "2008-11-25T11:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4598#issuecomment-34477",
    "user": "mabshoff"
}
```

Attachment [trac_4598.patch](tarball://root/attachments/some-uuid/ticket4598/trac_4598.patch) by mabshoff created at 2008-11-25 11:12:20



---

archive/issue_comments_034478.json:
```json
{
    "body": "Looks good to me. Thanks!",
    "created_at": "2008-11-25T13:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4598#issuecomment-34478",
    "user": "certik"
}
```

Looks good to me. Thanks!



---

archive/issue_comments_034479.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha1",
    "created_at": "2008-11-25T13:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4598#issuecomment-34479",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha1



---

archive/issue_comments_034480.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-25T13:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4598#issuecomment-34480",
    "user": "mabshoff"
}
```

Resolution: fixed
