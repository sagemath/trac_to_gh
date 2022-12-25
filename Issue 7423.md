# Issue 7423: plot3d can't handle log(0)

archive/issues_007423.json:
```json
{
    "body": "Assignee: @williamstein\n\nIn 4.2.1.alpha0:\n\n```\nsage: f(x,y)=ln(x)\nsage: P=plot3d(f,(x,0,1),(y,0,1))\nsage: P\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (16, 0))\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n<snip a lot>\nValueError: math domain error\n```\n\nSwitch to (x,0.1,1), and all is well.  I am pretty sure the problem is that line 404 in plot/plot3d/parametric_surface.pyx doesn't have an exception handler for log(0) or other such nan type values:\n\n```\nsage: math.log(0)\n<snip>\nValueError: math domain error\n```\n\nBut in the plotting context, it's silly not to just ignore this; we check for things like this all the time:\n\n```\nsage: plot(log,0,1)\n<works fine>\n```\n\nFor now it would probably be enough to fix it for the z variable.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/7423\n\n",
    "created_at": "2009-11-10T20:33:44Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.3",
    "title": "plot3d can't handle log(0)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7423",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @williamstein

In 4.2.1.alpha0:

```
sage: f(x,y)=ln(x)
sage: P=plot3d(f,(x,0,1),(y,0,1))
sage: P
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (16, 0))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<snip a lot>
ValueError: math domain error
```

Switch to (x,0.1,1), and all is well.  I am pretty sure the problem is that line 404 in plot/plot3d/parametric_surface.pyx doesn't have an exception handler for log(0) or other such nan type values:

```
sage: math.log(0)
<snip>
ValueError: math domain error
```

But in the plotting context, it's silly not to just ignore this; we check for things like this all the time:

```
sage: plot(log,0,1)
<works fine>
```

For now it would probably be enough to fix it for the z variable.  

Issue created by migration from https://trac.sagemath.org/ticket/7423





---

archive/issue_comments_062364.json:
```json
{
    "body": "This works for me in 4.6:\n\n\n```\nsage: f(x,y)=ln(x)\nsage: P=plot3d(f,(x,0,1),(y,0,1))\nsage: P\n```\n",
    "created_at": "2010-11-04T14:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7423#issuecomment-62364",
    "user": "https://github.com/jasongrout"
}
```

This works for me in 4.6:


```
sage: f(x,y)=ln(x)
sage: P=plot3d(f,(x,0,1),(y,0,1))
sage: P
```




---

archive/issue_comments_062365.json:
```json
{
    "body": "You're right, but I am baffled as to why.   The command `./sage -hg log -p ./devel/sage/sage/plot/plot3d/parametric_surface.pyx` doesn't give me any indication anything of this type has changed recently.  \n\nIf this worked on both Linux and Mac, and some other edge cases worked like this, I'd be satisfied to close this ticket with a patch that documented said edge cases worked; we can always fix other things like this as they occur.",
    "created_at": "2010-11-04T18:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7423#issuecomment-62365",
    "user": "https://github.com/kcrisman"
}
```

You're right, but I am baffled as to why.   The command `./sage -hg log -p ./devel/sage/sage/plot/plot3d/parametric_surface.pyx` doesn't give me any indication anything of this type has changed recently.  

If this worked on both Linux and Mac, and some other edge cases worked like this, I'd be satisfied to close this ticket with a patch that documented said edge cases worked; we can always fix other things like this as they occur.



---

archive/issue_comments_062366.json:
```json
{
    "body": "As pointed out in comment:1, this problem went away ten years ago. I also verified now on MacOS and `CoCalc`. The PR adds a doctest, so we can close this old ticket if the patchbots agree.\n----\nNew commits:",
    "created_at": "2021-01-11T01:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7423#issuecomment-62366",
    "user": "https://github.com/DaveWitteMorris"
}
```

As pointed out in comment:1, this problem went away ten years ago. I also verified now on MacOS and `CoCalc`. The PR adds a doctest, so we can close this old ticket if the patchbots agree.
----
New commits:



---

archive/issue_comments_062367.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-01-11T01:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7423#issuecomment-62367",
    "user": "https://github.com/DaveWitteMorris"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062368.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2021-01-11T01:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7423#issuecomment-62368",
    "user": "https://github.com/DaveWitteMorris"
}
```

Changing priority from major to minor.



---

archive/issue_comments_062369.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-01-11T23:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7423#issuecomment-62369",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062370.json:
```json
{
    "body": "LGTM.",
    "created_at": "2021-01-11T23:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7423#issuecomment-62370",
    "user": "https://github.com/tscrim"
}
```

LGTM.



---

archive/issue_comments_062371.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2021-01-24T10:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7423",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7423#issuecomment-62371",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
