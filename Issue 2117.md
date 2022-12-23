# Issue 2117: problems with "...?starup_token=..." URL in notebook

Issue created by migration from https://trac.sagemath.org/ticket/2117

Original creator: nbruin

Original creation time: 2008-02-08 18:47:44

Assignee: boothby

The following sequence of events leads to a "Internal Server Error" page:

 * Start up sage to serve a local notebook (sage -notebook)
[Browser pops up with "admin" already logged in, using a "startup_token" url]
 * select some worksheets
 * click "archive"

The notebook seems to be in a sane condition afterwards. If I change the URL to "https://localhost:8001/" (i.e., remove the "?startup_token=..." part) everything seems as it should be. I guess the notebook barfs at this stage on the "?" part in the URL?




---

Comment by mhansen created at 2009-01-23 13:22:29

As we don't get the URL at the beginning with the startup token, I'm going to mark this as invalid.  I can't reproduce it in 3.2.3.


---

Comment by mhansen created at 2009-01-23 13:22:29

Resolution: invalid


---

Comment by mabshoff created at 2009-01-23 16:25:59

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-01-23 16:25:59

This came up last week on sage-edu with Sage 3.2.3, so there is certainly a bug to be found and fixed here. It was reproducible with a wiped .sage by someone who seemed technically competent enough not to make a dumb mistake. So I am reopening this.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 16:25:59

Resolution changed from invalid to 


---

Comment by mhansen created at 2009-01-24 01:50:51

This thread ( http://groups.google.com/group/sage-edu/browse_thread/thread/4565115a21b28f5d/9e75206e7fada15b?lnk=gst&q=internal+server+error#9e75206e7fada15b ) is a different issue than the one reported here.


---

Comment by mhansen created at 2009-01-24 01:50:51

Resolution: invalid
