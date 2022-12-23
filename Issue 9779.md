# Issue 9779: Missing symbolic link for liblapack.a, so SAGE_ATLAS_LIB does not work on Solaris.

Issue created by migration from https://trac.sagemath.org/ticket/9780

Original creator: drkirkby

Original creation time: 2010-08-22 07:37:42

Assignee: AlexGhitza

CC:  jhpalmieri jsp mpatel

As noted at #9356, a change which was made to ensure `SAGE_ATLAS_LIB` worked on Solaris, is not a complete solution. On Solaris, no shared library `liblapack.so` is created, as for reasons unknown, this causes problems. Hence the static library liblapack.a needs to be available to programs using ATLAS on Solaris. This means an extra symbolic link needs to be created. I think adding 


```
os.system(' ln -sf ' + ATLAS_LIB + '/lib/liblapack.a '  + SAGE_LOCAL_LIB+'/liblapack.a')
```


will work, though this remains to be tested. 

Dave


---

Comment by drkirkby created at 2010-08-22 11:51:09

Changing component from algebra to solaris.


---

Comment by drkirkby created at 2010-08-22 11:51:09

Changing assignee from AlexGhitza to drkirkby.


---

Comment by mpatel created at 2010-09-06 21:21:03

From the end of `spkg/logs/atlas-3.8.3.p14.log` on sage.math:

```
ld -L/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3/local/lib -shared -soname liblapack.so -o liblapack.so --whole-archive liblapack.a --no-whole-archive -lc -lm -lgfortran
ld: cannot find -lgfortran
ld -L/mnt/usb1/scratch/mpatel/tmp/sage-4.5.3/local/lib -shared -soname libf77blas.so -o libf77blas.so --whole-archive libf77blas.a --no-whole-archive -lc -lm -lgfortran
ld: cannot find -lgfortran
```

In particular, `liblapack.so` and `libf77blas.so` aren't made.  Is this relevant here?  Running `ln -s libgfortran.so.2 libgfortran.so` in `SAGE_LOCAL/lib` and reinstalling ATLAS appears to help (cf. [comment:ticket:9356:5 comment 5] and [comment:ticket:9356:7 comment 7] at #9356).


---

Comment by drkirkby created at 2010-09-06 21:28:42

Replying to [comment:3 mpatel]:

> In particular, `liblapack.so` and `libf77blas.so` aren't made.  Is this relevant here?  Running `ln -s libgfortran.so.2 libgfortran.so` in `SAGE_LOCAL/lib` and reinstalling ATLAS appears to help (cf. [comment:ticket:9356:5 comment 5] and [comment:ticket:9356:7 comment 7] at #9356).

I think it proves we don't need the shared libraries myself. Note they are not built on OS X at all - see the badly name file `make_correct_shared.sh`

But more to the point, it's unwise to test for them before permitting the code associated with  `SAGE_ATLAS_LIB` to work. At the minute, that code tests for the 4 shared libraries on Linux, and 3 on Solaris. That seems to be rather flawed given only two are reliably built on Linux. Sure we might be able to get them to build, but that's far from obvious how to do that best. Just ignoring them seems simpler to me. 

Dave


---

Comment by drkirkby created at 2010-09-06 22:27:25

