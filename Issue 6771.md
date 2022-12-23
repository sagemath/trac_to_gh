# Issue 6771: speed up pynac --> polynomials conversion, since it is really slow

archive/issues_006771.json:
```json
{
    "body": "Assignee: burcin\n\n\n```\n> sage: var(\"x y z\")\n> (x, y, z)\n> sage: a = (x+y+z)**20\n> sage: b = a.expand()\n> sage: %time c = factor(b)\n> CPU times: user 0.14 s, sys: 0.00 s, total: 0.15 s\n> Wall time: 0.15 s\n>\n>\n> 1) it uses pari, right?\n\nNO.  Pari has no functionality at all for doing anything nontrivial with multivariate polynomials.    Do b.factor?? to see the source.  Sage tries to convert b to a poly over QQ, this works, then it calls SINGULAR to factor that.  If conversion doesn't work, it falls back to Maxima right now. \n\nAll the time is actually spent in converting b from Pynac to Singular:\n\nsage: timeit('c = b.polynomial(QQ)')\n5 loops, best of 3: 149 ms per loop\n\nIt is silly that this is slow.  I don't know why it is so slow. \n\nMike Hansen wrote some really beautiful-looking clever code in \n\nsage/symbolic/expression_conversions.py\n\nThe code that implements b.polynomial is some of this clever code.\nWhen I read that code (when refereeing the symbolic switch), I think \"wow, this is beautiful, it is so simple to read/understand, it is short. Wow.  I bet this is going to be really slow...\"     Well, evidently it is really slow.   Somebody should do some profiling and speed this up -- a factor of 100 should be easily obtained. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6771\n\n",
    "created_at": "2009-08-17T08:22:42Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "speed up pynac --> polynomials conversion, since it is really slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6771",
    "user": "was"
}
```
Assignee: burcin


```
> sage: var("x y z")
> (x, y, z)
> sage: a = (x+y+z)**20
> sage: b = a.expand()
> sage: %time c = factor(b)
> CPU times: user 0.14 s, sys: 0.00 s, total: 0.15 s
> Wall time: 0.15 s
>
>
> 1) it uses pari, right?

NO.  Pari has no functionality at all for doing anything nontrivial with multivariate polynomials.    Do b.factor?? to see the source.  Sage tries to convert b to a poly over QQ, this works, then it calls SINGULAR to factor that.  If conversion doesn't work, it falls back to Maxima right now. 

All the time is actually spent in converting b from Pynac to Singular:

sage: timeit('c = b.polynomial(QQ)')
5 loops, best of 3: 149 ms per loop

It is silly that this is slow.  I don't know why it is so slow. 

Mike Hansen wrote some really beautiful-looking clever code in 

sage/symbolic/expression_conversions.py

