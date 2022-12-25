# Issue 7797: basic interface to letterplace from singular

archive/issues_007797.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  polybori @saliola @malb @jhpalmieri sage-combinat oleksandrmotsak\n\nKeywords: singular\n\nAttached patches add a basic interface to the letterplace [1] component of Singular, which allows computation of Groebner bases (up to a degree bound) of (two-sided) ideals of free algebras.\n\n[1] http://www.singular.uni-kl.de/Manual/latest/sing_425.htm#SEC478\n\nThese patches depend on #7198.\n\nSince Sage only supports ideals over commutative rings for now, writing a better interface to this would take considerably more work. I suggest we review & merge these patches, and hook it up to the right place when it exists.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7797\n\n",
    "created_at": "2009-12-30T21:43:47Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.5",
    "title": "basic interface to letterplace from singular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7797",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

CC:  polybori @saliola @malb @jhpalmieri sage-combinat oleksandrmotsak

Keywords: singular

Attached patches add a basic interface to the letterplace [1] component of Singular, which allows computation of Groebner bases (up to a degree bound) of (two-sided) ideals of free algebras.

[1] http://www.singular.uni-kl.de/Manual/latest/sing_425.htm#SEC478

These patches depend on #7198.

Since Sage only supports ideals over commutative rings for now, writing a better interface to this would take considerably more work. I suggest we review & merge these patches, and hook it up to the right place when it exists.

Issue created by migration from https://trac.sagemath.org/ticket/7797





---

archive/issue_comments_067217.json:
```json
{
    "body": "hack to create an MPolynomialRing as a parent for letterplace polynomials",
    "created_at": "2009-12-30T21:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67217",
    "user": "https://github.com/burcin"
}
```

hack to create an MPolynomialRing as a parent for letterplace polynomials



---

archive/issue_comments_067218.json:
```json
{
    "body": "Attachment [trac_7797-letterplace_ring_hack.patch](tarball://root/attachments/some-uuid/ticket7797/trac_7797-letterplace_ring_hack.patch) by @burcin created at 2009-12-30 21:47:33\n\nbasic interface to compute groebner bases with letterplace",
    "created_at": "2009-12-30T21:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67218",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7797-letterplace_ring_hack.patch](tarball://root/attachments/some-uuid/ticket7797/trac_7797-letterplace_ring_hack.patch) by @burcin created at 2009-12-30 21:47:33

basic interface to compute groebner bases with letterplace



---

archive/issue_comments_067219.json:
```json
{
    "body": "Attachment [trac_7797-letterplace.patch](tarball://root/attachments/some-uuid/ticket7797/trac_7797-letterplace.patch) by @burcin created at 2009-12-30 21:47:50",
    "created_at": "2009-12-30T21:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67219",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7797-letterplace.patch](tarball://root/attachments/some-uuid/ticket7797/trac_7797-letterplace.patch) by @burcin created at 2009-12-30 21:47:50



---

archive/issue_comments_067220.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-30T21:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67220",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067221.json:
```json
{
    "body": "Doctest failure on sage.math:\n\n\n```\nFile \"/mnt/usb1/scratch/malb/sage-4.4/devel/sage-main/sage/libs/singular/letterplace.py\", line 32:\n    sage: freegb(l, 10)\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/malb/sage-4.4/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/malb/sage-4.4/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/malb/sage-4.4/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[5]>\", line 1, in <module>\n        freegb(l, Integer(10))###line 32:\n    sage: freegb(l, 10)\n      File \"/mnt/usb1/scratch/malb/sage-4.4/local/lib/python/site-packages/sage/libs/singular/letterplace.py\", line 70, in freegb\n        libsingular_options(bck)\n    TypeError: 'sage.libs.singular.option.LibSingularOptions' object is not callable\n```\n\n\nI think we used to allow calling libsingular option objects earlier, however load() replaces it.",
    "created_at": "2010-06-03T22:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67221",
    "user": "https://github.com/malb"
}
```

Doctest failure on sage.math:


```
File "/mnt/usb1/scratch/malb/sage-4.4/devel/sage-main/sage/libs/singular/letterplace.py", line 32:
    sage: freegb(l, 10)
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/malb/sage-4.4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/malb/sage-4.4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/malb/sage-4.4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[5]>", line 1, in <module>
        freegb(l, Integer(10))###line 32:
    sage: freegb(l, 10)
      File "/mnt/usb1/scratch/malb/sage-4.4/local/lib/python/site-packages/sage/libs/singular/letterplace.py", line 70, in freegb
        libsingular_options(bck)
    TypeError: 'sage.libs.singular.option.LibSingularOptions' object is not callable
