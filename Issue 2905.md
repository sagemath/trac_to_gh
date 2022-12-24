# Issue 2905: Various speedups

archive/issues_002905.json:
```json
{
    "body": "Assignee: gfurnish\n\nThis patch moves some things to cpdef and fixes various slowdowns.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2905\n\n",
    "created_at": "2008-04-13T06:02:46Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Various speedups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2905",
    "user": "gfurnish"
}
```
Assignee: gfurnish

This patch moves some things to cpdef and fixes various slowdowns.

Issue created by migration from https://trac.sagemath.org/ticket/2905





---

archive/issue_comments_020024.json:
```json
{
    "body": "Attachment [trac_2905.patch](tarball://root/attachments/some-uuid/ticket2905/trac_2905.patch) by gfurnish created at 2008-04-13 06:05:50",
    "created_at": "2008-04-13T06:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2905#issuecomment-20024",
    "user": "gfurnish"
}
```

Attachment [trac_2905.patch](tarball://root/attachments/some-uuid/ticket2905/trac_2905.patch) by gfurnish created at 2008-04-13 06:05:50



---

archive/issue_comments_020025.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-13T06:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2905#issuecomment-20025",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020026.json:
```json
{
    "body": "\n```\n<gfurnish> I changed from __domain to _domain because homspace uses MI so there is no easy way to cython it, but that makes it easy to grab the attribute directly for places in coercion where speed matters\n<mabshoff> ok\n<gfurnish> the other change was -O2 spyx's\n<mabshoff> yeah, saw that\n<gfurnish> and finally I moved to a try->except instead of a has_key in coercion in parent.pyx\n<mabshoff> :)\n<gfurnish> maybe I should just paste those three sentences into the description\n```\n",
    "created_at": "2008-04-13T06:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2905#issuecomment-20026",
    "user": "gfurnish"
}
```


```
<gfurnish> I changed from __domain to _domain because homspace uses MI so there is no easy way to cython it, but that makes it easy to grab the attribute directly for places in coercion where speed matters
<mabshoff> ok
<gfurnish> the other change was -O2 spyx's
<mabshoff> yeah, saw that
<gfurnish> and finally I moved to a try->except instead of a has_key in coercion in parent.pyx
<mabshoff> :)
<gfurnish> maybe I should just paste those three sentences into the description
```




---

archive/issue_comments_020027.json:
```json
{
    "body": "Patch passes doctest on Sage 3.0.alpha4. Somebody else needs to take a closer look and figure out of all of this is a good idea.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T07:40:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2905#issuecomment-20027",
    "user": "mabshoff"
}
```

Patch passes doctest on Sage 3.0.alpha4. Somebody else needs to take a closer look and figure out of all of this is a good idea.

Cheers,

Michael



---

archive/issue_comments_020028.json:
```json
{
    "body": "It all looks good to me.  testall passes (on 3.0 alpha3), the new code in parent.pyx is equivalent and plausibly faster (although I didn't benchmark it), and reducing optimization on .spyx files from -O3 to -O2 is good.",
    "created_at": "2008-04-13T17:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2905#issuecomment-20028",
    "user": "cwitty"
}
```

It all looks good to me.  testall passes (on 3.0 alpha3), the new code in parent.pyx is equivalent and plausibly faster (although I didn't benchmark it), and reducing optimization on .spyx files from -O3 to -O2 is good.



---

archive/issue_comments_020029.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-13T18:35:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2905#issuecomment-20029",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020030.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-13T18:35:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2905#issuecomment-20030",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha5
