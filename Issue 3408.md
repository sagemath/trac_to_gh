# Issue 3408: [with spkg] Cython 0.9.8 released

archive/issues_003408.json:
```json
{
    "body": "Assignee: mabshoff\n\nSpkg up at http://sage.math.washington.edu/home/robertwb/cython/\n\nIssue created by migration from https://trac.sagemath.org/ticket/3408\n\n",
    "created_at": "2008-06-12T23:50:10Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with spkg] Cython 0.9.8 released",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3408",
    "user": "robertwb"
}
```
Assignee: mabshoff

Spkg up at http://sage.math.washington.edu/home/robertwb/cython/

Issue created by migration from https://trac.sagemath.org/ticket/3408





---

archive/issue_comments_023904.json:
```json
{
    "body": "Attachment [3408-cython-0.9.8.patch](tarball://root/attachments/some-uuid/ticket3408/3408-cython-0.9.8.patch) by gfurnish created at 2008-06-13 02:53:29\n\nThis seems to break the future import in padic_generic_element.pyx",
    "created_at": "2008-06-13T02:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23904",
    "user": "gfurnish"
}
```

Attachment [3408-cython-0.9.8.patch](tarball://root/attachments/some-uuid/ticket3408/3408-cython-0.9.8.patch) by gfurnish created at 2008-06-13 02:53:29

This seems to break the future import in padic_generic_element.pyx



---

archive/issue_comments_023905.json:
```json
{
    "body": "\n```\nfrom __future__ import with_statement\n                                    ^\n------------------------------------------------------------\n\n/home/gfurnish/sage-3.0.2-symbolics/devel/sage-symbolics/sage/rings/padics/padic_generic_element.pyx:19:37: future feature with_statement is not defined\n```\n\nThere also seem to be issues with having to move the future statement to before any includes.",
    "created_at": "2008-06-13T02:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23905",
    "user": "gfurnish"
}
```


```
from __future__ import with_statement
                                    ^
------------------------------------------------------------

/home/gfurnish/sage-3.0.2-symbolics/devel/sage-symbolics/sage/rings/padics/padic_generic_element.pyx:19:37: future feature with_statement is not defined
```

There also seem to be issues with having to move the future statement to before any includes.



---

archive/issue_comments_023906.json:
```json
{
    "body": "Please be more precise, i.e. error message, which branch, i.e. non-symbolics and so on.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-13T02:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23906",
    "user": "mabshoff"
}
```

Please be more precise, i.e. error message, which branch, i.e. non-symbolics and so on.

Cheers,

Michael



---

archive/issue_comments_023907.json:
```json
{
    "body": "Gary: Notice that Robert attached a patch which you did not apply, so this issue is fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-13T03:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23907",
    "user": "mabshoff"
}
```

Gary: Notice that Robert attached a patch which you did not apply, so this issue is fixed.

Cheers,

Michael



---

archive/issue_comments_023908.json:
```json
{
    "body": "I am getting slight rejects here:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/devel/sage$ patch -p1 --dry-run < trac_3408-cython-0.9.8.patch \npatching file sage/ext/interactive_constructors_c.pyx\nHunk #1 FAILED at 24.\n1 out of 2 hunks FAILED -- saving rejects to file sage/ext/interactive_constructors_c.pyx.rej\npatching file sage/misc/cython.py\npatching file sage/rings/padics/padic_generic_element.pyx\npatching file sage/rings/padics/pow_computer_ext.pyx\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-06-13T03:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23908",
    "user": "mabshoff"
}
```

I am getting slight rejects here:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/devel/sage$ patch -p1 --dry-run < trac_3408-cython-0.9.8.patch 
patching file sage/ext/interactive_constructors_c.pyx
Hunk #1 FAILED at 24.
1 out of 2 hunks FAILED -- saving rejects to file sage/ext/interactive_constructors_c.pyx.rej
patching file sage/misc/cython.py
patching file sage/rings/padics/padic_generic_element.pyx
patching file sage/rings/padics/pow_computer_ext.pyx
```


Cheers,

Michael



---

archive/issue_comments_023909.json:
```json
{
    "body": "This seems to work for me except for the doctest rejects.",
    "created_at": "2008-06-13T03:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23909",
    "user": "gfurnish"
}
```

This seems to work for me except for the doctest rejects.



---

archive/issue_comments_023910.json:
```json
{
    "body": "rebased",
    "created_at": "2008-06-13T17:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23910",
    "user": "robertwb"
}
```

rebased



---

archive/issue_comments_023911.json:
```json
{
    "body": "Attachment [3408-cython-0.9.8.2.patch](tarball://root/attachments/some-uuid/ticket3408/3408-cython-0.9.8.2.patch) by robertwb created at 2008-06-13 17:11:51\n\nOK, I've rebased the patch. Note that interactive_constructors_c is sorted now, so this won't bite us again.",
    "created_at": "2008-06-13T17:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23911",
    "user": "robertwb"
}
```

Attachment [3408-cython-0.9.8.2.patch](tarball://root/attachments/some-uuid/ticket3408/3408-cython-0.9.8.2.patch) by robertwb created at 2008-06-13 17:11:51

OK, I've rebased the patch. Note that interactive_constructors_c is sorted now, so this won't bite us again.



---

archive/issue_comments_023912.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-23T23:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23912",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_comments_023913.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T23:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23913",
    "user": "mabshoff"
}
```

Resolution: fixed
