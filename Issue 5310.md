# Issue 5310: addition to Sage for Msieve factoring program

Issue created by migration from https://trac.sagemath.org/ticket/5310

Original creator: jblakeslee

Original creation time: 2009-02-19 04:25:19

Assignee: mabshoff

CC:  zimmerma wstein boothby leif jpflori

Keywords: msieve, factorization

This addition of Msieve will hopefully enhance Sage's Integer Factorization ability for all integers of a reasonable size, and provide the opportunity for users to utilize the Number Field Sieve.

spkg located:  

http://309codesign.com/code/

An explanation of Msieve from its documentation:
"There are plenty of algorithms for performing integer factorization. 
The Msieve library implements most of them from scratch, and relies on
optional external libraries for the rest of them. Trial division and
Pollard Rho is used on all inputs; if the result is less than 25 digits 
in size, tiny custom routines do the factoring. For larger numbers, the code
switches to the GMP-ECM library and runs the P-1, P+1 and ECM algorithms,
expending a user-configurable amount of effort to do so. If these do not 
completely factor the input number, the library switches to the heavy  
artillery. Unless told otherwise, Msieve runs the self-initializing quadratic
sieve algorithm, and if this doesn't factor the input number then you've
found a library problem. If you know what you're doing, Msieve also contains
a complete implementation of the number field sieve, that has helped complete
some of the largest public factorization efforts known."
and
"To be as fast as possible. I claim (without proof) that for
          completely factoring general inputs between 40 and 100 digits
          in size, Msieve is faster than any other code implementing any
          other algorithm."


---

Attachment


---

Comment by was created at 2009-02-19 23:31:44

I tried to build this on OS X Intel and immediately got this error, which suggests a bug in the spkg-install script itself.


```
gcc version 4.0.1 (Apple Inc. build 5465)
****************************************************
./spkg-install: line 5: [: missing `]'
./spkg-install: line 5: i386: command not found
pick a target:
x86       32-bit Intel/AMD systems (required if gcc used)
x86_64    64-bit Intel/AMD systems (required if gcc used)
generic   portable code
also add 'ECM=1' if GMP-ECM is available
Error building MSieve -- no file msieve was produced.

real	0m0.084s
user	0m0.011s
sys	0m0.022s
sage: An error occurred while installing msieve-1.39
```



---

Comment by was created at 2009-02-19 23:34:04

The above error also occurs on all linux systems too.


---

Comment by jblakeslee created at 2009-02-20 05:24:20

I apologize for that.  Please try once again.  I have place the updated spkg in the same location.

http://309codesign.com/code/msieve-1.39.spkg


---

Comment by mabshoff created at 2009-02-20 08:01:04

This is too late for Sage 3.3, so bumped to 3.4.1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 09:49:37

For mpQS vs. msieve Bill Hart has some numbers: 

```
Anything over about 75 digits will be much slower on mpQS than on 
msieve, due to the fact that the latter implements the double large 
prime variant and I don't. But the time for the second factorization 
is 15min 35s in mpQS. 

Here are some other times: 

msieve mpQS 

2891670903938774131753: 
0.010s 0.000s 

7223934149780053552120237: 
0.020s 0.020s 

10890325463531930685071186191: 
0.070s 0.020s 

22746696815551279204773065179537: 
0.100s 0.040s 

34714945933810757311137622885134169: 
0.110s 0.050s 

10173256651176584336392947473501127227: 
0.130s 0.080s 

13018279488865181129955874562185134688337: 
0.200s 0.090s 

22301677236991560444759885102875349454660651: 
0.230s 0.210s 

8941543217242472708029937221739551760158967009: 
0.340s 0.280s 

6399059753136044767573853384689913264328520902553: 
0.570s 1.740s 

25506563753254047681462924229892337031031187330409537: 
1.050s 1.250s 

37987772559424160043450717911696894399547208398069213931: 
1.930s 2.520s 

