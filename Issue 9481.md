# Issue 9481: random_element fails for power series over real field, has inaccurate docstring

archive/issues_009481.json:
```json
{
    "body": "Assignee: malb\n\nCC:  rishi\n\nKeywords: power series, random element\n\nThe random_element method of univariate power series does not pass arguments to the underlying polynomial ring accurately, and the description of its second argument is inaccurate.\n\nc.f. this [thread](http://groups.google.com/group/sage-devel/browse_thread/thread/2e4af4234e6bb33f) from sage-devel\n\n\n\n```\nsage: SQ = PowerSeriesRing(QQ,'v')\nsage: SR = PowerSeriesRing(RR,'v')\n\nsage: SQ.random_element(5,100)  # docstring promises coefficients are uniformly distributed between -100 and 100\n-7/3 + 5/8*v + 37/60*v^2 + 33/8*v^3 + 77/89*v^4 + O(v^5)\n\nsage: SR.random_element(5)  # broken\nTraceback (most recent call last):\n...\nTypeError: unsupported operand type(s) for -: 'int' and 'NoneType'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9481\n\n",
    "created_at": "2010-07-12T13:37:14Z",
    "labels": [
        "commutative algebra",
        "minor",
        "bug"
    ],
    "title": "random_element fails for power series over real field, has inaccurate docstring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9481",
    "user": "niles"
}
```
Assignee: malb

CC:  rishi

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

archive/issue_comments_091021.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2010-07-12T14:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91021",
    "user": "niles"
}
```

Changing priority from minor to major.



---

archive/issue_comments_091022.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-12T14:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91022",
    "user": "niles"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091023.json:
```json
{
    "body": "emulated behavior of polynomial ring random_element, as suggested on sage-devel; commit message now references ticket number",
    "created_at": "2010-08-01T16:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91023",
    "user": "niles"
}
```

emulated behavior of polynomial ring random_element, as suggested on sage-devel; commit message now references ticket number



---

archive/issue_comments_091024.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-08T02:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91024",
    "user": "rishi"
}
```

Attachment



---

archive/issue_comments_091025.json:
```json
{
    "body": "Changing keywords from \"power series, random element\" to \"power series, random element, beginner\".",
    "created_at": "2010-12-03T20:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91025",
    "user": "niles"
}
```

Changing keywords from "power series, random element" to "power series, random element, beginner".



---

archive/issue_comments_091026.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-10T22:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91026",
    "user": "aly.deines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091027.json:
```json
{
    "body": "Looks good.",
    "created_at": "2011-01-10T22:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91027",
    "user": "aly.deines"
}
```

Looks good.



---

archive/issue_comments_091028.json:
```json
{
    "body": "Attachment\n\nSame patch, fixed commit message",
    "created_at": "2011-01-19T02:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91028",
    "user": "jdemeyer"
}
```

Attachment

Same patch, fixed commit message



---

archive/issue_comments_091029.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-19T13:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91029",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_091030.json:
```json
{
    "body": "Docstring needs reformatting to proper Sphinx markup.",
    "created_at": "2011-01-19T13:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91030",
    "user": "jdemeyer"
}
```

Docstring needs reformatting to proper Sphinx markup.



---

archive/issue_comments_091031.json:
```json
{
    "body": "Apply on top of previous patch",
    "created_at": "2011-01-19T13:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91031",
    "user": "jdemeyer"
}
```

Apply on top of previous patch



---

archive/issue_comments_091032.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-19T13:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91032",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_091033.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-01-19T13:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91033",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_091034.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-19T13:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91034",
    "user": "niles"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091035.json:
```json
{
    "body": "All documentation now builds without error or warning, so positive review for [attachment:9481_docstring.patch]",
    "created_at": "2011-01-19T13:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91035",
    "user": "niles"
}
```

All documentation now builds without error or warning, so positive review for [attachment:9481_docstring.patch]



---

archive/issue_comments_091036.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9481#issuecomment-91036",
    "user": "jdemeyer"
}
```

Resolution: fixed
