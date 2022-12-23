# Issue 4101: [with spkg, needs review] cpdef horribly broken in last Cython

Issue created by migration from https://trac.sagemath.org/ticket/4101

Original creator: robertwb

Original creation time: 2008-09-11 17:14:55

Assignee: mabshoff

The way cpdef functions were implemented broke in some classes when being used across modules. This came up now because the new coercion uses cpdef much more. This is just the old cython+bug fix rather than a new release for time reasons, and passes sage -testall with the attached (nearly trivial) patch. A sage -ba is required. 

http://sage.math.washington.edu/home/robertwb/cython/cython-0.9.8.1.1p1.spkg




---

Attachment


---

Comment by mabshoff created at 2008-09-13 00:29:28

Hi Robert,

I fixed some issues in the spkg, which is now at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc2/cython-0.9.8.1.1.p0.spkg

Note that the patch level usually starts at p0 and that the name of the spkg and the directory name were not in sync.

I am testing the spkg with the patch to the Sage library applied right now, so expect a review in about 45 minutes.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-13 01:51:26

Spkg and a following `-ba` passes doctests. Positive review. Let's hope this spkg does not bite us in the ass so late in the release cycle :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-13 01:52:10

Merged in Sage 3.1.2.rc2


---

Comment by mabshoff created at 2008-09-13 01:52:10

Resolution: fixed


---

Comment by robertwb created at 2008-09-13 03:58:41

Thanks. I realized later that I had changed the name of the spkg rather than the folder name, but I was at work by then. 

This is intentionally a p0 rather than the next release, so I'm pretty sure it won't bite us. (Famous last words...)


---

Comment by mabshoff created at 2008-09-13 04:07:07

Replying to [comment:4 robertwb]:
> Thanks. I realized later that I had changed the name of the spkg rather than the folder name, but I was at work by then. 

Cool. It would be nice if you could base future cython.spkg off this on in 3.1.2.rc2. I did some fixed to spkg-install and SPKG.txt. It would also be great if you could add to the changes in SPKG.txt once you update it.

> This is intentionally a p0 rather than the next release, so I'm pretty sure it won't bite us. 

Well, the name was p1, so that was mostly my point. I fully understand that you added only one patch on top of the latest Cython release.

> (Famous last words...)

Yeah, what could go wrong :)

I am valgrinding the startup of 3.1.2.rc2 to see if anything fishy was introduced.

Cheers,

Michael
