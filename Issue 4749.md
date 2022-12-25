# Issue 4749: improve coercion of points between elliptic curves and reduction of points mod p

archive/issues_004749.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @cswiercz\n\nIf I have a point P on an elliptic curve E and F is another curve, then F(P) should work if possible.  It doesn't.   For example:\n\n```\nE = EllipticCurve([1,-1,0,94,9]) \nR = E([0,3]) + 5*E([8,31])      # big denom's\nE11 = E.change_ring(GF(11))\nE11(R) \n BOOM!\n```\n\nBut it should clear denominators and coerce in the triple like so:\n\n```\ndef reduce(R, p):\n    x, y = R.xy()\n    d = LCM(x.denominator(), y.denominator())\n    return R.curve().change_ring(GF(p))([x*d,y*d,d])\n```\n\n}}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/4749\n\n",
    "created_at": "2008-12-10T01:00:06Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "improve coercion of points between elliptic curves and reduction of points mod p",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4749",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @cswiercz

If I have a point P on an elliptic curve E and F is another curve, then F(P) should work if possible.  It doesn't.   For example:

```
E = EllipticCurve([1,-1,0,94,9]) 
R = E([0,3]) + 5*E([8,31])      # big denom's
E11 = E.change_ring(GF(11))
E11(R) 
 BOOM!
```

But it should clear denominators and coerce in the triple like so:

```
def reduce(R, p):
    x, y = R.xy()
    d = LCM(x.denominator(), y.denominator())
    return R.curve().change_ring(GF(p))([x*d,y*d,d])
```

}}}

Issue created by migration from https://trac.sagemath.org/ticket/4749





---

archive/issue_comments_035866.json:
```json
{
    "body": "Changing keywords from \"\" to \"elliptic curves\".",
    "created_at": "2008-12-16T05:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4749#issuecomment-35866",
    "user": "https://github.com/cswiercz"
}
```

Changing keywords from "" to "elliptic curves".



---

archive/issue_comments_035867.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-16T05:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4749#issuecomment-35867",
    "user": "https://github.com/cswiercz"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035868.json:
```json
{
    "body": "Attachment [4749.patch](tarball://root/attachments/some-uuid/ticket4749/4749.patch) by @cswiercz created at 2008-12-16 05:23:09",
    "created_at": "2008-12-16T05:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4749#issuecomment-35868",
    "user": "https://github.com/cswiercz"
}
```

Attachment [4749.patch](tarball://root/attachments/some-uuid/ticket4749/4749.patch) by @cswiercz created at 2008-12-16 05:23:09



---

archive/issue_comments_035869.json:
```json
{
    "body": "Changing assignee from @williamstein to @cswiercz.",
    "created_at": "2008-12-16T05:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4749#issuecomment-35869",
    "user": "https://github.com/cswiercz"
}
```

Changing assignee from @williamstein to @cswiercz.



---

archive/issue_comments_035870.json:
```json
{
    "body": "Change \"This functionality is implemented in the \\code{__call__} method. \" to \"This functionality is used in the \\code{__call__} method for elliptic curves.\"",
    "created_at": "2008-12-16T16:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4749#issuecomment-35870",
    "user": "https://github.com/williamstein"
}
```

Change "This functionality is implemented in the \code{__call__} method. " to "This functionality is used in the \code{__call__} method for elliptic curves."



---

archive/issue_comments_035871.json:
```json
{
    "body": "Attachment [4749-part2.patch](tarball://root/attachments/some-uuid/ticket4749/4749-part2.patch) by @cswiercz created at 2008-12-16 19:05:12",
    "created_at": "2008-12-16T19:05:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4749#issuecomment-35871",
    "user": "https://github.com/cswiercz"
}
```

Attachment [4749-part2.patch](tarball://root/attachments/some-uuid/ticket4749/4749-part2.patch) by @cswiercz created at 2008-12-16 19:05:12



---

archive/issue_comments_035872.json:
```json
{
    "body": "I have to give this a negative review.  This code does not treat the case where the point is 0 (i.e. E(0)).  It fails to reduce E(0) since the E.xy() will crash.  In the example, E11(E(0)) works ok since the __call__ function must test the input via is_zero() so that works, but:\n\n```\nsage: S = E11._reduce_point(E(0), 11)\n---------------------------------------------------------------------------\nZeroDivisionError  \n```\n\n\nSecondly, I don't know why this code is in ell_generic.  It only applies to elliptic curves defined over Q.  I think it belongs in ell_point.py, as a member function of class  EllipticCurvePoint_number_field.\n\nI noticed this patch just when I was working on something almost identical, though my code works over number fields.  So I would like to replace this patch with another, not just to correct the small glitch of E(0), but to make it work over number fields.  In fact, here is a chunk of code I wrote before I saw this patch posted in here with no changes:\n\n```\n        if K is rings.QQ:\n            pi = P\n        else:\n            pi = K.uniformizer(P)\n\n        # Make sure the curve is integral and locally minimal at P:\n        Emin = E.local_minimal_model(P)\n        urst = E.isomorphism_to(Emin)\n        Q = urst(self)\n\n        # Scale the homogeneous coordinates of the point to be primitive:\n        xyz = list(Q)\n        e = min([c.valuation(P) for c in xyz])\n        if e !=0:            \n            if K is rings.QQ:\n                pi = P\n            else:\n                pi = K.uniformizer(P)\n            pie = pi**e\n            xyz = [c/pie for c in xyz]\n```\n\nThis was just to get homogeneous coordinates in which one of x,y,z is a unit mod P, but then you could directly construct a point on the reduction from it.  (I was also concerned with having a non-minimal model at P.) \n\nI expect that I will post an alternative patch here before long.",
    "created_at": "2008-12-19T17:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4749#issuecomment-35872",
    "user": "https://github.com/JohnCremona"
}
```

I have to give this a negative review.  This code does not treat the case where the point is 0 (i.e. E(0)).  It fails to reduce E(0) since the E.xy() will crash.  In the example, E11(E(0)) works ok since the __call__ function must test the input via is_zero() so that works, but:

```
sage: S = E11._reduce_point(E(0), 11)
---------------------------------------------------------------------------
ZeroDivisionError  
```


Secondly, I don't know why this code is in ell_generic.  It only applies to elliptic curves defined over Q.  I think it belongs in ell_point.py, as a member function of class  EllipticCurvePoint_number_field.

I noticed this patch just when I was working on something almost identical, though my code works over number fields.  So I would like to replace this patch with another, not just to correct the small glitch of E(0), but to make it work over number fields.  In fact, here is a chunk of code I wrote before I saw this patch posted in here with no changes:

```
        if K is rings.QQ:
            pi = P
        else:
            pi = K.uniformizer(P)

        # Make sure the curve is integral and locally minimal at P:
        Emin = E.local_minimal_model(P)
        urst = E.isomorphism_to(Emin)
        Q = urst(self)

        # Scale the homogeneous coordinates of the point to be primitive:
        xyz = list(Q)
        e = min([c.valuation(P) for c in xyz])
        if e !=0:            
            if K is rings.QQ:
                pi = P
            else:
                pi = K.uniformizer(P)
            pie = pi**e
            xyz = [c/pie for c in xyz]
