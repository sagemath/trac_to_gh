# Issue 9860: Improving the Graph Theory table of contents

Issue created by migration from https://trac.sagemath.org/ticket/9861

Original creator: ncohen

Original creation time: 2010-09-06 17:34:24

Assignee: mvngu

CC:  rlm mvngu

The table of contents of the Graph Theory module is a bit hard to parse at the moment [1]. The file graph.py is even entitled "Graph Theory" itself, which must have remained from before this file was split into three, and the depth of 2 does not really help.

This patch is a possible way to clean it and make it.... readable ! I don't expect this patch to be merged as it is, as you probably have a different view of how it should be.. `:-)`

Nathann

[1] http://www.sagemath.org/doc/reference/graphs.html


---

Attachment


---

Attachment


---

Comment by mvngu created at 2010-09-07 09:21:28

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-09-07 09:21:28

I got these warnings after applying ncohen's patch to Sage 4.5.3.rc0:


```
/dev/shm/mvngu/sage-4.5.3/devel/sage/doc/en/reference/graphs.rst:36: (WARNING/2)
 Title underline too short.

Libraries of algorithms
--------------------
/dev/shm/mvngu/sage-4.5.3/devel/sage/doc/en/reference/graphs.rst:36: (WARNING/2)
 Title underline too short.

Libraries of algorithms
--------------------
```


These are fixed in my reviewer patch. The reviewer patch also adds some consistency to how module headings are named, and consistency on how to space headings in the index file graph.rst. Capitalized titles are more difficult to read than a title only whose first letter is capitalized. I have avoided capitalized titles. 



I like ncohen's re-organized table of content for graph theory. Now it's just a matter of someone checking my reviewer patch. If it gets a positive review, then the whole ticket is good to go.


---

Comment by ncohen created at 2010-09-07 10:31:32

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-09-07 10:31:32

Great ! Thank you again for your help ! `:-)`

Nathann


---

Comment by mpatel created at 2010-09-15 11:38:22

Resolution: fixed
