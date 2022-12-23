# Issue 9627: converting from symbolic ring to int is broken,

archive/issues_009627.json:
```json
{
    "body": "Assignee: robertwb\n\nCC:  katestange mjo\n\nHere is simple example:\n\n```\nsage: h = 3^64;\nsage: int(h)==int(SR(h))\nFALSE\n```\n\nLooking a bit deeper into this, it seems that the first 100 bits are correct, and after that int(SR(h)) is just zeroes. (As a side note, the conversion to ZZ works without a problem.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9627\n\n",
    "created_at": "2010-07-28T20:33:03Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "title": "converting from symbolic ring to int is broken,",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9627",
    "user": "syazdani"
}
```
Assignee: robertwb

CC:  katestange mjo

Here is simple example:

```
sage: h = 3^64;
sage: int(h)==int(SR(h))
FALSE
```

Looking a bit deeper into this, it seems that the first 100 bits are correct, and after that int(SR(h)) is just zeroes. (As a side note, the conversion to ZZ works without a problem.)


Issue created by migration from https://trac.sagemath.org/ticket/9627





---

archive/issue_comments_093299.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-28T21:01:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9627#issuecomment-93299",
    "user": "tornaria"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_093300.json:
```json
{
    "body": "Yikes!\n\n```\n    def __int__(self):\n        \"\"\"\n        EXAMPLES::\n        \n            sage: int(sin(2)*100)\n            90\n            sage: int(log(8)/log(2))\n            3\n        \"\"\"\n        #FIXME: can we do better?\n        return int(self.n(prec=100))\n```\n\n\nCan we just change that to\n\n```\n        return int(self._integer_())\n```\n\n?",
    "created_at": "2010-07-28T21:01:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9627#issuecomment-93300",
    "user": "tornaria"
}
```

Yikes!

```
    def __int__(self):
        """
        EXAMPLES::
        
            sage: int(sin(2)*100)
            90
            sage: int(log(8)/log(2))
            3
        """
        #FIXME: can we do better?
        return int(self.n(prec=100))
```


Can we just change that to

```
        return int(self._integer_())
