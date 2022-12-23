# Issue 3795: increase coverage of sage/server/notebook/cell.py

archive/issues_003795.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3795\n\n",
    "created_at": "2008-08-09T15:13:45Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "title": "increase coverage of sage/server/notebook/cell.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3795",
    "user": "mhansen"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/3795





---

archive/issue_comments_026988.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-09T15:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3795#issuecomment-26988",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_026989.json:
```json
{
    "body": "Before:\n\n```\nSCORE cell.py: 8% (7 of 82)\n```\n\n\nAfter:\n\n```\nSCORE cell.py: 79% (67 of 84)\n```\n",
    "created_at": "2008-08-09T15:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3795#issuecomment-26989",
    "user": "mhansen"
}
```

Before:

```
SCORE cell.py: 8% (7 of 82)
```


After:

```
SCORE cell.py: 79% (67 of 84)
```




---

archive/issue_comments_026990.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-10T23:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3795#issuecomment-26990",
    "user": "ncalexan"
}
```

Attachment



---

archive/issue_comments_026991.json:
```json
{
    "body": "I think mhansen's patch is excellent, but it broke if applied after #3568.  My updated patch depends on #3568 and makes the \"get a test notebook\" interface uniform using #3568.\n\nAll credit to mhansen.\n\nAttach only `3795-mhansen-doctest-cell.patch`, *after* #3568.",
    "created_at": "2008-08-10T23:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3795#issuecomment-26991",
    "user": "ncalexan"
}
```

I think mhansen's patch is excellent, but it broke if applied after #3568.  My updated patch depends on #3568 and makes the "get a test notebook" interface uniform using #3568.

All credit to mhansen.

Attach only `3795-mhansen-doctest-cell.patch`, *after* #3568.



---

archive/issue_comments_026992.json:
```json
{
    "body": "I think this can get \"positive review\" if it doctests.",
    "created_at": "2008-08-10T23:20:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3795#issuecomment-26992",
    "user": "ncalexan"
}
```

I think this can get "positive review" if it doctests.



---

archive/issue_comments_026993.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-11T08:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3795#issuecomment-26993",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026994.json:
```json
{
    "body": "Merged trac_3795.patch in Sage 3.1.alpha1. Sorry Nick, due to #3568 causing massive doctest failures William will redo it for 3.1.alpha2. Hopefully someone will take your patch and rebase it on the new release.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-11T08:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3795#issuecomment-26994",
    "user": "mabshoff"
}
```

Merged trac_3795.patch in Sage 3.1.alpha1. Sorry Nick, due to #3568 causing massive doctest failures William will redo it for 3.1.alpha2. Hopefully someone will take your patch and rebase it on the new release.

Cheers,

Michael
