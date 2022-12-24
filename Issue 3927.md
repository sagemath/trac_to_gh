# Issue 3927: Factorization class has no division implemented

archive/issues_003927.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: factorization\n\nThis works:\n\n```\nsage: factor(10)*factor(15)^(-1)             \n2 * 3^-1\n```\n\nand so does this:\n\n```\nsage: factor(10/15)        \n2 * 3^-1\n```\n\nbut not this:\n\n```\nsage: factor(10)/factor(15)     \n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/john/sage-3.1.test/spkg/build/python-2.5.2.p3/tmp/<ipython console> in <module>()\n\nTypeError: unsupported operand type(s) for /: 'Factorization' and 'Factorization'\n```\n\n\nSo: Factorizations can be multiplied and inverted but not divided, which is a bit silly.  I suggest adding a `__div___()` method.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3927\n\n",
    "created_at": "2008-08-22T12:33:08Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Factorization class has no division implemented",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3927",
    "user": "@JohnCremona"
}
```
Assignee: somebody

Keywords: factorization

This works:

```
sage: factor(10)*factor(15)^(-1)             
2 * 3^-1
```

and so does this:

```
sage: factor(10/15)        
2 * 3^-1
```

but not this:

```
sage: factor(10)/factor(15)     
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/john/sage-3.1.test/spkg/build/python-2.5.2.p3/tmp/<ipython console> in <module>()

