# Issue 4425: sqrt(4) returns a SymbolicComposition instead of the number 2!

archive/issues_004425.json:
```json
{
    "body": "Assignee: somebody\n\nIn Sage-3.1.4 we have this, which I consider wrong:\n\n\n```\nsage: n = 4\nsage: type(sqrt(n))\n<class 'sage.calculus.calculus.SymbolicComposition'>\nsage: type(n.sqrt())\n<type 'sage.rings.integer.Integer'>\n```\n\n\nI think sqrt(foo) should first check if foo has a sqrt method, and\nif so call it.    I realize there is a subtle problem here, because\nthe integer sqrt function calls the symbolic calculus one!  So we\nneed some sort of architecture to fix this right.   This isn't trivial.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4425\n\n",
    "created_at": "2008-11-02T17:34:58Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "sqrt(4) returns a SymbolicComposition instead of the number 2!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4425",
    "user": "was"
}
```
Assignee: somebody

In Sage-3.1.4 we have this, which I consider wrong:


```
sage: n = 4
sage: type(sqrt(n))
<class 'sage.calculus.calculus.SymbolicComposition'>
sage: type(n.sqrt())
<type 'sage.rings.integer.Integer'>
```


I think sqrt(foo) should first check if foo has a sqrt method, and
if so call it.    I realize there is a subtle problem here, because
the integer sqrt function calls the symbolic calculus one!  So we
need some sort of architecture to fix this right.   This isn't trivial.

Issue created by migration from https://trac.sagemath.org/ticket/4425





---

archive/issue_comments_032529.json:
```json
{
    "body": "Changing assignee from somebody to kcrisman.",
    "created_at": "2008-11-04T03:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32529",
    "user": "kcrisman"
}
```

Changing assignee from somebody to kcrisman.



---

archive/issue_comments_032530.json:
```json
{
    "body": "This patch takes care of the problem as stated, passes tests for integer.pyx and rational.pyx; test for calculus.py times out (as it always does on my computer, not just for this patch).  \n\nI am *fairly* certain it also does not introduce some new endless loops or other weird bugs, but that would be worth checking out by any reviewer.",
    "created_at": "2008-11-04T03:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32530",
    "user": "kcrisman"
}
```

This patch takes care of the problem as stated, passes tests for integer.pyx and rational.pyx; test for calculus.py times out (as it always does on my computer, not just for this patch).  

I am *fairly* certain it also does not introduce some new endless loops or other weird bugs, but that would be worth checking out by any reviewer.



---

archive/issue_comments_032531.json:
```json
{
    "body": "Based on 3.2.alpha0",
    "created_at": "2008-11-04T03:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32531",
    "user": "kcrisman"
}
```

Based on 3.2.alpha0



---

archive/issue_comments_032532.json:
```json
{
    "body": "Attachment\n\nI think that the .sqrt() method in Integer and Rational should call sqrt._do_sqrt instead of creating the SymbolicComposition themselves.  For example, see\n\n\n```\nsage: sqrt._do_sqrt(4)\n2\nsage: type(_)\n<class 'sage.calculus.calculus.SymbolicComposition'>\nsage: sqrt._do_sqrt(5)\nsqrt(5)\nsage: sqrt._do_sqrt(5, all=True)\n[sqrt(5), -sqrt(5)]\n```\n",
    "created_at": "2008-11-05T07:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32532",
    "user": "mhansen"
}
```

Attachment

I think that the .sqrt() method in Integer and Rational should call sqrt._do_sqrt instead of creating the SymbolicComposition themselves.  For example, see


```
sage: sqrt._do_sqrt(4)
2
sage: type(_)
<class 'sage.calculus.calculus.SymbolicComposition'>
sage: sqrt._do_sqrt(5)
sqrt(5)
sage: sqrt._do_sqrt(5, all=True)
[sqrt(5), -sqrt(5)]
```




---

archive/issue_comments_032533.json:
```json
{
    "body": "Attachment\n\nI've attached a patch which makes the change I suggested.  What are your thoughts?",
    "created_at": "2008-11-06T12:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32533",
    "user": "mhansen"
}
```

Attachment

I've attached a patch which makes the change I suggested.  What are your thoughts?



---

