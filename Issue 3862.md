# Issue 3862: axes in plot3d broken

archive/issues_003862.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman\n\nKeywords: plot3d, axes\n\nExample:\n\n```\nvar('x')\nvar('y')\nplot3d(cos(x) + sin(y), (x, -2,1), (y, -2,1), axes = True)\n```\n\n\nAt least one axis is in the right location, the other two...\n\nTranslating coordinates into jmol seems to be difficult, so maybe this is the reason?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3862\n\n",
    "created_at": "2008-08-14T22:27:04Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "axes in plot3d broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3862",
    "user": "mclean"
}
```
Assignee: @williamstein

CC:  @kcrisman

Keywords: plot3d, axes

Example:

```
var('x')
var('y')
plot3d(cos(x) + sin(y), (x, -2,1), (y, -2,1), axes = True)
```


At least one axis is in the right location, the other two...

Translating coordinates into jmol seems to be difficult, so maybe this is the reason?


Issue created by migration from https://trac.sagemath.org/ticket/3862





---

archive/issue_comments_027517.json:
```json
{
    "body": "The fix is to put `axes molecular` in the jmol script.  You can see the fix by right-clicking, selecting \"console\", and then entering the `axes molecular` command.",
    "created_at": "2009-02-10T19:40:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3862#issuecomment-27517",
    "user": "@jasongrout"
}
```

The fix is to put `axes molecular` in the jmol script.  You can see the fix by right-clicking, selecting "console", and then entering the `axes molecular` command.



---

archive/issue_comments_027518.json:
```json
{
    "body": "The attached patch makes the axes centered at the origin.",
    "created_at": "2009-02-10T19:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3862#issuecomment-27518",
    "user": "@jasongrout"
}
```

The attached patch makes the axes centered at the origin.



---

archive/issue_comments_027519.json:
```json
{
    "body": "Assigning this to sage-3.3 will get mabshoff's attention, probably before he comes back on IRC :).  Is this trivial enough to get in?  It corrects a very annoying thing that bothers me when trying to teach calculus and graphing things in 3d.",
    "created_at": "2009-02-10T19:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3862#issuecomment-27519",
    "user": "@jasongrout"
}
```

Assigning this to sage-3.3 will get mabshoff's attention, probably before he comes back on IRC :).  Is this trivial enough to get in?  It corrects a very annoying thing that bothers me when trying to teach calculus and graphing things in 3d.



---

archive/issue_comments_027520.json:
```json
{
    "body": "Okay, never mind.  Carl Witty pointed out that this ticket deals with the *Sage* axes, not the jmol axes.  I'm posting this patch up at #5229 and retracting my claim of a fix here.",
    "created_at": "2009-02-10T21:19:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3862#issuecomment-27520",
    "user": "@jasongrout"
}
```

Okay, never mind.  Carl Witty pointed out that this ticket deals with the *Sage* axes, not the jmol axes.  I'm posting this patch up at #5229 and retracting my claim of a fix here.
