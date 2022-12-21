# Issue 3716: [with spkg, needs review] add GINV as experimental/optional package

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-07-23 19:32:57

Assignee: mabshoff

CC:  burcin

From the Ginv website (http://invo.jinr.ru/ginv/index.html)
"The open source software GINV implements the Gröbner bases method for systems of equations. GINV is a C++ module of Python designed for constructing Gröbner bases of ideals and modules in polynomial, differential and difference rings. Gröbner bases are constructed by involutive algorithms. GINV is an open source software. The source codes, the installation package for Python, documentation in Russian and English are available on the Web page http://invo.jinr.ru"

The package has a pretty good reputation for fast GBs over QQ. It also is reported to have a fast multivariate GCD over QQ and GF(q) and GBs over ZZ.


---

Comment by malb created at 2008-07-23 19:33:35

The SPKG is here:

   http://sage.math.washington.edu/home/malb/spkgs/ginv-1.9-20080723.spkg


---

Comment by mabshoff created at 2008-07-29 17:11:16

There are some small issues, all of which I fixed:

 * .hgignore is missing and patches/setup.py was not under revision control
 * the dependencies in SPKG.txt were from M2 it seems - ginv only depends on gmp

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-29 17:11:39

Resolution: fixed


---

Comment by mabshoff created at 2008-07-29 17:11:39

Merged in the optinal repo in Sage 3.0.6.final
