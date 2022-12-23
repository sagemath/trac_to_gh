# Issue 5235: Detect when Sage is build on AFS and issue a warning

Issue created by migration from https://trac.sagemath.org/ticket/5235

Original creator: mabshoff

Original creation time: 2009-02-11 21:20:04

Assignee: mabshoff

From http://groups.google.com/group/sage-devel/t/894d29e0bde4550c

```
> Yes, afs is a strange filessystem and might be the root cause of your 
> trouble, but that is far from certain at this point. 


No longer far from certain. The build completed without ANY problems, 
including getting past gnutls without error. This is not unprecedented 
but somewhat surprising nevertheless. Running make test now. 

Gedaliah 
```


AFS seems to be commonly used with RHEL 4 in some instituations. It has come up twice now.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-11 21:20:12

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-11 22:52:58

Gedaliah responded to my question:

```
> In case you have a shell code snipped that identifies that the current 
> working directory is on an AFS mount I would be happy to integrate it. 


This will work unless somebody very foolishly changed the afs mount 
point to something other that /afs. 
[[ $(pwd | cut -d'/' -f2) = 'afs' ]] && echo "we are in afs" 
```


Cheers,

Michael


---

Comment by wjp created at 2010-01-16 23:21:52

Should anyone want to do this, Sun's `struct stat` has a `st_fstype` field which gives the filesystem type of a file, so from C this might be easy to check.


---

Comment by jdemeyer created at 2014-09-02 09:03:08

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-09-02 09:03:08

I don't think this issue is relevant anymore, haven't heard any such problems recently...


---

Comment by jdemeyer created at 2014-09-02 09:03:13

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-09-09 14:52:41

Resolution: fixed
