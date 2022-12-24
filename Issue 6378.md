# Issue 6378: make sage -merge more user-friendly

archive/issues_006378.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @craigcitro @nexttime\n\nA few features would be nice to add to sage -merge:\n\n1. Ask all questions at the start instead of between tickets (that way, the user can kick off the process and just wait until it finishes, instead of having to check back every 20 minutes)\n2. Display comments with the patches\n3. Email a final report\n\nAlso, sage -merge doesn't properly handle the '-a -f' combination.  Fix that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6378\n\n",
    "created_at": "2009-06-21T19:32:32Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "make sage -merge more user-friendly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6378",
    "user": "boothby"
}
```
Assignee: tbd

CC:  @craigcitro @nexttime

A few features would be nice to add to sage -merge:

1. Ask all questions at the start instead of between tickets (that way, the user can kick off the process and just wait until it finishes, instead of having to check back every 20 minutes)
2. Display comments with the patches
3. Email a final report

Also, sage -merge doesn't properly handle the '-a -f' combination.  Fix that.

Issue created by migration from https://trac.sagemath.org/ticket/6378





---

archive/issue_comments_051038.json:
```json
{
    "body": "The above adds all but the email functionality.  I'll add that in pretty soon.",
    "created_at": "2009-06-21T19:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51038",
    "user": "boothby"
}
```

The above adds all but the email functionality.  I'll add that in pretty soon.



---

archive/issue_comments_051039.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-06-21T19:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51039",
    "user": "boothby"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_051040.json:
```json
{
    "body": "Changing component from algebra to build.",
    "created_at": "2009-06-21T19:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51040",
    "user": "boothby"
}
```

Changing component from algebra to build.



---

archive/issue_comments_051041.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-06-21T19:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51041",
    "user": "boothby"
}
```

Changing priority from major to minor.



---

archive/issue_comments_051042.json:
```json
{
    "body": "Using `sage -merge`, I managed to hose the system pretty hard.  I'm pretty sure that an exception occurred which resulted in a bad patch not getting popped after some sort of failure.  Hopefully, part 2  will prevent that from happening again.  Part 3 fixes a typo in part 2.",
    "created_at": "2009-06-22T21:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51042",
    "user": "boothby"
}
```

Using `sage -merge`, I managed to hose the system pretty hard.  I'm pretty sure that an exception occurred which resulted in a bad patch not getting popped after some sort of failure.  Hopefully, part 2  will prevent that from happening again.  Part 3 fixes a typo in part 2.



---

archive/issue_comments_051043.json:
```json
{
    "body": "I guess I'm a little confused -- you've mentioned that the problem you were hitting is that the script would often forget to pop patches from the queue, yet you've removed code that pops patches in several places. That seems confusing to me ... in particular, in 4 places in the second patch above, you've removed code that pops patches -- why?",
    "created_at": "2009-06-22T23:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51043",
    "user": "@craigcitro"
}
```

I guess I'm a little confused -- you've mentioned that the problem you were hitting is that the script would often forget to pop patches from the queue, yet you've removed code that pops patches in several places. That seems confusing to me ... in particular, in 4 places in the second patch above, you've removed code that pops patches -- why?



---

archive/issue_comments_051044.json:
```json
{
    "body": "Attachment [scripts-6378-automerge.patch](tarball://root/attachments/some-uuid/ticket6378/scripts-6378-automerge.patch) by boothby created at 2009-06-26 05:48:28\n\nflattened & based on 4.0.2",
    "created_at": "2009-06-26T05:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51044",
    "user": "boothby"
}
```

