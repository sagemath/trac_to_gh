# Issue 4590: sage/interfaces/phc.py writes tmp files into cwd

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-23 04:16:14

Assignee: mhampton

From _output_from_command_list:

```
        EXAMPLES:
            sage: from sage.interfaces.phc import *  #optional
            sage: R2.<x,y> = PolynomialRing(QQ,2)    #optional
            sage: start_sys = [(x-1)^2+(y-1)-1, x^2+y^2-1]  #optional
            sage: a = phc._output_from_command_list(['phc -m','4','n','n','n'], start_sys)#optional
            sage: os.unlink(a)#optional
```

The Sage library might not be writable for the user who is running doctests, so the above doctest needs to be fixed.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2009-01-21 21:19:16

Actually, the only files that get used in that function are these:


```
        input_filename = sage.misc.misc.tmp_filename()
        output_filename = sage.misc.misc.tmp_filename()
```


The doctest may have been a little misleading.  The reviewer can decide if the patch should go in or the ticket should be marked as invalid.


---

Comment by mhansen created at 2009-01-21 21:19:16

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-21 21:19:16

Changing assignee from mhampton to mhansen.


---

Comment by jason created at 2009-01-22 15:23:31

Either way is fine with me.  Looking at the code, it seems that mhansen is right.  I'd probably go with the patch so things are less confusing.


---

Comment by mabshoff created at 2009-01-23 02:35:37

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 02:35:37

Merged in Sage 3.3.alpha1