So for smaller numbers, mpQS is faster than msieve. I just haven't 
worked on speeding it up for numbers of 75 digits and more. 
```


Cheers,

Michael


---

Comment by was created at 2009-04-12 06:37:54

I tried on sage.math (our x86_64 server with ubuntu 8.04.LTS):

```
****************************************************
Host system
uname -a:
Linux sage.math.washington.edu 2.6.24-23-server #1 SMP Mon Jan 26 01:36:05 UTC 2009 x86_64 GNU/Linux
****************************************************
****************************************************
GCC Version
gcc -v
Using built-in specs.
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.2 --program-suffix=-4.2 --enable-clocale=gnu --enable-libstdcxx-debug --enable-objc-gc --enable-mpfr --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu3)
****************************************************
gcc -D_FILE_OFFSET_BITS=64 -O3 -fomit-frame-pointer -march=athlon-xp -DNDEBUG  -Wall -W -Wconversion -Iinclude -Ignfs/poly -c -o common/lanczos/lanczos.o common/lanczos/lanczos.c
common/lanczos/lanczos.c:1: error: CPU you selected does not support x86-64 instruction set
common/lanczos/lanczos.c:1: error: CPU you selected does not support x86-64 instruction set
make: *** [common/lanczos/lanczos.o] Error 1
Error building M-Sieve

real    0m0.040s
user    0m0.010s
sys     0m0.010s
sage: An error occurred while installing msieve-1.39
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /scratch/wstein/build/sage-3.4.1.rc2-ref2/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/scratch/wstein/build/sage-3.4.1.rc2-ref2/spkg/build/msieve-1.39 and type 'make'.
Instead type "/scratch/wstein/build/sage-3.4.1.rc2-ref2/sage -sh"
in order to set all environment variables correctly, then cd to
/scratch/wstein/build/sage-3.4.1.rc2-ref2/spkg/build/msieve-1.39
(When you are done debugging, you can type "exit" to leave the
subshell.)
wstein@sage:~/build/sage-3.4.1.rc2-ref2$ 
```



I also tried building on 32-bit OS X 10.5 (my laptop):

```
Wall -W -Wconversion -Iinclude -Ignfs/poly -c -o common/ap.o common/ap.c
common/ap.c: In function ‘ap_mul’:
common/ap.c:339: error: can't find a register in class ‘GENERAL_REGS’ while reloading ‘asm’
common/ap.c:339: error: can't find a register in class ‘GENERAL_REGS’ while reloading ‘asm’
common/ap.c:339: error: can't find a register in class ‘GENERAL_REGS’ while reloading ‘asm’
common/ap.c:339: error: can't find a register in class ‘GENERAL_REGS’ while reloading ‘asm’
make: *** [common/ap.o] Error 1
Error building M-Sieve