Attachment [scripts-6378-automerge.patch](tarball://root/attachments/some-uuid/ticket6378/scripts-6378-automerge.patch) by boothby created at 2009-06-26 05:48:28

flattened & based on 4.0.2



---

archive/issue_comments_051045.json:
```json
{
    "body": "note, the 4 places I removed code to pop patches is actually handed in the calling function -- hence, it should be more robust, not less as a result.",
    "created_at": "2009-06-26T05:49:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51045",
    "user": "boothby"
}
```

note, the 4 places I removed code to pop patches is actually handed in the calling function -- hence, it should be more robust, not less as a result.



---

archive/issue_comments_051046.json:
```json
{
    "body": "I'm generally happy with Tom's changes. In fact, one should note that no patch of his needs merged -- these changes are already live in sage 4.1 and 4.1.1. Looks like someone's been editing trunk. (`*tsk tsk*`)\n\nMy referee report comes in the form of two new patches, one for the bin repo, and the other for the main repo. The change to the main repo is tiny -- it's just changing `sage/misc/hg.py` to use the new `subprocess` module instead of `popen3`, because the deprecation warning is annoying to see in the output of `sage -merge`. I could easily be convinced to move this to a new ticket, if people would prefer that. \n\nThe patch to the bin repo does the following:\n\n* remove a dirty hack involving `tee` by using python's `subprocess` module\n* add a few comments about the hackish parsing of trac pages\n* use `urllib2` to parse urls\n* be (unnecessarily?) pedantic about `os.path.join` instead of explicit use of `/`\n* clean up some spacing and indentation issues\n* add an option to e-mail when a run of `sage -merge -a` finishes\n\nI ran some tests, but I didn't do any exhaustive testing on `sage.math`, which should probably be done. (I'm currently on vacation, and without good internet access.)",
    "created_at": "2009-08-28T07:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51046",
    "user": "@craigcitro"
}
```

I'm generally happy with Tom's changes. In fact, one should note that no patch of his needs merged -- these changes are already live in sage 4.1 and 4.1.1. Looks like someone's been editing trunk. (`*tsk tsk*`)

My referee report comes in the form of two new patches, one for the bin repo, and the other for the main repo. The change to the main repo is tiny -- it's just changing `sage/misc/hg.py` to use the new `subprocess` module instead of `popen3`, because the deprecation warning is annoying to see in the output of `sage -merge`. I could easily be convinced to move this to a new ticket, if people would prefer that. 

The patch to the bin repo does the following:

* remove a dirty hack involving `tee` by using python's `subprocess` module
* add a few comments about the hackish parsing of trac pages
* use `urllib2` to parse urls
* be (unnecessarily?) pedantic about `os.path.join` instead of explicit use of `/`
* clean up some spacing and indentation issues
* add an option to e-mail when a run of `sage -merge -a` finishes

I ran some tests, but I didn't do any exhaustive testing on `sage.math`, which should probably be done. (I'm currently on vacation, and without good internet access.)



---

archive/issue_comments_051047.json:
```json
{
    "body": "apply to bin repo",
    "created_at": "2009-08-28T07:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51047",
    "user": "@craigcitro"
}
```

apply to bin repo



---

archive/issue_comments_051048.json:
```json
{
    "body": "Attachment [trac-6378-bin.patch](tarball://root/attachments/some-uuid/ticket6378/trac-6378-bin.patch) by @craigcitro created at 2009-08-28 07:22:52\n\napply to main repo",
    "created_at": "2009-08-28T07:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51048",
    "user": "@craigcitro"
}
```

