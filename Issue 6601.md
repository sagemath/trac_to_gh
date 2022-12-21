# Issue 6601: Crash loading rings.polynomial.pbori

Issue created by migration from Trac.

Original creator: stankewicz

Original creation time: 2009-07-23 12:14:56

Assignee: tbd

I tried to run a script and python crashed trying to load pbori. Sage_crash_report.txt is attached.


---

Attachment

It looks like you're using Sage 3.4.1. Would it be possible to try your script with a more recent version of Sage (like 4.1, the most recent as of now) and see whether you still get an error?


---

Comment by burcin created at 2010-01-16 23:30:42

Importing individual modules without initializing sage by doing `import sage.all` is not supported. You should add a line with


```
import sage.all
```


at the beginning of your script.


---

Comment by burcin created at 2010-01-16 23:30:42

Resolution: invalid
