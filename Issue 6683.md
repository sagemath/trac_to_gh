# Issue 6683: notebook worksheet rating_info link leads to error page

Issue created by migration from https://trac.sagemath.org/ticket/6683

Original creator: khorton

Original creation time: 2009-08-07 09:29:50

Assignee: wstein

Keywords: notebook worksheet rating_info error

Clicking on a rating_info link in a  list of notebook worksheets produces a blank page titled "Error | Sage Notebook".

Diagnosis and suggested solution found in this [thread](http://groups.google.com/group/sage-support/browse_frm/thread/4d2524b7ae5dd26c#) on sage-support.


---

Attachment

Delete message in Worksheet_rating_info and Worksheet_rate class from Sage 4.1 original source file server/notebook/twist.py


---

Comment by NoSyu created at 2009-08-07 21:37:59

In the Worksheet_rating_info and Worksheet_rate class in _server/notebook/twist.py_, it return the HTMLResponse that argument is stream and all return stream use message function. But message function in _twist.py_ is used for error page to use _error_message.html_ templete file. Unless the return is not error page, it use message function. So it always show the error page titled "Error | Sage Notebook".


---

Comment by timdumol created at 2010-01-19 16:12:24

This has already been fixed in #7786.


---

Comment by timdumol created at 2010-01-19 16:12:24

Resolution: duplicate
