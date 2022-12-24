# Issue 6049: [with patch, needs review] bitset complement zeroes out last word if the bitset is a multiple of the word size

archive/issues_006049.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @rlmill @robertwb\n\nI introduced a serious error in bitset complements when the bitsets are multiples of the word size.  This patch corrects this and doctests the correct behavior.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6049\n\n",
    "created_at": "2009-05-16T18:27:46Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] bitset complement zeroes out last word if the bitset is a multiple of the word size",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6049",
    "user": "@jasongrout"
}
```
Assignee: cwitty

CC:  @rlmill @robertwb

I introduced a serious error in bitset complements when the bitsets are multiples of the word size.  This patch corrects this and doctests the correct behavior.

Issue created by migration from https://trac.sagemath.org/ticket/6049





---

archive/issue_comments_048187.json:
```json
{
    "body": "Attachment [bitset-complement-wordsize.patch](tarball://root/attachments/some-uuid/ticket6049/bitset-complement-wordsize.patch) by @jasongrout created at 2009-05-16 18:28:14",
    "created_at": "2009-05-16T18:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6049#issuecomment-48187",
    "user": "@jasongrout"
}
```

Attachment [bitset-complement-wordsize.patch](tarball://root/attachments/some-uuid/ticket6049/bitset-complement-wordsize.patch) by @jasongrout created at 2009-05-16 18:28:14



---

archive/issue_comments_048188.json:
```json
{
    "body": "Code looks good, doctests pass.  Positive review.",
    "created_at": "2009-05-16T22:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6049#issuecomment-48188",
    "user": "cwitty"
}
```

Code looks good, doctests pass.  Positive review.



---

archive/issue_comments_048189.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-18T23:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6049#issuecomment-48189",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_048190.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-18T23:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6049#issuecomment-48190",
    "user": "mabshoff"
}
```

Resolution: fixed
