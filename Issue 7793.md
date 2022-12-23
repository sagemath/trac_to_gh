# Issue 7793: zorder not implemented in disk

archive/issues_007793.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason\n\nFrom the report a bug link:\n\nIt seems that the zorder does not work with disk(). I found a report saying that this was resolved for point() and polygon(), (and I know it works) but nothing about disk(). I found this using the following test:\n\n```\nd1 = disk((0,0), 1, (0, 2*pi), color = 'red', zorder=0) \nd2 = disk((0,0), 0.75, (0, 2*pi), color = 'brown', zorder=1)\nd3 = disk((0,0), 0.5, (0, 2*pi), color = 'green', zorder= 2)\nd4 = disk((0,0), 0.25, (0, 2*pi), color = 'yellow', zorder=3)\nfinal = d4 + d3 + d2 + d1\nfinal.show(aspect_ratio = 1)\n```\n\n\nIncidentally (not in the report), this shows that axes apparently have default zorder of 2.  So do arrows, but polygons have a default of 1.  This is confusing.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7793\n\n",
    "created_at": "2009-12-30T03:40:26Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "zorder not implemented in disk",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7793",
    "user": "kcrisman"
}
```
Assignee: was

CC:  jason

From the report a bug link:

It seems that the zorder does not work with disk(). I found a report saying that this was resolved for point() and polygon(), (and I know it works) but nothing about disk(). I found this using the following test:

```
d1 = disk((0,0), 1, (0, 2*pi), color = 'red', zorder=0) 
d2 = disk((0,0), 0.75, (0, 2*pi), color = 'brown', zorder=1)
d3 = disk((0,0), 0.5, (0, 2*pi), color = 'green', zorder= 2)
d4 = disk((0,0), 0.25, (0, 2*pi), color = 'yellow', zorder=3)
final = d4 + d3 + d2 + d1
final.show(aspect_ratio = 1)
```


Incidentally (not in the report), this shows that axes apparently have default zorder of 2.  So do arrows, but polygons have a default of 1.  This is confusing.

Issue created by migration from https://trac.sagemath.org/ticket/7793





---

archive/issue_comments_067259.json:
```json
{
    "body": "Based on 4.3",
    "created_at": "2009-12-30T03:40:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7793#issuecomment-67259",
    "user": "kcrisman"
}
```

Based on 4.3



---

archive/issue_comments_067260.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-30T03:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7793#issuecomment-67260",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067261.json:
```json
{
    "body": "Attachment\n\nWould be open to suggestions as to how to handle the issues raised in [this](http://groups.google.com/group/sage-devel/browse_thread/thread/ec30de67075e116f) thread, but for now this is up for review.",
    "created_at": "2009-12-30T03:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7793#issuecomment-67261",
    "user": "kcrisman"
}
```

Attachment

Would be open to suggestions as to how to handle the issues raised in [this](http://groups.google.com/group/sage-devel/browse_thread/thread/ec30de67075e116f) thread, but for now this is up for review.



---

archive/issue_comments_067262.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T11:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7793#issuecomment-67262",
    "user": "rossk"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067263.json:
```json
{
    "body": "The patch fixes the zorder problem (the code below produces 3 colorful bullseyes).\n\n```\nsage: d1 = disk((0,0), 1, (0, 2*pi), color = 'red', zorder=0) \nsage: d2 = disk((0,0), 0.75, (0, 2*pi), color = 'brown', zorder=1)\nsage: d3 = disk((0,0), 0.5, (0, 2*pi), color = 'green', zorder= 2)\nsage: d4 = disk((0,0), 0.25, (0, 2*pi), color = 'yellow', zorder=3)\nsage: final = d4 + d3 + d2 + d1\nsage: final.show(aspect_ratio = 1) \nsage: final2 = d1 + d2 + d3 + d4                                   \nsage: final2.show(aspect_ratio = 1)                                \nsage: final3 = d3 + d2 + d4 + d1   \nsage: final3.show(aspect_ratio = 1)\n```\n\n(Note: Intuitively, final, final2 and final3 should all produce the same image and they do)",
    "created_at": "2010-01-31T11:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7793#issuecomment-67263",
    "user": "rossk"
}
```

The patch fixes the zorder problem (the code below produces 3 colorful bullseyes).

```
sage: d1 = disk((0,0), 1, (0, 2*pi), color = 'red', zorder=0) 
sage: d2 = disk((0,0), 0.75, (0, 2*pi), color = 'brown', zorder=1)
sage: d3 = disk((0,0), 0.5, (0, 2*pi), color = 'green', zorder= 2)
sage: d4 = disk((0,0), 0.25, (0, 2*pi), color = 'yellow', zorder=3)
sage: final = d4 + d3 + d2 + d1
sage: final.show(aspect_ratio = 1) 
sage: final2 = d1 + d2 + d3 + d4                                   
sage: final2.show(aspect_ratio = 1)                                
sage: final3 = d3 + d2 + d4 + d1   
sage: final3.show(aspect_ratio = 1)
```

(Note: Intuitively, final, final2 and final3 should all produce the same image and they do)



---

archive/issue_comments_067264.json:
```json
{
    "body": "Please remember to update the relevant ticket fields --- the release\nmanagers use an automated script to generate lists of merged tickets.",
    "created_at": "2010-02-11T14:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7793#issuecomment-67264",
    "user": "mpatel"
}
```

Please remember to update the relevant ticket fields --- the release
managers use an automated script to generate lists of merged tickets.



---

archive/issue_comments_067265.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7793",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7793#issuecomment-67265",
    "user": "mpatel"
}
```

Resolution: fixed
