# Issue 6542: tachyon ouput seems broken in sage-4.1

archive/issues_006542.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman wstein boothby mvngu\n\nKeywords: graphics, tachyon, raytracer\n\nAs part of tracking this down, I am planning on adding doctests to more of the tachyon related files, which currently have low coverage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6542\n\n",
    "created_at": "2009-07-16T11:49:09Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "tachyon ouput seems broken in sage-4.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6542",
    "user": "mhampton"
}
```
Assignee: @williamstein

CC:  @kcrisman wstein boothby mvngu

Keywords: graphics, tachyon, raytracer

As part of tracking this down, I am planning on adding doctests to more of the tachyon related files, which currently have low coverage.

Issue created by migration from https://trac.sagemath.org/ticket/6542





---

archive/issue_comments_053328.json:
```json
{
    "body": "This problem was raised in this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/12104b9aec94c758) thread.",
    "created_at": "2009-07-16T11:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53328",
    "user": "mvngu"
}
```

This problem was raised in this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/12104b9aec94c758) thread.



---

archive/issue_comments_053329.json:
```json
{
    "body": "This might have been broken by 6269 or 6372.  At any rate, the tostr function in tachyon.py is now missing a crucial piece.  I am working on a patch.",
    "created_at": "2009-07-16T14:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53329",
    "user": "mhampton"
}
```

This might have been broken by 6269 or 6372.  At any rate, the tostr function in tachyon.py is now missing a crucial piece.  I am working on a patch.



---

archive/issue_comments_053330.json:
```json
{
    "body": "fixes a mistaken deletion of critical functionality in tachyon's tostr function",
    "created_at": "2009-07-16T18:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53330",
    "user": "mhampton"
}
```

fixes a mistaken deletion of critical functionality in tachyon's tostr function



---

archive/issue_comments_053331.json:
```json
{
    "body": "Attachment [trac_6542_tachyon_tostr.patch](tarball://root/attachments/some-uuid/ticket6542/trac_6542_tachyon_tostr.patch) by mhampton created at 2009-07-16 18:22:09\n\nThe patch fixes a mistaken deletion of critical functionality in tachyon's tostr function.  Looks like a piece of this function was sliced off by mistake during the colorsys refactoring.\n\nI will open a seperate ticket to improve the tachyon doctests; I think this patch should go in ASAP since tachyon is totally broken without it.",
    "created_at": "2009-07-16T18:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53331",
    "user": "mhampton"
}
```

Attachment [trac_6542_tachyon_tostr.patch](tarball://root/attachments/some-uuid/ticket6542/trac_6542_tachyon_tostr.patch) by mhampton created at 2009-07-16 18:22:09

The patch fixes a mistaken deletion of critical functionality in tachyon's tostr function.  Looks like a piece of this function was sliced off by mistake during the colorsys refactoring.

I will open a seperate ticket to improve the tachyon doctests; I think this patch should go in ASAP since tachyon is totally broken without it.



---

archive/issue_comments_053332.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-07-16T18:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53332",
    "user": "mhampton"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_053333.json:
```json
{
    "body": "This happened during the rebasing of #6372, moving the tachyon stuff.  Perhaps this is a warning against restoring positive reviews immediately upon rebase, or perhaps not.  In any case, the current patch needs a doctest to catch this - currently the function returns None every time this is called on a non-string, and that is probably why things didn't get caught before.",
    "created_at": "2009-07-16T18:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53333",
    "user": "@kcrisman"
}
```

This happened during the rebasing of #6372, moving the tachyon stuff.  Perhaps this is a warning against restoring positive reviews immediately upon rebase, or perhaps not.  In any case, the current patch needs a doctest to catch this - currently the function returns None every time this is called on a non-string, and that is probably why things didn't get caught before.



---

archive/issue_comments_053334.json:
```json
{
    "body": "Well, yeah - the whole damn file needs doctests, which will take a while.  But I really think this should be fixed as soon as possible.\n\nI made ticket #6543 to fix the lack of doctests; that can build on this patch.",
    "created_at": "2009-07-16T19:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53334",
    "user": "mhampton"
}
```

Well, yeah - the whole damn file needs doctests, which will take a while.  But I really think this should be fixed as soon as possible.

I made ticket #6543 to fix the lack of doctests; that can build on this patch.



---

archive/issue_comments_053335.json:
```json
{
    "body": "Replying to [comment:5 mhampton]:\n> Well, yeah - the whole damn file needs doctests, which will take a while.  But I really think this should be fixed as soon as possible.\nTrue; I just meant to add a string with doctest that \n\n```\ntostr([5,4,3])\n' 5.0 4.0 3.0 '\n```\n\nas per Sage convention to check that it was fixed; that shouldn't be too bad.  I'd do it myself but do not have a current Sage build available.\n> I made ticket #6543 to fix the lack of doctests; that can build on this patch.\nYes, I've been thinking about doing this for a while too.",
    "created_at": "2009-07-16T19:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53335",
    "user": "@kcrisman"
}
```

Replying to [comment:5 mhampton]:
> Well, yeah - the whole damn file needs doctests, which will take a while.  But I really think this should be fixed as soon as possible.
True; I just meant to add a string with doctest that 

```
tostr([5,4,3])
' 5.0 4.0 3.0 '
```

as per Sage convention to check that it was fixed; that shouldn't be too bad.  I'd do it myself but do not have a current Sage build available.
> I made ticket #6543 to fix the lack of doctests; that can build on this patch.
Yes, I've been thinking about doing this for a while too.



---

archive/issue_comments_053336.json:
```json
{
    "body": "Attachment [trac_6542_tachyon_tostr.2.patch](tarball://root/attachments/some-uuid/ticket6542/trac_6542_tachyon_tostr.2.patch) by mhampton created at 2009-07-16 20:06:22\n\nnew version with doctest",
    "created_at": "2009-07-16T20:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53336",
    "user": "mhampton"
}
```

Attachment [trac_6542_tachyon_tostr.2.patch](tarball://root/attachments/some-uuid/ticket6542/trac_6542_tachyon_tostr.2.patch) by mhampton created at 2009-07-16 20:06:22

new version with doctest



---

archive/issue_comments_053337.json:
```json
{
    "body": "OK, I added a doctest to the tostr function.",
    "created_at": "2009-07-16T20:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53337",
    "user": "mhampton"
}
```

OK, I added a doctest to the tostr function.



---

archive/issue_comments_053338.json:
```json
{
    "body": "The function itself (obviously, since just replaces from before) works fine for me as is, and the documentation works fine in testing.  Unfortunately, I can't currently merge it in a Sage build and do a test run, so needs further review to ensure that.  This should be REALLY EASY to do for anyone who has a current Sage 4.1.",
    "created_at": "2009-07-17T13:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53338",
    "user": "@kcrisman"
}
```

The function itself (obviously, since just replaces from before) works fine for me as is, and the documentation works fine in testing.  Unfortunately, I can't currently merge it in a Sage build and do a test run, so needs further review to ensure that.  This should be REALLY EASY to do for anyone who has a current Sage 4.1.



---

archive/issue_comments_053339.json:
```json
{
    "body": "Changing assignee from @williamstein to mhampton.",
    "created_at": "2009-07-23T03:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53339",
    "user": "mhampton"
}
```

Changing assignee from @williamstein to mhampton.



---

archive/issue_comments_053340.json:
```json
{
    "body": "Works perfectly for me -- Sage 4.1.",
    "created_at": "2009-07-27T09:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53340",
    "user": "@TimDumol"
}
```

Works perfectly for me -- Sage 4.1.



---

archive/issue_comments_053341.json:
```json
{
    "body": "Typo in the word \"seperated\" on line 990:\n\n```\n-Converts vector information to a space-seperated string.\n+Converts vector information to a space-separated string.\n```\n",
    "created_at": "2009-07-27T13:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53341",
    "user": "mvngu"
}
```

Typo in the word "seperated" on line 990:

```
-Converts vector information to a space-seperated string.
+Converts vector information to a space-separated string.
```




---

archive/issue_comments_053342.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-29T11:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6542#issuecomment-53342",
    "user": "mvngu"
}
```

Resolution: fixed
