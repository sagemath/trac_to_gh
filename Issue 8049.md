# Issue 8049: libgfortran *must* get shipped with the Sage binaries

Issue created by migration from https://trac.sagemath.org/ticket/8049

Original creator: was

Original creation time: 2010-01-24 02:22:18

Assignee: GeorgSWeber

CC:  jdemeyer tmonteil


```
I'm suddenly very concerned that Sage binaries won't work at all on computers without libgfortran.so installed. Does Sage even start up on such a box?

Yep.  If I take one of the Sage build machines, remove libgfortran, then start Sage I get:

$ sage
BOOM!

.... ImportError: libgfortran.so.3: cannot open shared object file: No such file or directory

----------------

Not good, since most Linux installs won't have libgfortran.  If I then reinstall gfortran, and copy libgfortran.so  to SAGE_ROOT/local/lib/, then uninstall gfortran, then Sage works fine again.

cp /usr/lib/libgfortran.so.3.0.0 local/lib/libgfortran.so.3

wstein@ubuntu910-64:/tmp/wstein/farm/sage-4.3.1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: import scipy.linalg
sage:
```



---

Comment by drkirkby created at 2010-01-24 02:32:40

I made the point the other day, that the library should be included in the binary, along with C++ library. 

Dave


---

Comment by drkirkby created at 2010-01-24 03:16:37

Actually, I think the C library too. The C library is very small anyway. If Sage is linked with a new library, and someone has an older one on their system, it could be a problem. 

'ldd' might be useful to get the location on Solaris, Linux or HP-UX, but not on OS X. Perhaps there is a more widely supported command, but I don't know of it. 

The configure script for gcc has these options. 


```
Fine tuning of the installation directories:
  --bindir=DIR           user executables [EPREFIX/bin]
  --libdir=DIR           object code libraries [EPREFIX/lib]
```


so while one could guess at the location of libraries from the location of the gfortran binary, it is not guaranteed to be right. 

On Solaris, in 64-bit mode, it will be in a subdirectory too


```
drkirkby@hawk:~$ find /usr/local -name libgfortran.so
/usr/local/gcc-4.3.4/lib/amd64/libgfortran.so
/usr/local/gcc-4.3.4/lib/libgfortran.so
/usr/local/gcc-4.5-20100114/lib/amd64/libgfortran.so
/usr/local/gcc-4.5-20100114/lib/libgfortran.so
/usr/local/lib/amd64/libgfortran.so
/usr/local/lib/libgfortran.so
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/libgfortran.so
/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/amd64/libgfortran.so
```


Dave


---

Comment by dimpase created at 2010-02-05 03:45:28

Replying to [comment:2 drkirkby]:
> Actually, I think the C library too. The C library is very small anyway. If Sage is linked with a new library, and someone has an older one on their system, it could be a problem. 
> 
> 'ldd' might be useful to get the location on Solaris, Linux or HP-UX, but not on OS X. Perhaps there is a more widely supported command, but I don't know of it. 
>

The OSX analog of ldd is called otool (otool -L), to be precise: 
{{
$ otool -L liblinboxsage.dylib
liblinboxsage.dylib:
	/tmp/sage-4.3.1/local/lib/liblinboxsage.0.dylib (compatibility version 1.0.0, current version 1.0.0)
	libntl.dylib (compatibility version 0.0.0, current version 0.0.0)
	/tmp/sage-4.3.1/local/lib/libgmpxx.3.dylib (compatibility version 5.0.0, current version 5.6.0)
	/tmp/sage-4.3.1/local/lib/libgmp.3.dylib (compatibility version 8.0.0, current version 8.6.0)
	/tmp/sage-4.3.1/local/lib/libgivaro.0.dylib (compatibility version 1.0.0, current version 1.2.0)
	/usr/lib/libstdc++.6.dylib (compatibility version 7.0.0, current version 7.4.0)
	/usr/lib/libgcc_s.1.dylib (compatibility version 1.0.0, current version 1.0.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 111.1.4)
}}

Just in case,
Dima


---

Comment by was created at 2010-02-13 00:29:07

I fixed this by writing a custom dist script that I use for building binaries.


---

Comment by was created at 2010-02-13 00:29:07

Resolution: fixed


---

Comment by drkirkby created at 2010-02-13 00:58:06

Does this do C and C++, or just Fortran? You can be 100% sure that the user needs the C and C++ libraries. You might well get away with it on most linux distros if gcc is installed. You certainly can't get away with it on Solaris, where a recent gcc is not installed unless someone has taken the steps to do so. 

