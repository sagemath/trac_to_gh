# Issue 4131: [with patch, needs review] unbreak sage-clone

Issue created by migration from https://trac.sagemath.org/ticket/4131

Original creator: mabshoff

Original creation time: 2008-09-16 01:37:36

Assignee: mabshoff

Some bash code snuck into the python script sage-clone. This patch fixes it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-16 01:38:31

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2008-09-16 01:40:42

Oops. :-)


---

Comment by wdj created at 2008-09-16 01:54:55

I'm confused:


```
wdj@hera:~/sagefiles/sage-3.1.2.rc4$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.2.rc4, Release Date: 2008-09-15                   |
| Type notebook() for the GUI, and license() for information.        |
sage: hg_sage.apply("/home/wdj/sagefiles/trac_4131.patch")
cd "/home/wdj/sagefiles/sage-3.1.2.rc4/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.2.rc4/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.2.rc4/devel/sage" && hg import   "/home/wdj/sagefiles/trac_4131.patch"
applying /home/wdj/sagefiles/trac_4131.patch
unable to find 'sage-clone' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage-clone.rej
abort: patch failed to apply
sage:                                                
```


I see sage-clone in /home/wdj/sagefiles/sage-3.1.2.rc4/local/bin,
so what the heck is going on?


---

Comment by mhansen created at 2008-09-16 01:55:53

You use hg_scripts.apply() to apply this patch.


---

Comment by wdj created at 2008-09-16 01:57:42

Thanks. Applied fine now and sage -clone is working:-)


---

Comment by mabshoff created at 2008-09-16 03:46:54

Resolution: fixed


---

Comment by mabshoff created at 2008-09-16 03:46:54

Merged in Sage 3.1.2.rc5
