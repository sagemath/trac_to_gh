# Issue 9923: Doctest error in sage/geometry/polyhedra.py

archive/issues_009923.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  alexghitza novoselt vbraun\n\nI get this doctest error with a trial 4.6.alpha1 on sage.math and many other Sage cluster and Skynet machines:\n\n```python\nsage -t -long  devel/sage/sage/geometry/polyhedra.py\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/geometry/polyhedra.py\", line 1270:\n    sage: p1.projection().show() + p2.projection().show() + p3.projection().show()\nExpected nothing\nGot:\n    doctest:4555: DeprecationWarning: (Since Sage 4.6) use the option 'width' instead of 'thickness'\n    <BLANKLINE>\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9924\n\n",
    "created_at": "2010-09-16T23:41:58Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Doctest error in sage/geometry/polyhedra.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9923",
    "user": "mpatel"
}
```
Assignee: mvngu

CC:  alexghitza novoselt vbraun

I get this doctest error with a trial 4.6.alpha1 on sage.math and many other Sage cluster and Skynet machines:

```python
sage -t -long  devel/sage/sage/geometry/polyhedra.py
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/geometry/polyhedra.py", line 1270:
    sage: p1.projection().show() + p2.projection().show() + p3.projection().show()
Expected nothing
Got:
    doctest:4555: DeprecationWarning: (Since Sage 4.6) use the option 'width' instead of 'thickness'
    <BLANKLINE>
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/9924





---

archive/issue_comments_098787.json:
```json
{
    "body": "If it's feasible to create a patch now, I can merge it into 4.6.alpha1, while I wait for a response to a build error at #4000.",
    "created_at": "2010-09-16T23:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9923#issuecomment-98787",
    "user": "mpatel"
}
```

If it's feasible to create a patch now, I can merge it into 4.6.alpha1, while I wait for a response to a build error at #4000.



---

archive/issue_comments_098788.json:
```json
{
    "body": "I'm not seeing this in 4.6.alpha0.  It looks like some graphics ticket you merged between alpha0 and alpha1 introduced a new deprecation warning.  Any idea which ticket it might be?\n\nIf we can find that out, it shouldn't be difficult to change either the code or the doctest to use the new non-deprecated way of doing things.",
    "created_at": "2010-09-17T00:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9923#issuecomment-98788",
    "user": "AlexGhitza"
}
```

I'm not seeing this in 4.6.alpha0.  It looks like some graphics ticket you merged between alpha0 and alpha1 introduced a new deprecation warning.  Any idea which ticket it might be?

If we can find that out, it shouldn't be difficult to change either the code or the doctest to use the new non-deprecated way of doing things.



---

archive/issue_comments_098789.json:
```json
{
    "body": "Ticket #7154 changed the options for point/arrow thickness and was merged in 4.6.alpha1. I didn't realize that this impacts the polyhedra package, but of course it does. Anyways, the obvious patch is to change the option name in polyhedra.py.",
    "created_at": "2010-09-17T00:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9923#issuecomment-98789",
    "user": "vbraun"
}
```

Ticket #7154 changed the options for point/arrow thickness and was merged in 4.6.alpha1. I didn't realize that this impacts the polyhedra package, but of course it does. Anyways, the obvious patch is to change the option name in polyhedra.py.



---

archive/issue_comments_098790.json:
```json
{
    "body": "By the way, the unofficial, trial 4.6.alpha1 is in `/home/release/sage-4.6.alpha1` on the Sage cluster.",
    "created_at": "2010-09-17T00:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9923#issuecomment-98790",
    "user": "mpatel"
}
```

By the way, the unofficial, trial 4.6.alpha1 is in `/home/release/sage-4.6.alpha1` on the Sage cluster.



---

archive/issue_comments_098791.json:
```json
{
    "body": "Attachment [trac_9924.patch](tarball://root/attachments/some-uuid/ticket9924/trac_9924.patch) by AlexGhitza created at 2010-09-17 01:39:58",
    "created_at": "2010-09-17T01:39:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9923#issuecomment-98791",
    "user": "AlexGhitza"
}
```

Attachment [trac_9924.patch](tarball://root/attachments/some-uuid/ticket9924/trac_9924.patch) by AlexGhitza created at 2010-09-17 01:39:58



---

archive/issue_comments_098792.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-17T01:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9923#issuecomment-98792",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098793.json:
```json
{
    "body": "OK, a fairly trivial patch is now up.",
    "created_at": "2010-09-17T01:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9923#issuecomment-98793",
    "user": "AlexGhitza"
}
```

OK, a fairly trivial patch is now up.



---

archive/issue_comments_098794.json:
```json
{
    "body": "Solves the for me issue!",
    "created_at": "2010-09-17T03:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9923#issuecomment-98794",
    "user": "novoselt"
}
```

Solves the for me issue!



---

archive/issue_comments_098795.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-17T03:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9923#issuecomment-98795",
    "user": "novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098796.json:
```json
{
    "body": "Thanks!",
    "created_at": "2010-09-17T03:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9923#issuecomment-98796",
    "user": "mpatel"
}
```

Thanks!



---

archive/issue_comments_098797.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-17T03:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9923#issuecomment-98797",
    "user": "mpatel"
}
```

Resolution: fixed
