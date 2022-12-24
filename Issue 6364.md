# Issue 6364: error message at end of successful "sage -merge"

archive/issues_006364.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: merge\n\nReported on sage-devel:\n\n```\nAll seemed well with that test (all tests passed, etc), but the final\nlines of output are\n\nAll tests passed! Popping patches from queue ...\ncd \"/home/jec/sage-4.0.2/devel/sage\" && hg qpop -a\ncd \"/home/jec/sage-4.0.2/devel/sage\" && hg qdelete trac_5307.patch\nBuilding failed with SystemExit: 0\n\n-- what's with the \"failed\" in the last line?\n```\n\n\nCraig suggested:\n\n```\nInteresting ... I've never seen that before. What os/arch are you on?\nCould I ask you to try one thing: go to $SAGE_ROOT/local/bin, and edit\nsage-apply-ticket. On the 5th line from the bottom is \"sys.exit(0)\" --\ncould you try deleting that line and moving it to the very bottom (and\noutdenting it)? I suspect that error will go away. Actually, you could\neven try just deleting that line, and I suspect that will fix it, too.\n```\n\nand was right:\n\n```\nThat did the trick -- ran fine and no \"failure\" line at the end.  (I\nmoved that line to the end as suggested)\n```\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6364\n\n",
    "created_at": "2009-06-20T13:25:47Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "error message at end of successful \"sage -merge\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6364",
    "user": "cremona"
}
```
Assignee: tbd

Keywords: merge

Reported on sage-devel:

```
All seemed well with that test (all tests passed, etc), but the final
lines of output are

All tests passed! Popping patches from queue ...
cd "/home/jec/sage-4.0.2/devel/sage" && hg qpop -a
cd "/home/jec/sage-4.0.2/devel/sage" && hg qdelete trac_5307.patch
Building failed with SystemExit: 0