Dave


---

Comment by startakovsky created at 2012-09-24 04:28:57

Hi, this is my first ticket, I just joined trac.  I have the following error when I try to import numpy:


```
ImportError: libgfortran.so.3: cannot open shared object file: No such file or directory
```


I have the latest releasted Sage Binary (5.3) installed on my linux machine, running Xubuntu.


---

Comment by dimpase created at 2012-09-24 04:42:25

Replying to [comment:6 startakovsky]:
> Hi, this is my first ticket, I just joined trac.  I have the following error when I try to import numpy:
> 
> {{{
> ImportError: libgfortran.so.3: cannot open shared object file: No such file or directory
> }}}
> 
> I have the latest releasted Sage Binary (5.3) installed on my linux machine, running Xubuntu. 

To help your particular installation, you can just do 

```
sudo apt-get install libgfortran3
```


We'll have to look into this more carefully, though.


---

Comment by mderickx created at 2012-09-24 06:06:23

It would be interesting to know whether this problem already occurred in sage 4.8 . The last thing I know that changed in relation to fortran is #12369  where the gcc package was added and the old fortran package removed. I think it would be good to open a new ticket for this issue, leaving this ticket as an "archive" for the old issue.


---

Comment by tmonteil created at 2012-10-28 15:24:30

Changing keywords from "" to "days43".


---

Comment by tmonteil created at 2012-10-28 15:24:30

Hi, is it possible to re-open this ticket ? Currently, libgfortran is not shipped with Sage.


---

Comment by jdemeyer created at 2012-10-29 08:19:55

Replying to [comment:9 tmonteil]:
> Hi, is it possible to re-open this ticket ?
It is certainly possible to re-open this ticket, but you should specify in more detail why.

In sage-5.3, libgfortran is shipped with the official Sage binaries, except for Ubuntu 12.04.  In sage-5.4, libgfortran will also be shipped with the Ubuntu 12.04 binaries, see #13515.


---

Comment by tcoffee created at 2014-08-30 07:52:23

Correct me if this issue has been superseded, but I just installed this binary

http://boxen.math.washington.edu/home/sagemath/sage-mirror/linux/64bit/sage-6.3-x86_64-Linux-Ubuntu_10.04_x86_64.tar.gz

and it appears not to include libgfortran.

I obtained the same ImportError as above when attempting to import numpy, and installing libgfortran3 fixed the problem.


---

Comment by dimpase created at 2014-08-30 08:18:49

Replying to [comment:11 tcoffee]:
> Correct me if this issue has been superseded, but I just installed this binary
> 
> http://boxen.math.washington.edu/home/sagemath/sage-mirror/linux/64bit/sage-6.3-x86_64-Linux-Ubuntu_10.04_x86_64.tar.gz
> 
> and it appears not to include libgfortran.

I imagine libgfortran comes from the gcc spkg nowadays, and this binary has no trace of gcc in it.


---

Comment by jdemeyer created at 2014-08-30 08:49:56

Yes, binaries _should_ be built with `SAGE_INSTALL_GCC=yes`, but apparently that's not the case.


---

Comment by leif created at 2014-08-30 11:45:12

Replying to [comment:13 jdemeyer]:
> Yes, binaries _should_ be built with `SAGE_INSTALL_GCC=yes`, but apparently that's not the case.

Does that make sense for distros with a more recent toolchain than Sage currently ships?


---

Comment by jdemeyer created at 2014-08-30 11:49:38

Replying to [comment:14 leif]:
> Does that make sense for distros with a more recent toolchain than Sage currently ships?
Yes, because you need to ship the libraries that you link against, such as `libgfortran.so`.


---

Comment by leif created at 2014-08-30 12:16:54

Replying to [comment:15 jdemeyer]:
> Replying to [comment:14 leif]:
> > Does that make sense for distros with a more recent toolchain than Sage currently ships?
> Yes, because you need to ship the libraries that you link against, such as `libgfortran.so`.

Well, these should be the "native" ones from the distro the binary was built on (and for).

So unless the distro's toolchain is exceptionally outdated or broken (I also wouldn't say Lucid's is), I think we shouldn't `SAGE_INSTALL_GCC`.

If we ship older libraries than the distro by default comes with / uses, we're IMHO just asking for trouble.  (Not all of them are properly versioned w.r.t. dynamically loading the "correct" one, IIRC.  So running other applications from within the Sage environment might fail.)




