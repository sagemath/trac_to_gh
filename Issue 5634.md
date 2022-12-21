# Issue 5634: installing optional R packages is broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-29 18:14:38

Assignee: mabshoff

CC:  jdemeyer

This email contains a bunch of good ideas for fixing this.


```
Mr. Stein,

I was on IRC sage-devel asking about some problems installing new packages for R.  You asked if I could fix it and unfortunately I can not completely fix it, but I did learn more about the problems preventing it from working.  I was up late waiting for the Formula 1 race to start and so I had a look at some of the problems with r.install_packages().

1. local/bin/R and/or local/lib/R/bin/R
    Not sure why there are two or which gets called ... but one (or both) seem to be called a lot during R package installation.  Anyway, they are both identical and have an echo line that seems to get piped into gcc command lines causing many problems.

[from local/bin/R]
  echo "WARNING: ignoring environment value of R_HOME"

This may be a total kludge in the grand scheme of things, but redirecting echo's output to stderr seems to allow many packages (e.g., nortest) to be built so that they can be used.

[I changed the above echo line in both files to ...]
  echo "WARNING: ignoring environment value of R_HOME" 1>&2

2. local/lib/R/etc/Makeconf
    Not sure what this fixes as there is still a problem with C++ packages, but the file above has:

CPPFLAGS = -I/home/rick/sage/sage-3.2.3/local/inlcude

The unfortunate character swapping is easily fixed with:

 CPPFLAGS = -I/home/rick/sage/sage-3.2.3/local/include

3. local/lib/gcc-lib/i686-pc-linux-gnu/4.0.3/libgcc_s.so.1
    I'm not exactly sure what the problem here is, but I believe it has to do with building C++ libraries with a gcc version that does not match.  I use Fedora 9 and my version of gcc is 4.3.1.  When, after making the changes described above in 1 and 2, I tried to build the R package Matrix (r.install_packages('Matrix')), the resulting library could not be loaded.

Error in dyn.load(file, ...) :
  unable to load shared library '/home/rick/sage/sage-3.2.3/local/lib/R/library/Matrix/libs/Matrix.so':
  /home/rick/sage/sage-3.2.3/local/lib/gcc-lib/i686-pc-linux-gnu/4.0.3/libgcc_s.so.1: version `GCC_4.2.0' not found (required by /usr/lib/libstdc++.so.6)
Error: require(Matrix) is not TRUE
Execution halted
ERROR: installing package indices failed
** Removing '/home/rick/sage/sage-3.2.3/local/lib/R/library/Matrix'

There are still some mysteries to be solved but I hope the above is a start.

Regards,
Richard Graham
```



---

Comment by kcrisman created at 2011-02-16 22:29:33

Is this still an issue?  I have installed all sorts of optional packages, including live, from the notebook, in front of R developers ...


---

Comment by kcrisman created at 2011-03-12 04:06:58

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-03-12 04:06:58

Changing component from optional packages to packages.


---

Comment by kcrisman created at 2011-03-12 04:06:58

I just installed an optional package earlier today in front of a very heavy R user, and it worked.  The package Matrix is now actually built in Sage's R, as a 'recommended' package, in fact, so the specific example above clearly is not correct any more.  Here are some examples.

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: r.library('Matrix') # no error, so ok
sage: r.install_packages('actuar')
| Sage Version 4.6.2, Release Date: 2011-02-25                       |
| Type notebook() for the GUI, and license() for information.        |
R version 2.10.1 (2009-12-14)
Copyright (C) 2009 The R Foundation for Statistical Computing
ISBN 3-900051-07-0
<snip>
> options(repos="http://cran.r-project.org/"); install.packages("actuar")
trying URL 'http://cran.r-project.org/src/contrib/actuar_1.1-1.tar.gz'
Content type 'application/x-gzip' length 844553 bytes (824 Kb)
opened URL
==================================================
downloaded 824 Kb

* installing *source* package ‘actuar’ ...
** libs
<snip normal gcc build messages>
** R
** data
**  moving datasets to lazyload DB
** demo
** inst
** preparing package for lazy loading
** help
*** installing help indices
** building package indices ...
* DONE (actuar)

The downloaded packages are in
	‘/private/var/folders/Yy/YytEJm5VEB0+pBRD7JNLe++++TQ/-Tmp-/RtmpkOoOEc/downloaded_packages’
Updating HTML index of packages in '.Library'
> 

real	0m12.514s
user	0m5.989s
sys	0m1.154s
Please restart Sage in order to use 'actuar'.
sage: r.library('actuar') # again, no error, so ok
```

Without more details, and given the age of the ticket, I believe this ticket should be closed.  I claim no credit for it, other than observing it works - probably fixed someplace along the line and no one noticed this ticket.

Changing component, since the optional package is for R; R itself is a standard Sage package.

To release manager: please close this ticket.


---

Comment by kcrisman created at 2011-03-12 04:07:11

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-03-22 21:15:14

Resolution: invalid
