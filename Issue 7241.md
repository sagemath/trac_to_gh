# Issue 7241: sage -upgrade will try to redownload spkg's that are already present

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-10-18 17:41:26

Assignee: tbd

Keywords: upgrade

This causes a problem with flaky internet connections since all of the spkgs have to be able to be downloaded all successfully one right after the other.  It shouldn't try to redownload files that are already present.


---

Comment by mhansen created at 2009-10-18 17:44:06

Changing status from new to needs_review.


---

Attachment

It would also be nice to have it use a more robust downloader such as cURL or wget if it is present.  The current one doesn't resume downloads.


---

Attachment


---

Comment by hivert created at 2009-11-07 08:58:36

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2009-11-07 08:58:36

For some reason the patch needed a little rebase. I just uploaded a rebased patch which is ready to go. => positive review. 

Cheers,

Florent


---

Comment by mhansen created at 2009-11-07 11:58:16

Resolution: fixed
