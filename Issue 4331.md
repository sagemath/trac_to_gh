# Issue 4331: sage-vmware image - add keyboard reconfigure option

Issue created by migration from https://trac.sagemath.org/ticket/4331

Original creator: was

Original creation time: 2008-10-20 16:26:21

Assignee: mabshoff

CC:  slelievre

Change the sage vmware image so there is another login option:


```
login: keyboard
```


This would run `dpkg-reconfigure console-setup`
as suggested by Martin Rubey in email:

```
>
> Sorry, I meant, of all the things you tried was
> just typing
>
>    dpkg-reconfigure console-setup
>
> the one and only thing you did, and that it worked?

Nearly: you will then be asked some simple questions which are obvious to
answer if you do not have an english keyboard.

-- Martin Rubey
```



---

Comment by mkoeppe created at 2021-08-26 02:16:22

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2021-08-26 02:16:22

outdated, should close


---

Comment by slelievre created at 2021-08-26 22:22:30

Changing status from needs_review to positive_review.


---

Comment by slelievre created at 2021-08-26 22:22:30

There seems to be no plan to resume producing
the vmware image at each Sage release.

Its main use was arguably to work around
the lack of a version of Sage for Windows.

That use case largely fell with Erik Bray's
Cygwin-based Sage installer for 64-bit Windows.

The Sage Debian Live distribution also
provides a versatile portable solution.

In view of that, ok to close this.


---

Comment by chapoton created at 2021-09-01 07:08:45

Resolution: invalid
