# Issue 2205: new spkg -- sqlalchemy

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-02-18 18:18:12

Assignee: yi

Keywords: dsage, database, sqlite, sql

spkg can be found here:

http://sage.math.washington.edu/home/yqiang/spkgs/SQLAlchemy-0.4.3.p0.spkg

tested on OSX (10.5), Linux

dsage is going to be using sqlalchemy from now on for the database backend since it will make switching database engines seamless and also prevent me from writing crappy sql. I think other parts of SAGE that have a database component could benefit significantly from this package, especially if they are able to use an ORM pattern.


---

Comment by was created at 2008-02-19 15:10:06

REFEREE REPORT:

(1) This spkg has the OS X "kiss of metajunk" (notice all the ._ files that need
to be stripped out):


```
teragon:Downloads was$ tar jxvf SQLAlchemy-0.4.3.p0.spkg 
SQLAlchemy-0.4.3.p0/
SQLAlchemy-0.4.3.p0/._spkg-install
SQLAlchemy-0.4.3.p0/spkg-install
SQLAlchemy-0.4.3.p0/._SPKG.txt
SQLAlchemy-0.4.3.p0/SPKG.txt
SQLAlchemy-0.4.3.p0/src/
SQLAlchemy-0.4.3.p0/src/._CHANGES
SQLAlchemy-0.4.3.p0/src/CHANGES
SQLAlchemy-0.4.3.p0/src/._doc
SQLAlchemy-0.4.3.p0/src/doc/
SQLAlchemy-0.4.3.p0/src/doc/._alphaapi.html
SQLAlchemy-0.4.3.p0/src/doc/alphaapi.html
SQLAlchemy-0.4.3.p0/src/doc/._alphaimplementation.html
SQLAlchemy-0.4.3.p0/src/doc/alphaimplementation.html
SQLAlchemy-0.4.3.p0/src/doc/._build
SQLAlchemy-0.4.3.p0/src/doc/build/
SQLAlchemy-0.4.3.p0/src/doc/build/._content
...
```


Maybe you can somehow build the spkg on sage.math -- that's what I have to do to avoid this metastuff on OS X?

(2) This spkg downloads stuff off the internet during install:

```

---------------------------------------------------------------------------
This script requires setuptools version 0.6c3 to run (even to display
help).  I will attempt to download it for you (from
http://cheeseshop.python.org/packages/2.5/s/setuptools/), but
you may need to enable firewall access for this script first.
I will start the download in 15 seconds.

(Note: if this machine does not have network access, please obtain the file

   http://cheeseshop.python.org/packages/2.5/s/setuptools/setuptools-0.6c3-py2.5.egg

and place it in this directory before rerunning this script.)
---------------------------------------------------------------------------
Downloading http://cheeseshop.python.org/packages/2.5/s/setuptools/s
```


This is absolutely 100% forbidden for Sage packages.   Imagine a computer installation that isn't on the internet at all -- installing Sage on such computers is fully supported by Sage and must remain so.

3. I think spkg-install should start with #!/bin/sh or something:

```
teragon:SQLAlchemy-0.4.3.p0 was$ more spkg-install 
cd src
python setup.py install
```


4. Since src/doc is included and is pretty big, maybe it should be installed somewhere standard, e.g., SAGE_ROOT/local/doc/  It's very nice html documentation and is a shame to not install it.  Actually, more generally we should install *all* the docs for packages to SAGE_ROOT/local/doc/.  I don't know why we don't do that already.  Right now only NTL's. docs get installed. 

5. Can you write an spkg-check script that runs the SQLAlchemy test suite and exists with code 0 if and only if there is success.


---

Comment by yi created at 2008-02-19 16:25:55

Thanks for the feedback.

1. Fixed

2. We will need to make a separate package for setuptools. We should talk about using setuptools to install python packages. It is *extremely* nice. Check out
http://peak.telecommunity.com/DevCenter/setuptools
These days if I want to install any python module, i just do 'easy_install python_module', it does the rest for me.

3. Fixed

4. Fixed

5. What calls spkg-check? Should I call it at the end of spkg-install?


---

Comment by mabshoff created at 2008-02-19 16:54:21

Replying to [comment:2 yi]:
> Thanks for the feedback.
> 
> 1. Fixed
> 
> 2. We will need to make a separate package for setuptools. We should talk about using setuptools to install python packages. It is *extremely* nice. Check out
> http://peak.telecommunity.com/DevCenter/setuptools
> These days if I want to install any python module, i just do 'easy_install python_module', it does the rest for me.

Jaap did make a setuptools.spkg already, so that should be easy to get that issue resolved. You said something about a specific version you needed. Which one is that?

> 3. Fixed
> 
> 4. Fixed
> 
> 5. What calls spkg-check? Should I call it at the end of spkg-install?

Nope, it is done automatically by sage-spkg when SAGE_CHECK is non-empty. It is run before deleting the build directory. Look at the mpfr.spkg for example for a good spkg-check script.

Cheers,

Michael


---

Comment by yi created at 2008-02-19 17:23:20

Replying to [comment:3 mabshoff]:
> Replying to [comment:2 yi]:
> > Thanks for the feedback.
> > 
> > 1. Fixed
> > 
> > 2. We will need to make a separate package for setuptools. We should talk about using setuptools to install python packages. It is *extremely* nice. Check out
> > http://peak.telecommunity.com/DevCenter/setuptools
> > These days if I want to install any python module, i just do 'easy_install python_module', it does the rest for me.
> 
> Jaap did make a setuptools.spkg already, so that should be easy to get that issue resolved. You said something about a specific version you needed. Which one is that?
> 
It needs setuptools-0.6c3 or higher.

> > 3. Fixed
> > 
> > 4. Fixed
> > 
> > 5. What calls spkg-check? Should I call it at the end of spkg-install?
> 
> Nope, it is done automatically by sage-spkg when SAGE_CHECK is non-empty. It is run before deleting the build directory. Look at the mpfr.spkg for example for a good spkg-check script.

Ok fantastic, I've added a spkg-check script which runs the unittests for SQLAlchemy. 

Please review the updated spkg here:

http://sage.math.washington.edu/home/yqiang/spkgs/SQLAlchemy-0.4.3.p0.spkg
> 
> Cheers,
> 
> Michael


---

Comment by yi created at 2008-02-19 17:24:46

Depends on http://trac.sagemath.org/sage_trac/ticket/1868


---

Comment by rlm created at 2008-03-12 05:25:14

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-03-14 15:23:38

Replying to [comment:5 yi]:
> Depends on http://trac.sagemath.org/sage_trac/ticket/1868

Nope, it depends on #2481 :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-14 17:00:56

Hi Yi,

I did various things:
 * add an hg repo
 * add .hgignore
 * fix various small issues.
 * rename the spkg to all lowercase

All changes can be found in 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.4/alpha0/sqlalchemy-0.4.3.p1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-14 17:01:20

Resolution: fixed


---

Comment by mabshoff created at 2008-03-14 17:01:20

Merged in Sage 2.10.4.alpha0


---

Comment by was created at 2008-03-14 19:50:55

Resolution changed from fixed to 


---

Comment by was created at 2008-03-14 19:50:55

Changing status from closed to reopened.


---

Comment by was created at 2008-03-14 19:50:55

I'm reopening this because there is now a procedure for new spkg's to go into sage, and we need to follow it.


---

Comment by mabshoff created at 2008-03-15 08:35:05

As per http://groups.google.com/group/sage-devel/t/1c42fb1e4ca32230 we have a unanimous vote for inclusion.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-15 08:35:05

Resolution: fixed
