# Issue 2458: bug in linbox's spkg-install: ${SAGE_LCOAL}

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-03-10 14:47:59

Assignee: mabshoff

Francois noted in http://groups.google.com/group/sage-devel/browse_thread/thread/4a902c07ebb7c45d that

```
In linbox in the spkg-install file on line 41 we have an interesting
reference to ${SAGE_LCOAL}. 
```



---

Comment by mabshoff created at 2008-03-10 14:53:58

An updated spkg which removes that elif case (since it is useless and leads to potential misdetection) can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.3/rc4/linbox-1.1.5rc2.p2.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-10 14:53:58

Changing status from new to assigned.


---

Comment by was created at 2008-03-10 15:27:34

Looks good to me, in that nothing new that is bad is introduced and it fixes the typo.  Of course I'm not saying linbox*spkg is perfect...


---

Comment by mabshoff created at 2008-03-10 17:17:51

Resolution: fixed


---

Comment by mabshoff created at 2008-03-10 17:17:51

Merged in Sage 2.10.3.rc4
