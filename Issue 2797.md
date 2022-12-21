# Issue 2797: [with spkg, needs review] fix memleaks in zn_poly

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-04-04 14:22:29

Assignee: mabshoff

A minor update to the `zn_poly` spkg I posted a few days ago. This fixes some memory leaks in the test suite and a read from uninitialised memory picked up by valgrind, and retrospectively renames the previous release to `zn_poly-0.8.alpha0` :-)



---

Attachment


---

Comment by mabshoff created at 2008-04-04 16:23:44

There are two issues with this SPKG which I have fixed:

 * the changes to SPKG.txt haven't been checked in
 * the spkg named zn_poly-0.8.p0.spkg must unpack to zn_poly-0.8.p0

I have fixed both issues [and some in accuracies in SPKG.txt, i.e. the renaming, in the SPKG I merged.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-04 16:26:56

Resolution: fixed


---

Comment by mabshoff created at 2008-04-04 16:26:56

Merged in Sage 3.0.alpha1
