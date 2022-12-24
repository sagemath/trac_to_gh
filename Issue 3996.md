# Issue 3996: [with patch, needs review] doctest the Singular interface

archive/issues_003996.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3996\n\n",
    "created_at": "2008-08-29T21:57:00Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] doctest the Singular interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3996",
    "user": "mhansen"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/3996





---

archive/issue_comments_028710.json:
```json
{
    "body": "**Review**\n* I don't think you need `sage: os.unlink(filename)` since the file is in tmp anyway\n* Sometimes the **r** before `\"\"\"` is missing but e.g. `\\var` is used\n\n\nIf those are fixed, I'll give it a positive review.",
    "created_at": "2008-08-29T22:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3996#issuecomment-28710",
    "user": "malb"
}
```

**Review**
* I don't think you need `sage: os.unlink(filename)` since the file is in tmp anyway
* Sometimes the **r** before `"""` is missing but e.g. `\var` is used


If those are fixed, I'll give it a positive review.



---

archive/issue_comments_028711.json:
```json
{
    "body": "Attachment [trac_3996.patch](tarball://root/attachments/some-uuid/ticket3996/trac_3996.patch) by mhansen created at 2008-08-29 22:10:14",
    "created_at": "2008-08-29T22:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3996#issuecomment-28711",
    "user": "mhansen"
}
```

Attachment [trac_3996.patch](tarball://root/attachments/some-uuid/ticket3996/trac_3996.patch) by mhansen created at 2008-08-29 22:10:14



---

archive/issue_comments_028712.json:
```json
{
    "body": "Unfortunately against my current alpha3 merge tree (the only relevant patch here over alpha2 is probably #3988):\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/devel/sage$ patch -p1 --dry-run < trac_3996.patch \npatching file sage/interfaces/singular.py\nHunk #13 succeeded at 1010 with fuzz 2.\nHunk #14 succeeded at 1106 (offset 44 lines).\nHunk #15 FAILED at 1168.\nHunk #16 succeeded at 1350 (offset 44 lines).\nHunk #17 succeeded at 1375 (offset 44 lines).\nHunk #18 succeeded at 1399 (offset 44 lines).\nHunk #19 succeeded at 1474 (offset 44 lines).\nHunk #20 succeeded at 1505 (offset 44 lines).\nHunk #21 succeeded at 1524 (offset 44 lines).\nHunk #22 succeeded at 1575 (offset 44 lines).\nHunk #23 succeeded at 1625 (offset 44 lines).\n1 out of 23 hunks FAILED -- saving rejects to file sage/interfaces/singular.py.rej\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-08-29T22:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3996#issuecomment-28712",
    "user": "mabshoff"
}
```

Unfortunately against my current alpha3 merge tree (the only relevant patch here over alpha2 is probably #3988):

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/devel/sage$ patch -p1 --dry-run < trac_3996.patch 
patching file sage/interfaces/singular.py
Hunk #13 succeeded at 1010 with fuzz 2.
Hunk #14 succeeded at 1106 (offset 44 lines).
Hunk #15 FAILED at 1168.
Hunk #16 succeeded at 1350 (offset 44 lines).
Hunk #17 succeeded at 1375 (offset 44 lines).
Hunk #18 succeeded at 1399 (offset 44 lines).
Hunk #19 succeeded at 1474 (offset 44 lines).
Hunk #20 succeeded at 1505 (offset 44 lines).
Hunk #21 succeeded at 1524 (offset 44 lines).
Hunk #22 succeeded at 1575 (offset 44 lines).
Hunk #23 succeeded at 1625 (offset 44 lines).
1 out of 23 hunks FAILED -- saving rejects to file sage/interfaces/singular.py.rej
```


Cheers,

Michael



---

archive/issue_comments_028713.json:
```json
{
    "body": "Attachment [trac_3996-rebase.patch](tarball://root/attachments/some-uuid/ticket3996/trac_3996-rebase.patch) by mhansen created at 2008-08-29 22:54:09\n\ntrac_3996-rebase.patch should apply cleanly.",
    "created_at": "2008-08-29T22:54:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3996#issuecomment-28713",
    "user": "mhansen"
}
```

Attachment [trac_3996-rebase.patch](tarball://root/attachments/some-uuid/ticket3996/trac_3996-rebase.patch) by mhansen created at 2008-08-29 22:54:09

trac_3996-rebase.patch should apply cleanly.



---

archive/issue_comments_028714.json:
```json
{
    "body": "Merged trac_3996-rebase.patch in Sage 3.1.2.alpha3",
    "created_at": "2008-08-30T00:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3996#issuecomment-28714",
    "user": "mabshoff"
}
```

Merged trac_3996-rebase.patch in Sage 3.1.2.alpha3



---

archive/issue_comments_028715.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-30T00:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3996",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3996#issuecomment-28715",
    "user": "mabshoff"
}
```

Resolution: fixed
