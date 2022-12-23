# Issue 5382: Update MPFR to 2.4.1 (security)

Issue created by migration from https://trac.sagemath.org/ticket/5382

Original creator: mabshoff

Original creation time: 2009-02-26 04:15:10

Assignee: mabshoff


```
After a buffer overflow has been found (and fixed) in the
mpfr_snprintf and mpfr_vsnprintf functions of MPFR 2.4.0,
it has been decided to release MPFR 2.4.1 immediately.
It is available for download from the MPFR web site:

  http://www.mpfr.org/mpfr-2.4.1/

The MD5's:
22402995cf2496d8faea42c8da02ce1f  mpfr-2.4.1.tar.lzma
c5ee0a8ce82ad55fe29ac57edd35d09e  mpfr-2.4.1.tar.bz2
a70bbde2a23d82e8f3314d4293500ae4  mpfr-2.4.1.tar.gz
63c1ebc19f720853c75e5bef22405490  mpfr-2.4.1.zip

Changes from version 2.4.0 to version 2.4.1:
- Security fix in mpfr_snprintf and mpfr_vsnprintf (buffer overflow).
- Configure: new checks for length modifiers hh and ll (new in C99)
  as hh is absent on alpha-OSF1-V5.
- Miscellaneous corrections in the MPFR manual. In particular,
  mpfr_inits, mpfr_inits2, mpfr_clears and MPFR_DECL_INIT have been
  in the public API since MPFR 2.4.0.

You can send success and failure reports to <mpfr@loria.fr>, and give
us the canonical system name as returned by the config.guess script,
the processor and compiler version, in order to complete the
"Platforms Known to Support MPFR" section of the MPFR 2.4.1 web page.
```



---

Comment by mabshoff created at 2009-02-26 04:15:17

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-03-02 23:17:05

The new spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4/rc0/mpfr-2.4.1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-02 23:25:23

Resolution: fixed


---

Comment by mabshoff created at 2009-03-02 23:25:23

Merged in Sage 3.4.rc0.

Cheers,

Michael