The code that implements b.polynomial is some of this clever code.
When I read that code (when refereeing the symbolic switch), I think "wow, this is beautiful, it is so simple to read/understand, it is short. Wow.  I bet this is going to be really slow..."     Well, evidently it is really slow.   Somebody should do some profiling and speed this up -- a factor of 100 should be easily obtained. 
```


Issue created by migration from https://trac.sagemath.org/ticket/6771





---

archive/issue_comments_055751.json:
```json
{
    "body": "We should do this via the code in `normal.cpp` in pynac. The interface defined there for polynomial conversions is very clean, and can be used for expressions containing symbolic terms (sin(x), etc.), treating them as separate variables.",
    "created_at": "2009-08-17T10:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6771#issuecomment-55751",
    "user": "burcin"
}
```

We should do this via the code in `normal.cpp` in pynac. The interface defined there for polynomial conversions is very clean, and can be used for expressions containing symbolic terms (sin(x), etc.), treating them as separate variables.



---

archive/issue_comments_055752.json:
```json
{
    "body": "Can you give some hints about this, Burcin?    Where in normal.cpp - and how would we hook into it?",
    "created_at": "2011-02-16T21:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6771#issuecomment-55752",
    "user": "kcrisman"
}
```

Can you give some hints about this, Burcin?    Where in normal.cpp - and how would we hook into it?



---

archive/issue_comments_055753.json:
```json
{
    "body": "This has nothing to do with Pynac which is not called here. The most time intensive functions (via `sage.misc.gperftools`):\n\n```\nsage: t=((x+y+z)^400).polynomial(QQ)\n\n     267  14.7%  45.4%      267  14.7% _int_free\n     178   9.8%  56.5%      181  10.0% _int_malloc\n     128   7.1%  73.0%      128   7.1% mpn_add_n\n     124   6.8%   6.9%      899  49.6% p_Minus_mm_Mult_qq__FieldQ_LengthThree_OrdPosNomogPos\n     117   6.5%  63.1%      178   9.8% __GI___libc_malloc\n     117   6.5%  79.5%      117   6.5% mpn_copyi\n     114   6.3%  20.3%      397  21.9% __GI___libc_realloc\n      80   4.4%  12.4%      529  29.2% _nlMult_aNoImm_OR_bNoImm\n      66   3.6%  83.1%       68   3.8% __GI___libc_free\n\n```\n\nIn fact, Pynac is one order of magnitude faster:\n\n```\nsage: %time t=((x+y+z)^400).expand()\nCPU times: user 1.69 s, sys: 21 ms, total: 1.71 s\nWall time: 1.71 s\nsage: %time t=((x+y+z)^400).polynomial(QQ)\nCPU times: user 15.5 s, sys: 6 ms, total: 15.5 s\nWall time: 15.5 s\n```\n",
    "created_at": "2015-05-12T14:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6771#issuecomment-55753",
    "user": "rws"
}
```

This has nothing to do with Pynac which is not called here. The most time intensive functions (via `sage.misc.gperftools`):

```
sage: t=((x+y+z)^400).polynomial(QQ)

     267  14.7%  45.4%      267  14.7% _int_free
     178   9.8%  56.5%      181  10.0% _int_malloc
     128   7.1%  73.0%      128   7.1% mpn_add_n
     124   6.8%   6.9%      899  49.6% p_Minus_mm_Mult_qq__FieldQ_LengthThree_OrdPosNomogPos
     117   6.5%  63.1%      178   9.8% __GI___libc_malloc
     117   6.5%  79.5%      117   6.5% mpn_copyi
     114   6.3%  20.3%      397  21.9% __GI___libc_realloc
      80   4.4%  12.4%      529  29.2% _nlMult_aNoImm_OR_bNoImm
      66   3.6%  83.1%       68   3.8% __GI___libc_free

```

In fact, Pynac is one order of magnitude faster:

```
sage: %time t=((x+y+z)^400).expand()
CPU times: user 1.69 s, sys: 21 ms, total: 1.71 s
Wall time: 1.71 s
sage: %time t=((x+y+z)^400).polynomial(QQ)
CPU times: user 15.5 s, sys: 6 ms, total: 15.5 s
Wall time: 15.5 s
```




---

archive/issue_comments_055754.json:
```json
{
    "body": "Changing component from calculus to commutative algebra.",
    "created_at": "2015-05-12T14:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6771#issuecomment-55754",
    "user": "rws"
}
```

Changing component from calculus to commutative algebra.



---

archive/issue_comments_055755.json:
```json
{
    "body": "Changing assignee from burcin to malb.",
    "created_at": "2015-05-12T14:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6771#issuecomment-55755",
    "user": "rws"
}
```

Changing assignee from burcin to malb.



---

archive/issue_comments_055756.json:
```json
{
    "body": "Why does this button keep changing?...",
    "created_at": "2015-05-12T15:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6771#issuecomment-55756",
    "user": "rws"
}
```

Why does this button keep changing?...



---

archive/issue_comments_055757.json:
```json
{
    "body": "Remove assignee malb.",
    "created_at": "2015-05-12T15:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6771#issuecomment-55757",
    "user": "rws"
}
```

Remove assignee malb.
