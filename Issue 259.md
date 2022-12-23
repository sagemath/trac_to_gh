# Issue 259: axiom bug

Issue created by migration from https://trac.sagemath.org/ticket/259

Original creator: was

Original creation time: 2007-02-11 23:01:58

Assignee: was


```
In sage-2.0 and sage-2.1.0.1 the first Axiom command that I enter
hangs the sage process but if I hit control-c and re-enter the
command, it works as it used to work. This also affects Axiom
commands entered via the notebook.
 
  sage: axiom('1+1')
  ... waits indefinitely ...
  ^C
  ...
  sage: axiom('1+1')
 
     2
 
  sage:
 
---------------
 
I will take a look at the axiom inteface code when I get time
but perhaps someone already knows what might have changed in
the way the interface works?
 
BTW, I am using the axiom4sage-0.1 download from sage.math but
I had a problem with the simple
 
  sage -I axiom4sage-0.1.spkg
 
command. I apparently received only a partial download and the
install failed. Later, I downloaded axiom4sage-0.1.spkg directly
to the sage root directory and repeated the command:
 
  sage -I axiom4sage-0.1.spkg
 
Then Axiom was built and installed as expected on my OpenSuSE 10.2
x86 linux system.
 
Regards,
Bill Page.
```



---

Comment by was created at 2007-08-18 09:50:41

axiom is in too much flux right now.


---

Comment by mabshoff created at 2007-09-10 02:33:25

Can somebody test if this is still the case? The bug report is rather stale and the current optional axiom4sage.spkg is around version number 0.3.

Cheers,

Michael


---

Comment by cwitty created at 2007-10-20 22:37:26

Resolution: worksforme


---

Comment by cwitty created at 2007-10-20 22:37:26

In sage 2.8.7.2 with axiom4sage 0.3.1, this works for me on 32-bit and 64-bit x86 linux.
