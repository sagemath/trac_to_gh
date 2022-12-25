# Issue 607: Coleman integration bug

archive/issues_000607.json:
```json
{
    "body": "Assignee: @williamstein\n\n        sage: p = 71; m = 4\n        sage: K = pAdicField(p, m)\n        sage: x = polygen(K)\n        sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)\n        sage: P = C(-1, 1); P1 = C(-1, -1)\n        sage: Q = C(0, 1/4); Q1 = C(0, -1/4)\n        sage: x, y = C.monsky_washnitzer_gens()\n        sage: w = C.invariant_differential()\n        sage: w.integrate(P, Q), (x*w).integrate(P, Q)\n        (O(71^4), O(71^4))\n        sage: R, R1 = C.lift_x(4, all=True)\n        sage: w.integrate(P, R)\n        42*71 + 63*71^2 + 55*71^3 + O(71^4)\n        sage: w.integrate(P, R) + w.integrate(P1, R1)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/607\n\n",
    "created_at": "2007-09-07T00:29:15Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "Coleman integration bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/607",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

        sage: p = 71; m = 4
        sage: K = pAdicField(p, m)
        sage: x = polygen(K)
        sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)
        sage: P = C(-1, 1); P1 = C(-1, -1)
        sage: Q = C(0, 1/4); Q1 = C(0, -1/4)
        sage: x, y = C.monsky_washnitzer_gens()
        sage: w = C.invariant_differential()
        sage: w.integrate(P, Q), (x*w).integrate(P, Q)
        (O(71^4), O(71^4))
        sage: R, R1 = C.lift_x(4, all=True)
        sage: w.integrate(P, R)
        42*71 + 63*71^2 + 55*71^3 + O(71^4)
        sage: w.integrate(P, R) + w.integrate(P1, R1)


Issue created by migration from https://trac.sagemath.org/ticket/607





---

archive/issue_comments_003110.json:
```json
{
    "body": "\n```\n+        sage: p = 71; m = 4\n+        sage: K = pAdicField(p, m)\n+        sage: x = polygen(K)\n+        sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)\n+        sage: P = C(-1, 1); P1 = C(-1, -1)\n+        sage: Q = C(0, 1/4); Q1 = C(0, -1/4)\n+        sage: x, y = C.monsky_washnitzer_gens()\n+        sage: w = C.invariant_differential()\n+        sage: w.integrate(P, Q), (x*w).integrate(P, Q)\n+        (O(71^4), O(71^4))\n+        sage: R, R1 = C.lift_x(4, all=True)\n+        sage: w.integrate(P, R)\n+        42*71 + 63*71^2 + 55*71^3 + O(71^4)\n+        sage: w.integrate(P, R) + w.integrate(P1, R1)\n\n```\n",
    "created_at": "2007-09-07T00:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/607#issuecomment-3110",
    "user": "https://github.com/robertwb"
}
```


```
+        sage: p = 71; m = 4
+        sage: K = pAdicField(p, m)
+        sage: x = polygen(K)
+        sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)
+        sage: P = C(-1, 1); P1 = C(-1, -1)
+        sage: Q = C(0, 1/4); Q1 = C(0, -1/4)
+        sage: x, y = C.monsky_washnitzer_gens()
+        sage: w = C.invariant_differential()
+        sage: w.integrate(P, Q), (x*w).integrate(P, Q)
+        (O(71^4), O(71^4))
+        sage: R, R1 = C.lift_x(4, all=True)
+        sage: w.integrate(P, R)
+        42*71 + 63*71^2 + 55*71^3 + O(71^4)
+        sage: w.integrate(P, R) + w.integrate(P1, R1)

```




---

archive/issue_comments_003111.json:
```json
{
    "body": "Attachment [607a.patch](tarball://root/attachments/some-uuid/ticket607/607a.patch) by @robertwb created at 2007-09-07 00:31:00",
    "created_at": "2007-09-07T00:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/607#issuecomment-3111",
    "user": "https://github.com/robertwb"
}
```

Attachment [607a.patch](tarball://root/attachments/some-uuid/ticket607/607a.patch) by @robertwb created at 2007-09-07 00:31:00



---

archive/issue_comments_003112.json:
```json
{
    "body": "Attachment [607b.patch](tarball://root/attachments/some-uuid/ticket607/607b.patch) by @robertwb created at 2007-09-07 00:31:28",
    "created_at": "2007-09-07T00:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/607#issuecomment-3112",
    "user": "https://github.com/robertwb"
}
```

Attachment [607b.patch](tarball://root/attachments/some-uuid/ticket607/607b.patch) by @robertwb created at 2007-09-07 00:31:28



---

archive/issue_comments_003113.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-07T00:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/607#issuecomment-3113",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003114.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2007-09-07T00:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/607#issuecomment-3114",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_comments_003115.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T04:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/607#issuecomment-3115",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