real	0m5.432s
user	0m1.786s
sys	0m0.348s
sage: An error occurred while installing msieve-1.39
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/wstein/build/sage-3.4.1.rc2/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/Users/wstein/build/sage-3.4.1.rc2/spkg/build/msieve-1.39 and type 'make'.
Instead type "/Users/wstein/build/sage-3.4.1.rc2/sage -sh"
in order to set all environment variables correctly, then cd to
/Users/wstein/build/sage-3.4.1.rc2/spkg/build/msieve-1.39
(When you are done debugging, you can type "exit" to leave the
subshell.)
teragon:~ wstein$ 
```


So I can't build this on either of my main devel machines, so it's hard to go anywhere with.


---

Comment by zimmerma created at 2009-04-17 12:51:16

> I tried on sage.math (our x86_64 server with ubuntu 8.04.LTS): [...]

William, you need to disable manually the default -march=athlon-xp in Makefile.


---

Comment by jblakeslee created at 2009-04-17 16:03:38

Replying to [comment:9 zimmerma]:
> > I tried on sage.math (our x86_64 server with ubuntu 8.04.LTS): [...]
> 
> William, you need to disable manually the default -march=athlon-xp in Makefile.

That change has been added to the .spkg and should now work on x86_64 without having to mess with the Makefile.  The new .spkg hopefully works for intel-based Macs, too, but I haven't had a chance to try it yet. 
Thanks.


---

Comment by jblakeslee created at 2009-04-20 05:56:30

Replying to [comment:10 jblakeslee]:
> Replying to [comment:9 zimmerma]:
> > > I tried on sage.math (our x86_64 server with ubuntu 8.04.LTS): [...]
> > 
> > William, you need to disable manually the default -march=athlon-xp in Makefile.
> 
> That change has been added to the .spkg and should now work on x86_64 without having to mess with the Makefile.  The new .spkg hopefully works for intel-based Macs, too, but I haven't had a chance to try it yet. 
> Thanks.

That version didn't work on the Intel Mac I tested, so updated again, and now does compile for me.


---

Comment by boothby created at 2009-10-01 05:10:02

jblakeslee, the url doesn't appear to be correct.  The file msieve-1.39.spkg appears to be missing, and msieve-1.38.spkg in that directory is broken.  Please upload again.


---

Comment by jblakeslee created at 2009-10-03 04:36:11

Replying to [comment:12 boothby]:
> jblakeslee, the url doesn't appear to be correct.  The file msieve-1.39.spkg appears to be missing, and msieve-1.38.spkg in that directory is broken.  Please upload again.

Please use this url:
http://309codesign.com/code/msieve-1.38.spkg

Please try again.  It is working for me with the following command:
sage -i msieve-1.38.spkg

If it fails again can you give os type and error info.  Thank you.


---

Attachment

I attached a patch for the msieve interface updated to version 1.47.

Someone has to check whether msieve can be compiled on every relevant system and if necessary update the spkg-file.
It works on x86_64.


---

Comment by aapitzsch created at 2010-10-28 14:52:38

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-10-28 21:56:46

Remove assignee mabshoff.


---

Attachment


---

Attachment


---

Comment by drkirkby created at 2011-04-27 20:57:50

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2011-04-27 20:57:50

Replying to [comment:14 jblakeslee]:
> Please use this url:
> http://309codesign.com/code/msieve-1.38.spkg

That link, which you posted 19 months ago, is not valid


```
drkirkby@hawk:~/sage-4.7.alpha5/spkg/standard$ wget http://309codesign.com/code/msieve-1.39.spkg
--2011-04-27 21:55:45--  http://309codesign.com/code/msieve-1.39.spkg
Resolving 309codesign.com (309codesign.com)... 74.220.215.62
Connecting to 309codesign.com (309codesign.com)|74.220.215.62|:80... connected.
HTTP request sent, awaiting response... 404 Not Found
2011-04-27 21:55:56 ERROR 404: Not Found.
```



---

Comment by jblakeslee created at 2011-05-03 02:48:02

Replying to [comment:18 drkirkby]:
> Replying to [comment:14 jblakeslee]:
> > Please use this url:
> > http://309codesign.com/code/msieve-1.38.spkg
> 
> That link, which you posted 19 months ago, is not valid
> 

Please use the msieve-1.48.spkg and patch, that are added by aapitzsch, just before your post, since I have stopped updating my link.  I had good luck with his msieve-1.47.spkg.
Thank you.


---

Comment by leif created at 2011-10-31 18:32:26

Ping.


---

Comment by zimmerma created at 2011-11-01 09:33:43

see also #6232


---

Attachment


---

Comment by aapitzsch created at 2011-11-01 18:40:46

Changing status from needs_work to needs_review.


---

Comment by aapitzsch created at 2011-11-01 18:40:46

Here is an updated version of msieve.


---

Comment by leif created at 2011-11-01 19:27:52

`EXAMPLE:` and `EXAMPLES:` should have a double-colon (`::`).

The indentation of the results in the first examples block looks strange; they should line up with the `sage:` prompt.

Haven't tested, but one should make sure that all temporary files are created in or below `SAGE_TMP` (or `SAGE_TMPDIR`?) [at least] during doctesting, since they should also pass if the user doesn't have write access on the Sage installation tree.

(An ordinary user should of course also be able to just _use_ the code without permission issues.)


---

Comment by leif created at 2011-11-01 19:42:10

P.S.: For inclusion into Sage, an spkg usually has to get an optional one first; then there should be a poll on sage-devel to make it a standard spkg.  The code should perhaps take care of that, i.e., not assume that `msieve` is installed, and print a meaningful error message (instructing the user how to install the spkg) in case it isn't.


---

Comment by aapitzsch created at 2011-11-01 21:11:54

Replying to [comment:23 leif]:
> `EXAMPLE:` and `EXAMPLES:` should have a double-colon (`::`).
> 
> The indentation of the results in the first examples block looks strange; they should line up with the `sage:` prompt.
> 
Fixed this.

> Haven't tested, but one should make sure that all temporary files are created in or below `SAGE_TMP` (or `SAGE_TMPDIR`?) [at least] during doctesting, since they should also pass if the user doesn't have write access on the Sage installation tree.
> 
> (An ordinary user should of course also be able to just _use_ the code without permission issues.)

More or less I copied the TMPDIR part from qsieve.py , so this shouldn't be a problem.

Examples are marked as optional now and in case msieve isn't installed there is warning.

There was already a discussion about adding msieve in 2009.
See http://groups.google.com/group/sage-devel/browse_thread/thread/91f1ecf4dca5511d/d68c74a19b741255


---

Comment by leif created at 2011-11-02 00:04:42

The spkg certainly needs some work, which I'll do later.

The patch to the Sage library could be tweaked w.r.t. markup (e.g. identifiers and program names should be typeset monospaced, i.e. ```parameter```, ```True```, ```msieve``` etc.).  I'll _perhaps_ make a reviewer patch as well.


---

Comment by leif created at 2011-11-02 00:18:17

Replying to [comment:25 aapitzsch]:
> [...] in case msieve isn't installed there is warning.

How about printing that message and raising `NotImplementedError` (or `RuntimeError`)?

That way other (higher-level) functions can call `msieve()` and catch these exceptions.

We could also put the "warning" into the message of the exception, such that the output isn't messed up by just trying to call `msieve()` (from other parts of Sage).




_SAGE_ should be _Sage_ btw.




The `TMPDIR` environment variable must not be modified globally; if there's no other way to tell `msieve` where it should put temporary files, a modified environment has to be passed to `msieve`.


---

Attachment

Patch updated.

Replying to [comment:27 leif]:
> Replying to [comment:25 aapitzsch]:
> > [...] in case msieve isn't installed there is warning.
> 
> How about printing that message and raising `NotImplementedError` (or `RuntimeError`)?
> 
Now `NotImplementedError` is raised.
> 
> _SAGE_ should be _Sage_ btw.
> 
Done.
> 
> The `TMPDIR` environment variable must not be modified globally; if there's no other way to tell `msieve` where it should put temporary files, a modified environment has to be passed to `msieve`.

Fixed.


---

Comment by zimmerma created at 2011-12-21 09:51:41

I tried installing the spkg with Sage 4.7.2 on a 32-bit computer and it failed:

```
macaron% ./sage -i msieve-1.49.p0.spkg
...

