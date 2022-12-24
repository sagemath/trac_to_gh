# Issue 5228: [with patch, needs review] make composite_fields and galois_closure return maps and preserve embeddings

archive/issues_005228.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: number fields composite fields galois closure embedding coercion\n\nThe patches describe and doctest this better, but...\n\n* Extends composite_fields and galois_closure to return maps when asked\n\n* Uses the new coercion embedding to only return \"coherent\" compositions if embeddings are specified.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5228\n\n",
    "created_at": "2009-02-10T18:20:38Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] make composite_fields and galois_closure return maps and preserve embeddings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5228",
    "user": "@ncalexan"
}
```
Assignee: @williamstein

Keywords: number fields composite fields galois closure embedding coercion

The patches describe and doctest this better, but...

* Extends composite_fields and galois_closure to return maps when asked

* Uses the new coercion embedding to only return "coherent" compositions if embeddings are specified.

Issue created by migration from https://trac.sagemath.org/ticket/5228





---

archive/issue_comments_040073.json:
```json
{
    "body": "Attachment [trac_5228-composite-fields.patch](tarball://root/attachments/some-uuid/ticket5228/trac_5228-composite-fields.patch) by @ncalexan created at 2009-02-10 18:26:29",
    "created_at": "2009-02-10T18:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5228#issuecomment-40073",
    "user": "@ncalexan"
}
```

Attachment [trac_5228-composite-fields.patch](tarball://root/attachments/some-uuid/ticket5228/trac_5228-composite-fields.patch) by @ncalexan created at 2009-02-10 18:26:29



---

archive/issue_comments_040074.json:
```json
{
    "body": "Attachment [trac_5228-composite-fields-embeddings.patch](tarball://root/attachments/some-uuid/ticket5228/trac_5228-composite-fields-embeddings.patch) by @ncalexan created at 2009-02-10 18:28:56\n\nApply `trac_5228-composite-fields.patch` and then `trac_5228-composite-fields-embeddings.patch`",
    "created_at": "2009-02-10T18:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5228#issuecomment-40074",
    "user": "@ncalexan"
}
```

Attachment [trac_5228-composite-fields-embeddings.patch](tarball://root/attachments/some-uuid/ticket5228/trac_5228-composite-fields-embeddings.patch) by @ncalexan created at 2009-02-10 18:28:56

Apply `trac_5228-composite-fields.patch` and then `trac_5228-composite-fields-embeddings.patch`



---

archive/issue_comments_040075.json:
```json
{
    "body": "Assign it to 3.4.1 for now. If it is reviewed in time and passes doctests it will go into 3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T05:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5228#issuecomment-40075",
    "user": "mabshoff"
}
```

Assign it to 3.4.1 for now. If it is reviewed in time and passes doctests it will go into 3.3.

Cheers,

Michael



---

archive/issue_comments_040076.json:
```json
{
    "body": "Since someone beat me to #5231, I had to review this one...\n\nLooks good.",
    "created_at": "2009-02-11T09:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5228#issuecomment-40076",
    "user": "@aghitza"
}
```

Since someone beat me to #5231, I had to review this one...

Looks good.



---

archive/issue_comments_040077.json:
```json
{
    "body": "Merged both patches in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-13T03:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5228#issuecomment-40077",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_040078.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-13T03:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5228#issuecomment-40078",
    "user": "mabshoff"
}
```

Resolution: fixed
