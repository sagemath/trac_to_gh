# Issue 6981: include 64-bit OS X gfortran in standard SAge

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-22 01:42:38

Assignee: tbd

This will make the tarball bigger (by 24MB), but is the only way to go at present.   With this one spkg update, building Sage 64-bit on OS X will be as simple as typing:


```
export SAGE64="yes"
make
```





---

Comment by was created at 2009-09-22 02:11:01

The spkg is here:

  http://sage.math.washington.edu/home/wstein/patches/fortran-20071120.p6.spkg


---

Comment by jhpalmieri created at 2009-09-22 04:11:56

For the 64-bit version, is there a reason to copy a big bzipped tar file to SAGE_LOCAL?  If not, then I think that in the file [{{/src/gfortran/fortran-OSX64-20090120/spkg-install}}}, the lines

```
cp src/gfortran-4.2.3.tar.bz2 $SAGE_LOCAL
cd $SAGE_LOCAL; tar -xjf gfortran-4.2.3.tar.bz2 -C .
```

should be changed to something like

```
cd $SAGE_LOCAL; tar -xjf $CUR/gfortran-4.2.3.tar.bz2 -C .
```

Also, there should be a message about the 64-bit version being installed: in the main spkg-install file, the function `install_fortran_osx64` could start with a message like

```
print "Installing OSX 64-bit gfortran compiler"
```

Some people who are sticklers might complain about the format of SPGK.txt, but I don't care that much.


---

Comment by mvngu created at 2009-09-22 07:18:00

Changing component from build to packages.


---

Comment by mvngu created at 2009-09-22 07:18:00

Replying to [comment:2 jhpalmieri]:
> For the 64-bit version, is there a reason to copy a big bzipped tar file to SAGE_LOCAL?  If not, then I think that in the file [{{/src/gfortran/fortran-OSX64-20090120/spkg-install}}}, the lines
> {{{
> cp src/gfortran-4.2.3.tar.bz2 $SAGE_LOCAL
> cd $SAGE_LOCAL; tar -xjf gfortran-4.2.3.tar.bz2 -C .
> }}}
> should be changed to something like
> {{{
> cd $SAGE_LOCAL; tar -xjf $CUR/gfortran-4.2.3.tar.bz2 -C .
> }}}
Done. I have added your reviewer comment to `src/gfortran/fortran-OSX64-20090120/spkg-install` and committed this change in your name.




> Also, there should be a message about the 64-bit version being installed: in the main spkg-install file, the function `install_fortran_osx64` could start with a message like
> {{{
> print "Installing OSX 64-bit gfortran compiler"
> }}}
Done. This line is now in the main `spkg-install`. The change has been committed in your name.





> Some people who are sticklers might complain about the format of SPGK.txt, but I don't care that much.
Also taken care of. An updated spkg with reviewer changes can be found at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/fortran-20071120.p6.spkg

I'm reviewing the actual building of that package now. You're more than welcome to try building Sage 4.1.2.alpha2 from source with this updated Fortran package. The more the merrier :-)


---

Comment by mvngu created at 2009-09-22 07:18:00

Changing assignee from tbd to mabshoff.


---

Comment by mvngu created at 2009-09-22 07:32:08

Replying to [comment:2 jhpalmieri]:
> For the 64-bit version, is there a reason to copy a big bzipped tar file to SAGE_LOCAL?  If not, then I think that in the file [{{/src/gfortran/fortran-OSX64-20090120/spkg-install}}}, the lines
> {{{
> cp src/gfortran-4.2.3.tar.bz2 $SAGE_LOCAL
> cd $SAGE_LOCAL; tar -xjf gfortran-4.2.3.tar.bz2 -C .
> }}}
> should be changed to something like
> {{{
> cd $SAGE_LOCAL; tar -xjf $CUR/gfortran-4.2.3.tar.bz2 -C .
> }}}
This results in the following error:

```
tar (child): /Volumes/LACIE/scratch/mvngu/sandbox-32/sage-4.1.2.alpha2/spkg/build/fortran-20071120.p6/src/gfortran/fortran-OSX64-20090120/gfortran-4.2.3.tar.bz2: Cannot open: No such file or directory
tar (child): Error is not recoverable: exiting now
tar: Child returned status 2
tar: Error exit delayed from previous errors
Installing OS X 64-bit gfortran compiler






**********************************************************************






Error installing Fortran: Error installing OS X 64-bit gfortran
```

The actual command should be 

```
cd $SAGE_LOCAL; tar -xjf $CUR/src/gfortran-4.2.3.tar.bz2 -C .
```

Notice the "src" part. The updated spkg includes this fix.


---

Comment by jhpalmieri created at 2009-09-22 14:52:56

Mac OS 10.5: open a new terminal (and doublecheck that SAGE64 is not set).  Untar sage-4.1.2.alpha2 and replace the fortran package there with the new one.  Type 'make' and wait: I see

```
Installing OS X 64-bit gfortran compiler
```

I don't know why...


---

Comment by was created at 2009-09-22 15:03:36

New spkg up here: http://sage.math.washington.edu/home/wstein/patches/fortran-20071120.p7.spkg


---

Comment by jhpalmieri created at 2009-09-22 15:29:59

Almost perfect.  To make it perfect, I would like to see this change from mvngu's version re-incorporated:

> Also, there should be a message about the 64-bit version being installed: in the main spkg-install file, the function install_fortran_osx64 could start with a message like

```
print "Installing OSX 64-bit gfortran compiler"
```



---

Comment by was created at 2009-09-22 15:31:55

OK, I refreshed the spkg with that.


---

Comment by jhpalmieri created at 2009-09-22 15:40:17

Looks good to me.  The SPKG.txt file isn't in the right format, but I don't care.


---

Comment by was created at 2009-09-25 06:37:57

I've made a major improvement to how this spkg detects "64 bit" so it will work when building Sage on OS X 10.6 without explicitly specifying SAGE64.  Instead of using that flag it simply checks the bitness of Python.  Without this we would get a 32-bit compiler, which is completely wrong. 

  New spkg: http://sage.math.washington.edu/home/wstein/patches/fortran-20071120.p8.spkg


---

Comment by mvngu created at 2009-09-27 00:11:41

New spkg up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/fortran-20071120.p9.spkg

The only changes from .p8 are:

 * remove junk files: `spkg-install~` and `SPKG.txt~`
 * add info to SPKG.txt


---

Comment by mvngu created at 2009-09-27 02:32:55

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 02:32:55

See palmieri's and my reports at #6849.


---

Comment by mvngu created at 2009-09-27 10:57:30

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
