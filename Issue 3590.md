# Issue 3590: dage_interfaces -- port detection code hangs solid

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-07 20:42:55

Assignee: yi


```
sage -t  devel/sage/sage/dsage/interface/dsage_interface.py *** ***
Error: TIMED OUT! *** ***
[DSage] Closed connection to localhost
[DSage] Closed connection to localhost
[DSage] Closed connection to localhost
[DSage] Closed connection to localhost
*** *** Error: TIMED OUT! *** ***
        [2697.3 s]
```


This is at

```
port = find_open_port().next()
```


This happens on *some machines*, e.g., fermat.math.harvard.edu, but not others.




---

Attachment


---

Attachment


---

Comment by ncalexan created at 2008-07-08 00:19:47

It's better than the existing code :)


---

Comment by was created at 2008-07-08 00:20:31

Resolution: fixed
