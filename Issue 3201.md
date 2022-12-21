# Issue 3201: notebook -- bug in parsing \ at end of line in %latex mode

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-14 01:18:07

Assignee: boothby


```

A subtle problem with "%latex" cells is illustrated at
<http://www-maths.swan.ac.uk/staff/fwc/sage-notebook-latex.tiff>

When "\\" occurs at the end of a line it seems to gooble the first
character in the next line.

I'm using Mac OS X 10.4.11, and the same thing happens both Firefox
and Safari.

Francis
```



---

Comment by was created at 2008-05-14 01:18:54

I can confirm that this sort of bug is very likely to happen.  I think \ parsing
gets done before the code gets sent to latex.eval or something like that.  It's an
interesting bug, and definitely something that needs to get fixed.


---

Comment by mhansen created at 2009-01-19 22:58:00

This is caused by the line


```
        I = I.replace('\\\n','')
```


in worksheet.py.  This should be cleaner to fix after some other changes I have planned.  This is here just as a reminder to me.


---

Comment by mhansen created at 2009-01-19 22:58:00

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2009-01-19 22:58:00

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2009-01-22 14:46:20

Note that this patch depends on #5050.


---

Comment by jason created at 2009-01-22 16:45:41

The patch works for me.  Where is the doctest?


---

Comment by mhansen created at 2009-01-24 04:53:57

I don't know a good way to add a doctest.  I've added a test to Selenium test suite.


---

Comment by mabshoff created at 2009-01-28 14:35:49

Positive review even though this skirts the doctesting rule.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 15:18:49

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 15:18:49

Merged in Sage 3.3.alpha3.

Cheers,

Michael
