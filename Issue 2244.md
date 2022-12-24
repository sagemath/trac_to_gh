# Issue 2244: [with patch; needs review] add a randomize=False option to the plot command, to avoid "wiggle" in animations

archive/issues_002244.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2244\n\n",
    "created_at": "2008-02-21T06:41:53Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] add a randomize=False option to the plot command, to avoid \"wiggle\" in animations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2244",
    "user": "was"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/2244





---

archive/issue_comments_014869.json:
```json
{
    "body": "The attached patch *also* fixes a bug where the right hand endpoint in the plot\nrange wasn't included.  This is very clear when doing plots with very few points.",
    "created_at": "2008-02-21T06:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2244#issuecomment-14869",
    "user": "was"
}
```

The attached patch *also* fixes a bug where the right hand endpoint in the plot
range wasn't included.  This is very clear when doing plots with very few points.



---

archive/issue_comments_014870.json:
```json
{
    "body": "Apply this after #2236.\n\nIgnore the comment above about also fixing endpoints -- #2236 also did so.",
    "created_at": "2008-02-21T06:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2244#issuecomment-14870",
    "user": "was"
}
```

Apply this after #2236.

Ignore the comment above about also fixing endpoints -- #2236 also did so.



---

archive/issue_comments_014871.json:
```json
{
    "body": "Attachment [wiggle-interior.patch](tarball://root/attachments/some-uuid/ticket2244/wiggle-interior.patch) by jason created at 2008-02-21 21:20:51\n\napply after William's patch",
    "created_at": "2008-02-21T21:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2244#issuecomment-14871",
    "user": "jason"
}
```

