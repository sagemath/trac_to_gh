# Issue 2236: plot randomizes the endpoints of the interval and causes wiggling in the graph

archive/issues_002236.json:
```json
{
    "body": "Assignee: was\n\n\np=plot(x, (x,-1,1))\np[0][0] == -1\np[0][-1] == 1\n\nThey will almost always return false before the patch.  After the patch, the two statements should return True always.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2236\n\n",
    "created_at": "2008-02-20T22:39:42Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "plot randomizes the endpoints of the interval and causes wiggling in the graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2236",
    "user": "jason"
}
```
Assignee: was


p=plot(x, (x,-1,1))
p[0][0] == -1
p[0][-1] == 1

They will almost always return false before the patch.  After the patch, the two statements should return True always.

Issue created by migration from https://trac.sagemath.org/ticket/2236





---

archive/issue_comments_014808.json:
```json
{
    "body": "I agree with the suggestion to *not* randomize the endpoints.  That's bad.",
    "created_at": "2008-02-20T22:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2236#issuecomment-14808",
    "user": "was"
}
```

I agree with the suggestion to *not* randomize the endpoints.  That's bad.



---

archive/issue_comments_014809.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-20T22:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2236#issuecomment-14809",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_014810.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha2",
    "created_at": "2008-02-20T23:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2236#issuecomment-14810",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha2



---

archive/issue_comments_014811.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-20T23:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2236#issuecomment-14811",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014812.json:
```json
{
    "body": "For the record, on IRC:\n\n[16:55] <wstein> #2236 -- positive review.",
    "created_at": "2008-02-20T23:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2236#issuecomment-14812",
    "user": "jason"
}
```

For the record, on IRC:

[16:55] <wstein> #2236 -- positive review.