On OpenSolaris at least, I can build sage-4.5.3.rc0 using only links to static libraries on a previous build (sage-4.5.3.alpha2). In other words, I set {{{SAGE_ATLAS_LIB}} with a modified version of the ATLAS package, which only made links to the static libraries. 


```
lrwxrwxrwx   1 drkirkby staff         62 Sep  6 21:52 libatlas.a -> /export/home/drkirkby/6/sage-4.5.3.alpha2/local/lib/libatlas.a
lrwxrwxrwx   1 drkirkby staff         62 Sep  6 21:52 libcblas.a -> /export/home/drkirkby/6/sage-4.5.3.alpha2/local/lib/libcblas.a
lrwxrwxrwx   1 drkirkby staff         64 Sep  6 21:52 libf77blas.a -> /export/home/drkirkby/6/sage-4.5.3.alpha2/local/lib/libf77blas.a
lrwxrwxrwx   1 drkirkby staff         63 Sep  6 21:52 liblapack.a -> /export/home/drkirkby/6/sage-4.5.3.alpha2/local/lib/liblapack.a
```


That passed all doctests:


```
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 1825.6 seconds
drkirkby@hawk:~/noatlas/sage-4.5.3.rc0$ ./sage -gap
```


A good sign, but I'll test that package on Linux too. 

Dave


---

Comment by drkirkby created at 2010-09-06 23:14:16

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-09-07 01:14:29

One small correction: on OS X, I don't think anything gets installed: the system's ATLAS gets used instead.  Notice these lines in `spkg-install-script`:

```
if [ `uname` = "Darwin" ]; then
    exit 0
fi
```

These happen before the call to `make_correct_shared.sh`, so any lines in the latter script actually have no effect on Darwin, as far as I can tell.


---

Comment by drkirkby created at 2010-09-07 07:28:32

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-09-07 07:28:32

Replying to [comment:7 jhpalmieri]:
> One small correction: on OS X, I don't think anything gets installed: the system's ATLAS gets used instead.  Notice these lines in `spkg-install-script`:
> {{{
> if [ `uname` = "Darwin" ]; then
>     exit 0
> fi
> }}}
> These happen before the call to `make_correct_shared.sh`, so any lines in the latter script actually have no effect on Darwin, as far as I can tell.

Thank you John,

In view of this, I'll delete those lines related to OS X in `make_correct_shared.sh`, as they only add confusion. 


The version I created that linked to the static libraries in /ATLAS on Solaris 10 SPARC (`t2.math`) 


```
kirkby@t2:32 ~/t2/32/sage-4.5.3.rc0/local/lib$ ls -l | grep ATLAS
lrwxrwxrwx   1 kirkby   1093          21 Sep  6 16:56 libatlas.a -> /ATLAS/lib/libatlas.a
lrwxrwxrwx   1 kirkby   1093          21 Sep  6 16:56 libcblas.a -> /ATLAS/lib/libcblas.a
lrwxrwxrwx   1 kirkby   1093          23 Sep  6 16:56 libf77blas.a -> /ATLAS/lib/libf77blas.a
lrwxrwxrwx   1 kirkby   1093          22 Sep  6 16:56 liblapack.a -> /ATLAS/lib/liblapack.a
```


failed one doc test


```
The following tests failed:

        sage -t  -long devel/sage/sage/parallel/decorate.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 11326.4 seconds
```


but the system had run out of swap space, as shown in the system logs. I added some swap space, then the test passed:


```
kirkby@t2:32 ~/t2/32/sage-4.5.3.rc0$ ./sage -t  -long devel/sage/sage/parallel/decorate.py
sage -t -long "devel/sage/sage/parallel/decorate.py"        
         [39.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 39.8 seconds
```


It also built OK on Linux (`sage.math`), though I've not run the doctests on that yet. 

I'm marking this as "needs work" as I want to remove the erroneous information about OS X that exists in  `make_correct_shared.sh` and probably in `SPKG.txt too`. 

It's very tempting to rename `make_correct_shared.sh` to something like `occasionally_make_correct_shared.sh` !!

Dave


---

Comment by drkirkby created at 2010-09-07 13:16:52

Changing status from needs_work to positive_review.


---

Comment by drkirkby created at 2010-09-07 13:16:52

Here's an updated package, 

http://boxen.math.washington.edu/home/kirkby/patches/atlas-3.8.3.p15.spkg

which uses the 4 static libraries, but add links to the shared ones too. If they don't exist, nothing is lost. This ensures the environment is the same as would be if SAGE_ATLAS_LIB was not used, and ATLAS build from scratch. 

I've tested this on sage.math, my OpenSolaris machine, and it seems to be going OK on t2.math. 

Dave


---

Comment by drkirkby created at 2010-09-07 13:57:05

I set this to "positive review" by mistake - it was supposed to be "needs review" !!


---

Comment by drkirkby created at 2010-09-07 13:57:05

Changing status from positive_review to needs_info.


---

Comment by drkirkby created at 2010-09-07 13:57:14

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-09-08 00:17:58

Check for static libraries only so SAGE_ATLAS_LIB is more relieable


---

Attachment

Overall the changes look sensible.

A few comments about `system_atlas.py`.  In line 15:

```
has_atlas = os.path.exists(ATLAS_LIB+'/lib//libatlas.a') 
```

should the double slash be a single one?  In the comments on lines 44-51 of the same file, there are a few typos ("relieably" and "Buidling"), but this is not very important.  In lines 64-72, there is an old error: as you can see from the code, `SAGE_ATLAS_LIB` should be a directory which contains subdirectories "lib" and "include/atlas".  In particular, it should not be set to the "parent directory of liblapack.a, libcblas.a, libatlas.a and libf77blas.a".  (I probably should have fixed this in #9356.)  In the [installation guide](http://sagemath.org/doc/installation/source.html#environment-variables), we documented this as saying "the parent directory of your ATLAS installation: it should have a subdirectory lib containing the files libatlas.so, liblapack.so, libcblas.so, and libf77blas.so, and it should have a subdirectory include/atlas/ containing header files." As far as I know, that is accurate, and we might use similar language here.  Oh, and I guess we should change the text in the installation guide from *.so to *.a...  I can add a patch for that if you want.

Finally, for testing this, I'm not sure I have access to a system with a genuine ATLAS installation.  I can use an ATLAS build from another version of Sage, but should we test this with other ATLAS installations as well?  I'll try it out on t2 and one or two skynet machines.


---

Comment by drkirkby created at 2010-09-08 21:20:28

Replying to [comment:12 jhpalmieri]:
> Overall the changes look sensible.
> 
> A few comments about `system_atlas.py`.  In line 15:
> {{{
> has_atlas = os.path.exists(ATLAS_LIB+'/lib//libatlas.a') 
> }}}
> should the double slash be a single one?  

Single

> In the comments on lines 44-51 of the same file, there are a few typos ("relieably" and "Buidling"), but this is not very important.  

But I can fix them. 

> In lines 64-72, there is an old error: as you can see from the code, `SAGE_ATLAS_LIB` should be a directory which contains subdirectories "lib" and "include/atlas".  

IMHO it is badly named. It should have been called SAGE_ATLAS. It is very unconventional. Take a look for example at gcc's configure options:


```
  --with-gmp=PATH         specify prefix directory for the installed GMP package.
                          Equivalent to --with-gmp-include=PATH/include
                          plus --with-gmp-lib=PATH/lib
  --with-gmp-include=PATH specify directory for installed GMP include files
  --with-gmp-lib=PATH     specify directory for the installed GMP library
```


The `LIB` in `SAGE_ATLAS_LIB` is confusing, when there are include files too. 

> In particular, it should not be set to the "parent directory of liblapack.a, libcblas.a, libatlas.a and libf77blas.a".  (I probably should have fixed this in #9356.)  In the [installation guide](http://sagemath.org/doc/installation/source.html#environment-variables), we documented this as saying "the parent directory of your ATLAS installation: it should have a subdirectory lib containing the files libatlas.so, liblapack.so, libcblas.so, and libf77blas.so, and it should have a subdirectory include/atlas/ containing header files." As far as I know, that is accurate, and we might use similar language here.  Oh, and I guess we should change the text in the installation guide from *.so to *.a...  I can add a patch for that if you want.

I think we have a difference of opinion about what a "parent" directory is. IMHO, if we have:


```
/usr/local/ATLAS/lib
/usr/local/ATLAS/include
```


Then the parent directory of the ATLAS installation is `/usr/local`. In other words, `SAGE_ATLAS_LIB` should be the parent directory of `/usr/local/ATLAS/lib`. I think the definition at http://en.wikipedia.org/wiki/Parent_directory is reasonable. 

I thought the wording was confusing, so thought I'd try to clarify it. Obviously you think I've made it more confusing. 

Perhaps it needs an example - the one above might be reasonable. Perhaps remove the word "parent", and just do it more by example. 

Perhaps you have a better idea. 

> Finally, for testing this, I'm not sure I have access to a system with a genuine ATLAS installation.  I can use an ATLAS build from another version of Sage, but should we test this with other ATLAS installations as well?  I'll try it out on t2 and one or two skynet machines.

I've not got access to any machine with a "genuine" ATLAS installation. Does such a thing exist? It's not really a standard package. I think given the nature of ATLAS, which (Automatically Tuned Linear Algebra System) one really should build it from source on the machine so it is tuned properly. So even if you can find a ATLAS library for Debian/Redhat etc, it is unlikely to be optimal for your hardware. 

The only other thing I have access to is Mathematica which uses ATLAS and has the 4 shared libraries. Unfortunately, since Mathematica is 64-bit, and we can only at this point build Sage reliably 32-bit, that's not an option. I might have an old version of Mathematica I could try, but that's a lot of messing around - installing the software just to try the library. 

I don't think it's unreasonable for someone to build Sage once with ATLAS, then at a later date use that install. 

Dave


---

Comment by jhpalmieri created at 2010-09-08 21:31:34

I mostly agree with what you're saying about parent directories, but "the parent directory of liblapack.a, libcblas.a, libatlas.a and libf77blas.a" sounds like it should be the directory containing those files (e.g. /usr/local/ATLAS/lib), not the parent directory of that one (/usr/local/ATLAS/).  Maybe it could be "the parent directory of the directory containing liblapack.a, libcblas.a, libatlas.a and libf77blas.a"?

(The wikipedia reference only discusses the parent directory of another directory, not of a file.  So what is the parent directory of /usr/local/ATLAS/lib/liblapack.a?)

> I don't think it's unreasonable for someone to build Sage once with ATLAS, then at a later date use that install.

That's what I'm trying right now with some skynet machines: taurus and eno (two linux boxes), mark (solaris on sparc) and fulvia (solaris on x86).


---

Comment by mpatel created at 2010-09-08 22:47:08

There's a [potentially relevant question](http://ask.sagemath.org/question/107/building-atlas) about `SAGE_ATLAS_LIB` at [AskSage](http://ask.sagemath.org/).


---

Comment by jhpalmieri created at 2010-09-09 05:20:56

On mark, I get the message

```
system_atlas.py:6: DeprecationWarning: os.popen2 is deprecated.  Use the subprocess module.
  fortran = os.popen2(os.environ['SAGE_LOCAL']+'/bin/'+'which_fortran')[1].read()
system_atlas.py:23: DeprecationWarning: os.popen2 is deprecated.  Use the subprocess module.
  s_gfortran = os.popen2('readelf -s ' +ATLAS_LIB+'/lib/libf77blas.so | grep gfortran')[1].read()
/bin/sh: readelf: not found
system_atlas.py:24: DeprecationWarning: os.popen2 is deprecated.  Use the subprocess module.
  s_g95 = os.popen2('readelf -s ' + ATLAS_LIB + '/lib/libf77blas.so | grep g95')[1].read()
/bin/sh: readelf: not found
```

I'm not worried about the deprecation messages, but what about `/bin/sh: readelf: not found`?  Is that important?


---

Comment by drkirkby created at 2010-09-09 08:37:08

Replying to [comment:16 jhpalmieri]:
> I'm not worried about the deprecation messages, but what about `/bin/sh: readelf: not found`?  Is that important?

I did notice that about `readelf`. It's basically non-portable code. No such command exists as part of the POSIX Unix standard. It appears to be part of the GNU binutils package. 

IMHO, the section:


```
            s_gfortran = os.popen2('readelf -s ' +ATLAS_LIB+'/lib/libf77blas.so | grep gfortran')[1].read()
            s_g95 = os.popen2('readelf -s ' + ATLAS_LIB + '/lib/libf77blas.so | grep g95')[1].read()

            if s_gfortran !='' and not fortran.startswith('gfortran'):
                print "Symbols in lib77blas indicate it was build with gfortran \n"
                print "However SAGE is using a different fortran compiler \n"
                print "If you wish to use this blas library, make sure SAGE_FORTRAN points \n"
                print "to a fortran compiler compatible with this library. \n"
                sys.exit(2)

            if s_g95 !='' and not fortran.startswith('g95'):
                print "Symbols in lib77blas indicate it was build with g95 \n"
                print "However SAGE is using a different fortran compiler \n"
                print "If you wish to use this blas library, make sure SAGE_FORTRAN points \n"
                print "to a fortran compiler compatible with this library. \n"
                sys.exit(2)
```


is of *extremely* limited value. It is certainly non-portable and whilst there was a time when `g95` was popular and someone might have compiled ATLAS with it, those days are long since passed. William said some time ago we can remove the g95 binaries from the fortran package. 

In any case, it is testing on a shared library `libf77blas.so` which often fails to build for people on various Linux distributions. I think removing that whole section would save a few CPU cycles and a few bytes of download. 

The failure is harmless in that if `readelf` does not exist, it will never find the symbols this bit of code tests for, so both `s_gfortran` and `s_g95` remain empty. 

It is worth bearing in mind is that this ATLAS code is never installed on Cygwin or OS X. So this code will only ever be executed on Linux, Solaris and rarer Unix systems like HP-UX, AIX etc. Only Linux systems will probably have the {{{readelf}} command, though it could be installed on Solaris, AIX, HP-UX etc. 

There are several options, ranked in order of my preference. 

 1. Remove that section of code above.
 2. Ignore it, since the error message is harmless. 
 3. Test first if `readelf` exists. 
 4. Make GNU binutils a perquisite for building Sage - i.e. add it as a  standard package. 


Dave


---

Comment by drkirkby created at 2010-09-09 08:37:08

Changing status from needs_review to needs_info.


---

Comment by jhpalmieri created at 2010-09-09 21:18:32

Okay, pointing SAGE_ATLAS_LIB to the "local" directory of a previous Sage installation works for me on several solaris machines (t2 and mark2: sparc; and fulvia: x86).  It also works for me on several linux machines (taurus and eno).  So I'm happy with it.  I would have liked to test it on some linux machine with a separately installed ATLAS, but it's not a perfect world.

As far as the readelf problem goes, I think we can leave it as is.  It doesn't do any harm, after all.  My second choice would be to test whether readelf exists, or at least hide the error -- just changing os.popen2 to os.popen3 will do this, so that's easy.  If course, it might be better to test whether the command produced an error, like this:

```
sage: p = os.popen3('readelf -s ' +ATLAS_LIB+'/lib/libf77blas.so | grep gfortran')
sage: p[2].read()  # stderr, so the empty string if no error
'/bin/sh: readelf: command not found\n'
sage: p[1].read()  # stdout, so the output of the command
''
```

So we could change the code

```
            s_gfortran = os.popen2('readelf -s ' +ATLAS_LIB+'/lib/libf77blas.so | grep gfortran')[1].read()
            s_g95 = os.popen2('readelf -s ' + ATLAS_LIB + '/lib/libf77blas.so | grep g95')[1].read()
```

to the following (untested):

```
            proc_gfortran = os.popen3('readelf -s ' +ATLAS_LIB+'/lib/libf77blas.so | grep gfortran')
            proc_g95 = os.popen3('readelf -s ' +ATLAS_LIB+'/lib/libf77blas.so | grep g95')
            err = (len(proc_gfortran[2].read()) > 0) or (len(proc_g95[2].read()) > 0)

            s_gfortran = ''
            s_g95 = ''
	    if not err:  # readelf is present and ran without error
		s_gfortran = proc_gfortran[1].read()
                s_g95 = proc_g95[1].read()
```

Even better, we should rewrite it using the subprocess module, to avoid the deprecation messages.  If you think that's worthwhile, I could probably do it pretty quickly.  You would probably prefer it not written in python at all, but that's a bit more work...  Completely removing the code involves more analysis of what's going on: are there any systems which execute this code from the atlas spkg, have readelf, and also use g95?  If not, then we can get rid of it, but how sure can we be of that?

I think we've agreed before that a major upgrade to the atlas spkg is long overdue, and if we don't eliminate this code, we can add its removal to the list of things to change.  If you make a new spkg addressing [my comments above](http://trac.sagemath.org/sage_trac/ticket/9780#comment:12), maybe you could add a comment to SPKG.txt about this?


---

Comment by drkirkby created at 2010-09-14 23:06:31

Replying to [comment:18 jhpalmieri]:
> Okay, pointing SAGE_ATLAS_LIB to the "local" directory of a previous Sage installation works for me on several solaris machines (t2 and mark2: sparc; and fulvia: x86).  It also works for me on several linux machines (taurus and eno).  So I'm happy with it.  I would have liked to test it on some linux machine with a separately installed ATLAS, but it's not a perfect world.

Good, the basic code seems to work. 

> As far as the readelf problem goes, I think we can leave it as is. 

I felt that too. Especially since I think it can be removed. I believe it's a complete waste of time to be honest. I've left it for now though. I added a message that a warning was harmless. (For reasons I do not understand, the warning is printed *before* my message, despite the code to execute `readlef` is *after* my message.) 

I addressed the other issue you had about the parent directory. See if the following makes any more sense. I've actually printed the directory where the libraries are expected to be, based on the setting of SAGE_ATLAS_LIB. I've not committed the changes yet - let me know what you think. 


```
drkirkby@hawk:~$ export SAGE_ATLAS_LIB=/some/random/directory/for/atlas
```


now prints


```
Unable to find one of liblapack.a, libcblas.a, libatlas.a or libf77blas.a
in the directory /some/random/directory/for/atlas/lib
```


Just run 'hg diff' if you want to see what I changed. 

The package is at 

http://boxen.math.washington.edu/home/kirkby/patches/atlas-3.8.3.p15.spkg

Dave


---

Comment by jhpalmieri created at 2010-09-16 19:38:54

Okay, looks good to me.  Once you commit the changes and post the link to the new spkg, if you think it's ready (the ticket is still marked "needs info"), then you can change it to "positive review".


---

Comment by drkirkby created at 2010-09-16 21:22:56

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-09-16 21:27:45

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-09-16 21:27:45

Replying to [comment:20 jhpalmieri]:
> Okay, looks good to me.  Once you commit the changes and post the link to the new spkg, if you think it's ready (the ticket is still marked "needs info"), then you can change it to "positive review".

Thank you John,

Yes, I'm sure it's ready. I've committed the changes and updated the .spkg at 

http://boxen.math.washington.edu/home/kirkby/patches/atlas-3.8.3.p15.spkg

Dave 
 
 == To the release manager ==
Only the .spkg at 
http://boxen.math.washington.edu/home/kirkby/patches/atlas-3.8.3.p15.spkg

needs to be added to Sage  - there are no patches to apply to it, the Sage library or anywhere else. 

Dave


---

Comment by mpatel created at 2010-09-29 08:40:19

Resolution: fixed


---

Comment by mpatel created at 2010-09-30 01:16:37

Just a clarification: I didn't merge p15 here into 4.6.alpha2, because p16 at #9952 is newer.  In this case, it didn't seem appropriate to close this ticket as a "duplicate."
