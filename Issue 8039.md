# Issue 8039: [with spkg, needs review] ATLAS libs fail to build on Open Solaris 64 bit due to wrong LDFLAG -melf_x86_64

Issue created by migration from https://trac.sagemath.org/ticket/8039

Original creator: jsp

Original creation time: 2010-01-22 13:11:49

Assignee: drkirkby

Keywords: building

in src/CONFIG/src/SpewMakeInc.c LDFLAGS are set for inclusion in Make.inc. This file is included in all Makefiles.

As a workaround I changed -melf_x86_64 in -64 in Make.inc in the directory where the libraries are built.

This is SunOS with SAGE64="yes" only.

An spkg can be found here:
[http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p11.spkg](http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p11.spkg)


---

Comment by jsp created at 2010-01-22 15:04:01

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-26 12:20:30

What has been changed? I can't find the changed file? You should not change the ATLAS source code, but create a patch, which gets applied with spkg-install.


---

Comment by drkirkby created at 2010-01-26 12:20:46

PS, you should also report this failure upstream.


---

Comment by jsp created at 2010-01-26 18:02:37

Replying to [comment:2 drkirkby]:
> What has been changed? I can't find the changed file? You should not change the ATLAS source code, but create a patch, which gets applied with spkg-install. 
> 

See the patch.

Jaap


---

Comment by drkirkby created at 2010-01-27 02:00:14

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-01-27 02:00:14

This will not work for me, as I believe there is a syntax error in your script.  This might be an example of things that work on one shell do not on another.


```
ATLAS-build/lib/Makefile will be changed.
'-shared' will be changed to '-G'
'-soname' will be changed to '-h'
'--whole-archive' will be changed to '-zallextract'
'--no-whole-archive' will be changed to '-zdefaultextract'
A copy of the original Makefile will be copied to Makefile.orig
./spkg-install-script: line 94: [: yes: unary operator expected
make[2]: Entering directory `/export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build/lib'
rm -f libatlas.so liblapack.so
```


This is line 94 of the script, which is causing the problem. 


```
  if [ $SAGE64 ="yes" ]; then 
```


I believe there should be a space after the '=' sign. 

I'd make a couple of other points tests in general, I've gleaned from studying the shell more, and from things from comp.unix.shell. 

 * It is better to test for "x$SAGE64" = xyes, as some shells have problems if SAGE64 is not defined. Adding an 'x' or anything else you fancy, will avoid that possibility, though 'x' is commonly used, so I would stick to a lower case x. That problem is not true of modern versions of bash, but its a good habit to get into, as then your scripts will work on any shell. 
 * It is desirable to quote "x$SAGE64" as potentially SAGE64 might be set to something with spaces in it. I know in this case, there unlikely to be spaces, but you don't know if someone has set it correctly or not. 

Hence the following is the safest test sort of test, and does not contain any unnecessary quotes. Quoting xNO will not hurt, but it is unnecessary as you know xNO will have no spaces, but you don't know that about FOOBAR.


``` 
             if [ "x$FOOBAR" = xNO ]; then
```


I leave you to convert it to what is needed here. Otherwise I become an author and can't review it!

I would also 
 * Report this upstream, and add to the trac ticket the URL of the ticket. Currently it is set to N/A which is clearly not true. 
 * Stick a note in the spkg-install saying why the change is made. i.e. the original flag is not valid. -64 is needed to build 64-bit, or something like that. 
 * I would echo a quick statement like I did before when changing flags, like I did before. 


``` 
'-shared' will be changed to '-G'
```


 * You are using a temporary variable of 'makefile' while editing 'Make.inc' I think that is unwise, and I know I was guilty of it above, but 'makefile' has some significance, and you could overwrite such a file if it existed. 

Better would be 


```
sed 's/-melf_x86_64/-64/g' Make.inc > Make.inc.tmp
```


or perhaps uses Make.inc.$$, which will create a file with the PID appended. 

Also, the description is inaccurate, as it says "As a workaround I changed -melf_x86_64 in -64 in Make.inc". I think you mean you changed it _'too_ -64. 

So with 

 * The syntax error removed
 * Description updated. 
 * Some other minor changes you might want to consider
 * Reported upstream, the URL posted. 
 * Change to "reported upstream" from N/A 
 * Revised patch attached. 

then I think this should be ok. But now, there is a syntax error so it will not build at all for me. 

Dave


---

Attachment

Mostly done as you wrote above.

Reported upstream:
[https://sourceforge.net/tracker/?func=detail&aid=2941029&group_id=23725&atid=379483](https://sourceforge.net/tracker/?func=detail&aid=2941029&group_id=23725&atid=379483)

Jaap


---

Comment by jsp created at 2010-01-27 15:02:55

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-01-28 14:04:38

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-01-28 14:04:38

I'm a bit worried about this one:


```
Platform detected to be 32 bits
```


Dave


---

Comment by drkirkby created at 2010-01-28 14:16:38

It also fails on my machine


```
make[1]: *** [atlas_run] Error 7
make[1]: Leaving directory `/export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build'
make: *** [IRun_comp] Error 2
Assertion failed: !system(ln), file /export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build/../src//CONFIG/src/config.c, line 125

OS configured as SunOS (2)

Assembly configured as GAS_x8632 (1)

Vector ISA Extension configured as  SSE3 (2,28)

Architecture configured as  Corei7 (16)

Clock rate configured as 3325Mhz
Cannot detect CPU throttling.
/bin/sh: line 1: 22300: Abort(coredump)
xconfig exited with 6
make -f Make.top build
make[1]: Entering directory `/export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build'
make[1]: Make.top: No such file or directory
make[1]: *** No rule to make target `Make.top'.  Stop.
make[1]: Leaving directory `/export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build'
make: *** [build] Error 2
Failed to build ATLAS.
Failed to build ATLAS.

