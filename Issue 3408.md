# Issue 3408: [with spkg] Cython 0.9.8 released

archive/issues_003408.json:
```json
{
    "body": "Assignee: mabshoff\n\nSpkg up at http://sage.math.washington.edu/home/robertwb/cython/\n\nIssue created by migration from https://trac.sagemath.org/ticket/3408\n\n",
    "created_at": "2008-06-12T23:50:10Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with spkg] Cython 0.9.8 released",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3408",
    "user": "https://github.com/robertwb"
}
```
Assignee: mabshoff

Spkg up at http://sage.math.washington.edu/home/robertwb/cython/

Issue created by migration from https://trac.sagemath.org/ticket/3408





---

archive/issue_comments_023856.json:
```json
{
    "body": "Attachment [3408-cython-0.9.8.patch](tarball://root/attachments/some-uuid/ticket3408/3408-cython-0.9.8.patch) by @garyfurnish created at 2008-06-13 02:53:29\n\nThis seems to break the future import in padic_generic_element.pyx",
    "created_at": "2008-06-13T02:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23856",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [3408-cython-0.9.8.patch](tarball://root/attachments/some-uuid/ticket3408/3408-cython-0.9.8.patch) by @garyfurnish created at 2008-06-13 02:53:29

This seems to break the future import in padic_generic_element.pyx



---

archive/issue_comments_023857.json:
```json
{
    "body": "\n```\nfrom __future__ import with_statement\n                                    ^\n------------------------------------------------------------\n\n/home/gfurnish/sage-3.0.2-symbolics/devel/sage-symbolics/sage/rings/padics/padic_generic_element.pyx:19:37: future feature with_statement is not defined\n```\n\nThere also seem to be issues with having to move the future statement to before any includes.",
    "created_at": "2008-06-13T02:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23857",
    "user": "https://github.com/garyfurnish"
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

archive/issue_comments_023858.json:
```json
{
    "body": "Please be more precise, i.e. error message, which branch, i.e. non-symbolics and so on.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-13T02:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23858",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Please be more precise, i.e. error message, which branch, i.e. non-symbolics and so on.

Cheers,

Michael



---

archive/issue_comments_023859.json:
```json
{
    "body": "Gary: Notice that Robert attached a patch which you did not apply, so this issue is fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-13T03:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23859",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Gary: Notice that Robert attached a patch which you did not apply, so this issue is fixed.

Cheers,

Michael



---

archive/issue_comments_023860.json:
```json
{
    "body": "I am getting slight rejects here:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/devel/sage$ patch -p1 --dry-run < trac_3408-cython-0.9.8.patch \npatching file sage/ext/interactive_constructors_c.pyx\nHunk #1 FAILED at 24.\n1 out of 2 hunks FAILED -- saving rejects to file sage/ext/interactive_constructors_c.pyx.rej\npatching file sage/misc/cython.py\npatching file sage/rings/padics/padic_generic_element.pyx\npatching file sage/rings/padics/pow_computer_ext.pyx\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-06-13T03:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23860",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_comments_023861.json:
```json
{
    "body": "This seems to work for me except for the doctest rejects.",
    "created_at": "2008-06-13T03:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23861",
    "user": "https://github.com/garyfurnish"
}
```

This seems to work for me except for the doctest rejects.



---

archive/issue_comments_023862.json:
```json
{
    "body": "rebased",
    "created_at": "2008-06-13T17:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23862",
    "user": "https://github.com/robertwb"
}
```

rebased



---

archive/issue_comments_023863.json:
```json
{
    "body": "Attachment [3408-cython-0.9.8.2.patch](tarball://root/attachments/some-uuid/ticket3408/3408-cython-0.9.8.2.patch) by @robertwb created at 2008-06-13 17:11:51\n\nOK, I've rebased the patch. Note that interactive_constructors_c is sorted now, so this won't bite us again.",
    "created_at": "2008-06-13T17:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23863",
    "user": "https://github.com/robertwb"
}
```

Attachment [3408-cython-0.9.8.2.patch](tarball://root/attachments/some-uuid/ticket3408/3408-cython-0.9.8.2.patch) by @robertwb created at 2008-06-13 17:11:51

OK, I've rebased the patch. Note that interactive_constructors_c is sorted now, so this won't bite us again.



---

archive/issue_comments_023864.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-23T23:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23864",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_events_003624.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-06-23T23:40:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3408#event-3624"
}
```



---

archive/issue_comments_023865.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T23:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3408#issuecomment-23865",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