```


I think we used to allow calling libsingular option objects earlier, however load() replaces it.



---

archive/issue_comments_067222.json:
```json
{
    "body": "Actually, this doesn't make sense to me:\n\n\n```python\nbck = int(libsingular_options)  \n#letter place needs these options\nlibsingular_options['redTail'] = True\nlibsingular_options['redSB'] = True\nlibsingular_options(bck)\n```\n\n\nFirst bck is stored and then options are changed. So far fine. However, then bck is loaded and thus overwrites the options just set.",
    "created_at": "2010-06-24T14:29:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67222",
    "user": "https://github.com/malb"
}
```

Actually, this doesn't make sense to me:


```python
bck = int(libsingular_options)  
#letter place needs these options
libsingular_options['redTail'] = True
libsingular_options['redSB'] = True
libsingular_options(bck)
```


First bck is stored and then options are changed. So far fine. However, then bck is loaded and thus overwrites the options just set.



---

archive/issue_comments_067223.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-24T14:29:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67223",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067224.json:
```json
{
    "body": "letter place singular interface",
    "created_at": "2010-06-30T09:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67224",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

letter place singular interface



---

archive/issue_comments_067225.json:
```json
{
    "body": "Attachment [trac_7797-letterplace.2.patch](tarball://root/attachments/some-uuid/ticket7797/trac_7797-letterplace.2.patch) by PolyBoRi created at 2010-06-30 09:07:40\n\nHi!\n\nI have corrected that using the new context interface.\n\nCheers,\nMichael",
    "created_at": "2010-06-30T09:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67225",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Attachment [trac_7797-letterplace.2.patch](tarball://root/attachments/some-uuid/ticket7797/trac_7797-letterplace.2.patch) by PolyBoRi created at 2010-06-30 09:07:40

Hi!

I have corrected that using the new context interface.

Cheers,
Michael



---

archive/issue_comments_067226.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-30T09:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67226",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067227.json:
```json
{
    "body": "Attachment [trac_7797-letterplace.3.patch](tarball://root/attachments/some-uuid/ticket7797/trac_7797-letterplace.3.patch) by PolyBoRi created at 2010-06-30 09:10:23",
    "created_at": "2010-06-30T09:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67227",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Attachment [trac_7797-letterplace.3.patch](tarball://root/attachments/some-uuid/ticket7797/trac_7797-letterplace.3.patch) by PolyBoRi created at 2010-06-30 09:10:23



---

archive/issue_comments_067228.json:
```json
{
    "body": "* While there are doctests, there is no documentation, no explanation what the functions are doing\n  * freegb should accept ideals (?)\n  * Why are you calling \"singular_system\"?",
    "created_at": "2010-07-14T22:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67228",
    "user": "https://github.com/malb"
}
```

* While there are doctests, there is no documentation, no explanation what the functions are doing
  * freegb should accept ideals (?)
  * Why are you calling "singular_system"?



---

archive/issue_comments_067229.json:
```json
{
    "body": "\n```\nFile \"/mnt/usb1/scratch/malb/sage-4.4/devel/sage-main/sage/libs/singular/letterplace.py\", line 32:\n\nsage: freegb(l, 10)\n\nExpected:\n\n[3*y*x*z^7*y + y*x*z^8, 3*y*x*z^6*y + y*x*z^7, y*x*z^6*x*z + 314928*y^2*x*z^2*x^5, 3*y*x*z^5*y + y*x*z^6, y*x*z^5*x*z - 17496*y^2*x*z^2*x^4, 3*y*x*z^4*y + y*x*z^5, y*x*z^4*x*z + 972*y^2*x*z^2*x^3, 3*y*x*z^4*x^2*z*y + y*x*z^4*x^2*z^2, 3*y*x*z^3*y + y*x*z^4, y*x*z^3*x*z - 54*y^2*x*z^2*x^2, 3*y*x*z^3*x^2*z^2*y + y*x*z^3*x^2*z^3, 3*y*x*z^3*x^2*z*y + y*x*z^3*x^2*z^2, 3*y*x*z^3*x^3*z*y + y*x*z^3*x^3*z^2, 3*y*x*z^2*y + y*x*z^3, y*x*z^2*x*z + 3*y^2*x*z^2*x, 3*y*x*z^2*x^2*z^3*y + y*x*z^2*x^2*z^4, 3*y*x*z^2*x^2*z^2*y + y*x*z^2*x^2*z^3, y*x*z^2*x^2*z^2*x*z + 3*y^2*x*z^2*x^2*z^2*x, 3*y*x*z^2*x^2*z*y + y*x*z^2*x^2*z^2, 3*y*x*z^2*x^3*z^2*y + y*x*z^2*x^3*z^3, 3*y*x*z^2*x^3*z*y + y*x*z^2*x^3*z^2, 3*y*x*z^2*x^4*z*y + y*x*z^2*x^4*z^2, 3*y*x*z*y + y*x*z^2, x*z*y^6*x*z - 7776*y*x*z^2*x^6, x*z*y^5*x*z - 1296*y*x*z^2*x^5, x*z*y^4*x*z - 216*y*x*z^2*x^4, x*z*y^3*x*z - 36*y*x*z^2*x^3, x*z*y^2*x*z - 6*y*x*z^2*x^2, x*z*y*x*z - y*x*z^2*x, 6*x*z*x - y*x*z, 3*x*y + x*z]\n\nGot\n[3*x*y + x*z, 6*x*z*x - y*x*z, 3*y*x*z*y + y*x*z^2, 3*y*x*z^2*y + y*x*z^3, x*z*y*x*z - y*x*z^2*x, 3*y*x*z^3*y + y*x*z^4, y*x*z^2*x*z + 3*y^2*x*z^2*x, x*z*y^2*x*z - 6*y*x*z^2*x^2, 3*y*x*z^4*y + y*x*z^5, y*x*z^3*x*z - 54*y^2*x*z^2*x^2, x*z*y^3*x*z - 36*y*x*z^2*x^3, 3*y*x*z^5*y + y*x*z^6, y*x*z^4*x*z + 972*y^2*x*z^2*x^3, 3*y*x*z^2*x^2*z*y + y*x*z^2*x^2*z^2, x*z*y^4*x*z - 216*y*x*z^2*x^4, 3*y*x*z^6*y + y*x*z^7, y*x*z^5*x*z - 17496*y^2*x*z^2*x^4, 3*y*x*z^3*x^2*z*y + y*x*z^3*x^2*z^2, 3*y*x*z^2*x^2*z^2*y + y*x*z^2*x^2*z^3, 3*y*x*z^2*x^3*z*y + y*x*z^2*x^3*z^2, x*z*y^5*x*z - 1296*y*x*z^2*x^5, 3*y*x*z^7*y + y*x*z^8, y*x*z^6*x*z + 314928*y^2*x*z^2*x^5, 3*y*x*z^4*x^2*z*y + y*x*z^4*x^2*z^2, 3*y*x*z^3*x^2*z^2*y + y*x*z^3*x^2*z^3, 3*y*x*z^3*x^3*z*y + y*x*z^3*x^3*z^2, 3*y*x*z^2*x^2*z^3*y + y*x*z^2*x^2*z^4, y*x*z^2*x^2*z^2*x*z + 3*y^2*x*z^2*x^2*z^2*x, 3*y*x*z^2*x^3*z^2*y + y*x*z^2*x^3*z^3, 3*y*x*z^2*x^4*z*y + y*x*z^2*x^4*z^2, x*z*y^6*x*z - 7776*y*x*z^2*x^6]\n```\n\nThis is with Singular 3-1-1-3 though.",
    "created_at": "2010-07-14T22:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67229",
    "user": "https://github.com/malb"
}
```


```
File "/mnt/usb1/scratch/malb/sage-4.4/devel/sage-main/sage/libs/singular/letterplace.py", line 32:

sage: freegb(l, 10)

Expected:

[3*y*x*z^7*y + y*x*z^8, 3*y*x*z^6*y + y*x*z^7, y*x*z^6*x*z + 314928*y^2*x*z^2*x^5, 3*y*x*z^5*y + y*x*z^6, y*x*z^5*x*z - 17496*y^2*x*z^2*x^4, 3*y*x*z^4*y + y*x*z^5, y*x*z^4*x*z + 972*y^2*x*z^2*x^3, 3*y*x*z^4*x^2*z*y + y*x*z^4*x^2*z^2, 3*y*x*z^3*y + y*x*z^4, y*x*z^3*x*z - 54*y^2*x*z^2*x^2, 3*y*x*z^3*x^2*z^2*y + y*x*z^3*x^2*z^3, 3*y*x*z^3*x^2*z*y + y*x*z^3*x^2*z^2, 3*y*x*z^3*x^3*z*y + y*x*z^3*x^3*z^2, 3*y*x*z^2*y + y*x*z^3, y*x*z^2*x*z + 3*y^2*x*z^2*x, 3*y*x*z^2*x^2*z^3*y + y*x*z^2*x^2*z^4, 3*y*x*z^2*x^2*z^2*y + y*x*z^2*x^2*z^3, y*x*z^2*x^2*z^2*x*z + 3*y^2*x*z^2*x^2*z^2*x, 3*y*x*z^2*x^2*z*y + y*x*z^2*x^2*z^2, 3*y*x*z^2*x^3*z^2*y + y*x*z^2*x^3*z^3, 3*y*x*z^2*x^3*z*y + y*x*z^2*x^3*z^2, 3*y*x*z^2*x^4*z*y + y*x*z^2*x^4*z^2, 3*y*x*z*y + y*x*z^2, x*z*y^6*x*z - 7776*y*x*z^2*x^6, x*z*y^5*x*z - 1296*y*x*z^2*x^5, x*z*y^4*x*z - 216*y*x*z^2*x^4, x*z*y^3*x*z - 36*y*x*z^2*x^3, x*z*y^2*x*z - 6*y*x*z^2*x^2, x*z*y*x*z - y*x*z^2*x, 6*x*z*x - y*x*z, 3*x*y + x*z]

Got
[3*x*y + x*z, 6*x*z*x - y*x*z, 3*y*x*z*y + y*x*z^2, 3*y*x*z^2*y + y*x*z^3, x*z*y*x*z - y*x*z^2*x, 3*y*x*z^3*y + y*x*z^4, y*x*z^2*x*z + 3*y^2*x*z^2*x, x*z*y^2*x*z - 6*y*x*z^2*x^2, 3*y*x*z^4*y + y*x*z^5, y*x*z^3*x*z - 54*y^2*x*z^2*x^2, x*z*y^3*x*z - 36*y*x*z^2*x^3, 3*y*x*z^5*y + y*x*z^6, y*x*z^4*x*z + 972*y^2*x*z^2*x^3, 3*y*x*z^2*x^2*z*y + y*x*z^2*x^2*z^2, x*z*y^4*x*z - 216*y*x*z^2*x^4, 3*y*x*z^6*y + y*x*z^7, y*x*z^5*x*z - 17496*y^2*x*z^2*x^4, 3*y*x*z^3*x^2*z*y + y*x*z^3*x^2*z^2, 3*y*x*z^2*x^2*z^2*y + y*x*z^2*x^2*z^3, 3*y*x*z^2*x^3*z*y + y*x*z^2*x^3*z^2, x*z*y^5*x*z - 1296*y*x*z^2*x^5, 3*y*x*z^7*y + y*x*z^8, y*x*z^6*x*z + 314928*y^2*x*z^2*x^5, 3*y*x*z^4*x^2*z*y + y*x*z^4*x^2*z^2, 3*y*x*z^3*x^2*z^2*y + y*x*z^3*x^2*z^3, 3*y*x*z^3*x^3*z*y + y*x*z^3*x^3*z^2, 3*y*x*z^2*x^2*z^3*y + y*x*z^2*x^2*z^4, y*x*z^2*x^2*z^2*x*z + 3*y^2*x*z^2*x^2*z^2*x, 3*y*x*z^2*x^3*z^2*y + y*x*z^2*x^3*z^3, 3*y*x*z^2*x^4*z*y + y*x*z^2*x^4*z^2, x*z*y^6*x*z - 7776*y*x*z^2*x^6]
```

This is with Singular 3-1-1-3 though.



---

archive/issue_comments_067230.json:
```json
{
    "body": "Aufruf von System ist offiziell, hei\u00dft aber nur, dass es nicht als extra Kommando eingebaut ist.\n\nhttp://www.singular.uni-kl.de/Manual/latest/sing_433.htm",
    "created_at": "2010-07-15T08:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67230",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Aufruf von System ist offiziell, heißt aber nur, dass es nicht als extra Kommando eingebaut ist.

http://www.singular.uni-kl.de/Manual/latest/sing_433.htm



---

archive/issue_comments_067231.json:
```json
{
    "body": "sorry, for the language:\ncalling system is official. Using singular system was easier for the authors of freegb.\n\nhttp://www.singular.uni-kl.de/Manual/latest/sing_433.htm",
    "created_at": "2010-07-15T08:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67231",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

sorry, for the language:
calling system is official. Using singular system was easier for the authors of freegb.

http://www.singular.uni-kl.de/Manual/latest/sing_433.htm



---

archive/issue_comments_067232.json:
```json
{
    "body": "the result seem to differ just in order.\n\nWhat Ideal class is used for free algebras?",
    "created_at": "2010-07-15T08:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67232",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

the result seem to differ just in order.

What Ideal class is used for free algebras?



---

archive/issue_comments_067233.json:
```json
{
    "body": "Attachment [plural_functions.patch](tarball://root/attachments/some-uuid/ticket7797/plural_functions.patch) by PolyBoRi created at 2010-07-15 13:21:24\n\nsome improvements to plural interface, still not much working",
    "created_at": "2010-07-15T13:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67233",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Attachment [plural_functions.patch](tarball://root/attachments/some-uuid/ticket7797/plural_functions.patch) by PolyBoRi created at 2010-07-15 13:21:24

some improvements to plural interface, still not much working



---

archive/issue_comments_067234.json:
```json
{
    "body": "Replying to [comment:11 PolyBoRi]:\n\n> the result seem to differ just in order. What Ideal class is used for free algebras?\n\nApparently, we don't have one which works yet\n\n\n```\nsage: P.<a,b,c> = FreeAlgebra(QQ,3)\nsage: P\nFree Algebra on 3 generators (a, b, c) over Rational Field\nsage: P.ideal([a*b+c,a+1])\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/malb/<ipython console> in <module>()\n\n/usr/local/sage-4.3/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.ideal (sage/rings/ring.c:3426)()\n\n/usr/local/sage-4.3/local/lib/python2.6/site-packages/sage/rings/ideal.pyc in Ideal(*args, **kwds)\n    187 \n    188     if not commutative_ring.is_CommutativeRing(R):\n--> 189         raise TypeError, \"R must be a commutative ring\"\n    190 \n    191     if len(gens) == 0:\n\nTypeError: R must be a commutative ring\n```\n",
    "created_at": "2010-07-15T15:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67234",
    "user": "https://github.com/malb"
}
```

Replying to [comment:11 PolyBoRi]:

> the result seem to differ just in order. What Ideal class is used for free algebras?

Apparently, we don't have one which works yet


```
sage: P.<a,b,c> = FreeAlgebra(QQ,3)
sage: P
Free Algebra on 3 generators (a, b, c) over Rational Field
sage: P.ideal([a*b+c,a+1])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/malb/<ipython console> in <module>()

/usr/local/sage-4.3/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.ideal (sage/rings/ring.c:3426)()

/usr/local/sage-4.3/local/lib/python2.6/site-packages/sage/rings/ideal.pyc in Ideal(*args, **kwds)
    187 
    188     if not commutative_ring.is_CommutativeRing(R):
--> 189         raise TypeError, "R must be a commutative ring"
    190 
    191     if len(gens) == 0:

TypeError: R must be a commutative ring
```




---

archive/issue_comments_067235.json:
```json
{
    "body": "Do I understand correctly that in this ticket it is *not* attempted to replace `FreeAlgebra` by a more efficient implementation based on Singular's Letterplace Algebra? This ticket is only about wrapping free Groebner bases, but not about wrapping the basic arithmetic?\n\nWhat Sage currently does in free algebras is generic and slow. As pointed out on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/ad16f4fbe4ab66f), bot Singular and Gap are faster in basic arithmetic than the current implementation in Sage.\n\nBut this should be on a different ticket, right?\n\nBest regards,\nSimon",
    "created_at": "2010-10-01T19:17:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67235",
    "user": "https://github.com/simon-king-jena"
}
```

Do I understand correctly that in this ticket it is *not* attempted to replace `FreeAlgebra` by a more efficient implementation based on Singular's Letterplace Algebra? This ticket is only about wrapping free Groebner bases, but not about wrapping the basic arithmetic?

What Sage currently does in free algebras is generic and slow. As pointed out on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/ad16f4fbe4ab66f), bot Singular and Gap are faster in basic arithmetic than the current implementation in Sage.

But this should be on a different ticket, right?

Best regards,
Simon



---

archive/issue_comments_067236.json:
```json
{
    "body": "As I understand, this makes the Singular's letterplace functionality accessible to Sage (in addition to the Plural functionality of #4539).",
    "created_at": "2010-10-01T20:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67236",
    "user": "https://github.com/alexanderdreyer"
}
```

As I understand, this makes the Singular's letterplace functionality accessible to Sage (in addition to the Plural functionality of #4539).



---

archive/issue_comments_067237.json:
```json
{
    "body": "This ticket is only about exposing the Groebner basis computation. We didn't think arithmetic was usable since\n\n* there is a degree bound, and\n* it is a hack in Singular.\n\nIf you think the arithmetic should be wrapped as well, that should be on a different ticket. I don't know how much the Plural wrapper (#4539) will help with that.",
    "created_at": "2010-10-01T20:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67237",
    "user": "https://github.com/burcin"
}
```

This ticket is only about exposing the Groebner basis computation. We didn't think arithmetic was usable since

* there is a degree bound, and
* it is a hack in Singular.

If you think the arithmetic should be wrapped as well, that should be on a different ticket. I don't know how much the Plural wrapper (#4539) will help with that.



---

archive/issue_comments_067238.json:
```json
{
    "body": "Replying to [comment:14 AlexanderDreyer]:\n> As I understand, this makes the Singular's letterplace functionality accessible to Sage (in addition to the Plural functionality of #4539).\n\nWhat is meant by \"Letterplace functionality\"? Is it \"simply\" computing Gr\u00f6bner basis with degree bound in free associative algebras?\n\nSomething that irritates me (and I already asked in the Singular forum) is that I could not find a way to *apply* such Groebner basis, e.g., in order to compute a normal form of an element of the free associative algebra w.r.t. this Gr\u00f6bner basis. Also I tend to call *basic arithmetic* a funtionality.\n\nReplying to [comment:15 burcin]:\n> This ticket is only about exposing the Groebner basis computation. We didn't think arithmetic was usable since\n> \n>  * there is a degree bound, and\n>  * it is a hack in Singular.\n> \n> If you think the arithmetic should be wrapped as well, that should be on a different ticket. I don't know how much the Plural wrapper (#4539) will help with that.\n\nOK. *If* I find the time, I'll finish the wrappers that I hacked together yesterday. The new ticket will then provide two alternative implementations of free (associative) algebras. One will be based on Gap, the other on Letterplace. The latter will be a hack as well: While doing arithmetic, the degree bound will be dynamically adapted. Currently I use Expect interfaces, but I guess using the Plural wrapper will improve things further.\n\nCheers,\nSimon",
    "created_at": "2010-10-02T07:41:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67238",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:14 AlexanderDreyer]:
> As I understand, this makes the Singular's letterplace functionality accessible to Sage (in addition to the Plural functionality of #4539).

What is meant by "Letterplace functionality"? Is it "simply" computing Gröbner basis with degree bound in free associative algebras?

Something that irritates me (and I already asked in the Singular forum) is that I could not find a way to *apply* such Groebner basis, e.g., in order to compute a normal form of an element of the free associative algebra w.r.t. this Gröbner basis. Also I tend to call *basic arithmetic* a funtionality.

Replying to [comment:15 burcin]:
> This ticket is only about exposing the Groebner basis computation. We didn't think arithmetic was usable since
> 
>  * there is a degree bound, and
>  * it is a hack in Singular.
> 
> If you think the arithmetic should be wrapped as well, that should be on a different ticket. I don't know how much the Plural wrapper (#4539) will help with that.

OK. *If* I find the time, I'll finish the wrappers that I hacked together yesterday. The new ticket will then provide two alternative implementations of free (associative) algebras. One will be based on Gap, the other on Letterplace. The latter will be a hack as well: While doing arithmetic, the degree bound will be dynamically adapted. Currently I use Expect interfaces, but I guess using the Plural wrapper will improve things further.

Cheers,
Simon



---

archive/issue_comments_067239.json:
```json
{
    "body": "I tried to apply the patches - apparently it is\n\nApply trac_7797-letterplace_ring_hack.patch trac_7797-letterplace.3.patch plural_functions.patch\n\nCorrect?\n\nUnfortunately, plural_functions.patch fails. Can you rebase it, please?",
    "created_at": "2011-03-17T14:32:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67239",
    "user": "https://github.com/simon-king-jena"
}
```

I tried to apply the patches - apparently it is

Apply trac_7797-letterplace_ring_hack.patch trac_7797-letterplace.3.patch plural_functions.patch

Correct?

Unfortunately, plural_functions.patch fails. Can you rebase it, please?



---

archive/issue_comments_067240.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-17T14:32:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67240",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067241.json:
```json
{
    "body": "In addition, one doc test has a different result:\n\n\n```\nsage: from sage.libs.singular.letterplace import freegb \nsage: F.<x,y,z> = FreeAlgebra(QQ, 3); F \nFree Algebra on 3 generators (x, y, z) over Rational Field\nsage: l=[2*x*z*x+y*x*y, 3*x*y+x*z] \nsage: freegb(l, 10) \n[3*x*y + x*z, 6*x*z*x - y*x*z, 3*y*x*z*y + y*x*z^2, 3*y*x*z^2*y + y*x*z^3, x*z*y*x*z - y*x*z^2*x, 3*y*x*z^3*y + y*x*z^4, y*x*z^2*x*z + 3*y^2*x*z^2*x, x*z*y^2*x*z - 6*y*x*z^2*x^2, 3*y*x*z^4*y + y*x*z^5, y*x*z^3*x*z - 54*y^2*x*z^2*x^2, x*z*y^3*x*z - 36*y*x*z^2*x^3, 3*y*x*z^5*y + y*x*z^6, y*x*z^4*x*z + 972*y^2*x*z^2*x^3, 3*y*x*z^2*x^2*z*y + y*x*z^2*x^2*z^2, x*z*y^4*x*z - 216*y*x*z^2*x^4, 3*y*x*z^6*y + y*x*z^7, y*x*z^5*x*z - 17496*y^2*x*z^2*x^4, 3*y*x*z^3*x^2*z*y + y*x*z^3*x^2*z^2, 3*y*x*z^2*x^2*z^2*y + y*x*z^2*x^2*z^3, 3*y*x*z^2*x^3*z*y + y*x*z^2*x^3*z^2, x*z*y^5*x*z - 1296*y*x*z^2*x^5, 3*y*x*z^7*y + y*x*z^8, y*x*z^6*x*z + 314928*y^2*x*z^2*x^5, 3*y*x*z^4*x^2*z*y + y*x*z^4*x^2*z^2, 3*y*x*z^3*x^2*z^2*y + y*x*z^3*x^2*z^3, 3*y*x*z^3*x^3*z*y + y*x*z^3*x^3*z^2, 3*y*x*z^2*x^2*z^3*y + y*x*z^2*x^2*z^4, y*x*z^2*x^2*z^2*x*z + 3*y^2*x*z^2*x^2*z^2*x, 3*y*x*z^2*x^3*z^2*y + y*x*z^2*x^3*z^3, 3*y*x*z^2*x^4*z*y + y*x*z^2*x^4*z^2, x*z*y^6*x*z - 7776*y*x*z^2*x^6]\n```\n\n\nWhich one is correct?",
    "created_at": "2011-03-17T14:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67241",
    "user": "https://github.com/simon-king-jena"
}
```

In addition, one doc test has a different result:


```
sage: from sage.libs.singular.letterplace import freegb 
sage: F.<x,y,z> = FreeAlgebra(QQ, 3); F 
Free Algebra on 3 generators (x, y, z) over Rational Field
sage: l=[2*x*z*x+y*x*y, 3*x*y+x*z] 
sage: freegb(l, 10) 
[3*x*y + x*z, 6*x*z*x - y*x*z, 3*y*x*z*y + y*x*z^2, 3*y*x*z^2*y + y*x*z^3, x*z*y*x*z - y*x*z^2*x, 3*y*x*z^3*y + y*x*z^4, y*x*z^2*x*z + 3*y^2*x*z^2*x, x*z*y^2*x*z - 6*y*x*z^2*x^2, 3*y*x*z^4*y + y*x*z^5, y*x*z^3*x*z - 54*y^2*x*z^2*x^2, x*z*y^3*x*z - 36*y*x*z^2*x^3, 3*y*x*z^5*y + y*x*z^6, y*x*z^4*x*z + 972*y^2*x*z^2*x^3, 3*y*x*z^2*x^2*z*y + y*x*z^2*x^2*z^2, x*z*y^4*x*z - 216*y*x*z^2*x^4, 3*y*x*z^6*y + y*x*z^7, y*x*z^5*x*z - 17496*y^2*x*z^2*x^4, 3*y*x*z^3*x^2*z*y + y*x*z^3*x^2*z^2, 3*y*x*z^2*x^2*z^2*y + y*x*z^2*x^2*z^3, 3*y*x*z^2*x^3*z*y + y*x*z^2*x^3*z^2, x*z*y^5*x*z - 1296*y*x*z^2*x^5, 3*y*x*z^7*y + y*x*z^8, y*x*z^6*x*z + 314928*y^2*x*z^2*x^5, 3*y*x*z^4*x^2*z*y + y*x*z^4*x^2*z^2, 3*y*x*z^3*x^2*z^2*y + y*x*z^3*x^2*z^3, 3*y*x*z^3*x^3*z*y + y*x*z^3*x^3*z^2, 3*y*x*z^2*x^2*z^3*y + y*x*z^2*x^2*z^4, y*x*z^2*x^2*z^2*x*z + 3*y^2*x*z^2*x^2*z^2*x, 3*y*x*z^2*x^3*z^2*y + y*x*z^2*x^3*z^3, 3*y*x*z^2*x^4*z*y + y*x*z^2*x^4*z^2, x*z*y^6*x*z - 7776*y*x*z^2*x^6]
```


Which one is correct?



---

archive/issue_comments_067242.json:
```json
{
    "body": "FYI: As I mentioned in an earlier post, just having a two-sided Gr\u00f6bner basis is not enough for my envisioned applications. I also need a competitive arithmetic for free associative algebras, normal form computation, and, if possible, ideals in non-commutative rings, and ring quotients.\n\nSo, I implemented something from scratch, *not* based on the previous patches. I already got an implementation of free associative algebras based on letterplace (with a dynamic degree bound). For example, computing `(x+y)**20` is 84 times faster than with the old implementation of free algebras.\n\nI also have a base class for left, right and twosided ideals: If R is any ring and L a list of elements, then R*L is a left ideal, L*R a right ideal, and R*L*R a twosided ideal.\n\nUsing freegb for the computation of a two-sided Gr\u00f6bner basis will be straight forward. In addition, Grischa Studzinski and Viktor Levandoskyy provided me with some code for computing normal forms in free algebras, that is supposed to be in a future Singular release. My plan is to back-port it.\n\nAnd then there's documentation to write...",
    "created_at": "2011-03-19T08:19:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67242",
    "user": "https://github.com/simon-king-jena"
}
```

FYI: As I mentioned in an earlier post, just having a two-sided Gröbner basis is not enough for my envisioned applications. I also need a competitive arithmetic for free associative algebras, normal form computation, and, if possible, ideals in non-commutative rings, and ring quotients.

So, I implemented something from scratch, *not* based on the previous patches. I already got an implementation of free associative algebras based on letterplace (with a dynamic degree bound). For example, computing `(x+y)**20` is 84 times faster than with the old implementation of free algebras.

I also have a base class for left, right and twosided ideals: If R is any ring and L a list of elements, then R*L is a left ideal, L*R a right ideal, and R*L*R a twosided ideal.

Using freegb for the computation of a two-sided Gröbner basis will be straight forward. In addition, Grischa Studzinski and Viktor Levandoskyy provided me with some code for computing normal forms in free algebras, that is supposed to be in a future Singular release. My plan is to back-port it.

And then there's documentation to write...



---

archive/issue_comments_067243.json:
```json
{
    "body": "I have attached a new patch that replaces all previous patches and provides a lot more functionality.\n\nSince I learned much from the previous patches, I hesitate to remove Michael and Burcin from the author list. But perhaps you like to be referee? Then you should move your name into the reviewer field.\n\n**__Technical Remarks__**\n\n`singular_function` is very useful! However, it was impossible to simply call the `freegb.lib` library functions of Singular, since they rely on ring attributes -- but ring attributes have not been wrapped in `libSingular`.\n\nMoreover, it is not a good idea to call the `makeLetterplaceRing` function from Singular and then transform the resulting `RingWrap` into a polynomial ring. It *is* possible -- but the result can not be pickled, since its variable names look like `x(1),y(1),x(2),y(2)` and are thus no valid identifiers.\n\nBut it is no problem to create another ring with more sober variable names, and apply the letterplace functions to it. One just needs to work around the attribute tests that these functions do. In fact, these functions do only one thing after the checking, namely a system call. So, I simply did this system calls as well.\n\nIn the current release, Singular does provide the Gr\u00f6bner basis computations in free algebras, but it does *not* provide normal form computations. Grischa Studzinski has send me some code that is supposed to become part of `freegb.lib` -- again, I can not call it directly, but it was fairly straight forward to implement along the lines of Grischa's code.\n\n**__New Features__**\n\n*__Free Algebra constructor as `UniqueFactory`__*\n\nUp to now, the `FreeAlgebra` constructor was based on an incomplete way of caching: When you pickle and unpickle a free algebra, you would not get the same object.\n\n```\n# old behaviour\nsage: F.<a,b,c> = FreeAlgebra(QQ,3)\nsage: loads(dumps(F)) is F\nFalse\n```\n\n\nThis is now resolved. Moreover, it is not needed to explicitly provide the number of generators, when it is obvious from the list of names:\n\n```\nsage: F.<x,y,z> = FreeAlgebra(QQ)\nsage: loads(dumps(F)) is F\nTrue\n```\n\n\nI did one change that may be subject to criticism, and I wouldn't oppose to revert it. A free algebra in one generator is a polynomial ring. So, I return a polynomial ring:\n\n```\nsage: FreeAlgebra(QQ,'x')\nUnivariate Polynomial Ring in x over Rational Field\n```\n\n\nThe constructor can now also be asked for a different implementation, as in all examples below.\n\n*__Free Algebra via Letterplace__*\n\nI provide a new implementation of free algebras. It can be constructed as follows:\n\n```\nsage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')\nsage: F\nFree Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field\n```\n\n\nDue to some shortcomings of Singular's letterplace implementation, unfortunately we need to restrict to homogeneous elements:\n\n```\nsage: (x+2*y)^2\nx*x + 2*x*y + 2*y*x + 4*y*y\nsage: x+0\nx\nTraceback (most recent call last):\n...\nArithmeticError: Can only add elements of the same degree\n```\n\nThis is why the new implementation can not yet become the default.\n\nHowever, the arithmetic in the new implementation is much faster than the old:\n\n```\nsage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')\nsage: F_old.<a,b,c> = FreeAlgebra(QQ)\nsage: timeit('t=(x+y)^15')\n5 loops, best of 3: 27.7 ms per loop\nsage: timeit('t=(a+b)^15')\nsage: %time t=(a+b)^15\nCPU times: user 4.51 s, sys: 0.09 s, total: 4.60 s\nWall time: 6.46 s\nsage: 4510/27.7\n162.815884476534\nsage: timeit('t=(x+y)^15')\n25 loops, best of 3: 19.7 ms per loop\nsage: %time t=(a+b)^15\nCPU times: user 2.70 s, sys: 0.02 s, total: 2.72 s\nWall time: 2.73 s\nsage: 2700/19.7\n137.055837563452\n```\n\n\n*__One- and Twosided Ideals of Noncommutative Rings__*\n\nI implemented it in a fairly general way, ideals can be created for any ring:\n\n```\nsage: A = SteenrodAlgebra(2)\nsage: IL = A*[A.1+A.2,A.1^2]; IL\nLeft Ideal (Sq(2) + Sq(4), Sq(1,1)) of mod 2 Steenrod algebra\nsage: IR = [A.1+A.2,A.1^2]*A; IR\nRight Ideal (Sq(2) + Sq(4), Sq(1,1)) of mod 2 Steenrod algebra\nsage: IT = A*[A.1+A.2,A.1^2]*A; IT\nTwosided Ideal (Sq(2) + Sq(4), Sq(1,1)) of mod 2 Steenrod algebra\n```\n\n\nNote some nastyness: The parent of an ideal still is the \"monoid of ideals of a ring\". But we actually have no multiplication in the non-commutative setting:\n\n```\nsage: IL*IR\nTraceback (most recent call last):\n...\nNotImplementedError: Can not multiply non-commutative ideals.\n```\n\n\nOf course, in general, we have no way to solve the ideal containment problem. But in free algebras, we have letterplace:\n\n```\nsage: I.groebner_basis(degbound=3)\nTwosided Ideal (y*y*y - y*y*z + y*z*y - y*z*z, y*y*x + y*y*z + y*z*x + y*z*z, x*y + y*z, x*x - y*x - y*y - y*z) of Free Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field\nsage: (x*y*z*y*x).normal_form(I)\ny*z*z*y*z + y*z*z*z*x + y*z*z*z*z\nsage: x*y*z*y*x - (x*y*z*y*x).normal_form(I) in I\nTrue\nsage: x*I.0-I.1*y+I.0*y in I\nTrue\nsage: 1 in I\nFalse\n```\n\n\n*__Quotient Rings__*\n\nPreviously, quotient rings have only been available for rings that inherit from the base class of commutative rings. My patch makes them available for all rings, and actually it should work to some extent even for objects that belong to the category `Rings()` but do not inherit from `sage.rings.ring.Ring`.\n\nThe requirement is that we mod by an ideal `I` that is *twosided* and that has a method `I.reduce(x)` that returns a normal form of an element `x` with respect to `I`. That requirement holds for ideals of polynomial rings, and also for homogeneous ideals of free associative algebras. In particular:\n\n```\nsage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')\nsage: I = F*[x*y+y*z,x^2+x*y-y*x-y^2]*F\nsage: Q.<a,b,c> = F.quo(I); Q\nQuotient of Free Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field by the ideal (x*y + y*z, x*x + x*y - y*x - y*y)\nsage: a*b\n-b*c\nsage: a^3\n-b*c*a - b*c*b - b*c*c\nsage: J = Q*[a^3-b^3]*Q\nsage: R.<i,j,k> = Q.quo(J); R\nQuotient of Free Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field by the ideal (-y*y*z - y*z*x - 2*y*z*z, x*y + y*z, x*x + x*y - y*x - y*y)\nsage: i^3\n-j*k*i - j*k*j - j*k*k\nsage: j^3\n-j*k*i - j*k*j - j*k*k\n```\n\n\nOne can also test if the quotient is commutative:\n\n```\nsage: Q.is_commutative()\nFalse\nsage: J = F*[x*y-y*x,x*z-z*x,y*z-z*y,x^3-y^3]*F\nsage: R = F.quo(J)\nsage: R.is_commutative()\nTrue\n```\n\n\n**__Miscellaneous__**\n\nI inserted the documentation of the new modules into the reference manual - I think it looks nice, but I guess a referee should double check.\n\nDoc tests pass for me. Thus: Ready for review!!",
    "created_at": "2011-03-24T16:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67243",
    "user": "https://github.com/simon-king-jena"
}
```

I have attached a new patch that replaces all previous patches and provides a lot more functionality.

Since I learned much from the previous patches, I hesitate to remove Michael and Burcin from the author list. But perhaps you like to be referee? Then you should move your name into the reviewer field.

**__Technical Remarks__**

`singular_function` is very useful! However, it was impossible to simply call the `freegb.lib` library functions of Singular, since they rely on ring attributes -- but ring attributes have not been wrapped in `libSingular`.

Moreover, it is not a good idea to call the `makeLetterplaceRing` function from Singular and then transform the resulting `RingWrap` into a polynomial ring. It *is* possible -- but the result can not be pickled, since its variable names look like `x(1),y(1),x(2),y(2)` and are thus no valid identifiers.

But it is no problem to create another ring with more sober variable names, and apply the letterplace functions to it. One just needs to work around the attribute tests that these functions do. In fact, these functions do only one thing after the checking, namely a system call. So, I simply did this system calls as well.

In the current release, Singular does provide the Gröbner basis computations in free algebras, but it does *not* provide normal form computations. Grischa Studzinski has send me some code that is supposed to become part of `freegb.lib` -- again, I can not call it directly, but it was fairly straight forward to implement along the lines of Grischa's code.

**__New Features__**

*__Free Algebra constructor as `UniqueFactory`__*

Up to now, the `FreeAlgebra` constructor was based on an incomplete way of caching: When you pickle and unpickle a free algebra, you would not get the same object.

```
# old behaviour
sage: F.<a,b,c> = FreeAlgebra(QQ,3)
sage: loads(dumps(F)) is F
False
```


This is now resolved. Moreover, it is not needed to explicitly provide the number of generators, when it is obvious from the list of names:

```
sage: F.<x,y,z> = FreeAlgebra(QQ)
sage: loads(dumps(F)) is F
True
```


I did one change that may be subject to criticism, and I wouldn't oppose to revert it. A free algebra in one generator is a polynomial ring. So, I return a polynomial ring:

```
sage: FreeAlgebra(QQ,'x')
Univariate Polynomial Ring in x over Rational Field
```


The constructor can now also be asked for a different implementation, as in all examples below.

*__Free Algebra via Letterplace__*

I provide a new implementation of free algebras. It can be constructed as follows:

```
sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
sage: F
Free Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field
```


Due to some shortcomings of Singular's letterplace implementation, unfortunately we need to restrict to homogeneous elements:

```
sage: (x+2*y)^2
x*x + 2*x*y + 2*y*x + 4*y*y
sage: x+0
x
Traceback (most recent call last):
...
ArithmeticError: Can only add elements of the same degree
```

This is why the new implementation can not yet become the default.

However, the arithmetic in the new implementation is much faster than the old:

```
sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
sage: F_old.<a,b,c> = FreeAlgebra(QQ)
sage: timeit('t=(x+y)^15')
5 loops, best of 3: 27.7 ms per loop
sage: timeit('t=(a+b)^15')
sage: %time t=(a+b)^15
CPU times: user 4.51 s, sys: 0.09 s, total: 4.60 s
Wall time: 6.46 s
sage: 4510/27.7
162.815884476534
sage: timeit('t=(x+y)^15')
25 loops, best of 3: 19.7 ms per loop
sage: %time t=(a+b)^15
CPU times: user 2.70 s, sys: 0.02 s, total: 2.72 s
Wall time: 2.73 s
sage: 2700/19.7
137.055837563452
```


*__One- and Twosided Ideals of Noncommutative Rings__*

I implemented it in a fairly general way, ideals can be created for any ring:

```
sage: A = SteenrodAlgebra(2)
sage: IL = A*[A.1+A.2,A.1^2]; IL
Left Ideal (Sq(2) + Sq(4), Sq(1,1)) of mod 2 Steenrod algebra
sage: IR = [A.1+A.2,A.1^2]*A; IR
Right Ideal (Sq(2) + Sq(4), Sq(1,1)) of mod 2 Steenrod algebra
sage: IT = A*[A.1+A.2,A.1^2]*A; IT
Twosided Ideal (Sq(2) + Sq(4), Sq(1,1)) of mod 2 Steenrod algebra
```


Note some nastyness: The parent of an ideal still is the "monoid of ideals of a ring". But we actually have no multiplication in the non-commutative setting:

```
sage: IL*IR
Traceback (most recent call last):
...
NotImplementedError: Can not multiply non-commutative ideals.
```


Of course, in general, we have no way to solve the ideal containment problem. But in free algebras, we have letterplace:

```
sage: I.groebner_basis(degbound=3)
Twosided Ideal (y*y*y - y*y*z + y*z*y - y*z*z, y*y*x + y*y*z + y*z*x + y*z*z, x*y + y*z, x*x - y*x - y*y - y*z) of Free Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field
sage: (x*y*z*y*x).normal_form(I)
y*z*z*y*z + y*z*z*z*x + y*z*z*z*z
sage: x*y*z*y*x - (x*y*z*y*x).normal_form(I) in I
True
sage: x*I.0-I.1*y+I.0*y in I
True
sage: 1 in I
False
```


*__Quotient Rings__*

Previously, quotient rings have only been available for rings that inherit from the base class of commutative rings. My patch makes them available for all rings, and actually it should work to some extent even for objects that belong to the category `Rings()` but do not inherit from `sage.rings.ring.Ring`.

The requirement is that we mod by an ideal `I` that is *twosided* and that has a method `I.reduce(x)` that returns a normal form of an element `x` with respect to `I`. That requirement holds for ideals of polynomial rings, and also for homogeneous ideals of free associative algebras. In particular:

```
sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
sage: I = F*[x*y+y*z,x^2+x*y-y*x-y^2]*F
sage: Q.<a,b,c> = F.quo(I); Q
Quotient of Free Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field by the ideal (x*y + y*z, x*x + x*y - y*x - y*y)
sage: a*b
-b*c
sage: a^3
-b*c*a - b*c*b - b*c*c
sage: J = Q*[a^3-b^3]*Q
sage: R.<i,j,k> = Q.quo(J); R
Quotient of Free Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field by the ideal (-y*y*z - y*z*x - 2*y*z*z, x*y + y*z, x*x + x*y - y*x - y*y)
sage: i^3
-j*k*i - j*k*j - j*k*k
sage: j^3
-j*k*i - j*k*j - j*k*k
```


One can also test if the quotient is commutative:

```
sage: Q.is_commutative()
False
sage: J = F*[x*y-y*x,x*z-z*x,y*z-z*y,x^3-y^3]*F
sage: R = F.quo(J)
sage: R.is_commutative()
True
```


**__Miscellaneous__**

I inserted the documentation of the new modules into the reference manual - I think it looks nice, but I guess a referee should double check.

Doc tests pass for me. Thus: Ready for review!!



---

archive/issue_comments_067244.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-24T16:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67244",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067245.json:
```json
{
    "body": "I forgot one technical detail:\n\nNot all rings inherit from the base class of rings. Examples are matrix algebras. In order to support non-commutative ideals for such rings, I provide the relevant methods as `ParentMethods` in the category of `Rings()`. Perhaps this duplication of code is considered a code smell.\n\nAt least, it enables the following:\n\n```\nsage: MS = MatrixSpace(QQ,2,2)\nsage: MS*[MS.1,2]\nLeft Ideal \n(\n  [0 1]\n  [0 0],\n\n  [2 0]\n  [0 2]\n)\n of Full MatrixSpace of 2 by 2 dense matrices over Rational Field\n```\n",
    "created_at": "2011-03-24T16:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67245",
    "user": "https://github.com/simon-king-jena"
}
```

I forgot one technical detail:

Not all rings inherit from the base class of rings. Examples are matrix algebras. In order to support non-commutative ideals for such rings, I provide the relevant methods as `ParentMethods` in the category of `Rings()`. Perhaps this duplication of code is considered a code smell.

At least, it enables the following:

```
sage: MS = MatrixSpace(QQ,2,2)
sage: MS*[MS.1,2]
Left Ideal 
(
  [0 1]
  [0 0],

  [2 0]
  [0 2]
)
 of Full MatrixSpace of 2 by 2 dense matrices over Rational Field
```




---

archive/issue_comments_067246.json:
```json
{
    "body": "Apparently the patchbot does not read the ticket description.\n\nApply trac7797-full_letterplace_wrapper.patch",
    "created_at": "2011-03-24T16:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67246",
    "user": "https://github.com/simon-king-jena"
}
```

Apparently the patchbot does not read the ticket description.

Apply trac7797-full_letterplace_wrapper.patch



---

archive/issue_comments_067247.json:
```json
{
    "body": "I realise that I made at least two copy-and-paste errors in the examples above: One of the \"timeit\" commands should be removed, and the ideals `I` always is the same, namely `I = F*[x*y+y*z,x<sup>2+x*y-y*x-y</sup>2]*F`.\n\nSorry, Simon",
    "created_at": "2011-03-24T16:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67247",
    "user": "https://github.com/simon-king-jena"
}
```

I realise that I made at least two copy-and-paste errors in the examples above: One of the "timeit" commands should be removed, and the ideals `I` always is the same, namely `I = F*[x*y+y*z,x<sup>2+x*y-y*x-y</sup>2]*F`.

Sorry, Simon



---

archive/issue_comments_067248.json:
```json
{
    "body": "Anne Schilling reported a problem on sage-combinat-devel: The patch did apply, but \"sage -br\" did not work. I think I found the reason: The patch did not contain the empty `__init__.py` file in `sage/algebras/letterplace/`. Simply I forgot to add it.\n\nI updated the patch, and now I hope it works. By the way, is the patchbot not working? I miss the coloured stamp on the ticket!\n\nApply trac7797-full_letterplace_wrapper.patch",
    "created_at": "2011-03-25T18:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67248",
    "user": "https://github.com/simon-king-jena"
}
```

Anne Schilling reported a problem on sage-combinat-devel: The patch did apply, but "sage -br" did not work. I think I found the reason: The patch did not contain the empty `__init__.py` file in `sage/algebras/letterplace/`. Simply I forgot to add it.

I updated the patch, and now I hope it works. By the way, is the patchbot not working? I miss the coloured stamp on the ticket!

Apply trac7797-full_letterplace_wrapper.patch



---

archive/issue_comments_067249.json:
```json
{
    "body": "Currently, the Letterplace Gr\u00f6bner bases can only be computed if the ring of coefficients is a field. I don't know whether this condition can be lifted and whether the Singular team is working on it.\n\nThat restriction *was* mentioned in the doc, but not very clearly, and the error message was obscure (namely, it came from the failing call to a Singular system function). There is now additional documentation of that restriction, and the error message is nicer.\n\nApply trac7797-full_letterplace_wrapper.patch",
    "created_at": "2011-03-27T06:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67249",
    "user": "https://github.com/simon-king-jena"
}
```

Currently, the Letterplace Gröbner bases can only be computed if the ring of coefficients is a field. I don't know whether this condition can be lifted and whether the Singular team is working on it.

That restriction *was* mentioned in the doc, but not very clearly, and the error message was obscure (namely, it came from the failing call to a Singular system function). There is now additional documentation of that restriction, and the error message is nicer.

Apply trac7797-full_letterplace_wrapper.patch



---

archive/issue_comments_067250.json:
```json
{
    "body": "Version rebased on top of #10961 available from:\n\nhttp://combinat.sagemath.org/patches/file/tip/trac7797-full_letterplace_wrapper.patch",
    "created_at": "2011-03-27T07:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67250",
    "user": "https://github.com/nthiery"
}
```

Version rebased on top of #10961 available from:

http://combinat.sagemath.org/patches/file/tip/trac7797-full_letterplace_wrapper.patch



---

archive/issue_comments_067251.json:
```json
{
    "body": "Replying to [comment:30 nthiery]:\n> Version rebased on top of #10961 available from:\n> \n> http://combinat.sagemath.org/patches/file/tip/trac7797-full_letterplace_wrapper.patch\n\nThank you!\n\nWhat is the procedure? Shall I replace my patch with the rebased one and state the dependency (to the patchbot), or shall the rebased version remain on the combinat patch server?\n\nBest regards,\nSimon",
    "created_at": "2011-03-27T07:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67251",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:30 nthiery]:
> Version rebased on top of #10961 available from:
> 
> http://combinat.sagemath.org/patches/file/tip/trac7797-full_letterplace_wrapper.patch

Thank you!

What is the procedure? Shall I replace my patch with the rebased one and state the dependency (to the patchbot), or shall the rebased version remain on the combinat patch server?

Best regards,
Simon



---

archive/issue_comments_067252.json:
```json
{
    "body": "This patch provides an interface to Singular, which gives a faster implementation of free algebras and adds new features such as for example quotients of free algebras (for terms of homogeneous degree). I have tested the quotient algebra features extensively and they seem to work great!\n\nI do not feel qualified to do a technical review, but I am happy to give a positive review for the new features added.\n\nAnne",
    "created_at": "2011-03-27T08:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67252",
    "user": "https://github.com/anneschilling"
}
```

This patch provides an interface to Singular, which gives a faster implementation of free algebras and adds new features such as for example quotients of free algebras (for terms of homogeneous degree). I have tested the quotient algebra features extensively and they seem to work great!

I do not feel qualified to do a technical review, but I am happy to give a positive review for the new features added.

Anne



---

archive/issue_comments_067253.json:
```json
{
    "body": "Replying to [comment:31 SimonKing]:\n> Replying to [comment:30 nthiery]:\n> > Version rebased on top of #10961 available from:\n> > \n> > http://combinat.sagemath.org/patches/file/tip/trac7797-full_letterplace_wrapper.patch\n> \n> Thank you!\n> \n> What is the procedure? Shall I replace my patch with the rebased one and state the dependency (to the patchbot), or shall the rebased version remain on the combinat patch server?\n> \n> Best regards,\n> Simon\n\nSince #10961 hopefully gets merged soon, you should probably upload the rebased version on trac and add `Dependencies: #10961' to the description. Then patchbot should in principle know!",
    "created_at": "2011-03-27T08:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67253",
    "user": "https://github.com/anneschilling"
}
```

Replying to [comment:31 SimonKing]:
> Replying to [comment:30 nthiery]:
> > Version rebased on top of #10961 available from:
> > 
> > http://combinat.sagemath.org/patches/file/tip/trac7797-full_letterplace_wrapper.patch
> 
> Thank you!
> 
> What is the procedure? Shall I replace my patch with the rebased one and state the dependency (to the patchbot), or shall the rebased version remain on the combinat patch server?
> 
> Best regards,
> Simon

Since #10961 hopefully gets merged soon, you should probably upload the rebased version on trac and add `Dependencies: #10961' to the description. Then patchbot should in principle know!



---

archive/issue_comments_067254.json:
```json
{
    "body": "For the patchbot:\n\nApply trac7797-full_letterplace_wrapper.patch\nDepends on #10961",
    "created_at": "2011-03-27T08:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67254",
    "user": "https://github.com/simon-king-jena"
}
```

For the patchbot:

Apply trac7797-full_letterplace_wrapper.patch
Depends on #10961



---

archive/issue_comments_067255.json:
```json
{
    "body": "Replying to [comment:32 aschilling]:\n> This patch provides an interface to Singular, which gives a faster implementation of free algebras and adds new features such as for example quotients of free algebras (for terms of homogeneous degree). I have tested the quotient algebra features extensively and they seem to work great!\n\nGood! I'll give that feedback to the Singular team as well.\n\n> I do not feel qualified to do a technical review, but I am happy to give a positive review for the new features added.\n\nThank you! There is at least one point that should probably be raised on sage-algebra: Is it acceptable that (with my patch) the `FreeAlgebra` constructor returns a polynomial ring when asked for a free algebra with only one generator? \n\nMathematically it is correct, but I wonder if that is acceptable in a CAS.\n\nSimon",
    "created_at": "2011-03-27T08:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67255",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:32 aschilling]:
> This patch provides an interface to Singular, which gives a faster implementation of free algebras and adds new features such as for example quotients of free algebras (for terms of homogeneous degree). I have tested the quotient algebra features extensively and they seem to work great!

Good! I'll give that feedback to the Singular team as well.

> I do not feel qualified to do a technical review, but I am happy to give a positive review for the new features added.

Thank you! There is at least one point that should probably be raised on sage-algebra: Is it acceptable that (with my patch) the `FreeAlgebra` constructor returns a polynomial ring when asked for a free algebra with only one generator? 

Mathematically it is correct, but I wonder if that is acceptable in a CAS.

Simon



---

archive/issue_comments_067256.json:
```json
{
    "body": "The new patch differs from the old one only in the comments.\n\nAgain for the patchbot:\n\nApply trac7797-full_letterplace_wrapper.patch\n\nDepends on #10961",
    "created_at": "2011-03-27T09:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67256",
    "user": "https://github.com/simon-king-jena"
}
```

The new patch differs from the old one only in the comments.

Again for the patchbot:

Apply trac7797-full_letterplace_wrapper.patch

Depends on #10961



---

archive/issue_comments_067257.json:
```json
{
    "body": "Attachment [trac7797-full_letterplace_wrapper.patch](tarball://root/attachments/some-uuid/ticket7797/trac7797-full_letterplace_wrapper.patch) by @simon-king-jena created at 2011-03-27 13:47:59\n\nA full wrapper for Singular's letterplace functionality, plus non-commutative ideals and ring quotients; rebased on top of 10961",
    "created_at": "2011-03-27T13:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67257",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac7797-full_letterplace_wrapper.patch](tarball://root/attachments/some-uuid/ticket7797/trac7797-full_letterplace_wrapper.patch) by @simon-king-jena created at 2011-03-27 13:47:59

A full wrapper for Singular's letterplace functionality, plus non-commutative ideals and ring quotients; rebased on top of 10961



---

archive/issue_comments_067258.json:
```json
{
    "body": "I added an `__iter__` method for `FreeAlgebraElement_letterplace`, returning the list of pairs \"exponent tuple, coefficient\", and a method of `FreeAlgebra_letterplace` that returns an element, such that `F(dict(p))==p` for any element p of F. That has been requested by Nicolas.\n\nFor the patchbot:\n\nApply trac7797-full_letterplace_wrapper.patch\n\nDepends on #10961",
    "created_at": "2011-03-27T13:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67258",
    "user": "https://github.com/simon-king-jena"
}
```

I added an `__iter__` method for `FreeAlgebraElement_letterplace`, returning the list of pairs "exponent tuple, coefficient", and a method of `FreeAlgebra_letterplace` that returns an element, such that `F(dict(p))==p` for any element p of F. That has been requested by Nicolas.

For the patchbot:

Apply trac7797-full_letterplace_wrapper.patch

Depends on #10961



---

archive/issue_comments_067259.json:
```json
{
    "body": "Replying to [comment:37 SimonKing]:\n> ...such that `F(dict(p))==p` for any element p of F.\n\nSorry, I meant to write `p == F._from_dict_(dict(p))`.",
    "created_at": "2011-03-27T14:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67259",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:37 SimonKing]:
> ...such that `F(dict(p))==p` for any element p of F.

Sorry, I meant to write `p == F._from_dict_(dict(p))`.



---

archive/issue_comments_067260.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-28T07:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67260",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067261.json:
```json
{
    "body": "It was suggested to split this ticket, and also it was suggested that the `FreeAlgebra` constructor always returns a free algebra, not a polynomial ring.",
    "created_at": "2011-03-28T07:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67261",
    "user": "https://github.com/simon-king-jena"
}
```

It was suggested to split this ticket, and also it was suggested that the `FreeAlgebra` constructor always returns a free algebra, not a polynomial ring.



---

archive/issue_comments_067262.json:
```json
{
    "body": "I managed to split my patch. The part concerning \"basic implementation of ideals in non-commutative rings\" is now at #11068. The new patch is based on top of that.\n\n**__TODO__**\n\nLet the `FreeAlgebra` constructor always return a free algebra, not a polynomial ring.\n\n**__New Feature__**\n\nIn addition to what was described in previous comments, my letterplace wrapper can compute *complete* twosided Gr\u00f6bnerbases by an adaptive algorithm. The idea is simple: If the Gr\u00f6bner basis is known out to degree `2*d-1`, but the highest degree of its generators is `d`, then the Gr\u00f6bner basis is complete.\n\nExample:\n\n```\nsage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')\nsage: I = F*[x*y-y*x,x*z-z*x,y*z-z*y,x^2*y-z^3,x*y^2+z*x^2]*F\nsage: I.groebner_basis(Infinity)\nTwosided Ideal (z*z*z*y*y + z*z*z*z*x, z*x*x*x + z*z*z*y, y*z - z*y, y*y*x + z*x*x, y*x*x - z*z*z, x*z - z*x, x*y - y*x) of Free Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field\n```\n\n\nSince the commutators are contained in the ideal, we can verify that result with a commutative Gr\u00f6bner basis, as follows:\n\n```\nsage: P.<c,b,a> = PolynomialRing(QQ,order='neglex')\nsage: J = P*[a^2*b-c^3,a*b^2+c*a^2]\nsage: J.groebner_basis()\n[b*a^2 - c^3, b^2*a + c*a^2, c*a^3 + c^3*b, c^3*b^2 + c^4*a]\n```\n\n\nSo, that's a good consistency test.\n\nApply trac7797-full_letterplace_wrapper_rel11068.patch\n\nDepends on #11068",
    "created_at": "2011-03-28T14:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67262",
    "user": "https://github.com/simon-king-jena"
}
```

I managed to split my patch. The part concerning "basic implementation of ideals in non-commutative rings" is now at #11068. The new patch is based on top of that.

**__TODO__**

Let the `FreeAlgebra` constructor always return a free algebra, not a polynomial ring.

**__New Feature__**

In addition to what was described in previous comments, my letterplace wrapper can compute *complete* twosided Gröbnerbases by an adaptive algorithm. The idea is simple: If the Gröbner basis is known out to degree `2*d-1`, but the highest degree of its generators is `d`, then the Gröbner basis is complete.

Example:

```
sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace')
sage: I = F*[x*y-y*x,x*z-z*x,y*z-z*y,x^2*y-z^3,x*y^2+z*x^2]*F
sage: I.groebner_basis(Infinity)
Twosided Ideal (z*z*z*y*y + z*z*z*z*x, z*x*x*x + z*z*z*y, y*z - z*y, y*y*x + z*x*x, y*x*x - z*z*z, x*z - z*x, x*y - y*x) of Free Associative Unital Algebra on 3 generators ('x', 'y', 'z') over Rational Field
```


Since the commutators are contained in the ideal, we can verify that result with a commutative Gröbner basis, as follows:

```
sage: P.<c,b,a> = PolynomialRing(QQ,order='neglex')
sage: J = P*[a^2*b-c^3,a*b^2+c*a^2]
sage: J.groebner_basis()
[b*a^2 - c^3, b^2*a + c*a^2, c*a^3 + c^3*b, c^3*b^2 + c^4*a]
```


So, that's a good consistency test.

Apply trac7797-full_letterplace_wrapper_rel11068.patch

Depends on #11068



---

archive/issue_comments_067263.json:
```json
{
    "body": "I don't know why, but even though mercurial claims that it tracks `sage/algebras/letterplace/__init__.py`, it kept forgetting to include it into the patch. So, I decided to fill `__init__.py` with some comment. Now it should work.\n\nOf course, you may play with the patch, but it still needs work. First of all, there is the issue that the free algebra constructor should never return a polynomial ring (in the univariate case). And then, my plan is to refactor things, such that there will also be dependencies with #9138 and #9944.\n\nDepends on #11068 \n\nApply trac7797-full_letterplace_wrapper_rel11068.patch",
    "created_at": "2011-04-01T06:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67263",
    "user": "https://github.com/simon-king-jena"
}
```

I don't know why, but even though mercurial claims that it tracks `sage/algebras/letterplace/__init__.py`, it kept forgetting to include it into the patch. So, I decided to fill `__init__.py` with some comment. Now it should work.

Of course, you may play with the patch, but it still needs work. First of all, there is the issue that the free algebra constructor should never return a polynomial ring (in the univariate case). And then, my plan is to refactor things, such that there will also be dependencies with #9138 and #9944.

Depends on #11068 

Apply trac7797-full_letterplace_wrapper_rel11068.patch



---

archive/issue_comments_067264.json:
```json
{
    "body": "I updated the patch.\n\nApply trac7797-full_letterplace_wrapper_rel11068.patch\n\nDepends on #11068\n\nActually I am not sure about all dependencies. #11068 should be enough on top of sage-4.7.alpha5. However, here is a full account of the patches that I had applied to sage-4.7.alpha5 before creating the patch here: #10296, #9944, #9138, #9976, #11115, #11068.\n\nIn particular, I think the refactoring of rings, quotient rings and non-commutative ideals is successfully solved in #9138 and #11068. Concerning unigenerated free algebras, it seems better to stay in the world of free algebras, rather than returning a polynomial ring. So, we have\n\n```\nsage: F.<x> = FreeAlgebra(QQ)\nsage: F\nFree Algebra on 1 generators (x,) over Rational Field\nsage: F.is_commutative()\nTrue\nsage: F.<x> = FreeAlgebra(QQ, implementation='letterplace')\nsage: F\nFree Associative Unital Algebra on 1 generators (x,) over Rational Field\nsage: F.is_commutative()\nTrue\n```\n\n\nIn principle, it could be reviewed now. But the patch chain in front of it is rather large, and not everything has a positive review, yet.\n\nMy next plan: Allow positive integer degree weights on the generators, extending the scope of the letterplace wrapper from homogeneous to weighted homogeneous elements, and allow degree-wise computation of weighted homogeneous Gr\u00f6bner bases. Note that this goes beyond what is currently implemented in Singular, but it should work using a little hack (slack variables).",
    "created_at": "2011-04-27T10:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67264",
    "user": "https://github.com/simon-king-jena"
}
```

I updated the patch.

Apply trac7797-full_letterplace_wrapper_rel11068.patch

Depends on #11068

Actually I am not sure about all dependencies. #11068 should be enough on top of sage-4.7.alpha5. However, here is a full account of the patches that I had applied to sage-4.7.alpha5 before creating the patch here: #10296, #9944, #9138, #9976, #11115, #11068.

In particular, I think the refactoring of rings, quotient rings and non-commutative ideals is successfully solved in #9138 and #11068. Concerning unigenerated free algebras, it seems better to stay in the world of free algebras, rather than returning a polynomial ring. So, we have

```
sage: F.<x> = FreeAlgebra(QQ)
sage: F
Free Algebra on 1 generators (x,) over Rational Field
sage: F.is_commutative()
True
sage: F.<x> = FreeAlgebra(QQ, implementation='letterplace')
sage: F
Free Associative Unital Algebra on 1 generators (x,) over Rational Field
sage: F.is_commutative()
True
```


In principle, it could be reviewed now. But the patch chain in front of it is rather large, and not everything has a positive review, yet.

My next plan: Allow positive integer degree weights on the generators, extending the scope of the letterplace wrapper from homogeneous to weighted homogeneous elements, and allow degree-wise computation of weighted homogeneous Gröbner bases. Note that this goes beyond what is currently implemented in Singular, but it should work using a little hack (slack variables).



---

archive/issue_comments_067265.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-27T10:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67265",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067266.json:
```json
{
    "body": "Sorry, I needed to update the patch due to some outdated doc tests that I forgot to correct.\n\nApply trac7797-full_letterplace_wrapper_rel11068.patch\n\nDepends on #11068",
    "created_at": "2011-04-27T12:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67266",
    "user": "https://github.com/simon-king-jena"
}
```

Sorry, I needed to update the patch due to some outdated doc tests that I forgot to correct.

Apply trac7797-full_letterplace_wrapper_rel11068.patch

Depends on #11068



---

archive/issue_comments_067267.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-28T11:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67267",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067268.json:
```json
{
    "body": "I just found that the documentation (at least with #9976 applied) is not good. Some stuff is included that certainly does not belong there.",
    "created_at": "2011-04-28T11:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67268",
    "user": "https://github.com/simon-king-jena"
}
```

I just found that the documentation (at least with #9976 applied) is not good. Some stuff is included that certainly does not belong there.



---

archive/issue_comments_067269.json:
```json
{
    "body": "Replying to [comment:44 SimonKing]:\n> I just found that the documentation (at least with #9976 applied) is not good. Some stuff is included that certainly does not belong there.\n\nActually, on second thought, it belongs there: I am talking about the two singular_function instances included in the module. The main problem was that singular_function includes the documentation provided by Singular without taking care of formatting -- resulting in numerous errors (e.g., back ticks are misinterpreted as the beginning of Latex expressions, the indentation is handled differently, and so on).\n\nIn #11268, I suggest to take care if it by turning the Singular documentation into a verbose code block. With that change, the documentation looks a lot better. I therefore make it a new dependency.\n\nDepends on #11068 #11268",
    "created_at": "2011-04-28T12:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67269",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:44 SimonKing]:
> I just found that the documentation (at least with #9976 applied) is not good. Some stuff is included that certainly does not belong there.

Actually, on second thought, it belongs there: I am talking about the two singular_function instances included in the module. The main problem was that singular_function includes the documentation provided by Singular without taking care of formatting -- resulting in numerous errors (e.g., back ticks are misinterpreted as the beginning of Latex expressions, the indentation is handled differently, and so on).

In #11268, I suggest to take care if it by turning the Singular documentation into a verbose code block. With that change, the documentation looks a lot better. I therefore make it a new dependency.

Depends on #11068 #11268



---

archive/issue_comments_067270.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-28T12:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67270",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067271.json:
```json
{
    "body": "Attachment [trac7797-letterplace_degree_weights.patch](tarball://root/attachments/some-uuid/ticket7797/trac7797-letterplace_degree_weights.patch) by @simon-king-jena created at 2011-05-26 09:12:05\n\nPositive integral degree weights for letterplace. UniqueFactory for free algebras.",
    "created_at": "2011-05-26T09:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67271",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac7797-letterplace_degree_weights.patch](tarball://root/attachments/some-uuid/ticket7797/trac7797-letterplace_degree_weights.patch) by @simon-king-jena created at 2011-05-26 09:12:05

Positive integral degree weights for letterplace. UniqueFactory for free algebras.



---

archive/issue_comments_067272.json:
```json
{
    "body": "Changing keywords from \"singular\" to \"singular, free algebra, letterplace\".",
    "created_at": "2011-05-26T09:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67272",
    "user": "https://github.com/simon-king-jena"
}
```

Changing keywords from "singular" to "singular, free algebra, letterplace".



---

archive/issue_comments_067273.json:
```json
{
    "body": "Meanwhile I implemented two other features:\n\n**Uniqueness of parents**\n\nWe had\n\n```\nsage: F.<x,y,z> = FreeAlgebra(QQ, 3)\nsage: loads(dumps(F)) is F\nFalse\n```\n\n\nI rewrote the `FreeAlgebra` constructor using `UniqueFactory`, so that the answer above becomes `True`.\n\n**Degree weights**\n\nThe letterplace implementation in Singular is restricted to homogeneous ideals, and each generator can only have degree 1. With a little hack, I introduced positive integral degree weights for generators, so that we can now do:\n\n```\nsage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace', degrees=[1,2,3])\nsage: I = F*[x*y+z-y*x,x*y*z-x^6+y^3]*F\nsage: I.groebner_basis(Infinity)\nTwosided Ideal (x*z*z - y*x*x*z - y*x*y*y + y*x*z*x + y*y*y*x + z*x*z + z*y*y - z*z*x, x*y - y*x + z, x*x*x*x*z*y*y + x*x*x*z*y*y*x - x*x*x*z*y*z - x*x*z*y*x*z + x*x*z*y*y*x*x + x*x*z*y*y*y - x*x*z*y*z*x - x*z*y*x*x*z - x*z*y*x*z*x + x*z*y*y*x*x*x + 2*x*z*y*y*y*x - 2*x*z*y*y*z - x*z*y*z*x*x - x*z*y*z*y + y*x*z*x*x*x*x*x - 4*y*x*z*x*x*z - 4*y*x*z*x*z*x + 4*y*x*z*y*x*x*x + 3*y*x*z*y*y*x - 4*y*x*z*y*z + y*y*x*x*x*x*z + y*y*x*x*x*z*x - 3*y*y*x*x*z*x*x - y*y*x*x*z*y + 5*y*y*x*z*x*x*x + 4*y*y*x*z*y*x - 4*y*y*y*x*x*z + 4*y*y*y*x*z*x + 3*y*y*y*y*z + 4*y*y*y*z*x*x + 6*y*y*y*z*y + y*y*z*x*x*x*x + y*y*z*x*z + 7*y*y*z*y*x*x + 7*y*y*z*y*y - 7*y*y*z*z*x - y*z*x*x*x*z - y*z*x*x*z*x + 3*y*z*x*z*x*x + y*z*x*z*y + y*z*y*x*x*x*x - 3*y*z*y*x*z + 7*y*z*y*y*x*x + 3*y*z*y*y*y - 3*y*z*y*z*x - 5*y*z*z*x*x*x - 4*y*z*z*y*x + 4*y*z*z*z - z*y*x*x*x*z - z*y*x*x*z*x - z*y*x*z*x*x - z*y*x*z*y + z*y*y*x*x*x*x - 3*z*y*y*x*z + 3*z*y*y*y*x*x + z*y*y*y*y - 3*z*y*y*z*x - z*y*z*x*x*x - 2*z*y*z*y*x + 2*z*y*z*z - z*z*x*x*x*x*x + 4*z*z*x*x*z + 4*z*z*x*z*x - 4*z*z*y*x*x*x - 3*z*z*y*y*x + 4*z*z*y*z + 4*z*z*z*x*x + 2*z*z*z*y, x*x*x*x*x*z + x*x*x*x*z*x + x*x*x*z*x*x + x*x*z*x*x*x + x*z*x*x*x*x + y*x*z*y - y*y*x*z + y*z*z + z*x*x*x*x*x - z*z*y, x*x*x*x*x*x - y*x*z - y*y*y + z*z) of Free Associative Unital Algebra on 3 generators (x, y, z) over Rational Field\n```\n\nThis and the possibility to compute a complete Gr\u00f6bner basis (provided a finite complete Gr\u00f6bner basis exists) go beyond what is currently in Singular.\n\nThe underlying idea of the degree weights is: Introduce a homogenizing variable. By default, it is called `x`, but a different name is chosen if there is a name conflict. Here, it is renamed to `x_`. And then, we represent a generator `z` of degree `d` internally as `z*x_^(d-1)` (of course with non-commutative multiplication).\n\nHence, the underlying truncated letterplace ring becomes a bit bigger, and in the bigger ring all generators are of degree one. Of course, the additional variable is omitted in the string representation. We have for example\n\n```\nsage: z\nz\nsage: z.degree()\n3\nsage: z.letterplace_polynomial()\nz*x__1*x__2\n```\n\n\nAs much as I know, with that approach, Gr\u00f6bner bases are correctly computed: If in all polynomials each occurrence of `z` is followed by `x_^(d-1)` then all S-polynomials and reductions (computed in the ring with additional generator `x_` and with all generators in degree 1) will have the same property.\n\nI know this is a hack, but I guess it may be useful. It certainly will be usefull for my current project, because I *need* degree weights.\n\nApply trac7797-full_letterplace_wrapper_rel11068.patch trac7797-letterplace_degree_weights.patch\n\nDepends on #11068, #11268",
    "created_at": "2011-05-26T09:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67273",
    "user": "https://github.com/simon-king-jena"
}
```

Meanwhile I implemented two other features:

**Uniqueness of parents**

We had

```
sage: F.<x,y,z> = FreeAlgebra(QQ, 3)
sage: loads(dumps(F)) is F
False
```


I rewrote the `FreeAlgebra` constructor using `UniqueFactory`, so that the answer above becomes `True`.

**Degree weights**

The letterplace implementation in Singular is restricted to homogeneous ideals, and each generator can only have degree 1. With a little hack, I introduced positive integral degree weights for generators, so that we can now do:

```
sage: F.<x,y,z> = FreeAlgebra(QQ, implementation='letterplace', degrees=[1,2,3])
sage: I = F*[x*y+z-y*x,x*y*z-x^6+y^3]*F
sage: I.groebner_basis(Infinity)
Twosided Ideal (x*z*z - y*x*x*z - y*x*y*y + y*x*z*x + y*y*y*x + z*x*z + z*y*y - z*z*x, x*y - y*x + z, x*x*x*x*z*y*y + x*x*x*z*y*y*x - x*x*x*z*y*z - x*x*z*y*x*z + x*x*z*y*y*x*x + x*x*z*y*y*y - x*x*z*y*z*x - x*z*y*x*x*z - x*z*y*x*z*x + x*z*y*y*x*x*x + 2*x*z*y*y*y*x - 2*x*z*y*y*z - x*z*y*z*x*x - x*z*y*z*y + y*x*z*x*x*x*x*x - 4*y*x*z*x*x*z - 4*y*x*z*x*z*x + 4*y*x*z*y*x*x*x + 3*y*x*z*y*y*x - 4*y*x*z*y*z + y*y*x*x*x*x*z + y*y*x*x*x*z*x - 3*y*y*x*x*z*x*x - y*y*x*x*z*y + 5*y*y*x*z*x*x*x + 4*y*y*x*z*y*x - 4*y*y*y*x*x*z + 4*y*y*y*x*z*x + 3*y*y*y*y*z + 4*y*y*y*z*x*x + 6*y*y*y*z*y + y*y*z*x*x*x*x + y*y*z*x*z + 7*y*y*z*y*x*x + 7*y*y*z*y*y - 7*y*y*z*z*x - y*z*x*x*x*z - y*z*x*x*z*x + 3*y*z*x*z*x*x + y*z*x*z*y + y*z*y*x*x*x*x - 3*y*z*y*x*z + 7*y*z*y*y*x*x + 3*y*z*y*y*y - 3*y*z*y*z*x - 5*y*z*z*x*x*x - 4*y*z*z*y*x + 4*y*z*z*z - z*y*x*x*x*z - z*y*x*x*z*x - z*y*x*z*x*x - z*y*x*z*y + z*y*y*x*x*x*x - 3*z*y*y*x*z + 3*z*y*y*y*x*x + z*y*y*y*y - 3*z*y*y*z*x - z*y*z*x*x*x - 2*z*y*z*y*x + 2*z*y*z*z - z*z*x*x*x*x*x + 4*z*z*x*x*z + 4*z*z*x*z*x - 4*z*z*y*x*x*x - 3*z*z*y*y*x + 4*z*z*y*z + 4*z*z*z*x*x + 2*z*z*z*y, x*x*x*x*x*z + x*x*x*x*z*x + x*x*x*z*x*x + x*x*z*x*x*x + x*z*x*x*x*x + y*x*z*y - y*y*x*z + y*z*z + z*x*x*x*x*x - z*z*y, x*x*x*x*x*x - y*x*z - y*y*y + z*z) of Free Associative Unital Algebra on 3 generators (x, y, z) over Rational Field
```

This and the possibility to compute a complete Gröbner basis (provided a finite complete Gröbner basis exists) go beyond what is currently in Singular.

The underlying idea of the degree weights is: Introduce a homogenizing variable. By default, it is called `x`, but a different name is chosen if there is a name conflict. Here, it is renamed to `x_`. And then, we represent a generator `z` of degree `d` internally as `z*x_^(d-1)` (of course with non-commutative multiplication).

Hence, the underlying truncated letterplace ring becomes a bit bigger, and in the bigger ring all generators are of degree one. Of course, the additional variable is omitted in the string representation. We have for example

```
sage: z
z
sage: z.degree()
3
sage: z.letterplace_polynomial()
z*x__1*x__2
```


As much as I know, with that approach, Gröbner bases are correctly computed: If in all polynomials each occurrence of `z` is followed by `x_^(d-1)` then all S-polynomials and reductions (computed in the ring with additional generator `x_` and with all generators in degree 1) will have the same property.

I know this is a hack, but I guess it may be useful. It certainly will be usefull for my current project, because I *need* degree weights.

Apply trac7797-full_letterplace_wrapper_rel11068.patch trac7797-letterplace_degree_weights.patch

Depends on #11068, #11268



---

archive/issue_comments_067274.json:
```json
{
    "body": "I noticed that I forgot one detail: Latex!\n\nWith the latest patch, we also get\n\n```\nsage: K.<z> = GF(25)\nsage: F.<a,b,c> = FreeAlgebra(K, implementation='letterplace', degrees=[1,2,3])\nsage: -(a*b*(z+1)-c)^2\n(2*z + 1)*a*b*a*b + (z + 1)*a*b*c + (z + 1)*c*a*b - c*c\nsage: latex(-(a*b*(z+1)-c)^2)\n\\left(2 z + 1\\right) a b a b + \\left(z + 1\\right) a b c + \\left(z + 1\\right) c a b - c c\n```\n\nApply trac7797-full_letterplace_wrapper_rel11068.patch trac7797-letterplace_degree_weights.patch trac7797-latex_letterplace.patch\n\nDepends on #11068, #11268",
    "created_at": "2011-05-26T10:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67274",
    "user": "https://github.com/simon-king-jena"
}
```

I noticed that I forgot one detail: Latex!

With the latest patch, we also get

```
sage: K.<z> = GF(25)
sage: F.<a,b,c> = FreeAlgebra(K, implementation='letterplace', degrees=[1,2,3])
sage: -(a*b*(z+1)-c)^2
(2*z + 1)*a*b*a*b + (z + 1)*a*b*c + (z + 1)*c*a*b - c*c
sage: latex(-(a*b*(z+1)-c)^2)
\left(2 z + 1\right) a b a b + \left(z + 1\right) a b c + \left(z + 1\right) c a b - c c
```

Apply trac7797-full_letterplace_wrapper_rel11068.patch trac7797-letterplace_degree_weights.patch trac7797-latex_letterplace.patch

Depends on #11068, #11268



---

archive/issue_comments_067275.json:
```json
{
    "body": "... or also\n\n```\nsage: F.<bla,alpha,z> = FreeAlgebra(QQ, implementation='letterplace', degrees=[1,2,3])\nsage: latex(-3*alpha*bla-z)\n-3 \\alpha \\mbox{bla} - z\n```\n",
    "created_at": "2011-05-26T10:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67275",
    "user": "https://github.com/simon-king-jena"
}
```

... or also

```
sage: F.<bla,alpha,z> = FreeAlgebra(QQ, implementation='letterplace', degrees=[1,2,3])
sage: latex(-3*alpha*bla-z)
-3 \alpha \mbox{bla} - z
```




---

archive/issue_comments_067276.json:
```json
{
    "body": "Odd. The documentation for letterplace used to build fine. But now, it does not build *at all*! The output are three empty html pages (empty except for the title and the navigation) - the doc strings do not appear.\n\nAny idea where that might come from?",
    "created_at": "2011-05-26T10:49:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67276",
    "user": "https://github.com/simon-king-jena"
}
```

Odd. The documentation for letterplace used to build fine. But now, it does not build *at all*! The output are three empty html pages (empty except for the title and the navigation) - the doc strings do not appear.

Any idea where that might come from?



---

archive/issue_comments_067277.json:
```json
{
    "body": "I don't know where it came from. But after deleting doc/output/html/en/reference and doc/output/doctrees/, building the documentation finally succeeded.\n\nSo, problem vanished.",
    "created_at": "2011-05-26T13:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67277",
    "user": "https://github.com/simon-king-jena"
}
```

I don't know where it came from. But after deleting doc/output/html/en/reference and doc/output/doctrees/, building the documentation finally succeeded.

So, problem vanished.



---

archive/issue_comments_067278.json:
```json
{
    "body": "Apparently I had changed the milestone by accident...",
    "created_at": "2011-05-27T06:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67278",
    "user": "https://github.com/simon-king-jena"
}
```

Apparently I had changed the milestone by accident...



---

archive/issue_comments_067279.json:
```json
{
    "body": "In my application, I also need conversion from graded sub-algebras. Hence, I implemented it in the new patch.\n\nTo be precise: If we have free graded algebras A and B in letterplace implementation, then there is a coercion from A to B if and only if there is a coercion from the base ring of A to the base ring of B, and the set of generator names of A is a subset of the generator names of B, and the degrees of equally named generators of A and B are equal.\n\nThe coercion is always name and degree preserving.\n\nExample:\n\n```\nsage: F.<t,y,z> = FreeAlgebra(ZZ, implementation='letterplace', degrees=[4,2,3])\nsage: G = FreeAlgebra(GF(5), implementation='letterplace', names=['x','y','z','t'], degrees=[1,2,3,4])\nsage: t*G.0       # indirect doctest\nt*x\nsage: (t*G.0 + G.1*G.2)*y\ny*z*y + t*x*y\n```\n\n\nApply trac7797-full_letterplace_wrapper_rel11068.patch trac7797-letterplace_degree_weights.patch trac7797-latex_letterplace.patch trac7797-letterplace_coercion.patch",
    "created_at": "2011-07-27T15:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67279",
    "user": "https://github.com/simon-king-jena"
}
```

In my application, I also need conversion from graded sub-algebras. Hence, I implemented it in the new patch.

To be precise: If we have free graded algebras A and B in letterplace implementation, then there is a coercion from A to B if and only if there is a coercion from the base ring of A to the base ring of B, and the set of generator names of A is a subset of the generator names of B, and the degrees of equally named generators of A and B are equal.

The coercion is always name and degree preserving.

Example:

```
sage: F.<t,y,z> = FreeAlgebra(ZZ, implementation='letterplace', degrees=[4,2,3])
sage: G = FreeAlgebra(GF(5), implementation='letterplace', names=['x','y','z','t'], degrees=[1,2,3,4])
sage: t*G.0       # indirect doctest
t*x
sage: (t*G.0 + G.1*G.2)*y
y*z*y + t*x*y
```


Apply trac7797-full_letterplace_wrapper_rel11068.patch trac7797-letterplace_degree_weights.patch trac7797-latex_letterplace.patch trac7797-letterplace_coercion.patch



---

archive/issue_comments_067280.json:
```json
{
    "body": "Attachment [trac7797-full_letterplace_wrapper_rel11068.patch](tarball://root/attachments/some-uuid/ticket7797/trac7797-full_letterplace_wrapper_rel11068.patch) by @simon-king-jena created at 2011-08-01 16:37:37\n\nA full wrapper for Singular's letterplace functionality, plus complete Groebner bases; based on top of 11068",
    "created_at": "2011-08-01T16:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67280",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac7797-full_letterplace_wrapper_rel11068.patch](tarball://root/attachments/some-uuid/ticket7797/trac7797-full_letterplace_wrapper_rel11068.patch) by @simon-king-jena created at 2011-08-01 16:37:37

A full wrapper for Singular's letterplace functionality, plus complete Groebner bases; based on top of 11068



---

archive/issue_comments_067281.json:
```json
{
    "body": "Attachment [trac7797-latex_letterplace.patch](tarball://root/attachments/some-uuid/ticket7797/trac7797-latex_letterplace.patch) by @simon-king-jena created at 2011-08-01 16:45:29\n\nImplement latex for letterplace polynomials and letterplace algebras",
    "created_at": "2011-08-01T16:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67281",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac7797-latex_letterplace.patch](tarball://root/attachments/some-uuid/ticket7797/trac7797-latex_letterplace.patch) by @simon-king-jena created at 2011-08-01 16:45:29

Implement latex for letterplace polynomials and letterplace algebras



---

archive/issue_comments_067282.json:
```json
{
    "body": "Implementing coercion for letterplace algebras",
    "created_at": "2011-08-01T16:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67282",
    "user": "https://github.com/simon-king-jena"
}
```

Implementing coercion for letterplace algebras



---

archive/issue_comments_067283.json:
```json
{
    "body": "Attachment [trac7797-letterplace_coercion.patch](tarball://root/attachments/some-uuid/ticket7797/trac7797-letterplace_coercion.patch) by @simon-king-jena created at 2011-08-01 16:48:22\n\nI had to rebase three of the four patches. Still needing review...\n\nApply trac7797-full_letterplace_wrapper_rel11068.patch trac7797-letterplace_degree_weights.patch trac7797-latex_letterplace.patch trac7797-letterplace_coercion.patch",
    "created_at": "2011-08-01T16:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67283",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac7797-letterplace_coercion.patch](tarball://root/attachments/some-uuid/ticket7797/trac7797-letterplace_coercion.patch) by @simon-king-jena created at 2011-08-01 16:48:22

I had to rebase three of the four patches. Still needing review...

Apply trac7797-full_letterplace_wrapper_rel11068.patch trac7797-letterplace_degree_weights.patch trac7797-latex_letterplace.patch trac7797-letterplace_coercion.patch



---

archive/issue_comments_067284.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-08-01T21:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67284",
    "user": "https://github.com/kiwifb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067285.json:
```json
{
    "body": "In [attachment:trac7797-full_letterplace_wrapper_rel11068.patch] please do not use SAGE_ROOT + local/include in module_list.py use SAGE_INC instead. I spent sometime cleaning all that up for 4.7.1 and would like to see it stay clean for a little while longer.",
    "created_at": "2011-08-01T21:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67285",
    "user": "https://github.com/kiwifb"
}
```

In [attachment:trac7797-full_letterplace_wrapper_rel11068.patch] please do not use SAGE_ROOT + local/include in module_list.py use SAGE_INC instead. I spent sometime cleaning all that up for 4.7.1 and would like to see it stay clean for a little while longer.



---

archive/issue_comments_067286.json:
```json
{
    "body": "Replying to [comment:55 fbissey]:\n> In [attachment:trac7797-full_letterplace_wrapper_rel11068.patch] please do not use SAGE_ROOT + local/include in module_list.py use SAGE_INC instead. \n\nI didn't know that SAGE_INC exists. It is certainly a good idea to use such variables whenever possible.",
    "created_at": "2011-08-01T23:35:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67286",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:55 fbissey]:
> In [attachment:trac7797-full_letterplace_wrapper_rel11068.patch] please do not use SAGE_ROOT + local/include in module_list.py use SAGE_INC instead. 

I didn't know that SAGE_INC exists. It is certainly a good idea to use such variables whenever possible.



---

archive/issue_comments_067287.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-08-01T23:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67287",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067288.json:
```json
{
    "body": "I'm now using SAGE_INC, and I used the occasion to create a combined patch.\n \nApply trac7797-full_letterplace_wrapper_combined.patch",
    "created_at": "2011-08-01T23:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67288",
    "user": "https://github.com/simon-king-jena"
}
```

I'm now using SAGE_INC, and I used the occasion to create a combined patch.
 
Apply trac7797-full_letterplace_wrapper_combined.patch



---

archive/issue_comments_067289.json:
```json
{
    "body": "I had to rebase my patch: Some trivial changes in the doc tests were needed, since block orders are now displayed differently.\n\nApply trac7797-full_letterplace_wrapper_combined.patch",
    "created_at": "2011-08-15T09:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67289",
    "user": "https://github.com/simon-king-jena"
}
```

I had to rebase my patch: Some trivial changes in the doc tests were needed, since block orders are now displayed differently.

Apply trac7797-full_letterplace_wrapper_combined.patch



---

archive/issue_comments_067290.json:
```json
{
    "body": "sage-4.7.2alpha3-prerelease with the following patches applies:\n\n```\ntrac11815_format_must_preserve_embedding.patch\ntrac11115-cached_cython.patch\ntrac11115_cached_function_pickling.patch\ntrac11068_nc_ideals_and_quotients.patch\ntrac11068_quotient_ring_without_names.patch\ntrac11068_lifting_map.patch\ntrac7797-full_letterplace_wrapper_combined.patch\n```\n\ncompiles/installs and runs `sage -testall` successfully  on a SuSE Enterprise 11.1.\nThis is close to a positive review, but I'll check out another platform before and have a look at the patch.",
    "created_at": "2011-09-26T20:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67290",
    "user": "https://github.com/alexanderdreyer"
}
```

sage-4.7.2alpha3-prerelease with the following patches applies:

```
trac11815_format_must_preserve_embedding.patch
trac11115-cached_cython.patch
trac11115_cached_function_pickling.patch
trac11068_nc_ideals_and_quotients.patch
trac11068_quotient_ring_without_names.patch
trac11068_lifting_map.patch
trac7797-full_letterplace_wrapper_combined.patch
```

compiles/installs and runs `sage -testall` successfully  on a SuSE Enterprise 11.1.
This is close to a positive review, but I'll check out another platform before and have a look at the patch.



---

archive/issue_comments_067291.json:
```json
{
    "body": "Remove assignee @burcin.",
    "created_at": "2011-09-26T20:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67291",
    "user": "https://github.com/alexanderdreyer"
}
```

Remove assignee @burcin.



---

archive/issue_comments_067292.json:
```json
{
    "body": "Set assignee to @burcin.",
    "created_at": "2011-09-26T20:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67292",
    "user": "https://github.com/alexanderdreyer"
}
```

Set assignee to @burcin.



---

archive/issue_comments_067293.json:
```json
{
    "body": "Also compiles/installs and runs `sage -testall` successfully on Mac OSX ppc (32bit). So I can give a positive review for the technical part. Somebody needs to look for the Maths.",
    "created_at": "2011-09-27T20:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67293",
    "user": "https://github.com/alexanderdreyer"
}
```

Also compiles/installs and runs `sage -testall` successfully on Mac OSX ppc (32bit). So I can give a positive review for the technical part. Somebody needs to look for the Maths.



---

archive/issue_comments_067294.json:
```json
{
    "body": "I think it makes sense to use #4539 (which already has a positive review, but is pending because of #9138) as a dependency. I have updated the patch accordingly. The doc tests pass (at least on my machine).",
    "created_at": "2011-10-26T18:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67294",
    "user": "https://github.com/simon-king-jena"
}
```

I think it makes sense to use #4539 (which already has a positive review, but is pending because of #9138) as a dependency. I have updated the patch accordingly. The doc tests pass (at least on my machine).



---

archive/issue_comments_067295.json:
```json
{
    "body": "I forgot to notify the patch bot:\n\nApply trac7797-full_letterplace_wrapper_combined.patch",
    "created_at": "2011-10-26T18:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67295",
    "user": "https://github.com/simon-king-jena"
}
```

I forgot to notify the patch bot:

Apply trac7797-full_letterplace_wrapper_combined.patch



---

archive/issue_comments_067296.json:
```json
{
    "body": "The patch fails to apply to 5.0.beta11 -- see patchbot logs. I suspect #12461 is the cause.",
    "created_at": "2012-03-29T11:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67296",
    "user": "https://github.com/loefflerd"
}
```

The patch fails to apply to 5.0.beta11 -- see patchbot logs. I suspect #12461 is the cause.



---

archive/issue_comments_067297.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-29T11:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67297",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067298.json:
```json
{
    "body": "Yes, #12641 was to blame. The reason was that apparently #12641 did remove four blank spaces. So, the change is trivial.\n\nBy the way: At the recent annual meeting of the German Science Foundation Priority Programme on computer algebra, I was talking to Viktor Levandovskii, who is responsible for Letterplace in Singular. He confirmed that my hacks for implementing degree weights and for computing complete Gr\u00f6bner bases are correct.\n\nApply trac7797-full_letterplace_wrapper_combined.patch",
    "created_at": "2012-03-30T09:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67298",
    "user": "https://github.com/simon-king-jena"
}
```

Yes, #12641 was to blame. The reason was that apparently #12641 did remove four blank spaces. So, the change is trivial.

By the way: At the recent annual meeting of the German Science Foundation Priority Programme on computer algebra, I was talking to Viktor Levandovskii, who is responsible for Letterplace in Singular. He confirmed that my hacks for implementing degree weights and for computing complete Gröbner bases are correct.

Apply trac7797-full_letterplace_wrapper_combined.patch



---

archive/issue_comments_067299.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-30T09:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67299",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067300.json:
```json
{
    "body": "It needs to be rebased wrt. #12749: This ticket adds doctests, but one hunk for sage/algebras/free_algebra.py adds some doctest as well...",
    "created_at": "2012-04-15T11:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67300",
    "user": "https://github.com/simon-king-jena"
}
```

It needs to be rebased wrt. #12749: This ticket adds doctests, but one hunk for sage/algebras/free_algebra.py adds some doctest as well...



---

archive/issue_comments_067301.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-04-15T11:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67301",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067302.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-04-15T11:30:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67302",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067303.json:
```json
{
    "body": "Done. And please please find someone for a review!\n\nApply trac7797-full_letterplace_wrapper_combined.patch",
    "created_at": "2012-04-15T11:30:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67303",
    "user": "https://github.com/simon-king-jena"
}
```

Done. And please please find someone for a review!

Apply trac7797-full_letterplace_wrapper_combined.patch



---

archive/issue_comments_067304.json:
```json
{
    "body": "It is now 4 months ago that I last asked if someone could review the patch, so that we would have Gr\u00f6bner bases of two-sided homogeneous ideals in free associative algebras. Which other CAS has those? So: BUMP!",
    "created_at": "2012-08-13T13:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67304",
    "user": "https://github.com/simon-king-jena"
}
```

It is now 4 months ago that I last asked if someone could review the patch, so that we would have Gröbner bases of two-sided homogeneous ideals in free associative algebras. Which other CAS has those? So: BUMP!



---

archive/issue_comments_067305.json:
```json
{
    "body": "I had to modify one doctest, due to a new test in the category of rings - see #12988.\n\nApply trac7797-full_letterplace_wrapper_combined.patch",
    "created_at": "2012-08-14T12:39:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67305",
    "user": "https://github.com/simon-king-jena"
}
```

I had to modify one doctest, due to a new test in the category of rings - see #12988.

Apply trac7797-full_letterplace_wrapper_combined.patch



---

archive/issue_comments_067306.json:
```json
{
    "body": "The patch looks good to me, just use  the `:trac:`7791`` statement to refer to this ticket here. Provided, that the tests succeeds (I'm currently building a recent sage), I'd say, that we are close to positive.",
    "created_at": "2012-08-14T22:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67306",
    "user": "https://github.com/alexanderdreyer"
}
```

The patch looks good to me, just use  the `:trac:`7791`` statement to refer to this ticket here. Provided, that the tests succeeds (I'm currently building a recent sage), I'd say, that we are close to positive.



---

archive/issue_comments_067307.json:
```json
{
    "body": "Replying to [comment:70 AlexanderDreyer]:\n> The patch looks good to me, just use  the `:trac:`7791`` statement to refer to this ticket here. Provided, that the tests succeeds (I'm currently building a recent sage), I'd say, that we are close to positive.\n\nYep, I think I wrote the patch before the `:trac:` directive has been introduced. The patchbot complains about trailing white space - so, I'll take care of that as well.",
    "created_at": "2012-08-15T06:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67307",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:70 AlexanderDreyer]:
> The patch looks good to me, just use  the `:trac:`7791`` statement to refer to this ticket here. Provided, that the tests succeeds (I'm currently building a recent sage), I'd say, that we are close to positive.

Yep, I think I wrote the patch before the `:trac:` directive has been introduced. The patchbot complains about trailing white space - so, I'll take care of that as well.



---

archive/issue_comments_067308.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-08-15T06:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67308",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067309.json:
```json
{
    "body": "Now it should be fine, regarding whitespace and regarding `:trac:` directive.\n\nApply trac7797-full_letterplace_wrapper_combined.patch",
    "created_at": "2012-08-15T06:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67309",
    "user": "https://github.com/simon-king-jena"
}
```

Now it should be fine, regarding whitespace and regarding `:trac:` directive.

Apply trac7797-full_letterplace_wrapper_combined.patch



---

archive/issue_comments_067310.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-08-15T06:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67310",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067311.json:
```json
{
    "body": "The patch applies nicely to sage-5.3 beta1 and the rebuild of the sage library was successful. So let' s wait for `make ptestlong` to finish.",
    "created_at": "2012-08-15T07:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67311",
    "user": "https://github.com/alexanderdreyer"
}
```

The patch applies nicely to sage-5.3 beta1 and the rebuild of the sage library was successful. So let' s wait for `make ptestlong` to finish.



---

archive/issue_comments_067312.json:
```json
{
    "body": "Ok, `ptestlong` succeeded, so we ave a positive review!",
    "created_at": "2012-08-15T11:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67312",
    "user": "https://github.com/alexanderdreyer"
}
```

Ok, `ptestlong` succeeded, so we ave a positive review!



---

archive/issue_comments_067313.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-15T11:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67313",
    "user": "https://github.com/alexanderdreyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067314.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-08-23T12:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67314",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_067315.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2012-08-24T20:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67315",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_067316.json:
```json
{
    "body": "This leads to lots of failures on Solaris SPARC:\n\n```\n\n        sage -t  --long -force_lib devel/sage/sage/algebras/free_algebra.py # 3 doctests failed\n        sage -t  --long -force_lib devel/sage/sage/algebras/letterplace/free_algebra_element_letterplace.pyx # 13 doctests failed\n        sage -t  --long -force_lib devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx # 6 doctests failed\n        sage -t  --long -force_lib devel/sage/sage/algebras/letterplace/letterplace_ideal.pyx # 14 doctests failed\n        sage -t  --long -force_lib devel/sage/sage/rings/quotient_ring.py # 11 doctests failed\n        sage -t  --long -force_lib devel/sage/sage/rings/quotient_ring_element.py # 1 doctests failed\n```\n\nSee [http://build.sagemath.org/sage/builders/Skynet%20mark%20%28SunOS%205.10-32%29/builds/207/steps/shell_7/logs/stdio](http://build.sagemath.org/sage/builders/Skynet%20mark%20%28SunOS%205.10-32%29/builds/207/steps/shell_7/logs/stdio).",
    "created_at": "2012-08-24T20:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67316",
    "user": "https://github.com/jdemeyer"
}
```

This leads to lots of failures on Solaris SPARC:

```

        sage -t  --long -force_lib devel/sage/sage/algebras/free_algebra.py # 3 doctests failed
        sage -t  --long -force_lib devel/sage/sage/algebras/letterplace/free_algebra_element_letterplace.pyx # 13 doctests failed
        sage -t  --long -force_lib devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx # 6 doctests failed
        sage -t  --long -force_lib devel/sage/sage/algebras/letterplace/letterplace_ideal.pyx # 14 doctests failed
        sage -t  --long -force_lib devel/sage/sage/rings/quotient_ring.py # 11 doctests failed
        sage -t  --long -force_lib devel/sage/sage/rings/quotient_ring_element.py # 1 doctests failed
```

See [http://build.sagemath.org/sage/builders/Skynet%20mark%20%28SunOS%205.10-32%29/builds/207/steps/shell_7/logs/stdio](http://build.sagemath.org/sage/builders/Skynet%20mark%20%28SunOS%205.10-32%29/builds/207/steps/shell_7/logs/stdio).



---

archive/issue_comments_067317.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2012-08-24T20:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67317",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_067318.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-08-24T20:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67318",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067319.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-08-24T20:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67319",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067320.json:
```json
{
    "body": "I see that most (or all?) the errors reported in the log file occur while calling a singular_function. Is it perhaps the case that singular_function is generally problematic on Solaris SPARC? \n\nDoes Letterplace works on Solaris SPARC in Singular? I think I was told that Singular's system function could be a problem -- but Letterplace relies on it, both in Singular and here.\n\nI.e., is the problem on the side of Singular, or of the wrapper?",
    "created_at": "2012-08-24T22:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67320",
    "user": "https://github.com/simon-king-jena"
}
```

I see that most (or all?) the errors reported in the log file occur while calling a singular_function. Is it perhaps the case that singular_function is generally problematic on Solaris SPARC? 

Does Letterplace works on Solaris SPARC in Singular? I think I was told that Singular's system function could be a problem -- but Letterplace relies on it, both in Singular and here.

I.e., is the problem on the side of Singular, or of the wrapper?



---

archive/issue_comments_067321.json:
```json
{
    "body": "Replying to [comment:79 SimonKing]:\n> I.e., is the problem on the side of Singular, or of the wrapper?\nHow can I check?  What commands should I run in Singular to check?\n\nAlso, I added #13237 (Upgrade to Singular-3-1-5) as dependency just in case it matters.  My tests on Solaris SPARC were done with the new Singular from #13237.",
    "created_at": "2012-08-27T11:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67321",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:79 SimonKing]:
> I.e., is the problem on the side of Singular, or of the wrapper?
How can I check?  What commands should I run in Singular to check?

Also, I added #13237 (Upgrade to Singular-3-1-5) as dependency just in case it matters.  My tests on Solaris SPARC were done with the new Singular from #13237.



---

archive/issue_comments_067322.json:
```json
{
    "body": "Replying to [comment:80 jdemeyer]:\n> Replying to [comment:79 SimonKing]:\n> > I.e., is the problem on the side of Singular, or of the wrapper?\n> How can I check?  What commands should I run in Singular to check?\n> \n> Also, I added #13237 (Upgrade to Singular-3-1-5) as dependency just in case it matters.  My tests on Solaris SPARC were done with the new Singular from #13237.\n\nHans Sch\u00f6nemann has tested it. He used Singular-3-1-5, or in more detail:\n\n```\nSingular for SunOS-5 version 3-1-5 (3150)  Aug 27 2012 19:23:52\nwith\n        factory(@(#) factoryVersion = 3.1.5),libfac(3.1.5,July 2012),\n        GMP(4.2),NTL(5.5.2),64bit,static readline,Plural,DBM,\n        dynamic modules,dynamic p_Procs,OM_CHECK=0,OM_TRACK=0,random=1346170574\n        CC= gcc -m64 -mptr64 -mcpu=ultrasparc3 -O2 -w -fomit-frame-pointer -pipe -DNDEBUG -DOM_NDEBUG -DSunOS_5 -DHAVE_CONFIG_H,\n        CXX= g++ -m64 -mptr64 -mcpu=ultrasparc3 -O2 -w -fomit-frame-pointer -I.. -I/users/cip/alggeom/hannes/galois64 -pipe -DNDEBUG -DOM_NDEBUG -DSunOS_5 -DHAVE_CONFIG_H (3.3.2)\n```\n\n\nThe example worked fine, which indicates that it is a problem with my wrapper. If you want to test it for yourself:\n\n```\nLIB \"freegb.lib\";\nring r = 0,(x,y,z),dp;\nint d =4; // degree bound\ndef R = makeLetterplaceRing(d);\nsetring R;\nideal I = x(1)*y(2) + y(1)*z(2), x(1)*x(2) + x(1)*y(2) - y(1)*x(2) - y(1)*y(2);\noption(redSB); option(redTail);\nideal J = letplaceGBasis(I);\nJ;\n```\n\nThe expected result is\n\n```\n==> J[1]=x(1)*y(2)+y(1)*z(2)\n==> J[2]=x(1)*x(2)-y(1)*x(2)-y(1)*y(2)-y(1)*z(2)\n==> J[3]=y(1)*y(2)*y(3)-y(1)*y(2)*z(3)+y(1)*z(2)*y(3)-y(1)*z(2)*z(3)\n==> J[4]=y(1)*y(2)*x(3)+y(1)*y(2)*z(3)+y(1)*z(2)*x(3)+y(1)*z(2)*z(3)\n==> J[5]=y(1)*z(2)*y(3)*y(4)-y(1)*z(2)*y(3)*z(4)+y(1)*z(2)*z(3)*y(4)-y(1)*z(2\\\n   )*z(3)*z(4)\n==> J[6]=y(1)*z(2)*y(3)*x(4)+y(1)*z(2)*y(3)*z(4)+y(1)*z(2)*z(3)*x(4)+y(1)*z(2\\\n   )*z(3)*z(4)\n==> J[7]=y(1)*y(2)*z(3)*y(4)-y(1)*y(2)*z(3)*z(4)+y(1)*z(2)*z(3)*y(4)-y(1)*z(2\\\n   )*z(3)*z(4)\n==> J[8]=y(1)*y(2)*z(3)*x(4)+y(1)*y(2)*z(3)*z(4)+y(1)*z(2)*z(3)*x(4)+y(1)*z(2\\\n   )*z(3)*z(4)\n```\n\nI will see whether `letplaceGBasis` does anything new - perhaps I can learn from it?",
    "created_at": "2012-08-28T16:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67322",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:80 jdemeyer]:
> Replying to [comment:79 SimonKing]:
> > I.e., is the problem on the side of Singular, or of the wrapper?
> How can I check?  What commands should I run in Singular to check?
> 
> Also, I added #13237 (Upgrade to Singular-3-1-5) as dependency just in case it matters.  My tests on Solaris SPARC were done with the new Singular from #13237.

Hans Schönemann has tested it. He used Singular-3-1-5, or in more detail:

```
Singular for SunOS-5 version 3-1-5 (3150)  Aug 27 2012 19:23:52
with
        factory(@(#) factoryVersion = 3.1.5),libfac(3.1.5,July 2012),
        GMP(4.2),NTL(5.5.2),64bit,static readline,Plural,DBM,
        dynamic modules,dynamic p_Procs,OM_CHECK=0,OM_TRACK=0,random=1346170574
        CC= gcc -m64 -mptr64 -mcpu=ultrasparc3 -O2 -w -fomit-frame-pointer -pipe -DNDEBUG -DOM_NDEBUG -DSunOS_5 -DHAVE_CONFIG_H,
        CXX= g++ -m64 -mptr64 -mcpu=ultrasparc3 -O2 -w -fomit-frame-pointer -I.. -I/users/cip/alggeom/hannes/galois64 -pipe -DNDEBUG -DOM_NDEBUG -DSunOS_5 -DHAVE_CONFIG_H (3.3.2)
```


The example worked fine, which indicates that it is a problem with my wrapper. If you want to test it for yourself:

```
LIB "freegb.lib";
ring r = 0,(x,y,z),dp;
int d =4; // degree bound
def R = makeLetterplaceRing(d);
setring R;
ideal I = x(1)*y(2) + y(1)*z(2), x(1)*x(2) + x(1)*y(2) - y(1)*x(2) - y(1)*y(2);
option(redSB); option(redTail);
ideal J = letplaceGBasis(I);
J;
```

The expected result is

```
==> J[1]=x(1)*y(2)+y(1)*z(2)
==> J[2]=x(1)*x(2)-y(1)*x(2)-y(1)*y(2)-y(1)*z(2)
==> J[3]=y(1)*y(2)*y(3)-y(1)*y(2)*z(3)+y(1)*z(2)*y(3)-y(1)*z(2)*z(3)
==> J[4]=y(1)*y(2)*x(3)+y(1)*y(2)*z(3)+y(1)*z(2)*x(3)+y(1)*z(2)*z(3)
==> J[5]=y(1)*z(2)*y(3)*y(4)-y(1)*z(2)*y(3)*z(4)+y(1)*z(2)*z(3)*y(4)-y(1)*z(2\
   )*z(3)*z(4)
==> J[6]=y(1)*z(2)*y(3)*x(4)+y(1)*z(2)*y(3)*z(4)+y(1)*z(2)*z(3)*x(4)+y(1)*z(2\
   )*z(3)*z(4)
==> J[7]=y(1)*y(2)*z(3)*y(4)-y(1)*y(2)*z(3)*z(4)+y(1)*z(2)*z(3)*y(4)-y(1)*z(2\
   )*z(3)*z(4)
==> J[8]=y(1)*y(2)*z(3)*x(4)+y(1)*y(2)*z(3)*z(4)+y(1)*z(2)*z(3)*x(4)+y(1)*z(2\
   )*z(3)*z(4)
```

I will see whether `letplaceGBasis` does anything new - perhaps I can learn from it?



---

archive/issue_comments_067323.json:
```json
{
    "body": "Replying to [comment:81 SimonKing]:\n> I will see whether `letplaceGBasis` does anything new - perhaps I can learn from it?\n\nNo, the essential part is the same. Namely:\n\n```\n  ideal J = system(\"freegb\",I,uptodeg,lV);\n```\n\nIf I am not mistaken, it is the analogue of this command that fails in my code.\n\nThe question that I'd like to be answered is: Are calls to Singular's \"system\" function possible in Sage on Solaris SPARC? Could you please test the following in Sage on Solaris SPARC?\n\n```\nsage: from sage.libs.singular.function import singular_function\nsage: sing_system = singular_function(\"system\")\nsage: R.<x,y> = QQ[]\nsage: sing_system(\"uname\", ring=R)\n'x86_64-Linux'  # ok, the answer will be different on Solaris SPARC...\n```\n",
    "created_at": "2012-08-28T16:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67323",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:81 SimonKing]:
> I will see whether `letplaceGBasis` does anything new - perhaps I can learn from it?

No, the essential part is the same. Namely:

```
  ideal J = system("freegb",I,uptodeg,lV);
```

If I am not mistaken, it is the analogue of this command that fails in my code.

The question that I'd like to be answered is: Are calls to Singular's "system" function possible in Sage on Solaris SPARC? Could you please test the following in Sage on Solaris SPARC?

```
sage: from sage.libs.singular.function import singular_function
sage: sing_system = singular_function("system")
sage: R.<x,y> = QQ[]
sage: sing_system("uname", ring=R)
'x86_64-Linux'  # ok, the answer will be different on Solaris SPARC...
```




---

archive/issue_comments_067324.json:
```json
{
    "body": "Solaris SPARC, Sage 5.2 (i.e. Singular-3-1-3-3):\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sage.libs.singular.function.singular_function(\"system\")(\"uname\", ring=PolynomialRing(QQ,2,'x'))\n// ** s_internalDelete: cannot delete type sqrfree(493)\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n| Sage Version 5.2, Release Date: 2012-07-25                         |\n| Type \"notebook()\" for the browser-based notebook interface.        |\n| Type \"help()\" for help.                                            |\n/home/jdemeyer/mark/sage-5.2/<ipython console> in <module>()\n\n/home/jdemeyer/mark/sage-5.2/local/lib/python2.7/site-packages/sage/libs/singular/function.so in sage.libs.singular.function.SingularFunction.__call__ (sage/libs/singular/function.cpp:11875)()\n\n/home/jdemeyer/mark/sage-5.2/local/lib/python2.7/site-packages/sage/libs/singular/function.so in sage.libs.singular.function.call_function (sage/libs/singular/function.cpp:13425)()\n\nRuntimeError: Error in Singular function call 'system':\n system(`sqrfree`) failed\n```\n",
    "created_at": "2012-08-28T17:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67324",
    "user": "https://github.com/jdemeyer"
}
```

Solaris SPARC, Sage 5.2 (i.e. Singular-3-1-3-3):

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage.libs.singular.function.singular_function("system")("uname", ring=PolynomialRing(QQ,2,'x'))
// ** s_internalDelete: cannot delete type sqrfree(493)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
| Sage Version 5.2, Release Date: 2012-07-25                         |
| Type "notebook()" for the browser-based notebook interface.        |
| Type "help()" for help.                                            |
/home/jdemeyer/mark/sage-5.2/<ipython console> in <module>()

/home/jdemeyer/mark/sage-5.2/local/lib/python2.7/site-packages/sage/libs/singular/function.so in sage.libs.singular.function.SingularFunction.__call__ (sage/libs/singular/function.cpp:11875)()

/home/jdemeyer/mark/sage-5.2/local/lib/python2.7/site-packages/sage/libs/singular/function.so in sage.libs.singular.function.call_function (sage/libs/singular/function.cpp:13425)()

RuntimeError: Error in Singular function call 'system':
 system(`sqrfree`) failed
```




---

archive/issue_comments_067325.json:
```json
{
    "body": "Thank you, Jeroen!\n\nSo, the bug is not in my wrapper, but in singular_function. And that error looks rather strange. I'll ask Hans, tomorrow.\n\nMartin, do you have an idea where that error might come from?",
    "created_at": "2012-08-28T17:52:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67325",
    "user": "https://github.com/simon-king-jena"
}
```

Thank you, Jeroen!

So, the bug is not in my wrapper, but in singular_function. And that error looks rather strange. I'll ask Hans, tomorrow.

Martin, do you have an idea where that error might come from?



---

archive/issue_comments_067326.json:
```json
{
    "body": "Here is the code for `system(\"uname\")` (to be found in Singular/extra.cc):\n\n```C\n/*==================== uname ==================================*/\n    if(strcmp(sys_cmd,\"uname\")==0)\n    {\n      res->rtyp=STRING_CMD;\n      res->data = omStrDup(S_UNAME);\n      return FALSE;\n    }\n```\n\n\nAbout `// ** s_internalDelete: cannot delete type sqrfree(493)`: According to Hans, 493 is the token for the command `sqrfree`, which is *not* a type but a command. Therefore deleting an object with 493's type is impossible. He doesn't understand how that happens here.\n\n`res->data` is a C string, and `STRING_CMD` is the token 495, which stands for the type of a string (`char *`). Could Solares SPARC mistake 495 for 493??",
    "created_at": "2012-08-29T08:48:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67326",
    "user": "https://github.com/simon-king-jena"
}
```

Here is the code for `system("uname")` (to be found in Singular/extra.cc):

```C
/*==================== uname ==================================*/
    if(strcmp(sys_cmd,"uname")==0)
    {
      res->rtyp=STRING_CMD;
      res->data = omStrDup(S_UNAME);
      return FALSE;
    }
```


About `// ** s_internalDelete: cannot delete type sqrfree(493)`: According to Hans, 493 is the token for the command `sqrfree`, which is *not* a type but a command. Therefore deleting an object with 493's type is impossible. He doesn't understand how that happens here.

`res->data` is a C string, and `STRING_CMD` is the token 495, which stands for the type of a string (`char *`). Could Solares SPARC mistake 495 for 493??



---

archive/issue_comments_067327.json:
```json
{
    "body": "Replying to [comment:85 SimonKing]:\n> `res->data` is a C string, and `STRING_CMD` is the token 495, which stands for the type of a string (`char *`). Could Solares SPARC mistake 495 for 493??\nThere probably an outdated Singular/tok.h around. Tokens like INTMOD_CMD were added recently, so this would explain the shift in the enum.",
    "created_at": "2012-08-29T09:00:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67327",
    "user": "https://github.com/alexanderdreyer"
}
```

Replying to [comment:85 SimonKing]:
> `res->data` is a C string, and `STRING_CMD` is the token 495, which stands for the type of a string (`char *`). Could Solares SPARC mistake 495 for 493??
There probably an outdated Singular/tok.h around. Tokens like INTMOD_CMD were added recently, so this would explain the shift in the enum.



---

archive/issue_comments_067328.json:
```json
{
    "body": "Okay, with a build from scratch:\n\n```\nsage: sage.libs.singular.function.singular_function(\"system\")(\"uname\", ring=PolynomialRing(QQ,2,'x'))\n'SunOS-5'\n```\n\n\nSo I probably messed up something last time (e.g. forget `sage -b`).",
    "created_at": "2012-08-30T20:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67328",
    "user": "https://github.com/jdemeyer"
}
```

Okay, with a build from scratch:

```
sage: sage.libs.singular.function.singular_function("system")("uname", ring=PolynomialRing(QQ,2,'x'))
'SunOS-5'
```


So I probably messed up something last time (e.g. forget `sage -b`).



---

archive/issue_comments_067329.json:
```json
{
    "body": "Changing assignee from @burcin to @jdemeyer.",
    "created_at": "2012-08-30T20:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67329",
    "user": "https://github.com/jdemeyer"
}
```

Changing assignee from @burcin to @jdemeyer.



---

archive/issue_comments_067330.json:
```json
{
    "body": "Strange.  I applied the patch of this ticket again and get only one doctest failure now in `sage/algebras`:\n\n```\nsage -t  \"devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx\"\n**********************************************************************\nFile \"/home/jdemeyer/mark/sage-5.4.beta0/devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx\", line 684:\n    sage: G = F._reductor_(I.gens(),3); G\nExpected:\n    Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3 over Rational Field\nGot:\n    Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2 over Rational Field\n**********************************************************************\n```\n\n\nThis calls for some further investigation...",
    "created_at": "2012-08-30T20:35:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67330",
    "user": "https://github.com/jdemeyer"
}
```

Strange.  I applied the patch of this ticket again and get only one doctest failure now in `sage/algebras`:

```
sage -t  "devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx"
**********************************************************************
File "/home/jdemeyer/mark/sage-5.4.beta0/devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx", line 684:
    sage: G = F._reductor_(I.gens(),3); G
Expected:
    Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3 over Rational Field
Got:
    Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2 over Rational Field
**********************************************************************
```


This calls for some further investigation...



---

archive/issue_comments_067331.json:
```json
{
    "body": "Replying to [comment:88 jdemeyer]:\n> {{{\n> sage -t  \"devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx\"\n> **********************************************************************\n> File \"/home/jdemeyer/mark/sage-5.4.beta0/devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx\", line 684:\n>     sage: G = F._reductor_(I.gens(),3); G\n> Expected:\n>     Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3 over Rational Field\n> Got:\n>     Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2 over Rational Field\n> **********************************************************************\n> }}}\n> \n> This calls for some further investigation...\n\nThat test is about an internally used method (note the underscores), and the output depends on a polynomial ring that is used to simulate computations in free associative algebras out to a certain degree. As you can see, the ideal we expect and the ideal we got are alike - only the polynomial rings differ.\n\nThe point is that the underlying polynomial ring can change during computations, and the free associative algebras are unique parents. Hence, if tests are executed in different order then it may very well be that the polynomial ring used behind the scenes is different. Only the final result (i.e., interpreted in the free associative algebra) is unique.\n\nI suggest to modify that test (and perhaps others as well) as follows:\n\n```\n>     sage: G = F._reductor_(I.gens(),3); G\n> Expected:\n>     Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2... over Rational Field\n```\n\nThe variables before the `...` are guaranteed to occur, and we don't know (and don't care) whether more variables appear behind the scenes.\n\nWould you accept that solution?",
    "created_at": "2012-08-30T20:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67331",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:88 jdemeyer]:
> {{{
> sage -t  "devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx"
> **********************************************************************
> File "/home/jdemeyer/mark/sage-5.4.beta0/devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx", line 684:
>     sage: G = F._reductor_(I.gens(),3); G
> Expected:
>     Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3 over Rational Field
> Got:
>     Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2 over Rational Field
> **********************************************************************
> }}}
> 
> This calls for some further investigation...

That test is about an internally used method (note the underscores), and the output depends on a polynomial ring that is used to simulate computations in free associative algebras out to a certain degree. As you can see, the ideal we expect and the ideal we got are alike - only the polynomial rings differ.

The point is that the underlying polynomial ring can change during computations, and the free associative algebras are unique parents. Hence, if tests are executed in different order then it may very well be that the polynomial ring used behind the scenes is different. Only the final result (i.e., interpreted in the free associative algebra) is unique.

I suggest to modify that test (and perhaps others as well) as follows:

```
>     sage: G = F._reductor_(I.gens(),3); G
> Expected:
>     Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2... over Rational Field
```

The variables before the `...` are guaranteed to occur, and we don't know (and don't care) whether more variables appear behind the scenes.

Would you accept that solution?



---

archive/issue_comments_067332.json:
```json
{
    "body": "Replying to [comment:89 SimonKing]:\n> I suggest to modify that test (and perhaps others as well) as follows:\n> {{{\n> >     sage: G = F._reductor_(I.gens(),3); G\n> > Expected:\n> >     Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2... over Rational Field\n> }}}\n> The variables before the `...` are guaranteed to occur, and we don't know (and don't care) whether more variables appear behind the scenes.\n> \n> Would you accept that solution?\nSounds reasonable to me. So I'd reestablished the positive review, if Jeroen likes is, too.",
    "created_at": "2012-08-30T23:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67332",
    "user": "https://github.com/alexanderdreyer"
}
```

Replying to [comment:89 SimonKing]:
> I suggest to modify that test (and perhaps others as well) as follows:
> {{{
> >     sage: G = F._reductor_(I.gens(),3); G
> > Expected:
> >     Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2... over Rational Field
> }}}
> The variables before the `...` are guaranteed to occur, and we don't know (and don't care) whether more variables appear behind the scenes.
> 
> Would you accept that solution?
Sounds reasonable to me. So I'd reestablished the positive review, if Jeroen likes is, too.



---

archive/issue_comments_067333.json:
```json
{
    "body": "Good for me.",
    "created_at": "2012-08-31T14:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67333",
    "user": "https://github.com/jdemeyer"
}
```

Good for me.



---

archive/issue_comments_067334.json:
```json
{
    "body": "Replying to [comment:91 jdemeyer]:\n> Good for me.\n\nOK, then I'll prepare a patch. Probably not before Sunday, though...",
    "created_at": "2012-08-31T14:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67334",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:91 jdemeyer]:
> Good for me.

OK, then I'll prepare a patch. Probably not before Sunday, though...



---

archive/issue_comments_067335.json:
```json
{
    "body": "I have updated the patch, using an ellipse (...) in the failing test.\n\nApply  trac7797-full_letterplace_wrapper_combined.patch",
    "created_at": "2012-09-02T07:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67335",
    "user": "https://github.com/simon-king-jena"
}
```

I have updated the patch, using an ellipse (...) in the failing test.

Apply  trac7797-full_letterplace_wrapper_combined.patch



---

archive/issue_comments_067336.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-09-02T07:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67336",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067337.json:
```json
{
    "body": "Hi, I can positively review for Linux. I don't get Sage 5.* compiled on Solaris. Are there any precompiled recent binaries around, maybe at *.washington.edu?",
    "created_at": "2012-09-07T19:44:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67337",
    "user": "https://github.com/alexanderdreyer"
}
```

Hi, I can positively review for Linux. I don't get Sage 5.* compiled on Solaris. Are there any precompiled recent binaries around, maybe at *.washington.edu?



---

archive/issue_comments_067338.json:
```json
{
    "body": "Passes tests for me (I just tested the modified files, not the whole Sage library) on Mac OS X 10.7 and OpenSolaris. I'm working on Solaris, but the only Solaris machines I have access to are really slow.\n\nBy the way, can you explain the role of the new line 821 in `sage/structure/parent.pyx`?",
    "created_at": "2012-09-07T20:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67338",
    "user": "https://github.com/jhpalmieri"
}
```

Passes tests for me (I just tested the modified files, not the whole Sage library) on Mac OS X 10.7 and OpenSolaris. I'm working on Solaris, but the only Solaris machines I have access to are really slow.

By the way, can you explain the role of the new line 821 in `sage/structure/parent.pyx`?



---

archive/issue_comments_067339.json:
```json
{
    "body": "Replying to [comment:96 jhpalmieri]:\n> By the way, can you explain the role of the new line 821 in `sage/structure/parent.pyx`?\n\nI guess the plan was to add a doc test, then I changed my mind and deleted the doctest incompletely. I guess that line can be removed (by a reviewer patch?).",
    "created_at": "2012-09-07T20:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67339",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:96 jhpalmieri]:
> By the way, can you explain the role of the new line 821 in `sage/structure/parent.pyx`?

I guess the plan was to add a doc test, then I changed my mind and deleted the doctest incompletely. I guess that line can be removed (by a reviewer patch?).



---

archive/issue_comments_067340.json:
```json
{
    "body": "Attachment [trac_7797-ref.patch](tarball://root/attachments/some-uuid/ticket7797/trac_7797-ref.patch) by @jhpalmieri created at 2012-09-07 21:24:58",
    "created_at": "2012-09-07T21:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67340",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_7797-ref.patch](tarball://root/attachments/some-uuid/ticket7797/trac_7797-ref.patch) by @jhpalmieri created at 2012-09-07 21:24:58



---

archive/issue_comments_067341.json:
```json
{
    "body": "Tests pass on skynet machine mark.",
    "created_at": "2012-10-24T15:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67341",
    "user": "https://github.com/jhpalmieri"
}
```

Tests pass on skynet machine mark.



---

archive/issue_comments_067342.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-10-24T15:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67342",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067343.json:
```json
{
    "body": "I'm getting (in a trial sage-5.5.beta1, so it includes many other tickets)\n\n```\nsage -t  -force_lib devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx\n**********************************************************************\nFile \"/release/merger/sage-5.5.beta1/devel/sage-main/sage/algebras/letterplace/free_algebra_letterplace.pyx\", line 684:\n    sage: G = F._reductor_(I.gens(),3); G\nExpected:\n    Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3... over Rational Field\nGot:\n    Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2 over Rational Field\n**********************************************************************\n```\n",
    "created_at": "2012-10-30T15:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67343",
    "user": "https://github.com/jdemeyer"
}
```

I'm getting (in a trial sage-5.5.beta1, so it includes many other tickets)

```
sage -t  -force_lib devel/sage/sage/algebras/letterplace/free_algebra_letterplace.pyx
**********************************************************************
File "/release/merger/sage-5.5.beta1/devel/sage-main/sage/algebras/letterplace/free_algebra_letterplace.pyx", line 684:
    sage: G = F._reductor_(I.gens(),3); G
Expected:
    Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3... over Rational Field
Got:
    Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2 over Rational Field
**********************************************************************
```




---

archive/issue_comments_067344.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-10-30T15:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67344",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_067345.json:
```json
{
    "body": "I think we have already discussed that the order of doctests may influence the size of the polynomial ring used to represent the letterplace elements.\n\nSo, the fix should be to have `Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2... over Rational Field`. I'll do so (hopefully) soonish.",
    "created_at": "2012-10-30T16:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67345",
    "user": "https://github.com/simon-king-jena"
}
```

I think we have already discussed that the order of doctests may influence the size of the polynomial ring used to represent the letterplace elements.

So, the fix should be to have `Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2... over Rational Field`. I'll do so (hopefully) soonish.



---

archive/issue_comments_067346.json:
```json
{
    "body": "Doctest error confirmed with (unreleased but essentially ready) sage-5.5.beta0, but not with sage-5.4.rc2.",
    "created_at": "2012-10-30T16:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67346",
    "user": "https://github.com/jdemeyer"
}
```

Doctest error confirmed with (unreleased but essentially ready) sage-5.5.beta0, but not with sage-5.4.rc2.



---

archive/issue_comments_067347.json:
```json
{
    "body": "A full wrapper for Singular's letterplace functionality, plus positive integral degree weights, plus complete Groebner bases of weighted homogeneous two-sided ideals, plus coercion. Rel #12988",
    "created_at": "2012-11-09T10:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67347",
    "user": "https://github.com/simon-king-jena"
}
```

A full wrapper for Singular's letterplace functionality, plus positive integral degree weights, plus complete Groebner bases of weighted homogeneous two-sided ideals, plus coercion. Rel #12988



---

archive/issue_comments_067348.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-11-09T10:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67348",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_067349.json:
```json
{
    "body": "Attachment [trac7797-full_letterplace_wrapper_combined.patch](tarball://root/attachments/some-uuid/ticket7797/trac7797-full_letterplace_wrapper_combined.patch) by @simon-king-jena created at 2012-11-09 10:20:36\n\nI am sorry that I took so long to fix it.\n\nI have changed the \"big\" patch. The diff of the two patch versions is:\n\n```diff\n--- trac7797-full_letterplace_wrapper_combined.patch    2012-11-09 11:15:19.355793326 +0100\n+++ trac7797-full_letterplace_wrapper_combined.patch        2012-09-02 09:00:20.000000000 +0200\n@@ -2176,7 +2176,7 @@\n +            sage: p.reduce(I)\n +            y*y*y - y*y*z + y*z*y - y*z*z\n +            sage: G = F._reductor_(I.gens(),3); G\n-+            Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2... over Rational Field\n++            Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3... over Rational Field\n +\n +        We do not use the usual reduction method for polynomials in\n +        Sage, since it does the reductions in a different order\n```\n\n\nI hope it is ok to restore the positive review, since I assume doctests will be run anyway before releasing.\n\nApply trac7797-full_letterplace_wrapper_combined.patch trac_7797-ref.patch",
    "created_at": "2012-11-09T10:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67349",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac7797-full_letterplace_wrapper_combined.patch](tarball://root/attachments/some-uuid/ticket7797/trac7797-full_letterplace_wrapper_combined.patch) by @simon-king-jena created at 2012-11-09 10:20:36

I am sorry that I took so long to fix it.

I have changed the "big" patch. The diff of the two patch versions is:

```diff
--- trac7797-full_letterplace_wrapper_combined.patch    2012-11-09 11:15:19.355793326 +0100
+++ trac7797-full_letterplace_wrapper_combined.patch        2012-09-02 09:00:20.000000000 +0200
@@ -2176,7 +2176,7 @@
 +            sage: p.reduce(I)
 +            y*y*y - y*y*z + y*z*y - y*z*z
 +            sage: G = F._reductor_(I.gens(),3); G
-+            Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2... over Rational Field
++            Ideal (x*y_1 + y*z_1, x_1*y_2 + y_1*z_2, x*x_1 + x*y_1 - y*x_1 - y*y_1, x_1*x_2 + x_1*y_2 - y_1*x_2 - y_1*y_2) of Multivariate Polynomial Ring in x, y, z, x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3... over Rational Field
 +
 +        We do not use the usual reduction method for polynomials in
 +        Sage, since it does the reductions in a different order
```


I hope it is ok to restore the positive review, since I assume doctests will be run anyway before releasing.

Apply trac7797-full_letterplace_wrapper_combined.patch trac_7797-ref.patch



---

archive/issue_comments_067350.json:
```json
{
    "body": "Just realized, that I'm the reviewer: I'm fine with reestablishing to positive review.",
    "created_at": "2012-11-09T11:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67350",
    "user": "https://github.com/alexanderdreyer"
}
```

Just realized, that I'm the reviewer: I'm fine with reestablishing to positive review.



---

archive/issue_comments_067351.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-11-16T21:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67351",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_067352.json:
```json
{
    "body": "See #13802 for a problem this causes on Cygwin, though it looks like the fix is easy.  I'd appreciate knowing whether it's okay to add `libraries=singular_libs` or whether that would cause problems; I think I *have* to add `SAGE_INC + 'factory'`.",
    "created_at": "2012-12-05T19:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67352",
    "user": "https://github.com/kcrisman"
}
```

See #13802 for a problem this causes on Cygwin, though it looks like the fix is easy.  I'd appreciate knowing whether it's okay to add `libraries=singular_libs` or whether that would cause problems; I think I *have* to add `SAGE_INC + 'factory'`.



---

archive/issue_comments_067353.json:
```json
{
    "body": "Replying to [comment:108 kcrisman]:\n> See #13802 for a problem this causes on Cygwin, though it looks like the fix is easy.  I'd appreciate knowing whether it's okay to add `libraries=singular_libs` or whether that would cause problems; I think I *have* to add `SAGE_INC + 'factory'`.\nIndeed, looking at the other singular-based modules it makes sense. I don't expect problems doing so.",
    "created_at": "2012-12-05T21:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67353",
    "user": "https://github.com/alexanderdreyer"
}
```

Replying to [comment:108 kcrisman]:
> See #13802 for a problem this causes on Cygwin, though it looks like the fix is easy.  I'd appreciate knowing whether it's okay to add `libraries=singular_libs` or whether that would cause problems; I think I *have* to add `SAGE_INC + 'factory'`.
Indeed, looking at the other singular-based modules it makes sense. I don't expect problems doing so.



---

archive/issue_comments_067354.json:
```json
{
    "body": "> > See #13802 for a problem this causes on Cygwin, though it looks like the fix is easy.  I'd appreciate knowing whether it's okay to add `libraries=singular_libs` or whether that would cause problems; I think I *have* to add `SAGE_INC + 'factory'`.\n> Indeed, looking at the other singular-based modules it makes sense. I don't expect problems doing so.\nGreat, can you give some feedback on the patch at #13802 then?  Thanks!",
    "created_at": "2012-12-05T22:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67354",
    "user": "https://github.com/kcrisman"
}
```

> > See #13802 for a problem this causes on Cygwin, though it looks like the fix is easy.  I'd appreciate knowing whether it's okay to add `libraries=singular_libs` or whether that would cause problems; I think I *have* to add `SAGE_INC + 'factory'`.
> Indeed, looking at the other singular-based modules it makes sense. I don't expect problems doing so.
Great, can you give some feedback on the patch at #13802 then?  Thanks!



---

archive/issue_comments_067355.json:
```json
{
    "body": "Replying to [comment:110 kcrisman]:\n> Great, can you give some feedback on the patch at #13802 then?  Thanks!\nVery well, I was able to positively review that patch.",
    "created_at": "2012-12-06T08:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67355",
    "user": "https://github.com/alexanderdreyer"
}
```

Replying to [comment:110 kcrisman]:
> Great, can you give some feedback on the patch at #13802 then?  Thanks!
Very well, I was able to positively review that patch.



---

archive/issue_comments_067356.json:
```json
{
    "body": "> > Great, can you give some feedback on the patch at #13802 then?  Thanks!\n> Very well, I was able to positively review that patch.\nVery helpful, thank you.",
    "created_at": "2012-12-06T15:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7797",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7797#issuecomment-67356",
    "user": "https://github.com/kcrisman"
}
```

> > Great, can you give some feedback on the patch at #13802 then?  Thanks!
> Very well, I was able to positively review that patch.
Very helpful, thank you.
