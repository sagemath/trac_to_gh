# Issue 5801: Delete sage/server/notebook/{test.txt|todo.txt} and move their content to documentation trac

Issue created by migration from https://trac.sagemath.org/ticket/5801

Original creator: mabshoff

Original creation time: 2009-04-16 06:14:35

Assignee: cwitty

CC:  was mhansen

While looking around for something else I noticed test.txt and todo.txt. Both are surprisingly related to notebook development. Both files should be looked at and dealt with since they do not belong inside the tree. 

 * test.txt can probably be removed since we have a webtesting framework written by Mike Hansen
 * todo.txt should be looked over and the issues in there that aren't in trac yet should have tickets opened. Then the file should be removed.

Cheers,

Michael


---

Comment by timdumol created at 2010-01-18 04:41:49

This works now, apparently. Confirm and close?


---

Comment by aapitzsch created at 2014-05-01 08:17:19

Files no longer exist. So let's close this.


---

Comment by aapitzsch created at 2014-05-01 08:17:19

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-05-01 08:50:49

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-05-01 10:25:00

Resolution: fixed
