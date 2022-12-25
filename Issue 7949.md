# Issue 7949: Bit-shifts in Z/(n)

archive/issues_007949.json:
```json
{
    "body": "Assignee: spancratz\n\nKeywords: bit shift, integer mod ring\n\nCurrently, some code for bit-shifts in Z/(n) looks like\n\n```\n    def __lshift__(IntegerMod_gmp self, int right):\n        ...\n        cdef IntegerMod_gmp x\n        x = self._new_c()\n        mpz_mul_2exp(x.value, self.value, right)\n        mpz_fdiv_r(x.value, x.value, self.__modulus.sageInteger.value)\n        return x\n```\n\nwhere the method ``mpz_mul_2exp`` expect an ``unsigned long``.  Negative values of ``right`` thus cause undesired integral promotion.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7949\n\n",
    "created_at": "2010-01-16T17:43:34Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Bit-shifts in Z/(n)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7949",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```
Assignee: spancratz

Keywords: bit shift, integer mod ring

Currently, some code for bit-shifts in Z/(n) looks like

```
    def __lshift__(IntegerMod_gmp self, int right):
        ...
        cdef IntegerMod_gmp x
        x = self._new_c()
        mpz_mul_2exp(x.value, self.value, right)
        mpz_fdiv_r(x.value, x.value, self.__modulus.sageInteger.value)
        return x
```

where the method ``mpz_mul_2exp`` expect an ``unsigned long``.  Negative values of ``right`` thus cause undesired integral promotion.

Issue created by migration from https://trac.sagemath.org/ticket/7949





---

archive/issue_comments_069237.json:
```json
{
    "body": "Looking at the related methods for types ``IntegerMod_int``, note that\n\n```\n    def __rshift__(IntegerMod_int self, int right):\n        ...\n        return self._new_c(self.ivalue >> right)\n```\nHere, the code ignores right shifts with negative values of ``right``, in which case one has to take the modulus.\n\nThe patch (to be attached) will address this, too.",
    "created_at": "2010-01-16T18:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7949#issuecomment-69237",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Looking at the related methods for types ``IntegerMod_int``, note that

```
    def __rshift__(IntegerMod_int self, int right):
        ...
        return self._new_c(self.ivalue >> right)
```
Here, the code ignores right shifts with negative values of ``right``, in which case one has to take the modulus.

The patch (to be attached) will address this, too.



---

archive/issue_comments_069238.json:
```json
{
    "body": "For each of the three types for moduli (32-bit, 64-bit, mpz_t), the patch provides a method ``shift``, which in turns is called by the methods ``__lshift__`` and ``__rshift__``.\n\nFinally, in the previous code the doctests with modulus `2^{31}-1` did not test any of the 64-bit code because of code in the method ``def __init__(NativeIntStruct self, sage.rings.integer.Integer z)`` in the file ``integer_mod.pyx``.  There, a comparisons were carried out with ``<`` rather than ``<=``, which this patch changes, too.",
    "created_at": "2010-01-16T18:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7949#issuecomment-69238",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

For each of the three types for moduli (32-bit, 64-bit, mpz_t), the patch provides a method ``shift``, which in turns is called by the methods ``__lshift__`` and ``__rshift__``.

Finally, in the previous code the doctests with modulus `2^{31}-1` did not test any of the 64-bit code because of code in the method ``def __init__(NativeIntStruct self, sage.rings.integer.Integer z)`` in the file ``integer_mod.pyx``.  There, a comparisons were carried out with ``<`` rather than ``<=``, which this patch changes, too.



---

archive/issue_comments_069239.json:
```json
{
    "body": "Attachment [trac7949.patch](tarball://root/attachments/some-uuid/ticket7949/trac7949.patch) by spancratz created at 2010-01-16 18:55:12",
    "created_at": "2010-01-16T18:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7949#issuecomment-69239",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac7949.patch](tarball://root/attachments/some-uuid/ticket7949/trac7949.patch) by spancratz created at 2010-01-16 18:55:12



---

archive/issue_comments_069240.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T18:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7949#issuecomment-69240",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069241.json:
```json
{
    "body": "Attachment [trac7949_doc.patch](tarball://root/attachments/some-uuid/ticket7949/trac7949_doc.patch) by spancratz created at 2010-01-19 02:59:21\n\nAdditional patch (more doctests)",
    "created_at": "2010-01-19T02:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7949#issuecomment-69241",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac7949_doc.patch](tarball://root/attachments/some-uuid/ticket7949/trac7949_doc.patch) by spancratz created at 2010-01-19 02:59:21

Additional patch (more doctests)



---

archive/issue_comments_069242.json:
```json
{
    "body": "This patch adds documentation, hopefully this will do.",
    "created_at": "2010-01-19T03:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7949#issuecomment-69242",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

This patch adds documentation, hopefully this will do.



---

archive/issue_comments_069243.json:
```json
{
    "body": "looks good to me.  I tested on 64-bit.",
    "created_at": "2010-01-19T07:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7949#issuecomment-69243",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

looks good to me.  I tested on 64-bit.



---

archive/issue_comments_069244.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T07:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7949#issuecomment-69244",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019026.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-22T21:36:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7949",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7949#event-19026"
}
```



---

archive/issue_comments_069245.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-22T21:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7949#issuecomment-69245",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
