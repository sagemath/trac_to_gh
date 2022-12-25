# Issue 6273: Improve random_element for number field orders and ideals (easy)

archive/issues_006273.json:
```json
{
    "body": "Assignee: @williamstein\n\nAt the moment, random_element for number field orders returns a random integer coerced into the order, which isn't very useful. A much better solution would be to use the random_element method of the underlying free ZZ-module. \n\nMore generally, one could ask for the same functionality for fractional ideals (and the above would be the special case for the ideal (1).)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6273\n\n",
    "created_at": "2009-06-13T10:36:05Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Improve random_element for number field orders and ideals (easy)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6273",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @williamstein

At the moment, random_element for number field orders returns a random integer coerced into the order, which isn't very useful. A much better solution would be to use the random_element method of the underlying free ZZ-module. 

More generally, one could ask for the same functionality for fractional ideals (and the above would be the special case for the ideal (1).)

Issue created by migration from https://trac.sagemath.org/ticket/6273





---

archive/issue_comments_050008.json:
```json
{
    "body": "I have implemented this.  using the random_element() function for ZZ and integral bases.  It works for absolute and relative orders and ideals.\n\nI started out using the random_element() function for the module class, but that did not work in the relative situation.  It is a little strange that the classes for orders and ideals do not derive from free ZZ-modules.",
    "created_at": "2009-06-13T19:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6273#issuecomment-50008",
    "user": "https://github.com/JohnCremona"
}
```

I have implemented this.  using the random_element() function for ZZ and integral bases.  It works for absolute and relative orders and ideals.

I started out using the random_element() function for the module class, but that did not work in the relative situation.  It is a little strange that the classes for orders and ideals do not derive from free ZZ-modules.



---

archive/issue_comments_050009.json:
```json
{
    "body": "Changing keywords from \"\" to \"number field ideal order\".",
    "created_at": "2009-06-13T19:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6273#issuecomment-50009",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "" to "number field ideal order".



---

archive/issue_comments_050010.json:
```json
{
    "body": "REVIEW:\n\nI think it would be better to do\n\n```\n def random_element(self, *args, **kwds)\n```\n\nthen in the docstring say that the inputs are identical to ZZ.random_element, whatever those are.  This will if ZZ.random_element is ever improved, changed, or extended in any way (and let's hope it is), then this docstring won't have to change. \n\nThen in the call to ZZ.random_element, just do ZZ.random_element(*args, **kwds).  This shorter and more robust.\n\n -- William",
    "created_at": "2009-06-14T10:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6273#issuecomment-50010",
    "user": "https://github.com/williamstein"
}
```

REVIEW:

I think it would be better to do

```
 def random_element(self, *args, **kwds)
```

then in the docstring say that the inputs are identical to ZZ.random_element, whatever those are.  This will if ZZ.random_element is ever improved, changed, or extended in any way (and let's hope it is), then this docstring won't have to change. 

Then in the call to ZZ.random_element, just do ZZ.random_element(*args, **kwds).  This shorter and more robust.

 -- William



---

archive/issue_comments_050011.json:
```json
{
    "body": "Replying to [comment:3 was]:\n> REVIEW:\n> \n> I think it would be better to do\n> {{{\n>  def random_element(self, *args, **kwds)\n> }}}\n> then in the docstring say that the inputs are identical to ZZ.random_element, whatever those are.  This will if ZZ.random_element is ever improved, changed, or extended in any way (and let's hope it is), then this docstring won't have to change. \n> \n> Then in the call to ZZ.random_element, just do ZZ.random_element(*args, **kwds).  This shorter and more robust.\n> \n>  -- William\n\nOK, I'll do that.  John",
    "created_at": "2009-06-14T15:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6273#issuecomment-50011",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:3 was]:
> REVIEW:
> 
> I think it would be better to do
> {{{
>  def random_element(self, *args, **kwds)
> }}}
> then in the docstring say that the inputs are identical to ZZ.random_element, whatever those are.  This will if ZZ.random_element is ever improved, changed, or extended in any way (and let's hope it is), then this docstring won't have to change. 
> 
> Then in the call to ZZ.random_element, just do ZZ.random_element(*args, **kwds).  This shorter and more robust.
> 
>  -- William

OK, I'll do that.  John



---

archive/issue_comments_050012.json:
```json
{
    "body": "Attachment [trac_6273.patch](tarball://root/attachments/some-uuid/ticket6273/trac_6273.patch) by @JohnCremona created at 2009-06-14 15:44:55\n\nThe revised patch does what was asked for in the review!",
    "created_at": "2009-06-14T15:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6273#issuecomment-50012",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_6273.patch](tarball://root/attachments/some-uuid/ticket6273/trac_6273.patch) by @JohnCremona created at 2009-06-14 15:44:55

The revised patch does what was asked for in the review!



---

archive/issue_comments_050013.json:
```json
{
    "body": "In the relative case, the parents are wrong.  I am fixing this right now.",
    "created_at": "2009-06-15T20:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6273#issuecomment-50013",
    "user": "https://github.com/ncalexan"
}
```

In the relative case, the parents are wrong.  I am fixing this right now.



---

archive/issue_comments_050014.json:
```json
{
    "body": "Sorry about that.  I'll review your fix as soon as I can.  John",
    "created_at": "2009-06-15T20:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6273#issuecomment-50014",
    "user": "https://github.com/JohnCremona"
}
```

Sorry about that.  I'll review your fix as soon as I can.  John



---

archive/issue_comments_050015.json:
```json
{
    "body": "Attachment [trac_6273-replacement.patch](tarball://root/attachments/some-uuid/ticket6273/trac_6273-replacement.patch) by @JohnCremona created at 2009-06-15 21:53:37\n\nThe new patch sorts out the parent problem ok, with suitable new doctests.  I note that you now delegate the random function for orders to that of ideals -- this means that the new code is *not* used for non-maximal order, unfortunately.  But then the same was true for my version.\n\nSo I would have given this a positive review, while noting that at some point non-maximal orders will need to be dealt with too.\n\nUnfortunately:\n\n```\nsage -t  \"devel/sage-6273/sage/rings/number_field/number_field_ideal.py\"\n**********************************************************************\nFile \"/home/john/sage-4.0.2.rc0/devel/sage-6273/sage/rings/number_field/number_field_ideal.py\", line 1045:\n    sage: I.basis()\nExpected:\n    [3, -a + 1, (-3/2*b - 1497/2)*a, (-1/2*b - 499/2)*a - b - 499]\nGot:\n    [3, a + 2, (3/2*b + 1497/2)*a, (b + 499)*a - b - 499]\n```\n\nso it's still \"needs work\"",
    "created_at": "2009-06-15T21:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6273#issuecomment-50015",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_6273-replacement.patch](tarball://root/attachments/some-uuid/ticket6273/trac_6273-replacement.patch) by @JohnCremona created at 2009-06-15 21:53:37

The new patch sorts out the parent problem ok, with suitable new doctests.  I note that you now delegate the random function for orders to that of ideals -- this means that the new code is *not* used for non-maximal order, unfortunately.  But then the same was true for my version.

So I would have given this a positive review, while noting that at some point non-maximal orders will need to be dealt with too.

Unfortunately:

```
sage -t  "devel/sage-6273/sage/rings/number_field/number_field_ideal.py"
**********************************************************************
File "/home/john/sage-4.0.2.rc0/devel/sage-6273/sage/rings/number_field/number_field_ideal.py", line 1045:
    sage: I.basis()
Expected:
    [3, -a + 1, (-3/2*b - 1497/2)*a, (-1/2*b - 499/2)*a - b - 499]
Got:
    [3, a + 2, (3/2*b + 1497/2)*a, (b + 499)*a - b - 499]
```

so it's still "needs work"



---

archive/issue_comments_050016.json:
```json
{
    "body": "Replying to [comment:8 cremona]:\n> The new patch sorts out the parent problem ok, with suitable new doctests.  I note that you now delegate the random function for orders to that of ideals -- this means that the new code is *not* used for non-maximal order, unfortunately.  But then the same was true for my version.\n> \n> So I would have given this a positive review, while noting that at some point non-maximal orders will need to be dealt with too.\n> \n> Unfortunately:\n> {{{\n> sage -t  \"devel/sage-6273/sage/rings/number_field/number_field_ideal.py\"\n> **********************************************************************\n> File \"/home/john/sage-4.0.2.rc0/devel/sage-6273/sage/rings/number_field/number_field_ideal.py\", line 1045:\n>     sage: I.basis()\n> Expected:\n>     [3, -a + 1, (-3/2*b - 1497/2)*a, (-1/2*b - 499/2)*a - b - 499]\n> Got:\n>     [3, a + 2, (3/2*b + 1497/2)*a, (b + 499)*a - b - 499]\n> }}}\n> so it's still \"needs work\"\n\nLet's just comment out both basis lines (since basis works, and it's essentially random).  Can you make non-maximal orders work with the previous code?  If so, do it and I will review.",
    "created_at": "2009-06-15T22:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6273#issuecomment-50016",
    "user": "https://github.com/ncalexan"
}
```

Replying to [comment:8 cremona]:
> The new patch sorts out the parent problem ok, with suitable new doctests.  I note that you now delegate the random function for orders to that of ideals -- this means that the new code is *not* used for non-maximal order, unfortunately.  But then the same was true for my version.
> 
> So I would have given this a positive review, while noting that at some point non-maximal orders will need to be dealt with too.
> 
> Unfortunately:
> {{{
> sage -t  "devel/sage-6273/sage/rings/number_field/number_field_ideal.py"
> **********************************************************************
> File "/home/john/sage-4.0.2.rc0/devel/sage-6273/sage/rings/number_field/number_field_ideal.py", line 1045:
>     sage: I.basis()
> Expected:
>     [3, -a + 1, (-3/2*b - 1497/2)*a, (-1/2*b - 499/2)*a - b - 499]
> Got:
>     [3, a + 2, (3/2*b + 1497/2)*a, (b + 499)*a - b - 499]
> }}}
> so it's still "needs work"

Let's just comment out both basis lines (since basis works, and it's essentially random).  Can you make non-maximal orders work with the previous code?  If so, do it and I will review.



---

archive/issue_comments_050017.json:
```json
{
    "body": "Attachment [trac_6273_new.patch](tarball://root/attachments/some-uuid/ticket6273/trac_6273_new.patch) by @JohnCremona created at 2009-06-16 09:51:07\n\nReplaces both previous",
    "created_at": "2009-06-16T09:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6273#issuecomment-50017",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_6273_new.patch](tarball://root/attachments/some-uuid/ticket6273/trac_6273_new.patch) by @JohnCremona created at 2009-06-16 09:51:07

Replaces both previous



---

archive/issue_comments_050018.json:
```json
{
    "body": "I removed the lines showing the bases (which were not part of the test exactly, just there for illustration).  I reinstated my original for orders, since it works for non-maximal orders, and added a new doctest to show that;  but I kept in the additional doctests from the review patch to show that theparent are now correct (which I also borrowed from the review patch).\n\nThis one tests ok on both 32- and 64-bit, and I hope contains the best of both earlier patches with none of the problems!  And in view of the trouble this took to get right, I removed the \"(easy)\" from the ticket's title!",
    "created_at": "2009-06-16T09:54:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6273#issuecomment-50018",
    "user": "https://github.com/JohnCremona"
}
```

I removed the lines showing the bases (which were not part of the test exactly, just there for illustration).  I reinstated my original for orders, since it works for non-maximal orders, and added a new doctest to show that;  but I kept in the additional doctests from the review patch to show that theparent are now correct (which I also borrowed from the review patch).

This one tests ok on both 32- and 64-bit, and I hope contains the best of both earlier patches with none of the problems!  And in view of the trouble this took to get right, I removed the "(easy)" from the ticket's title!



---

archive/issue_comments_050019.json:
```json
{
    "body": "I'm a fan!",
    "created_at": "2009-06-16T17:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6273#issuecomment-50019",
    "user": "https://github.com/ncalexan"
}
```

I'm a fan!



---

archive/issue_comments_050020.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T09:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6273#issuecomment-50020",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
