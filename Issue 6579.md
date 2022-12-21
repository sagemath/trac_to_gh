# Issue 6579: Error building 'modified sage library code' when including paripriv.h

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-07-21 15:10:58

Assignee: tbd

Keywords: Solaris hack

Although the build of pari goes ok on Solaris, there is an error when building the modified sage library code. It complains about syntax errors - see below. 


```
Time to execute 1 commands: 2.75036501884 seconds
Finished compiling Cython code (time = 4.44064807892 seconds)
running install
running build
running build_py
copying sage/symbolic/constants.py -> 
build/lib.solaris-2.10-sun4u-2.6/sage/symbolic
running build_ext
building 'sage.ext.fast_callable' extension
creating build/temp.solaris-2.10-sun4u-2.6/sage/ext
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall 
-Wstrict-prototypes -fPIC 
-I/export/home/drkirkby/sage/sage-4.1.rc0/local//include 
-I/export/home/drkirkby/sage/sage-4.1.rc0/local//include/csage 
-I/export/home/drkirkby/sage/sage-4.1.rc0/devel//sage/sage/ext 
-I/export/home/drkirkby/sage/sage-4.1.rc0/local/include/python2.6 -c 
sage/ext/fast_callable.c -o 
build/temp.solaris-2.10-sun4u-2.6/sage/ext/fast_callable.o -w
In file included from sage/ext/fast_callable.c:141:
/export/home/drkirkby/sage/sage-4.1.rc0/local//include/pari/paripriv.h:258: 
error: expected ';', ',' or ')' before numeric constant
/export/home/drkirkby/sage/sage-4.1.rc0/local//include/pari/paripriv.h:259: 
error: expected ';', ',' or ')' before numeric constant
In file included from sage/ext/fast_callable.c:141:
/export/home/drkirkby/sage/sage-4.1.rc0/local//include/pari/paripriv.h:428: 
error: expected identifier before numeric constant
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.
```


I have developed a patch, and will apply it later, including this tick number. 

Dave 


---

Comment by drkirkby created at 2009-07-21 15:34:31

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2009-07-23 07:29:28

Well, the patch is more of a hack. With manual editing of 


```

$SAGE_HOME/local/include/pari/paripriv.h
```

(comment out lines 258, 259 and 428) 

the 'modified sage library code' will build if /opt/SUNWspro/bin/CC is NOT to be found, but will fail if that can be found. See trac #6595


---

Comment by drkirkby created at 2009-10-13 10:57:46

Having disucssed my patch idea, it seems they were not optimal, so I'd like someone else to do this. 

I've updated it to blocker, as is the only problem that stops Sage building on Solaris simply by typing 'make'.


---

Comment by drkirkby created at 2009-10-13 10:57:46

Changing keywords from "Solaris hack" to "Solaris".


---

Comment by drkirkby created at 2009-10-13 10:57:46

Changing priority from major to blocker.


---

Comment by drkirkby created at 2009-10-16 01:25:50

Changing status from new to needs_review.


---

Comment by drkirkby created at 2009-10-16 01:25:50

Having looked at this more, and the pari package in particular, it was clear similar (but more severe) issues had arisen on OS X with the inclusion of this pari header file. The solution adopted for OS X was to create a specific header file for OS X, and copy that over. 

The following package does exactly the same thing, but only for Solaris. The changes needed appeared different from those needed for OS X, so I could not use the OS version of the header file for Solaris too. In the case of OS X, libraries had to be manually copied around too - no such changes were needed on Solaris, just a simple copy of a file. The extra code added to spkg-install was:


```

    if [ `uname` = "SunOS" ]; then
       set -e
       echo "Patching include/pari/paripriv.h so it works on Solaris"
       echo "The changes are much smaller than needed on OS X"
       cp  "$TOP"/patches/paripriv-Solaris.h $SAGE_LOCAL/include/pari/paripriv.h       
       set +e
    fi

```


The files can be found at

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/pari-2.3.3.p5/

This is the last remaining issue that prevent Sage building on Solaris with no manual intervention. It requires that gcc is used, and that SAGE64 is *not* set to 'yes', as this code will only build in 32-bit mode. 

Dave


---

Comment by mhansen created at 2009-10-21 06:44:56

Looks good to me.


---

Comment by mhansen created at 2009-10-21 06:44:56

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-21 06:45:14

Resolution: fixed
