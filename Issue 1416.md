# Issue 1416: get the R statistics software into Sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-07 07:23:33

Assignee: was

TODO list
 * upgrade to 2.6.1
 * patch rpy
 * fix build issues and install issues
 * finish pexpect interface.
 * worry about graphics / X11 issues
 * readline
 * gfortran support (extra setup.py in rpy package)


---

Comment by was created at 2007-12-07 07:40:19

NOTE: For building on OSX I had to remove SAGE_ROOT/local/lib/libsqlite3.so


---

Comment by was created at 2007-12-07 07:58:11

See this for valuable info for building on osx 10.5:
http://r.research.att.com/building.html


---

Comment by mabshoff created at 2007-12-07 10:10:03

For the integration of R we already had #348, but this ticket had more info, I turned the other ticket into a dup and closed it.

Cheers,

Michael


---

Comment by was created at 2007-12-09 18:48:13

Add this to spkg/install

```
R=`$newest r`
export R
```


Add this to spkg/standard/deps (somewhere in the middle):

```
$(INST)/$(R): $(INST)/$(PYTHON)      
        $(SAGE_SPKG) $(R) 2>&1
        $(MAKEREL)
```

and also add this to the big list of things the $(INST)/$(SAGE) target depends on:

```
                $(INST)/$(R)  \
```


WARNING: The above is untested, so probably not perfect -- though I'm pretty confident.


---

Comment by was created at 2007-12-09 18:53:26

Get the latest spkg for R here:

http://sagemath.org/packages/optional/


---

Comment by was created at 2007-12-09 19:54:51

WAIT: Readline detection still doesn't work -- i.e., only using the readline in sage -- at least on one platform, namely sagemath.org (opteron ubuntu 64bit):


```
0.3 -L/usr/lib/gcc -lf95 -lm  ../extra/zlib/libz.a ../extra/bzip2/libbz2.a ../extra/pcre/libpcre.a  -lreadline -lncurses  -ldl -lm
/usr/bin/ld: cannot find -lreadline
collect2: ld returned 1 exit status
make[3]: *** [libR.so] Error 1
make[3]: Leaving directory `/home2/sage/s/local/lib/r/src/main'
make[2]: *** [R] Error 2
make[2]: Leaving directory `/home2/sage/s/local/lib/r/src/main'
make[1]: *** [R] Error 1
make[1]: Leaving directory `/home2/sage/s/local/lib/r/src'
make: *** [R] Error 1
Error building R.

real	2m59.168s
user	1m9.016s
sys	0m30.386s
sage: An error occurred while installing r-2.6.1.p2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home2/sage/s/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/home2/sage/s/spkg/build/r-2.6.1.p2 and type 'make'.
Instead type "/home2/sage/s/sage -sh"
in order to set all environment variables correctly, then cd to
/home2/sage/s/spkg/build/r-2.6.1.p2
(When you are done debugging, you can type "exit" to leave the
subshell.)

```



---

Comment by jkantor created at 2007-12-09 20:59:08

The r package itself appears to check versions and correctly link libf95 or libgfortran on its own. 
It compiled fine using gfortran. The rpy package does not do this, but the spkg in 1427 that fixes the osx 10.4 build also makes is work with g95 or gfortran. So just use that rpy package.


---

Comment by jkantor created at 2007-12-09 21:05:15

you may just want to grab the newest rpy from my home directory to make sure you actually got the newest one. 

                                                          Josh


---

Comment by mabshoff created at 2007-12-10 05:22:50

Merged in 2.9.alpha3.


---

Comment by mabshoff created at 2007-12-10 05:22:50

Resolution: fixed
