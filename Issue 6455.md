# Issue 6455: Bug in twisting for p_primary_bound on Tate-Shafarevich groups

archive/issues_006455.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein\n\nKeywords: Tate Sharafevich group, Elliptic curves\n\nWilliam Stein found a bug in `p_primary_part`, namely\n\n\n```\nsage: E = EllipticCurve([-19,34]); E.cremona_label()  # y^2 = x^3 - 19*x + 34\n'944e1'\nsage: S = E.sha(); S\nShafarevich-Tate group for the Elliptic Curve defined by y^2 = x^3 -\n19*x + 34 over Rational Field\nsage: E.ap(5)\n-3\nsage: factor(944)\n2^4 * 59\nsage: S.an_padic(5)\nTraceback (most recent call last):\n...\nValueError: can not twist a curve of conductor (=472) by the quadratic\ntwist (=-4).\n```\n\n\nThe problem is at 2 and 3, we have to check if we are allowed to twist.\n\n\nAnd John Cremona suggested \n\n*Is it possible to add a doctest illustrating the suggestion to \"try an_padic instead\"? That would be useful for the reference manual.*\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6455\n\n",
    "created_at": "2009-07-01T13:57:06Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "Bug in twisting for p_primary_bound on Tate-Shafarevich groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6455",
    "user": "https://github.com/categorie"
}
```
Assignee: @williamstein

CC:  @williamstein

Keywords: Tate Sharafevich group, Elliptic curves

William Stein found a bug in `p_primary_part`, namely


```
sage: E = EllipticCurve([-19,34]); E.cremona_label()  # y^2 = x^3 - 19*x + 34
'944e1'
sage: S = E.sha(); S
Shafarevich-Tate group for the Elliptic Curve defined by y^2 = x^3 -
19*x + 34 over Rational Field
sage: E.ap(5)
-3
sage: factor(944)
2^4 * 59
sage: S.an_padic(5)
Traceback (most recent call last):
...
ValueError: can not twist a curve of conductor (=472) by the quadratic
twist (=-4).
```


The problem is at 2 and 3, we have to check if we are allowed to twist.


And John Cremona suggested 

*Is it possible to add a doctest illustrating the suggestion to "try an_padic instead"? That would be useful for the reference manual.*



Issue created by migration from https://trac.sagemath.org/ticket/6455





---

archive/issue_comments_051872.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T19:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6455#issuecomment-51872",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_051873.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T19:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6455#issuecomment-51873",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_051874.json:
```json
{
    "body": "I believe that the patch chooses now the correct twist. \n\nWilliam : could you use it for the table, before it goes in ? so that I am sure that there are no further problems with it. I have tested it only on a few examples.",
    "created_at": "2009-07-21T21:37:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6455#issuecomment-51874",
    "user": "https://github.com/categorie"
}
```

I believe that the patch chooses now the correct twist. 

William : could you use it for the table, before it goes in ? so that I am sure that there are no further problems with it. I have tested it only on a few examples.



---

archive/issue_comments_051875.json:
```json
{
    "body": "Attachment [trac_6455.patch](tarball://root/attachments/some-uuid/ticket6455/trac_6455.patch) by @categorie created at 2009-07-21 21:37:33",
    "created_at": "2009-07-21T21:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6455#issuecomment-51875",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_6455.patch](tarball://root/attachments/some-uuid/ticket6455/trac_6455.patch) by @categorie created at 2009-07-21 21:37:33



---

archive/issue_comments_051876.json:
```json
{
    "body": "Patch applies fine to 4.1.1, and tests run ok.  The code looks ok to me too.  I'm not quite expert enough to be 100% confident, but enough to pass this!",
    "created_at": "2009-08-17T19:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6455#issuecomment-51876",
    "user": "https://github.com/JohnCremona"
}
```

Patch applies fine to 4.1.1, and tests run ok.  The code looks ok to me too.  I'm not quite expert enough to be 100% confident, but enough to pass this!



---

archive/issue_comments_051877.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-06T19:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6455#issuecomment-51877",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_051878.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-06T19:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6455#issuecomment-51878",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051879.json:
```json
{
    "body": "Remove assignee @loefflerd.",
    "created_at": "2009-10-09T09:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6455#issuecomment-51879",
    "user": "https://github.com/loefflerd"
}
```

Remove assignee @loefflerd.



---

archive/issue_comments_051880.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-19T06:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6455#issuecomment-51880",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_006695.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-19T06:02:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6455",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6455#event-6695"
}
```
