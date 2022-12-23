# Issue 8657: libgcrypt spkg has incorrect DSO linking

Issue created by migration from https://trac.sagemath.org/ticket/8657

Original creator: vbraun

Original creation time: 2010-04-07 21:54:40

Assignee: GeorgSWeber

CC:  pjeremy drkirby was

Keywords: DSO

The libgcrypt src/tests/ have a subtle linker bug which is exposed by the DSO linking changes for Fedora 13, see https://fedoraproject.org/wiki/UnderstandingDSOLinkChange. This version adds libgpg-error to the link command line.

The change is completely safe and is required to compile libgcrypt on Fedora 13 (beta).

http://www.stp.dias.ie/~vbraun/Sage/spkg/libgcrypt-1.4.4.p3.spkg


---

Comment by mhansen created at 2010-06-09 17:14:20

Duplicate of #9189.  I'm not sure why I didn't see this one before.


---

Comment by mhansen created at 2010-06-09 17:14:20

Resolution: duplicate
