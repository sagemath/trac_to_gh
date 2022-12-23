# Issue 4745: [with patch, needs review] Dsage performance is poor

archive/issues_004745.json:
```json
{
    "body": "Assignee: gfurnish\n\nCC:  mhansen\n\nDSage latency is poor, this patch seeks to improve this by a combination of pushing jobs and improving the speed of which new results are detected.  This is the first of many patches that could be made to organically improve DSage, so this is a small patch which should have big results (but there is still plenty of work to be done on DSage.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/4745\n\n",
    "created_at": "2008-12-09T07:23:01Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Dsage performance is poor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4745",
    "user": "gfurnish"
}
```
Assignee: gfurnish

CC:  mhansen

DSage latency is poor, this patch seeks to improve this by a combination of pushing jobs and improving the speed of which new results are detected.  This is the first of many patches that could be made to organically improve DSage, so this is a small patch which should have big results (but there is still plenty of work to be done on DSage.)

Issue created by migration from https://trac.sagemath.org/ticket/4745





---

archive/issue_comments_035900.json:
```json
{
    "body": "Attachment\n\nApply on top of first patch.",
    "created_at": "2008-12-09T08:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4745#issuecomment-35900",
    "user": "gfurnish"
}
```

Attachment

Apply on top of first patch.



---

archive/issue_comments_035901.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-09T08:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4745#issuecomment-35901",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035902.json:
```json
{
    "body": "For the record this last patch fixed a race condition that could *potentially* cause #3746 (but theres no guarentee there isn't a different race condition).",
    "created_at": "2008-12-09T08:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4745#issuecomment-35902",
    "user": "gfurnish"
}
```

For the record this last patch fixed a race condition that could *potentially* cause #3746 (but theres no guarentee there isn't a different race condition).



---

archive/issue_comments_035903.json:
```json
{
    "body": "Fix for doctest failure upon reenabling.",
    "created_at": "2008-12-09T18:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4745#issuecomment-35903",
    "user": "gfurnish"
}
```

Fix for doctest failure upon reenabling.



---

archive/issue_comments_035904.json:
```json
{
    "body": "Attachment\n\nMike,\n\ncan you put this on your to review list? It would be nice if this went into 3.2.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-10T09:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4745#issuecomment-35904",
    "user": "mabshoff"
}
```

Attachment

Mike,

can you put this on your to review list? It would be nice if this went into 3.2.2.

Cheers,

Michael



---

archive/issue_comments_035905.json:
```json
{
    "body": "Attachment\n\nI attached a folded patch since I wanted one for the review.  Really good work on this!  It make DSage way more useable.\n\nJust merge the -combined patch.",
    "created_at": "2008-12-11T14:47:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4745#issuecomment-35905",
    "user": "mhansen"
}
```

Attachment

I attached a folded patch since I wanted one for the review.  Really good work on this!  It make DSage way more useable.

Just merge the -combined patch.



---

archive/issue_comments_035906.json:
```json
{
    "body": "Merged trac_4745-combined.patch in Sage 3.2.2.alpha2",
    "created_at": "2008-12-11T15:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4745#issuecomment-35906",
    "user": "mabshoff"
}
```

Merged trac_4745-combined.patch in Sage 3.2.2.alpha2



---

archive/issue_comments_035907.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-11T15:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4745",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4745#issuecomment-35907",
    "user": "mabshoff"
}
```

Resolution: fixed
