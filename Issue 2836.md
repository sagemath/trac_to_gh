# Issue 2836: [with patch, needs review] twisted.conch.ssh deprecated functions

archive/issues_002836.json:
```json
{
    "body": "Assignee: yi\n\nPatch attached which uses the new twisted.conch.ssh.keys.Key object instead of the old helper functions. If we don't apply this patch we'll get a bunch of annoying deprecated API warnings :-) \n\nIssue created by migration from https://trac.sagemath.org/ticket/2836\n\n",
    "created_at": "2008-04-07T00:11:07Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] twisted.conch.ssh deprecated functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2836",
    "user": "yi"
}
```
Assignee: yi

Patch attached which uses the new twisted.conch.ssh.keys.Key object instead of the old helper functions. If we don't apply this patch we'll get a bunch of annoying deprecated API warnings :-) 

Issue created by migration from https://trac.sagemath.org/ticket/2836





---

archive/issue_comments_019460.json:
```json
{
    "body": "Attachment [conch_deprecated_warnings.patch](tarball://root/attachments/some-uuid/ticket2836/conch_deprecated_warnings.patch) by yi created at 2008-04-07 00:11:40",
    "created_at": "2008-04-07T00:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2836#issuecomment-19460",
    "user": "yi"
}
```

Attachment [conch_deprecated_warnings.patch](tarball://root/attachments/some-uuid/ticket2836/conch_deprecated_warnings.patch) by yi created at 2008-04-07 00:11:40



---

archive/issue_comments_019461.json:
```json
{
    "body": "Looks good to me.  Passes on alpha1 + new twisted spkg.",
    "created_at": "2008-04-07T01:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2836#issuecomment-19461",
    "user": "mhansen"
}
```

Looks good to me.  Passes on alpha1 + new twisted spkg.



---

archive/issue_comments_019462.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T01:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2836#issuecomment-19462",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019463.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-07T01:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2836#issuecomment-19463",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2
