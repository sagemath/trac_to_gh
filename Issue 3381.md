# Issue 3381: iconv library needs to be added to Sage to allow R to build on Solaris.

Issue created by migration from https://trac.sagemath.org/ticket/3381

Original creator: drkirkby

Original creation time: 2008-06-07 13:19:55

Assignee: mabshoff

I believe it is known that Sage does not build on Solaris due to several problems, one of which is in R. Whilst trying to build R 2.6.1.p17 as part of Sage 3.0.3.alpha1 I get the following from the R configure script:


```
checking iconv.h usability... yes
checking iconv.h presence... yes
checking for iconv.h... yes
checking for iconv... in libiconv
checking whether iconv accepts "UTF-8", "latin1" and "UCS-*"... no
checking for iconvlist... yes
configure: error: --with-iconv=yes (default) and a suitable iconv is
not available 
```


I believe (hope) I have got to the bottom of this, with the help of Brian D. Ripley who is one of the R developers.

R needs a powerful version of iconv - the one supplied by Sun is not sufficiently powerful. This is documented in the 'R Installation and Administration' manual. 

http://cran.r-project.org/doc/manuals/R-admin.pdf

Section C 4.1 says:

''Modern Solaris systems allow a large selection of Open Source software to be installed via
pkg-get: a Sparc Solaris 10 system came with libreadline and libiconv and a choice of gcc3
and gcc4 compilers, installed under ‘/opt/csw’. (You will need GNU libiconv: the Solaris
version of iconv is not sufficiently powerful.)''

The GNU one is ok, for which a Blastwave package is available. But since it is the Sage policy of including all the libraries like this, I suspect you want to add iconv. 

Although I had iconv from Blastwave, I just downloaded the source code for version 1.12 and found iconv took less than two minutes to build on my Blade 2000 (2 x 1.2 GHz, 8 GB RAM). It's 4.1 MB in size. Get it from

http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.12.tar.gz

A few relavant links are:

http://groups.google.com/group/sage-devel/browse_thread/thread/67c8234f07758c06
(where it was pointed out by an R-developer that my analysis was wrong)

http://www.nabble.com/Fail-to-call-AC_CACHE_CHECK-on-R-2.7.0-for-Solaris-td17707789.html
(My question about this on the R developer mailing list).


Dr. David Kirkby



---

Comment by mabshoff created at 2008-09-06 00:54:49

Wontfix since we have disabled libiconv for the R build on Solaris for now. Should iconv become mandatory we will revisit the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-06 00:54:49

Resolution: wontfix


---

Comment by drkirkby created at 2010-01-28 11:14:09

Since this has come up again, I'll make a few further comments. 

 * 'pkg-get' is not a Solaris command, but a command from 'Blastwave'. 
 * You need root access to use software from Blastwave. 
 * Blastwave has had some _issues_ with bitter arguments between those involved. It was down for several weeks, but is now online. There is a _fork_ of OpenCSW now. 
 * The link I gave to the source for iconv is probably well out of date now. 

Dave
