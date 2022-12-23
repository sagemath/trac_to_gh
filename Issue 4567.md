# Issue 4567: Create Sage 3.2 release notes

Issue created by migration from https://trac.sagemath.org/ticket/4567

Original creator: mabshoff

Original creation time: 2008-11-20 18:51:10

Assignee: mabshoff

As the subject says.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-20 18:51:19

Changing status from new to assigned.


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment

trivial typos and consistency issues


---

Comment by mvngu created at 2008-11-29 09:09:01

The patch *Sage-3.2-release-notes-draft2.patch* fixes some trivial typos and consistency issues in the second draft of the release note for sage-3.2. It should be applied on top of *Sage-3.2-release-notes-draft2.txt*.


---

Comment by mvngu created at 2008-11-29 10:08:17

The file *Sage-3.1.4-release-notes-draft2.txt* claims that Sage 3.1.4 was released on 2008-10-16, which is indeed the case from the "Last modified" field at this [directory listing](http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.4/). But note that at this [download page](http://www.sagemath.org/download-source.html), the row for release 294 (i.e. sage-3.1.4.tar) says that the particular source tarball was released on 2008-10-20. This inconsistency in release date for sage-3.1.4 has caused me some problem in the past. In particular, please refer to [this comment](http://trac.sagemath.org/sage_trac/ticket/1389#comment:24). Now, is it correct to change the release date for sage-3.1.4 from 2008-10-16 to 2008-10-20?


---

Comment by mvngu created at 2008-11-29 10:16:26

fixed trivial typos and consistency issues


---

Attachment

The patch *Sage-3.1.4-release-notes-draft2.patch* fixes some trivial typos and consistency issues in the file *Sage-3.1.4-release-notes-draft2.txt*.


---

Comment by mabshoff created at 2008-11-29 10:19:11

Replying to [comment:3 mvngu]:
> The file *Sage-3.1.4-release-notes-draft2.txt* claims that Sage 3.1.4 was released on 2008-10-16, which is indeed the case from the "Last modified" field at this [directory listing](http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.4/). But note that at this [download page](http://www.sagemath.org/download-source.html), the row for release 294 (i.e. sage-3.1.4.tar) says that the particular source tarball was released on 2008-10-20. This inconsistency in release date for sage-3.1.4 has caused me some problem in the past. In particular, please refer to [this comment](http://trac.sagemath.org/sage_trac/ticket/1389#comment:24). Now, is it correct to change the release date for sage-3.1.4 from 2008-10-16 to 2008-10-20?

Hi Minh,


I use the trac date when a milestone was closed, but I guess the official time stamp of the release tarball at sagemath.org would be better. We should just make sure that it is consistent in the future.

Cheers,

Michal


---

Comment by mvngu created at 2008-11-29 10:32:22

trivial typos and consistency issues


---

Attachment

The patch *Sage-3.1.3-release-notes-draft2.patch* fixes some trivial typos and consistency issues in the release note *Sage-3.1.3-release-notes-draft2.txt*.


---

Comment by mabshoff created at 2008-11-30 05:53:59

Thanks Minh,

positive review on all three patches.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-30 05:57:57

Final Sage 3.2 release notes


---

Attachment

Final Sage 3.1.4 release notes


---

Attachment

Final Sage 3.1.3 release notes


---

Comment by mabshoff created at 2008-11-30 06:01:21

Resolution: fixed


---

Comment by mabshoff created at 2008-11-30 06:01:21

Merged in Sage 3.2. Thanks Minh.

Cheers,

Michael
