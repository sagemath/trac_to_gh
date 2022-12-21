# Issue 5803: [with patch, needs review] Upgrade Cython to 0.11.1

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-04-16 08:38:38

Assignee: mabshoff

Spkg up at http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.1.spkg


---

Attachment


---

Comment by mabshoff created at 2009-04-24 07:41:32

Ok, positive review on the spkg. I did a number of cleanups and added a proper SPKG.txt changelog entry that Robert has been skipping forever. In the ultimate move of irony I also deleted the .hg repo inside the src repo (given the current discussion on the cython mailing list). That way the size of the spkg decreased by 3.5 MB :)

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/alpha0/cython-0.11.1.p0.spkg

Robert: Please base future spkgs on this one since I have cleaned up this spkg before. You have then based it on the a non-clean spkg and last time I let it slide, but it won't happen again and I will give it a non-positive review :)

Doctesting the patch right now, but changing the review in anticipation.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 08:13:59

Resolution: fixed


---

Comment by mabshoff created at 2009-04-24 08:13:59

Merged patch and spkg into Sage 3.4.2.alpha0.

Cheers,

Michael