Attachment [wiggle-interior.patch](tarball://root/attachments/some-uuid/ticket2244/wiggle-interior.patch) by jason created at 2008-02-21 21:20:51

apply after William's patch



---

archive/issue_comments_014872.json:
```json
{
    "body": "Williams patch looks good to me, but I slightly changed the wording of his examples to specify that the *initial* sample points were the things guaranteed to be consistent.\n\nI also added a small type-cast to the adaptive code to be consistent with the code above for regular sample points.",
    "created_at": "2008-02-21T21:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2244#issuecomment-14872",
    "user": "jason"
}
```

Williams patch looks good to me, but I slightly changed the wording of his examples to specify that the *initial* sample points were the things guaranteed to be consistent.

I also added a small type-cast to the adaptive code to be consistent with the code above for regular sample points.



---

archive/issue_comments_014873.json:
```json
{
    "body": "Both patches fail to apply cleanly against 2.10.2. Please rebase.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-24T03:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2244#issuecomment-14873",
    "user": "mabshoff"
}
```

Both patches fail to apply cleanly against 2.10.2. Please rebase.

Cheers,

Michael



---

archive/issue_comments_014874.json:
```json
{
    "body": "this should apply cleanly (it replaces the patch that was here before)",
    "created_at": "2008-02-24T04:57:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2244#issuecomment-14874",
    "user": "was"
}
```

this should apply cleanly (it replaces the patch that was here before)



---

archive/issue_comments_014875.json:
```json
{
    "body": "Attachment [sage-2244-nowiggle.patch](tarball://root/attachments/some-uuid/ticket2244/sage-2244-nowiggle.patch) by was created at 2008-02-24 04:58:06\n\nApply sage-2244-nowiggle.patch (which has now been rebased) followed by wiggle-interior.patch which will apply correctly with some \"fuzz\". \n\n -- William",
    "created_at": "2008-02-24T04:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2244#issuecomment-14875",
    "user": "was"
}
```

Attachment [sage-2244-nowiggle.patch](tarball://root/attachments/some-uuid/ticket2244/sage-2244-nowiggle.patch) by was created at 2008-02-24 04:58:06

Apply sage-2244-nowiggle.patch (which has now been rebased) followed by wiggle-interior.patch which will apply correctly with some "fuzz". 

 -- William



---

archive/issue_comments_014876.json:
```json
{
    "body": "Replying to [comment:6 was]:\n> Apply sage-2244-nowiggle.patch (which has now been rebased) followed by wiggle-interior.patch which will apply correctly with some \"fuzz\". \n> \n>  -- William\n\nNo, it doesn't, at least for me:\n\n```\nsage$ patch -p1 --dry-run < trac_2244-nowiggle.patch \npatching file sage/plot/plot.py\nHunk #1 FAILED at 3284.\nHunk #2 succeeded at 3421 with fuzz 2 (offset -11 lines).\nHunk #3 succeeded at 3445 (offset -12 lines).\n1 out of 3 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\n```\n\nI checked for hunk one in plot.py and it just isn't there. Maybe this patch depends on another patch to be applied first? \n\nCheers,\n\nMichael",
    "created_at": "2008-02-25T02:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2244#issuecomment-14876",
    "user": "mabshoff"
}
```

Replying to [comment:6 was]:
> Apply sage-2244-nowiggle.patch (which has now been rebased) followed by wiggle-interior.patch which will apply correctly with some "fuzz". 
> 
>  -- William

No, it doesn't, at least for me:

```
sage$ patch -p1 --dry-run < trac_2244-nowiggle.patch 
patching file sage/plot/plot.py
Hunk #1 FAILED at 3284.
Hunk #2 succeeded at 3421 with fuzz 2 (offset -11 lines).
Hunk #3 succeeded at 3445 (offset -12 lines).
1 out of 3 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
```

I checked for hunk one in plot.py and it just isn't there. Maybe this patch depends on another patch to be applied first? 

Cheers,

Michael



---

archive/issue_comments_014877.json:
```json
{
    "body": "This gives the following reject:\n\n\n```\n\n--- plot.py\n+++ plot.py\n@@ -3284,8 +3284,9 @@ class PlotFactory(GraphicPrimitiveFactor\n         200\n         sage: P          # render\n \n-    We plot with randomize=False, so that the same points are\n-    evenly spaced (and always the same):\n+    We plot with randomize=False, which makes the initial sample\n+    points evenly spaced (hence always the same).  Adaptive plotting\n+    might insert other points, however.\n         sage: p = plot(sin,-1,1,plot_points=3,plot_division=0,randomize=False)\n         sage: p[0][1][0]\n         -0.66666666666666...\n\n```\n\n\nand the corresponding bit in plot.py in 2.10.3.rc1 is\n\n\n```\n\n        sage: len(P[0])  # random output\n        80\n        sage: P          # render\n\n    Some colored functions:\n\n        sage: plot(sin, 0, 10, rgbcolor='#ff00ff')\n        sage: plot(sin, 0, 10, rgbcolor='purple')\n    \n    We plot several functions together by passing a list\n    of functions as input:\n        sage: plot([sin(n*x) for n in [1..4]], (0, pi))\n\n```\n",
    "created_at": "2008-03-05T00:37:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2244#issuecomment-14877",
    "user": "mhansen"
}
```

This gives the following reject:


```

--- plot.py
+++ plot.py
@@ -3284,8 +3284,9 @@ class PlotFactory(GraphicPrimitiveFactor
         200
         sage: P          # render
 
-    We plot with randomize=False, so that the same points are
-    evenly spaced (and always the same):
+    We plot with randomize=False, which makes the initial sample
+    points evenly spaced (hence always the same).  Adaptive plotting
+    might insert other points, however.
         sage: p = plot(sin,-1,1,plot_points=3,plot_division=0,randomize=False)
         sage: p[0][1][0]
         -0.66666666666666...

```


and the corresponding bit in plot.py in 2.10.3.rc1 is


```

        sage: len(P[0])  # random output
        80
        sage: P          # render

    Some colored functions:

        sage: plot(sin, 0, 10, rgbcolor='#ff00ff')
        sage: plot(sin, 0, 10, rgbcolor='purple')
    
    We plot several functions together by passing a list
    of functions as input:
        sage: plot([sin(n*x) for n in [1..4]], (0, pi))

```




---

archive/issue_comments_014878.json:
```json
{
    "body": "Attachment [2244_nowiggle_new.patch](tarball://root/attachments/some-uuid/ticket2244/2244_nowiggle_new.patch) by AlexGhitza created at 2008-03-15 18:11:16\n\napply instead of the two above",
    "created_at": "2008-03-15T18:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2244#issuecomment-14878",
    "user": "AlexGhitza"
}
```

Attachment [2244_nowiggle_new.patch](tarball://root/attachments/some-uuid/ticket2244/2244_nowiggle_new.patch) by AlexGhitza created at 2008-03-15 18:11:16

apply instead of the two above



---

archive/issue_comments_014879.json:
```json
{
    "body": "I'm attaching a new patch replacing the other two, made against sage-2.10.3.  doctests in sage/plot/ work fine on it.",
    "created_at": "2008-03-15T18:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2244#issuecomment-14879",
    "user": "AlexGhitza"
}
```

I'm attaching a new patch replacing the other two, made against sage-2.10.3.  doctests in sage/plot/ work fine on it.



---

archive/issue_comments_014880.json:
```json
{
    "body": "Merged 2244_nowiggle_new.patch in Sage 2.10.4.rc0",
    "created_at": "2008-03-15T23:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2244#issuecomment-14880",
    "user": "mabshoff"
}
```

Merged 2244_nowiggle_new.patch in Sage 2.10.4.rc0



---

archive/issue_comments_014881.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-15T23:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2244#issuecomment-14881",
    "user": "mabshoff"
}
```

Resolution: fixed
