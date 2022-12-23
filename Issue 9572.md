# Issue 9572: SageNB 0.8.2

archive/issues_009572.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  acleone leif timdumol\n\nThis should include #9554 and perhaps other positively reviewed notebook tickets.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9572\n\n",
    "created_at": "2010-07-22T03:40:26Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "title": "SageNB 0.8.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9572",
    "user": "mpatel"
}
```
Assignee: jason, was

CC:  acleone leif timdumol

This should include #9554 and perhaps other positively reviewed notebook tickets.

Issue created by migration from https://trac.sagemath.org/ticket/9572





---

archive/issue_comments_092436.json:
```json
{
    "body": "You might consider #8574 and #9512, which are both positively reviewed.",
    "created_at": "2010-07-23T02:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92436",
    "user": "ddrake"
}
```

You might consider #8574 and #9512, which are both positively reviewed.



---

archive/issue_comments_092437.json:
```json
{
    "body": "Replying to [comment:1 ddrake]:\n> You might consider #8574 and #9512, which are both positively reviewed.\n\nEr, I mean, #8754.",
    "created_at": "2010-07-23T02:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92437",
    "user": "ddrake"
}
```

Replying to [comment:1 ddrake]:
> You might consider #8574 and #9512, which are both positively reviewed.

Er, I mean, #8754.



---

archive/issue_comments_092438.json:
```json
{
    "body": "All long doctests pass for me on sage.math with 4.5.2.alpha0 + sagenb-0.8.2.spkg.  But given my current computer setup, I can't run the Selenium tests.",
    "created_at": "2010-07-23T07:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92438",
    "user": "mpatel"
}
```

All long doctests pass for me on sage.math with 4.5.2.alpha0 + sagenb-0.8.2.spkg.  But given my current computer setup, I can't run the Selenium tests.



---

archive/issue_comments_092439.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-23T07:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92439",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092440.json:
```json
{
    "body": "Remember to do http://trac.sagemath.org/sage_trac/ticket/9580#comment:2 ...",
    "created_at": "2010-07-23T07:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92440",
    "user": "leif"
}
```

Remember to do http://trac.sagemath.org/sage_trac/ticket/9580#comment:2 ...



---

archive/issue_comments_092441.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-24T23:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92441",
    "user": "cwitty"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092442.json:
```json
{
    "body": "Doctests and selenium tests passed for me, using Firefox (well, Iceweasel) 3.6.4.  (Except for test_7434, which failed with both sagenb 0.8.1 and 0.8.2, presumably because I don't have Java set up on this machine.)\n\nThis will be a positive review once you fix #9580 :)",
    "created_at": "2010-07-24T23:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92442",
    "user": "cwitty"
}
```

Doctests and selenium tests passed for me, using Firefox (well, Iceweasel) 3.6.4.  (Except for test_7434, which failed with both sagenb 0.8.1 and 0.8.2, presumably because I don't have Java set up on this machine.)

This will be a positive review once you fix #9580 :)



---

archive/issue_comments_092443.json:
```json
{
    "body": "Actually, I found a bug: the \"source editor\" feature (#9512) converts line endings from Unix to DOS (so once you've edited the file, mercurial thinks every line has changed).\n\nGiven the total non-discoverability of #9512, I'm not sure this bug is worth holding up the new spkg; I'll let somebody else decide that.",
    "created_at": "2010-07-25T00:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92443",
    "user": "cwitty"
}
```

Actually, I found a bug: the "source editor" feature (#9512) converts line endings from Unix to DOS (so once you've edited the file, mercurial thinks every line has changed).

Given the total non-discoverability of #9512, I'm not sure this bug is worth holding up the new spkg; I'll let somebody else decide that.



---

archive/issue_comments_092444.json:
```json
{
    "body": "In order to have a new SageNB package ready for 4.5.2, I've decided to change #9512's status to *needs_work* and \"unmerge\" it from SageNB 0.8.2.  I've included #3342, #9554, and #9580 in an updated SageNB 0.8.2, which is available at the link in the description.\n\nNote: I haven't added a patch level (e.g., `sagenb-0.8.2p0.spkg`), but I have renamed the previous version to `sagenb-0.8.2-9572.spkg`.",
    "created_at": "2010-07-25T07:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92444",
    "user": "mpatel"
}
```

In order to have a new SageNB package ready for 4.5.2, I've decided to change #9512's status to *needs_work* and "unmerge" it from SageNB 0.8.2.  I've included #3342, #9554, and #9580 in an updated SageNB 0.8.2, which is available at the link in the description.

Note: I haven't added a patch level (e.g., `sagenb-0.8.2p0.spkg`), but I have renamed the previous version to `sagenb-0.8.2-9572.spkg`.



---

archive/issue_comments_092445.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-25T07:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92445",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092446.json:
```json
{
    "body": "Doctests and selenium tests passed (except, again, for test_7434).\n\nPositive review.",
    "created_at": "2010-07-25T19:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92446",
    "user": "cwitty"
}
```

Doctests and selenium tests passed (except, again, for test_7434).

Positive review.



---

archive/issue_comments_092447.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-25T19:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92447",
    "user": "cwitty"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092448.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-26T07:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92448",
    "user": "ddrake"
}
```

Resolution: fixed



---

archive/issue_comments_092449.json:
```json
{
    "body": "Belated note for the release manager: Please merge #3342's sage repository patch with SageNB 0.8.2.\n\n(I should have followed [our own advice](http://groups.google.com/group/sage-release/browse_thread/thread/456f14fd92ee61a5/0962395dd19cc9c6#0962395dd19cc9c6)!)",
    "created_at": "2010-07-27T02:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92449",
    "user": "mpatel"
}
```

Belated note for the release manager: Please merge #3342's sage repository patch with SageNB 0.8.2.

(I should have followed [our own advice](http://groups.google.com/group/sage-release/browse_thread/thread/456f14fd92ee61a5/0962395dd19cc9c6#0962395dd19cc9c6)!)



---

archive/issue_comments_092450.json:
```json
{
    "body": "Replying to [comment:10 mpatel]:\n\n> Belated note for the release manager: Please merge #3342's sage repository patch with SageNB 0.8.2.\n\nBut if it's too late for 4.5.2.alpha1, we could, I think, just include the patch in 4.5.2.rc0.",
    "created_at": "2010-07-27T02:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92450",
    "user": "mpatel"
}
```

Replying to [comment:10 mpatel]:

> Belated note for the release manager: Please merge #3342's sage repository patch with SageNB 0.8.2.

But if it's too late for 4.5.2.alpha1, we could, I think, just include the patch in 4.5.2.rc0.



---

archive/issue_comments_092451.json:
```json
{
    "body": "Replying to [comment:10 mpatel]:\n> Belated note for the release manager: Please merge #3342's sage repository patch with SageNB 0.8.2.\n> \n> (I should have followed [our own advice](http://groups.google.com/group/sage-release/browse_thread/thread/456f14fd92ee61a5/0962395dd19cc9c6#0962395dd19cc9c6)!)\n\nYes, you should have. :)  You're lucky though, I managed to sneak it into alpha1.",
    "created_at": "2010-07-27T02:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9572#issuecomment-92451",
    "user": "ddrake"
}
```

Replying to [comment:10 mpatel]:
> Belated note for the release manager: Please merge #3342's sage repository patch with SageNB 0.8.2.
> 
> (I should have followed [our own advice](http://groups.google.com/group/sage-release/browse_thread/thread/456f14fd92ee61a5/0962395dd19cc9c6#0962395dd19cc9c6)!)

Yes, you should have. :)  You're lucky though, I managed to sneak it into alpha1.
