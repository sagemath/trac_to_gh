# Issue 4147: Upgrade to linbox-1.1.6

Issue created by migration from https://trac.sagemath.org/ticket/4147

Original creator: cpernet

Original creation time: 2008-09-19 00:37:38

Assignee: cpernet

Upgrade the linbox spkg to upstream latest version, that will be released as v1.1.6.
This is a defect since the current 1.1.6rc1 version does not compile under cygwin (linker and gcc-3.4 related issues).


---

Comment by cpernet created at 2008-09-19 00:43:49

The proposed spkg is here: [http://sage.math.washington.edu/home/pernet/linbox-1.1.6.spkg](http://sage.math.washington.edu/home/pernet/linbox-1.1.6.spkg)

Already succesfully tested on sage.math and on my x86_32 Linux box.


---

Comment by cpernet created at 2008-09-19 00:43:49

Changing priority from trivial to major.


---

Comment by mabshoff created at 2008-09-20 01:48:12

Spkg looks good to me. I added some code to touch the extensions linked against LinBox so they are automatically rebuild when doing a "sage -b". The updated spkg is in

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha0/linbox-1.1.6.spkg

Positive review, but I am doing some more build testing to be sure the spkg actually works.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-20 02:46:22

Merged in Sage 3.1.3.alpha0


---

Comment by mabshoff created at 2008-09-20 02:46:22

Resolution: fixed
