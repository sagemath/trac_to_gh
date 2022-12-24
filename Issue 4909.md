# Issue 4909: convert sage.dsage.* docstrings to Sphinx

archive/issues_004909.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4909\n\n",
    "created_at": "2009-01-01T22:50:29Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "convert sage.dsage.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4909",
    "user": "mhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4909





---

archive/issue_comments_037256.json:
```json
{
    "body": "Attachment [trac_4909.patch](tarball://root/attachments/some-uuid/ticket4909/trac_4909.patch) by mhansen created at 2009-01-02 02:25:34",
    "created_at": "2009-01-02T02:25:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4909#issuecomment-37256",
    "user": "mhansen"
}
```

Attachment [trac_4909.patch](tarball://root/attachments/some-uuid/ticket4909/trac_4909.patch) by mhansen created at 2009-01-02 02:25:34



---

archive/issue_comments_037257.json:
```json
{
    "body": "Attachment [sage.dsage-final.patch](tarball://root/attachments/some-uuid/ticket4909/sage.dsage-final.patch) by mhansen created at 2009-02-21 19:17:23",
    "created_at": "2009-02-21T19:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4909#issuecomment-37257",
    "user": "mhansen"
}
```

Attachment [sage.dsage-final.patch](tarball://root/attachments/some-uuid/ticket4909/sage.dsage-final.patch) by mhansen created at 2009-02-21 19:17:23



---

archive/issue_comments_037258.json:
```json
{
    "body": "A little problem:\n\n```\nNote that configuration files will be stored in the  \n    directory \\code{\\$DOT\\_SAGE/dsage}.\n```\n\nIs replaced now by\n\n```\nNote that configuration files will be stored in the directory \n``$DOT \nSage/dsage``. \n```\n \nthe \"_\" must be kept. \n\nOtherwise this is correct. \n\nCheers,\n\nFlorent",
    "created_at": "2009-02-24T17:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4909#issuecomment-37258",
    "user": "hivert"
}
```

A little problem:

```
Note that configuration files will be stored in the  
    directory \code{\$DOT\_SAGE/dsage}.
```

Is replaced now by

```
Note that configuration files will be stored in the directory 
``$DOT 
Sage/dsage``. 
```
 
the "_" must be kept. 

Otherwise this is correct. 

Cheers,

Florent



---

archive/issue_comments_037259.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4909#issuecomment-37259",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Cheers,

Michael



---

archive/issue_comments_037260.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T18:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4909#issuecomment-37260",
    "user": "mabshoff"
}
```

Resolution: fixed
