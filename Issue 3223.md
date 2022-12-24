# Issue 3223: notebook -- it is now broken on the iphone

archive/issues_003223.json:
```json
{
    "body": "Assignee: boothby\n\nNow I think left or right parenthesis sends carriage return.  I think this likely has something to do with updating the keyboard support for the new safari browser.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/3223\n\n",
    "created_at": "2008-05-16T18:45:37Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "notebook -- it is now broken on the iphone",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3223",
    "user": "was"
}
```
Assignee: boothby

Now I think left or right parenthesis sends carriage return.  I think this likely has something to do with updating the keyboard support for the new safari browser.  

Issue created by migration from https://trac.sagemath.org/ticket/3223





---

archive/issue_comments_022307.json:
```json
{
    "body": "Attachment [sage-3223.patch](tarball://root/attachments/some-uuid/ticket3223/sage-3223.patch) by was created at 2008-11-17 15:46:10",
    "created_at": "2008-11-17T15:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3223#issuecomment-22307",
    "user": "was"
}
```

Attachment [sage-3223.patch](tarball://root/attachments/some-uuid/ticket3223/sage-3223.patch) by was created at 2008-11-17 15:46:10



---

archive/issue_comments_022308.json:
```json
{
    "body": "I fixed this by disabling *all* keyboard shortcut handling on the iphone.  This is a good idea, since the iphone does not have any of the keys needed to send any of the keyboard shortcuts, and it gets around the problem.  \n\nTo referee this 3-line patch, just verify that clearly I didn't break anything, since all I did was add a special case to check for the iphone string in the browser UA tag, and only then disable keyboard shortcut handling.",
    "created_at": "2008-11-17T15:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3223#issuecomment-22308",
    "user": "was"
}
```

I fixed this by disabling *all* keyboard shortcut handling on the iphone.  This is a good idea, since the iphone does not have any of the keys needed to send any of the keyboard shortcuts, and it gets around the problem.  

To referee this 3-line patch, just verify that clearly I didn't break anything, since all I did was add a special case to check for the iphone string in the browser UA tag, and only then disable keyboard shortcut handling.



---

archive/issue_comments_022309.json:
```json
{
    "body": "I'm moving this back to 3.2.  It's harmless (famous last words), and I really think having iphone support working again is an extremely important bug fix.",
    "created_at": "2008-11-17T15:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3223#issuecomment-22309",
    "user": "was"
}
```

I'm moving this back to 3.2.  It's harmless (famous last words), and I really think having iphone support working again is an extremely important bug fix.



---

archive/issue_comments_022310.json:
```json
{
    "body": "+1",
    "created_at": "2008-11-17T20:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3223#issuecomment-22310",
    "user": "boothby"
}
```

+1



---

archive/issue_comments_022311.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-11-18T06:49:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3223#issuecomment-22311",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_022312.json:
```json
{
    "body": "Merged in Sage 3.2.rc2",
    "created_at": "2008-11-18T18:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3223#issuecomment-22312",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.rc2



---

archive/issue_comments_022313.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-18T18:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3223#issuecomment-22313",
    "user": "mabshoff"
}
```

Resolution: fixed
