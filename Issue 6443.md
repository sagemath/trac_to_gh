# Issue 6443: A GNUism in zn_poly-0.9.p0 causes linking problems wiith Sun's linker

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-06-29 01:27:54

Assignee: drkirkby

Keywords: GNUism linker flags soname

The basic problem is seen below. gcc is called with the -Wl,-soname flag, so -soname gets passed to the linker. But if the linker is the Sun linker, this breaks. 

gcc -shared -Wl,-soname,libzn_poly-`cat VERSION`.so -o libzn_poly-`cat VERSION`.so src/array.o src/invert.o src/ks_support.o src/mulmid.o src/mulmid_ks.o src/misc.o src/mpn_mulmid.o src/mul.o src/mul_fft.o src/mul_fft_dft.o src/mul_ks.o src/nuss.o src/pack.o src/pmf.o src/pmfvec_fft.o src/tuning.o src/zn_mod.o -L/export/home/drkirkby/sage/sage-4.1.alpha2/local/lib -lgmp -lm
ld: warning: option -o appears more than once, first setting taken
ld: fatal: file libzn_poly-0.9.so: unknown file type

I should be able to fix this without too many problems. 





---

Comment by drkirkby created at 2009-06-29 02:36:57

It was very easily fixed, with just a bit of code to change a flag is the operating system is Solaris and the linker is Suns. There was already code to apply a patch for OS X, do I just added to that, so spkg-install now has:


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
   echo "64 bit MacIntel"
   CFLAGS="-O3 -g -m64 -fPIC -L."; export CFLAGS
   LDFLAGS="-m64 "; export LDFLAGS
   cp patches/makemakefile.py src/makemakefile.py
elif [ `uname` = "SunOS" -a "`ld  --version  2>&1  | grep GNU`" = ""  ]; then
   # Change -soname to -h if the Sun linker is used.
   sed 's/-soname/-h/g' src/makemakefile.py > /tmp/makemakefile.py.$$
   mv /tmp/makemakefile.py.$$ src/makemakefile.py
   CFLAGS="-fPIC -O3 -L."; export CFLAGS
   LDFLAGS=""; export LDFLAGS
else
   CFLAGS="-fPIC -O3 -L."; export CFLAGS
   LDFLAGS=""; export LDFLAGS
fi
```


http://sage.math.washington.edu/home/kirkby/Solaris-fixes/zn_poly/


---

Comment by drkirkby created at 2009-06-29 02:36:57

Changing status from new to assigned.


---

Comment by was created at 2009-06-29 13:59:59


```
William Stein wrote:

> Can you post instructions there that explain to me (at least) how to use
> the Sun linker on t2.math to test your spkg?  It's difficult to review your
> spkg if I don't know what to do to test it.
>
> Whenever I post track tickets that involve the build system and spkg's, I
> always write, to test this do:
>    1.
>    2.
>    3.
>
> so it is easy on reviewers.
>
>  -- William

I have not given details before, since I am still not 100% happy with
the installation of the compiler. But

source /usr/local/gcc-4.4.0-sun-linker/gcc440sun

will probably work for you. Stick that at the end of your .profile and
.bashrc

But it requires the setting of LD_LIBRARY_PATH (which that script does),
which is generally a bad thing to do, except as a last resort. It should
not be necessary to build or run a compiler with LD_LIBRARY_PATH set.

See the following links for why it is bad.

http://xahlee.org/UnixResource_dir/_/ldpath.html
http://www.sunmanagers.org/pipermail/summaries/2002-May/001694.html

I seem to be pulling my hair out trying to get gcc to build *properly*,
without hacks to get it to run well.

The gcc developers take the attitude you stick everything in /usr/local
and consider that a 'standard'. That's fine if you only want one version
of gcc, but not so clever if you want to have multiple versions, and
keep them all separate, with the ability to upgrade one program without
it having implications on lots of others.

I've stuck a few libraries in /usr/local/lib. It would be nice to be
able to try updates of those, test them somewhere else and test, but
it's a bit difficult with gcc's insistance of looking in /usr/local/lib.
I have thought of taking a sed script to the gcc-4.4.0 tar fail, so
avoid some of its internal paths which can't be changed!!


Anyway, that aside,

source /usr/local/gcc-4.4.0-sun-linker/gcc440sun

should set the following things up.

1) The linker and assembler in the path before the GNU ones (the latest
versions of which reside in /usr/local/bin)

2) make and tar to the GNU ones (I don't like forcing that on people,
but it will have to do here to avoid issues with Sage)

3) C and C++ compiler to those that use the Sun linker in
/usr/local/gcc-4.4.0-sun-linker/bin/

if you type

gcc -v

you will see it uses the Sun linker and assembler.


