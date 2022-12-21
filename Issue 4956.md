# Issue 4956: html accents in the notebook aren't saved properly on second load

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-08 20:32:42

Assignee: boothby

CC:  was mhansen

Reported in http://groups.google.com/group/sage-support/browse_thread/thread/60a863def66c05a1

```
This works 
html(r'Donde $\Sigma$ es la sumatoria de los n&uacute;meros... etc.' ) 
but only works the first time. If you save & quit your work, after 
trying again it fails. This is because when saving it converts 
"n&uacute;meros" to "números". 
```


Note that this issue might be closely related to some other notebook tickets.

Cheers,

Michael


---

Comment by jason created at 2009-05-30 07:17:31

mhansen says this is fixed at #5564.


---

Comment by mvngu created at 2009-08-26 19:59:21

Ticket #5564 has been closed because it addresses many issues. The issues it addresses are also considered by other tickets. If anyone is working on this ticket, please refer to #5564 for code and inspiration.


---

Comment by timdumol created at 2009-11-15 12:05:48

This works for me now, since the output files now have the magic utf-8 comment. Please close this.


---

Comment by mhansen created at 2009-11-15 13:47:16

Resolution: invalid
