# Issue 9513: Sage 4.4.4 build fails due to mixing prefix/home

Issue created by migration from https://trac.sagemath.org/ticket/9513

Original creator: PolyBoRi

Original creation time: 2010-07-15 21:06:03

Assignee: AlexGhitza

On my System (SuSE 11.1 x86_64). The build fails and complains about mixing --prefix and --home when doing `python install` on various packages: 
networkx, mercurial (perhaps more to come))
In addition in the spkg of scons --prefix is missing completely.


---

Comment by davidloeffler created at 2010-07-29 13:09:35

Changing component from algebra to build.


---

Comment by davidloeffler created at 2010-07-29 13:09:35

This has very little to do with algebra -- please use appropriate values for "component" when creating tickets.


---

Comment by davidloeffler created at 2010-07-29 13:09:35

Changing assignee from AlexGhitza to GeorgSWeber.


---

Comment by AlexanderDreyer created at 2010-07-29 14:02:40

Hello,
I think this is just the same as #9536. Its Fix also cures this problem.

Regards,
  Alexander


---

Comment by AlexanderDreyer created at 2010-08-19 06:47:51

See #9536.


---

Comment by AlexanderDreyer created at 2010-08-19 06:47:51

Resolution: duplicate
