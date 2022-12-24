# Issue 3757: [with preliminary patch, needs review] change printing for intervals (and AA/QQbar)

archive/issues_003757.json:
```json
{
    "body": "Assignee: somebody\n\nThis patch introduces \"question-mark style printing\" for intervals, where instead of [1.123 .. 1.125] we get 1.124? (the question mark means that the previous digit may be off by +/- 1).  (The slightly unfortunate thing is that [1.1238 .. 1.1242] will also print as 1.124?, so the new default printing loses a lot of information about exactly how tight the interval is.)\n\nI'm going to post a preliminary patch first, that actually changes the printing and adds extensive docstrings and doctests for the new/changed methods.  This leaves many, many doctests broken throughout the rest of Sage.\n\nIf/when this preliminary patch is positively reviewed, I will go ahead and post a follow-on patch that fixes all the doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3757\n\n",
    "created_at": "2008-08-02T14:33:47Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with preliminary patch, needs review] change printing for intervals (and AA/QQbar)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3757",
    "user": "cwitty"
}
```
Assignee: somebody

This patch introduces "question-mark style printing" for intervals, where instead of [1.123 .. 1.125] we get 1.124? (the question mark means that the previous digit may be off by +/- 1).  (The slightly unfortunate thing is that [1.1238 .. 1.1242] will also print as 1.124?, so the new default printing loses a lot of information about exactly how tight the interval is.)

I'm going to post a preliminary patch first, that actually changes the printing and adds extensive docstrings and doctests for the new/changed methods.  This leaves many, many doctests broken throughout the rest of Sage.

If/when this preliminary patch is positively reviewed, I will go ahead and post a follow-on patch that fixes all the doctests.

Issue created by migration from https://trac.sagemath.org/ticket/3757





---

archive/issue_comments_026685.json:
```json
{
    "body": "Attachment [trac3757-question-printing-part1.patch](tarball://root/attachments/some-uuid/ticket3757/trac3757-question-printing-part1.patch) by jason created at 2008-08-02 16:19:57\n\nLooks good to me!  Positive review for part1.patch",
    "created_at": "2008-08-02T16:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3757#issuecomment-26685",
    "user": "jason"
}
```

Attachment [trac3757-question-printing-part1.patch](tarball://root/attachments/some-uuid/ticket3757/trac3757-question-printing-part1.patch) by jason created at 2008-08-02 16:19:57

Looks good to me!  Positive review for part1.patch



---

archive/issue_comments_026686.json:
```json
{
    "body": "Attachment [trac3757-question-printing-part2.patch](tarball://root/attachments/some-uuid/ticket3757/trac3757-question-printing-part2.patch) by cwitty created at 2008-08-02 20:35:24",
    "created_at": "2008-08-02T20:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3757#issuecomment-26686",
    "user": "cwitty"
}
```

Attachment [trac3757-question-printing-part2.patch](tarball://root/attachments/some-uuid/ticket3757/trac3757-question-printing-part2.patch) by cwitty created at 2008-08-02 20:35:24



---

archive/issue_comments_026687.json:
```json
{
    "body": "OK, I've added the rest of the patch; after applying both patches, testall passes (on 32-bit and 64-bit x86 Debian testing).",
    "created_at": "2008-08-02T20:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3757#issuecomment-26687",
    "user": "cwitty"
}
```

OK, I've added the rest of the patch; after applying both patches, testall passes (on 32-bit and 64-bit x86 Debian testing).



---

archive/issue_comments_026688.json:
```json
{
    "body": "REVIEW:\n\nI just read through both patches.  Wow, these are models of how to write good quality code that is very very well documented!!\n\nAlso, I very much appreciate the added discussion of the \"error digits\" in the second patch.\n\nThis passes all tests for me on OS X.  Thus positive review for the whole thing.",
    "created_at": "2008-08-03T18:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3757#issuecomment-26688",
    "user": "was"
}
```

REVIEW:

I just read through both patches.  Wow, these are models of how to write good quality code that is very very well documented!!

Also, I very much appreciate the added discussion of the "error digits" in the second patch.

This passes all tests for me on OS X.  Thus positive review for the whole thing.



---

archive/issue_comments_026689.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-05T23:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3757#issuecomment-26689",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha1



---

archive/issue_comments_026690.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-05T23:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3757#issuecomment-26690",
    "user": "mabshoff"
}
```

Resolution: fixed
