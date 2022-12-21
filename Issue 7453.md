# Issue 7453: add sandpile experimental package

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2009-11-13 18:13:08

Assignee: AlexGhitza

CC:  wdj

Keywords: sandpile

David Perkinson created a sage module for doing sandpile computations.  See http://people.reed.edu/~davidp/sand/sage/html/sage_sandpiles.html#projective
for his documentation of it.
This ticket makes an experimental spkg for the module.  It installs glpk and 4ti2 which are required for the full functionality.
First attempt is up at:
http://sage.math.washington.edu/home/mhampton/sandpile-1.51.spkg


---

Comment by mhampton created at 2009-11-13 18:19:01

Changing status from new to needs_review.


---

Comment by mhampton created at 2009-11-16 13:57:20

I just updated the spkg since I had accidently used version 1.4 of the sandpile.sage file instead of 1.51.


---

Comment by drkirkby created at 2009-12-24 00:07:33

I get a problem with what it is trying to download. I guess this may be a problem with what is on the server, rather than what this package needs, but this is what I get (Solaris 10, Sun Blade 2000)


```
sandpile-1.51/src/sandpile.py
sandpile-1.51/src/setup.py
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_141444-09 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/usr/local/gcc-4.4.1-sun-linker/bin/gcc -v
Using built-in specs.
Target: sparc-sun-solaris2.10
Configured with: ../gcc-4.4.1/configure --prefix=/usr/local/gcc-4.4.1-sun-linker/ --with-as=/usr/ccs/bin/as --without-gnu-as --with-ld=/usr/ccs/bin/ld --without-gnu-ld --enable-languages=c,c++,fortran --with-mpfr-include=/usr/local/include --with-mpfr-lib=/usr/local/lib --with-gmp-include=/usr/local/include --with-gmp-lib=/usr/local/lib CC=/usr/sfw/bin/gcc CXX=/usr/sfw/bin/g++ LDFLAGS='-R /usr/local/lib -L /usr/local/lib'
Thread model: posix
gcc version 4.4.1 (GCC) 
****************************************************
running install
running build
running build_py
creating build
creating build/lib
copying sandpile.py -> build/lib
running install_lib
running install_egg_info
Removing /export/home/drkirkby/sage-4.2.1/local/lib/python2.6/site-packages/sandpile-1.51-py2.6.egg-info
Writing /export/home/drkirkby/sage-4.2.1/local/lib/python2.6/site-packages/sandpile-1.51-py2.6.egg-info
Possible names of non-installed packages starting with 'glpk':
  glpk-4.38.p4
  glpk-4.9
Traceback (most recent call last):
  File "/export/home/drkirkby/sage-4.2.1/local/bin/sage-eval", line 15, in <module>
    eval(compile(s,'<cmdline>','exec'))
  File "<cmdline>", line 1, in <module>
  File "/export/home/drkirkby/sage-4.2.1/local/lib/python2.6/site-packages/sage/misc/package.py", line 141, in install_package
    raise ValueError, "There is more than one package name starting with '%s'. Please specify!"%(package)
ValueError: There is more than one package name starting with 'glpk'. Please specify!
Force installing 4ti2.p0
Calling sage-spkg on 4ti2.p0
Warning: Attempted to overwrite SAGE_ROOT environment variable
4ti2.p0
Machine:
SunOS swan 5.10 Generic_141444-09 sun4u sparc SUNW,Sun-Blade-1000
Deleting directories from past builds of previous/current versions of 4ti2.p0

```



---

Comment by mhampton created at 2009-12-24 01:47:18

That's a flaw in the install_package script if there is more than one package with the same name.

As a workaround I will change it to use the 4.9 package.  I uploaded it to the same file as above (http://sage.math.washington.edu/home/mhampton/sandpile-1.51.spkg).


---

Comment by schilly created at 2010-02-05 20:14:06

but isn't glpk 4.9 years old? you should take 4.38.


---

Comment by mhampton created at 2010-02-06 14:11:51

Really? That's confusing version numbering.  For the sandpiles package I don't think the version matters too much.

Anyway, this is just going in the experimental packages so I would appreciate someone giving it a try and then a positive review if it works for you - I think the bar is set pretty low for experimental.


---

Comment by drkirkby created at 2010-02-06 14:44:40

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-02-06 14:44:40

It appears to make use of a GNU specific option to 'grep' (either that, or someone else has screwed something up, to make use of a GNU specific option). 


```
drkirkby`@`swan:[~/sage-4.3.0.1] $ ./sage -i http://sage.math.washington.edu/home/mhampton/sandpile-1.51.spkg
Installing http://sage.math.washington.edu/home/mhampton/sandpile-1.51.spkg
Calling sage-spkg on http://sage.math.washington.edu/home/mhampton/sandpile-1.51.spkg
Warning: Attempted to overwrite SAGE_ROOT environment variable
sandpile-1.51
Machine:
SunOS swan 5.10 Generic_141444-09 sun4u sparc SUNW,Sun-Blade-1000
Deleting directories from past builds of previous/current versions of sandpile-1.51
/export/home/drkirkby/sage-4.3.0.1/local/bin/sage-spkg: file sandpile-1.51 does not exist
Attempting to download it.
grep: illegal option -- o
Usage: grep -hblcnsviw pattern file . . .
Searching for latest version of sandpile-1.51
Could not find a version for sandpile-1.51.
```


Dave


---

Comment by drkirkby created at 2010-02-06 14:47:26

I've added myself as a reviewer. The author field is not filled in either.


---

Comment by drkirkby created at 2010-02-06 14:50:44

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-02-06 14:50:44

I realised some someone else must have screwed up and added the GNUism, so its not this package. Hence I am changing to needs review again.


---

Comment by wdj created at 2010-02-06 17:46:25

This installs on a mac 10.6.2 and runs at least some of the commands on
http://people.reed.edu/~davidp/sand/sage/2.0/html/sandpile.html
(I just did this today). I also installed it a few months ago on a linux 
(ubuntu) machine at work.

What more do you want for a positive review?


---

Comment by mhampton created at 2010-02-07 03:42:15

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2010-02-07 03:42:15

I don't want anything more for a positive review.  I think for an
experimental package just about anything goes.  The advantage of the
experimental package is that David Perkinson can at least say: if you
want to install this package in sage, just do: sage -i sandpile-1.51

That will make it easier for other people (besides sage developers) to
give it a try.  It would be nice to eventually get it into Sage
itself, and this is just a first step.

-Marshall


---

Comment by was created at 2010-02-07 05:37:48

I've added the spkg here:

   http://sagemath.org/packages/experimental/


---

Comment by was created at 2010-02-07 05:37:48

Resolution: fixed
