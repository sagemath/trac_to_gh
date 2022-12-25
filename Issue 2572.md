# Issue 2572: imag() not defined for Algebraic Real Field

archive/issues_002572.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @ncalexan\n\nKeywords: imag algebraic reals\n\nThis makes it hard to write generic code:\n\n\n```\nsage: L, (_, a), L_into_A = number_field_elements_from_algebraics([sqrt(2), sqrt(-2 + sqrt(2))*I], minimal=True)\nsage: L_into_A\n\nRing morphism:\n  From: Number Field in a with defining polynomial y^4 - 4*y^2 + 2\n  To:   Algebraic Real Field\n  Defn: a |--> [-0.76536686473017957 .. -0.76536686473017945]\nsage: L_into_A(a)\n[-0.76536686473017957 .. -0.76536686473017945]\nsage: L_into_A(a).imag()\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/Users/ncalexan/Documents/School/MATH235/genus2cm/<ipython console> in <module>()\n\n<type 'exceptions.AttributeError'>: 'AlgebraicReal' object has no attribute 'imag'\nsage: L, (z, ), L_into_A = number_field_elements_from_algebraics([QQbar.zeta(5)], minimal=True)\nsage: L_into_A\n\nRing morphism:\n  From: Cyclotomic Field of order 5 and degree 4\n  To:   Algebraic Field\n  Defn: zeta5 |--> [0.30901699437494739 .. 0.30901699437494746] + [0.95105651629515353 .. 0.95105651629515365]*I\nsage: L_into_A(z)\n[0.30901699437494739 .. 0.30901699437494746] + [0.95105651629515353 .. 0.95105651629515365]*I\nsage: L_into_A(z).imag()\n[0.95105651629515353 .. 0.95105651629515365]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2572\n\n",
    "created_at": "2008-03-17T17:29:07Z",
    "labels": [
        "component: commutative algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "imag() not defined for Algebraic Real Field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2572",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @malb

CC:  @ncalexan

Keywords: imag algebraic reals

This makes it hard to write generic code:


```
sage: L, (_, a), L_into_A = number_field_elements_from_algebraics([sqrt(2), sqrt(-2 + sqrt(2))*I], minimal=True)
sage: L_into_A

Ring morphism:
  From: Number Field in a with defining polynomial y^4 - 4*y^2 + 2
  To:   Algebraic Real Field
  Defn: a |--> [-0.76536686473017957 .. -0.76536686473017945]
sage: L_into_A(a)
[-0.76536686473017957 .. -0.76536686473017945]
sage: L_into_A(a).imag()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/ncalexan/Documents/School/MATH235/genus2cm/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'AlgebraicReal' object has no attribute 'imag'
sage: L, (z, ), L_into_A = number_field_elements_from_algebraics([QQbar.zeta(5)], minimal=True)
sage: L_into_A

Ring morphism:
  From: Cyclotomic Field of order 5 and degree 4
  To:   Algebraic Field
  Defn: zeta5 |--> [0.30901699437494739 .. 0.30901699437494746] + [0.95105651629515353 .. 0.95105651629515365]*I
sage: L_into_A(z)
[0.30901699437494739 .. 0.30901699437494746] + [0.95105651629515353 .. 0.95105651629515365]*I
sage: L_into_A(z).imag()
[0.95105651629515353 .. 0.95105651629515365]
```


Issue created by migration from https://trac.sagemath.org/ticket/2572





---

archive/issue_comments_017538.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-17T21:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2572#issuecomment-17538",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017539.json:
```json
{
    "body": "Changing assignee from @malb to cwitty.",
    "created_at": "2008-03-17T21:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2572#issuecomment-17539",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing assignee from @malb to cwitty.



---

archive/issue_comments_017540.json:
```json
{
    "body": "Attachment [trac2572-aa-real-imag.patch](tarball://root/attachments/some-uuid/ticket2572/trac2572-aa-real-imag.patch) by cwitty created at 2008-03-18 02:24:24\n\nThe attached patch adds the requested method (and .real() as well).  Doctests pass in sage/rings.",
    "created_at": "2008-03-18T02:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2572#issuecomment-17540",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac2572-aa-real-imag.patch](tarball://root/attachments/some-uuid/ticket2572/trac2572-aa-real-imag.patch) by cwitty created at 2008-03-18 02:24:24

The attached patch adds the requested method (and .real() as well).  Doctests pass in sage/rings.



---

archive/issue_comments_017541.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-03-20T01:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2572#issuecomment-17541",
    "user": "https://github.com/aghitza"
}
```

Looks good.



---

archive/issue_comments_017542.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-22T04:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2572#issuecomment-17542",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017543.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-22T04:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2572#issuecomment-17543",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha1



---

archive/issue_events_002755.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-22T04:03:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2572",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2572#event-2755"
}
```
