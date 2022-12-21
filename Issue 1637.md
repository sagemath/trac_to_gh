# Issue 1637: Update to mpfr 2.3.1 - fix small issues in the spkg

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-29 19:31:15

Assignee: mabshoff

From the MPFR mailing list:

```
The release of MPFR 2.3.1 is imminent. Please help to make this
release as good as possible by downloading and testing this
release candidate:

http://www.mpfr.org/mpfr-2.3.1/mpfr-2.3.1-rc1.tar.bz2
http://www.mpfr.org/mpfr-2.3.1/mpfr-2.3.1-rc1.tar.gz
http://www.mpfr.org/mpfr-2.3.1/mpfr-2.3.1-rc1.zip

The MD5's:
3a029172c380fc28f17db9c727d244e5  mpfr-2.3.1-rc1.tar.bz2
59f3523b93ec6674241110512b932f22  mpfr-2.3.1-rc1.tar.gz
ec69f43ad4bf00c3ce28467f0650bcb8  mpfr-2.3.1-rc1.zip

Changes from version 2.3.0 to version 2.3.1:
- Bug fixes; see <http://www.mpfr.org/mpfr-2.3.0/#bugs>.
- Improved MPFR manual.

Please send success and failure reports to <mpfr`@`loria.fr>.

If no problems are found, MPFR 2.3.1 should be released around
2008-01-12.

Happy New Year,

-- Vincent Lefèvre <vincent`@`vinc17.org> - Web: <http://www.vinc17.org/> 100% accessible validated (X)HTML - Blog: <http://www.vinc17.org/blog/> Work: CR INRIA - computer arithmetic / Arenaire project (LIP, ENS-Lyon) 
```

Paul Zimmermann also suggested:

```
## Paul Zimmerman's MPFR

My name ends with two 'n', and more importantly I'm not the only author.
The simplest is to just remove my name.

Also 'occured' should be 'occurred' in that file.
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 10:26:46

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-29 13:33:36

An updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/rc3/mpfr-2.3.1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-29 13:49:16

Passes build and `spkg-check` on Linux, MacOSX 10.5 and Solaris.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-29 13:49:46

Merged in Sage 2.10.1.rc3


---

Comment by mabshoff created at 2008-01-29 13:49:46

Resolution: fixed
