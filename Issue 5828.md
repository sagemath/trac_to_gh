# Issue 5828: number fields -- serious bug in coercion to a relative extension of degree 1

archive/issues_005828.json:
```json
{
    "body": "Assignee: was\n\nCC:  robertwb mstreng\n\n\n```\n\n\nOn Sun, Apr 19, 2009 at 10:16 AM, Utpal Sarkar <doetoe@gmail.com> wrote:\n>\n> Hi,\n>\n> I found some strange behaviour of the Hilbert class field of a\n> quadratic number field when the class number is 1, so the Hilbert\n> class field is equal to the ground field:\n> sage: K.<w> = QuadraticField(-5); KX.<X> = K[]; H.<h> =\n> K.hilbert_class_field()\n> sage: (X + w + 1).base_extend(H)\n> X + w + 1\n> No problem: the Hilbert class field is a proper extension, and the\n> polynomial remains the same.\n>\n> sage: K.<w> = QuadraticField(-1); KX.<X> = K[]; H.<h> =\n> K.hilbert_class_field()\n> sage: (X + w + 1).base_extend(H)\n> X + 1\n> In this case the Hilbert class field is equal to K, and the part of\n> the polynomial that is not in QQ disappears.\n\nYou've found a bug in the coercion in the special case of a relative extension of degree 1.\nHere's some simpler code to illustrate it:\n\nsage: K.<w> = QuadraticField(-1)\nsage: KX.<X> = K[]\nsage: H.<h> = K.extension(X-1)\nsage: H(w)\n0\n\nThe internal function responsible for the bug is:\n\nsage: H._NumberField_relative__base_inclusion(w)\n0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5828\n\n",
    "created_at": "2009-04-20T03:58:47Z",
    "labels": [
        "number theory",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "number fields -- serious bug in coercion to a relative extension of degree 1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5828",
    "user": "was"
}
```
Assignee: was

CC:  robertwb mstreng


```


On Sun, Apr 19, 2009 at 10:16 AM, Utpal Sarkar <doetoe@gmail.com> wrote:
>
> Hi,
>
> I found some strange behaviour of the Hilbert class field of a
> quadratic number field when the class number is 1, so the Hilbert
> class field is equal to the ground field:
> sage: K.<w> = QuadraticField(-5); KX.<X> = K[]; H.<h> =
> K.hilbert_class_field()
> sage: (X + w + 1).base_extend(H)
> X + w + 1
> No problem: the Hilbert class field is a proper extension, and the
> polynomial remains the same.
>
> sage: K.<w> = QuadraticField(-1); KX.<X> = K[]; H.<h> =
> K.hilbert_class_field()
> sage: (X + w + 1).base_extend(H)
> X + 1
> In this case the Hilbert class field is equal to K, and the part of
> the polynomial that is not in QQ disappears.

You've found a bug in the coercion in the special case of a relative extension of degree 1.
Here's some simpler code to illustrate it:

sage: K.<w> = QuadraticField(-1)
sage: KX.<X> = K[]
sage: H.<h> = K.extension(X-1)
sage: H(w)
0

The internal function responsible for the bug is:

sage: H._NumberField_relative__base_inclusion(w)
0
```


Issue created by migration from https://trac.sagemath.org/ticket/5828





---

archive/issue_comments_045814.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5828#issuecomment-45814",
    "user": "davidloeffler"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_045815.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-21T08:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5828#issuecomment-45815",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_045816.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-02T13:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5828#issuecomment-45816",
    "user": "lftabera"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_045817.json:
```json
{
    "body": "This is solved now (4.4.4)\n\n\n```\nsage: K.<w> = QuadraticField(-1)\nsage: KX.<X> = K[]\nsage: H.<h> = K.extension(X-1)\nsage: H(w)\nw\nsage: H._NumberField_relative__base_inclusion(w)\nw\n```\n\n\n\n```\nsage: K.<w> = QuadraticField(-1);\nsage: KX.<X> = K[]\nsage: H.<h> =K.hilbert_class_field()\nsage: (X + w + 1).base_extend(H)\nX + w + 1\n```\n\n\nThe bug should be closed, at most add the attached doctest.",
    "created_at": "2010-07-02T13:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5828#issuecomment-45817",
    "user": "lftabera"
}
```

This is solved now (4.4.4)


```
sage: K.<w> = QuadraticField(-1)
sage: KX.<X> = K[]
sage: H.<h> = K.extension(X-1)
sage: H(w)
w
sage: H._NumberField_relative__base_inclusion(w)
w
```



```
sage: K.<w> = QuadraticField(-1);
sage: KX.<X> = K[]
sage: H.<h> =K.hilbert_class_field()
sage: (X + w + 1).base_extend(H)
X + w + 1
```


The bug should be closed, at most add the attached doctest.



---

archive/issue_comments_045818.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-22T17:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5828#issuecomment-45818",
    "user": "mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_045819.json:
```json
{
    "body": "The tests should be indented, and you should only have \"::\" only on the last line before the test.\nThe patch now has\n\n```\n        TESTS::\n\n        Check that #5828 is solved::\n\n        sage: K.<w> = QuadraticField(-1)\n        sage: KX.<X> = K[]\n        sage: H.<h> = K.extension(X-1)\n        sage: H(w)\n        w\n```\n\nbut I think it should be\n\n```\n        TESTS:\n\n        Check that #5828 is solved::\n\n            sage: K.<w> = QuadraticField(-1)\n            sage: KX.<X> = K[]\n            sage: H.<h> = K.extension(X-1)\n            sage: H(w)\n            w\n```\n",
    "created_at": "2010-07-22T17:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5828#issuecomment-45819",
    "user": "mstreng"
}
```

The tests should be indented, and you should only have "::" only on the last line before the test.
The patch now has

```
        TESTS::

        Check that #5828 is solved::

        sage: K.<w> = QuadraticField(-1)
        sage: KX.<X> = K[]
        sage: H.<h> = K.extension(X-1)
        sage: H(w)
        w
```

but I think it should be

```
        TESTS:

        Check that #5828 is solved::

            sage: K.<w> = QuadraticField(-1)
            sage: KX.<X> = K[]
            sage: H.<h> = K.extension(X-1)
            sage: H(w)
            w
```




---

archive/issue_comments_045820.json:
```json
{
    "body": "Changing priority from critical to minor.",
    "created_at": "2010-07-22T17:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5828#issuecomment-45820",
    "user": "mstreng"
}
```

Changing priority from critical to minor.



---

archive/issue_comments_045821.json:
```json
{
    "body": "Attachment [trac_5828_already_solved.patch](tarball://root/attachments/some-uuid/ticket5828/trac_5828_already_solved.patch) by lftabera created at 2010-07-26 12:52:15\n\nYou are right, \n\nI have updated the patch accordingly.\n\nThanks",
    "created_at": "2010-07-26T12:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5828#issuecomment-45821",
    "user": "lftabera"
}
```

Attachment [trac_5828_already_solved.patch](tarball://root/attachments/some-uuid/ticket5828/trac_5828_already_solved.patch) by lftabera created at 2010-07-26 12:52:15

You are right, 

I have updated the patch accordingly.

Thanks



---

archive/issue_comments_045822.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-26T12:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5828#issuecomment-45822",
    "user": "lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_045823.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-31T13:29:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5828#issuecomment-45823",
    "user": "mstreng"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_045824.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:41:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5828#issuecomment-45824",
    "user": "mpatel"
}
```

Resolution: fixed
