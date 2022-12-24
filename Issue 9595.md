# Issue 9595: Conversion from constant PARI polynomials to QQ doesn't work

archive/issues_009595.json:
```json
{
    "body": "Assignee: robertwb\n\nWe create a constant PARI polynomial with value 1/2 and coerce it to QQ:\n\n```\nsage: constpol = pari('Pol([1/2])')\nsage: QQ(constpol)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/usr/local/src/sage-4.5.2.alpha0/<ipython console> in <module>()\n\n/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()\n\n/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()\n\n/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()\n\n/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)()\n\n/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:6853)()\n\n/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6285)()\n\nTypeError: Unable to coerce PARI 1/2 to an Integer.\n```\n\n\nNote how the error message indicated conversion to Integer somehow.  Indeed, `QQ(pari('Pol([1])'))` works\n\nIssue created by migration from https://trac.sagemath.org/ticket/9595\n\n",
    "created_at": "2010-07-25T12:03:14Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Conversion from constant PARI polynomials to QQ doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9595",
    "user": "jdemeyer"
}
```
Assignee: robertwb

We create a constant PARI polynomial with value 1/2 and coerce it to QQ:

```
sage: constpol = pari('Pol([1/2])')
sage: QQ(constpol)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/usr/local/src/sage-4.5.2.alpha0/<ipython console> in <module>()

/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()

/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)()

/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:6853)()

/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6285)()

TypeError: Unable to coerce PARI 1/2 to an Integer.
```


Note how the error message indicated conversion to Integer somehow.  Indeed, `QQ(pari('Pol([1])'))` works

Issue created by migration from https://trac.sagemath.org/ticket/9595





---

archive/issue_comments_092834.json:
```json
{
    "body": "Attachment [9595.patch](tarball://root/attachments/some-uuid/ticket9595/9595.patch) by jdemeyer created at 2010-07-25 12:37:05",
    "created_at": "2010-07-25T12:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9595#issuecomment-92834",
    "user": "jdemeyer"
}
```

Attachment [9595.patch](tarball://root/attachments/some-uuid/ticket9595/9595.patch) by jdemeyer created at 2010-07-25 12:37:05



---

archive/issue_comments_092835.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-25T12:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9595#issuecomment-92835",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092836.json:
```json
{
    "body": "Patch looks good and applies fine to 4.5.1.  Runnng a full test on 32-bit now.",
    "created_at": "2010-07-31T18:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9595#issuecomment-92836",
    "user": "cremona"
}
```

Patch looks good and applies fine to 4.5.1.  Runnng a full test on 32-bit now.



---

archive/issue_comments_092837.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-01T21:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9595#issuecomment-92837",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092838.json:
```json
{
    "body": "Full long test worked fine.",
    "created_at": "2010-08-01T21:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9595#issuecomment-92838",
    "user": "cremona"
}
```

Full long test worked fine.



---

archive/issue_comments_092839.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9595#issuecomment-92839",
    "user": "mpatel"
}
```

Resolution: fixed
