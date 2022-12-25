# Issue 4219: MacOSX: work around java detection hang in r due to "Mac OS X 10.5 Update 2"

archive/issues_004219.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n[7:13pm] dphilp: mabshoff: I have the Java compiler issue now.  Any requests?\n[7:14pm] mabshoff: can you change the configure script to use \"#!/bin/bash -x\" and see what happens in the configure log?\n[7:15pm] dphilp: that's sage-3.1.2/spkg/build/r-2.6.1.p19/src/configure, first line change?\n[7:15pm] mabshoff: yes\n[7:15pm] dphilp: and then \"make\" from sageroot?\n[7:15pm] mabshoff: Nope, you might want to run sage -sh\n[7:16pm] mabshoff: cd into the sage-3.1.2/spkg/build/r-2.6.1.p19 directory and run ./spkg-install there\n[7:17pm] dphilp: Incidentally the \"check\" exited with Error 130 if that's useful.\n[7:17pm] mabshoff: mmmh\n[7:17pm] mabshoff: I thought it hangs?\n[7:18pm] dphilp: When I pressed Ctrl-C\n[7:18pm] mabshoff: ok\n[7:18pm] mabshoff: I assume the java binary works?\n[7:18pm] mabshoff: Which line exactly hangs?\n[7:18pm] dphilp: Hang on.  I just ran ./spkg-install.\n[7:19pm] dphilp: Last output lines are:\n[7:19pm] mabshoff: I mean while check does hang.\n[7:19pm] dphilp: Eh??\n[7:19pm] mabshoff: the last line in configure that hanks\n[7:19pm] mabshoff: *hangs\n[7:20pm] mabshoff: There are various java checks in configure\n[7:20pm] dphilp: When checking whether Java compiler works...\n[7:20pm] dphilp: When checking whether Java compiler works...\n[7:20pm] dphilp: \"checking whether Java compiler works...\"\n[7:20pm] dphilp: Ignore first two lines...\n[7:20pm] dphilp: The \"checking whether Java compiler works...\" was what failed.  Now, javac has failed.\n[7:20pm] dphilp: (hanged)\n[7:20pm] dphilp: \"+ /usr/bin/javac A.java\"\n[7:20pm] mabshoff: ok\n[7:21pm] mabshoff: can you add two scripts to the $SAGE_LOCAL/bin directory\n[7:21pm] mabshoff: java and javac, both like the following\n[7:21pm] mabshoff: #!/usr/bin/env bash\n[7:21pm] dphilp: ok\n[7:21pm] mabshoff: exit 1\n[7:21pm] mabshoff: And make them executable. Then R should pick them up.\n[7:23pm] dphilp: Scripts are made.  I will kill the spkg-install, then rerun?\n[7:23pm] mabshoff: yes, exactly\n[7:24pm] dphilp: Configure seems to have finished, there is a lot of \"mkdir\" and \"making\"\n[7:24pm] mabshoff: good, so we have a temporary workaround.\n[7:24pm] mabshoff: You should remove those scripts after R is build since jmol will otherwise fail\n[7:25pm] jason- joined the chat room.\n[7:26pm] dphilp: ok, I'm still using 3.1.1 anyway.\n[7:27pm] mabshoff: Well, no problem there.\n[7:28pm] dphilp: That macenstein comment refers to 10.5.2, not Java update 2.\n[7:28pm] mabshoff: I also mean in the spkg-install we will use two scirpts like that to fake java and javac during the build, then remove them once R is done building.\n[7:28pm] mabshoff: ok\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4219\n\n",
    "created_at": "2008-09-30T02:39:04Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "MacOSX: work around java detection hang in r due to \"Mac OS X 10.5 Update 2\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4219",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