```

This was just to get homogeneous coordinates in which one of x,y,z is a unit mod P, but then you could directly construct a point on the reduction from it.  (I was also concerned with having a non-minimal model at P.) 

I expect that I will post an alternative patch here before long.



---

archive/issue_comments_035873.json:
```json
{
    "body": "Attachment [4749-part3.patch](tarball://root/attachments/some-uuid/ticket4749/4749-part3.patch) by @JohnCremona created at 2008-12-19 17:23:11",
    "created_at": "2008-12-19T17:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4749#issuecomment-35873",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [4749-part3.patch](tarball://root/attachments/some-uuid/ticket4749/4749-part3.patch) by @JohnCremona created at 2008-12-19 17:23:11



---

archive/issue_comments_035874.json:
```json
{
    "body": "OK, I relented.  I have added a patch which addresses the specific bug.  There is still a case for something more general, but it is quite hard to see how to get the __call__ function to do the right thing.  There has to be a way of telling in some more generality whether the base field of the point is a residue field of the base field of the curve (I mean that the other way round).  So it's harder than I thought, and its 5.22pm on the last Friday before a holiday, and the patch does do something which is already useful, so let's go for it!",
    "created_at": "2008-12-19T17:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4749#issuecomment-35874",
    "user": "https://github.com/JohnCremona"
}
```

OK, I relented.  I have added a patch which addresses the specific bug.  There is still a case for something more general, but it is quite hard to see how to get the __call__ function to do the right thing.  There has to be a way of telling in some more generality whether the base field of the point is a residue field of the base field of the curve (I mean that the other way round).  So it's harder than I thought, and its 5.22pm on the last Friday before a holiday, and the patch does do something which is already useful, so let's go for it!



---

archive/issue_events_004992.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-21T12:37:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4749",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4749#event-4992"
}
```



---

archive/issue_comments_035875.json:
```json
{
    "body": "Merged all three patches in Sage 3.2.3.alpha0",
    "created_at": "2008-12-21T12:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4749#issuecomment-35875",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.2.3.alpha0



---

archive/issue_comments_035876.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-21T12:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4749#issuecomment-35876",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
