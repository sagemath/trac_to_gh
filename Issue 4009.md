# Issue 4009: [with spkg, needs review] OSX 10.4/5: build R without the aqua support

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-08-30 23:46:01

Assignee: mabshoff

This is a followup to #4407: When we build R on OSX we per default build extensions that depend on OSX specific frameworks, namely aqua dependent code. That FrameWork ends up pulling in Apple's libpng.dylib which is incompatible with the one we build. Consequently the build of R fails. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha3/r-2.6.1.p18.spkg

disables aqua support for R just like the 64 bit OSX build. The spkg builds fine on OSX 10.4 and 10.5 and passes doctests. 

Cheers,

Michael

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-30 23:46:07

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-30 23:52:21

Merged in Sage 3.1.2.alpha3


---

Comment by mabshoff created at 2008-08-30 23:52:21

Resolution: fixed
