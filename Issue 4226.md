# Issue 4226: [with patch, needs reivew] Real Lazy Field

archive/issues_004226.json:
```json
{
    "body": "Assignee: @robertwb\n\nThis is needed for number field embedding. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4226\n\n",
    "created_at": "2008-09-30T21:10:57Z",
    "labels": [
        "component: coercion"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, needs reivew] Real Lazy Field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4226",
    "user": "https://github.com/robertwb"
}
```
Assignee: @robertwb

This is needed for number field embedding. 

Issue created by migration from https://trac.sagemath.org/ticket/4226





---

archive/issue_comments_030654.json:
```json
{
    "body": "Attachment [4226-real-lazy.patch](tarball://root/attachments/some-uuid/ticket4226/4226-real-lazy.patch) by @mwhansen created at 2008-10-01 06:48:32",
    "created_at": "2008-10-01T06:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4226#issuecomment-30654",
    "user": "https://github.com/mwhansen"
}
```

Attachment [4226-real-lazy.patch](tarball://root/attachments/some-uuid/ticket4226/4226-real-lazy.patch) by @mwhansen created at 2008-10-01 06:48:32



---

archive/issue_comments_030655.json:
```json
{
    "body": "Attachment [trac_4226-2.patch](tarball://root/attachments/some-uuid/ticket4226/trac_4226-2.patch) by @mwhansen created at 2008-10-01 06:49:26\n\nLooks good to me.  Note that the second patch should be applied as well since we got rid of the *_impl methods.",
    "created_at": "2008-10-01T06:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4226#issuecomment-30655",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4226-2.patch](tarball://root/attachments/some-uuid/ticket4226/trac_4226-2.patch) by @mwhansen created at 2008-10-01 06:49:26

Looks good to me.  Note that the second patch should be applied as well since we got rid of the *_impl methods.



---

archive/issue_comments_030656.json:
```json
{
    "body": "The doctest \"hash(RLF(sin(1)))\" should probably not be #random, but should have separate #32 and #64 bit output.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-01T08:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4226#issuecomment-30656",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The doctest "hash(RLF(sin(1)))" should probably not be #random, but should have separate #32 and #64 bit output.

Cheers,

Michael



---

archive/issue_comments_030657.json:
```json
{
    "body": "Fix a typo so the ticket is picked up by reports.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-01T08:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4226#issuecomment-30657",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fix a typo so the ticket is picked up by reports.

Cheers,

Michael



---

archive/issue_comments_030658.json:
```json
{
    "body": "I fixed the 32 vs. 64 bit hashing issue in a trivial patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-01T10:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4226#issuecomment-30658",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I fixed the 32 vs. 64 bit hashing issue in a trivial patch.

Cheers,

Michael



---

archive/issue_comments_030659.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-01T10:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4226#issuecomment-30659",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030660.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha3",
    "created_at": "2008-10-01T10:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4226#issuecomment-30660",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha3



---

archive/issue_comments_030661.json:
```json
{
    "body": "Thanks for the fixes (I should have remembered that arithmetic patch got in).",
    "created_at": "2008-10-01T19:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4226#issuecomment-30661",
    "user": "https://github.com/robertwb"
}
```

Thanks for the fixes (I should have remembered that arithmetic patch got in).
