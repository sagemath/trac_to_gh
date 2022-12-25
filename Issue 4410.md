# Issue 4410: [with patch, positive review] Map.__pow__ should return identity for power 0

archive/issues_004410.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @robertwb\n\n`sage.categories.map.Map.__pow__` calls `generic_power`, which messes up power 0. There is this todo note there:\n\n```\n        # todo -- what about the case n=0 -- need to specify the identity map somehow.\n```\n\nAttached patch returns the identity map for power 0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4410\n\n",
    "closed_at": "2008-10-31T15:36:46Z",
    "created_at": "2008-10-31T09:05:10Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, positive review] Map.__pow__ should return identity for power 0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4410",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

CC:  @robertwb

`sage.categories.map.Map.__pow__` calls `generic_power`, which messes up power 0. There is this todo note there:

```
        # todo -- what about the case n=0 -- need to specify the identity map somehow.
```

Attached patch returns the identity map for power 0.

Issue created by migration from https://trac.sagemath.org/ticket/4410





---

archive/issue_comments_032358.json:
```json
{
    "body": "make Map.__pow__ return identity for power 0",
    "created_at": "2008-10-31T09:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4410#issuecomment-32358",
    "user": "https://github.com/burcin"
}
```

make Map.__pow__ return identity for power 0



---

archive/issue_comments_032359.json:
```json
{
    "body": "Attachment [trac_4410_map_pow.patch](tarball://root/attachments/some-uuid/ticket4410/trac_4410_map_pow.patch) by mabshoff created at 2008-10-31 15:35:42\n\nThis is the suggested fix discussed by RobertWB and Burcin in IRC last night. The code looks correct and passes doctests, positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T15:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4410#issuecomment-32359",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4410_map_pow.patch](tarball://root/attachments/some-uuid/ticket4410/trac_4410_map_pow.patch) by mabshoff created at 2008-10-31 15:35:42

This is the suggested fix discussed by RobertWB and Burcin in IRC last night. The code looks correct and passes doctests, positive review.

Cheers,

Michael



---

archive/issue_comments_032360.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T15:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4410#issuecomment-32360",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_comments_032361.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T15:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4410#issuecomment-32361",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009961.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T15:36:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4410",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4410#event-9961"
}
```