ranlib libmsieve.a
gcc -D_FILE_OFFSET_BITS=64 -O3 -fomit-frame-pointer -march=k8 -DNDEBUG -D_LARGEFILE64_SOURCE  -Wall -W -DMSIEVE_SVN_VERSION="\"exported\"" -I. -Iinclude -Ignfs -Ignfs/poly -Ignfs/poly/stage1 -DHAVE_GMP_ECM "-I/localdisk/tmp/sage-4.7.2/local/include" demo.c -o msieve  \
                        libmsieve.a -lecm -lz -lgmp -lm -lpthread
libmsieve.a(sieve.qo): In function `do_sieving':
sieve.c:(.text+0x1335): undefined reference to `qs_core_sieve_p3_64k'
sieve.c:(.text+0x175b): undefined reference to `qs_core_sieve_p2_64k'
sieve.c:(.text+0x2556): undefined reference to `qs_core_sieve_pm_32k'
sieve.c:(.text+0x2603): undefined reference to `qs_core_sieve_k7_64k'
sieve.c:(.text+0x266b): undefined reference to `qs_core_sieve_k7xp_64k'
collect2: ld returned 1 exit status
make: *** [x86_64] Error 1
Error building Msieve -- no file msieve was produced.

real    1m33.556s
user    0m29.657s
sys     0m2.000s
sage: An error occurred while installing msieve-1.49.p0
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /localdisk/tmp/sage-4.7.2/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/localdisk/tmp/sage-4.7.2/spkg/build/msieve-1.49.p0 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/localdisk/tmp/sage-4.7.2/spkg/build/msieve-1.49.p0' && '/localdisk/tmp/sage-4.7.2/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
Error: Failed to install package 'msieve-1.49.p0'.
```

The processor is a Pentium 4. The system is Fedora 10.

Paul Zimmermann


---

Comment by zimmerma created at 2011-12-21 09:51:41

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2012-01-03 23:29:29

The fails on my OpenSolaris box, and I can see will fail on any sort of Solaris system. These lines:


```
if [ "`uname -m`" = "SunOS" ]; then
    $MAKE generic ECM=1
