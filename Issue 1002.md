# Issue 1002: update clisp to 2.42

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-10-26 09:07:30

Assignee: was

Clisp 2.42 was released on October 16th.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-04 14:18:38

clisp 2.43 is actually out already!

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-05 21:00:57

Bill Page writes:

```
Well, so far I can confirm only that the following modified spkg:

  http://sage.math.washington.edu/home/page/clisp-2.43-alpha.spkg

which is based on clisp-2.43 as distributed by the clisp project,
installs in Sage running on sage.math and it can re-build (-f ...)
maxima-5.13.0.p1, axiom4sage-0.3.1 and the full version of FriCAS
(rev: 134).

I did only a fairly mimimal change to 'clisp-2.43-alpha.spkg' to
eliminate all patches and adapt to the slightly changed build process
(no intermediate makemake step necessary). FFI is automatically
included. It it quite possible that this version may not build on OSX
etc. however I know that the clisp developers have made some
significant improvements in the build since 2.41. I would be glad in
anyone can try this 'clisp-2.43-alpha.spkg' and let me know what works
and what doesn't. Also please feel free to take the above and run with
it. ;-)

```


I build tested on OSX 10.5 and clisp as well as maxima builds, doctesting at the moment. I will also test on OSX 10.4 PPC.

The spkg is about 3 MB larger than the 2.41 one? Can we shrink the spkg?

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-06 02:12:14

Resolution: fixed


---

Comment by mabshoff created at 2007-12-06 02:12:14

Merged in 2.9.alpha0.


---

Comment by mabshoff created at 2007-12-06 17:54:02

The spkg miscompiles with the current gcc from Debian testing x86. See

http://sourceforge.net/tracker/index.php?func=detail&aid=1836142&group_id=1355&atid=101355

It is a known issue that so far is unresolved.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-06 17:54:02

Resolution changed from fixed to 


---

Comment by mabshoff created at 2007-12-06 17:54:02

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-12-06 22:50:08

Carl Witty writes:

```
On my Debian testing 32-bit x86 Linux laptop, the clisp build failed.
The last few lines of the build log were:
rm -f dutch.lisp
ln -s /home/cwitty/sage-2.9.alpha0/spkg/build/clisp-2.43/src/src/
dutch.lisp dutch.lisp
rm -f deprecated.lisp
ln -s /home/cwitty/sage-2.9.alpha0/spkg/build/clisp-2.43/src/src/
deprecated.lisp deprecated.lisp
./lisp.run -B . -N locale -E 1:1 -Efile UTF-8 -Eterminal UTF-8 -norc -
m 1800KW -x "(and (load \"init.lisp\") (sys::%saveinitmem)
(ext::exit)) (ext::exit t)"
make[2]: *** [interpreted.mem] Segmentation fault
make[2]: Leaving directory `/home/cwitty/sage-2.9.alpha0/spkg/build/
clisp-2.43/build'

Recompiling without optimization may have worked (the compiles of
clisp and maxima have succeeded, but Sage as a whole isn't done
building yet, so I haven't tested).

I did this by adding
  export CFLAGS=-O0
to spkg-install, before the call to configure; and editing src/src/
makemake.in to replace every instance of "-O2" with '-O0".

(I'm not sure if both of these changes were necessary.) 
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-02-24 21:09:59

There is now a 2.43.1 release that supposedly fixes the gcc 4.2 and 4.3 problems at

http://www.haible.de/bruno/clisp/clisp-2.43.1.tar.gz

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-01 22:42:16

2.44.1 is also out and it has the same fix as 2.43.1, so let's try to update to the latest version.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-01 14:13:48

Resolution: wontfix


---

Comment by mabshoff created at 2008-05-01 14:13:48

This will not happen due to problems of clisp 2.44.1 with gcc 4.2 and 4.3.

We will likely build Maxima on top of ecl in the near future.

Cheers,

Michael