I've linked gfortran to g77 and f77, so if a program calls f77, it will
get the GNU fortran compiler (using the Sun linker) rather than the Sun
fortran compiler.

Let me know how you get on, but I do consider it a bit of a fudge. (It's
the same fudge Michael, but it must be possible to build gcc without it).

Be warned, trying to link shared libraries created with the GNU linker,
with those created with the Sun linker, might (probably will) cause
problems. In theory it should be ok, but I know lots of people have had
issues with this. Hence I suggest you start a new build if using that
compiler.

Since the disks are so slow, It's worth doing that in /tmp if you don't
mind the risk of loosing the stuff if the machine gets rebooted for any
reason. Otherwise it takes ages to build. Obviously, don't put too much
in /tmp, but it seems the only practical way to build anything on t2 in
a reasonable period of time.

Dave
```



---

Comment by drkirkby created at 2009-07-13 23:51:16

I've set the default compiler to be gcc 4.2.4, as that is the latest which will build MPFR with no test failures. So to test

1) Log onto t2, where the default compiler will be fine. 
2) gcc -v should include in the output:

```
--with-ld=/usr/ccs/bin/ld --without-gnu-ld
```

which indicates gcc is configured to gnu linker. 

3) Install the patch for NTL, which changes an option on 'cp', which has already received positive review (6380), IF it is not incorporated already. It is not in 4.1, but might be in a later release. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ntl-5.4.2.p9/ntl-5.4.2.p9.spkg

This is needed, as ntl is built in Sage before znpoly. 

5) Depending on what version of Sage you build it with, and so the exact order znpoly gets built, it may be necessary to apply one of the other Solaris patches as well. 

Check here for a patch. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/


---

Comment by mvngu created at 2009-07-15 12:59:08

Replying to [comment:3 drkirkby]: 
> 3) Install the patch for NTL, which changes an option on 'cp', which has already received positive review (6380), IF it is not incorporated already. It is not in 4.1, but might be in a later release. 
> 
> http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ntl-5.4.2.p9/ntl-5.4.2.p9.spkg
> 
> This is needed, as ntl is built in Sage before znpoly.
After uncompressing `ntl-5.4.2.p9.spkg`, I see two junk files:

```
[mvngu`@`sage ntl-5.4.2.p9]$ hg st
M SPKG.txt
M patches/mfile
M patches/mfile.patch
? patches/mfile.orig
```

namely `patches/mfile.patch` and `patches/mfile.orig`. If you have already patched `patches/mfile`, then remove those junk files. Then review your changes to `patches/mfile` and `SPKG.txt` using

```
hg diff
```

If you're happy with your changes, then check in your changes with

```
hg ci
```

This will open up an editor. Enter a meaningful commit message. Preferably, your commit message should follow this template

```
trac 6443: <meaningful-commit-message-here>
```

Then create an updated version of your spkg and post a link to that updated version on this ticket.


---

Comment by mvngu created at 2009-07-15 16:19:09

Replying to [comment:1 drkirkby]:
> It was very easily fixed, with just a bit of code to change a flag is the operating system is Solaris and the linker is Suns. There was already code to apply a patch for OS X, do I just added to that, so spkg-install now has:
> 
> {{{
> if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
>    echo "64 bit MacIntel"
>    CFLAGS="-O3 -g -m64 -fPIC -L."; export CFLAGS
>    LDFLAGS="-m64 "; export LDFLAGS
>    cp patches/makemakefile.py src/makemakefile.py
> elif [ `uname` = "SunOS" -a "`ld  --version  2>&1  | grep GNU`" = ""  ]; then
>    # Change -soname to -h if the Sun linker is used.
>    sed 's/-soname/-h/g' src/makemakefile.py > /tmp/makemakefile.py.$$
>    mv /tmp/makemakefile.py.$$ src/makemakefile.py
>    CFLAGS="-fPIC -O3 -L."; export CFLAGS
>    LDFLAGS=""; export LDFLAGS
> else
>    CFLAGS="-fPIC -O3 -L."; export CFLAGS
>    LDFLAGS=""; export LDFLAGS
> fi
> }}}
> 
> http://sage.math.washington.edu/home/kirkby/Solaris-fixes/zn_poly/
The spkg at that address has some junks in it. I removed them, checked in changes in David Kirkby's name, and have uploaded an updated version at

http://sage.math.washington.edu/home/mvngu/patch/zn_poly-0.9.p1.spkg


---

Comment by mvngu created at 2009-07-15 18:48:24

This is a 

```
****************
POSITIVE REVIEW!
****************
```

May the Solarisification of Sage... er... I mean the force be with you :-)


---

Comment by mvngu created at 2009-07-16 10:26:55

Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by mvngu created at 2009-07-16 21:26:29

Resolution: fixed
