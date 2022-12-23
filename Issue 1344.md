# Issue 1344: make it crystal clear that one should use tar not some .app to extract sage

Issue created by migration from https://trac.sagemath.org/ticket/1344

Original creator: was

Original creation time: 2007-11-30 18:47:25

Assignee: tba


```
I have now successfully started SAGE. My problem was using "The
Unarchiver" to open the compressed file. (The Unarchiver.app is
available at http://www.apple.com/downloads/macosx/system_disk_utilities/theunarchiver.html.)
When I used the standard shell tools gunzip and tar to install SAGE,
everything worked fine. I assume this has been the problem all along.
This might be worth a warning to other Mac users.

Thanks, Max
```




---

Comment by malb created at 2008-01-06 13:25:33

Possibly invalid because of the switch to DMGs?


---

Comment by mabshoff created at 2008-01-20 03:06:47

malb is right. Since we switched to DMGs this issue is wontfix.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-20 03:06:47

Resolution: wontfix
