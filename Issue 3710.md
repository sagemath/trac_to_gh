# Issue 3710: Segfault in Tachyon on some latest GCC versions

Issue created by migration from https://trac.sagemath.org/ticket/3710

Original creator: aginiewicz

Original creation time: 2008-07-23 00:18:44

Assignee: was

Segfault confirmed on 32 bit linux with GCC 4.3.1 and GCC 4.2.4, versions prior to GCC 4.2.3 including should work, status of version 4.3.0 is still not known, also status of 64 bit builds is not known. This bug is bug in gcc or bug in Tachyon that showed up after some changes to GCC somewhere in between 2008-02-01 and 2008-05-19. Status of 64 bit version is unknown because I have no access to hardware with those compile versions.

When 32 bit threaded version of Tachyon is built using "make linux-thr" and used to render attached scene, it segfaults around 59%. Non threaded version works (one built with "make linux"), threaded version works when -fno-crossjumping -fno-reorder-blocks compilation flags are added.

Still working to get smaller test case and informations on gcc 4.3.0, there will hopefully be patch/spkg soon.

This ticket is follow-up of report from "Sage 3.0.6.alpha0 released" sage-devel thread.



---

Comment by aginiewicz created at 2008-07-23 00:19:25

testcase made from simplified doctest example that was found to segfault


---

Comment by aginiewicz created at 2008-07-23 00:20:15

Changing assignee from was to aginiewicz.


---

Attachment


---

Comment by aginiewicz created at 2008-07-23 00:20:15

Changing status from new to assigned.


---

Comment by aginiewicz created at 2008-08-02 02:01:52

There's what I did to fix it: I added gcc version check and set GCCFIX variable to flags needed to fix the issue for gcc 4.2.4 and all 4.3.* (I wasn't able to test 4.3.0), also added simple patch that adds it to src/unix/Make-arch... I put it into patches directory and spkg-install, basing how it's done with some other packages

I hope all is ok because that's my only second fix but first tracked from start and with own ticket... if anything would look better other way I'd be happy to know


---

Comment by aginiewicz created at 2008-08-03 00:35:47

btw, as this is segfault fix only I guess it could go to 3.1 so I reassign it to 3.1 as I don't know if before release tickets ready to review from next milestone are searched for... are there reasons for it to not make in for 3.1?

cheers,
Andrzej.


---

Comment by aginiewicz created at 2008-08-17 20:06:57

Changed spkg along with information from #3882 - there are both patch (to generate new file if new version of Tachyon will come out) and patched file that is copied over.


---

Comment by mabshoff created at 2008-08-22 21:23:48

Hi Andrzej,

a couple remarks:

 * You deleted the hg history of the spkg - that is not good :)
 * Instead of the construct using "gcc -v ..." it is much easier to use "gcc -dumpversion". I did that in the updated spkg.
 * Please do not attach spkgs to tickets. Put them up somewhere and post a link.

I am giving the spkg with the changes I made a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-22 21:42:25

For the record: the updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha0/tachyon-0.98beta.p6.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-22 21:42:38

Merged in Sage 3.1.2.alpha0


---

Comment by mabshoff created at 2008-08-22 21:42:38

Resolution: fixed


---

Comment by aginiewicz created at 2008-08-23 03:05:16

will know next time, thanks for pointing all this out!
