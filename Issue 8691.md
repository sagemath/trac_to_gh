# Issue 8691: Implement Plain Change algorithm in cython

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2010-04-15 06:19:19

Assignee: sage-combinat

CC:  rlm

The implementation is already done, I just need a ticket number.

My fix for #8655 will depend on this.


---

Attachment


---

Comment by boothby created at 2010-04-15 22:03:32

Changing status from new to needs_review.


---

Comment by hivert created at 2010-04-15 22:22:58

Hi Tom,

This looks very good ! Thanks for this. I've only one concerns: from the name, I would never guess what it does. I'm not sure to have a better name but I think we should ask for better proposal on the mailing lists.


---

Comment by hivert created at 2010-04-15 22:28:59

> This looks very good ! Thanks for this. I've only one concerns: from the name, I would never guess what it does. I'm not sure to have a better name but I think we should ask for better proposal on the mailing lists. 

Sorry for the double answer. Is you algorithm different from 
http://en.wikipedia.org/wiki/Steinhaus–Johnson–Trotter_algorithm
If not this is maybe a good name.


---

Comment by boothby created at 2010-04-16 20:31:42

Oops, turns out that freeing a call to `malloc(0)` is a bad idea.


---

Comment by boothby created at 2010-04-16 20:31:42

Changing status from needs_review to needs_work.


---

Comment by boothby created at 2010-04-28 22:05:59

replaces previous


---

Attachment


---

Comment by boothby created at 2010-04-28 22:06:18

Changing status from needs_work to needs_review.


---

Comment by boothby created at 2010-05-21 21:33:16

replaces all previous


---

Attachment

Updated version has changed the filename, and removed reference implementation because there's a better one in `sage/graphs/genus.pyx`.


---

Comment by rlm created at 2010-05-21 21:48:40

I think the usual convention here is to have Python functions that can test low-level C functions. It would also check input, etc...


---

Comment by boothby created at 2010-05-22 03:54:18

apply on top of v3


---

Comment by boothby created at 2010-05-22 03:55:58

Changing priority from major to minor.


---

Comment by boothby created at 2010-05-22 03:55:58

Changing type from defect to enhancement.


---

Attachment


---

Comment by rlm created at 2010-05-25 23:48:20

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-05-25 23:48:20

Looks good to me.


---

Comment by mhansen created at 2010-06-05 22:04:23

Resolution: fixed
