# Issue 9481: random_element fails for power series over real field, has inaccurate docstring

archive/issues_009481.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @rishikesha\n\nKeywords: power series, random element\n\nThe random_element method of univariate power series does not pass arguments to the underlying polynomial ring accurately, and the description of its second argument is inaccurate.\n\nc.f. this [thread](http://groups.google.com/group/sage-devel/browse_thread/thread/2e4af4234e6bb33f) from sage-devel\n\n\n\n```\nsage: SQ = PowerSeriesRing(QQ,'v')\nsage: SR = PowerSeriesRing(RR,'v')\n\nsage: SQ.random_element(5,100)  # docstring promises coefficients are uniformly distributed between -100 and 100\n-7/3 + 5/8*v + 37/60*v^2 + 33/8*v^3 + 77/89*v^4 + O(v^5)\n\nsage: SR.random_element(5)  # broken\nTraceback (most recent call last):\n...\nTypeError: unsupported operand type(s) for -: 'int' and 'NoneType'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9481\n\n",
    "created_at": "2010-07-12T13:37:14Z",
    "labels": [
        "component: commutative algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "random_element fails for power series over real field, has inaccurate docstring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9481",
    "user": "https://github.com/nilesjohnson"
}
```
Assignee: @malb

CC:  @rishikesha

Keywords: power series, random element

The random_element method of univariate power series does not pass arguments to the underlying polynomial ring accurately, and the description of its second argument is inaccurate.

c.f. this [thread](http://groups.google.com/group/sage-devel/browse_thread/thread/2e4af4234e6bb33f) from sage-devel



```
sage: SQ = PowerSeriesRing(QQ,'v')
sage: SR = PowerSeriesRing(RR,'v')

sage: SQ.random_element(5,100)  # docstring promises coefficients are uniformly distributed between -100 and 100
-7/3 + 5/8*v + 37/60*v^2 + 33/8*v^3 + 77/89*v^4 + O(v^5)

sage: SR.random_element(5)  # broken
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for -: 'int' and 'NoneType'
```


Issue created by migration from https://trac.sagemath.org/ticket/9481





---

archive/issue_comments_090869.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-12T14:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90869",
    "user": "https://github.com/nilesjohnson"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090870.json:
```json
{
    "body": "emulated behavior of polynomial ring random_element, as suggested on sage-devel; commit message now references ticket number",
    "created_at": "2010-08-01T16:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90870",
    "user": "https://github.com/nilesjohnson"
}
```

emulated behavior of polynomial ring random_element, as suggested on sage-devel; commit message now references ticket number



---

archive/issue_comments_090871.json:
```json
{
    "body": "Attachment [trac_9481_ps_random_element.patch](tarball://root/attachments/some-uuid/ticket9481/trac_9481_ps_random_element.patch) by @rishikesha created at 2010-08-08 02:52:29",
    "created_at": "2010-08-08T02:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90871",
    "user": "https://github.com/rishikesha"
}
```

Attachment [trac_9481_ps_random_element.patch](tarball://root/attachments/some-uuid/ticket9481/trac_9481_ps_random_element.patch) by @rishikesha created at 2010-08-08 02:52:29



---

archive/issue_comments_090872.json:
```json
{
    "body": "Changing keywords from \"power series, random element\" to \"power series, random element, beginner\".",
    "created_at": "2010-12-03T20:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90872",
    "user": "https://github.com/nilesjohnson"
}
```

Changing keywords from "power series, random element" to "power series, random element, beginner".



---

archive/issue_comments_090873.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-10T22:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90873",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090874.json:
```json
{
    "body": "Looks good.",
    "created_at": "2011-01-10T22:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90874",
    "user": "https://github.com/adeines"
}
```

Looks good.



---

archive/issue_events_023507.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-11T06:02:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9481#event-23507"
}
```



---

archive/issue_comments_090875.json:
```json
{
    "body": "Attachment [trac_9481_ps_random_element.2.patch](tarball://root/attachments/some-uuid/ticket9481/trac_9481_ps_random_element.2.patch) by @jdemeyer created at 2011-01-19 02:00:19\n\nSame patch, fixed commit message",
    "created_at": "2011-01-19T02:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90875",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [trac_9481_ps_random_element.2.patch](tarball://root/attachments/some-uuid/ticket9481/trac_9481_ps_random_element.2.patch) by @jdemeyer created at 2011-01-19 02:00:19

Same patch, fixed commit message



---

archive/issue_comments_090876.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-19T13:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90876",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_090877.json:
```json
{
    "body": "Docstring needs reformatting to proper Sphinx markup.",
    "created_at": "2011-01-19T13:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90877",
    "user": "https://github.com/jdemeyer"
}
```

Docstring needs reformatting to proper Sphinx markup.



---

archive/issue_comments_090878.json:
```json
{
    "body": "Apply on top of previous patch",
    "created_at": "2011-01-19T13:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90878",
    "user": "https://github.com/jdemeyer"
}
```

Apply on top of previous patch



---

archive/issue_comments_090879.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-19T13:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90879",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090880.json:
```json
{
    "body": "Attachment [9481_docstring.patch](tarball://root/attachments/some-uuid/ticket9481/9481_docstring.patch) by @jdemeyer created at 2011-01-19 13:30:47",
    "created_at": "2011-01-19T13:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90880",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9481_docstring.patch](tarball://root/attachments/some-uuid/ticket9481/9481_docstring.patch) by @jdemeyer created at 2011-01-19 13:30:47



---

archive/issue_comments_090881.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-19T13:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90881",
    "user": "https://github.com/nilesjohnson"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090882.json:
```json
{
    "body": "All documentation now builds without error or warning, so positive review for [attachment:9481_docstring.patch]",
    "created_at": "2011-01-19T13:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90882",
    "user": "https://github.com/nilesjohnson"
}
```

All documentation now builds without error or warning, so positive review for [attachment:9481_docstring.patch]



---

archive/issue_events_023508.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-19T22:21:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9481#event-23508"
}
```



---

archive/issue_comments_090883.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-90883",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
