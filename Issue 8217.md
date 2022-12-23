# Issue 8217: make 4ti2 an optional package

Issue created by migration from https://trac.sagemath.org/ticket/8217

Original creator: mhampton

Original creation time: 2010-02-08 20:28:50

Assignee: tbd

The 4ti2 package should be cleaned up and made into an optional package.

I know of no build issues.  The .DS_Store files from OS X need to be removed, it needs to be under mercurial revision control, and the upstream project should be checked for updates.  After that I know of no reason why this shouldn't be an optional package.


---

Comment by wdj created at 2010-02-09 18:01:47

This seems reasonable. I think this is supposed to be voted on on sage-devel? Also, a link to the spkg would be helpful.


---

Comment by jhpalmieri created at 2010-02-09 19:33:40

See also #5489.


---

Comment by mhampton created at 2010-10-20 02:15:50

Spkg at:
[http://sage.math.washington.edu/home/mhampton/4ti2-3.2.1.p1.spkg](http://sage.math.washington.edu/home/mhampton/4ti2-3.2.1.p1.spkg)
addresses all the points above.  Please add to optional packages and remove the 4ti2.p0 package from experimental.


---

Comment by mhampton created at 2010-10-20 02:16:05

Changing status from new to needs_review.


---

Comment by mhampton created at 2011-01-04 21:57:52

Oops, I reversed the version order, should be this:

[http://sage.math.washington.edu/home/mhampton/4ti2-1.3.2.p1.spkg](http://sage.math.washington.edu/home/mhampton/4ti2-1.3.2.p1.spkg)


---

Comment by wdj created at 2011-01-17 17:30:18

At the very least, this should replace the version currently posted, since Marshall's newest version at least installs fine (on 10.6.6 macs and on ubuntu linux), whereas 
the older version posted on the sage website doesn't install at all.


---

Comment by mhampton created at 2011-03-22 20:17:08

I have tested this on OS X 10.5 and 10.6; 64-bit linux (Ubuntu 10.04), and solaris (the machine Mark on skynet).


---

Comment by dperkinson created at 2011-09-13 23:50:33

I just tested 4ti2-1.3.2.p1.spkg on Ubuntu 11.04 with sage-4.7.1 on a 64bit Dell Optiplex.  There were no problems with the installation, and it worked with several calculations involving sandpiles that require 4ti2.


---

Comment by dperkinson created at 2011-09-13 23:50:33

Changing status from needs_review to positive_review.


---

Comment by leif created at 2011-09-16 11:32:51

Changing keywords from "" to "sandpiles".


---

Comment by leif created at 2011-09-17 04:31:27

Resolution: fixed
