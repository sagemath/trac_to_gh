# Issue 5780: [with patch; needs review] plotting -- deal with NaN's in plot range

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-13 20:13:41

Assignee: was




---

Attachment

I like this patch, but there is a slight doctesting issue:

```
bash-3.00$ ./sage -t -long devel/sage/sage/coding/code_bounds.py
sage -t -long "devel/sage/sage/coding/code_bounds.py"       
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc2/sage-3.4.1.rc2-fulvia-gcc-4.3.3/devel/sage/sage/coding/code_bounds.py", line 383:
    sage: plot(f,0,1)
Expected nothing
Got:
    verbose 0 (1365: plot.py, get_minmax_data) ymin was NaN (setting to 0)
    verbose 0 (1365: plot.py, get_minmax_data) ymax was NaN (setting to 0)
    <BLANKLINE>
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc2/sage-3.4.1.rc2-fulvia-gcc-4.3.3/devel/sage/sage/coding/code_bounds.py", line 395:
    sage: plot(f,0,1)
Expected nothing
Got:
    verbose 0 (1365: plot.py, get_minmax_data) ymin was NaN (setting to 0)
    verbose 0 (1365: plot.py, get_minmax_data) ymax was NaN (setting to 0)
    <BLANKLINE>
**********************************************************************
```

This is on Solaris and #5779 which RobertWB should have a patch for tonight might then fix the problem. 

Another possibility would be to set verbosity to -1 for this particular doctest, but I would like to avoid that. Positive review for the fix, but I will wait to change the subject once we have dealt with the verbosity.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-15 23:18:08

Looks good to me. There is another problem unrelated to this in this area of the plotting code, but that is another ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-15 23:18:35

Resolution: fixed


---

Comment by mabshoff created at 2009-04-15 23:18:35

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
