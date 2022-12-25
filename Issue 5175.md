# Issue 5175: [bug] Bug computing Bessel function J0(0)

archive/issues_005175.json:
```json
{
    "body": "Assignee: tbd\n\nA bug under sage 3.2.3 computing J_0(0)\n(which should be just \"1\")\n\nsage: g=Bessel(0)\nsage: g          \nJ_{0}            \nsage: g(1)\n0.765197686557967\nsage: g(0)      \n\n---\nPariError                                 Traceback (most recent call last)\n\n/home/pablo/sage/sage-3.1/<ipython console> in <module>()\n\n/home/pablo/sage/sage-3.1/local/lib/python2.5/site-packages/sage/functions/special.pyc in __call__(self, z)\n    689             return bessel_I(nu,z,algorithm=s,prec=p)\n    690         if t == \"J\":\n--> 691             return bessel_J(nu,z,algorithm=s,prec=p)\n    692         if t == \"K\":\n    693             return bessel_K(nu,z,algorithm=s,prec=p)\n\n/home/pablo/sage/sage-3.1/local/lib/python2.5/site-packages/sage/functions/special.pyc in bessel_J(nu, z, algorithm, prec)\n    522             K = C\n    523         K = z.parent()\n--> 524         return K(pari(nu).besselj(z, precision=prec))\n    525     elif algorithm==\"scipy\":\n    526         if prec != 53:\n\n/home/pablo/sage/sage-3.1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38645)()\n\nPariError:  (8)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5175\n\n",
    "created_at": "2009-02-04T17:19:04Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[bug] Bug computing Bessel function J0(0)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5175",
    "user": "https://github.com/pdenapo"
}
```
Assignee: tbd

A bug under sage 3.2.3 computing J_0(0)
(which should be just "1")

sage: g=Bessel(0)
sage: g          
J_{0}            
sage: g(1)
0.765197686557967
sage: g(0)      

---
PariError                                 Traceback (most recent call last)

/home/pablo/sage/sage-3.1/<ipython console> in <module>()

/home/pablo/sage/sage-3.1/local/lib/python2.5/site-packages/sage/functions/special.pyc in __call__(self, z)
    689             return bessel_I(nu,z,algorithm=s,prec=p)
    690         if t == "J":
--> 691             return bessel_J(nu,z,algorithm=s,prec=p)
    692         if t == "K":
    693             return bessel_K(nu,z,algorithm=s,prec=p)

/home/pablo/sage/sage-3.1/local/lib/python2.5/site-packages/sage/functions/special.pyc in bessel_J(nu, z, algorithm, prec)
    522             K = C
    523         K = z.parent()
--> 524         return K(pari(nu).besselj(z, precision=prec))
    525     elif algorithm=="scipy":
    526         if prec != 53:

/home/pablo/sage/sage-3.1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38645)()

PariError:  (8)

Issue created by migration from https://trac.sagemath.org/ticket/5175





---

archive/issue_events_011972.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-04T20:28:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5175",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5175#event-11972"
}
```



---

archive/issue_comments_039568.json:
```json
{
    "body": "Changing component from algebra to interfaces.",
    "created_at": "2009-07-11T11:18:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5175#issuecomment-39568",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to interfaces.



---

archive/issue_comments_039569.json:
```json
{
    "body": "This works in sage-4.1:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: g = Bessel(0)\nsage: g(0)\n1.00000000000000\n```",
    "created_at": "2009-07-11T11:18:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5175#issuecomment-39569",
    "user": "https://github.com/aghitza"
}
```

This works in sage-4.1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: g = Bessel(0)
sage: g(0)
1.00000000000000
```



---

archive/issue_comments_039570.json:
```json
{
    "body": "Changing assignee from tbd to @williamstein.",
    "created_at": "2009-07-11T11:18:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5175#issuecomment-39570",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from tbd to @williamstein.



---

archive/issue_events_011973.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-12T16:04:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5175",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5175#event-11973"
}
```



---

archive/issue_comments_039571.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-12T16:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5175#issuecomment-39571",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
