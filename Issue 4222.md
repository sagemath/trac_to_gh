# Issue 4222: Building R fails due to problem with readline

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2008-09-30 13:09:01

Assignee: mabshoff

Keywords: R, readline, .d-files

Under GNU/Linux i686, the built of R failed, and the complaint is
`  making sys-std.d from sys-std.c`
`  sys-std.c:401:33: error: readline/readline.h: No such file or directory`
`  sys-std.c:431:32: error: readline/history.h: No such file or directory`

mabshoff reportedly has hit that problem before, it seems to be a bug in R when doing processing on .d files, but it isn't fixed yet.




---

Comment by mabshoff created at 2008-09-30 13:22:52

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/r-2.6.1.p20.spkg

should fix the issue by setting CPPFLAGS correctly. The issue I saw on another box is likely orthogonal.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-30 13:22:52

Changing status from new to assigned.


---

Comment by SimonKing created at 2008-09-30 13:39:07

I tried to replace the old with the new package and did "make" again, but it did not help.


---

Comment by mabshoff created at 2008-09-30 13:41:26

The commonly used label is "needs work"

Cheers,

Michael


---

Comment by SimonKing created at 2008-09-30 18:16:07

The most recent version of that spkg (md5sum de0de83b25ca7b9e0a65246c067f0afa) works! Now R builds although the global readline headers are not present.

So, I guess this is a positive review.


---

Comment by mabshoff created at 2008-09-30 18:17:33

Resolution: fixed


---

Comment by mabshoff created at 2008-09-30 18:17:33

Merged in Sage 3.1.3.alpha2
