# Issue 9466: square root with all=True should not return ValueError but empty list

archive/issues_009466.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  mderickx ruckers\n\n\n```\nsage: FiniteField(3)(2).sqrt(all = True)\n[]\n\nsage: 2.sqrt(extend = False, all = True)\nValueError: square root of 2 not an integer\n\nsage: FiniteField(next_prime(2^100))(2).sqrt(extend = False, all = True)\nValueError: self must be a square\n\nsage: _.<a>=FiniteField(9)\nsage: a.sqrt(extend = False, all = True)\nValueError: must be a perfect square.\n```\n\n\nAt sage days 23 we agreed that square root with all=True should not raise an error. If no square roots exist, then it should return an empty list.\n\nRight now, it returns an empty list for elements of small prime finite fields, but raises an error for integers, elements of large prime finite fields, and elements of non-prime finite fields.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9466\n\n",
    "created_at": "2010-07-09T13:18:25Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "square root with all=True should not return ValueError but empty list",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9466",
    "user": "mstreng"
}
```
Assignee: AlexGhitza

CC:  mderickx ruckers


```
sage: FiniteField(3)(2).sqrt(all = True)
[]

sage: 2.sqrt(extend = False, all = True)
ValueError: square root of 2 not an integer

sage: FiniteField(next_prime(2^100))(2).sqrt(extend = False, all = True)
ValueError: self must be a square

sage: _.<a>=FiniteField(9)
sage: a.sqrt(extend = False, all = True)
ValueError: must be a perfect square.
```


At sage days 23 we agreed that square root with all=True should not raise an error. If no square roots exist, then it should return an empty list.

Right now, it returns an empty list for elements of small prime finite fields, but raises an error for integers, elements of large prime finite fields, and elements of non-prime finite fields.

Issue created by migration from https://trac.sagemath.org/ticket/9466





---

archive/issue_comments_090795.json:
```json
{
    "body": "Fixes the code:   sage: 2.sqrt(extend = False, all = True)",
    "created_at": "2012-02-08T05:08:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9466#issuecomment-90795",
    "user": "ruckers"
}
```

Fixes the code:   sage: 2.sqrt(extend = False, all = True)



---

archive/issue_comments_090796.json:
```json
{
    "body": "Attachment\n\nFixes the code:  sage: FiniteField(next_prime(2^100))(2).sqrt(extend = False, all = True)",
    "created_at": "2012-02-08T05:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9466#issuecomment-90796",
    "user": "ruckers"
}
```

Attachment

Fixes the code:  sage: FiniteField(next_prime(2^100))(2).sqrt(extend = False, all = True)



---

archive/issue_comments_090797.json:
```json
{
    "body": "I was not able to fix this code.\n\nsage: _.<a>=FiniteField(9)\n\nsage: a.sqrt(extend = False, all = True)\n\nValueError: must be a perfect square.",
    "created_at": "2012-02-08T05:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9466#issuecomment-90797",
    "user": "ruckers"
}
```

I was not able to fix this code.

sage: _.<a>=FiniteField(9)

sage: a.sqrt(extend = False, all = True)

ValueError: must be a perfect square.



---

archive/issue_comments_090798.json:
```json
{
    "body": "Thanks! That bug has been around for too long :)\n\nWhy were you not able to fix the `FiniteField(9)` case?\n\nUnfortunately, the patches need some more work, for the following three reasons.\n* With my2.patch:\n  {{{\n  sage: Zmod(7)(3).sqrt(extend=True)\n  sqrt3\n  sage: Zmod(7)(3).sqrt(all=True, extend=True)\n  []\n  }}}\n  The second one should either output `[sqrt3, -sqrt3]` or raise `NotImplementedError`, but never an empty list.\n* Patches must have your name and email address in them. This is done by putting your email address and name in your `.hgrc` file as specified [here](http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change)\n* Add an example of the new functionality to the documentation:\n  * This helps the user understand what the function does.\n  * Through the doctesting framework, this prevents other people from accidentally breaking your added functionality.\n  * This is [required](http://www.sagemath.org/doc/developer/trac.html#reviewing-patches) for your patch to be able to get a positive review. In fact, the manual says that you should also mention the ticket number #9466 with your example.\n\nIf you have any questions, let me know!",
    "created_at": "2012-02-08T10:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9466#issuecomment-90798",
    "user": "mstreng"
}
```

Thanks! That bug has been around for too long :)

Why were you not able to fix the `FiniteField(9)` case?

Unfortunately, the patches need some more work, for the following three reasons.
* With my2.patch:
  {{{
  sage: Zmod(7)(3).sqrt(extend=True)
  sqrt3
  sage: Zmod(7)(3).sqrt(all=True, extend=True)
  []
  }}}
  The second one should either output `[sqrt3, -sqrt3]` or raise `NotImplementedError`, but never an empty list.
* Patches must have your name and email address in them. This is done by putting your email address and name in your `.hgrc` file as specified [here](http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change)
* Add an example of the new functionality to the documentation:
  * This helps the user understand what the function does.
  * Through the doctesting framework, this prevents other people from accidentally breaking your added functionality.
  * This is [required](http://www.sagemath.org/doc/developer/trac.html#reviewing-patches) for your patch to be able to get a positive review. In fact, the manual says that you should also mention the ticket number #9466 with your example.

If you have any questions, let me know!



---

archive/issue_comments_090799.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-07-25T18:20:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9466#issuecomment-90799",
    "user": "mstreng"
}
```

Attachment



---

archive/issue_comments_090800.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-07-25T18:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9466#issuecomment-90800",
    "user": "mstreng"
}
```

Attachment



---

archive/issue_comments_090801.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd23 sd51 sqrt all\".",
    "created_at": "2013-07-25T18:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9466#issuecomment-90801",
    "user": "mstreng"
}
```

Changing keywords from "" to "sd23 sd51 sqrt all".



---

archive/issue_comments_090802.json:
```json
{
    "body": "Attachment\n\nDoes anyone know who user \"ruckers\" is? (s)he should be added to the list of authors\n\napply 9466.patch",
    "created_at": "2013-07-25T18:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9466#issuecomment-90802",
    "user": "mstreng"
}
```

Attachment

Does anyone know who user "ruckers" is? (s)he should be added to the list of authors

apply 9466.patch



---

archive/issue_comments_090803.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-07-25T20:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9466#issuecomment-90803",
    "user": "mstreng"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090804.json:
```json
{
    "body": "please review!",
    "created_at": "2013-07-25T20:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9466#issuecomment-90804",
    "user": "mstreng"
}
```

please review!



---

archive/issue_comments_090805.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-07-26T10:04:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9466#issuecomment-90805",
    "user": "akoutsianas"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090806.json:
```json
{
    "body": "The patch passed all the tests for sage 5.11 version.",
    "created_at": "2013-07-26T10:04:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9466#issuecomment-90806",
    "user": "akoutsianas"
}
```

The patch passed all the tests for sage 5.11 version.



---

archive/issue_comments_090807.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-08-20T12:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9466#issuecomment-90807",
    "user": "jdemeyer"
}
```

Resolution: fixed
