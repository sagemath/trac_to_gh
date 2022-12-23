# Issue 4645: in setup.py module_list.py is hidden with no comment.  VERY CONFUSING

archive/issues_004645.json:
```json
{
    "body": "Assignee: mabshoff\n\nRight in the middle of setup.py we find:\n\n```\n\nfrom module_list import ext_modules\n\n```\n\nwithout further comment.\n\nMove this line to the very top of setup.py and surround it be huge helpful comments.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4645\n\n",
    "created_at": "2008-11-28T21:47:12Z",
    "labels": [
        "build",
        "major",
        "enhancement"
    ],
    "title": "in setup.py module_list.py is hidden with no comment.  VERY CONFUSING",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4645",
    "user": "was"
}
```
Assignee: mabshoff

Right in the middle of setup.py we find:

```

from module_list import ext_modules

```

without further comment.

Move this line to the very top of setup.py and surround it be huge helpful comments.



Issue created by migration from https://trac.sagemath.org/ticket/4645





---

archive/issue_comments_034965.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-29T06:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4645#issuecomment-34965",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034966.json:
```json
{
    "body": "Patch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T06:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4645#issuecomment-34966",
    "user": "mabshoff"
}
```

Patch coming up.

Cheers,

Michael



---

archive/issue_comments_034967.json:
```json
{
    "body": "The patch is at #4647. William gave the code already a blessing in IRC.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T06:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4645#issuecomment-34967",
    "user": "mabshoff"
}
```

The patch is at #4647. William gave the code already a blessing in IRC.

Cheers,

Michael



---

archive/issue_comments_034968.json:
```json
{
    "body": "Yeah, it was pretty sloppy to not make any comments about where the module listing went. Positive review.",
    "created_at": "2008-11-29T07:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4645#issuecomment-34968",
    "user": "craigcitro"
}
```

Yeah, it was pretty sloppy to not make any comments about where the module listing went. Positive review.



---

archive/issue_comments_034969.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-29T07:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4645#issuecomment-34969",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034970.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc0",
    "created_at": "2008-11-29T07:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4645#issuecomment-34970",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.rc0
