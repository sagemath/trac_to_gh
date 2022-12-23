# Issue 4886: notebook -- make notebook autosave configurable from notebook settings

Issue created by migration from https://trac.sagemath.org/ticket/4886

Original creator: TimothyClemans

Original creation time: 2008-12-29 08:09:34

Assignee: boothby

CC:  wjp

Depends on #4552


---

Attachment


---

Comment by ddrake created at 2009-09-05 02:56:22

I'm changing this to needs work. This ticket and #4887 have basically the same title and both have patch. I don't understand why Timothy opened two tickets and added a patch to each to solve the same problem. Looking over the patches, it appears that the patch at #4887 is supposed to be applied on top of the patch here, which is really annoying; if you want to fix something about a patch, fix it and attach a new one, don't make an entirely new ticket and upload a new patch to fix the problems in your first patch.

Also, aside from issues related to using trac efficiently, didn't a lot of work on the autosave interval go in? I thought that some patches making the autosave a lot better got merged a while back.


---

Comment by was created at 2009-12-09 14:28:09

Resolution: invalid


---

Comment by kcrisman created at 2014-09-18 16:06:44

See #5459.  This is about the _notebook_ autosave interval.