TypeError: unsupported operand type(s) for /: 'Factorization' and 'Factorization'
```


So: Factorizations can be multiplied and inverted but not divided, which is a bit silly.  I suggest adding a `__div___()` method.

Issue created by migration from https://trac.sagemath.org/ticket/3927





---

archive/issue_comments_028108.json:
```json
{
    "body": "Attachment [sage-trac3927.patch](tarball://root/attachments/some-uuid/ticket3927/sage-trac3927.patch) by @JohnCremona created at 2008-08-22 15:26:51",
    "created_at": "2008-08-22T15:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3927#issuecomment-28108",
    "user": "@JohnCremona"
}
```

Attachment [sage-trac3927.patch](tarball://root/attachments/some-uuid/ticket3927/sage-trac3927.patch) by @JohnCremona created at 2008-08-22 15:26:51



---

archive/issue_comments_028109.json:
```json
{
    "body": "Attachment [sage-trac3927a.patch](tarball://root/attachments/some-uuid/ticket3927/sage-trac3927a.patch) by @JohnCremona created at 2008-08-22 15:34:09\n\nTwo patches:  the first implements division, the second implements gcd() and lcm() for Factorizations.  The first also fixes a small gap discovered while testing those, namely that for FreeAlgebras, the element 1 could not be inverted.  Now, in any ring, for an element a for which a.is_unit() is true, a.__invert__() returns self.  (For many rings, 1 is the only element for which .is_unit() does not return a NotImplementedError).\n\nTheses patches are essentially orthogonal to the other one #2460 concerning factorization.py.\nThey are based on 3.1.1.\n\n\nJohn",
    "created_at": "2008-08-22T15:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3927#issuecomment-28109",
    "user": "@JohnCremona"
}
```

Attachment [sage-trac3927a.patch](tarball://root/attachments/some-uuid/ticket3927/sage-trac3927a.patch) by @JohnCremona created at 2008-08-22 15:34:09

Two patches:  the first implements division, the second implements gcd() and lcm() for Factorizations.  The first also fixes a small gap discovered while testing those, namely that for FreeAlgebras, the element 1 could not be inverted.  Now, in any ring, for an element a for which a.is_unit() is true, a.__invert__() returns self.  (For many rings, 1 is the only element for which .is_unit() does not return a NotImplementedError).

Theses patches are essentially orthogonal to the other one #2460 concerning factorization.py.
They are based on 3.1.1.


John



---

archive/issue_comments_028110.json:
```json
{
    "body": "Attachment [sage-trac3927b.patch](tarball://root/attachments/some-uuid/ticket3927/sage-trac3927b.patch) by @JohnCremona created at 2008-08-23 16:06:34\n\nThe third patch deals with the issues left from trac #2460.  Each Factorization now has a universe (cached as attribute `self.__universe`) computed using the Sequence idea proposed in trac #2460.  The base_ring() function has been changed to universe() and returns the universe.  If no universe is found it just sets it to None (for example, this is the case for Factorizations of modular symbol spaces).\n\nI also added a new function is_integral and changed the docstrings to reflect the fact that the exponents needs not be positive (for example, factor(2/3) has always worked and returned a prime factorization with a negative exponent).\n\nSince Factorization is used in a lot of different places I did -testall before posting this, and dealt with a few minor things which arose (no-one minded base_ring() being renamed universe(), but in 2 or 3 places unit_part() was changed to unit()).\n\nAll three patches should be applied in order;  based on 3.1.1.\n\nI think the __add__ and __sub__ methods are totally pointless but have left them in for now.",
    "created_at": "2008-08-23T16:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3927#issuecomment-28110",
    "user": "@JohnCremona"
}
```

Attachment [sage-trac3927b.patch](tarball://root/attachments/some-uuid/ticket3927/sage-trac3927b.patch) by @JohnCremona created at 2008-08-23 16:06:34

The third patch deals with the issues left from trac #2460.  Each Factorization now has a universe (cached as attribute `self.__universe`) computed using the Sequence idea proposed in trac #2460.  The base_ring() function has been changed to universe() and returns the universe.  If no universe is found it just sets it to None (for example, this is the case for Factorizations of modular symbol spaces).

I also added a new function is_integral and changed the docstrings to reflect the fact that the exponents needs not be positive (for example, factor(2/3) has always worked and returned a prime factorization with a negative exponent).

Since Factorization is used in a lot of different places I did -testall before posting this, and dealt with a few minor things which arose (no-one minded base_ring() being renamed universe(), but in 2 or 3 places unit_part() was changed to unit()).

All three patches should be applied in order;  based on 3.1.1.

I think the __add__ and __sub__ methods are totally pointless but have left them in for now.



---

archive/issue_comments_028111.json:
```json
{
    "body": "I fixed a few issues with gcd and lcm, but everything else looks good.\n\nPositive review.  (Apply all four patches.)",
    "created_at": "2008-08-23T23:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3927#issuecomment-28111",
    "user": "cwitty"
}
```

I fixed a few issues with gcd and lcm, but everything else looks good.

Positive review.  (Apply all four patches.)



---

archive/issue_comments_028112.json:
```json
{
    "body": "Attachment [trac3927-fix-gcd-lcm.patch](tarball://root/attachments/some-uuid/ticket3927/trac3927-fix-gcd-lcm.patch) by cwitty created at 2008-08-23 23:31:32",
    "created_at": "2008-08-23T23:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3927#issuecomment-28112",
    "user": "cwitty"
}
```

Attachment [trac3927-fix-gcd-lcm.patch](tarball://root/attachments/some-uuid/ticket3927/trac3927-fix-gcd-lcm.patch) by cwitty created at 2008-08-23 23:31:32



---

archive/issue_comments_028113.json:
```json
{
    "body": "Last patch is fine -- thanks.",
    "created_at": "2008-08-24T08:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3927#issuecomment-28113",
    "user": "@JohnCremona"
}
```

Last patch is fine -- thanks.



---

archive/issue_comments_028114.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-25T02:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3927#issuecomment-28114",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028115.json:
```json
{
    "body": "Merged sage-trac3927.patch, sage-trac3927a.patch, sage-trac3927b.patch and trac3927-fix-gcd-lcm.patch in Sage 3.1.2.alpha1",
    "created_at": "2008-08-25T02:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3927#issuecomment-28115",
    "user": "mabshoff"
}
```

Merged sage-trac3927.patch, sage-trac3927a.patch, sage-trac3927b.patch and trac3927-fix-gcd-lcm.patch in Sage 3.1.2.alpha1
