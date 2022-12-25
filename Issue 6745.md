# Issue 6745: quaternion algebras -- add computation of left and right orders associated to ideals

archive/issues_006745.json:
```json
{
    "body": "Assignee: tbd\n\nA big gap in functionality for quaternion algebras right now is that one can't compute the left and right orders associated to ideals (the functions raise NotImplementedError).    I just designed a little algorithm and wrote code to do this for my research and will post a patch here soon. \n\nJust in case I misplace it, some demo code that works is the following:\n\n```\ndef left_order(I):\n    Q = O.quaternion_algebra()\n    M = [matrix([(a*b).coefficient_tuple() for a in Q.basis()]) for b in I.basis()]\n    B = I.basis_matrix()\n    invs = [(B*m^(-1)).row_module(ZZ) for m in M]\n    IS = invs[0].intersection(invs[1]).intersection(invs[2]).intersection(invs[3])\n    ISB = [Q(v) for v in IS.basis()]\n    return Q.quaternion_order(ISB)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6745\n\n",
    "created_at": "2009-08-14T16:23:57Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "quaternion algebras -- add computation of left and right orders associated to ideals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6745",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

A big gap in functionality for quaternion algebras right now is that one can't compute the left and right orders associated to ideals (the functions raise NotImplementedError).    I just designed a little algorithm and wrote code to do this for my research and will post a patch here soon. 

Just in case I misplace it, some demo code that works is the following:

```
def left_order(I):
    Q = O.quaternion_algebra()
    M = [matrix([(a*b).coefficient_tuple() for a in Q.basis()]) for b in I.basis()]
    B = I.basis_matrix()
    invs = [(B*m^(-1)).row_module(ZZ) for m in M]
    IS = invs[0].intersection(invs[1]).intersection(invs[2]).intersection(invs[3])
    ISB = [Q(v) for v in IS.basis()]
    return Q.quaternion_order(ISB)
```


Issue created by migration from https://trac.sagemath.org/ticket/6745





---

archive/issue_comments_055391.json:
```json
{
    "body": "Attachment [trac_6745.patch](tarball://root/attachments/some-uuid/ticket6745/trac_6745.patch) by @robertwb created at 2009-08-16 09:18:21\n\nsage/algebras/quatalg/quaternion_algebra.py:1272\n\n\n```\nALGORITHM: Let `b_1, b_2, b_3, b_3` be a basis for this \n```\n\n\n(Typo, you want b_4). \n\nTabularUnified  sage/matrix/matrix_integer_dense.pyx:2310\n\n\n```\nif max(self._nrows, self._ncols) <= 50: \n```\n\n\nI think you intended to have an `elif` here. \n\nOther than that, looks good to me. Also, while I was playing around with it trying it out, I found #6762 useful.",
    "created_at": "2009-08-16T09:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6745#issuecomment-55391",
    "user": "https://github.com/robertwb"
}
```

Attachment [trac_6745.patch](tarball://root/attachments/some-uuid/ticket6745/trac_6745.patch) by @robertwb created at 2009-08-16 09:18:21

sage/algebras/quatalg/quaternion_algebra.py:1272


```
ALGORITHM: Let `b_1, b_2, b_3, b_3` be a basis for this 
```


(Typo, you want b_4). 

TabularUnified  sage/matrix/matrix_integer_dense.pyx:2310


```
if max(self._nrows, self._ncols) <= 50: 
```


I think you intended to have an `elif` here. 

Other than that, looks good to me. Also, while I was playing around with it trying it out, I found #6762 useful.



---

archive/issue_comments_055392.json:
```json
{
    "body": "William: any words on the typos reported by Robert?",
    "created_at": "2009-08-25T03:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6745#issuecomment-55392",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

William: any words on the typos reported by Robert?



---

archive/issue_comments_055393.json:
```json
{
    "body": "Regarding Robert's comments:\n\n* I posted a patch fixing the `b_3 |--> b_4` typo.\n\n* The matrix_integer_dense.pyx is *not* a typo.  The issue is that I want to default to pari for small matrices, *unless* said small matrix has huge entries, so the logic is correct (i.e., if entries huge, still use padic).  I've put in some spaces and an {{{# endif} comment to maybe make that seem more intentional. \n\nSo the attached patch changes no logic in the code, but changes/improves two comments.",
    "created_at": "2009-08-30T21:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6745#issuecomment-55393",
    "user": "https://github.com/williamstein"
}
```

Regarding Robert's comments:

* I posted a patch fixing the `b_3 |--> b_4` typo.

* The matrix_integer_dense.pyx is *not* a typo.  The issue is that I want to default to pari for small matrices, *unless* said small matrix has huge entries, so the logic is correct (i.e., if entries huge, still use padic).  I've put in some spaces and an {{{# endif} comment to maybe make that seem more intentional. 

So the attached patch changes no logic in the code, but changes/improves two comments.



---

archive/issue_comments_055394.json:
```json
{
    "body": "Attachment [trac_6745-part2.patch](tarball://root/attachments/some-uuid/ticket6745/trac_6745-part2.patch) by @williamstein created at 2009-08-30 21:58:48\n\nfix comments",
    "created_at": "2009-08-30T21:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6745#issuecomment-55394",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6745-part2.patch](tarball://root/attachments/some-uuid/ticket6745/trac_6745-part2.patch) by @williamstein created at 2009-08-30 21:58:48

fix comments



---

archive/issue_comments_055395.json:
```json
{
    "body": "Great. Positive review.",
    "created_at": "2009-08-31T16:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6745#issuecomment-55395",
    "user": "https://github.com/robertwb"
}
```

Great. Positive review.



---

archive/issue_comments_055396.json:
```json
{
    "body": "Merged both patches.",
    "created_at": "2009-09-02T15:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6745#issuecomment-55396",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged both patches.



---

archive/issue_comments_055397.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-02T15:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6745#issuecomment-55397",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_015909.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-02T15:41:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6745",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6745#event-15909"
}
```
