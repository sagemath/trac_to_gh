# Issue 674: Solaris 10: sympow is broken

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-17 00:36:38

Assignee: somebody

CC:  drkirkby

Keywords: Solaris 10, sympow


```
-bash-3.00$ sympow
sympow 1.018 RELEASE  (c) Mark Watkins -**ERROR** QD_check failed at x[1]
```



---

Comment by mabshoff created at 2009-01-15 06:48:50

I have a fixed Sympow build that passes doctests now on Solaris 10.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-15 06:48:50

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-15 06:48:50

Changing assignee from somebody to mabshoff.


---

Comment by mabshoff created at 2009-01-15 06:49:05

Changing component from packages to solaris.


---

Comment by kcrisman created at 2009-12-30 04:57:52

I'm cc:ing Dr. Kirkby on this since he is likely to have a way to test this easily.  Unfortunately, it seems this fix - whatever it was - was never integrated.


---

Comment by drkirkby created at 2009-12-30 15:01:46

If the subject lines is to believed, then this was Solaris 10 x86. I do not have such a system. I've got Open Solaris (Solaris 11) on x86 and Solaris 10 on SPARC. But I do not have any Solaris 10 x86 system. I could install Solaris 10 on a virtual machine, but I don't have it running just now and would rather concentrate on Solaris 11 (Open Solaris). 

I'm not getting any doctest failures with the name _sympow_ in them. I know nothing about this package, but I do not see anything obviously wrong on Solaris 10 SPARC. 


```
kirkby`@`t2:[~/sage-4.3] $ ./sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

Bypassing shell configuration files ...

/rootpool2/local/kirkby/sage-4.3
sage subshell$ sympow
sympow 1.018 RELEASE  (c) Mark Watkins --- see README and COPYING for details
```


There is a copy of Sage 4.3 at /rootpool2/local/kirkby/sage-4.3 on 't2'. If you are able to test that there, it would be helpful, but I do not see the obvious crash. But x86 could be a different matter of course. 

dave


---

Comment by mhansen created at 2010-08-26 20:35:34

Closed due to #9703


---

Comment by mhansen created at 2010-08-26 20:35:34

Resolution: duplicate


---

Comment by drkirkby created at 2010-08-26 21:14:29

Thank you for closing this Mike. It's nice to know I fixed a 3-year old bug!

Dave


---

Comment by mhansen created at 2010-08-26 21:15:34

:-)
