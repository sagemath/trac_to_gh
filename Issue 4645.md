# Issue 4645: in setup.py module_list.py is hidden with no comment.  VERY CONFUSING

archive/issues_004645.json:
```json
{
    "body": "Assignee: mabshoff\n\nRight in the middle of setup.py we find:\n\n```\n\nfrom module_list import ext_modules\n\n```\n\nwithout further comment.\n\nMove this line to the very top of setup.py and surround it be huge helpful comments.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4645\n\n",
    "created_at": "2008-11-28T21:47:12Z",
    "labels": [
        "component: build"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "in setup.py module_list.py is hidden with no comment.  VERY CONFUSING",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4645",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_034897.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-29T06:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4645#issuecomment-34897",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034898.json:
```json
{
    "body": "Patch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T06:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4645#issuecomment-34898",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch coming up.

Cheers,

Michael



---

archive/issue_comments_034899.json:
```json
{
    "body": "The patch is at #4647. William gave the code already a blessing in IRC.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T06:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4645#issuecomment-34899",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch is at #4647. William gave the code already a blessing in IRC.

Cheers,

Michael



---

archive/issue_comments_034900.json:
```json
{
    "body": "Yeah, it was pretty sloppy to not make any comments about where the module listing went. Positive review.",
    "created_at": "2008-11-29T07:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4645#issuecomment-34900",
    "user": "https://github.com/craigcitro"
}
```

Yeah, it was pretty sloppy to not make any comments about where the module listing went. Positive review.



---

archive/issue_comments_034901.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-29T07:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4645#issuecomment-34901",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034902.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc0",
    "created_at": "2008-11-29T07:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4645",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4645#issuecomment-34902",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.rc0
