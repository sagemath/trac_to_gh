# Issue 5228: [with patch, needs review] make composite_fields and galois_closure return maps and preserve embeddings

archive/issues_005228.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: number fields composite fields galois closure embedding coercion\n\nThe patches describe and doctest this better, but...\n\n* Extends composite_fields and galois_closure to return maps when asked\n\n* Uses the new coercion embedding to only return \"coherent\" compositions if embeddings are specified.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5228\n\n",
    "created_at": "2009-02-10T18:20:38Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] make composite_fields and galois_closure return maps and preserve embeddings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5228",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

Keywords: number fields composite fields galois closure embedding coercion

The patches describe and doctest this better, but...

* Extends composite_fields and galois_closure to return maps when asked

* Uses the new coercion embedding to only return "coherent" compositions if embeddings are specified.

Issue created by migration from https://trac.sagemath.org/ticket/5228





---

archive/issue_comments_039995.json:
```json
{
    "body": "Attachment [trac_5228-composite-fields.patch](tarball://root/attachments/some-uuid/ticket5228/trac_5228-composite-fields.patch) by @ncalexan created at 2009-02-10 18:26:29",
    "created_at": "2009-02-10T18:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5228#issuecomment-39995",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_5228-composite-fields.patch](tarball://root/attachments/some-uuid/ticket5228/trac_5228-composite-fields.patch) by @ncalexan created at 2009-02-10 18:26:29



---

archive/issue_comments_039996.json:
```json
{
    "body": "Attachment [trac_5228-composite-fields-embeddings.patch](tarball://root/attachments/some-uuid/ticket5228/trac_5228-composite-fields-embeddings.patch) by @ncalexan created at 2009-02-10 18:28:56\n\nApply `trac_5228-composite-fields.patch` and then `trac_5228-composite-fields-embeddings.patch`",
    "created_at": "2009-02-10T18:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5228#issuecomment-39996",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_5228-composite-fields-embeddings.patch](tarball://root/attachments/some-uuid/ticket5228/trac_5228-composite-fields-embeddings.patch) by @ncalexan created at 2009-02-10 18:28:56

Apply `trac_5228-composite-fields.patch` and then `trac_5228-composite-fields-embeddings.patch`



---

archive/issue_comments_039997.json:
```json
{
    "body": "Assign it to 3.4.1 for now. If it is reviewed in time and passes doctests it will go into 3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T05:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5228#issuecomment-39997",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Assign it to 3.4.1 for now. If it is reviewed in time and passes doctests it will go into 3.3.

Cheers,

Michael



---

archive/issue_comments_039998.json:
```json
{
    "body": "Since someone beat me to #5231, I had to review this one...\n\nLooks good.",
    "created_at": "2009-02-11T09:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5228#issuecomment-39998",
    "user": "https://github.com/aghitza"
}
```

Since someone beat me to #5231, I had to review this one...

Looks good.



---

archive/issue_comments_039999.json:
```json
{
    "body": "Merged both patches in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-13T03:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5228#issuecomment-39999",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_events_005485.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-13T03:58:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5228",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5228#event-5485"
}
```



---

archive/issue_comments_040000.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-13T03:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5228#issuecomment-40000",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
