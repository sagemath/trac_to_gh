# Issue 2745: upgrade twisted to 8.0.1

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-04-01 00:42:44

Assignee: mabshoff

A major new version of twisted has been released and I strongly recommend that we upgrade to it for sage-3.0.  There are a ton of new features and many bug fixes. Some specifics that are relevant to dsage are:

 - The reactor now has a blockingCallFromThread method for non-reactor threads
   to use to wait for a reactor-scheduled call to return a result (#1042, #3030)
 - LoopingCall now allows you to specify the reactor to use to schedule new
   calls, allowing much better testing techniques (#2633, #2634)
 - twisted.python.log now contains a Twisted log observer which can forward
   messages to the Python logging system (#1351)
 - Log files now include seconds in the timestamps (#867)
 - PB now supports anonymous login (#439, #2312)
 - twisted.spread.jelly now supports decimal objects (#2920)
 - twisted.spread.jelly now supports all forms of sets (#2958)

Also, this release is easy_install'able. I don't know if we ever use easy_install to install packages or what the thought on it is. 



---

Comment by yi created at 2008-04-05 23:57:54

new package up at

http://sage.math.washington.edu/home/yqiang/spkgs/twisted-8.0.1.spkg

Please review & test!


---

Comment by mabshoff created at 2008-04-06 00:20:43

I guess the "Summary" is supposed to say SPGK.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-06 03:24:10

mhansen did play with this and did give it a positive review. It builds and installs fine for me. I added a mercurial repo and some other small bits.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-06 03:24:23

Merged in Sage 3.0.alpha2


---

Comment by mabshoff created at 2008-04-06 03:24:23

Resolution: fixed
