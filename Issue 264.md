# Issue 264: Coercion of axiom Float to python float

archive/issues_000264.json:
```json
{
    "body": "Assignee: @williamstein\n\nHere is the output of this type of coercion:\n\nsage: float axiom(1.7)\n----> float(axiom(RealNumber('1.7')))\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/home/greg/<ipython console> in <module>()\n\n/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/axiom.py in __float__(self)\n    422 \n    423     def __float__(self):\n--> 424         return float(str(self.numer()))\n    425 \n    426     def __len__(self):\n\n<type 'exceptions.ValueError'>: invalid literal for float(): float(250875719402449901978,-67,2)\n\nThe problem is that the Axiom Float is coerced to InputForm and in this format (actually) the internal representation of this Float is obtained : 250875719402449901978*2**-67.\n\nIssue created by migration from https://trac.sagemath.org/ticket/264\n\n",
    "created_at": "2007-02-15T22:32:46Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "Coercion of axiom Float to python float",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/264",
    "user": "https://trac.sagemath.org/admin/accounts/users/gvanuxem"
}
```
Assignee: @williamstein

Here is the output of this type of coercion:

sage: float axiom(1.7)
----> float(axiom(RealNumber('1.7')))
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/home/greg/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/axiom.py in __float__(self)
    422 
    423     def __float__(self):
--> 424         return float(str(self.numer()))
    425 
    426     def __len__(self):

<type 'exceptions.ValueError'>: invalid literal for float(): float(250875719402449901978,-67,2)

The problem is that the Axiom Float is coerced to InputForm and in this format (actually) the internal representation of this Float is obtained : 250875719402449901978*2**-67.

Issue created by migration from https://trac.sagemath.org/ticket/264





---

archive/issue_events_000579.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-06T13:58:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/264",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/264#event-579"
}
```



---

archive/issue_events_000580.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-21T02:01:27Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/264",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/264#event-580"
}
```



---

archive/issue_events_000581.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-21T02:01:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/264",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/264#event-581"
}
```



---

archive/issue_events_000582.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-21T02:01:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/264",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/264#event-582"
}
```



---

archive/issue_comments_001244.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T02:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/264#issuecomment-1244",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_001245.json:
```json
{
    "body": "This works fine in sage-2.8.8.",
    "created_at": "2007-10-21T02:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/264#issuecomment-1245",
    "user": "https://github.com/williamstein"
}
```

This works fine in sage-2.8.8.
