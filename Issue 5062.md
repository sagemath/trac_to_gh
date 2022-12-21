# Issue 5062: Make sure that "sage -b" checks build compatibility on shared filesystems

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-23 00:33:30

Assignee: mabshoff

This is a followup to #22:

Having thought about this and played around a little with uname it seems that it will not work and is not fine grained enough anyway. I would suggest to do write a small C program that identifies the following:

    * mode: i.e. 32, 64 bit
    * os: linux, osx, solaris, freebsd, cygwin
    * release: this would be the distribution on Linux, OSX 10.4/10.5, Solaris 10/Solaris 11/Opensolaris and so on 

The way we can properly identify the build platform and decide more intelligently if we issue a warning, i.e running the Fedora 10 build on a Fedora 9 box should abort since it doesn't work. The test should be wrapped in a shell script since the binary will obviously only run on a subset of arches, i.e. if the binary fails to run we just about and print a canned warning together with a config info saved as text that is created when building the binary.

This is enough a task to split it off to a new ticket. I have some basic code that does some of the above already for OSX since I need this kind of code while cleaning up the build system.

Thoughts?

Cheers,

Michael



---

Comment by mabshoff created at 2009-01-23 00:33:39

Changing status from new to assigned.


---

Comment by jdemeyer created at 2013-12-19 12:12:37

No idea really what this is about...


---

Comment by jdemeyer created at 2013-12-19 12:12:37

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-12-19 12:12:45

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2013-12-20 15:58:23

E.g. on skynet one could print an error when trying to run a sparc binary on x86. Though I can assure you there will be an error even without the theck ;-)  In any case, implementation would just have to compare some uname entries, no need for a C program.


---

Comment by vbraun created at 2013-12-20 15:58:23

Resolution: wontfix
