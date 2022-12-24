# Issue 4037: [with trivial patch, needs review] list_of_first_n() broken in interact.py

archive/issues_004037.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nIn server/notebook/interact.py, the function list_of_first_n() claims to return n elements, but it returns n+1 of them.  The attached trivial patch fixes the function and the doctests.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4037\n\n",
    "created_at": "2008-09-02T04:37:21Z",
    "labels": [
        "interact",
        "minor",
        "bug"
    ],
    "title": "[with trivial patch, needs review] list_of_first_n() broken in interact.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4037",
    "user": "AlexGhitza"
}
```
Assignee: AlexGhitza

In server/notebook/interact.py, the function list_of_first_n() claims to return n elements, but it returns n+1 of them.  The attached trivial patch fixes the function and the doctests.


Issue created by migration from https://trac.sagemath.org/ticket/4037





---

archive/issue_comments_029128.json:
```json
{
    "body": "Attachment [4037-interact_list_of_first_n.patch](tarball://root/attachments/some-uuid/ticket4037/4037-interact_list_of_first_n.patch) by cremona created at 2008-09-02 08:24:07\n\nOk, a simple out-by-one bug.  Patch applies cleanly to 3.1.2.alpha3 and doctests in sage.server.notebook all pass.\n\nOK by me, though I usually steer clear of notebook patches as I rarely use the notebook!",
    "created_at": "2008-09-02T08:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4037#issuecomment-29128",
    "user": "cremona"
}
```

Attachment [4037-interact_list_of_first_n.patch](tarball://root/attachments/some-uuid/ticket4037/4037-interact_list_of_first_n.patch) by cremona created at 2008-09-02 08:24:07

Ok, a simple out-by-one bug.  Patch applies cleanly to 3.1.2.alpha3 and doctests in sage.server.notebook all pass.

OK by me, though I usually steer clear of notebook patches as I rarely use the notebook!



---

archive/issue_comments_029129.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-02T09:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4037#issuecomment-29129",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029130.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha4",
    "created_at": "2008-09-02T09:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4037#issuecomment-29130",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha4
