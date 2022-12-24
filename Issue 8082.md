# Issue 8082: correct point and line behavior with complex numbers

archive/issues_008082.json:
```json
{
    "body": "Assignee: vdelecroix\n\nKeywords: plot\n\nWe have a strange behavior\n\n\n```\nsage: point(CC(0))  # plot a point with coordinates (0, 0)\nsage: point(CC(1))  # plot a point with coordinates (1, 0)\nsage: point([CC(0),CC(1)])  # plot a point with coordinates (0, 1)\n```\n\n\nThis patch add a line in sage.plot to correct this and get the two points (0,0) and (1,0) when doing\n\n\n```\nsage: point([CC(0), CC(1)])\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8082\n\n",
    "created_at": "2010-01-26T18:37:49Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "correct point and line behavior with complex numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8082",
    "user": "vdelecroix"
}
```
Assignee: vdelecroix

Keywords: plot

We have a strange behavior


```
sage: point(CC(0))  # plot a point with coordinates (0, 0)
sage: point(CC(1))  # plot a point with coordinates (1, 0)
sage: point([CC(0),CC(1)])  # plot a point with coordinates (0, 1)
```


This patch add a line in sage.plot to correct this and get the two points (0,0) and (1,0) when doing


```
sage: point([CC(0), CC(1)])
```


Issue created by migration from https://trac.sagemath.org/ticket/8082





---

archive/issue_comments_070825.json:
```json
{
    "body": "Attachment [trac_8082.patch](tarball://root/attachments/some-uuid/ticket8082/trac_8082.patch) by vdelecroix created at 2010-01-26 18:47:16",
    "created_at": "2010-01-26T18:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8082#issuecomment-70825",
    "user": "vdelecroix"
}
```

Attachment [trac_8082.patch](tarball://root/attachments/some-uuid/ticket8082/trac_8082.patch) by vdelecroix created at 2010-01-26 18:47:16



---

archive/issue_comments_070826.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-26T18:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8082#issuecomment-70826",
    "user": "vdelecroix"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070827.json:
```json
{
    "body": "Changing keywords from \"plot\" to \"plot, complex numbers\".",
    "created_at": "2010-01-26T18:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8082#issuecomment-70827",
    "user": "vdelecroix"
}
```

Changing keywords from "plot" to "plot, complex numbers".



---

archive/issue_comments_070828.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-27T17:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8082#issuecomment-70828",
    "user": "vdelecroix"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070829.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-29T22:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8082#issuecomment-70829",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070830.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T10:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8082#issuecomment-70830",
    "user": "rossk"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070831.json:
```json
{
    "body": "Works as advertised\n\n\n```\n# (1) pre-patch, this plotted a point with coordinates (0, 1)\n# (2) post-patch, this plots 2 points at (0,0) and (1,0) as designed\nsage: point([CC(0),CC(1)])\n\n# plot the 8 vertices of an octagon\nsage: point([CC(cos(theta)+I*sin(theta)) for theta in srange(0, 2*pi, pi/4)],aspect_ratio=1)\n```\n",
    "created_at": "2010-01-31T10:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8082#issuecomment-70831",
    "user": "rossk"
}
```

Works as advertised


```
# (1) pre-patch, this plotted a point with coordinates (0, 1)
# (2) post-patch, this plots 2 points at (0,0) and (1,0) as designed
sage: point([CC(0),CC(1)])

# plot the 8 vertices of an octagon
sage: point([CC(cos(theta)+I*sin(theta)) for theta in srange(0, 2*pi, pi/4)],aspect_ratio=1)
```




---

archive/issue_comments_070832.json:
```json
{
    "body": "The patch commit string is insufficiently descriptive. I've refreshed it to `#8082: Correct point and line behavior with complex numbers` in the queue for 4.3.3.alpha0.",
    "created_at": "2010-02-10T15:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8082#issuecomment-70832",
    "user": "mpatel"
}
```

The patch commit string is insufficiently descriptive. I've refreshed it to `#8082: Correct point and line behavior with complex numbers` in the queue for 4.3.3.alpha0.



---

archive/issue_comments_070833.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8082#issuecomment-70833",
    "user": "mpatel"
}
```

Resolution: fixed