fi
```


make no sense, as the -m option to 'uname' is defined by POSIX to return the hardware, not the operating system. See:

http://pubs.opengroup.org/onlinepubs/009695399/utilities/uname.html

So it produces:


```
drkirkby@hawk:~$ uname -m
i86pc
```


and on a SPARC would produce something different, like sun4m, sun4u, sun4v and possibly something else for the newer processors. On my old SPARC


```
-bash-3.00$ uname -m
sun4u
```



Rather than invoke the external program 'uname', it is better to use the sage variable UNAME. The following is the most robust way of testing a variable, which will work for any shell, and pretty much any circumstances. 


```
if [ "x$UNAME" = xSunOS ] ; then
```


There's nothing to build a 64-bit version on Solaris - the SAGE64 variable is not used. 

I also got another failure:


```
****************************************************
patching file Makefile
Error building Msieve -- no file msieve was produced.

real	0m0.022s
user	0m0.006s
sys	0m0.015s
sage: An error occurred while installing msieve-1.49.p0
```


I suspect this is picking up the Solaris version of patch, not the GNU one which is part of Sage, though I've never seen this issue before. 

Also, this seems a bit pointless


```
$CP msieve "$SAGE_LOCAL"/bin/
```


We should just call 'cp' directly. Variables are useful for programs like "make", but not for a simple copy like this. 

The whole of spkg-install is a bit of a mess. It basically needs a total re-write. 

Also, there is no spkg-check file. 

Dave


---

Comment by drkirkby created at 2012-01-03 23:43:14

Ignore the comment about the wrong version of 'patch'. I somehow thought the error message was being generated during the patch, but its simply that the code does not build, which is hardly surprising, as the operating system is not tested properly. 

It would make sense to default to "generic", which according to the makefile produces portable code. So it then has some hope of working on Android, AIX, HP-UX or any of the numerous other operating systems.


---

Comment by jdemeyer created at 2015-06-23 13:49:38

Changing component from interfaces to packages: optional.


---

Comment by zimmerma created at 2015-06-23 13:57:59

in comment [comment:21] I forgot to put CADO-NFS so that we hit this ticket when searching
for CADO-NFS. This is the only purpose of this new comment.


---

Comment by kartikv created at 2015-08-23 03:36:16

Changing status from needs_work to needs_review.


---

Comment by kartikv created at 2015-08-23 03:36:16

Changed to an experimental package in order to get into Sage for 64-bit systems, seems to work fine on those. Reasonably tested with good speed and documentation for main function provided, may be useful to include additional doctests.
----
New commits:


---

Comment by kartikv created at 2015-08-23 03:36:16

Changing component from packages: optional to packages: experimental.


---

Comment by zimmerma created at 2015-08-24 14:39:16

I managed to build the git branch, but I failed to install the upstream package
(renamed to msieve-1.49.tar.gz as mentioned in the description above):

```
zimmerma@barbecue:/localdisk/tmp/sage-6.7$ ./sage -i /tmp/msieve-1.49.tar.gz 
msieve-1.49.tar.gz
====================================================
Extracting package /tmp/msieve-1.49.tar.gz
-rw-r----- 1 zimmerma caramel 457682 Aug 24 14:06 /tmp/msieve-1.49.tar.gz
Finished extraction
/localdisk/tmp/sage-6.7/build/bin/sage-spkg: line 512: cd: msieve-1.49.tar.gz: No such file or directory
Error: after extracting, the directory msieve-1.49.tar.gz does not exist
```

What did I do wrong?


---

Comment by zimmerma created at 2015-08-24 14:39:16

Changing status from needs_review to needs_info.


---

Comment by kartikv created at 2015-08-24 17:23:58

Move msieve-1.49.tar.gz to SAGE_ROOT/upstream and then ./sage -i msieve should work.


---

Comment by kartikv created at 2015-08-24 17:23:58

Changing status from needs_info to needs_review.


---

Comment by novoselt created at 2017-01-15 01:10:40

Changing status from needs_review to needs_work.


---

Comment by mkoeppe created at 2020-06-19 18:16:00

Changing status from needs_work to needs_info.


---

Comment by mkoeppe created at 2020-06-19 18:16:00

Setting spkg proposals that have not seen recent activity to "sage-wishlist".
