# Issue 8352: twisted-8.2.0.p1 fails to build in Open Solaris x64 as 64 bit even if SAGE64=yes

archive/issues_008352.json:
```json
{
    "body": "Assignee: drkirkby\n\ntwisted builds in 32 bit mode on Open Solaris x64.\n\nA fix is coming up.\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8352\n\n",
    "created_at": "2010-02-24T21:07:49Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "title": "twisted-8.2.0.p1 fails to build in Open Solaris x64 as 64 bit even if SAGE64=yes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8352",
    "user": "jsp"
}
```
Assignee: drkirkby

twisted builds in 32 bit mode on Open Solaris x64.

A fix is coming up.

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/8352





---

archive/issue_comments_074592.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-24T21:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8352#issuecomment-74592",
    "user": "jsp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074593.json:
```json
{
    "body": "Attachment [twisted-8.2.0.p2.patch](tarball://root/attachments/some-uuid/ticket8352/twisted-8.2.0.p2.patch) by jsp created at 2010-02-24 21:17:04\n\nThe new spkg can be found here:\n\n[http://boxen.math.washington.edu/home/jsp/ports/twisted-8.2.0.p2.spkg](http://boxen.math.washington.edu/home/jsp/ports/twisted-8.2.0.p2.spkg)\n\nJaap",
    "created_at": "2010-02-24T21:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8352#issuecomment-74593",
    "user": "jsp"
}
```

Attachment [twisted-8.2.0.p2.patch](tarball://root/attachments/some-uuid/ticket8352/twisted-8.2.0.p2.patch) by jsp created at 2010-02-24 21:17:04

The new spkg can be found here:

[http://boxen.math.washington.edu/home/jsp/ports/twisted-8.2.0.p2.spkg](http://boxen.math.washington.edu/home/jsp/ports/twisted-8.2.0.p2.spkg)

Jaap



---

archive/issue_comments_074594.json:
```json
{
    "body": "You might want to take a look at #7552 too, as that is an update to the twisted package. There are two tickets both updating twisted. I will put a note on that ticket about this one. \n\n\nI don't know the best way to handle this. I could give this positive review now (there is nothing wrong with it), but I'm not sure of the most logical way to do about this.",
    "created_at": "2010-02-24T21:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8352#issuecomment-74594",
    "user": "drkirkby"
}
```

You might want to take a look at #7552 too, as that is an update to the twisted package. There are two tickets both updating twisted. I will put a note on that ticket about this one. 


I don't know the best way to handle this. I could give this positive review now (there is nothing wrong with it), but I'm not sure of the most logical way to do about this.



---

archive/issue_comments_074595.json:
```json
{
    "body": "With no response on how to handle this, I'm giving this positive review. I'll make a note on #7552 that these changes have been reviewed, and that the ticket will have to incorporate your changes.",
    "created_at": "2010-02-25T03:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8352#issuecomment-74595",
    "user": "drkirkby"
}
```

With no response on how to handle this, I'm giving this positive review. I'll make a note on #7552 that these changes have been reviewed, and that the ticket will have to incorporate your changes.



---

archive/issue_comments_074596.json:
```json
{
    "body": "The \"p2\" spkg at #7552 includes the patch.",
    "created_at": "2010-02-25T07:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8352#issuecomment-74596",
    "user": "mpatel"
}
```

The "p2" spkg at #7552 includes the patch.



---

archive/issue_comments_074597.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> The \"p2\" spkg at #7552 includes the patch.\n\nMeaning? Does this mean this ticket will be closed?\n\nJaap",
    "created_at": "2010-02-25T11:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8352#issuecomment-74597",
    "user": "jsp"
}
```

Replying to [comment:4 mpatel]:
> The "p2" spkg at #7552 includes the patch.

Meaning? Does this mean this ticket will be closed?

Jaap



---

archive/issue_comments_074598.json:
```json
{
    "body": "It can't be closed yet (and in any case you should not close it, but leave a message for the release manager to do so) until #7552 is merged. \n\nBut looking at #7552, there does seem little reason that can't be reviewed quite easily. It would appear there were some minor issues with exactly how the changes were checked in via Mercurial, but otherwise it would appear that the ticket should be quite easy to review. I need to do something else just now, but I'll take a look at that later today. \n\nI think this will be resolved today. \n\nDave",
    "created_at": "2010-02-25T12:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8352#issuecomment-74598",
    "user": "drkirkby"
}
```

It can't be closed yet (and in any case you should not close it, but leave a message for the release manager to do so) until #7552 is merged. 

But looking at #7552, there does seem little reason that can't be reviewed quite easily. It would appear there were some minor issues with exactly how the changes were checked in via Mercurial, but otherwise it would appear that the ticket should be quite easy to review. I need to do something else just now, but I'll take a look at that later today. 

I think this will be resolved today. 

Dave



---

archive/issue_comments_074599.json:
```json
{
    "body": "**Note to release manager**\n\nI've given #7552, (which is an update of the version of twisted) positive review. That ticket now incorporates these changes, so this ticket does not need incorporating now. I've added Jaap as an author on #7552. \n\nI've stuck this to 'needs info' as really it no longer needs reviewing. I believe it should be closed, but I'm not allowed to do that, so 'needs info' seemed the least confusing. \n\nDave",
    "created_at": "2010-02-25T13:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8352#issuecomment-74599",
    "user": "drkirkby"
}
```

**Note to release manager**

I've given #7552, (which is an update of the version of twisted) positive review. That ticket now incorporates these changes, so this ticket does not need incorporating now. I've added Jaap as an author on #7552. 

I've stuck this to 'needs info' as really it no longer needs reviewing. I believe it should be closed, but I'm not allowed to do that, so 'needs info' seemed the least confusing. 

Dave



---

archive/issue_comments_074600.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-02-25T13:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8352#issuecomment-74600",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_074601.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T22:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8352#issuecomment-74601",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_074602.json:
```json
{
    "body": "Close as fixed by #7552.",
    "created_at": "2010-03-02T22:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8352#issuecomment-74602",
    "user": "mvngu"
}
```

Close as fixed by #7552.