Requiring the user installing a Sage binary to eventually also install some stuff with the distro's package manager first isn't too much to ask for, provided that's sufficiently documented and/or a (start-up) script tells her/him to do so...

After all, the whole point of building binaries for _specific_ distros is that we know  which, or can expect that such and such (versions of) libraries and programs are present (or at least available through the package manager).


---

Comment by jdemeyer created at 2014-08-30 12:31:15

Replying to [comment:16 leif]:
> or at least available through the package manager
That's exactly the whole point here, this isn't about versions. We _do not want_ that users need to install something with their package manager. Sage binaries should work "out of the box".


---

Comment by leif created at 2014-08-30 12:53:36

Replying to [comment:17 jdemeyer]:
> Replying to [comment:16 leif]:
> > or at least available through the package manager
> That's exactly the whole point here, this isn't about versions. We _do not want_ that users need to install something with their package manager. Sage binaries should work "out of the box".

"Installing [with the distro's package manager]" (usually) doesn't mean building/compiling something, which is the point of bdists.

The Sage binary for Foonux 17.12 shouldn't contain any _part of that_ distro, because that'd just be redundant (not to mention potentially bypassing security updates etc.).

But my main point was that _using Sage's GCC_ for building bdists in general is not the same as shipping _the distro's_ libraries -- the former may cause further (or different) trouble.  So if you think we should ship libgfortran, just copy the system's one into `$SAGE_LOCAL/lib`; no need to install Sage's GCC just for that reason, whose libgfortran might (or typically will) be even older than the system's.


---

Comment by leif created at 2014-08-30 13:09:37

P.S.:  If you want to run Sage really "out of the box", use one of the Live CDs (or probably the VirtualBox image), or SMC... ;-)

The only flaw with the bdists currently is that Sage apparently doesn't check on (first) start-up whether its prerequisites are present, instead a probably mysterious or hard to understand error might(!) occur.  That's the bug.


---

Comment by jdemeyer created at 2014-08-30 13:16:30

Replying to [comment:18 leif]:
> "Installing [with the distro's package manager]" (usually) doesn't mean building/compiling something, which is the point of bdists.
> 
> The Sage binary for Foonux 17.12 shouldn't contain any _part of that_ distro, because that'd just be redundant (not to mention potentially bypassing security updates etc.).
> 
> But my main point was that _using Sage's GCC_ for building bdists in general is not the same as shipping _the distro's_ libraries -- the former may cause further (or different) trouble.  So if you think we should ship libgfortran, just copy the system's one into `$SAGE_LOCAL/lib`; no need to install Sage's GCC just for that reason, whose libgfortran might (or typically will) be even older than the system's.

This discussion should really be moved to `sage-release` instead of this ticket.


---

Comment by leif created at 2014-08-30 13:24:51

Replying to [comment:20 jdemeyer]:
> This discussion should really be moved to `sage-release` instead of this ticket.

I was thinking of replying there, but thought it was more on topic (or had the right audience) here.

We should probably invite fbissey, Snark and Jan Groenewald et al. to the party, in case they're not already cc'ed (haven't checked).


---

Comment by kcrisman created at 2014-09-09 12:23:57

Once again, lack of fortran or lapack or something causes trouble - see [this discussion](https://groups.google.com/forum/#!topic/sage-support/2BrsaLxkRIk), which references this ticket.


---

Comment by jdemeyer created at 2014-09-09 12:32:10

Replying to [comment:22 kcrisman]:
> Once again, lack of fortran or lapack or something causes trouble - see [this discussion](https://groups.google.com/forum/#!topic/sage-support/2BrsaLxkRIk), which references this ticket.
Not once again, it's the same issue as [comment:13]. It has been fixed in the sense that the next binaries which will be released will not have this problem.


---

Comment by tmonteil created at 2014-09-27 11:44:59

See also [this recent question on ask.sagemath.org](http://ask.sagemath.org/question/24286/cant-get-plotting-to-work/) showing that the problem still exists with 6.3 Ubuntu binary.


---

Comment by jdemeyer created at 2014-09-27 20:34:12

Replying to [comment:24 tmonteil]:
> See also [this recent question on ask.sagemath.org](http://ask.sagemath.org/question/24286/cant-get-plotting-to-work/) showing that the problem still exists with 6.3 Ubuntu binary.
Yes of course it does, in case you haven't read the recent comments: It has been fixed in the sense that the *next binaries* which will be released will not have this problem.
