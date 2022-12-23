# Issue 4051: [with patch; needs review] Use of tar -j in sage-pkg

Issue created by migration from https://trac.sagemath.org/ticket/4051

Original creator: anakha

Original creation time: 2008-09-03 18:47:22

Assignee: anakha

The -j option to tar is a gnu tar specific option.  Workaround is to pipe output trough bzip2.  


---

Attachment

Patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-04 00:34:29

One more thing: This does introduce a dependency on bzip2. If that turns out to be a problem (we expect tar with bzip2 support anyway) we can fall back to gtar.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-04 00:36:59

Merged in Sage 3.1.2.rc0


---

Comment by mabshoff created at 2008-09-04 00:36:59

Resolution: fixed


---

Comment by anakha created at 2008-09-04 04:15:23

Replying to [comment:2 mabshoff]:
> One more thing: This does introduce a dependency on bzip2. If that turns out to be a problem (we expect tar with bzip2 support anyway) we can fall back to gtar.

tar -j just invokes the bzip2 command.  So there is exactly the same dependency.  Try it on a system without bzip2 installed.

> Cheers,
> 
> Michael
