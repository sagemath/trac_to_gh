# Issue 9633: binomial does not accept float

archive/issues_009633.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @kcrisman\n\n```\nsage: binomial(0.5r,5)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call\nlast)\n\n/home/bo198214/projects/<ipython console> in <module>()\n\n/opt/sage-4.5-linux-32bit-ubuntu_10.04_lts-i686-Linux/local/lib/\npython2.6/site-packages/sage/rings/arith.pyc in binomial(x, m)\n   2887     if isinstance(x, (float, sage.rings.real_mpfr.RealNumber,\n   2888                       sage.rings.real_mpfr.RealLiteral)):\n-> 2889         P = x.parent()\n   2890         if m < 0:\n   2891             return P(0)\n\nAttributeError: 'float' object has no attribute 'parent' \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9633\n\n",
    "closed_at": "2011-05-03T12:28:45Z",
    "created_at": "2010-07-29T07:23:07Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "binomial does not accept float",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9633",
    "user": "https://trac.sagemath.org/admin/accounts/users/Henryk.Trappmann"
}
```
Assignee: @aghitza

CC:  @kcrisman

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

archive/issue_comments_093203.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-04-11T20:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93203",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093204.json:
```json
{
    "body": "Two points: (1) I think \"P = parent(x)\" is simpler, if I'm reading sage.structure.parent correctly.  (2) Doctest? `:^)`",
    "created_at": "2011-04-12T06:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93204",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

Two points: (1) I think "P = parent(x)" is simpler, if I'm reading sage.structure.parent correctly.  (2) Doctest? `:^)`



---

archive/issue_comments_093205.json:
```json
{
    "body": "Attachment [trac_9633_binomial_float.patch](tarball://root/attachments/some-uuid/ticket9633/trac_9633_binomial_float.patch) by johanbosman created at 2011-04-12 09:08:25",
    "created_at": "2011-04-12T09:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93205",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```

Attachment [trac_9633_binomial_float.patch](tarball://root/attachments/some-uuid/ticket9633/trac_9633_binomial_float.patch) by johanbosman created at 2011-04-12 09:08:25



---

archive/issue_comments_093206.json:
```json
{
    "body": "Good points. :).",
    "created_at": "2011-04-12T09:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93206",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```

Good points. :).



---

archive/issue_comments_093207.json:
```json
{
    "body": "Certainly looks good!   Interesting that we didn't catch that when we put it in, even though it explicitly has 'float' in the previous version :( \n\nCurrently running tests in case there was something subtle about `x.parent()` that was different from `parent(x)`, though I can't see what that would be ...",
    "created_at": "2011-04-25T15:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93207",
    "user": "https://github.com/kcrisman"
}
```

Certainly looks good!   Interesting that we didn't catch that when we put it in, even though it explicitly has 'float' in the previous version :( 

Currently running tests in case there was something subtle about `x.parent()` that was different from `parent(x)`, though I can't see what that would be ...



---

archive/issue_comments_093208.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-25T16:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93208",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_024018.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2011-04-25T16:41:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9633#event-24018"
}
```



---

archive/issue_comments_093209.json:
```json
{
    "body": "Pass :)  Good catch.",
    "created_at": "2011-04-25T16:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93209",
    "user": "https://github.com/kcrisman"
}
```

Pass :)  Good catch.



---

archive/issue_events_024019.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-03T12:28:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9633#event-24019"
}
```



---

archive/issue_comments_093210.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-03T12:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9633#issuecomment-93210",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
