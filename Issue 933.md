# Issue 933: Permanents of (0,1)-matrices

archive/issues_000933.json:
```json
{
    "body": "Assignee: @williamstein\n\nLet A = (a_{ij}) be an m x n (m <= n) (0,1)-matrix. We define a\nmatrix X = (x_{ij}) with independent indeterminates x_{ij}:\nx_{ij} = 0 iff a_{ij} = 0.\n\nSo x_{ij} only exists iff a_{ij} = 1.\n\n\nNow define a list of equations: (how do I format them properly here?)\n\n\\sum_{i=1}^{i=m} x_{ij} = 1 for j = 1, ..., n\n\n\\sum_{j=1}^{j=n} x_{ij} = 1 for i = 1, ..., m\n\nx_{ij}^2 = x_{ij} for i = 1, ..., m and j = 1, ..., n\n\n\nIt is easy to prove that the number of solutions to this equations is\nequal to the permanent of A.\n\nBased on a paper from Bernasconi, et al.: Computing Groebner Bases\nin the Boolean Setting with Applications to Counting (1997) (which\nrestricts itself to square matrices and a number of polynomials less than 255),\nwe can do the following:\n\n1) calculate a Groebner basis\n\n2) compute the number of solutions (the permanent)\n\nIf this could be done fast, it beats Ryser's algorithm (See the\narticle above).\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/933\n\n",
    "created_at": "2007-10-19T19:00:37Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Permanents of (0,1)-matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/933",
    "user": "https://github.com/jaapspies"
}
```
Assignee: @williamstein

Let A = (a_{ij}) be an m x n (m <= n) (0,1)-matrix. We define a
matrix X = (x_{ij}) with independent indeterminates x_{ij}:
x_{ij} = 0 iff a_{ij} = 0.

So x_{ij} only exists iff a_{ij} = 1.


Now define a list of equations: (how do I format them properly here?)

\sum_{i=1}^{i=m} x_{ij} = 1 for j = 1, ..., n

\sum_{j=1}^{j=n} x_{ij} = 1 for i = 1, ..., m

x_{ij}^2 = x_{ij} for i = 1, ..., m and j = 1, ..., n


It is easy to prove that the number of solutions to this equations is
equal to the permanent of A.

Based on a paper from Bernasconi, et al.: Computing Groebner Bases
in the Boolean Setting with Applications to Counting (1997) (which
restricts itself to square matrices and a number of polynomials less than 255),
we can do the following:

1) calculate a Groebner basis

2) compute the number of solutions (the permanent)

If this could be done fast, it beats Ryser's algorithm (See the
article above).

Jaap

Issue created by migration from https://trac.sagemath.org/ticket/933





---

archive/issue_comments_005681.json:
```json
{
    "body": "> calculate a Groebner basis \n\n\nover which field?",
    "created_at": "2008-09-17T14:06:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/933#issuecomment-5681",
    "user": "https://github.com/malb"
}
```

> calculate a Groebner basis 


over which field?



---

archive/issue_events_002564.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/933",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/933#event-2564"
}
```



---

archive/issue_events_002565.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/933",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/933#event-2565"
}
```



---

archive/issue_events_002566.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/933",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/933#event-2566"
}
```



---

archive/issue_events_002567.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/933",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/933#event-2567"
}
```



---

archive/issue_events_002568.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/933",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/933#event-2568"
}
```



---

archive/issue_events_002569.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/933",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/933#event-2569"
}
```



---

archive/issue_events_002570.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/933",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/933#event-2570"
}
```



---

archive/issue_comments_005682.json:
```json
{
    "body": "Replying to [comment:3 malb]:\n> > calculate a Groebner basis \n\n> \n> over which field?\n\n\n`ZZ`. You want the `0-1` solutions and the `x = x^2` guarantees exactly that.",
    "created_at": "2015-08-17T12:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/933#issuecomment-5682",
    "user": "https://github.com/videlec"
}
```

Replying to [comment:3 malb]:
> > calculate a Groebner basis 

> 
> over which field?


`ZZ`. You want the `0-1` solutions and the `x = x^2` guarantees exactly that.
