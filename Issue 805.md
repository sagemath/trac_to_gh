# Issue 805: is_trivial() does not work for fractional ideals of number field

archive/issues_000805.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: F.<a> = QuadraticField(-5)\nsage: I = F.ideal(3)\nsage: I.is_trivial()\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/Users/david/sage-2.8.5/<ipython console> in <module>()\n\n/Users/david/sage-2.8.5/local/lib/python2.5/site-packages/sage/rings/ideal.py in is_trivial(self)\n    229             return True\n    230         elif self.is_principal():\n--> 231             return self.gen().is_unit()\n    232         raise NotImplementedError\n    233 \n\n<type 'exceptions.AttributeError'>: 'NumberFieldIdeal' object has no attribute 'gen'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/805\n\n",
    "created_at": "2007-10-03T14:12:24Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.13",
    "title": "is_trivial() does not work for fractional ideals of number field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/805",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @williamstein


```
sage: F.<a> = QuadraticField(-5)
sage: I = F.ideal(3)
sage: I.is_trivial()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/david/sage-2.8.5/<ipython console> in <module>()

/Users/david/sage-2.8.5/local/lib/python2.5/site-packages/sage/rings/ideal.py in is_trivial(self)
    229             return True
    230         elif self.is_principal():
--> 231             return self.gen().is_unit()
    232         raise NotImplementedError
    233 

<type 'exceptions.AttributeError'>: 'NumberFieldIdeal' object has no attribute 'gen'
```



Issue created by migration from https://trac.sagemath.org/ticket/805





---

archive/issue_comments_004847.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-04T02:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/805#issuecomment-4847",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004848.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2007-11-04T02:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/805#issuecomment-4848",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_comments_004849.json:
```json
{
    "body": "Attachment [805-trivial_nf_ideal.diff](tarball://root/attachments/some-uuid/ticket805/805-trivial_nf_ideal.diff) by @robertwb created at 2007-11-04 02:37:43",
    "created_at": "2007-11-04T02:37:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/805#issuecomment-4849",
    "user": "https://github.com/robertwb"
}
```

Attachment [805-trivial_nf_ideal.diff](tarball://root/attachments/some-uuid/ticket805/805-trivial_nf_ideal.diff) by @robertwb created at 2007-11-04 02:37:43



---

archive/issue_comments_004850.json:
```json
{
    "body": "Attachment [805-ncalexan-general-2.diff](tarball://root/attachments/some-uuid/ticket805/805-ncalexan-general-2.diff) by @ncalexan created at 2007-11-04 03:07:59\n\nBoth patches above should be applied: Robert's handles the special case of number fields; mine fixes a bug in multipolynomial ideals and makes generic ideals more robust.",
    "created_at": "2007-11-04T03:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/805#issuecomment-4850",
    "user": "https://github.com/ncalexan"
}
```

Attachment [805-ncalexan-general-2.diff](tarball://root/attachments/some-uuid/ticket805/805-ncalexan-general-2.diff) by @ncalexan created at 2007-11-04 03:07:59

Both patches above should be applied: Robert's handles the special case of number fields; mine fixes a bug in multipolynomial ideals and makes generic ideals more robust.



---

archive/issue_comments_004851.json:
```json
{
    "body": "GOOD -- I especially like Nick's improvements.",
    "created_at": "2007-11-18T04:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/805#issuecomment-4851",
    "user": "https://github.com/williamstein"
}
```

GOOD -- I especially like Nick's improvements.



---

archive/issue_comments_004852.json:
```json
{
    "body": "Merged in 2.8.13.alpha1.",
    "created_at": "2007-11-19T22:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/805#issuecomment-4852",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.13.alpha1.



---

archive/issue_comments_004853.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-19T22:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/805#issuecomment-4853",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
