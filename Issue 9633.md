# Issue 9633: binomial does not accept float

archive/issues_009633.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  kcrisman\n\n\n```\nsage: binomial(0.5r,5)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call\nlast)\n\n/home/bo198214/projects/<ipython console> in <module>()\n\n/opt/sage-4.5-linux-32bit-ubuntu_10.04_lts-i686-Linux/local/lib/\npython2.6/site-packages/sage/rings/arith.pyc in binomial(x, m)\n   2887     if isinstance(x, (float, sage.rings.real_mpfr.RealNumber,\n   2888                       sage.rings.real_mpfr.RealLiteral)):\n-> 2889         P = x.parent()\n   2890         if m < 0:\n   2891             return P(0)\n\nAttributeError: 'float' object has no attribute 'parent' \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9633\n\n",
    "created_at": "2010-07-29T07:23:07Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "binomial does not accept float",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9633",
    "user": "Henryk.Trappmann"
}
```
Assignee: AlexGhitza

CC:  kcrisman


```
sage: binomial(0.5r,5)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call
last)

/home/bo198214/projects/<ipython console> in <module>()

/opt/sage-4.5-linux-32bit-ubuntu_10.04_lts-i686-Linux/local/lib/
python2.6/site-packages/sage/rings/arith.pyc in binomial(x, m)
   2887     if isinstance(x, (float, sage.rings.real_mpfr.RealNumber,
   2888                       sage.rings.real_mpfr.RealLiteral)):
-> 2889         P = x.parent()
   2890         if m < 0:
   2891             return P(0)

AttributeError: 'float' object has no attribute 'parent' 
```



Issue created by migration from https://trac.sagemath.org/ticket/9633





---

archive/issue_comments_093359.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-04-11T20:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93359",
    "user": "johanbosman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093360.json:
```json
{
    "body": "Two points: (1) I think \"P = parent(x)\" is simpler, if I'm reading sage.structure.parent correctly.  (2) Doctest? `:^)`",
    "created_at": "2011-04-12T06:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93360",
    "user": "dsm"
}
```

Two points: (1) I think "P = parent(x)" is simpler, if I'm reading sage.structure.parent correctly.  (2) Doctest? `:^)`



---

archive/issue_comments_093361.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-04-12T09:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93361",
    "user": "johanbosman"
}
```

Attachment



---

archive/issue_comments_093362.json:
```json
{
    "body": "Good points. :).",
    "created_at": "2011-04-12T09:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93362",
    "user": "johanbosman"
}
```

Good points. :).



---

archive/issue_comments_093363.json:
```json
{
    "body": "Certainly looks good!   Interesting that we didn't catch that when we put it in, even though it explicitly has 'float' in the previous version :( \n\nCurrently running tests in case there was something subtle about `x.parent()` that was different from `parent(x)`, though I can't see what that would be ...",
    "created_at": "2011-04-25T15:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93363",
    "user": "kcrisman"
}
```

Certainly looks good!   Interesting that we didn't catch that when we put it in, even though it explicitly has 'float' in the previous version :( 

Currently running tests in case there was something subtle about `x.parent()` that was different from `parent(x)`, though I can't see what that would be ...



---

archive/issue_comments_093364.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-25T16:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93364",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093365.json:
```json
{
    "body": "Pass :)  Good catch.",
    "created_at": "2011-04-25T16:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93365",
    "user": "kcrisman"
}
```

Pass :)  Good catch.



---

archive/issue_comments_093366.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-03T12:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93366",
    "user": "jdemeyer"
}
```

Resolution: fixed
