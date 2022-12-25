# Issue 9616: segfault / NFS problems with parallel/decorate.py

archive/issues_009616.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @nexttime @jhpalmieri @kcrisman @malb mvngu simonking @williamstein\n\nKeywords: fork nfs segfault\n\nIn 4.5.2.alpha1, we have for many people:\n\n```\nsage -t -long \"devel/sage/sage/parallel/decorate.py\"        \n\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occurred in Sage.\nThis probably occurred because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n\n**********************************************************************\nFile \"/mnt/usb1/scratch/drake/release/tmp/sage-4.5.2.alpha1/devel/sage/sage/parallel/decorate.py\", line 300:\n    sage: g()\nExpected:\n    '10'\nGot:\n    [Errno 16] Device or resource busy: '/home/drake/.sage/temp/sage.math.washington.edu/30336/dir_0/.nfs0000000000591f8700069d5c'\n    '10'\n**********************************************************************\nFile \"/mnt/usb1/scratch/drake/release/tmp/sage-4.5.2.alpha1/devel/sage/sage/parallel/decorate.py\", line 311:\n    sage: g()\nExpected:\n    'a'\nGot:\n    [Errno 16] Device or resource busy: '/home/drake/.sage/temp/sage.math.washington.edu/30336/dir_1/.nfs0000000000591f8d00069d5d'\n    'a'\n**********************************************************************\n```\nand so on. See https://groups.google.com/group/sage-release/msg/88b030aa31926459 and that thread.\n\nThis seems related to #9501.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9616\n\n",
    "created_at": "2010-07-28T02:51:53Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "segfault / NFS problems with parallel/decorate.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9616",
    "user": "https://github.com/dandrake"
}
```
Assignee: mvngu

CC:  @nexttime @jhpalmieri @kcrisman @malb mvngu simonking @williamstein

Keywords: fork nfs segfault

In 4.5.2.alpha1, we have for many people:

```
sage -t -long "devel/sage/sage/parallel/decorate.py"        


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------

**********************************************************************
File "/mnt/usb1/scratch/drake/release/tmp/sage-4.5.2.alpha1/devel/sage/sage/parallel/decorate.py", line 300:
    sage: g()
Expected:
    '10'
Got:
    [Errno 16] Device or resource busy: '/home/drake/.sage/temp/sage.math.washington.edu/30336/dir_0/.nfs0000000000591f8700069d5c'
    '10'
**********************************************************************
File "/mnt/usb1/scratch/drake/release/tmp/sage-4.5.2.alpha1/devel/sage/sage/parallel/decorate.py", line 311:
    sage: g()
Expected:
    'a'
Got:
    [Errno 16] Device or resource busy: '/home/drake/.sage/temp/sage.math.washington.edu/30336/dir_1/.nfs0000000000591f8d00069d5d'
    'a'
**********************************************************************
```
and so on. See https://groups.google.com/group/sage-release/msg/88b030aa31926459 and that thread.

This seems related to #9501.

Issue created by migration from https://trac.sagemath.org/ticket/9616





---

archive/issue_comments_092974.json:
```json
{
    "body": "For what they're worth, tests on sage.math with variations on\n\n```sh\n#!/bin/bash                                                                     \n\n# This does not keep overall statistics:                                        \n# env SAGE_TEST_GLOBAL_ITER=100 ./sage -tp 1 -long /path/to/file.py                     \n\nSAGE_TEST=\"./sage -t -long\"\n#SAGE_TEST=\"env DOT_SAGE=/dev/shm/$USER/.sage $SAGE_TEST\"                       \n#SAGE_TEST=\"env DOT_SAGE=/scratch/$USER/.sage $SAGE_TEST\"                       \nRUNS=100\nfor I in `seq 1 $RUNS`;\ndo\n    $SAGE_TEST devel/sage/sage/parallel/decorate.py\n    CODE[$I]=$?\n\n    echo \"Results after $I of $RUNS runs:\"\n    echo \"${CODE[*]}\" | tr ' ' '\\n' | sort -n | uniq -c\ndone\n```\nend with\n\n```\nResults after 100 of 100 runs:                                          \n     1 0                                                                      \n    99 128                                                                    \nResults after 100 of 100 runs:                                       \n   100 0                                                                      \nResults after 100 of 100 runs:                                       \n   100 0                                                                      \n```\nfor the default DOT_SAGE, `/scratch/$USER/.sage`, and `/dev/shm/$USER/.sage`, respectively.",
    "created_at": "2010-07-28T05:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92974",
    "user": "https://github.com/qed777"
}
```

For what they're worth, tests on sage.math with variations on

```sh
#!/bin/bash                                                                     