real	0m3.065s
user	0m1.150s
sys	0m1.074s
sage: An error occurred while installing atlas-3.8.3.p11
```



---

Comment by jsp created at 2010-01-28 14:26:41

This is on your machine too:



```
chmod: cannot access `/export/home/jaap/sage_port/sage-4.3.1/local/lib/libptf77blas.a': No such file or directory
make[1]: [install_lib] Error 1 (ignored)
make[1]: Leaving directory `/export/home/jaap/sage_port/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build'
Deleting liblapack.so on Solaris due to bug in numpy/scipy

real    8m49.450s
user    7m35.780s
sys     1m0.353s
Successfully installed atlas-3.8.3.p11

```



What's wrong?

Jaap


---

Comment by jsp created at 2010-02-05 14:56:05

Changing status from needs_work to needs_review.


---

Comment by jsp created at 2010-02-05 14:56:05

Dave, Did you try again? Still no reaction from upstream.

Jaap


---

Comment by drkirkby created at 2010-02-05 17:25:57

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-02-05 17:25:57

Given
 * I found -m64 fixed the problem on the command line, and 
 * you have proven it works on my machine

I am going to give this is a positive review.


---

Comment by mpatel created at 2010-02-10 17:37:09

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-02-10 17:37:09

Sage 4.3.2 includes `atlas-3.8.3.p11.spkg`.  Should the package here be `p12`?


---

Comment by jsp created at 2010-02-10 19:39:30

Replying to [comment:12 mpatel]:
> Sage 4.3.2 includes `atlas-3.8.3.p11.spkg`.  Should the package here be `p12`?


Maybe now, but not on the moment I wrote the patch!

There is a real danger that tickets with positive review are not merged for a long time and bitrot.

Jaap


---

Comment by mpatel created at 2010-02-10 19:51:35

I think I've merged all the other Solaris-related tickets at {32} into a candidate 4.3.3.alpha0.


---

Comment by jsp created at 2010-02-10 20:30:26

Replying to [comment:14 mpatel]:
> I think I've merged all the other Solaris-related tickets at {32} into a candidate 4.3.3.alpha0.

Look at 'porting' to see some more!

Jaap


---

Comment by mpatel created at 2010-02-10 22:58:09

Yes, I've already those.


---

Attachment

Updated patch


---

Comment by jsp created at 2010-02-22 21:45:14

Changing status from needs_work to needs_review.


---

Comment by jsp created at 2010-02-22 21:45:14

Rebased and increased patch level. New spkg:

[http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p12.spkg](http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p12.spkg)



```
make[1]: Leaving directory `/export/home/jaap/sage_port/sage-4.3.2.alpha1/spkg/build/atlas-3.8.3.p12/ATLAS-build'
Deleting liblapack.so on Solaris due to bug in numpy/scipy

real    9m5.693s
user    7m45.589s
sys     1m3.860s
Successfully installed atlas-3.8.3.p12
You can safely delete the temporary build directory
/export/home/jaap/sage_port/sage-4.3.2.alpha1/spkg/build/atlas-3.8.3.p12
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing atlas-3.8.3.p12.spkg
-bash-3.2$ file local/lib/libatlas.*
local/lib/libatlas.a:   current ar archive, not a dynamic executable or shared object
local/lib/libatlas.so:  ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available

```


Jaap


---

Comment by drkirkby created at 2010-02-22 22:07:19

That looks good. It would be nice to find out exactly what -melf_x86_64 is supposed to do, but on a practical level, this allows ATLAS to build on OpenSolaris. Some more changees may be needed once Sage builds and we can run the doctests. But at least this builds, only effects Solaris and allows progress to be made.


---

Comment by drkirkby created at 2010-02-22 22:07:19

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-02 23:08:09

Resolution: fixed


---

Comment by mvngu created at 2010-03-02 23:08:09

Merged [atlas-3.8.3.p12.spkg](http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p12.spkg) in the standard spkg repository.