archive/issue_comments_032534.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-11-06T14:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32534",
    "user": "kcrisman"
}
```

Attachment



---

archive/issue_comments_032535.json:
```json
{
    "body": "This is fine; in the meantime I did get around to implementing this.  However, I also moved the prec evaluation to the _do_sqrt function as well, since it seemed consonant with your review.\n\nAfter thinking about it, it also makes more sense do that because if for some reason something lands in sqrt with prec which isn't RR, Rational, Integer, etc. then _do_sqrt() should still make the square root be in RR if x is positive; the previous behavior was to automatically put it in CC.  \n\nDoes this seem okay?",
    "created_at": "2008-11-06T14:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32535",
    "user": "kcrisman"
}
```

This is fine; in the meantime I did get around to implementing this.  However, I also moved the prec evaluation to the _do_sqrt function as well, since it seemed consonant with your review.

After thinking about it, it also makes more sense do that because if for some reason something lands in sqrt with prec which isn't RR, Rational, Integer, etc. then _do_sqrt() should still make the square root be in RR if x is positive; the previous behavior was to automatically put it in CC.  

Does this seem okay?



---

archive/issue_comments_032536.json:
```json
{
    "body": "I attached a trivial followup patch to sqrt-nonsymbolic-1.patch which adds a docstring for the _do_sqrt function (which had no docstring) and some doctests to that function.  The new docstring also clarifies that the extend option to _do_sqrt is completely ignored, and why that is the right behavior. \n\nThe original patch sqrt-nonsymbolic-1.patch and that patch plus the attached followup sqrt-nonsymblic-2.patch together pass all doctests for me in rings and calculus.",
    "created_at": "2008-11-06T19:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32536",
    "user": "was"
}
```

I attached a trivial followup patch to sqrt-nonsymbolic-1.patch which adds a docstring for the _do_sqrt function (which had no docstring) and some doctests to that function.  The new docstring also clarifies that the extend option to _do_sqrt is completely ignored, and why that is the right behavior. 

The original patch sqrt-nonsymbolic-1.patch and that patch plus the attached followup sqrt-nonsymblic-2.patch together pass all doctests for me in rings and calculus.



---

archive/issue_comments_032537.json:
```json
{
    "body": "Attachment\n\nmabshoff -- apply this and sqrt-nonsymbolic-1.patch; don't apply anything else",
    "created_at": "2008-11-06T19:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32537",
    "user": "was"
}
```

Attachment

mabshoff -- apply this and sqrt-nonsymbolic-1.patch; don't apply anything else



---

archive/issue_comments_032538.json:
```json
{
    "body": "Replying to [comment:5 was]:\n> I attached a trivial followup patch to sqrt-nonsymbolic-1.patch which adds a docstring for the _do_sqrt function (which had no docstring) and some doctests to that function.  The new docstring also clarifies that the extend option to _do_sqrt is completely ignored, and why that is the right behavior. \n\nThis seems okay; I didn't have time to merge it but the new tests behave correctly.  So this means that the following is the desired behavior for when to extend and when not to extend?\n\n```\nsage: sqrt._do_sqrt(Integer(3),extend=False)\nsqrt(3)\nsage: a=3; type(a)\n<type 'sage.rings.integer.Integer'>\nsage: a.sqrt(extend=False)\n---------------------------------------------------------------------------\nValueError: square root of 3 not an integer\n```\n\nIf so, then let's finally let the square root of 4 be 2!",
    "created_at": "2008-11-06T21:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32538",
    "user": "kcrisman"
}
```

Replying to [comment:5 was]:
> I attached a trivial followup patch to sqrt-nonsymbolic-1.patch which adds a docstring for the _do_sqrt function (which had no docstring) and some doctests to that function.  The new docstring also clarifies that the extend option to _do_sqrt is completely ignored, and why that is the right behavior. 

This seems okay; I didn't have time to merge it but the new tests behave correctly.  So this means that the following is the desired behavior for when to extend and when not to extend?

```
sage: sqrt._do_sqrt(Integer(3),extend=False)
sqrt(3)
sage: a=3; type(a)
<type 'sage.rings.integer.Integer'>
sage: a.sqrt(extend=False)
---------------------------------------------------------------------------
ValueError: square root of 3 not an integer
```

If so, then let's finally let the square root of 4 be 2!



---

archive/issue_comments_032539.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-08T07:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32539",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032540.json:
```json
{
    "body": "Merged sqrt-nonsymbolic-1.patch and sqrt-nonsymbolic-2.patch in Sage 3.2.rc0",
    "created_at": "2008-11-08T07:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32540",
    "user": "mabshoff"
}
```

Merged sqrt-nonsymbolic-1.patch and sqrt-nonsymbolic-2.patch in Sage 3.2.rc0
