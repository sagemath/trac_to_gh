# Issue 1756: implement MPolynomialIdeal.hilbert_[series|polynomial]

archive/issues_001756.json:
```json
{
    "body": "Assignee: @malb\n\nThe result should be somewhat similar to what MAGMA has to offer\n\n   http://magma.maths.usyd.edu.au/magma/htmlhelp/text1128.htm\n\n. SINGULAR has support for Hilbert Series computation\n\n  http://www.singular.uni-kl.de/Manual/3-0-4/sing_212.htm\n\nwhich probably can be wrapped to provide the desired functionality.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1756\n\n",
    "closed_at": "2008-01-16T15:47:08Z",
    "created_at": "2008-01-11T18:34:12Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "implement MPolynomialIdeal.hilbert_[series|polynomial]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1756",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

The result should be somewhat similar to what MAGMA has to offer

   http://magma.maths.usyd.edu.au/magma/htmlhelp/text1128.htm

. SINGULAR has support for Hilbert Series computation

  http://www.singular.uni-kl.de/Manual/3-0-4/sing_212.htm

which probably can be wrapped to provide the desired functionality.

Issue created by migration from https://trac.sagemath.org/ticket/1756





---

archive/issue_comments_011056.json:
```json
{
    "body": "Singular's Hilbert series has overflow issues in certain situations. Let me digg out some email about a test case and report this to the Singular team.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-11T18:40:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1756#issuecomment-11056",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Singular's Hilbert series has overflow issues in certain situations. Let me digg out some email about a test case and report this to the Singular team.

Cheers,

Michael



---

archive/issue_comments_011057.json:
```json
{
    "body": "See #1793 for a patch, copying mabshoff's comment over to that ticket now and closing this as dupe.",
    "created_at": "2008-01-16T15:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1756#issuecomment-11057",
    "user": "https://github.com/malb"
}
```

See #1793 for a patch, copying mabshoff's comment over to that ticket now and closing this as dupe.



---

archive/issue_events_004258.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2008-01-16T15:47:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1756",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1756#event-4258"
}
```



---

archive/issue_comments_011058.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-01-16T15:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1756#issuecomment-11058",
    "user": "https://github.com/malb"
}
```

Resolution: duplicate
