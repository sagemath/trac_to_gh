# Issue 3043: The SPKG.txt  of the gfan spkg does not specify license exactly

Issue created by migration from https://trac.sagemath.org/ticket/3043

Original creator: broune

Original creation time: 2008-04-27 12:58:06

Assignee: malb

The gfan SPKG.txt says:

## License
 * GPL

it does not say which version of the GPL it is.



---

Comment by mabshoff created at 2008-04-29 06:54:04

Well, the gfan code base is rather sloppy in this regard:

 * it never specifies the license other than GPL
 * zero files have a copyright statement in them

So in conclusion this must be solved upstream by the author. The FSF read on this is if you include a version of the GPL Version X then your software is licensed under GPL Version X+

Cheers,

Michael


---

Comment by malb created at 2008-06-03 14:16:54

Remove assignee malb.


---

Comment by AlexGhitza created at 2010-01-02 13:18:41

Both the version of gfan that's currently in Sage (0.3) and the latest version (0.4plus) have a file COPYING which is just the text of GPL version 2.  I would say that's pretty clear, and it should be in the file SPKG.txt.


---

Comment by mvngu created at 2010-01-25 14:13:32

Close as fixed by #7820.


---

Comment by mvngu created at 2010-01-25 14:13:32

Resolution: fixed
