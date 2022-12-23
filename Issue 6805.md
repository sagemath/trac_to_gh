# Issue 6805: [with patch, needs review] Integrality check in LatticePolytope

archive/issues_006805.json:
```json
{
    "body": "Assignee: mhampton\n\nIt is possible now to create a lattice polytope with rational vertices, which allows things to work, but causes wrong answers:\n\n```\nsage: m = matrix([1/2, 3/2])\nsage: m\n[1/2 3/2]\nsage: LatticePolytope(m).points()\n[0 1]\n```\n\nThis patch adds an extra check/conversion to the constructor to prevent this:\n\n```\nsage: m = matrix([1/2, 3/2])\nsage: m\n[1/2 3/2]\nsage: LatticePolytope(m).points()\nTraceback (most recent call last):\n...\nValueError: Points must be integral!\nGiven:\n[1/2 3/2]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6805\n\n",
    "created_at": "2009-08-22T20:25:59Z",
    "labels": [
        "geometry",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Integrality check in LatticePolytope",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6805",
    "user": "novoselt"
}
```
Assignee: mhampton

It is possible now to create a lattice polytope with rational vertices, which allows things to work, but causes wrong answers:

```
sage: m = matrix([1/2, 3/2])
sage: m
[1/2 3/2]
sage: LatticePolytope(m).points()
[0 1]
```

This patch adds an extra check/conversion to the constructor to prevent this:

```
sage: m = matrix([1/2, 3/2])
sage: m
[1/2 3/2]
sage: LatticePolytope(m).points()
Traceback (most recent call last):
...
ValueError: Points must be integral!
Given:
[1/2 3/2]
```


Issue created by migration from https://trac.sagemath.org/ticket/6805





---

archive/issue_comments_056031.json:
```json
{
    "body": "Attachment\n\nSeems like a reasonable change, and tests out OK, so positive review.",
    "created_at": "2009-10-29T18:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6805#issuecomment-56031",
    "user": "mhampton"
}
```

Attachment

Seems like a reasonable change, and tests out OK, so positive review.



---

archive/issue_comments_056032.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-29T18:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6805#issuecomment-56032",
    "user": "mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056033.json:
```json
{
    "body": "This patch is included as a part of a rebased patch for #6831.",
    "created_at": "2009-10-30T05:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6805#issuecomment-56033",
    "user": "novoselt"
}
```

This patch is included as a part of a rebased patch for #6831.



---

archive/issue_comments_056034.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-02T04:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6805#issuecomment-56034",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_056035.json:
```json
{
    "body": "Fixed in #6831.",
    "created_at": "2009-11-02T04:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6805#issuecomment-56035",
    "user": "mhansen"
}
```

Fixed in #6831.
