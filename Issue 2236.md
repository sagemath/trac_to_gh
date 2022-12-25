# Issue 2236: plot randomizes the endpoints of the interval and causes wiggling in the graph

archive/issues_002236.json:
```json
{
    "body": "Assignee: @williamstein\n\n\np=plot(x, (x,-1,1))\np[0][0] == -1\np[0][-1] == 1\n\nThey will almost always return false before the patch.  After the patch, the two statements should return True always.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2236\n\n",
    "created_at": "2008-02-20T22:39:42Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "plot randomizes the endpoints of the interval and causes wiggling in the graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2236",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein


p=plot(x, (x,-1,1))
p[0][0] == -1
p[0][-1] == 1

They will almost always return false before the patch.  After the patch, the two statements should return True always.

Issue created by migration from https://trac.sagemath.org/ticket/2236





---

archive/issue_comments_014777.json:
```json
{
    "body": "I agree with the suggestion to *not* randomize the endpoints.  That's bad.",
    "created_at": "2008-02-20T22:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2236#issuecomment-14777",
    "user": "https://github.com/williamstein"
}
```

I agree with the suggestion to *not* randomize the endpoints.  That's bad.



---

archive/issue_comments_014778.json:
```json
{
    "body": "Attachment [plot_fix_endpoints.patch](tarball://root/attachments/some-uuid/ticket2236/plot_fix_endpoints.patch) by @jasongrout created at 2008-02-20 22:51:08",
    "created_at": "2008-02-20T22:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2236#issuecomment-14778",
    "user": "https://github.com/jasongrout"
}
```

Attachment [plot_fix_endpoints.patch](tarball://root/attachments/some-uuid/ticket2236/plot_fix_endpoints.patch) by @jasongrout created at 2008-02-20 22:51:08



---

archive/issue_comments_014779.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha2",
    "created_at": "2008-02-20T23:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2236#issuecomment-14779",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha2



---

archive/issue_comments_014780.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-20T23:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2236#issuecomment-14780",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014781.json:
```json
{
    "body": "For the record, on IRC:\n\n[16:55] <wstein> #2236 -- positive review.",
    "created_at": "2008-02-20T23:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2236#issuecomment-14781",
    "user": "https://github.com/jasongrout"
}
```

For the record, on IRC:

[16:55] <wstein> #2236 -- positive review.
