# Issue 1141: Number Field elements arithmetic speed

archive/issues_001141.json:
```json
{
    "body": "Assignee: somebody\n\nThis patch just makes a few minor adjustments which gain a bit of speed with number field elements.  It's barely worth talking about for absolute fields, but its quite nice for relative number fields.\n\nThe main work of the patch is to place a pointer to the defining polynomial into the number field element.  This possibly introduces more maintenance, but the alternative is to move the number field parent class to cython.\n\noriginal:\n\n```\nsage: L.<a> = CyclotomicField(3).extension(x^3 - 2)\nsage: timeit a^6\n100 loops, best of 3: 2.89 ms per loop\nsage: K.<a> = NumberField(x^3-2*x^2+12)\nsage: timeit a^4\n10000 loops, best of 3: 44.3 \u00c2\u00b5s per loop\nsage: O.<a,b> = EquationOrder([x^2+1, x^2+2])\nsage: timeit a*b\n1000 loops, best of 3: 770 \u00c2\u00b5s per loop\n```\n\n\npatched:\n\n```\nsage: L.<a> = CyclotomicField(3).extension(x^3 - 2)\nsage: timeit a^6\n10000 loops, best of 3: 92.7 \u00c2\u00b5s per loop\nsage: K.<a> = NumberField(x^3-2*x^2+12)\nsage: timeit a^4\n10000 loops, best of 3: 30.6 \u00c2\u00b5s per loop\nsage: O.<a,b> = EquationOrder([x^2+1, x^2+2])\nsage: timeit a*b\n100000 loops, best of 3: 19 \u00c2\u00b5s per loop\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1141\n\n",
    "created_at": "2007-11-10T20:55:02Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Number Field elements arithmetic speed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1141",
    "user": "jbmohler"
}
```
Assignee: somebody

This patch just makes a few minor adjustments which gain a bit of speed with number field elements.  It's barely worth talking about for absolute fields, but its quite nice for relative number fields.

The main work of the patch is to place a pointer to the defining polynomial into the number field element.  This possibly introduces more maintenance, but the alternative is to move the number field parent class to cython.

original:

```
sage: L.<a> = CyclotomicField(3).extension(x^3 - 2)
sage: timeit a^6
100 loops, best of 3: 2.89 ms per loop
sage: K.<a> = NumberField(x^3-2*x^2+12)
sage: timeit a^4
10000 loops, best of 3: 44.3 Âµs per loop
sage: O.<a,b> = EquationOrder([x^2+1, x^2+2])
sage: timeit a*b
1000 loops, best of 3: 770 Âµs per loop
```


patched:

```
sage: L.<a> = CyclotomicField(3).extension(x^3 - 2)
sage: timeit a^6
10000 loops, best of 3: 92.7 Âµs per loop
sage: K.<a> = NumberField(x^3-2*x^2+12)
sage: timeit a^4
10000 loops, best of 3: 30.6 Âµs per loop
sage: O.<a,b> = EquationOrder([x^2+1, x^2+2])
sage: timeit a*b
100000 loops, best of 3: 19 Âµs per loop
```



Issue created by migration from https://trac.sagemath.org/ticket/1141





---

archive/issue_comments_006936.json:
```json
{
    "body": "the patch!",
    "created_at": "2007-11-10T20:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1141#issuecomment-6936",
    "user": "jbmohler"
}
```

the patch!



---

archive/issue_comments_006937.json:
```json
{
    "body": "Attachment [nf_poly_pointer.hg](tarball://root/attachments/some-uuid/ticket1141/nf_poly_pointer.hg) by jbmohler created at 2007-11-10 20:55:35",
    "created_at": "2007-11-10T20:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1141#issuecomment-6937",
    "user": "jbmohler"
}
```

Attachment [nf_poly_pointer.hg](tarball://root/attachments/some-uuid/ticket1141/nf_poly_pointer.hg) by jbmohler created at 2007-11-10 20:55:35



---

archive/issue_comments_006938.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-11-10T20:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1141#issuecomment-6938",
    "user": "jbmohler"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_006939.json:
```json
{
    "body": "I applied the patch, verified the promised performance improvements, and checked that doctests in sage/rings/numberfield/* still pass.\n\nI do think that moving the number field parent class to cython may be a better strategy long-term, if only to avoid the extra memory footprint of two more pointers per number field element (although that's probably a silly thing to worry about, given how big number field elements are anyway).  But regardless, this patch should be applied for now.\n\nI approve.",
    "created_at": "2007-12-01T03:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1141#issuecomment-6939",
    "user": "cwitty"
}
```

I applied the patch, verified the promised performance improvements, and checked that doctests in sage/rings/numberfield/* still pass.

I do think that moving the number field parent class to cython may be a better strategy long-term, if only to avoid the extra memory footprint of two more pointers per number field element (although that's probably a silly thing to worry about, given how big number field elements are anyway).  But regardless, this patch should be applied for now.

I approve.



---

archive/issue_comments_006940.json:
```json
{
    "body": "Merged in 2.8.15.alpha0",
    "created_at": "2007-12-01T11:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1141#issuecomment-6940",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha0



---

archive/issue_comments_006941.json:
```json
{
    "body": "Merged in 2.8.15.alpha0",
    "created_at": "2007-12-01T11:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1141#issuecomment-6941",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha0



---

archive/issue_comments_006942.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T07:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1141#issuecomment-6942",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006943.json:
```json
{
    "body": "Merged in 2.8.15.alpha0 - 3rd time's the charm!",
    "created_at": "2007-12-02T07:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1141#issuecomment-6943",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha0 - 3rd time's the charm!
