# Issue 9331: can't build PDF version of reference manual in Sage 4.4.4

archive/issues_009331.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  sage-combinat\n\nFrom [sage-devel](https://groups.google.com/group/sage-devel/browse_thread/thread/bd0ef674ff168fe7):\n\n```\nIn Sage 4.4.4, I can't build the PDF version of the reference manual,\neven though the HTML version builds fine. Here is the error messsage:\n\nOverfull \\hbox (41.96407pt too wide) in paragraph at lines 73487--73489\n[]\\T1/pcr/m/n/10 MyClass2.__classcall__() \\T1/ptm/m/n/10 should re-turn the re-\nsult of \\T1/pcr/m/n/10 UniqueRepresentation.__classcall__()\n[890]\n! TeX capacity exceeded, sorry [input stack size=5000].\n\\reserved@a ->\\def \\reserved@a\n                               *{\\ttl@assign@i {\\@tempskipb }}\\reserved@a\nl.73597 ...{UniqueRepresentation}} and unpickling}\n\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on reference.log.\nmake: *** [reference.pdf] Error 1 \n```\n\nThis is traced to ticket #9106.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9331\n\n",
    "created_at": "2010-06-24T17:56:34Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "can't build PDF version of reference manual in Sage 4.4.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9331",
    "user": "mvngu"
}
```
Assignee: mvngu

CC:  sage-combinat

From [sage-devel](https://groups.google.com/group/sage-devel/browse_thread/thread/bd0ef674ff168fe7):

```
In Sage 4.4.4, I can't build the PDF version of the reference manual,
even though the HTML version builds fine. Here is the error messsage:

Overfull \hbox (41.96407pt too wide) in paragraph at lines 73487--73489
[]\T1/pcr/m/n/10 MyClass2.__classcall__() \T1/ptm/m/n/10 should re-turn the re-
sult of \T1/pcr/m/n/10 UniqueRepresentation.__classcall__()
[890]
! TeX capacity exceeded, sorry [input stack size=5000].
\reserved@a ->\def \reserved@a
                               *{\ttl@assign@i {\@tempskipb }}\reserved@a
l.73597 ...{UniqueRepresentation}} and unpickling}

!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on reference.log.
make: *** [reference.pdf] Error 1 
```

This is traced to ticket #9106.

Issue created by migration from https://trac.sagemath.org/ticket/9331





---

archive/issue_comments_088024.json:
```json
{
    "body": "Attachment [trac_9331-pdf-build.patch](tarball://root/attachments/some-uuid/ticket9331/trac_9331-pdf-build.patch) by mvngu created at 2010-06-24 18:01:00",
    "created_at": "2010-06-24T18:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9331#issuecomment-88024",
    "user": "mvngu"
}
```

Attachment [trac_9331-pdf-build.patch](tarball://root/attachments/some-uuid/ticket9331/trac_9331-pdf-build.patch) by mvngu created at 2010-06-24 18:01:00



---

archive/issue_comments_088025.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-24T18:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9331#issuecomment-88025",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088026.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-25T05:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9331#issuecomment-88026",
    "user": "@nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088027.json:
```json
{
    "body": "I am fine with the change! Thanks for tracking it down. Please open a new ticket to remind us about putting the link back once sphinx is fixed!",
    "created_at": "2010-06-25T05:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9331#issuecomment-88027",
    "user": "@nthiery"
}
```

I am fine with the change! Thanks for tracking it down. Please open a new ticket to remind us about putting the link back once sphinx is fixed!



---

archive/issue_comments_088028.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-06T08:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9331#issuecomment-88028",
    "user": "@rlmill"
}
```

Resolution: fixed
