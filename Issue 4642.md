# Issue 4642: Limit sage-flags.txt to vector math flags

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-28 07:41:37

Assignee: mabshoff

Jeffrey reported:

```
I've just downloaded and launched Sage on an Ubuntu 8.10 box.  I 
unzipped the file and ran ./sage and got this: 
  WARNING!  This Sage install was built on a machine that supports 
  instructions that are not available on this computer.  Sage will 
  likely fail with ILLEGAL INSTRUCTION errors! The following processor 
  flags were on the build machine but are not on this computer: 
  nx up 
I downloaded this image of Sage: 
  sage-3.2-ubuntu32bit-intel-i686-Linux.tar.gz 
Is there anything I can do? 
Thanks in advance 
Jeffrey 
```


The problem is that nx for example is a no execute flag and has zero impact on compatibility for binaries. We should only trac sse, sse2 and see3 flags (and potentially others, but I will do some research here.

Cheers,

Michael


---

Comment by was created at 2008-11-28 15:42:56

Can somebody please post a list of flags to be ignored here.  Obviously up and nx are on it.  Anything else?


---

Comment by was created at 2008-11-28 15:42:56

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-11-28 18:28:02

Replying to [comment:1 was]:
> Can somebody please post a list of flags to be ignored here.  Obviously up and nx are on it.  Anything else?

Why don't we do it the other way around, i.e. only consider flags we know cause trouble: sse, sse2, sse4 and maybe three or four more. These flags are vectorization flags and are the only ones I am aware of that need consideration. All the other flags are CPU properties that aren't related to instruction sets.

Cheers,

Michael


---

Attachment

I named the patch trac_4642_sage.patch but it should be trac_4642_scripts.patch


---

Comment by mabshoff created at 2008-11-28 21:32:11

This is a true blocker for 3.2.1. Positive review, but I will do some more testing.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 00:13:00

Two more flags I would consider:

 * pni - prescott new instructions
 * cmov - an older instruction present on Pentiums or higher - that might be pushing it, but you never know :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 00:25:41

I did some more testing and the patch works as expected. One problem is when one does a -bdist from a 3.2 install with the old flags then the new binary complains about all the lfags that are now omitted, but since one generally does not -bdist repeatedly from the same install that seems fine by me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 04:28:23

Updated version of William's patch with cmov and pni flags added


---

Comment by mabshoff created at 2008-11-29 04:28:57

Resolution: fixed


---

Attachment

Merged in Sage 3.2.1.rc0


---

Comment by mabshoff created at 2008-11-29 04:29:32

For the record: trac_4642_sage.2.patch was merged.

Cheers,

Michael
