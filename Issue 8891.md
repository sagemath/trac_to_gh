# Issue 8891: sage -t doesn't accept . as current directory

archive/issues_008891.json:
```json
{
    "body": "Assignee: tbd\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8891\n\n",
    "created_at": "2010-05-05T16:31:01Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "sage -t doesn't accept . as current directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8891",
    "user": "wjlaffin"
}
```
Assignee: tbd



Issue created by migration from https://trac.sagemath.org/ticket/8891





---

archive/issue_comments_081742.json:
```json
{
    "body": "Attachment [trac_8891.patch](tarball://root/attachments/some-uuid/ticket8891/trac_8891.patch) by mhansen created at 2010-05-05 16:48:11\n\nIt was explicitly disabled long ago (before Trac), but I don't see any reason why it should be now.",
    "created_at": "2010-05-05T16:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8891#issuecomment-81742",
    "user": "mhansen"
}
```

Attachment [trac_8891.patch](tarball://root/attachments/some-uuid/ticket8891/trac_8891.patch) by mhansen created at 2010-05-05 16:48:11

It was explicitly disabled long ago (before Trac), but I don't see any reason why it should be now.



---

archive/issue_comments_081743.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-05T16:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8891#issuecomment-81743",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081744.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-12T08:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8891#issuecomment-81744",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081745.json:
```json
{
    "body": "Without the patch, I get, e.g.,\n\n```sh\nmpatel@sage monoids$ sage -t .\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 0.0 seconds\nmpatel@sage monoids$ \n```\n\nWith the patch, I get\n\n```sh\nmpatel@sage monoids$ sage -t .\nsage -t  \"./string_monoid_element.py\"                       \n         [2.1 s]\n[...]\n```\n",
    "created_at": "2010-06-12T08:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8891#issuecomment-81745",
    "user": "mpatel"
}
```

Without the patch, I get, e.g.,

```sh
mpatel@sage monoids$ sage -t .
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 0.0 seconds
mpatel@sage monoids$ 
```

With the patch, I get

```sh
mpatel@sage monoids$ sage -t .
sage -t  "./string_monoid_element.py"                       
         [2.1 s]
[...]
```




---

archive/issue_comments_081746.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8891#issuecomment-81746",
    "user": "rlm"
}
```

Resolution: fixed