Attachment [trac-6378-bin.patch](tarball://root/attachments/some-uuid/ticket6378/trac-6378-bin.patch) by @craigcitro created at 2009-08-28 07:22:52

apply to main repo



---

archive/issue_comments_051049.json:
```json
{
    "body": "Attachment [trac-6378-main.patch](tarball://root/attachments/some-uuid/ticket6378/trac-6378-main.patch) by @JohnCremona created at 2009-08-31 13:17:57\n\nQuestion:  how well is this documented?  As well as all the functions in the scripts having docstrings, I think we need to have this all properly in the developers manual.  Recently I wanted to demonstrate the merge feature to a newcomer, and found that I couldn't remember what all the command line options were, and could not find them documented.  (Of course, it is possible that they are somewhere!  I remember seeing them in a sage-devel post, but that is hardly acceptable!)",
    "created_at": "2009-08-31T13:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51049",
    "user": "@JohnCremona"
}
```

Attachment [trac-6378-main.patch](tarball://root/attachments/some-uuid/ticket6378/trac-6378-main.patch) by @JohnCremona created at 2009-08-31 13:17:57

Question:  how well is this documented?  As well as all the functions in the scripts having docstrings, I think we need to have this all properly in the developers manual.  Recently I wanted to demonstrate the merge feature to a newcomer, and found that I couldn't remember what all the command line options were, and could not find them documented.  (Of course, it is possible that they are somewhere!  I remember seeing them in a sage-devel post, but that is hardly acceptable!)



---

archive/issue_comments_051050.json:
```json
{
    "body": "This is a very good point. I wrote up an explanation at `wiki.sagemath.org/release`, but there should be some documentation in the source itself. I'll work on that and post another patch -- after all, documentation makes things **much** more user-friendly. `:)`",
    "created_at": "2009-08-31T14:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51050",
    "user": "@craigcitro"
}
```

This is a very good point. I wrote up an explanation at `wiki.sagemath.org/release`, but there should be some documentation in the source itself. I'll work on that and post another patch -- after all, documentation makes things **much** more user-friendly. `:)`



---

archive/issue_comments_051051.json:
```json
{
    "body": "Great -- I also meant that when you get this:\n\n```\nUsage: sage -merge <ticket_number>\nFor more advanced usage, see the file /home/john/sage-4.1.1/local/bin/sage-apply-ticket.\n```\n\nthen as well as finding something human-readable in that script file, there could be more usage instructions in (say) the reference manual.\n\nThat should go for all the other command-line options, of course: a sort of \"man sage\"-type output.\n\nAnyway, adding a reference to wiki.sagemath.org/release would already be useful!",
    "created_at": "2009-08-31T15:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51051",
    "user": "@JohnCremona"
}
```

Great -- I also meant that when you get this:

```
Usage: sage -merge <ticket_number>
For more advanced usage, see the file /home/john/sage-4.1.1/local/bin/sage-apply-ticket.
```

then as well as finding something human-readable in that script file, there could be more usage instructions in (say) the reference manual.

That should go for all the other command-line options, of course: a sort of "man sage"-type output.

Anyway, adding a reference to wiki.sagemath.org/release would already be useful!



---

archive/issue_comments_051052.json:
```json
{
    "body": "Replying to [comment:9 craigcitro]:\n> I wrote up an explanation at `wiki.sagemath.org/release`, but there should be some documentation in the source itself. I'll work on that and post another patch -- after all, documentation makes things **much** more user-friendly. `:)`\n\n\nMeanwhile(?) http://wiki.sagemath.org/release appears to be a dead link.\n\nhttp://wiki.sagemath.org/devel/ReleaseManagement is all I've found.\n\n[I really love trac... I **did not** delete `work_issues` (it was empty; same for `upstream`).]\n\n-Leif",
    "created_at": "2010-01-31T23:23:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51052",
    "user": "@nexttime"
}
```

Replying to [comment:9 craigcitro]:
> I wrote up an explanation at `wiki.sagemath.org/release`, but there should be some documentation in the source itself. I'll work on that and post another patch -- after all, documentation makes things **much** more user-friendly. `:)`


Meanwhile(?) http://wiki.sagemath.org/release appears to be a dead link.

http://wiki.sagemath.org/devel/ReleaseManagement is all I've found.

[I really love trac... I **did not** delete `work_issues` (it was empty; same for `upstream`).]

-Leif



---

archive/issue_comments_051053.json:
```json
{
    "body": "Hi Leif,\n\nYep, you're right -- someone moved that content and didn't leave a link. You're right -- the content was moved to the second link you mention. I've left a note pointing people to the right place on the wiki ...\n\nThanks!",
    "created_at": "2010-02-01T17:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51053",
    "user": "@craigcitro"
}
```

Hi Leif,

Yep, you're right -- someone moved that content and didn't leave a link. You're right -- the content was moved to the second link you mention. I've left a note pointing people to the right place on the wiki ...

Thanks!



---

archive/issue_comments_051054.json:
```json
{
    "body": "Rebase on #8712. Apply this patch only. See comments for more info.",
    "created_at": "2010-04-18T13:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51054",
    "user": "@TimDumol"
}
```

Rebase on #8712. Apply this patch only. See comments for more info.



---

archive/issue_comments_051055.json:
```json
{
    "body": "Attachment [trac_6378-scripts-rebase.patch](tarball://root/attachments/some-uuid/ticket6378/trac_6378-scripts-rebase.patch) by @TimDumol created at 2010-04-18 13:23:22\n\nThe patch to the main Sage respository is unneeded now, as it's been fixed already by sage-4.4.alpha0. The patch to the scripts repository works fine, except for the email part. It doesn't get the mail argument. Calling it with, say,\n\n\n```\nsage -merge -a -e timdumol@gmail.com\n```\n\n\nresults in an error after merging everything, stating that the email address, which is the null string (''), is invalid.\n\nThis patch rebases it on #8712, while adding the requested documentation. This seems to detect the email argument.",
    "created_at": "2010-04-18T13:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51055",
    "user": "@TimDumol"
}
```

