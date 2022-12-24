# Issue 9192: Tab-completion misses some elements

archive/issues_009192.json:
```json
{
    "body": "Assignee: jason\n\n\n```\nsage.crypto.bl[tab]\n```\n\nThis should give\n\n```\nsage.crypto.block_cipher\n```\n\nBut does not.  In fact, \n\n```\nsage.crypto.[tab]\n```\n\nonly gives 10 of the 13 things which appear when you do\n\n```\nfrom sage.crypto.[tab]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9192\n\n",
    "created_at": "2010-06-09T02:18:04Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Tab-completion misses some elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9192",
    "user": "kcrisman"
}
```
Assignee: jason


```
sage.crypto.bl[tab]
```

This should give

```
sage.crypto.block_cipher
```

But does not.  In fact, 

```
sage.crypto.[tab]
```

only gives 10 of the 13 things which appear when you do

```
from sage.crypto.[tab]
```


Issue created by migration from https://trac.sagemath.org/ticket/9192


