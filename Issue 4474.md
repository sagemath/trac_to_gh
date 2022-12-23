# Issue 4474: A hack in preparsing files is dangerous/confusing

archive/issues_004474.json:
```json
{
    "body": "Assignee: cwitty\n\nThere is a dangerous hack in preparser.py. Given input file:\n\n```\nload a.sage\nload b.py\n```\n\n   \nThen b.py will be loaded while the file is being *parsed*, and *before* a.sage is loaded.  That would be very confusing.  See the related #4473 and apply that patch before working on this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4474\n\n",
    "created_at": "2008-11-09T03:16:04Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "A hack in preparsing files is dangerous/confusing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4474",
    "user": "was"
}
```
Assignee: cwitty

There is a dangerous hack in preparser.py. Given input file:

```
load a.sage
load b.py
```

   
Then b.py will be loaded while the file is being *parsed*, and *before* a.sage is loaded.  That would be very confusing.  See the related #4473 and apply that patch before working on this.

Issue created by migration from https://trac.sagemath.org/ticket/4474





---

archive/issue_comments_033044.json:
```json
{
    "body": "The hack has been removed in #7514.",
    "created_at": "2014-05-01T08:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4474#issuecomment-33044",
    "user": "aapitzsch"
}
```

The hack has been removed in #7514.



---

archive/issue_comments_033045.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-05-01T08:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4474#issuecomment-33045",
    "user": "aapitzsch"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_033046.json:
```json
{
    "body": "You must set it to positive_review in this case.",
    "created_at": "2014-05-05T11:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4474#issuecomment-33046",
    "user": "ncohen"
}
```

You must set it to positive_review in this case.



---

archive/issue_comments_033047.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-05-05T11:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4474#issuecomment-33047",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_033048.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-05-06T15:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4474#issuecomment-33048",
    "user": "vbraun"
}
```

Resolution: duplicate
