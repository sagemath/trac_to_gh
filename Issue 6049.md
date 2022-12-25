# Issue 6049: [with patch, positive review] bitset complement zeroes out last word if the bitset is a multiple of the word size

archive/issues_006049.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @rlmill @robertwb\n\nI introduced a serious error in bitset complements when the bitsets are multiples of the word size.  This patch corrects this and doctests the correct behavior.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6049\n\n",
    "closed_at": "2009-05-18T23:09:30Z",
    "created_at": "2009-05-16T18:27:46Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, positive review] bitset complement zeroes out last word if the bitset is a multiple of the word size",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6049",
    "user": "https://github.com/jasongrout"
}
```
Assignee: cwitty

CC:  @rlmill @robertwb

I introduced a serious error in bitset complements when the bitsets are multiples of the word size.  This patch corrects this and doctests the correct behavior.

Issue created by migration from https://trac.sagemath.org/ticket/6049





---

archive/issue_comments_048096.json:
```json
{
    "body": "Attachment [bitset-complement-wordsize.patch](tarball://root/attachments/some-uuid/ticket6049/bitset-complement-wordsize.patch) by @jasongrout created at 2009-05-16 18:28:14",
    "created_at": "2009-05-16T18:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6049#issuecomment-48096",
    "user": "https://github.com/jasongrout"
}
```

Attachment [bitset-complement-wordsize.patch](tarball://root/attachments/some-uuid/ticket6049/bitset-complement-wordsize.patch) by @jasongrout created at 2009-05-16 18:28:14



---

archive/issue_comments_048097.json:
```json
{
    "body": "Code looks good, doctests pass.  Positive review.",
    "created_at": "2009-05-16T22:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6049#issuecomment-48097",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Code looks good, doctests pass.  Positive review.



---

archive/issue_events_014204.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-18T23:09:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6049",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6049#event-14204"
}
```



---

archive/issue_comments_048098.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-18T23:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6049#issuecomment-48098",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_048099.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-18T23:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6049#issuecomment-48099",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
