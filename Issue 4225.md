# Issue 4225: faster sqrt for complex numbers

archive/issues_004225.json:
```json
{
    "body": "Assignee: tbd\n\nThis is a followup to #4132.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4225\n\n",
    "created_at": "2008-09-30T20:51:33Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "faster sqrt for complex numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4225",
    "user": "https://github.com/robertwb"
}
```
Assignee: tbd

This is a followup to #4132.

Issue created by migration from https://trac.sagemath.org/ticket/4225





---

archive/issue_comments_030642.json:
```json
{
    "body": "Code: \n\n\n```\ndef new_sqrt(ComplexNumber self, all=False):\n    cdef ComplexNumber z = self._new()\n    if mpfr_zero_p(self.__im):\n        if mpfr_sgn(self.__re) >= 0:\n            mpfr_set_ui(z.__im, 0, rnd)\n            mpfr_sqrt(z.__re, self.__re, rnd)\n        else:\n            mpfr_set_ui(z.__re, 0, rnd)\n            mpfr_neg(z.__im, self.__re, rnd)\n            mpfr_sqrt(z.__im, z.__im, rnd)\n        if all:\n            return [z, -z] if z else [z]\n        else:\n            return z\n    # self = x + yi = (a+bi)^2\n    # expand, substitute, solve\n    # a^2 = (x + sqrt(x^2+y^2))/2\n    cdef bint avoid_branch = mpfr_sgn(self.__re) < 0 and mpfr_cmpabs(self.__im, self.__re) < 0\n    cdef mpfr_t a2\n    mpfr_init2(a2, self._prec)\n    mpfr_hypot(a2, self.__re, self.__im, rnd)\n    if avoid_branch:\n        # x + sqrt(x^2+y^2) numerically unstable for x near negative real axis\n        # so we compute sqrt of (-z) and shift by i at the end\n        mpfr_sub(a2, a2, self.__re, rnd)\n    else:\n        mpfr_add(a2, a2, self.__re, rnd)\n    mpfr_mul_2si(a2, a2, -1, rnd)\n    # a = sqrt(a2)\n    mpfr_sqrt(z.__re, a2, rnd)\n    # b = y/(2a)\n    mpfr_div(z.__im, self.__im, z.__re, rnd)\n    mpfr_mul_2si(z.__im, z.__im, -1, rnd)\n    mpfr_clear(a2)\n    if avoid_branch:\n        # Now we shift by i depending on what side of the branch we were on.\n        mpfr_swap(z.__re, z.__im)\n        # Note that y was never negated, so b already has the opposite sign. \n        if mpfr_sgn(self.__im) < 0:\n            mpfr_neg(z.__re, z.__re, rnd)\n            mpfr_neg(z.__im, z.__im, rnd)\n    if all:\n        return [z, -z]\n    else:\n        return z\n```\n\n\nI will post a patch (with more documentation) when I have a copy of sage with #4132 included.",
    "created_at": "2008-09-30T20:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4225#issuecomment-30642",
    "user": "https://github.com/robertwb"
}
```

Code: 


```
def new_sqrt(ComplexNumber self, all=False):
    cdef ComplexNumber z = self._new()
    if mpfr_zero_p(self.__im):
        if mpfr_sgn(self.__re) >= 0:
            mpfr_set_ui(z.__im, 0, rnd)
            mpfr_sqrt(z.__re, self.__re, rnd)
        else:
            mpfr_set_ui(z.__re, 0, rnd)
            mpfr_neg(z.__im, self.__re, rnd)
            mpfr_sqrt(z.__im, z.__im, rnd)
        if all:
            return [z, -z] if z else [z]
        else:
            return z
    # self = x + yi = (a+bi)^2
    # expand, substitute, solve
    # a^2 = (x + sqrt(x^2+y^2))/2
    cdef bint avoid_branch = mpfr_sgn(self.__re) < 0 and mpfr_cmpabs(self.__im, self.__re) < 0
    cdef mpfr_t a2
    mpfr_init2(a2, self._prec)
    mpfr_hypot(a2, self.__re, self.__im, rnd)
    if avoid_branch:
        # x + sqrt(x^2+y^2) numerically unstable for x near negative real axis
        # so we compute sqrt of (-z) and shift by i at the end
        mpfr_sub(a2, a2, self.__re, rnd)
    else:
        mpfr_add(a2, a2, self.__re, rnd)
    mpfr_mul_2si(a2, a2, -1, rnd)
    # a = sqrt(a2)
    mpfr_sqrt(z.__re, a2, rnd)
    # b = y/(2a)
    mpfr_div(z.__im, self.__im, z.__re, rnd)
    mpfr_mul_2si(z.__im, z.__im, -1, rnd)
    mpfr_clear(a2)
    if avoid_branch:
        # Now we shift by i depending on what side of the branch we were on.
        mpfr_swap(z.__re, z.__im)
        # Note that y was never negated, so b already has the opposite sign. 
        if mpfr_sgn(self.__im) < 0:
            mpfr_neg(z.__re, z.__re, rnd)
            mpfr_neg(z.__im, z.__im, rnd)
    if all:
        return [z, -z]
    else:
        return z