[7:13pm] dphilp: mabshoff: I have the Java compiler issue now.  Any requests?
[7:14pm] mabshoff: can you change the configure script to use "#!/bin/bash -x" and see what happens in the configure log?
[7:15pm] dphilp: that's sage-3.1.2/spkg/build/r-2.6.1.p19/src/configure, first line change?
[7:15pm] mabshoff: yes
[7:15pm] dphilp: and then "make" from sageroot?
[7:15pm] mabshoff: Nope, you might want to run sage -sh
[7:16pm] mabshoff: cd into the sage-3.1.2/spkg/build/r-2.6.1.p19 directory and run ./spkg-install there
[7:17pm] dphilp: Incidentally the "check" exited with Error 130 if that's useful.
[7:17pm] mabshoff: mmmh
[7:17pm] mabshoff: I thought it hangs?
[7:18pm] dphilp: When I pressed Ctrl-C
[7:18pm] mabshoff: ok
[7:18pm] mabshoff: I assume the java binary works?
[7:18pm] mabshoff: Which line exactly hangs?
[7:18pm] dphilp: Hang on.  I just ran ./spkg-install.
[7:19pm] dphilp: Last output lines are:
[7:19pm] mabshoff: I mean while check does hang.
[7:19pm] dphilp: Eh??
[7:19pm] mabshoff: the last line in configure that hanks
[7:19pm] mabshoff: *hangs
[7:20pm] mabshoff: There are various java checks in configure
[7:20pm] dphilp: When checking whether Java compiler works...
[7:20pm] dphilp: When checking whether Java compiler works...
[7:20pm] dphilp: "checking whether Java compiler works..."
[7:20pm] dphilp: Ignore first two lines...
[7:20pm] dphilp: The "checking whether Java compiler works..." was what failed.  Now, javac has failed.
[7:20pm] dphilp: (hanged)
[7:20pm] dphilp: "+ /usr/bin/javac A.java"
[7:20pm] mabshoff: ok
[7:21pm] mabshoff: can you add two scripts to the $SAGE_LOCAL/bin directory
[7:21pm] mabshoff: java and javac, both like the following
[7:21pm] mabshoff: #!/usr/bin/env bash
[7:21pm] dphilp: ok
[7:21pm] mabshoff: exit 1
[7:21pm] mabshoff: And make them executable. Then R should pick them up.
[7:23pm] dphilp: Scripts are made.  I will kill the spkg-install, then rerun?
[7:23pm] mabshoff: yes, exactly
[7:24pm] dphilp: Configure seems to have finished, there is a lot of "mkdir" and "making"
[7:24pm] mabshoff: good, so we have a temporary workaround.
[7:24pm] mabshoff: You should remove those scripts after R is build since jmol will otherwise fail
[7:25pm] jason- joined the chat room.
[7:26pm] dphilp: ok, I'm still using 3.1.1 anyway.
[7:27pm] mabshoff: Well, no problem there.
[7:28pm] dphilp: That macenstein comment refers to 10.5.2, not Java update 2.
[7:28pm] mabshoff: I also mean in the spkg-install we will use two scirpts like that to fake java and javac during the build, then remove them once R is done building.
[7:28pm] mabshoff: ok
```


Issue created by migration from https://trac.sagemath.org/ticket/4219





---

archive/issue_comments_030599.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-30T02:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4219#issuecomment-30599",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030600.json:
```json
{
    "body": "Spkg coming up shortly.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-30T18:58:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4219#issuecomment-30600",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Spkg coming up shortly.

Cheers,

Michael



---

archive/issue_comments_030601.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/rc0/r-2.6.1.p21.spkg\n\nfixes the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-13T00:29:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4219#issuecomment-30601",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/rc0/r-2.6.1.p21.spkg

fixes the issue.

Cheers,

Michael



---

archive/issue_comments_030602.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-10-13T00:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4219#issuecomment-30602",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_004456.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-13T00:35:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4219",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4219#event-4456"
}
```



---

archive/issue_comments_030603.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-13T00:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4219#issuecomment-30603",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030604.json:
```json
{
    "body": "Merged in Sage 3.1.3.rc0",
    "created_at": "2008-10-13T00:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4219#issuecomment-30604",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.rc0
