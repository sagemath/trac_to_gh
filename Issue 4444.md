# Issue 4444: Remove duplicate source names in setup.py

archive/issues_004444.json:
```json
{
    "body": "Assignee: @craigcitro\n\nIn `setup.py`, there are several source files which appear in the `sources` list more than once. For instance, the entry for `sage.rings.rational` looks like:\n\n\n```\nExtension('sage.rings.rational',\n           sources = ['sage/rings/rational.pyx',\n                      'sage/ext/arith.pyx', \\\n                      'sage/rings/integer.pyx'],\n           libraries=['ntl', 'gmp'])\n```\n\n\nThe other two `.pyx` files that appear there were added in the old days, when Pyrex needed us to do this in order to compile `rational.pyx` correctly. Note that because of this, several files in the Sage library get compiled multiple times. (For instance, try changing `sage/ext/arith.pyx` and doing a `sage -br`.) We should fix this.\n\nI've already made the changes to `setup.py`, but I really need to do a `sage -ba` to feel like I've appropriately tested this. I'll do that tomorrow. I'm going to make this ticket dependent on #4443, since I already fixed the situation for `sage/ext/arith.pyx` while working on that ticket.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4444\n\n",
    "created_at": "2008-11-05T10:21:20Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Remove duplicate source names in setup.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4444",
    "user": "@craigcitro"
}
```
Assignee: @craigcitro

In `setup.py`, there are several source files which appear in the `sources` list more than once. For instance, the entry for `sage.rings.rational` looks like:


```
Extension('sage.rings.rational',
           sources = ['sage/rings/rational.pyx',
                      'sage/ext/arith.pyx', \
                      'sage/rings/integer.pyx'],
           libraries=['ntl', 'gmp'])
```


The other two `.pyx` files that appear there were added in the old days, when Pyrex needed us to do this in order to compile `rational.pyx` correctly. Note that because of this, several files in the Sage library get compiled multiple times. (For instance, try changing `sage/ext/arith.pyx` and doing a `sage -br`.) We should fix this.

I've already made the changes to `setup.py`, but I really need to do a `sage -ba` to feel like I've appropriately tested this. I'll do that tomorrow. I'm going to make this ticket dependent on #4443, since I already fixed the situation for `sage/ext/arith.pyx` while working on that ticket.

Issue created by migration from https://trac.sagemath.org/ticket/4444





---

archive/issue_comments_032697.json:
```json
{
    "body": "trac-4443.patch already contains some fixes to setup.py - are the more coming?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-05T13:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4444#issuecomment-32697",
    "user": "mabshoff"
}
```

trac-4443.patch already contains some fixes to setup.py - are the more coming?

Cheers,

Michael



---

archive/issue_comments_032698.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-05T16:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4444#issuecomment-32698",
    "user": "@craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032699.json:
```json
{
    "body": "Yep, more coming.",
    "created_at": "2008-11-05T16:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4444#issuecomment-32699",
    "user": "@craigcitro"
}
```

Yep, more coming.



---

archive/issue_comments_032700.json:
```json
{
    "body": "This has been taken care off via #4480. \n\nCheers,\n\nMichael",
    "created_at": "2008-11-10T08:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4444#issuecomment-32700",
    "user": "mabshoff"
}
```

This has been taken care off via #4480. 

Cheers,

Michael



---

archive/issue_comments_032701.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-10T08:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4444#issuecomment-32701",
    "user": "mabshoff"
}
```

Resolution: fixed
