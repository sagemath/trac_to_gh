# Issue 2051: [with doc patch, needs review] added documentation for parameters of groebner_basis method of boolean ideals

archive/issues_002051.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin\n\nSee patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2051\n\n",
    "created_at": "2008-02-05T11:53:47Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with doc patch, needs review] added documentation for parameters of groebner_basis method of boolean ideals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2051",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin

See patch.

Issue created by migration from https://trac.sagemath.org/ticket/2051





---

archive/issue_comments_013251.json:
```json
{
    "body": "Attachment [pbori_gb_doc.patch](tarball://root/attachments/some-uuid/ticket2051/pbori_gb_doc.patch) by @burcin created at 2008-02-05 12:16:35\n\nIt might be a good idea not to document features that don't work. (I.e., as outlined in #2052, draw_matrices, invert, noro, preprocess_only) As a matter of fact, I am not sure if all the other options work as they should. Maybe we should include optional doctests for them.\n\nBTW, last time I asked Michael Brickenstein, `PolyBoRi` did not include a usable noro implementation.",
    "created_at": "2008-02-05T12:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2051#issuecomment-13251",
    "user": "https://github.com/burcin"
}
```

Attachment [pbori_gb_doc.patch](tarball://root/attachments/some-uuid/ticket2051/pbori_gb_doc.patch) by @burcin created at 2008-02-05 12:16:35

It might be a good idea not to document features that don't work. (I.e., as outlined in #2052, draw_matrices, invert, noro, preprocess_only) As a matter of fact, I am not sure if all the other options work as they should. Maybe we should include optional doctests for them.

BTW, last time I asked Michael Brickenstein, `PolyBoRi` did not include a usable noro implementation.



---

archive/issue_comments_013252.json:
```json
{
    "body": "Attachment [pbori_gb_doc2.patch](tarball://root/attachments/some-uuid/ticket2051/pbori_gb_doc2.patch) by @malb created at 2008-02-05 13:44:06\n\nThe patch `pbori_gb_doc2.patch` addresses Burcin's comments above. It should be applied on top of the first patch.",
    "created_at": "2008-02-05T13:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2051#issuecomment-13252",
    "user": "https://github.com/malb"
}
```

Attachment [pbori_gb_doc2.patch](tarball://root/attachments/some-uuid/ticket2051/pbori_gb_doc2.patch) by @malb created at 2008-02-05 13:44:06

The patch `pbori_gb_doc2.patch` addresses Burcin's comments above. It should be applied on top of the first patch.



---

archive/issue_comments_013253.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-02-05T13:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2051#issuecomment-13253",
    "user": "https://github.com/burcin"
}
```

Looks good to me.



---

archive/issue_comments_013254.json:
```json
{
    "body": "Merged both patches in Sage 2.10.2.alpha0",
    "created_at": "2008-02-07T05:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2051#issuecomment-13254",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 2.10.2.alpha0



---

archive/issue_events_002212.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-07T05:18:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2051",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2051#event-2212"
}
```



---

archive/issue_comments_013255.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-07T05:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2051#issuecomment-13255",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