Attachment [trac_6378-scripts-rebase.patch](tarball://root/attachments/some-uuid/ticket6378/trac_6378-scripts-rebase.patch) by @TimDumol created at 2010-04-18 13:23:22

The patch to the main Sage respository is unneeded now, as it's been fixed already by sage-4.4.alpha0. The patch to the scripts repository works fine, except for the email part. It doesn't get the mail argument. Calling it with, say,


```
sage -merge -a -e timdumol@gmail.com
```


results in an error after merging everything, stating that the email address, which is the null string (''), is invalid.

This patch rebases it on #8712, while adding the requested documentation. This seems to detect the email argument.



---

archive/issue_comments_051056.json:
```json
{
    "body": "This needs a little rebasing because of my referee's patch at #8712.  See the new patch; this replaces the previous one(s).\n\nOtherwise, I'm happy with it.",
    "created_at": "2010-06-23T21:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51056",
    "user": "@jhpalmieri"
}
```

This needs a little rebasing because of my referee's patch at #8712.  See the new patch; this replaces the previous one(s).

Otherwise, I'm happy with it.



---

archive/issue_comments_051057.json:
```json
{
    "body": "Attachment [trac_6378-scripts-rebase.v2.patch](tarball://root/attachments/some-uuid/ticket6378/trac_6378-scripts-rebase.v2.patch) by @jhpalmieri created at 2010-06-23 21:16:05\n\nuse this patch only",
    "created_at": "2010-06-23T21:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51057",
    "user": "@jhpalmieri"
}
```

Attachment [trac_6378-scripts-rebase.v2.patch](tarball://root/attachments/some-uuid/ticket6378/trac_6378-scripts-rebase.v2.patch) by @jhpalmieri created at 2010-06-23 21:16:05

use this patch only



---

archive/issue_comments_051058.json:
```json
{
    "body": "(The only differences between my patch and the previous one are at the top, the printing of the help messages.)\n\nSee #9319 for a follow-up.",
    "created_at": "2010-06-23T21:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51058",
    "user": "@jhpalmieri"
}
```

(The only differences between my patch and the previous one are at the top, the printing of the help messages.)

See #9319 for a follow-up.



---

archive/issue_comments_051059.json:
```json
{
    "body": "I'm willing to give timdumol's version a positive review.  If someone can review mine (the help messages on lines 95-110 are the only difference), that would be appreciated.",
    "created_at": "2010-07-22T22:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51059",
    "user": "@jhpalmieri"
}
```

I'm willing to give timdumol's version a positive review.  If someone can review mine (the help messages on lines 95-110 are the only difference), that would be appreciated.



---

archive/issue_comments_051060.json:
```json
{
    "body": "Replying to [comment:16 jhpalmieri]:\n> I'm willing to give timdumol's version a positive review.  If someone can review mine (the help messages on lines 95-110 are the only difference), that would be appreciated.\n\nHmmm, I'm ok with John's new help messages, but when will more return codes be tested?\n\nI can't tell if this ticket is that urgent s.t. we should postpone such to the follow-up.\n\nAt least there is already one... (#9319) ;-)",
    "created_at": "2010-07-22T23:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51060",
    "user": "@nexttime"
}
```

Replying to [comment:16 jhpalmieri]:
> I'm willing to give timdumol's version a positive review.  If someone can review mine (the help messages on lines 95-110 are the only difference), that would be appreciated.

Hmmm, I'm ok with John's new help messages, but when will more return codes be tested?

I can't tell if this ticket is that urgent s.t. we should postpone such to the follow-up.

At least there is already one... (#9319) ;-)



---

archive/issue_comments_051061.json:
```json
{
    "body": "Changing component from build to scripts.",
    "created_at": "2012-08-13T12:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51061",
    "user": "@jdemeyer"
}
```

Changing component from build to scripts.



---

archive/issue_comments_051062.json:
```json
{
    "body": "`sage -merge` is gone.",
    "created_at": "2013-05-22T09:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51062",
    "user": "@jdemeyer"
}
```

`sage -merge` is gone.



---

archive/issue_comments_051063.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-05-22T09:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6378#issuecomment-51063",
    "user": "@jdemeyer"
}
```

Resolution: invalid
