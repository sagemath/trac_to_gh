# Issue 7610: `readline-6.0` causes "undefined symbol: PC" errors on Arch Linux

Issue created by migration from https://trac.sagemath.org/ticket/7610

Original creator: timdumol

Original creation time: 2009-12-06 02:43:36

Assignee: tbd

CC:  drkirkby alexghitza

On running Sage or the next build, readline fails with:


```
bash: symbol lookup error: /opt/sage-bin/local/lib/libreadline.so.6: undefined symbol: PC
```



---

Attachment

Adds Arch Linux workaround (copies over system library)


---

Comment by timdumol created at 2009-12-06 02:54:47

Changing status from new to needs_review.


---

Comment by timdumol created at 2009-12-06 02:54:47

This patch adds the standard workaround (copying over the system package to $SAGE_LOCAL/lib). This should not ever fail since `readline` is in the `base` repository, and so should be installed in all systems.

Originally I thought it was because readline linked to termcap, which is disabled in Arch, but linking to curses did not help.


---

Comment by timdumol created at 2009-12-06 02:55:36

I've also added double quotes around almost all variable references (otherwise, there will be issues if there are spaces in the path to $SAGE_LOCAL, etc.)


---

Comment by mhansen created at 2009-12-09 02:34:20

I've merge http://sage.math.washington.edu/home/mhansen/readline-6.0.p1.spkg which has these changes applied on top of the ones at #7164.


---

Comment by mhansen created at 2009-12-09 02:34:20

Resolution: fixed


---

Comment by leif created at 2011-10-29 22:55:36

Replying to [ticket:7610 timdumol]:
> On running Sage or the next build, readline fails with:
> 

```
bash: symbol lookup error: /opt/sage-bin/local/lib/libreadline.so.6: undefined symbol: PC
```


This is because our shared libreadline lacks a `DT_NEEDED` tag for libtermcap, libncurses, libtinfo or whichever library provides these symbols (depends on the OS / distro).

I have a readline 6.2.p2 spkg which fixes this, but haven't yet opened a ticket for it...

(Just in case someone searches for this error and ends up here.)
