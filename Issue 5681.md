# Issue 5681: [with patch; needs review] notebook -- worksheets open in new page/tab

Issue created by migration from https://trac.sagemath.org/ticket/5681

Original creator: was

Original creation time: 2009-04-04 07:09:46

Assignee: boothby

I'm so so so SICK (!) of accidentally hitting the back button and corrupting my worksheet.  It happens to me and everybody constantly. It's horrible and confusing.  The attached trivial 1-line patch makes it so when open a worksheet it appears in a new tab (or windows), hence there is *no history*, hence nothing to accidentally go back to.



---

Attachment


```
YYY   YYY  EEEEEEEEE    SSSSSS   !!!  !!!
 YYY YYY   EEE         SSS  SSS  !!!  !!!
  YYYYY    EEE        SSS        !!!  !!!
   YYY     EEEEEEEEE   SSSSSSS   !!!  !!!
   YYY     EEE              SSS  
   YYY     EEE        SSS  SSS   !!!  !!!
   YYY     EEEEEEEEE   SSSSSS    !!!  !!!
```



---

Comment by mabshoff created at 2009-04-05 01:35:07

Resolution: fixed


---

Comment by mabshoff created at 2009-04-05 01:35:07

Merged in Sage 3.4.1.rc0.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-04-08 22:53:17

See #5720 for a related ticket and a comment about the current state of affairs.
