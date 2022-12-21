# Issue 2873: Customize JMOL menu

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-04-10 22:42:45

Assignee: was

It would be nice to shorten the menu quite a bit and pick the options that make sense to us.

See http://chemapps.stolaf.edu/jmol/docs/examples-11/new4.htm point 13 for how to do this.




---

Comment by jason created at 2009-02-13 21:10:04

See also the very nice writeup at http://wiki.jmol.org:81/index.php/Custom_Menus


---

Comment by jason created at 2009-02-13 21:11:12

Whoever fixes this, please make sure that #1777 is taken care of (which can be fixed by this ticket, I believe).


---

Attachment


---

Comment by jason created at 2009-02-14 09:49:23

We need both a patch and a new spkg (which contains the custom menu file).  The spkg is up at http://sage.math.washington.edu/home/jason/jmol-11.6.16.spkg (I took the opportunity to update to the latest jmol stable version).


---

Comment by jason created at 2009-02-14 10:01:53

This patch and spkg take care of #1777 too.


---

Comment by jason created at 2009-02-14 10:04:12

Changing assignee from was to jason.


---

Comment by jason created at 2009-02-14 10:04:12

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-14 13:57:09

The spkg is *not* based in the latest jmol.spkg in tree and is missing fixes to spkg-install. Bad Jason :)

Timothy: *always* check the repo and verify that it is based on the previous spkg.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 14:31:14

I will put up a new jmol spkg at #5271.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 14:51:03

Resolution: fixed


---

Comment by mabshoff created at 2009-02-14 14:51:03

Merged jmol-custom-menu.patch in Sage 3.3.rc1. 

Note that the spkg above was *not* merged, but the one at #5271.

Cheers,

Michael
