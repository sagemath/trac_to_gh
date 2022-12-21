# Issue 8566: Upate prereq to 0.8, removing 'm' option from 'tar'

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-03-20 11:00:49

Assignee: GeorgSWeber

As reported on sage-support:

http://groups.google.com/group/sage-support/msg/c636e1b5b820eb19

the 'm' option to tar used in prereq is causing a problem on a minimal linux system, as no such option is supported. The option seems to be unnecessary, as Sage seems to build fine without this option, which is only to 'touch' the files. I don't see this being necessary. 

I'll update the prereq script, to remove the option - a simple one-byte change. 



---

Attachment

prereq 0.8 tar file - unchanged from 0.7, except directory name


---

Attachment

prereq 0.8 script - removes 'm' option to 'tar'


---

Comment by dimpase created at 2011-05-06 16:22:50

this is dealt with in #11280


---

Comment by dimpase created at 2011-05-06 16:22:50

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2011-05-09 09:17:45

Resolution: duplicate
