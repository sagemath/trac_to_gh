# Issue 6623: Memory leak when calling binomial

archive/issues_006623.json:
```json
{
    "body": "Keywords: binomial, leak\n\nThere appears to be a memory leak when repeatedly calling binomial with different parameters.  This sometimes also appears when the parameters to binomial are not varied, but is not consistent.  This is a problem for the Combinations rank code, which makes many repeated calls to binomial.\n\n\n```\nsage: import random\nprint get_memory_usage()\nfor i in xrange(100000):\n    x=random.randint(10,100)\n    y=random.randint(0,x)\n    r=binomial(x,y)\nprint get_memory_usage()\n\n730.6328125\n736.5625\n```\n\n\nThe output is from running the code in Sage 4.1 on sagenb.org.  I think the same problem may involve the symbolic backend and GiNaC, since the same problem also occurs with log.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6623\n\n",
    "created_at": "2009-07-26T01:41:23Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Memory leak when calling binomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6623",
    "user": "hartke"
}
```
Keywords: binomial, leak

There appears to be a memory leak when repeatedly calling binomial with different parameters.  This sometimes also appears when the parameters to binomial are not varied, but is not consistent.  This is a problem for the Combinations rank code, which makes many repeated calls to binomial.


```
sage: import random
print get_memory_usage()
for i in xrange(100000):
    x=random.randint(10,100)
    y=random.randint(0,x)
    r=binomial(x,y)
print get_memory_usage()

730.6328125
736.5625
```


The output is from running the code in Sage 4.1 on sagenb.org.  I think the same problem may involve the symbolic backend and GiNaC, since the same problem also occurs with log.

Issue created by migration from https://trac.sagemath.org/ticket/6623





---

archive/issue_comments_054261.json:
```json
{
    "body": "Perhaps Pari, or our wrapping of it, is the problem.  Do the same thing as above, but replace\n\n```\n    r=binomial(x,y)\n```\n\nwith\n\n```\n    r=pari(x).binomial(y)\n```\n\nand you get the same thing.  Interestingly, the memory change is *exactly* 3 MB.  I can also get similar results using pari(x).gcd(y), except exactly twice the memory is lost.  Also, changing the size of the xrange makes less memory get lost, and then seems to break the spell a bit. \n\nAt any rate, it doesn't seem to happen for small ranges, does for bigger ones, with more memory lost.  If input is not random, definitely hard to reproduce.  Totally naively, could there be too many new_gen's for Pari to handle after a certain point?",
    "created_at": "2009-09-29T03:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6623#issuecomment-54261",
    "user": "@kcrisman"
}
```

Perhaps Pari, or our wrapping of it, is the problem.  Do the same thing as above, but replace

```
    r=binomial(x,y)
```

with

```
    r=pari(x).binomial(y)
```

and you get the same thing.  Interestingly, the memory change is *exactly* 3 MB.  I can also get similar results using pari(x).gcd(y), except exactly twice the memory is lost.  Also, changing the size of the xrange makes less memory get lost, and then seems to break the spell a bit. 

At any rate, it doesn't seem to happen for small ranges, does for bigger ones, with more memory lost.  If input is not random, definitely hard to reproduce.  Totally naively, could there be too many new_gen's for Pari to handle after a certain point?



---

archive/issue_comments_054262.json:
```json
{
    "body": "Is this leak still alive? I can't reproduce on sagenb 4.7.2 or linux 4.8.alpha1/2, the only two I have at hand.",
    "created_at": "2011-12-14T00:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6623#issuecomment-54262",
    "user": "dsm"
}
```

Is this leak still alive? I can't reproduce on sagenb 4.7.2 or linux 4.8.alpha1/2, the only two I have at hand.



---

archive/issue_comments_054263.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-07-23T15:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6623#issuecomment-54263",
    "user": "@mwhansen"
}
```

Resolution: invalid



---

archive/issue_comments_054264.json:
```json
{
    "body": "I don't get this either:\n\n\n```\nsage: %cpaste\nPasting code; enter '--' alone on the line to stop or use Ctrl-D.\n:sage: import random\n:print get_memory_usage()\n:for i in xrange(100000):\n:    x=random.randint(10,100)\n:    y=random.randint(0,x)\n:    r=binomial(x,y)\n:print get_memory_usage()\n:\n:--\n1072.046875\n1072.046875\n```\n",
    "created_at": "2013-07-23T15:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6623#issuecomment-54264",
    "user": "@mwhansen"
}
```

I don't get this either:


```
sage: %cpaste
Pasting code; enter '--' alone on the line to stop or use Ctrl-D.
:sage: import random
:print get_memory_usage()
:for i in xrange(100000):
:    x=random.randint(10,100)
:    y=random.randint(0,x)
:    r=binomial(x,y)
:print get_memory_usage()
:
:--
1072.046875
1072.046875
```

