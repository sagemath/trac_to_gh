# Issue 4425: sqrt(4) returns a SymbolicComposition instead of the number 2!

archive/issues_004425.json:
```json
{
    "body": "Assignee: somebody\n\nIn Sage-3.1.4 we have this, which I consider wrong:\n\n\n```\nsage: n = 4\nsage: type(sqrt(n))\n<class 'sage.calculus.calculus.SymbolicComposition'>\nsage: type(n.sqrt())\n<type 'sage.rings.integer.Integer'>\n```\n\n\nI think sqrt(foo) should first check if foo has a sqrt method, and\nif so call it.    I realize there is a subtle problem here, because\nthe integer sqrt function calls the symbolic calculus one!  So we\nneed some sort of architecture to fix this right.   This isn't trivial.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4425\n\n",
    "created_at": "2008-11-02T17:34:58Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "sqrt(4) returns a SymbolicComposition instead of the number 2!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4425",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_032466.json:
```json
{
    "body": "Changing assignee from somebody to @kcrisman.",
    "created_at": "2008-11-04T03:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32466",
    "user": "https://github.com/kcrisman"
}
```

Changing assignee from somebody to @kcrisman.



---

archive/issue_comments_032467.json:
```json
{
    "body": "This patch takes care of the problem as stated, passes tests for integer.pyx and rational.pyx; test for calculus.py times out (as it always does on my computer, not just for this patch).  \n\nI am *fairly* certain it also does not introduce some new endless loops or other weird bugs, but that would be worth checking out by any reviewer.",
    "created_at": "2008-11-04T03:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32467",
    "user": "https://github.com/kcrisman"
}
```

This patch takes care of the problem as stated, passes tests for integer.pyx and rational.pyx; test for calculus.py times out (as it always does on my computer, not just for this patch).  

I am *fairly* certain it also does not introduce some new endless loops or other weird bugs, but that would be worth checking out by any reviewer.



---

archive/issue_comments_032468.json:
```json
{
    "body": "Based on 3.2.alpha0",
    "created_at": "2008-11-04T03:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32468",
    "user": "https://github.com/kcrisman"
}
```

Based on 3.2.alpha0



---

archive/issue_comments_032469.json:
```json
{
    "body": "Attachment [sqrt-nonsymbolic.patch](tarball://root/attachments/some-uuid/ticket4425/sqrt-nonsymbolic.patch) by @mwhansen created at 2008-11-05 07:31:34\n\nI think that the .sqrt() method in Integer and Rational should call sqrt._do_sqrt instead of creating the SymbolicComposition themselves.  For example, see\n\n\n```\nsage: sqrt._do_sqrt(4)\n2\nsage: type(_)\n<class 'sage.calculus.calculus.SymbolicComposition'>\nsage: sqrt._do_sqrt(5)\nsqrt(5)\nsage: sqrt._do_sqrt(5, all=True)\n[sqrt(5), -sqrt(5)]\n```\n",
    "created_at": "2008-11-05T07:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32469",
    "user": "https://github.com/mwhansen"
}
```

Attachment [sqrt-nonsymbolic.patch](tarball://root/attachments/some-uuid/ticket4425/sqrt-nonsymbolic.patch) by @mwhansen created at 2008-11-05 07:31:34

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

archive/issue_comments_032470.json:
```json
{
    "body": "Attachment [trac_4425.patch](tarball://root/attachments/some-uuid/ticket4425/trac_4425.patch) by @mwhansen created at 2008-11-06 12:59:31\n\nI've attached a patch which makes the change I suggested.  What are your thoughts?",
    "created_at": "2008-11-06T12:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32470",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4425.patch](tarball://root/attachments/some-uuid/ticket4425/trac_4425.patch) by @mwhansen created at 2008-11-06 12:59:31

I've attached a patch which makes the change I suggested.  What are your thoughts?



---

archive/issue_comments_032471.json:
```json
{
    "body": "Attachment [sqrt-nonsymbolic-1.patch](tarball://root/attachments/some-uuid/ticket4425/sqrt-nonsymbolic-1.patch) by @kcrisman created at 2008-11-06 14:17:14",
    "created_at": "2008-11-06T14:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32471",
    "user": "https://github.com/kcrisman"
}
```

Attachment [sqrt-nonsymbolic-1.patch](tarball://root/attachments/some-uuid/ticket4425/sqrt-nonsymbolic-1.patch) by @kcrisman created at 2008-11-06 14:17:14



---

archive/issue_comments_032472.json:
```json
{
    "body": "This is fine; in the meantime I did get around to implementing this.  However, I also moved the prec evaluation to the _do_sqrt function as well, since it seemed consonant with your review.\n\nAfter thinking about it, it also makes more sense do that because if for some reason something lands in sqrt with prec which isn't RR, Rational, Integer, etc. then _do_sqrt() should still make the square root be in RR if x is positive; the previous behavior was to automatically put it in CC.  \n\nDoes this seem okay?",
    "created_at": "2008-11-06T14:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32472",
    "user": "https://github.com/kcrisman"
}
```

This is fine; in the meantime I did get around to implementing this.  However, I also moved the prec evaluation to the _do_sqrt function as well, since it seemed consonant with your review.

After thinking about it, it also makes more sense do that because if for some reason something lands in sqrt with prec which isn't RR, Rational, Integer, etc. then _do_sqrt() should still make the square root be in RR if x is positive; the previous behavior was to automatically put it in CC.  

Does this seem okay?



---

archive/issue_comments_032473.json:
```json
{
    "body": "I attached a trivial followup patch to sqrt-nonsymbolic-1.patch which adds a docstring for the _do_sqrt function (which had no docstring) and some doctests to that function.  The new docstring also clarifies that the extend option to _do_sqrt is completely ignored, and why that is the right behavior. \n\nThe original patch sqrt-nonsymbolic-1.patch and that patch plus the attached followup sqrt-nonsymblic-2.patch together pass all doctests for me in rings and calculus.",
    "created_at": "2008-11-06T19:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32473",
    "user": "https://github.com/williamstein"
}
```

I attached a trivial followup patch to sqrt-nonsymbolic-1.patch which adds a docstring for the _do_sqrt function (which had no docstring) and some doctests to that function.  The new docstring also clarifies that the extend option to _do_sqrt is completely ignored, and why that is the right behavior. 

The original patch sqrt-nonsymbolic-1.patch and that patch plus the attached followup sqrt-nonsymblic-2.patch together pass all doctests for me in rings and calculus.



---

archive/issue_comments_032474.json:
```json
{
    "body": "Attachment [sqrt-nonsymbolic-2.patch](tarball://root/attachments/some-uuid/ticket4425/sqrt-nonsymbolic-2.patch) by @williamstein created at 2008-11-06 19:50:07\n\nmabshoff -- apply this and sqrt-nonsymbolic-1.patch; don't apply anything else",
    "created_at": "2008-11-06T19:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32474",
    "user": "https://github.com/williamstein"
}
```

Attachment [sqrt-nonsymbolic-2.patch](tarball://root/attachments/some-uuid/ticket4425/sqrt-nonsymbolic-2.patch) by @williamstein created at 2008-11-06 19:50:07

mabshoff -- apply this and sqrt-nonsymbolic-1.patch; don't apply anything else



---

archive/issue_comments_032475.json:
```json
{
    "body": "Replying to [comment:5 was]:\n> I attached a trivial followup patch to sqrt-nonsymbolic-1.patch which adds a docstring for the _do_sqrt function (which had no docstring) and some doctests to that function.  The new docstring also clarifies that the extend option to _do_sqrt is completely ignored, and why that is the right behavior. \n\nThis seems okay; I didn't have time to merge it but the new tests behave correctly.  So this means that the following is the desired behavior for when to extend and when not to extend?\n\n```\nsage: sqrt._do_sqrt(Integer(3),extend=False)\nsqrt(3)\nsage: a=3; type(a)\n<type 'sage.rings.integer.Integer'>\nsage: a.sqrt(extend=False)\n---------------------------------------------------------------------------\nValueError: square root of 3 not an integer\n```\n\nIf so, then let's finally let the square root of 4 be 2!",
    "created_at": "2008-11-06T21:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32475",
    "user": "https://github.com/kcrisman"
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

archive/issue_events_004669.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-08T07:12:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4425#event-4669"
}
```



---

archive/issue_comments_032476.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-08T07:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32476",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032477.json:
```json
{
    "body": "Merged sqrt-nonsymbolic-1.patch and sqrt-nonsymbolic-2.patch in Sage 3.2.rc0",
    "created_at": "2008-11-08T07:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4425",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4425#issuecomment-32477",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged sqrt-nonsymbolic-1.patch and sqrt-nonsymbolic-2.patch in Sage 3.2.rc0
