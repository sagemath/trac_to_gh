# Issue 2506: Problem with inequality operator (!=) in graph.py

archive/issues_002506.json:
```json
{
    "body": "Assignee: rlm\n\n\n```\nsage: g = Graph()\nsage: g2 = g.copy()\nsage: g == g   # fine\nTrue\nsage: g != g   # fine\nFalse\nsage: g2 == g  # PROBLEM: either this one\nTrue\nsage: g2 != g  # or this one should be false\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2506\n\n",
    "created_at": "2008-03-13T16:56:38Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "Problem with inequality operator (!=) in graph.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2506",
    "user": "rhinton"
}
```
Assignee: rlm


```
sage: g = Graph()
sage: g2 = g.copy()
sage: g == g   # fine
True
sage: g != g   # fine
False
sage: g2 == g  # PROBLEM: either this one
True
sage: g2 != g  # or this one should be false
True
```


Issue created by migration from https://trac.sagemath.org/ticket/2506





---

archive/issue_comments_016976.json:
```json
{
    "body": "I think this may be a subtlety having to do with Python comparison (although I'm tempted to call it a bug, maybe \"subtlety\" is more P.C.). The funny thing is if you define the method\n\n```\ndef __ne__(self, other):\n    return (not (self == other))\n```\n\nyou get the correct behavior. Before making a patch, it might be good to figure out why this is the case...",
    "created_at": "2008-03-14T00:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2506#issuecomment-16976",
    "user": "rlm"
}
```

I think this may be a subtlety having to do with Python comparison (although I'm tempted to call it a bug, maybe "subtlety" is more P.C.). The funny thing is if you define the method

```
def __ne__(self, other):
    return (not (self == other))
```

you get the correct behavior. Before making a patch, it might be good to figure out why this is the case...



---

archive/issue_comments_016977.json:
```json
{
    "body": "The correct behavior is the following:\n\n```\nsage: g = Graph()\nsage: g2 = g.copy()\nsage: g == g\nTrue\nsage: g != g\nFalse\nsage: g2 == g\nTrue\nsage: g2 != g\nFalse\nsage: g is g\nTrue\nsage: g2 is g\nFalse\n```\n",
    "created_at": "2008-03-14T00:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2506#issuecomment-16977",
    "user": "rlm"
}
```

The correct behavior is the following:

```
sage: g = Graph()
sage: g2 = g.copy()
sage: g == g
True
sage: g != g
False
sage: g2 == g
True
sage: g2 != g
False
sage: g is g
True
sage: g2 is g
False
```




---

archive/issue_comments_016978.json:
```json
{
    "body": "Aparently, to have proper behavior, we do have to implement the `__ne__` method:\n\nhttp://www.voidspace.org.uk/python/articles/comparison.shtml",
    "created_at": "2008-03-14T13:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2506#issuecomment-16978",
    "user": "rlm"
}
```

Aparently, to have proper behavior, we do have to implement the `__ne__` method:

http://www.voidspace.org.uk/python/articles/comparison.shtml



---

archive/issue_comments_016979.json:
```json
{
    "body": "Attachment [2506-fix.patch](tarball://root/attachments/some-uuid/ticket2506/2506-fix.patch) by rlm created at 2008-03-14 13:46:44",
    "created_at": "2008-03-14T13:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2506#issuecomment-16979",
    "user": "rlm"
}
```

Attachment [2506-fix.patch](tarball://root/attachments/some-uuid/ticket2506/2506-fix.patch) by rlm created at 2008-03-14 13:46:44



---

archive/issue_comments_016980.json:
```json
{
    "body": "Patch looks good to me and fixes the bug.",
    "created_at": "2008-03-14T14:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2506#issuecomment-16980",
    "user": "mabshoff"
}
```

Patch looks good to me and fixes the bug.



---

archive/issue_comments_016981.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T14:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2506#issuecomment-16981",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0



---

archive/issue_comments_016982.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T14:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2506#issuecomment-16982",
    "user": "mabshoff"
}
```

Resolution: fixed
