# Issue 6432: plot and especially animate are very slow

archive/issues_006432.json:
```json
{
    "body": "Assignee: was\n\nCC:  mhansen\n\nKeywords: plot speed slow animate\n\nFor anything but the smallest animations, I'm getting very slow times for `animate()` (of course, most of the time is spent writing individual png files).  Is this just the price for python?  Can we improve this to be at least usable for the several hundred frame animations I would like to create?\n\nFor example:\n\n```\nsage: anim\nAnimation with 22 frames\nsage: %time show(anim)\nCPU times: user 6.01 s, sys: 0.14 s, total: 6.15 s\nWall time: 9.68 s\n```\n\n\nThe frames of this animation are just a few lines and points representing paths in the complex plane.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6432\n\n",
    "created_at": "2009-06-27T16:52:23Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "plot and especially animate are very slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6432",
    "user": "ncalexan"
}
```
Assignee: was

CC:  mhansen

Keywords: plot speed slow animate

For anything but the smallest animations, I'm getting very slow times for `animate()` (of course, most of the time is spent writing individual png files).  Is this just the price for python?  Can we improve this to be at least usable for the several hundred frame animations I would like to create?

For example:

```
sage: anim
Animation with 22 frames
sage: %time show(anim)
CPU times: user 6.01 s, sys: 0.14 s, total: 6.15 s
Wall time: 9.68 s
```


The frames of this animation are just a few lines and points representing paths in the complex plane.

Issue created by migration from https://trac.sagemath.org/ticket/6432





---

archive/issue_comments_051654.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-06-27T16:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6432#issuecomment-51654",
    "user": "ncalexan"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_051655.json:
```json
{
    "body": "This seems to overlap a lot with #1483:\n\n[http://trac.sagemath.org/sage_trac/ticket/1483](http://trac.sagemath.org/sage_trac/ticket/1483)\n\nThe gifs that convert produces just aren't a very good solution once things are scaled up beyond small simple animations.\nUsing javascript instead seems like the best solution, but for very high quality exportable movies I don't see an alternative to an optional ffmpeg package.",
    "created_at": "2009-07-17T12:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6432#issuecomment-51655",
    "user": "mhampton"
}
```

This seems to overlap a lot with #1483:

[http://trac.sagemath.org/sage_trac/ticket/1483](http://trac.sagemath.org/sage_trac/ticket/1483)

The gifs that convert produces just aren't a very good solution once things are scaled up beyond small simple animations.
Using javascript instead seems like the best solution, but for very high quality exportable movies I don't see an alternative to an optional ffmpeg package.
