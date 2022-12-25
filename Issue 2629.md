# Issue 2629: Bottom of page problems

archive/issues_002629.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @jhpalmieri\n\nWhen working on a notebook, one tends to end up at the bottom of browser window in the final cell.   However: \n\na) If you evaluate this final cell, a new input cell is created, but it is frequently at least partially off-screen and you have to scroll down to get to it.  Currently, window scrolls to accommodate the output of the evaluation, and so should scroll a little more to make the new input cell fully visible.\n\nb) If you do a tab completion or ?-query in the final cell, the output often is partially of screen.   In bad cases, the output is completely off screen and this is very confusing the to user since the program appears to be not responding to their input.   This could be solved either by having the window scroll or having the box appear above the input cell in this instance, though the latter behavior is probably only appropriate for tab completion.  \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2629\n\n",
    "created_at": "2008-03-21T16:01:38Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Bottom of page problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2629",
    "user": "https://github.com/NathanDunfield"
}
```
Assignee: boothby

CC:  @jhpalmieri

When working on a notebook, one tends to end up at the bottom of browser window in the final cell.   However: 

a) If you evaluate this final cell, a new input cell is created, but it is frequently at least partially off-screen and you have to scroll down to get to it.  Currently, window scrolls to accommodate the output of the evaluation, and so should scroll a little more to make the new input cell fully visible.

b) If you do a tab completion or ?-query in the final cell, the output often is partially of screen.   In bad cases, the output is completely off screen and this is very confusing the to user since the program appears to be not responding to their input.   This could be solved either by having the window scroll or having the box appear above the input cell in this instance, though the latter behavior is probably only appropriate for tab completion.  



Issue created by migration from https://trac.sagemath.org/ticket/2629





---

archive/issue_comments_018029.json:
```json
{
    "body": "There is an assessment at #4963 that this issue would largely be resolved by #4963, but this doesn't seem to do it (at least not in the way it is resolved), after testing on Safari and Firefox 2 and 3 on OSX.4 PPC.  \n\nThe browser still only shows a little bit; with the proposed fix at #4963, now the browser doesn't have to scroll at all if you are on the last cell and it is at the bottom (not even with a large output), also for tab-completion etc, so the behavior described above is still possible, though perhaps harder because you would have to be unlucky with how you scrolled after your previous computation.\n\nSince this has been dormant for nearly a year, though, moving to minor priority.  If the original reporter disagrees and thinks this should now be closed or stay major, that is okay too, of course!",
    "created_at": "2009-01-21T17:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2629#issuecomment-18029",
    "user": "https://github.com/kcrisman"
}
```

There is an assessment at #4963 that this issue would largely be resolved by #4963, but this doesn't seem to do it (at least not in the way it is resolved), after testing on Safari and Firefox 2 and 3 on OSX.4 PPC.  

The browser still only shows a little bit; with the proposed fix at #4963, now the browser doesn't have to scroll at all if you are on the last cell and it is at the bottom (not even with a large output), also for tab-completion etc, so the behavior described above is still possible, though perhaps harder because you would have to be unlucky with how you scrolled after your previous computation.

Since this has been dormant for nearly a year, though, moving to minor priority.  If the original reporter disagrees and thinks this should now be closed or stay major, that is okay too, of course!



---

archive/issue_comments_018030.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-01-21T17:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2629#issuecomment-18030",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_018031.json:
```json
{
    "body": "The second thing is still an issue.  The first does not seem to be any more, upon extremely brief testing.",
    "created_at": "2012-07-07T04:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2629#issuecomment-18031",
    "user": "https://github.com/kcrisman"
}
```

The second thing is still an issue.  The first does not seem to be any more, upon extremely brief testing.



---

archive/issue_comments_018032.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-03-28T10:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2629#issuecomment-18032",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_018033.json:
```json
{
    "body": "old ticket about deprecated sagenb, can we close ?",
    "created_at": "2020-03-28T10:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2629#issuecomment-18033",
    "user": "https://github.com/fchapoton"
}
```

old ticket about deprecated sagenb, can we close ?



---

archive/issue_comments_018034.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-03-28T14:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2629#issuecomment-18034",
    "user": "https://github.com/NathanDunfield"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_018035.json:
```json
{
    "body": "This ancient ticket should definitely be closed.  Setting positive review.",
    "created_at": "2020-03-28T14:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2629#issuecomment-18035",
    "user": "https://github.com/NathanDunfield"
}
```

This ancient ticket should definitely be closed.  Setting positive review.



---

archive/issue_comments_018036.json:
```json
{
    "body": "thx",
    "created_at": "2020-03-28T15:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2629#issuecomment-18036",
    "user": "https://github.com/fchapoton"
}
```

thx



---

archive/issue_comments_018037.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-28T15:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2629#issuecomment-18037",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
