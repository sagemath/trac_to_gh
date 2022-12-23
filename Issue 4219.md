# Issue 4219: MacOSX: work around java detection hang in r due to "Mac OS X 10.5 Update 2"

Issue created by migration from https://trac.sagemath.org/ticket/4219

Original creator: mabshoff

Original creation time: 2008-09-30 02:39:04

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



---

Comment by mabshoff created at 2008-09-30 02:39:10

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-30 18:58:08

Spkg coming up shortly.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-13 00:29:01

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/rc0/r-2.6.1.p21.spkg

fixes the issue.

Cheers,

Michael


---

Comment by mhansen created at 2008-10-13 00:34:58

Looks good to me.


---

Comment by mabshoff created at 2008-10-13 00:35:44

Resolution: fixed


---

Comment by mabshoff created at 2008-10-13 00:35:44

Merged in Sage 3.1.3.rc0
