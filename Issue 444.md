# Issue 444: solve the rubik's cube fast!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-18 20:32:09

Assignee: was

Hi:

Two Rubik's cube programs have just been posted to
http://sage.math.washington.edu/home/wdj/rubik/
Both one is GPL's (Michael Reid's) and the other is
under the MIT license (Dik Winter's). These programs
have been around for some time but have never
been licensed until recently (and I thank both the
authors for kindly replying to my emails and agreeing
to an open source license). The tarballs you will find there
are identical to the author's version except that I have
added a license.txt following their email directions.
Now that the semester has started, I lack the time to
do anything but am emailing the list in case anyone
is interested and has the time to create Python
wrappers for one (or both) of them. SAGE
currently has a Rubik's cube solver which uses GAP
and is quite slow and far from optimal. Maybe one of these
could be used instead one day?
 --- David Joyner


---

Comment by robertwb created at 2007-09-12 09:22:35

Here's an spkg of solvers, needs to be tested on lots of different computers. 

http://sage.math.washington.edu/home/robertwb/spkgs/


---

Comment by robertwb created at 2007-09-12 09:22:35

Changing status from new to assigned.


---

Comment by robertwb created at 2007-09-12 09:22:35

Changing assignee from was to robertwb.


---

Attachment


---

Comment by mabshoff created at 2007-10-19 18:33:44

Is this in or not? What should we do with this patch?

Cheers,

Michael


---

Comment by cwitty created at 2007-10-26 04:26:53

I tried the spkg and the associated patch; they worked fine (on 32-bit x86 Linux; Debian testing).  However, I don't think the solvers belong as a standard spkg (adding a third of a megabyte to every Sage download); I think they should be optional.  And if the spkg is optional, then the patch has some problems: it turns a working-by-default (if slow) method into a method which raises an exception when the spkg is not installed.

I think the patch should be modified to either leave the original GAP algorithm as the default, or to change the default but automatically fall back to GAP if the solvers are not installed.

Also, there should be at least one doctest for each solver.

I'm removing "[with patch]" from the summary for now; anybody who supplies a revised patch should reinstate it (or, I guess, you could reinstate it if you want to argue that the solvers should be a standard Sage package).


---

Attachment


---

Comment by robertwb created at 2007-11-27 11:39:08

In light of David Joyner's re-release of his book on Solving the Rubiks cube (using Sage) I think a fast solver is important to include even if just for marketing purposes. The GAP implementation isn't just a little bit slow, it's almost unusable (especially compared to nearly instantaneous solutions provided by the other packages). 

Also I think 370K is really a quite small, 0.2% of the size of Sage itself, compared to the provided functionality. 

I did, however, add doctests for the solvers.


---

Attachment


---

Attachment


---

Comment by cwitty created at 2007-12-15 05:39:59

OK, assuming the rubik solvers are to become a standard part of Sage, then this patch set looks good to me.

To install:
add http://sage.math.washington.edu/home/robertwb/spkgs/rubiks-20070912.spkg as a standard spkg,
then apply all 4 attachments to this bug (one bundle, and 3 patches) in order.


---

Comment by mabshoff created at 2007-12-15 11:23:27

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 11:23:27

Merged in 2.9.rc0.
