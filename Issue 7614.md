# Issue 7614: change plot to use fast_callable

archive/issues_007614.json:
```json
{
    "body": "Assignee: was\n\n\n```\n\n\nOn Sun, Dec 6, 2009 at 4:51 PM, Michel <vdbergh@gmail.com> wrote:\n> Thanks for the reply. But no. The problem is not due to the fact that\n> the function has a singularity. Indeed.\n>\n> plot(20*log(abs((1+I*x)^4),10),(x,0,3))\n>\n> fails with the same error which is incomprehensible to me.\n>\n> On the other hand turning the expression into a lambda function made\n> it possible to plot it. Thanks for this practical advice.\n>\n> I wish someone could explain this rationally to me.\n>\n> 20*log(abs((1+I*x)^4),10)\n>\n> seems to be a perfectly fine symbolic expression so IMHO it should be\n> possible to plot it.\n\nThis is a bug.  There absolutely no reason that plotting should give the error\n   \"float() argument must be a string or a number\".\nWe could give an error about not being able to evaluate the function at certain\npoints.  However, the above error is not OK.    The error in fact is not in plotting\nbut in making a fast_float compiled version of the expression:\n\nsage: s = 20*log(abs((1+I*x)^4),10)\nsage: fast_float(s,x)\nTraceback (most recent call last):\n...\nTypeError: float() argument must be a string or a number\n\nIn fact, SAge *should* be using fast_callable, not fast_float.  This works just fine if you force it manually:\n\ns = 20*log(abs((1+I*x)^4),10)\nplot(fast_callable(s,vars=[x]), (x,0,3))\n[[nice picture as output]]\n\nMany, many thanks for your bug report.  It is bug reports from users like you that really helps Sage to be a first-rate mathematical software system. \n\n  }}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/7614\n\n",
    "created_at": "2009-12-06T22:30:12Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "change plot to use fast_callable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7614",
    "user": "was"
}
```
Assignee: was


```


On Sun, Dec 6, 2009 at 4:51 PM, Michel <vdbergh@gmail.com> wrote:
> Thanks for the reply. But no. The problem is not due to the fact that
> the function has a singularity. Indeed.
>
> plot(20*log(abs((1+I*x)^4),10),(x,0,3))
>
> fails with the same error which is incomprehensible to me.
>
> On the other hand turning the expression into a lambda function made
> it possible to plot it. Thanks for this practical advice.
>
> I wish someone could explain this rationally to me.
>
> 20*log(abs((1+I*x)^4),10)
>
> seems to be a perfectly fine symbolic expression so IMHO it should be
> possible to plot it.

This is a bug.  There absolutely no reason that plotting should give the error
   "float() argument must be a string or a number".
We could give an error about not being able to evaluate the function at certain
points.  However, the above error is not OK.    The error in fact is not in plotting
but in making a fast_float compiled version of the expression:

sage: s = 20*log(abs((1+I*x)^4),10)
sage: fast_float(s,x)
Traceback (most recent call last):
...
TypeError: float() argument must be a string or a number

In fact, SAge *should* be using fast_callable, not fast_float.  This works just fine if you force it manually:

s = 20*log(abs((1+I*x)^4),10)
plot(fast_callable(s,vars=[x]), (x,0,3))
[[nice picture as output]]

Many, many thanks for your bug report.  It is bug reports from users like you that really helps Sage to be a first-rate mathematical software system. 

  }}}

Issue created by migration from https://trac.sagemath.org/ticket/7614





---

archive/issue_comments_065017.json:
```json
{
    "body": "From this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/19de9e09ff948cbc) thread:\n\n```\nOn Sun, Dec 6, 2009 at 4:51 PM, Michel <vdbergh@gmail.com> wrote:\n> Thanks for the reply. But no. The problem is not due to the fact that\n> the function has a singularity. Indeed.\n>\n> plot(20*log(abs((1+I*x)^4),10),(x,0,3))\n>\n> fails with the same error which is incomprehensible to me.\n>\n> On the other hand turning the expression into a lambda function made\n> it possible to plot it. Thanks for this practical advice.\n>\n> I wish someone could explain this rationally to me.\n>\n> 20*log(abs((1+I*x)^4),10)\n>\n> seems to be a perfectly fine symbolic expression so IMHO it should be\n> possible to plot it.\n\nThis is a bug.  There absolutely no reason that plotting should give the error\n   \"float() argument must be a string or a number\".\nWe could give an error about not being able to evaluate the function at certain\npoints.  However, the above error is not OK.    The error in fact is not in plotting\nbut in making a fast_float compiled version of the expression:\n\nsage: s = 20*log(abs((1+I*x)^4),10)\nsage: fast_float(s,x)\nTraceback (most recent call last):\n...\nTypeError: float() argument must be a string or a number\n\nIn fact, SAge *should* be using fast_callable, not fast_float.  This works\njust fine if you force it manually:\n\ns = 20*log(abs((1+I*x)^4),10)\nplot(fast_callable(s,vars=[x]), (x,0,3))\n[[nice picture as output]]\n\nMany, many thanks for your bug report.  It is bug reports from users like\nyou that really helps Sage to be a first-rate mathematical software system.\n```\n",
    "created_at": "2009-12-07T00:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7614#issuecomment-65017",
    "user": "mvngu"
}
```

From this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/19de9e09ff948cbc) thread:

```
On Sun, Dec 6, 2009 at 4:51 PM, Michel <vdbergh@gmail.com> wrote:
> Thanks for the reply. But no. The problem is not due to the fact that
> the function has a singularity. Indeed.
>
> plot(20*log(abs((1+I*x)^4),10),(x,0,3))
>
> fails with the same error which is incomprehensible to me.
>
> On the other hand turning the expression into a lambda function made
> it possible to plot it. Thanks for this practical advice.
>
> I wish someone could explain this rationally to me.
>
> 20*log(abs((1+I*x)^4),10)
>
> seems to be a perfectly fine symbolic expression so IMHO it should be
> possible to plot it.

