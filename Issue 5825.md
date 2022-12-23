# Issue 5825: sage -i $FOO.spkg should abort cleanly when write permissions are lacking

Issue created by migration from https://trac.sagemath.org/ticket/5825

Original creator: mabshoff

Original creation time: 2009-04-20 01:07:19

Assignee: mabshoff

CC:  jhpalmieri

I just ran into the following:

```
<SNIP>
**********************************************************************
* Unable to download clisp-2.47
* Please see http://www.sagemath.org//packages for a list of valid
* packages or check the package name.
**********************************************************************
/Users/mabshoff/sage-3.3.rc3/spkg/build
bunzip2: Can't open input file clisp-2.47.spkg: No such file or directory.
tar: clisp-2.47.spkg: Cannot open: No such file or directory
tar: Error is not recoverable: exiting now
Second download resulted in a corrupted package.
varro:/Users/mabshoff/sage-3.3.rc3 mabshoff$ file /home/mabshoff/clisp-2.47.spkg 
/home/mabshoff/clisp-2.47.spkg: bzip2 compressed data, block size = 900k
varro:/Users/mabshoff/sage-3.3.rc3 mabshoff$ cp /home/mabshoff/clisp-2.47.spkg .
cp: ./clisp-2.47.spkg: Permission denied
```


Note that I do not have write permissions in the local directory.


---

Comment by jdemeyer created at 2013-05-16 08:48:45

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-05-16 08:48:45

Changing component from packages: standard to scripts.


---

Comment by jhpalmieri created at 2013-05-21 18:51:40

Is it worth checking permissions before attempting to download an spkg?

```
$ sage -i pybtex
tee: /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/logs/install.log: Permission denied
tee: /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/logs/pkgs/pybtex.log: Permission denied
Attempting to download package pybtex
>>> Checking online list of optional packages.
[.]
>>> Found pybtex-20120618
>>> Downloading http://www.sagemath.org/spkg/optional/pybtex-20120618.spkg.
/Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/spkg/bin/sage-spkg: line 354: pybtex-20120618.tmp: Permission denied
Error: failed to download package pybtex-20120618
```

This is not as nice an error message as you added in other situations:

```
$ sage -f gcc
tee: /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/logs/install.log: Permission denied
tee: /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/logs/pkgs/gcc.log: Permission denied
Found package gcc in spkg/standard/gcc-4.7.3.p0.spkg
Error: no write access to build directory /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/spkg/build.
```



---

Attachment

OK, fixed.


---

Comment by jhpalmieri created at 2013-05-22 17:10:43

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2013-05-22 17:10:43

Great, looks good.


---

Comment by jdemeyer created at 2013-05-24 09:39:47

Resolution: fixed