# This does not keep overall statistics:                                        
# env SAGE_TEST_GLOBAL_ITER=100 ./sage -tp 1 -long /path/to/file.py                     

SAGE_TEST="./sage -t -long"
#SAGE_TEST="env DOT_SAGE=/dev/shm/$USER/.sage $SAGE_TEST"                       
#SAGE_TEST="env DOT_SAGE=/scratch/$USER/.sage $SAGE_TEST"                       
RUNS=100
for I in `seq 1 $RUNS`;
do
    $SAGE_TEST devel/sage/sage/parallel/decorate.py
    CODE[$I]=$?

    echo "Results after $I of $RUNS runs:"
    echo "${CODE[*]}" | tr ' ' '\n' | sort -n | uniq -c
done
```
end with

```
Results after 100 of 100 runs:                                          
     1 0                                                                      
    99 128                                                                    
Results after 100 of 100 runs:                                       
   100 0                                                                      
Results after 100 of 100 runs:                                       
   100 0                                                                      
```
for the default DOT_SAGE, `/scratch/$USER/.sage`, and `/dev/shm/$USER/.sage`, respectively.



---

archive/issue_comments_092975.json:
```json
{
    "body": "For now, should we tag the relevant tests with `# not tested` or [backout the whole patch](https://groups.google.com/group/sage-release/browse_thread/thread/9455213e89f94692/5aba6862d5c35b8c#5aba6862d5c35b8c)?  Other options?",
    "created_at": "2010-07-28T05:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92975",
    "user": "https://github.com/qed777"
}
```

For now, should we tag the relevant tests with `# not tested` or [backout the whole patch](https://groups.google.com/group/sage-release/browse_thread/thread/9455213e89f94692/5aba6862d5c35b8c#5aba6862d5c35b8c)?  Other options?



---

archive/issue_comments_092976.json:
```json
{
    "body": "By the way, here are the latest doctesting exist codes (cf. #9243), from the top of `sage-doctest`:\n\n```\n# Return value in process exit code:\n# 0: all tests passed\n# 1: file not found\n# 2: KeyboardInterrupt\n# 4: doctest process was terminated by a signal\n# 8: the doctesting framework raised an exception\n# 16: script called with bad options\n# 32: (used internally in sage-ptest)\n# 64: time out\n# 128: failed doctests\n```",
    "created_at": "2010-07-28T05:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92976",
    "user": "https://github.com/qed777"
}
```

By the way, here are the latest doctesting exist codes (cf. #9243), from the top of `sage-doctest`:

```
# Return value in process exit code:
# 0: all tests passed
# 1: file not found
# 2: KeyboardInterrupt
# 4: doctest process was terminated by a signal
# 8: the doctesting framework raised an exception
# 16: script called with bad options
# 32: (used internally in sage-ptest)
# 64: time out
# 128: failed doctests
```



---

archive/issue_comments_092977.json:
```json
{
    "body": "According to William on sage-release, the segfault is an intentional part of a doctest, so I've changed the ticket's title.",
    "created_at": "2010-07-28T13:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92977",
    "user": "https://github.com/nexttime"
}
```

According to William on sage-release, the segfault is an intentional part of a doctest, so I've changed the ticket's title.



---

archive/issue_comments_092978.json:
```json
{
    "body": "Changing keywords from \"fork nfs segfault\" to \"fork nfs device resource busy\".",
    "created_at": "2010-07-28T13:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92978",
    "user": "https://github.com/nexttime"
}
```

Changing keywords from "fork nfs segfault" to "fork nfs device resource busy".



---

archive/issue_comments_092979.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> For now, should we tag the relevant tests with `# not tested` or [backout the whole patch](https://groups.google.com/group/sage-release/browse_thread/thread/9455213e89f94692/5aba6862d5c35b8c#5aba6862d5c35b8c)?  Other options?\n\n\nIf we backout the whole patch, I have more confidence that the doctests will get fixed quickly.",
    "created_at": "2010-07-28T14:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92979",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:2 mpatel]:
