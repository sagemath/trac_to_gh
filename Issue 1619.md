# Issue 1619: update cddlib to 0.94d

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-29 04:34:07

Assignee: was




---

Comment by mabshoff created at 2007-12-29 04:37:49

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-12-29 04:37:49

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-08-26 17:23:19

The latest release is  cddlib-094f.

Cheers,

Michael


---

Comment by sbarthelemy created at 2009-01-27 16:09:12

Here a [new cddlib spkg](http://perso.crans.org/barthelemy/cddlib-094f.spkg), based on the current 094b.p3

I...

    * packaged upstream version 0.94f
    * removed some temporary files
    * adapted the allfaces.c patch
    * updated the SPKG changelog
    * did not update the dist/debian directory
    * did not integrate #3297 nor #3304
    * did not commit anything into the .hg repository 

PS: this comment was at first mis-located at #3297


---

Comment by mabshoff created at 2009-01-29 06:07:26

Nice work. I checked in all changes at

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha3/cddlib-094f.spkg

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 06:07:44

Resolution: fixed


---

Comment by mabshoff created at 2009-01-29 06:07:44

Merged in Sage 3.3.alpha3.

Cheers,

Michael
