# Issue 5769: power series are accidentally *mutable* (really dangerous)

archive/issues_005769.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nwstein@sage:~/build/sage-3.4.1.rc2$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: ref2\nsage: R.<t> = ZZ[[]]\nsage: f = 1 + 17*t - 4*t^3 + O(t^5)\nsage: f[1] = 10\n...\nIndexError: power series are immutable\n```\n\nExcept they are mutable:\n\n```\nsage: f *= 2\nsage: f\n2 + 34*t - 8*t^3 + O(t^5)\n```\n\nBut they shouldn't be!  The _imul_ method needs to be deleted.\n| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |\n| Type notebook() for the GUI, and license() for information.        |\n\nIssue created by migration from https://trac.sagemath.org/ticket/5769\n\n",
    "created_at": "2009-04-12T05:19:59Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "power series are accidentally *mutable* (really dangerous)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5769",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody


```
wstein@sage:~/build/sage-3.4.1.rc2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: ref2
sage: R.<t> = ZZ[[]]
sage: f = 1 + 17*t - 4*t^3 + O(t^5)
sage: f[1] = 10
...
IndexError: power series are immutable
```

Except they are mutable:

```
sage: f *= 2
sage: f
2 + 34*t - 8*t^3 + O(t^5)
```

But they shouldn't be!  The _imul_ method needs to be deleted.
| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |
| Type notebook() for the GUI, and license() for information.        |

Issue created by migration from https://trac.sagemath.org/ticket/5769





---

archive/issue_comments_045042.json:
```json
{
    "body": "The code has nothing to do with mutability. \n\nsage: a= (1,2,3)\n\na is a tuple, an immutable object\n\nsage: a += a\nsage: a\n(1, 2, 3, 1, 2, 3)\n\nsage: R.<t> = ZZ[[]]\nsage: f = 1 + 17*t - 4*t^3 + O(t^5)\nsage: g=f\nsage: g is f\nTrue\nsage: f+=f\nsage: f\n2 + 34*t - 8*t^3 + O(t^5)\nsage: g\n1 + 17*t - 4*t^3 + O(t^5)\nsage: f is g\nFalse",
    "created_at": "2010-06-16T08:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5769#issuecomment-45042",
    "user": "https://github.com/lftabera"
}
```

The code has nothing to do with mutability. 

sage: a= (1,2,3)

a is a tuple, an immutable object

sage: a += a
sage: a
(1, 2, 3, 1, 2, 3)

sage: R.<t> = ZZ[[]]
sage: f = 1 + 17*t - 4*t^3 + O(t^5)
sage: g=f
sage: g is f
True
sage: f+=f
sage: f
2 + 34*t - 8*t^3 + O(t^5)
sage: g
1 + 17*t - 4*t^3 + O(t^5)
sage: f is g
False



---

archive/issue_comments_045043.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-06-16T08:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5769#issuecomment-45043",
    "user": "https://github.com/lftabera"
}
```

Resolution: invalid
