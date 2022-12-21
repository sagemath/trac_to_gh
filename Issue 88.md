# Issue 88: start writing "How To Make Pyrex FAST"

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-09-26 22:31:30

Assignee: dmharvey

I want to start writing a document on the wiki explaining various ways to make Pyrex code even faster than it already is. Each technique should have examples, including the generated C code and some timing experiments. We've started discovering quite a few things, and it would be helpful for new developers to be able to learn these techniques quickly.



---

Comment by dmharvey created at 2006-09-26 22:31:41

Changing type from defect to task.


---

Attachment

Here's a work in progress that is relevant...


---

Comment by dfdeshom created at 2007-03-12 05:54:01

I noticed that 
_ Wrapping C++ Code _ section in ` pyrex_guide.tex `  is empty. Lenard Lindstrom has a well-written post about writing C++ code in Pyrex that I've gone back to many times for clarity. The url is: http://lists.copyleft.no/pipermail/pyrex/2006-April/001704.html . Could it be included?


---

Comment by dmharvey created at 2007-09-28 04:05:16

Changing assignee from dmharvey to somebody.


---

Comment by malb created at 2008-02-26 23:58:23

Is this still a valid ticket? Certainly the tex is outdated. Also, this should be done over at the Cython project, shouldn't it?


---

Comment by dmharvey created at 2008-02-27 00:23:08

Yeah, I think since the Cython project now exists, this ticket should probably be marked invalid.


---

Comment by malb created at 2008-02-27 11:08:55

Resolution: invalid


---

Comment by malb created at 2008-02-27 11:08:55

So lets do it ... one ticket less to worry about :-)
