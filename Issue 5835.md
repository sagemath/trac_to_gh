# Issue 5835: deleting a file from the DATA directory gives an error page

Issue created by migration from https://trac.sagemath.org/ticket/5835

Original creator: jason

Original creation time: 2009-04-20 17:09:44

Assignee: boothby

CC:  was

Steps to reproduce:

 * Upload a file to a worksheet using the Data... menu
 * Click on the filename in the Data... menu
 * Click the link to delete the file.

My guess is that it deletes the file, but then tries to display it.  Instead, it should either go back to the worksheet view or to some list of all files in the DATA directory.


---

Comment by timdumol created at 2010-01-18 04:38:24

This has been fixed. Confirm and chekc please?


---

Comment by timdumol created at 2010-01-19 03:11:32

Works with sagenb-0.6


---

Comment by timdumol created at 2010-01-19 03:11:32

Resolution: duplicate


---

Comment by timdumol created at 2010-01-19 03:37:06

Resolution changed from duplicate to fixed
