# Issue 2886: change an error message

Issue created by migration from https://trac.sagemath.org/ticket/2886

Original creator: was

Original creation time: 2008-04-12 00:09:35

Assignee: was

When you crash Sage you get this error message:

```
**********************************************************************

Oops, SAGE crashed. We do our best to make it stable, but...

A crash report was automatically generated with the following information:
  - A verbatim copy of the crash traceback.
  - A copy of your input history during this session.
  - Data on your current SAGE configuration.

It was left in the file named:
	'/Users/was/.sage/ipython/SAGE_crash_report.txt'
If you can email this file to the developers, the information in it will help
them in understanding and correcting the problem.

You can mail it to: William Stein at wstein@gmail.com
with the subject 'SAGE Crash Report'.

If you want to do it now, the following command will work (under Unix):
mail -s 'SAGE Crash Report' wstein@gmail.com < /Users/was/.sage/ipython/SAGE_crash_report.txt

To ensure accurate tracking of this issue, please file a report about it at:
http://www.sagemath.org:9002/sage_trac

```


Issues: 
  (1) People need accounts to file a report.  It might be much better to tell people to report to sage-support.

  (2) the url for trac is now trac.sagemath.org/sage_trac

--

I think doing (2) would be fine to fix this ticket.

William


---

Attachment


---

Comment by mhansen created at 2008-04-12 07:45:54

Changing status from new to assigned.


---

Comment by mhansen created at 2008-04-12 07:45:54

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-04-12 07:45:54

The patch applies to hg_scripts.


---

Comment by ncalexan created at 2008-04-15 16:36:05

Fine by me.


---

Comment by mabshoff created at 2008-04-15 20:01:17

Merged in Sage 3.0.alpha6


---

Comment by mabshoff created at 2008-04-15 20:01:17

Resolution: fixed