```


I will post a patch (with more documentation) when I have a copy of sage with #4132 included.



---

archive/issue_comments_030643.json:
```json
{
    "body": "Attachment [4225-complex-sqrt.patch](tarball://root/attachments/some-uuid/ticket4225/4225-complex-sqrt.patch) by @robertwb created at 2008-10-03 07:45:44",
    "created_at": "2008-10-03T07:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4225#issuecomment-30643",
    "user": "https://github.com/robertwb"
}
```

Attachment [4225-complex-sqrt.patch](tarball://root/attachments/some-uuid/ticket4225/4225-complex-sqrt.patch) by @robertwb created at 2008-10-03 07:45:44



---

archive/issue_comments_030644.json:
```json
{
    "body": "Looks good to me.\n\nFor some reason I had some trouble applying the patch to my 3.1.3.alpha2, but I think that might be something messed up on my end.  I applied the patch manually and it works.",
    "created_at": "2008-10-03T12:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4225#issuecomment-30644",
    "user": "https://github.com/aghitza"
}
```

Looks good to me.

For some reason I had some trouble applying the patch to my 3.1.3.alpha2, but I think that might be something messed up on my end.  I applied the patch manually and it works.



---

archive/issue_comments_030645.json:
```json
{
    "body": "Yeah, I am having merge trouble against 3.1.3.alpha3, too. Can someone rebase this against alpha2?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-07T19:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4225#issuecomment-30645",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yeah, I am having merge trouble against 3.1.3.alpha3, too. Can someone rebase this against alpha2?

Cheers,

Michael



---

archive/issue_comments_030646.json:
```json
{
    "body": "Shoot... It's a pain to build an alpha just to do a rebase, but I'll see what I can do.",
    "created_at": "2008-10-07T19:17:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4225#issuecomment-30646",
    "user": "https://github.com/robertwb"
}
```

Shoot... It's a pain to build an alpha just to do a rebase, but I'll see what I can do.



---

archive/issue_comments_030647.json:
```json
{
    "body": "Replying to [comment:5 robertwb]:\n> Shoot... It's a pain to build an alpha just to do a rebase, but I'll see what I can do. \n\nYou can pull from\n\n/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/devel/sage\n\nCheers,\n\nMichael",
    "created_at": "2008-10-07T19:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4225#issuecomment-30647",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 robertwb]:
> Shoot... It's a pain to build an alpha just to do a rebase, but I'll see what I can do. 

You can pull from

/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/devel/sage

Cheers,

Michael



---

archive/issue_comments_030648.json:
```json
{
    "body": "Replying to [comment:5 robertwb]:\n\nI can do it in a couple of hours (since I already have alpha2 built).",
    "created_at": "2008-10-07T22:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4225#issuecomment-30648",
    "user": "https://github.com/aghitza"
}
```

Replying to [comment:5 robertwb]:

I can do it in a couple of hours (since I already have alpha2 built).



---

archive/issue_comments_030649.json:
```json
{
    "body": "rebased against 3.1.3.alpha2",
    "created_at": "2008-10-08T06:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4225#issuecomment-30649",
    "user": "https://github.com/aghitza"
}
```

rebased against 3.1.3.alpha2



---

archive/issue_comments_030650.json:
```json
{
    "body": "Attachment [4225-complex-sqrt.2.patch](tarball://root/attachments/some-uuid/ticket4225/4225-complex-sqrt.2.patch) by @aghitza created at 2008-10-08 06:09:15\n\nOK, I've uploaded a version rebased against 3.1.3.alpha2.\n\nFor the record, here is some timing info:\n\nbefore the patch:\n\n\n```\nsage: C = ComplexField()\nsage: z = C(1+i)\nsage: timeit(\"z.sqrt()\")\n625 loops, best of 3: 8.57 \u00b5s per loop\nsage: C = ComplexField(10000)\nsage: z = C(1+i)\nsage: timeit(\"z.sqrt()\")\n125 loops, best of 3: 6.95 ms per loop\n```\n\n\nafter the patch:\n\n\n```\nsage: C = ComplexField()\nsage: z = C(1+i)\nsage: timeit(\"z.sqrt()\")\n625 loops, best of 3: 2.27 \u00b5s per loop\nsage: C = ComplexField(10000)\nsage: z = C(1+i)\nsage: timeit(\"z.sqrt()\")\n625 loops, best of 3: 509 \u00b5s per loop\n```\n",
    "created_at": "2008-10-08T06:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4225#issuecomment-30650",
    "user": "https://github.com/aghitza"
}
```

Attachment [4225-complex-sqrt.2.patch](tarball://root/attachments/some-uuid/ticket4225/4225-complex-sqrt.2.patch) by @aghitza created at 2008-10-08 06:09:15

OK, I've uploaded a version rebased against 3.1.3.alpha2.

For the record, here is some timing info:

before the patch:


```
sage: C = ComplexField()
sage: z = C(1+i)
sage: timeit("z.sqrt()")
625 loops, best of 3: 8.57 µs per loop
sage: C = ComplexField(10000)
sage: z = C(1+i)
sage: timeit("z.sqrt()")
125 loops, best of 3: 6.95 ms per loop
```


after the patch:


```
sage: C = ComplexField()
sage: z = C(1+i)
sage: timeit("z.sqrt()")
625 loops, best of 3: 2.27 µs per loop
sage: C = ComplexField(10000)
sage: z = C(1+i)
sage: timeit("z.sqrt()")
625 loops, best of 3: 509 µs per loop
```




---

archive/issue_comments_030651.json:
```json
{
    "body": "Thanks!",
    "created_at": "2008-10-08T06:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4225#issuecomment-30651",
    "user": "https://github.com/robertwb"
}
```

Thanks!



---

archive/issue_comments_030652.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha3",
    "created_at": "2008-10-08T08:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4225#issuecomment-30652",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha3



---

archive/issue_comments_030653.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-08T08:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4225#issuecomment-30653",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009565.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-08T08:43:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4225",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4225#event-9565"
}
```
