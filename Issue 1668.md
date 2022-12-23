# Issue 1668: fix polybori's variable names: _P->PB_P

archive/issues_001668.json:
```json
{
    "body": "Assignee: burcin\n\nVariable names like `_[A-Z]` cause trouble on Cygwin and Solaris. The polybori wrapper uses a couple of those. The renamed variables could be in some other for, but `_PP` also won't work. I have a patch, but since there are a bunch of other patches that touch the code and would need to be fixed wait for those to be merged before redoing this. burcin has volunteered to do this.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1668\n\n",
    "created_at": "2008-01-03T15:35:10Z",
    "labels": [
        "commutative algebra",
        "critical",
        "bug"
    ],
    "title": "fix polybori's variable names: _P->PB_P",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1668",
    "user": "mabshoff"
}
```
Assignee: burcin

Variable names like `_[A-Z]` cause trouble on Cygwin and Solaris. The polybori wrapper uses a couple of those. The renamed variables could be in some other for, but `_PP` also won't work. I have a patch, but since there are a bunch of other patches that touch the code and would need to be fixed wait for those to be merged before redoing this. burcin has volunteered to do this.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1668





---

archive/issue_comments_010594.json:
```json
{
    "body": "Attachment\n\nrename polybori variables",
    "created_at": "2008-01-08T14:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1668#issuecomment-10594",
    "user": "burcin"
}
```

Attachment

rename polybori variables



---

archive/issue_comments_010595.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-08T14:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1668#issuecomment-10595",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010596.json:
```json
{
    "body": "attachment:trac_1668.patch renames the problem variables used by the `PolyBoRi` wrapper.",
    "created_at": "2008-01-08T14:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1668#issuecomment-10596",
    "user": "burcin"
}
```

attachment:trac_1668.patch renames the problem variables used by the `PolyBoRi` wrapper.



---

archive/issue_comments_010597.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-01-13T17:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1668#issuecomment-10597",
    "user": "mabshoff"
}
```

Looks good to me.



---

archive/issue_comments_010598.json:
```json
{
    "body": "Merged in Sage 2.10.alpha3",
    "created_at": "2008-01-13T18:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1668#issuecomment-10598",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.alpha3



---

archive/issue_comments_010599.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-13T18:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1668#issuecomment-10599",
    "user": "mabshoff"
}
```

Resolution: fixed