```

?



---

archive/issue_comments_093301.json:
```json
{
    "body": "OTOH,\n\n```\nsage: ZZ(log(8)/log(2))\n...\nTypeError: unable to convert x (=log(8)/log(2)) to an integer\n```\n\nbut\n\n```\nsage: int(log(8)/log(2))  \n3\n```\n\n\nOTOH, `int(sin(2)*100)` is not equal to 90... not an integer anyway... What's the expected meaning of `int(x)`?",
    "created_at": "2010-07-28T21:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9627#issuecomment-93301",
    "user": "tornaria"
}
```

OTOH,

```
sage: ZZ(log(8)/log(2))
...
TypeError: unable to convert x (=log(8)/log(2)) to an integer
```

but

```
sage: int(log(8)/log(2))  
3
```


OTOH, `int(sin(2)*100)` is not equal to 90... not an integer anyway... What's the expected meaning of `int(x)`?



---

archive/issue_comments_093302.json:
```json
{
    "body": "Changing component from coercion to symbolics.",
    "created_at": "2010-07-28T21:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9627#issuecomment-93302",
    "user": "tornaria"
}
```

Changing component from coercion to symbolics.



---

archive/issue_comments_093303.json:
```json
{
    "body": "Pure Python implements int() of a float as truncating toward zero:\n\n```\n>>> int(3.14159)\n3\n>>> int(-3.14159)\n-3\n>>> int(2.71828)\n2\n>>> int(-2.71828)\n-2\n```\n\nI think in general we've implemented int() on real numbers of various types as truncating toward zero to follow this precedent.",
    "created_at": "2010-08-03T00:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9627#issuecomment-93303",
    "user": "cwitty"
}
```

Pure Python implements int() of a float as truncating toward zero:

```
>>> int(3.14159)
3
>>> int(-3.14159)
-3
>>> int(2.71828)
2
>>> int(-2.71828)
-2
```

I think in general we've implemented int() on real numbers of various types as truncating toward zero to follow this precedent.



---

archive/issue_comments_093304.json:
```json
{
    "body": "Something like this may work:\n\n```\ndef SR_int(x):\n    \"\"\"\n    sage: SR_int(sin(2)*100)\n    90\n    sage: SR_int(-sin(2)*100)\n    -90\n    sage: SR_int(log(8)/log(2))\n    3\n    sage: SR_int(-log(8)/log(2))\n    -3\n    sage: SR_int(SR(3^64)) == 3^64\n    True\n    sage: SR_int(SR(10^100)) == 10^100\n    True\n    sage: SR_int(SR(10^100+10^-100)) == 10^100\n    True\n    sage: SR_int(SR(10^100-10^-100)) == 10^100 - 1\n    True\n\n    sage: SR_int(sqrt(-1))\n    ...\n    ValueError: math domain error\n    sage: SR_int(x)\n    ...\n    ValueError: math domain error\n    \"\"\"\n    try:\n        if x in RR:\n            ## truncate toward zero\n            y = floor(abs(x))\n            if parent(y) is ZZ:\n                return int(ZZ(sign(x) * y))\n    except:\n        pass\n    raise ValueError, \"math domain error\"\n```\n\n\nNote that `floor(log(8)/log(2))` takes about 1s to complete, which means `SR_int(log(8)/log(2))` is waaay slower than `int(log(8)/log(2)`. But this is at the cost of `int(x)` being incorrect when `x` is very close to an integer (cf. `int(SR(10<sup>20-10</sup>-20))`).\n\nOTOH, `(log(8)/log(2)).full_simplify()` takes 35ms to give `3`, so it may be worth revisiting the `floor()` strategy. Opens a can of worms, I guess...\n\n----\n\nI won't turn the snippet above into a patch, if somebody likes it and wants to produce a patch, go ahead.",
    "created_at": "2010-08-03T01:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9627#issuecomment-93304",
    "user": "tornaria"
}
```

Something like this may work:

```
def SR_int(x):
    """
    sage: SR_int(sin(2)*100)
    90
    sage: SR_int(-sin(2)*100)
    -90
    sage: SR_int(log(8)/log(2))
    3
    sage: SR_int(-log(8)/log(2))
    -3
    sage: SR_int(SR(3^64)) == 3^64
    True
    sage: SR_int(SR(10^100)) == 10^100
    True
    sage: SR_int(SR(10^100+10^-100)) == 10^100
    True
    sage: SR_int(SR(10^100-10^-100)) == 10^100 - 1
    True

    sage: SR_int(sqrt(-1))
    ...
    ValueError: math domain error
    sage: SR_int(x)
    ...
    ValueError: math domain error
    """
    try:
        if x in RR:
            ## truncate toward zero
            y = floor(abs(x))
            if parent(y) is ZZ:
                return int(ZZ(sign(x) * y))
    except:
        pass
    raise ValueError, "math domain error"
```


Note that `floor(log(8)/log(2))` takes about 1s to complete, which means `SR_int(log(8)/log(2))` is waaay slower than `int(log(8)/log(2)`. But this is at the cost of `int(x)` being incorrect when `x` is very close to an integer (cf. `int(SR(10<sup>20-10</sup>-20))`).

OTOH, `(log(8)/log(2)).full_simplify()` takes 35ms to give `3`, so it may be worth revisiting the `floor()` strategy. Opens a can of worms, I guess...

----

I won't turn the snippet above into a patch, if somebody likes it and wants to produce a patch, go ahead.



---

archive/issue_comments_093305.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-05-22T22:41:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9627#issuecomment-93305",
    "user": "burcin"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_093306.json:
```json
{
    "body": "#12968 has a patch with a positive review which fixes this. We should close this as a duplicate.",
    "created_at": "2012-05-22T22:41:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9627#issuecomment-93306",
    "user": "burcin"
}
```

#12968 has a patch with a positive review which fixes this. We should close this as a duplicate.



---

archive/issue_comments_093307.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-06-19T13:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9627#issuecomment-93307",
    "user": "jdemeyer"
}
```

Resolution: duplicate
