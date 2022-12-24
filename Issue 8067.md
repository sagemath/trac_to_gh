# Issue 8067: New linbox-1.1.6.p3.spkg works with Open Solaris 64 bit

archive/issues_008067.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  drkirby was\n\nMake sure SAGE64=\"yes\" is respected on Open Solaris 64 bit\n\nThe package can be found here:\n[http://boxen.math.washington.edu/home/jsp/ports/linbox-1.1.6.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/linbox-1.1.6.p3.spkg)\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8067\n\n",
    "created_at": "2010-01-25T23:04:06Z",
    "labels": [
        "porting",
        "major",
        "enhancement"
    ],
    "title": "New linbox-1.1.6.p3.spkg works with Open Solaris 64 bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8067",
    "user": "jsp"
}
```
Assignee: drkirkby

CC:  drkirby was

Make sure SAGE64="yes" is respected on Open Solaris 64 bit

The package can be found here:
[http://boxen.math.washington.edu/home/jsp/ports/linbox-1.1.6.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/linbox-1.1.6.p3.spkg)

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/8067





---

archive/issue_comments_070695.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-25T23:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8067#issuecomment-70695",
    "user": "jsp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070696.json:
```json
{
    "body": "Without some way to be able to see what you have changed, it is difficult to review. Again, without a patch, it could never be integrated with anyone else that might change this package. \n\nI really like the fact that you have made a complete .spkg file, as patches are difficult to review too. But having both, it's possible to see the changes, and test it complete. \n\nDave",
    "created_at": "2010-01-26T11:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8067#issuecomment-70696",
    "user": "drkirkby"
}
```

Without some way to be able to see what you have changed, it is difficult to review. Again, without a patch, it could never be integrated with anyone else that might change this package. 

I really like the fact that you have made a complete .spkg file, as patches are difficult to review too. But having both, it's possible to see the changes, and test it complete. 

Dave



---

archive/issue_comments_070697.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-26T11:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8067#issuecomment-70697",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070698.json:
```json
{
    "body": "Attachment [linbox-1.1.6.p3.patch](tarball://root/attachments/some-uuid/ticket8067/linbox-1.1.6.p3.patch) by jsp created at 2010-01-26 18:15:23",
    "created_at": "2010-01-26T18:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8067#issuecomment-70698",
    "user": "jsp"
}
```

Attachment [linbox-1.1.6.p3.patch](tarball://root/attachments/some-uuid/ticket8067/linbox-1.1.6.p3.patch) by jsp created at 2010-01-26 18:15:23



---

archive/issue_comments_070699.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-26T18:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8067#issuecomment-70699",
    "user": "jsp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070700.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2010-01-27T12:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8067#issuecomment-70700",
    "user": "drkirkby"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_070701.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-27T12:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8067#issuecomment-70701",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070702.json:
```json
{
    "body": "That's fine. My only long-term concern is that hard-coding -m64 is not a great idea, since it is not portable, but hopefully we will have a solution to that. \n\nI've changed it to 'defect'  rather than 'enhancement', as the latter is supposed to be used where you have enhanced Sage - i.e normally by adding functionality, or similar. But in this case you have corrected a defect. \n\nDave",
    "created_at": "2010-01-27T12:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8067#issuecomment-70702",
    "user": "drkirkby"
}
```

That's fine. My only long-term concern is that hard-coding -m64 is not a great idea, since it is not portable, but hopefully we will have a solution to that. 

I've changed it to 'defect'  rather than 'enhancement', as the latter is supposed to be used where you have enhanced Sage - i.e normally by adding functionality, or similar. But in this case you have corrected a defect. 

Dave



---

archive/issue_comments_070703.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8067",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8067#issuecomment-70703",
    "user": "mpatel"
}
```

Resolution: fixed
