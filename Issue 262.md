# Issue 262: extend point counting on elliptic curves to non-prime finite fields

archive/issues_000262.json:
```json
{
    "body": "Assignee: @williamstein\n\nAs a first step, do the case when the coefficients of the curve are\nin GF(p).\n\n```\nHello,\n \nCurrently, asking SAGE for the cardinality of an elliptic curve over a non-prime finite field gives the following message\n \nWARNING: Using very very stupid algorithm for counting\npoints over non-prime finite field. Please rewrite.\n \nFor elliptic curves with coefficients in the integers this is a fairly easy rewrite, which I've attached as the function smartercard; I describe the mathematical background here- http://maths.straylight.co.uk/archives/67 . However, I lack the programming skills to tie this into SAGE; since there are coding sprints in the near future, perhaps someone could take a look at incorporating this idea?\n \nCheers, Graeme\n```\n\n\n\n```\ndef smartercard(E):\n        G=E.base_field();\n        p=G.characteristic();\n        q=G.cardinality();\n        r=log(q,b=p);\n        Ep=EllipticCurve(GF(p,'a'),E.a_invariants());\n        t=Ep.trace_of_frobenius();\n        alphap=t/2 + I*sqrt(p-t^2/4);\n        Np=q + 1 - (alphap)^r - (alphap.conjugate())^r;\n        return(int(Np))\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/262\n\n",
    "created_at": "2007-02-15T15:57:47Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4.2",
    "title": "extend point counting on elliptic curves to non-prime finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/262",
    "user": "@williamstein"
}
```
Assignee: @williamstein

As a first step, do the case when the coefficients of the curve are
in GF(p).

```
Hello,
 
Currently, asking SAGE for the cardinality of an elliptic curve over a non-prime finite field gives the following message
 
WARNING: Using very very stupid algorithm for counting
points over non-prime finite field. Please rewrite.
 
For elliptic curves with coefficients in the integers this is a fairly easy rewrite, which I've attached as the function smartercard; I describe the mathematical background here- http://maths.straylight.co.uk/archives/67 . However, I lack the programming skills to tie this into SAGE; since there are coding sprints in the near future, perhaps someone could take a look at incorporating this idea?
 
Cheers, Graeme
```



```
def smartercard(E):
        G=E.base_field();
        p=G.characteristic();
        q=G.cardinality();
        r=log(q,b=p);
        Ep=EllipticCurve(GF(p,'a'),E.a_invariants());
        t=Ep.trace_of_frobenius();
        alphap=t/2 + I*sqrt(p-t^2/4);
        Np=q + 1 - (alphap)^r - (alphap.conjugate())^r;
        return(int(Np))
```


Issue created by migration from https://trac.sagemath.org/ticket/262





---

archive/issue_comments_001244.json:
```json
{
    "body": "I have added the code by Alex Ghitza that implements the algorithm mentioned above into SAGE for 2.8.4.2.",
    "created_at": "2007-09-13T05:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/262#issuecomment-1244",
    "user": "@williamstein"
}
```

I have added the code by Alex Ghitza that implements the algorithm mentioned above into SAGE for 2.8.4.2.



---

archive/issue_comments_001245.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-13T05:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/262#issuecomment-1245",
    "user": "@williamstein"
}
```

Resolution: fixed
