# Issue 2474: RealIntervalField should have a round method (maybe ComplexIntervalField should too)

archive/issues_002474.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  ncalexan\n\nKeywords: RIF CIF RealIntervalField ComplexIntervalField round\n\n\n```\nsage: round(RIF(10))\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/ncalexan/sage-2.10.3.rc3/<ipython console> in <module>()\n\n/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/misc/functional.py in round(x, ndigits)\n    864     else:\n    865         try: return x.round()\n--> 866         except AttributeError: return RealDoubleElement(__builtin__.round(x, 0))\n    867 \n    868 def quotient(x, y, *args, **kwds):\n\n<type 'exceptions.TypeError'>: a float is required\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2474\n\n",
    "created_at": "2008-03-11T22:09:18Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "RealIntervalField should have a round method (maybe ComplexIntervalField should too)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2474",
    "user": "ncalexan"
}
```
Assignee: somebody

CC:  ncalexan

Keywords: RIF CIF RealIntervalField ComplexIntervalField round


```
sage: round(RIF(10))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/ncalexan/sage-2.10.3.rc3/<ipython console> in <module>()

/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/misc/functional.py in round(x, ndigits)
    864     else:
    865         try: return x.round()
--> 866         except AttributeError: return RealDoubleElement(__builtin__.round(x, 0))
    867 
    868 def quotient(x, y, *args, **kwds):

<type 'exceptions.TypeError'>: a float is required
```


Issue created by migration from https://trac.sagemath.org/ticket/2474





---

archive/issue_comments_016753.json:
```json
{
    "body": "But what should it return?  In particular, what should round(RIF(1.5, 12345.678)) return, and why?\n\nMy vote is that RIF should not have a round method, since I can't think of a definition that's sensible and useful.",
    "created_at": "2008-03-12T01:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16753",
    "user": "cwitty"
}
```

But what should it return?  In particular, what should round(RIF(1.5, 12345.678)) return, and why?

My vote is that RIF should not have a round method, since I can't think of a definition that's sensible and useful.



---

archive/issue_comments_016754.json:
```json
{
    "body": "This now exists, with some definition.",
    "created_at": "2017-09-13T19:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16754",
    "user": "chapoton"
}
```

This now exists, with some definition.



---

archive/issue_comments_016755.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-09-13T19:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16755",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_016756.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-09-15T08:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16756",
    "user": "vdelecroix"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_016757.json:
```json
{
    "body": "Indeed!",
    "created_at": "2017-09-15T08:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16757",
    "user": "vdelecroix"
}
```

Indeed!



---

archive/issue_comments_016758.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-12-12T08:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16758",
    "user": "embray"
}
```

Resolution: wontfix



---

archive/issue_comments_016759.json:
```json
{
    "body": "I wonder why \"wontfix\" since this now seems to work:\n\n```\nsage: sage.rings.real_mpfi.printing_style = 'brackets'\nsage: round(RIF(1.5, 12345.678)) \n[2.0000000000000000 .. 12346.000000000000]\n```\n",
    "created_at": "2017-12-12T09:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16759",
    "user": "zimmerma"
}
```

I wonder why "wontfix" since this now seems to work:

```
sage: sage.rings.real_mpfi.printing_style = 'brackets'
sage: round(RIF(1.5, 12345.678)) 
[2.0000000000000000 .. 12346.000000000000]
```




---

archive/issue_comments_016760.json:
```json
{
    "body": "It was a batch edit; it doesn't make a lot of difference either way but I suppose \"worksforme\" would be more appropriate (but \"wontfix\" could also be read as \"won't fix because it's already fixed\" :)",
    "created_at": "2017-12-12T13:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16760",
    "user": "embray"
}
```

It was a batch edit; it doesn't make a lot of difference either way but I suppose "worksforme" would be more appropriate (but "wontfix" could also be read as "won't fix because it's already fixed" :)



---

archive/issue_comments_016761.json:
```json
{
    "body": "Resolution changed from wontfix to worksforme",
    "created_at": "2017-12-12T13:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2474#issuecomment-16761",
    "user": "embray"
}
```

Resolution changed from wontfix to worksforme
