# Issue 20: coercion issues

archive/issues_000020.json:
```json
{
    "body": "Assignee: somebody\n\n```\nFrom David Harvey:\nFurther to our discussion of a few days ago, I found something quite confusing, not sure what the correct behaviour should be.\n \nsage: poly_ring1.<gen1> = PolynomialRing(QQ)\nsage: poly_ring2.<gen2> = PolynomialRing(QQ)\nsage: huge_ring.<x> = PolynomialRing(poly_ring1)\nsage: huge_ring(gen1)\n gen1\nsage: huge_ring(gen2)\n x\n \nIn the first example gen1 is getting coerced into a constant polynomial because it belongs to the coefficient ring, and in the second example it's \"renaming the variable\". I suppose that makes sense, although I'm a bit uneasy about the second one.\n \nBUT it's not consistent with the behaviour for power series:\n \nsage: power_ring1.<gen1> = PowerSeriesRing(QQ)\nsage: power_ring2.<gen2> = PowerSeriesRing(QQ)\nsage: huge_power_ring.<x> = PowerSeriesRing(power_ring1)\nsage: huge_power_ring(gen1)\n x\nsage: huge_power_ring(gen2)\n x\n \nIs this a bug?\n\nResponse: from william: \"Yes\"\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/20\n\n",
    "created_at": "2006-09-12T23:20:48Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "coercion issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/20",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

```
From David Harvey:
Further to our discussion of a few days ago, I found something quite confusing, not sure what the correct behaviour should be.
 
sage: poly_ring1.<gen1> = PolynomialRing(QQ)
sage: poly_ring2.<gen2> = PolynomialRing(QQ)
sage: huge_ring.<x> = PolynomialRing(poly_ring1)
sage: huge_ring(gen1)
 gen1
sage: huge_ring(gen2)
 x
 
In the first example gen1 is getting coerced into a constant polynomial because it belongs to the coefficient ring, and in the second example it's "renaming the variable". I suppose that makes sense, although I'm a bit uneasy about the second one.
 
BUT it's not consistent with the behaviour for power series:
 
sage: power_ring1.<gen1> = PowerSeriesRing(QQ)
sage: power_ring2.<gen2> = PowerSeriesRing(QQ)
sage: huge_power_ring.<x> = PowerSeriesRing(power_ring1)
sage: huge_power_ring(gen1)
 x
sage: huge_power_ring(gen2)
 x
 
Is this a bug?

Response: from william: "Yes"
```

Issue created by migration from https://trac.sagemath.org/ticket/20





---

archive/issue_events_000029.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-07T03:36:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/20",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/20#event-29"
}
```



---

archive/issue_comments_000077.json:
```json
{
    "body": "This is fixed in sage-1.5:\n\n```\nsage: power_ring1.<gen1> = PowerSeriesRing(QQ)\nsage: power_ring2.<gen2> = PowerSeriesRing(QQ)\nsage: huge_power_ring.<x> = PowerSeriesRing(power_ring1)\nsage: huge_power_ring(gen1)\ngen1\nsage: huge_power_ring(gen2)\nx\n```",
    "created_at": "2007-01-07T03:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/20",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/20#issuecomment-77",
    "user": "https://github.com/williamstein"
}
```

This is fixed in sage-1.5:

```
sage: power_ring1.<gen1> = PowerSeriesRing(QQ)
sage: power_ring2.<gen2> = PowerSeriesRing(QQ)
sage: huge_power_ring.<x> = PowerSeriesRing(power_ring1)
sage: huge_power_ring(gen1)
gen1
sage: huge_power_ring(gen2)
x
```



---

archive/issue_comments_000078.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-07T03:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/20",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/20#issuecomment-78",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
