# Issue 3727: bug report link in notebook for quick submitting

Issue created by migration from https://trac.sagemath.org/ticket/3727

Original creator: schilly

Original creation time: 2008-07-25 22:14:57

Assignee: boothby

I created a google spreadsheet form to collect bugs far more easier than registering at a mailing list and so on. In order to make this happen:

 1. [proofread my form](http://spreadsheets.google.com/viewform?key=pCwvGVwSMxTzT6E2xNdo5fA)
 1. include a (red?) "Bug Report" link in the top right corner of the notebook pointing to this website:

```
<a href="http://spreadsheets.google.com/viewform?key=pCwvGVwSMxTzT6E2xNdo5fA" target="_blank"><span stype="font-color: red;">Bug Report</span></a>
```


I'll check the data, report bugs on sage-devel or just directly in trac if there is no discussion necessary.

If somebody wants to help me, request a shared access at harald.schilly`@`gmail.com and delete a row after you have processed it.


---

Comment by schilly created at 2008-07-25 22:15:48

Changing type from defect to enhancement.


---

Comment by schilly created at 2008-07-26 16:06:57

an additional place to include that link would be at the end of a stack trace output. so, that there is an active call for submitting this particlar problem.

including the stack trace automatically is not possible, but i added an additional input field for stack traces.


---

Attachment

duplicating functionality of help() to bugreport() in javascript, updated


---

Comment by TimothyClemans created at 2008-08-05 18:51:10

Note: there is a script for applying the various Notebook patches. The base is sage-3.0.6.

http://sage.math.washington.edu/home/tclemans/uw_contract_work/apply_patches.sage


---

Comment by mabshoff created at 2008-08-09 23:26:51

Resolution: fixed


---

Comment by mabshoff created at 2008-08-09 23:26:51

Merged in Sage 3.1.alpha1
