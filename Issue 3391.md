# Issue 3391: update scipy to match the numpy 1.1.0 release

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-06-10 19:06:36

Assignee: mabshoff

CC:  jason jkantor

#3390 updates numpy to 1.1.0. Since that no longer works with the last stable release we also need to upgrade scipy to svn - figure out which revision to use.


---

Comment by robertwb created at 2008-07-08 23:58:02

See if this fixes the issue at #2303 and re-enable the option if so. (Though perhaps with a rewrite to remove the exessive string processing...)


---

Comment by mabshoff created at 2008-09-26 07:08:05

This is now the 1.2.0 numpy release once we merge #4200. We do need this since otherwise we get a boadload of deprecation warnings.

Cheers,

Michael


---

Comment by jason created at 2008-09-27 06:23:53

Updated spkg at http://sage.math.washington.edu/home/jason/scipy-20080927-0.6.spkg

I have successfully installed it.  I haven't run doctests yet.


---

Comment by jason created at 2008-09-27 06:35:17

Actually, use this spkg: http://sage.math.washington.edu/home/jason/scipy-0.7r4752svn.spkg


---

Comment by mabshoff created at 2008-09-27 07:18:50

I fixed a couple tiny issues and 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha2/scipy-0.7r4752svn.spkg

is the latest version. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-27 07:38:25

We have to fix some deprecation warning, but that will be fixed via #4205.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-27 07:38:37

Merged in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-27 07:38:37

Resolution: fixed


---

Comment by mabshoff created at 2008-09-27 22:21:54

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-09-27 22:21:54

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-09-27 22:21:54

Due to some trouble with deprecation and other bad, bad things reopen this for now. We will deal with the fallout post Sage 3.1.3. For some details about the trouble see #4205 and #4210.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-12 10:12:50

Note that there are various tickets which will can be resolved at the same time as the update.

Cheers,

Michael


---

Comment by jason created at 2009-05-27 08:03:35

A new spkg for scipy 0.7.0 is here: http://sage.math.washington.edu/home/jason/scipy-0.7.spkg

I'm attaching a patch which fixes many of the errors and deprecations.  There are a few other errors I am inquiring on the scipy mailing list about.


---

Attachment


---

Comment by jason created at 2009-05-27 22:14:17

#4205 can likely be closed once this ticket is closed.  See also #6140 for the numpy update.


---

Comment by jkantor created at 2009-06-01 08:31:31

Looks good, positive review.


---

Comment by craigcitro created at 2009-06-12 06:58:21

spkg and patch merged in 4.0.2.alpha0.


---

Comment by craigcitro created at 2009-06-12 06:58:21

Resolution: fixed


---

Comment by craigcitro created at 2009-06-12 06:58:39

Oops, forgot a field.
