# Issue 5517: cvxopt-0.9.p7: build failure due to missing perl modules

Issue created by migration from Trac.

Original creator: tornaria

Original creation time: 2009-03-14 16:08:06

Assignee: mabshoff

The error reported by `cvxopt-0.9.p7` is:

```
Can't locate File/Copy.pm in `@`INC (`@`INC contains: /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ./spkg-install line 2.
BEGIN failed--compilation aborted at ./spkg-install line 2.
```

I did have perl installed in the system, but only the `perl-base` package (5.10.0-19, debian/lenny).

However, the `File/Copy.pm` module is in `perl-modules` package, which wasn't installed in my system (`perl-base` priority is required, and `perl-modules` priority is standard).

The workaround was to `apt-get install perl-modules`; maybe this issue with `File/Copy.pm` could be checked in the prereq spkg?


---

Comment by mabshoff created at 2009-03-14 17:03:02

The real fix here is to get rid of the dependency since it is introduced by the Fortran library handling code written by Josh Kantor. The spkg-install should just be a shell script instead of a perl script given that we only copy two different setup.py files depending on the Fortran runtime used.

Cheers,

Michael


---

Attachment

patch for cvxopt-0.9.p7.spkg: replace spkg-install perl script by a bash script, eliminating the dependency on perl


---

Comment by tornaria created at 2009-05-01 21:58:42

Changing assignee from mabshoff to tornaria.


---

Comment by tornaria created at 2009-05-01 21:58:42

Changing status from new to assigned.


---

Comment by tornaria created at 2009-05-01 21:58:42

With the patch above, compilation of 3.4.1 was successful in a minimal debian lenny chroot created with `debootstrap` (minimal install) + `apt-get install make gcc g++ m4` inside the chroot.


---

Comment by tornaria created at 2009-05-17 02:04:41

See also #5964; it turns out building R documentation also requires perl-modules. Compilation of Sage proceeds without it, but some doctests (which use R documentation) fail. IOW, it seems perl-modules is a requirement for compilation after all...


---

Comment by mhansen created at 2009-06-20 01:27:06

Looks good to me.

The spkg with this patch applied can be found at: http://sage.math.washington.edu/home/mhansen/cvxopt-0.9.p8.spkg


---

Comment by rlm created at 2009-07-02 21:41:59

Resolution: fixed
