# Issue 2496: bug in introspection (probably easy to fix)

archive/issues_002496.json:
```json
{
    "body": "Assignee: tba\n\nSee near the bottom below.    In particular the `X.points??` input\nshould fail gracefully rather than going boom with an eval error.  Closing\nthis ticket does not necessarily mean fixing anything more than making this\nfail gracefully. \n\n```\n> \n>  I had a Sage worksheet that created an Elliptic curve\n>  (E=EllipticCurve([0,17]))\n>  and then invoked E.rational_points(10).\n>  The code has obviously changed as it now expects\n>  different parameters and needs to be E.rational_points(bound=10).\n>  The real problems is I no longer get all the rational points. Maybe\n>  the\n>  definition of bound has changed? I had assumed it was a logarithmic\n>  bound on the points, but I get only the first few points (max X=4).\n>  \n>  I then tried to follow through the code and it's changed a lot since I\n>  first looked\n>  at it. rational_points() is now defined in .../schemes/generic/\n>  algebraic_schemes\n>  and I'm unable to figure out where to go from there. The code reads:\n>  \n>  ...\n>   if F == None:\n>             F = self.base_ring()\n>         X = self(F)\n>  ...\n>   return X.points(bound)\n>  \n>  Substituting the first part into my worksheet, with substituting E for\n>  self, I get\n>  X is Abelian group of points on Elliptic Curve defined by y^2  = x^3 +\n>  17\n>  over Rational Field.\n>  \n>  Next I try:\n>   X.points??\n>  \n>  and get\n>  ---------------------\n>  Traceback (most recent call last):\n>   File \"<stdin>\", line 1, in <module>\n>   File \"/home/bill/.sage/sage_notebook/worksheets/bill/5/code/16.py\",\n>  line 6, in <module>\n>     print _support_.source_code(\"\", globals())\n>   File \"/sage/current/local/lib/python2.5/site-packages/sage/server/\n>  support.py\", line 154, in source_code\n>     obj = eval(s, globs)\n>   File \"<string>\", line 0\n>  \n>     ^\n>  SyntaxError: unexpected EOF while parsing\n>  ----------------------\n>  Not much help there...\n>  Is this a  bug, two bugs, or am I just being my usual stupid self?\n>  \n\nYou score +1 for at least one bug (the second one).  The first\nregarding the bound is *probably* related to changes John Cremona\nmade to elliptic curves, and I hope he will comment on them soon.\nI've made your second bug above trac # \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2496\n\n",
    "closed_at": "2008-05-11T06:12:05Z",
    "created_at": "2008-03-12T15:48:31Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "bug in introspection (probably easy to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2496",
    "user": "https://github.com/williamstein"
}
```
Assignee: tba

See near the bottom below.    In particular the `X.points??` input
should fail gracefully rather than going boom with an eval error.  Closing
this ticket does not necessarily mean fixing anything more than making this
fail gracefully. 

```
> 
>  I had a Sage worksheet that created an Elliptic curve
>  (E=EllipticCurve([0,17]))
>  and then invoked E.rational_points(10).
>  The code has obviously changed as it now expects
>  different parameters and needs to be E.rational_points(bound=10).
>  The real problems is I no longer get all the rational points. Maybe
>  the
>  definition of bound has changed? I had assumed it was a logarithmic
>  bound on the points, but I get only the first few points (max X=4).
>  
>  I then tried to follow through the code and it's changed a lot since I
>  first looked
>  at it. rational_points() is now defined in .../schemes/generic/
>  algebraic_schemes
>  and I'm unable to figure out where to go from there. The code reads:
>  
>  ...
>   if F == None:
>             F = self.base_ring()
>         X = self(F)
>  ...
>   return X.points(bound)
>  
>  Substituting the first part into my worksheet, with substituting E for
>  self, I get
>  X is Abelian group of points on Elliptic Curve defined by y^2  = x^3 +
>  17
>  over Rational Field.
>  
>  Next I try:
>   X.points??
>  
>  and get
>  ---------------------
>  Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
>   File "/home/bill/.sage/sage_notebook/worksheets/bill/5/code/16.py",
>  line 6, in <module>
>     print _support_.source_code("", globals())
>   File "/sage/current/local/lib/python2.5/site-packages/sage/server/
>  support.py", line 154, in source_code
>     obj = eval(s, globs)
>   File "<string>", line 0
>  
>     ^
>  SyntaxError: unexpected EOF while parsing
>  ----------------------
>  Not much help there...
>  Is this a  bug, two bugs, or am I just being my usual stupid self?
>  

You score +1 for at least one bug (the second one).  The first
regarding the bound is *probably* related to changes John Cremona
made to elliptic curves, and I hope he will comment on them soon.
I've made your second bug above trac # 
```

Issue created by migration from https://trac.sagemath.org/ticket/2496





---

archive/issue_events_005876.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-05-11T06:12:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2496",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2496#event-5876"
}
```



---

archive/issue_comments_016887.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T06:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2496#issuecomment-16887",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_016888.json:
```json
{
    "body": "This is already fixed.  First, I can't figure out how to replicate any sort of X.points?? problem.  For me that works just fine.  Also, the questionable eval above in the traceback is as of sage-3.0.1 already wrapped in a try/except block.",
    "created_at": "2008-05-11T06:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2496",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2496#issuecomment-16888",
    "user": "https://github.com/williamstein"
}
```

This is already fixed.  First, I can't figure out how to replicate any sort of X.points?? problem.  For me that works just fine.  Also, the questionable eval above in the traceback is as of sage-3.0.1 already wrapped in a try/except block.
