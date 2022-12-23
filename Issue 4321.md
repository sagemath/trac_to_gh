# Issue 4321: wrong Unix permissions

Issue created by migration from https://trac.sagemath.org/ticket/4321

Original creator: zimmerma

Original creation time: 2008-10-18 20:33:42

Assignee: mabshoff

CC:  polybori

The Unix permissions are too restrictive in sage-3.1.4, they don't allow installation on a
multi-user system:

```
drwx------ 12 zimmerma cacao 4096 2008-10-17 10:13 /usr/local/sage-3.1.4/sage/local/include/boost
-rw-------  1 zimmerma cacao 2664 2008-09-01 15:36 /usr/local/sage-3.1.4/sage/local/man/man1/ipbori.1
```



---

Comment by mabshoff created at 2008-10-30 05:53:29

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-10-30 05:53:29

I will fix that in Sage 3.2.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-29 10:20:23

Changing priority from major to blocker.


---

Attachment

Fix man-page permissions for PolyBoRi's install target


---

Comment by PolyBoRi created at 2008-11-29 22:08:16

I believe for the man page the problem could be fixed upstream, see attached patch. 

Best regards,
  Alexander


---

Comment by mabshoff created at 2008-11-29 22:20:29

Thanks Alexander, I will test the patch and report back. The issue with the boost permissions I will fix in the spkg itself.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-01 06:49:23

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/rc1/polybori-0.5rc.p6.spkg

incorporates Alexander's fix as well as my fix to set boost permissions correctly. As a test do cp -r on $SAGE_LOCAL/include/boost as the non-owner of the files. To check for any other issues I am doing a complete cp of the Sage tree to see if anything else has permission issues.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-01 06:51:56

Oops, wrong fix. New spkg coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-01 07:15:32

The spkg in the same place has been updated and finally fixes the issue for me.

Cheers,

Michael


---

Comment by craigcitro created at 2008-12-01 08:15:26

Everything looks good.


---

Comment by mabshoff created at 2008-12-01 08:16:47

Merged in Sage 3.2.1.rc1


---

Comment by mabshoff created at 2008-12-01 08:16:47

Resolution: fixed


---

Comment by was created at 2008-12-01 08:17:57

It seems to me Michael that you reviewed the patch, and I think putting it in the spkg is just sort of applying it.  So I think all that has to be done is somebody else to check that the spkg looks good. 

I have looked in the spkg and it looks good.  I also tried building it and it built fine.  After building, I looked at the permissions and they are now right.  so... another positive review in addition to Craig's. :-)


---

Comment by mabshoff created at 2008-12-01 08:21:19

Replying to [comment:12 was]:
> It seems to me Michael that you reviewed the patch, and I think putting it in the spkg is just sort of applying it.  So I think all that has to be done is somebody else to check that the spkg looks good. 

There were two issues: one is the headers, the other one was the man page. Craig reviewed the header issue as well as Alexander's fix once I told him what it did.

> I have looked in the spkg and it looks good.  I also tried building it and it built fine.  After building, I looked at the permissions and they are now right.  so... another positive review in addition to Craig's. :-)

I did a cp of the whole Sage tree after fixing this and the Singular header permission issue and for now there are no more problems, so Paul can be assured that issue is gone for now. I will keep testing that no other permission issues return since Sage should never be released with such a permission problem.

Cheers,

Michael
