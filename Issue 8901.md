# Issue 8901: negative integers in IntegerVectors()

archive/issues_008901.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  @sdenton4\n\nKeywords: integer, vector\n\nIntegerVectors() seems to only include vectors with positive integer entries:\n\n```\nsage: [-1,4] in IntegerVectors()\nFalse\n```\n\n\nCan the class be changed to include vectors with some/all negative integer entries as well, or create a new, larger class for all integer vectors (since I can imagine that having a class for positive integer vectors would be useful in some applications)?\n\nThanks,\nEva\n\nIssue created by migration from https://trac.sagemath.org/ticket/8901\n\n",
    "created_at": "2010-05-06T01:14:18Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.1",
    "title": "negative integers in IntegerVectors()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8901",
    "user": "ecurry"
}
```
Assignee: sage-combinat

CC:  @sdenton4

Keywords: integer, vector

IntegerVectors() seems to only include vectors with positive integer entries:

```
sage: [-1,4] in IntegerVectors()
False
```


Can the class be changed to include vectors with some/all negative integer entries as well, or create a new, larger class for all integer vectors (since I can imagine that having a class for positive integer vectors would be useful in some applications)?

Thanks,
Eva

Issue created by migration from https://trac.sagemath.org/ticket/8901





---

archive/issue_comments_081923.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2010-05-06T14:00:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81923",
    "user": "ecurry"
}
```

Changing priority from minor to major.



---

archive/issue_comments_081924.json:
```json
{
    "body": "Changing assignee from sage-combinat to ecurry.",
    "created_at": "2010-05-06T14:00:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81924",
    "user": "ecurry"
}
```

Changing assignee from sage-combinat to ecurry.



---

archive/issue_comments_081925.json:
```json
{
    "body": "Status: Eva will look into funding for a Sage Days at Acadia where updating IntegerVectors can be one of the focuses.",
    "created_at": "2010-05-06T14:00:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81925",
    "user": "ecurry"
}
```

Status: Eva will look into funding for a Sage Days at Acadia where updating IntegerVectors can be one of the focuses.



---

archive/issue_comments_081926.json:
```json
{
    "body": "This is not a bug, but instead a misnomer. I've updated the doc-strings to warn the users about this and created a Ticket #12932 to ask for the new class.",
    "created_at": "2012-05-09T22:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81926",
    "user": "@tscrim"
}
```

This is not a bug, but instead a misnomer. I've updated the doc-strings to warn the users about this and created a Ticket #12932 to ask for the new class.



---

archive/issue_comments_081927.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-09T22:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81927",
    "user": "@tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081928.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2012-05-09T22:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81928",
    "user": "@tscrim"
}
```

Changing priority from major to minor.



---

archive/issue_comments_081929.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-09T22:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81929",
    "user": "@sdenton4"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081930.json:
```json
{
    "body": "Changing keywords from \"integer, vector\" to \"integer, vector, days38\".",
    "created_at": "2012-05-09T22:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81930",
    "user": "@sdenton4"
}
```

Changing keywords from "integer, vector" to "integer, vector, days38".



---

archive/issue_comments_081931.json:
```json
{
    "body": "Positive review assuming doc tests pass.",
    "created_at": "2012-05-09T22:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81931",
    "user": "@sdenton4"
}
```

Positive review assuming doc tests pass.



---

archive/issue_comments_081932.json:
```json
{
    "body": "The formatting of the documentation should be like\n\n```\nEntries are non-negative::\n```\n\nwith the double colon at the end.",
    "created_at": "2012-05-11T11:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81932",
    "user": "@jdemeyer"
}
```

The formatting of the documentation should be like

```
Entries are non-negative::
```

with the double colon at the end.



---

archive/issue_comments_081933.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-05-11T11:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81933",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_081934.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-05-11T13:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81934",
    "user": "@tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081935.json:
```json
{
    "body": "Changed formatting of doc-string. Now consistent with the rest of the file.",
    "created_at": "2012-05-11T13:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81935",
    "user": "@tscrim"
}
```

Changed formatting of doc-string. Now consistent with the rest of the file.



---

archive/issue_comments_081936.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-15T16:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81936",
    "user": "@sdenton4"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081937.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-05-18T14:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81937",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_081938.json:
```json
{
    "body": "There is a further problem with the documentation formatting: the list of AUTHORS should be indented like\n\n```\nAUTHORS:\n\n * bla bla bla\n * bla bla bla\n   bla bla bla\n```\n\nas opposed to\n\n```\nAUTHORS:\n\n * bla bla bla\n * bla bla bla\n bla bla bla\n```\n",
    "created_at": "2012-05-18T14:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81938",
    "user": "@jdemeyer"
}
```

There is a further problem with the documentation formatting: the list of AUTHORS should be indented like

```
AUTHORS:

 * bla bla bla
 * bla bla bla
   bla bla bla
```

as opposed to

```
AUTHORS:

 * bla bla bla
 * bla bla bla
 bla bla bla
```




---

archive/issue_comments_081939.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-05-19T16:13:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81939",
    "user": "@tscrim"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081940.json:
```json
{
    "body": "Attachment [trac_8901-integer_vectors_docstrings_fix-ts.patch](tarball://root/attachments/some-uuid/ticket8901/trac_8901-integer_vectors_docstrings_fix-ts.patch) by @tscrim created at 2012-05-19 16:13:36\n\nCorrected.",
    "created_at": "2012-05-19T16:13:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81940",
    "user": "@tscrim"
}
```

Attachment [trac_8901-integer_vectors_docstrings_fix-ts.patch](tarball://root/attachments/some-uuid/ticket8901/trac_8901-integer_vectors_docstrings_fix-ts.patch) by @tscrim created at 2012-05-19 16:13:36

Corrected.



---

archive/issue_comments_081941.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-22T08:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81941",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081942.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-05-23T21:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8901#issuecomment-81942",
    "user": "@jdemeyer"
}
```

Resolution: fixed
