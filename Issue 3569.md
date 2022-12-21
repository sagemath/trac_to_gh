# Issue 3569: optimize import of sage.dsage.interface.dsage_interface

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-06 20:13:04

Assignee: cwitty

BEFORE

```
teragon-2:misc was$ sage -startuptime|grep dsage_interface
        sage.dsage.interface.dsage_interface: 0.092 (dist_function)
         twisted.cred.credentials: 0.009 (sage.dsage.interface.dsage_interface)
         twisted.internet.threads: 0.011 (sage.dsage.interface.dsage_interface)
         twisted.internet.interfaces: 0.040 (sage.dsage.interface.dsage_interface)
0.092 sage.dsage.interface.dsage_interface (dist_function)
0.040 twisted.internet.interfaces (sage.dsage.interface.dsage_interface)
```


This is after using it multiple times (so caching).


---

Attachment

AFTER

```
teragon-2:dsage was$ sage -startuptime|grep twisted
```



```
teragon-2:dsage was$ sage -startuptime|grep dsage_interface
        sage.dsage.interface.dsage_interface: 0.007 (dist_function)
         sage.dsage.misc.misc: 0.005 (sage.dsage.interface.dsage_interface)
```



---

Comment by mhansen created at 2008-07-06 20:28:39

+1


---

Comment by mabshoff created at 2008-07-07 02:38:12

Resolution: fixed


---

Comment by mabshoff created at 2008-07-07 02:38:12

Merged in Sage 3.0.4.alpha2