This is a bug.  There absolutely no reason that plotting should give the error
   "float() argument must be a string or a number".
We could give an error about not being able to evaluate the function at certain
points.  However, the above error is not OK.    The error in fact is not in plotting
but in making a fast_float compiled version of the expression:

sage: s = 20*log(abs((1+I*x)^4),10)
sage: fast_float(s,x)
Traceback (most recent call last):
...
TypeError: float() argument must be a string or a number

In fact, SAge *should* be using fast_callable, not fast_float.  This works
just fine if you force it manually:

s = 20*log(abs((1+I*x)^4),10)
plot(fast_callable(s,vars=[x]), (x,0,3))
[[nice picture as output]]

Many, many thanks for your bug report.  It is bug reports from users like
you that really helps Sage to be a first-rate mathematical software system.
```




---

archive/issue_comments_065018.json:
```json
{
    "body": "Some of the things at #5572 need to be fixed (like constant functions) before this switch.  Right now, fast_float handles things like constant functions, but fast_callable does not.",
    "created_at": "2009-12-07T11:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7614#issuecomment-65018",
    "user": "jason"
}
```

Some of the things at #5572 need to be fixed (like constant functions) before this switch.  Right now, fast_float handles things like constant functions, but fast_callable does not.



---

archive/issue_comments_065019.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n> Some of the things at #5572 need to be fixed (like constant functions) before this switch.  Right now, fast_float handles things like constant functions, but fast_callable does not.\n\n1. fast_float is just as bad as fast_callable, IMHO, since fast_float fails to handle many things too.  \n\n2. Nobody is working on fast_callable, as far as I know, since Carl Witty is no longer working on Sage. \n\n3. The specific problem under consideration could nicely by solved with a simple try/except:\n\n```\ntry: \n    fast_float(...)\nexcept:\n    fast_callable(...)\n```\n",
    "created_at": "2009-12-09T15:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7614#issuecomment-65019",
    "user": "was"
}
```

Replying to [comment:3 jason]:
> Some of the things at #5572 need to be fixed (like constant functions) before this switch.  Right now, fast_float handles things like constant functions, but fast_callable does not.

1. fast_float is just as bad as fast_callable, IMHO, since fast_float fails to handle many things too.  

2. Nobody is working on fast_callable, as far as I know, since Carl Witty is no longer working on Sage. 

3. The specific problem under consideration could nicely by solved with a simple try/except:

```
try: 
    fast_float(...)
except:
    fast_callable(...)
```




---

archive/issue_comments_065020.json:
```json
{
    "body": "Attachment [trac_7614.patch](tarball://root/attachments/some-uuid/ticket7614/trac_7614.patch) by was created at 2009-12-09 16:13:20",
    "created_at": "2009-12-09T16:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7614#issuecomment-65020",
    "user": "was"
}
```

Attachment [trac_7614.patch](tarball://root/attachments/some-uuid/ticket7614/trac_7614.patch) by was created at 2009-12-09 16:13:20



---

archive/issue_comments_065021.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-09T16:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7614#issuecomment-65021",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065022.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-09T17:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7614#issuecomment-65022",
    "user": "jason"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065023.json:
```json
{
    "body": "passes doctests, fixes the problem above.",
    "created_at": "2009-12-09T17:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7614#issuecomment-65023",
    "user": "jason"
}
```

passes doctests, fixes the problem above.



---

archive/issue_comments_065024.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-14T16:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7614#issuecomment-65024",
    "user": "mhansen"
}
```

Resolution: fixed
