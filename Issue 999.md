# Issue 999: add optional sloccount script to sage-dist

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-10-25 16:37:13

Assignee: mabshoff

Keywords: sloccount sage-dist

sloccount measures the total numbers of lines in a project and estimates the time as well as amount of money needed to create the project. It also creates nice html output - for an example see

http://sage.math.washington.edu/home/mabshoff/2.8.9.rc1-sloccount.html

It would be nice to have an optional script that would automatically create the output for the whole sage project.

Cheers,

Michael


---

Comment by wdj created at 2007-10-25 16:51:30

To include the GAP code which is written in GAP, you need to count the lines in the *.gi files
as well. I don't know if you can exclude all lines beginning with a # or not (these would be
comments or documentation).


---

Comment by mabshoff created at 2007-10-25 17:55:12

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-03 02:18:58

Changing type from defect to enhancement.


---

Comment by jdemeyer created at 2013-06-13 12:27:05

I don't think we need such a thing...


---

Comment by jdemeyer created at 2013-06-13 12:27:05

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-06-13 12:27:11

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-06-19 12:21:29

Resolution: wontfix
