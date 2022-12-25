# Issue 5201: make solve understand matrix equations

archive/issues_005201.json:
```json
{
    "body": "Assignee: @burcin\n\nI think it would be a great thing if solve could recognize matrices and that two matrices are equal if each entry is equal.  I believe MMA does this (but it's easier there; matrices are nothing more than nested lists).  It'd certainly make certain things I do more natural if I could do:\n\n`solve(matrixA==matrixB)`\n\nand that was equivalent to:\n\n`solve([i==j for i,j in zip(matrixA.list(), matrixB.list())]) `\n\n\nOkay, so now that I've written my piece, I suppose the next step is to open a trac ticket, write a patch to implement it, and post it for review :).\n\nIssue created by migration from https://trac.sagemath.org/ticket/5201\n\n",
    "created_at": "2009-02-07T19:18:01Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "make solve understand matrix equations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5201",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @burcin

I think it would be a great thing if solve could recognize matrices and that two matrices are equal if each entry is equal.  I believe MMA does this (but it's easier there; matrices are nothing more than nested lists).  It'd certainly make certain things I do more natural if I could do:

`solve(matrixA==matrixB)`

and that was equivalent to:

`solve([i==j for i,j in zip(matrixA.list(), matrixB.list())]) `


Okay, so now that I've written my piece, I suppose the next step is to open a trac ticket, write a patch to implement it, and post it for review :).

Issue created by migration from https://trac.sagemath.org/ticket/5201





---

archive/issue_comments_039778.json:
```json
{
    "body": "Which part of no non-ReST tickets against 3.4 is hard to understand? :p\n\nCheers,\n\nMichael",
    "created_at": "2009-02-07T19:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5201#issuecomment-39778",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Which part of no non-ReST tickets against 3.4 is hard to understand? :p

Cheers,

Michael



---

archive/issue_events_012037.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-07T19:23:11Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5201#event-12037"
}
```



---

archive/issue_comments_039779.json:
```json
{
    "body": "argh!  I looked at the list and thought \"the first item is the ReST transition, so I have to pick the second item\".  Apparently I was thinking that the next release was already out and 3.3 was the ReST transition.",
    "created_at": "2009-02-07T19:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5201#issuecomment-39779",
    "user": "https://github.com/jasongrout"
}
```

argh!  I looked at the list and thought "the first item is the ReST transition, so I have to pick the second item".  Apparently I was thinking that the next release was already out and 3.3 was the ReST transition.



---

archive/issue_comments_039780.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-05-26T15:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5201#issuecomment-39780",
    "user": "https://github.com/jasongrout"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_039781.json:
```json
{
    "body": "Could this be accomplished by overriding the comparison operator for the matrix class?\n\nfor example\n\n\n```python\ndef __richcmp__(self, other_matrix, cmptype):\n  if cmptype == 2:  #this is the '==' operator\n    if is_Matrix(other_matrix):\n      if False in [i==j for i,j in zip(self.list(), other_matrix.list())]:\n        return False\n      else: return True\n```\n\n\nI'm just not sure where the 'matrix class' is.  This would allow comparisons like\n\n\n```\nsage: matrixA == matrixB\nTrue\n```\n",
    "created_at": "2011-04-14T03:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5201#issuecomment-39781",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Could this be accomplished by overriding the comparison operator for the matrix class?

for example


```python
def __richcmp__(self, other_matrix, cmptype):
  if cmptype == 2:  #this is the '==' operator
    if is_Matrix(other_matrix):
      if False in [i==j for i,j in zip(self.list(), other_matrix.list())]:
        return False
      else: return True
```


I'm just not sure where the 'matrix class' is.  This would allow comparisons like


```
sage: matrixA == matrixB
True
```




---

archive/issue_comments_039782.json:
```json
{
    "body": "You bring up a good point, and make me doubt whether the feature request is even feasible.  Certainly it's probably not a beginner ticket after all.  The problem is that we already have an == operator:\n\n\n```\nsage: a=matrix(SR,2,[x,x^2,x+1,x+4])\nsage: b=matrix(SR,2,[4,3,2,1])\nsage: a==b\nFalse\n```\n\n\nThat means that all solve will see is False.  Instead, we want something like:\n\n\n```\n\nsage: SR(a)==SR(b)\n([    x   x^2]\n[x + 1 x + 4]) == ([4 3]\n[2 1])\n```\n\n \n(i.e., we want the == in the solve to construct an equation, which it does for symbolic objects.  One of the issues at heart here is that a symbolic object wrapping a Sage matrix is different from a Sage matrix containing symbolic objects.\n\nSo I'm going to take off beginner status for this ticket here.  It would still be nice if solve(SR(a)==SR(b)) worked in the above example.",
    "created_at": "2011-04-14T03:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5201#issuecomment-39782",
    "user": "https://github.com/jasongrout"
}
```

You bring up a good point, and make me doubt whether the feature request is even feasible.  Certainly it's probably not a beginner ticket after all.  The problem is that we already have an == operator:


```
sage: a=matrix(SR,2,[x,x^2,x+1,x+4])
sage: b=matrix(SR,2,[4,3,2,1])
sage: a==b
False
```


That means that all solve will see is False.  Instead, we want something like:


```

sage: SR(a)==SR(b)
([    x   x^2]
[x + 1 x + 4]) == ([4 3]
[2 1])
```

 
(i.e., we want the == in the solve to construct an equation, which it does for symbolic objects.  One of the issues at heart here is that a symbolic object wrapping a Sage matrix is different from a Sage matrix containing symbolic objects.

So I'm going to take off beginner status for this ticket here.  It would still be nice if solve(SR(a)==SR(b)) worked in the above example.



---

archive/issue_comments_039783.json:
```json
{
    "body": "Changing keywords from \"beginner\" to \"\".",
    "created_at": "2011-04-14T03:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5201#issuecomment-39783",
    "user": "https://github.com/jasongrout"
}
```

Changing keywords from "beginner" to "".



---

archive/issue_events_012038.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5201#event-12038"
}
```



---

archive/issue_events_012039.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5201#event-12039"
}
```



---

archive/issue_events_012040.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5201#event-12040"
}
```



---

archive/issue_events_012041.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5201#event-12041"
}
```



---

archive/issue_events_012042.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5201#event-12042"
}
```



---

archive/issue_events_012043.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5201#event-12043"
}
```



---

archive/issue_events_012044.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5201#event-12044"
}
```



---

archive/issue_events_012045.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5201#event-12045"
}
```



---

archive/issue_events_012046.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2015-02-24T09:07:56Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5201#event-12046"
}
```



---

archive/issue_events_012047.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2015-02-24T09:07:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5201",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5201#event-12047"
}
```
