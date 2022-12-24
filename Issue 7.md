# Issue 7: very strange bug with LaurentSeriesRing

archive/issues_000007.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R.<u> = LaurentSeriesRing(pAdicField(5, 10))\nsage: S.<t> = LaurentSeriesRing(RationalField())\nsage: R(t + t^2 + O(t^3))\n u^1 + t + O(t^2) + u^2 + t + O(t^2) + O(u^3 + t + O(t^2))\n```\n\n\n???!!!!???\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7\n\n",
    "created_at": "2006-09-12T02:35:46Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "very strange bug with LaurentSeriesRing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7",
    "user": "dmharvey"
}
```
Assignee: somebody


```
sage: R.<u> = LaurentSeriesRing(pAdicField(5, 10))
sage: S.<t> = LaurentSeriesRing(RationalField())
sage: R(t + t^2 + O(t^3))
 u^1 + t + O(t^2) + u^2 + t + O(t^2) + O(u^3 + t + O(t^2))
```


???!!!!???


Issue created by migration from https://trac.sagemath.org/ticket/7





---

archive/issue_comments_000022.json:
```json
{
    "body": "Attachment [1790.patch](tarball://root/attachments/some-uuid/ticket7/1790.patch) by was created at 2006-11-06 08:22:04",
    "created_at": "2006-11-06T08:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7#issuecomment-22",
    "user": "was"
}
```

Attachment [1790.patch](tarball://root/attachments/some-uuid/ticket7/1790.patch) by was created at 2006-11-06 08:22:04



---

archive/issue_comments_000023.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-11-06T08:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7#issuecomment-23",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000024.json:
```json
{
    "body": "Fixed for sage-1.5",
    "created_at": "2006-11-06T08:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7#issuecomment-24",
    "user": "was"
}
```

Fixed for sage-1.5



---

archive/issue_comments_000025.json:
```json
{
    "body": "a comment to facilitate GH import, please ignore.",
    "created_at": "2022-09-08T08:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7#issuecomment-25",
    "user": "dimpase"
}
```

a comment to facilitate GH import, please ignore.
