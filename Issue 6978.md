# Issue 6978: [patch, needs review] fixes matplotlib to compile in cygwin

Issue created by migration from Trac.

Original creator: certik

Original creation time: 2009-09-21 16:41:33

Assignee: tbd

Here is a fixed package:

http://femhub.googlecode.com/files/matplotlib-0.98.5.3rc0-svn6910.p5.spkg


---

Comment by jason created at 2009-09-21 22:12:22

The latest matplotlib we have in Sage is 0.99, though.  It's in 4.1.2 already.  See #5448 for the spkg.

I was just going to update the spkg to have 0.99.1, which was just pre-announced on matplotlib-devel (barring any problems) as svn 7813.

So at bare minimum, the spkg above needs to use the spkg from #5448.  Ondrej, if you want to update to 0.99.1, that would be great too.  0.99.1 obsoletes several of the patches in the spkg, as they've been merged upstream.


---

Comment by certik created at 2009-09-21 22:18:13

I'll do so. I don't know why I used 0.98.5. I will first build femhub with this tonight and if all works, update matplotlib and see if I can fix that one too.


---

Comment by was created at 2009-09-22 09:10:08

the new matplotlib already fixed this problem. so closed as invalid.


---

Comment by was created at 2009-09-22 09:10:08

Resolution: fixed


---

Comment by mvngu created at 2009-09-22 16:59:38

Changing status from closed to reopened.


---

Comment by mvngu created at 2009-09-22 16:59:38

Resolution changed from fixed to 


---

Comment by mvngu created at 2009-09-22 16:59:46

Resolution: invalid
