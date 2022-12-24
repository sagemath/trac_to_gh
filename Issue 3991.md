# Issue 3991: [with patch, needs review] Matrix_mod2_dense.__hash__ 32-bit doctest failure

archive/issues_003991.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @JohnCremona\n\nKeywords: doctest failure\n\nJohn reported this:\n> The third is this:\n>> File \"/home/john/sage-3.1.2.alpha1/tmp/matrix_mod2_dense.py\", line 267:\n>>     sage: hex(hash(A))\n>> Expected:\n>>     '0xdeadbeed'\n>> Got:\n>>     '-0x21524113'\n\nIssue created by migration from https://trac.sagemath.org/ticket/3991\n\n",
    "created_at": "2008-08-29T11:30:54Z",
    "labels": [
        "linear algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] Matrix_mod2_dense.__hash__ 32-bit doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3991",
    "user": "@malb"
}
```
Assignee: @malb

CC:  @JohnCremona

Keywords: doctest failure

John reported this:
> The third is this:
>> File "/home/john/sage-3.1.2.alpha1/tmp/matrix_mod2_dense.py", line 267:
>>     sage: hex(hash(A))
>> Expected:
>>     '0xdeadbeed'
>> Got:
>>     '-0x21524113'

Issue created by migration from https://trac.sagemath.org/ticket/3991





---

archive/issue_comments_028687.json:
```json
{
    "body": "Attachment [trac_3991_matrix_mod2_dense_hash_32_bit.patch](tarball://root/attachments/some-uuid/ticket3991/trac_3991_matrix_mod2_dense_hash_32_bit.patch) by mabshoff created at 2008-08-30 01:43:22\n\nJohn,\n\ncan you verify that this patch fixes the issue for you on your 32 bit box? Otherwise this is an \"obvious\" positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T01:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3991#issuecomment-28687",
    "user": "mabshoff"
}
```

Attachment [trac_3991_matrix_mod2_dense_hash_32_bit.patch](tarball://root/attachments/some-uuid/ticket3991/trac_3991_matrix_mod2_dense_hash_32_bit.patch) by mabshoff created at 2008-08-30 01:43:22

John,

can you verify that this patch fixes the issue for you on your 32 bit box? Otherwise this is an "obvious" positive review.

Cheers,

Michael



---

archive/issue_comments_028688.json:
```json
{
    "body": "Patch applies fine and all doctests in sage.matrix pass.  OK!",
    "created_at": "2008-08-30T10:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3991#issuecomment-28688",
    "user": "@JohnCremona"
}
```

Patch applies fine and all doctests in sage.matrix pass.  OK!



---

archive/issue_comments_028689.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha3",
    "created_at": "2008-08-30T18:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3991#issuecomment-28689",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha3



---

archive/issue_comments_028690.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-30T18:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3991#issuecomment-28690",
    "user": "mabshoff"
}
```

Resolution: fixed