> For now, should we tag the relevant tests with `# not tested` or [backout the whole patch](https://groups.google.com/group/sage-release/browse_thread/thread/9455213e89f94692/5aba6862d5c35b8c#5aba6862d5c35b8c)?  Other options?


If we backout the whole patch, I have more confidence that the doctests will get fixed quickly.



---

archive/issue_comments_092980.json:
```json
{
    "body": "Attachment [trac_9616-backout_9501_fork_deco.patch](tarball://root/attachments/some-uuid/ticket9616/trac_9616-backout_9501_fork_deco.patch) by @qed777 created at 2010-07-28 22:32:06\n\nBackout #9501",
    "created_at": "2010-07-28T22:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92980",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_9616-backout_9501_fork_deco.patch](tarball://root/attachments/some-uuid/ticket9616/trac_9616-backout_9501_fork_deco.patch) by @qed777 created at 2010-07-28 22:32:06

Backout #9501



---

archive/issue_comments_092981.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-28T22:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92981",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092982.json:
```json
{
    "body": "Replying to [comment:5 jhpalmieri]:\n> Replying to [comment:2 mpatel]:\n> > For now, should we tag the relevant tests with `# not tested` or [backout the whole patch](https://groups.google.com/group/sage-release/browse_thread/thread/9455213e89f94692/5aba6862d5c35b8c#5aba6862d5c35b8c)?  Other options?\n\n> \n> If we backout the whole patch, I have more confidence that the doctests will get fixed quickly.\n\n\nAdapting the procedure in [comment:ticket:9583:47 this comment] at #9583, I've attached a patch that undoes (or should undo) all of #9501.  If the patch gets a positive review, we can open a new ticket for re-merging #9501.",
    "created_at": "2010-07-28T22:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92982",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:5 jhpalmieri]:
> Replying to [comment:2 mpatel]:
> > For now, should we tag the relevant tests with `# not tested` or [backout the whole patch](https://groups.google.com/group/sage-release/browse_thread/thread/9455213e89f94692/5aba6862d5c35b8c#5aba6862d5c35b8c)?  Other options?

> 
> If we backout the whole patch, I have more confidence that the doctests will get fixed quickly.


Adapting the procedure in [comment:ticket:9583:47 this comment] at #9583, I've attached a patch that undoes (or should undo) all of #9501.  If the patch gets a positive review, we can open a new ticket for re-merging #9501.



---

archive/issue_comments_092983.json:
```json
{
    "body": "Hmmm, of course a simple procedure, but we'd back out too much in my opinion...\n\nBut I can live with that. (And I'm currently too (laz|bus)y to sort out the desirable parts of the original patch.)",
    "created_at": "2010-07-28T23:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92983",
    "user": "https://github.com/nexttime"
}
```

Hmmm, of course a simple procedure, but we'd back out too much in my opinion...

But I can live with that. (And I'm currently too (laz|bus)y to sort out the desirable parts of the original patch.)



---

archive/issue_comments_092984.json:
```json
{
    "body": "Attachment [trac_9616-backout_only_some_of_9501.patch](tarball://root/attachments/some-uuid/ticket9616/trac_9616-backout_only_some_of_9501.patch) by @nexttime created at 2010-07-28 23:44:14\n\nBackouts only ticket-relevant parts of #9501 (subset of Mitesh's patch)",
    "created_at": "2010-07-28T23:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92984",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_9616-backout_only_some_of_9501.patch](tarball://root/attachments/some-uuid/ticket9616/trac_9616-backout_only_some_of_9501.patch) by @nexttime created at 2010-07-28 23:44:14

Backouts only ticket-relevant parts of #9501 (subset of Mitesh's patch)



---

archive/issue_comments_092985.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> (And I'm currently too (laz|bus)y to sort out the desirable parts of the original patch.)\n\n\nCouldn't resist though (simpler as expected).\n\nNot very tested, only successfully ran `./sage -t -long devel/sage/sage/parallel/` and rebuilt the documentation without errors or warnings.\n(Ubuntu 9.04 x86_64, Core2, gcc 4.3.3)\n\nSo now two concurrent patches to review... ;-)",
    "created_at": "2010-07-28T23:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92985",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:7 leif]:
> (And I'm currently too (laz|bus)y to sort out the desirable parts of the original patch.)


Couldn't resist though (simpler as expected).

Not very tested, only successfully ran `./sage -t -long devel/sage/sage/parallel/` and rebuilt the documentation without errors or warnings.
(Ubuntu 9.04 x86_64, Core2, gcc 4.3.3)

So now two concurrent patches to review... ;-)



---

archive/issue_comments_092986.json:
```json
{
    "body": "I've tested mpatel's patch on 5 machines: 4 on which the problem originally occurred (sage.math and skynet machines eno, iras, and taurus) and one machine (running OS X) which didn't have the original problem.  After applying the patch, all tests pass for the directory \"parallel\" on all 5 machines.  Long doctests for the whole Sage library pass on sage.math and taurus except for previously known, unrelated, failures.\n\nI don't know if I'll get to leif's patch.\n\nSince this is a rollback to a previous situation, I think this is good enough for a positive review for mpatel's patch, though.  Opinions?",
    "created_at": "2010-07-29T00:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92986",
    "user": "https://github.com/jhpalmieri"
}
```

I've tested mpatel's patch on 5 machines: 4 on which the problem originally occurred (sage.math and skynet machines eno, iras, and taurus) and one machine (running OS X) which didn't have the original problem.  After applying the patch, all tests pass for the directory "parallel" on all 5 machines.  Long doctests for the whole Sage library pass on sage.math and taurus except for previously known, unrelated, failures.

I don't know if I'll get to leif's patch.

Since this is a rollback to a previous situation, I think this is good enough for a positive review for mpatel's patch, though.  Opinions?



---

archive/issue_comments_092987.json:
```json
{
    "body": "Let the release managers decide... ;-)",
    "created_at": "2010-07-29T00:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92987",
    "user": "https://github.com/nexttime"
}
```

Let the release managers decide... ;-)



---

archive/issue_comments_092988.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-29T00:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92988",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092989.json:
```json
{
    "body": "Replying to [comment:9 jhpalmieri]:\n> Since this is a rollback to a previous situation, I think this is good enough for a positive review for mpatel's patch, though.  Opinions?\n\n\nYou've done some good testing, and since the original patch was an enhancement, and didn't fix any bugs or failing doctests (right?), I think a positive review is warranted here.",
    "created_at": "2010-07-29T00:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92989",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:9 jhpalmieri]:
> Since this is a rollback to a previous situation, I think this is good enough for a positive review for mpatel's patch, though.  Opinions?


You've done some good testing, and since the original patch was an enhancement, and didn't fix any bugs or failing doctests (right?), I think a positive review is warranted here.



---

archive/issue_comments_092990.json:
```json
{
    "body": "Replying to [comment:11 ddrake]:\n> ... since the original patch was an enhancement, and didn't fix any bugs or failing doctests (right?)\n\n\nWell, I pushed back in mostly fixes (and improvements) to the documentation (one might consider bugfixes, too).",
    "created_at": "2010-07-29T00:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92990",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:11 ddrake]:
> ... since the original patch was an enhancement, and didn't fix any bugs or failing doctests (right?)


Well, I pushed back in mostly fixes (and improvements) to the documentation (one might consider bugfixes, too).



---

archive/issue_comments_092991.json:
```json
{
    "body": "Besides the above mentioned, this would completely miss, too:\n\n```\n       - ``reset_interface`` -- if True (the default), all the \n         pexpect interfaces are reset in the forked off \n         subprocesses.  You definitely want this, since not doing \n         this can lead to weird issues.\n```",
    "created_at": "2010-07-29T00:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92991",
    "user": "https://github.com/nexttime"
}
```

Besides the above mentioned, this would completely miss, too:

```
       - ``reset_interface`` -- if True (the default), all the 
         pexpect interfaces are reset in the forked off 
         subprocesses.  You definitely want this, since not doing 
         this can lead to weird issues.
```



---

archive/issue_comments_092992.json:
```json
{
    "body": "Ooops, forget my last comment: The reset is performed just unconditionally in Mitesh's version.",
    "created_at": "2010-07-29T00:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92992",
    "user": "https://github.com/nexttime"
}
```

Ooops, forget my last comment: The reset is performed just unconditionally in Mitesh's version.



---

archive/issue_comments_092993.json:
```json
{
    "body": "A partial backout, since it retains only some of the changes from #9501, needs a new review, which currently, at least, we don't have.  Given the need to press forward with the 4.5.2 release cycle, I'm merging [attachment:trac_9616-backout_9501_fork_deco.patch] into 4.5.2.rc0.\n\nThis may not be an ideal resolution, but it seems reasonable given the circumstances.  Absolutely no offense is intended.\n\nI've opened #9631 for re-merging #9501 after we fix the NFS/doctest problem.",
    "created_at": "2010-07-29T05:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92993",
    "user": "https://github.com/qed777"
}
```

A partial backout, since it retains only some of the changes from #9501, needs a new review, which currently, at least, we don't have.  Given the need to press forward with the 4.5.2 release cycle, I'm merging [attachment:trac_9616-backout_9501_fork_deco.patch] into 4.5.2.rc0.

This may not be an ideal resolution, but it seems reasonable given the circumstances.  Absolutely no offense is intended.

I've opened #9631 for re-merging #9501 after we fix the NFS/doctest problem.



---

archive/issue_events_023970.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-29T05:31:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9616#event-23970"
}
```



---

archive/issue_comments_092994.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-29T05:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9616#issuecomment-92994",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
