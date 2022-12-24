# Issue 4849: add functionality for computing Heegner points to Sage

archive/issues_004849.json:
```json
{
    "body": "Assignee: was\n\nSee #4848 for a motivation. Attached is some Magma code, but note that according to William\n\n```\nThen the file heegner.py should be attached to that ticket, since to do that \nticket, one might want to port some of what's in there to Sage. That said, it's \nnot so simple, since better algorithms for computing Heegner points were found \nafter that code was written.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4849\n\n",
    "created_at": "2008-12-21T22:08:10Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "add functionality for computing Heegner points to Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4849",
    "user": "mabshoff"
}
```
Assignee: was

See #4848 for a motivation. Attached is some Magma code, but note that according to William

```
Then the file heegner.py should be attached to that ticket, since to do that 
ticket, one might want to port some of what's in there to Sage. That said, it's 
not so simple, since better algorithms for computing Heegner points were found 
after that code was written.
```


Issue created by migration from https://trac.sagemath.org/ticket/4849





---

archive/issue_comments_036768.json:
```json
{
    "body": "Attachment [heegner.py](tarball://root/attachments/some-uuid/ticket4849/heegner.py) by mabshoff created at 2008-12-21 22:10:31\n\nThis is mostly Magma code",
    "created_at": "2008-12-21T22:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4849#issuecomment-36768",
    "user": "mabshoff"
}
```

Attachment [heegner.py](tarball://root/attachments/some-uuid/ticket4849/heegner.py) by mabshoff created at 2008-12-21 22:10:31

This is mostly Magma code



---

archive/issue_comments_036769.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-12-21T22:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4849#issuecomment-36769",
    "user": "mabshoff"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_036770.json:
```json
{
    "body": "This is fixed by #6045. I'm flagging this to \"positive review\" so it will come to the attention of mvngu, who has the authority to close tickets as 4.1.1 release manager.",
    "created_at": "2009-07-15T20:39:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4849#issuecomment-36770",
    "user": "davidloeffler"
}
```

This is fixed by #6045. I'm flagging this to "positive review" so it will come to the attention of mvngu, who has the authority to close tickets as 4.1.1 release manager.



---

archive/issue_comments_036771.json:
```json
{
    "body": "The patches on #6045 result in some numerical noise. Once that is fixed, this ticket can get positive review. At the moment, I don't have the privilege to close tickets. But I've merged some tickets in my tree. If you're interested, refer to the file\n\nhttp://sage.math.washington.edu/home/mvngu/release/merged-tkt.txt",
    "created_at": "2009-07-16T10:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4849#issuecomment-36771",
    "user": "mvngu"
}
```

The patches on #6045 result in some numerical noise. Once that is fixed, this ticket can get positive review. At the moment, I don't have the privilege to close tickets. But I've merged some tickets in my tree. If you're interested, refer to the file

http://sage.math.washington.edu/home/mvngu/release/merged-tkt.txt



---

archive/issue_comments_036772.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-07-20T15:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4849#issuecomment-36772",
    "user": "mvngu"
}
```

Resolution: duplicate



---

archive/issue_comments_036773.json:
```json
{
    "body": "I'm closing this as a duplicate of #6045.",
    "created_at": "2009-07-20T15:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4849#issuecomment-36773",
    "user": "mvngu"
}
```

I'm closing this as a duplicate of #6045.