-- what's with the "failed" in the last line?
```


Craig suggested:

```
Interesting ... I've never seen that before. What os/arch are you on?
Could I ask you to try one thing: go to $SAGE_ROOT/local/bin, and edit
sage-apply-ticket. On the 5th line from the bottom is "sys.exit(0)" --
could you try deleting that line and moving it to the very bottom (and
outdenting it)? I suspect that error will go away. Actually, you could
even try just deleting that line, and I suspect that will fix it, too.
```

and was right:

```
That did the trick -- ran fine and no "failure" line at the end.  (I
moved that line to the end as suggested)
```





Issue created by migration from https://trac.sagemath.org/ticket/6364





---

archive/issue_comments_050912.json:
```json
{
    "body": "Attachment [trac-6364-bin.patch](tarball://root/attachments/some-uuid/ticket6364/trac-6364-bin.patch) by craigcitro created at 2009-06-20 17:55:37",
    "created_at": "2009-06-20T17:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6364#issuecomment-50912",
    "user": "craigcitro"
}
```

Attachment [trac-6364-bin.patch](tarball://root/attachments/some-uuid/ticket6364/trac-6364-bin.patch) by craigcitro created at 2009-06-20 17:55:37



---

archive/issue_comments_050913.json:
```json
{
    "body": "The patch looks good, but would not apply using the usual system (which could not find the file being patched).\nIf you tell me how to apply it I will do so and test it!",
    "created_at": "2009-06-20T19:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6364#issuecomment-50913",
    "user": "cremona"
}
```

The patch looks good, but would not apply using the usual system (which could not find the file being patched).
If you tell me how to apply it I will do so and test it!



---

archive/issue_comments_050914.json:
```json
{
    "body": "How do you usually apply patches? Do you use `hg_sage` or do you change to the appropriate directory and apply directly with `hg`? If it's the former, use `hg_scripts`; if it's the latter, go to `$SAGE_ROOT/local/bin` and use `hg`. If neither of those work, copy-paste the error message and I'll go from there. `:)`",
    "created_at": "2009-06-20T20:34:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6364#issuecomment-50914",
    "user": "craigcitro"
}
```

How do you usually apply patches? Do you use `hg_sage` or do you change to the appropriate directory and apply directly with `hg`? If it's the former, use `hg_scripts`; if it's the latter, go to `$SAGE_ROOT/local/bin` and use `hg`. If neither of those work, copy-paste the error message and I'll go from there. `:)`



---

archive/issue_comments_050915.json:
```json
{
    "body": "I did not know about hg_scripts.  I always used to use hg_sage (though did not realise the significance in the \"sage\" part of that as meaning \"the sage library, i.e. the devel directory\");  more recently I usually use mercurial queues via \"sage -hg\" from the command line.\n\nNow using hg_scripts pops up various editor windows, complaining about unsaved changes.  Same in a completely new clone.  I'll try again tomorrow, but it may be that my failed attempts at this trivial test have messed up my sage build so I might have to rebuild from source.  Meanwhile perhaps someone who knows what they are doing can review the patch!",
    "created_at": "2009-06-20T21:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6364#issuecomment-50915",
    "user": "cremona"
}
```

I did not know about hg_scripts.  I always used to use hg_sage (though did not realise the significance in the "sage" part of that as meaning "the sage library, i.e. the devel directory");  more recently I usually use mercurial queues via "sage -hg" from the command line.

Now using hg_scripts pops up various editor windows, complaining about unsaved changes.  Same in a completely new clone.  I'll try again tomorrow, but it may be that my failed attempts at this trivial test have messed up my sage build so I might have to rebuild from source.  Meanwhile perhaps someone who knows what they are doing can review the patch!



---

archive/issue_comments_050916.json:
```json
{
    "body": "apply to 4.1 (instead of previous patch)",
    "created_at": "2009-07-11T15:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6364#issuecomment-50916",
    "user": "cremona"
}
```

apply to 4.1 (instead of previous patch)



---

archive/issue_comments_050917.json:
```json
{
    "body": "Attachment [trac_6364.patch](tarball://root/attachments/some-uuid/ticket6364/trac_6364.patch) by cremona created at 2009-07-11 15:23:29\n\nCraig's patch would not work for me, it failed to apply, perhaps because the script has changed in the interim.\n\nI have added a new patch and hope it can be reviewed before things  change again!",
    "created_at": "2009-07-11T15:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6364#issuecomment-50917",
    "user": "cremona"
}
```

Attachment [trac_6364.patch](tarball://root/attachments/some-uuid/ticket6364/trac_6364.patch) by cremona created at 2009-07-11 15:23:29

Craig's patch would not work for me, it failed to apply, perhaps because the script has changed in the interim.

I have added a new patch and hope it can be reviewed before things  change again!



---

archive/issue_comments_050918.json:
```json
{
    "body": "Attachment [scripts_6364_pre.patch](tarball://root/attachments/some-uuid/ticket6364/scripts_6364_pre.patch) by boothby created at 2009-07-17 22:08:52",
    "created_at": "2009-07-17T22:08:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6364#issuecomment-50918",
    "user": "boothby"
}
```

Attachment [scripts_6364_pre.patch](tarball://root/attachments/some-uuid/ticket6364/scripts_6364_pre.patch) by boothby created at 2009-07-17 22:08:52



---

archive/issue_comments_050919.json:
```json
{
    "body": "Works for me -- however, there was a typo in the file (my fault) which prevents the merge script from working at all.  I attached a patch which fixes that typo.",
    "created_at": "2009-07-17T22:10:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6364#issuecomment-50919",
    "user": "boothby"
}
```

Works for me -- however, there was a typo in the file (my fault) which prevents the merge script from working at all.  I attached a patch which fixes that typo.



---

archive/issue_comments_050920.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-18T18:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6364#issuecomment-50920",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_050921.json:
```json
{
    "body": "Merged only `trac_6364.patch`. The typo issue addressed by `scripts_6364_pre.patch` has been fixed by ticket #6511.",
    "created_at": "2009-07-18T18:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6364#issuecomment-50921",
    "user": "mvngu"
}
```

Merged only `trac_6364.patch`. The typo issue addressed by `scripts_6364_pre.patch` has been fixed by ticket #6511.
