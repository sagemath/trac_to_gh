# Issue 8067: New linbox-1.1.6.p3.spkg works with Open Solaris 64 bit

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2010-01-25 23:04:06

Assignee: drkirkby

CC:  drkirby was

Make sure SAGE64="yes" is respected on Open Solaris 64 bit

The package can be found here:
[http://boxen.math.washington.edu/home/jsp/ports/linbox-1.1.6.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/linbox-1.1.6.p3.spkg)

Jaap




---

Comment by jsp created at 2010-01-25 23:04:19

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-26 11:36:38

Without some way to be able to see what you have changed, it is difficult to review. Again, without a patch, it could never be integrated with anyone else that might change this package. 

I really like the fact that you have made a complete .spkg file, as patches are difficult to review too. But having both, it's possible to see the changes, and test it complete. 

Dave


---

Comment by drkirkby created at 2010-01-26 11:36:38

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by jsp created at 2010-01-26 18:16:45

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-01-27 12:01:25

Changing type from enhancement to defect.


---

Comment by drkirkby created at 2010-01-27 12:01:25

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-27 12:01:25

That's fine. My only long-term concern is that hard-coding -m64 is not a great idea, since it is not portable, but hopefully we will have a solution to that. 

I've changed it to 'defect'  rather than 'enhancement', as the latter is supposed to be used where you have enhanced Sage - i.e normally by adding functionality, or similar. But in this case you have corrected a defect. 

Dave


---

Comment by mpatel created at 2010-02-11 15:17:28

Resolution: fixed
