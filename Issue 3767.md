# Issue 3767: move jquery into its own spkg

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-08-03 19:27:58

Assignee: mabshoff

CC:  wstein itolkov

We should move jquery into its own standard spkg (and figure out how to merge the two different copies of it in sage in the process).  


---

Comment by jason created at 2008-10-10 04:32:34

I could only find one copy of jquery in Sage, in data/extcode/notebook/javascript/jquery.  Where is the other copy?


---

Comment by jason created at 2008-10-10 04:35:18

Okay, a jquery spkg (that's also been updated to the latest release, which has some really nice performance improvements), is here:

http://sage.math.washington.edu/home/jason/jquery-1.2.6.spkg


---

Attachment

Okay, apply the patch to the extcode repository, then install the spkg, and you should have an updated jquery.


---

Comment by jason created at 2008-10-10 04:38:55

itolkov, wstein, tabbot, or mabshoff, do you want to review this?


---

Comment by jason created at 2008-10-10 04:43:39

I just found the other copy of jquery; it's in the jqueryui folder.  jqueryui should also be an spkg...


---

Comment by jason created at 2008-10-10 05:55:31

Don't review this just yet; I'm fixing it so that it doesn't install in extcode.


---

Comment by jason created at 2008-10-10 23:52:29

Also, incorporate the jeditable and extendedclicks plugins, if the licenses allow.


---

Comment by jason created at 2008-10-18 04:02:42

Changing status from new to assigned.


---

Comment by jason created at 2008-10-18 04:02:42

Changing assignee from mabshoff to jason.


---

Comment by jason created at 2008-10-18 04:11:55

This is done at #4267.


---

Comment by jason created at 2008-10-18 04:12:29

Ignore any patches of spkgs here.  See #4267 instead.


---

Attachment

use instead of any previous patches


---

Comment by jason created at 2008-12-05 10:18:41

This depends on #4674.

Ignore any previous comments.  Apply jquery-and-friends-spkg.patch.  The spkgs are here:

http://sage.math.washington.edu/home/jason/notebook/jquery-1.2.6.spkg

http://sage.math.washington.edu/home/jason/notebook/jqueryui-1.6r807svn.spkg

Eventually, we need to also delete the obsolete directories in the extcode repository.


---

Comment by jason created at 2008-12-05 10:19:26

When this ticket is closed, close #4184.


---

Comment by jason created at 2008-12-05 10:39:33

Changing priority from minor to major.


---

Attachment

Apply tclemans  jquery-and-friends-spkg.2.patch patch instead of mine.


---

Comment by mabshoff created at 2009-01-19 06:31:19

Positive review due to #4705.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-19 08:06:40

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 08:06:40

Merged jquery-and-friends-spkg.2.patch, jquery-1.2.6.spkg and jqueryui-1.6r807svn.spkg in Sage 3.3.alpha0
