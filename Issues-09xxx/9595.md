# Issue 9595: Conversion from constant PARI polynomials to QQ doesn't work

archive/issues_009595.json:
```json
{
    "body": "Assignee: @robertwb\n\nWe create a constant PARI polynomial with value 1/2 and coerce it to QQ:\n\n```\nsage: constpol = pari('Pol([1/2])')\nsage: QQ(constpol)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/usr/local/src/sage-4.5.2.alpha0/<ipython console> in <module>()\n\n/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()\n\n/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()\n\n/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()\n\n/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)()\n\n/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:6853)()\n\n/usr/local/src/sage-4.5.2.alpha0/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6285)()\n\nTypeError: Unable to coerce PARI 1/2 to an Integer.\n```\n\nNote how the error message indicated conversion to Integer somehow.  Indeed, `QQ(pari('Pol([1])'))` works\n\nIssue created by migration from https://trac.sagemath.org/ticket/9595\n\n",
    "closed_at": "2010-08-09T09:47:37Z",
    "created_at": "2010-07-25T12:03:14Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Conversion from constant PARI polynomials to QQ doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9595",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: @robertwb

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

archive/issue_comments_092680.json:
```json
{
    "body": "Attachment [9595.patch](tarball://root/attachments/some-uuid/ticket9595/9595.patch) by @jdemeyer created at 2010-07-25 12:37:05",
    "created_at": "2010-07-25T12:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9595#issuecomment-92680",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9595.patch](tarball://root/attachments/some-uuid/ticket9595/9595.patch) by @jdemeyer created at 2010-07-25 12:37:05



---

archive/issue_comments_092681.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-25T12:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9595#issuecomment-92681",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_events_023896.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-07-29T14:46:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9595",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9595#event-23896"
}
```



---

archive/issue_comments_092682.json:
```json
{
    "body": "Patch looks good and applies fine to 4.5.1.  Runnng a full test on 32-bit now.",
    "created_at": "2010-07-31T18:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9595#issuecomment-92682",
    "user": "https://github.com/JohnCremona"
}
```

Patch looks good and applies fine to 4.5.1.  Runnng a full test on 32-bit now.



---

archive/issue_comments_092683.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-01T21:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9595#issuecomment-92683",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092684.json:
```json
{
    "body": "Full long test worked fine.",
    "created_at": "2010-08-01T21:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9595#issuecomment-92684",
    "user": "https://github.com/JohnCremona"
}
```

Full long test worked fine.



---

archive/issue_comments_092685.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9595#issuecomment-92685",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_023897.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-09T09:47:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9595",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9595#event-23897"
}
```
