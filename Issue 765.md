# Issue 765: Ctrl-C unresponsive in rational_points

archive/issues_000765.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following isn't implemented in a useful way anyway, but the fact that crtl-C does not work properly is a bad sign:\n\n```\nP.<x>=QQ[]\nf=x^6+x^2+1\nC=HyperellipticCurve(f)\nJ=C.jacobian()\nK=J.kummer_surface()\nK.rational_points(bound=100)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/765\n\n",
    "created_at": "2007-09-30T20:25:27Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "Ctrl-C unresponsive in rational_points",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/765",
    "user": "@nbruin"
}
```
Assignee: @williamstein

The following isn't implemented in a useful way anyway, but the fact that crtl-C does not work properly is a bad sign:

```
P.<x>=QQ[]
f=x^6+x^2+1
C=HyperellipticCurve(f)
J=C.jacobian()
K=J.kummer_surface()
K.rational_points(bound=100)
```


Issue created by migration from https://trac.sagemath.org/ticket/765





---

archive/issue_comments_004527.json:
```json
{
    "body": "Weird.",
    "created_at": "2007-11-03T15:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/765#issuecomment-4527",
    "user": "@williamstein"
}
```

Weird.



---

archive/issue_comments_004528.json:
```json
{
    "body": "Control-c works fine now (tested on linux and osx).  Maybe this was fixed by the other control-c related fixes that Gonzalo Tornaria and I made at SD5.",
    "created_at": "2007-11-03T18:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/765#issuecomment-4528",
    "user": "@williamstein"
}
```

Control-c works fine now (tested on linux and osx).  Maybe this was fixed by the other control-c related fixes that Gonzalo Tornaria and I made at SD5.



---

archive/issue_comments_004529.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T18:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/765#issuecomment-4529",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_004530.json:
```json
{
    "body": "I found this ancient ticket while looking for anything mentioning kummer_surface.  With Sage 5.10 it does not work at all:\n\n```\nsage: P.<x>=QQ[]\nsage: f=x^6+x^2+1                                                                                \nsage: C=HyperellipticCurve(f)                                                                    \nsage: J=C.jacobian()                                                                             \nsage: K=J.kummer_surface()\n...\n/home/jec/sage-5.10/local/lib/python2.7/site-packages/sage/schemes/projective/projective_morphism.pyc in __init__(self, parent, polys, check)\n    139                 d = polys[0].degree()\n    140             except AttributeError:\n--> 141                 polys = [f.lift() for f in polys]\n    142             if not all([f.is_homogeneous() for f in polys]):\n    143                 raise  ValueError(\"polys (=%s) must be homogeneous\"%polys)\n\nAttributeError: 'int' object has no attribute 'lift'\n```\n",
    "created_at": "2013-07-11T10:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/765#issuecomment-4530",
    "user": "@JohnCremona"
}
```

I found this ancient ticket while looking for anything mentioning kummer_surface.  With Sage 5.10 it does not work at all:

```
sage: P.<x>=QQ[]
sage: f=x^6+x^2+1                                                                                
sage: C=HyperellipticCurve(f)                                                                    
sage: J=C.jacobian()                                                                             
sage: K=J.kummer_surface()
...
/home/jec/sage-5.10/local/lib/python2.7/site-packages/sage/schemes/projective/projective_morphism.pyc in __init__(self, parent, polys, check)
    139                 d = polys[0].degree()
    140             except AttributeError:
--> 141                 polys = [f.lift() for f in polys]
    142             if not all([f.is_homogeneous() for f in polys]):
    143                 raise  ValueError("polys (=%s) must be homogeneous"%polys)

AttributeError: 'int' object has no attribute 'lift'
```

