# Issue 7726: Upgrade biopython package to 1.53

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2009-12-17 19:10:15

Assignee: tbd

CC:  awebb

Keywords: biopython

Biopython was released December 15th, 2009.  No major changes were made, so the new package just updates the source and SPKG.txt.


---

Comment by mhampton created at 2009-12-17 19:11:15

New package available at:
[http://sage.math.washington.edu/home/mhampton/biopython-1.53.p0.spkg](http://sage.math.washington.edu/home/mhampton/biopython-1.53.p0.spkg)


---

Comment by mhampton created at 2009-12-17 19:11:15

Changing status from new to needs_review.


---

Comment by awebb created at 2009-12-17 21:24:38

The package installs and the check runs fine. I got a couple of warnings from the BioSQL test but that seems to be expected if I understand the code. 

One small thing: The changes haven't been committed to the hg depository in the package. Otherwise, it looks good to me.

Adam


---

Comment by awebb created at 2009-12-17 21:24:38

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2009-12-17 22:52:00

Thanks for the quick review.  I commited the changes in hg, and removed a couple of .DS_Store files that my mac had added.  This new package is up at the same link above.


---

Comment by mhansen created at 2009-12-20 07:29:47

Resolution: fixed


---

Comment by chapoton created at 2017-07-19 08:44:30

wrong name
