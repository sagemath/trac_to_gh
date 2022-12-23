# Issue 2193: doctest framework should check for keywords only in comments

Issue created by migration from https://trac.sagemath.org/ticket/2193

Original creator: burcin

Original creation time: 2008-02-17 14:19:35

Assignee: burcin

CC:  ncalexan

Checking for keywords on the whole line causes unexpected behavior while testing. The test framework should only check for the keywords in the comments.

This thread is also relevant:

http://groups.google.com/group/sage-devel/browse_thread/thread/c63998dbd4ee6a27/fc6643a2a871bf34#fc6643a2a871bf34


---

Comment by burcin created at 2008-02-17 16:30:03

make sage-doctest search for keywords in comments


---

Attachment

add random keyword to tests in doc-main


---

Attachment

add random keyword to comments


---

Attachment

attachment:2193-doctest_keywords_in_comments.patch changes the `sage-doctest` script to search for keywords only in comments. It also changes the way random keyword is handled to match wstein's suggestions in the sage-devel thread mentioned above.

attachment:2193-doc_add_random.patch and attachment:2193-add_random_keyword.patch add the random keyword to comments for tests which relied on the old behavior in the documentation, and the sage library respectively.


---

Comment by ncalexan created at 2008-02-18 19:31:24

Looks fine to me.  I say apply.


---

Comment by mabshoff created at 2008-02-18 19:37:06

Resolution: fixed


---

Comment by mabshoff created at 2008-02-18 19:37:06

Merged in Sage 2.10.2.alpha1
