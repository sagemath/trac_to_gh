# Issue 7821: readline-6.0.p1 fails on FreeBSD

Issue created by migration from https://trac.sagemath.org/ticket/7821

Original creator: pjeremy

Original creation time: 2010-01-03 00:53:06

Assignee: pjeremy

readline-6.0.p1/spkg-install contains a typo in some FreeBSD-specific code, leading to the following error:

```
...
/bin/sh ../support/shlib-install -O freebsd8.0 -d /home/peter/sage/sage-4.3/local/lib -b /home/peter/sage/sage-4.3/local/bin -i "/usr/bin/install -c -m 644" libreadline.so.6.0
install: you may need to run ldconfig
make[1]: Leaving directory `/home/peter/sage/sage-4.3/spkg/build/readline-6.0.p1/src/shlib'
ln: SAGE_LOCAL/lib/libreadline.so: No such file or directory
```


The affected code is no longer required with readline-6.0 so delete it.

FreeBSD 3.x and later default to ELF, rather then a.out. A utility objformat(1) was temporarily introduced to enable third-party applications to determine te object format. This has now been deleted and code should assume ELF format if it does not exist. Explicitly linking libreadline against libtermcap is necessary to ensure that dependencies are picked up.


---

Attachment


---

Comment by pjeremy created at 2010-01-03 01:57:47

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-06-22 22:18:33

This looks good to me.  I've made an spkg out of the changes at http://sage.math.washington.edu/home/mhansen/readline-6.0.p2.spkg


---

Comment by mhansen created at 2010-06-22 22:18:33

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-25 15:43:43

Resolution: fixed


---

Comment by leif created at 2011-10-28 11:38:37

For the record:

The proper fix (btw. also for a couple of other systems, like Arch Linux, OpenSuSE and meanwhile also Ubuntu 11.10 I think) is to add `$(TERMCAP_LIB)` to the link command of `libreadline.so` in `src/shlib/Makefile.in`, rather than setting `SHLIB_LIBS='-ltermcap'`.  This is more generic, since readline's `configure` determines what the proper `libtermcap` (or its replacement) is.  No need to special-case on the platform (operating system / distro).
