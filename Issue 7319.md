# Issue 7319: gdmodule requires libiconv on cygwin

Issue created by migration from https://trac.sagemath.org/ticket/7319

Original creator: mhansen

Original creation time: 2009-10-27 05:13:46

Assignee: tbd

CC:  was

On Cywgin, the gdmodule spkg requires libiconv.  I think we have two choices for handling this:

1. Making sure that libiconv is always installed in the system Cygwin environment.  We can probably have control over this if we include the Cygwin install with Sage.

2. Add a libiconv spkg that is only installed if we are in Cygwin.  Note that this would probably amount to including it in all source tarballs.

Once libiconv is present, we need to patch Setup.py in gdmodule to add libiconv to the list of required libraries.

I'll put up an spkg for libiconv and gdmodule here shortly.


---

Comment by mhansen created at 2009-10-27 14:01:18

The spkg can be found a http://sage.math.washington.edu/home/mhansen/gdmodule-0.56.p7.spkg


---

Comment by mhansen created at 2009-10-27 14:01:18

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-31 05:26:32

The latest version of R will need iconv on Solaris - currently an option to configure, something like --no-iconv is added on R. But iconv is mandatory on the latest version with Solaris. Given iconv is not large, and does not take long to build, I believe that is should be added. I would also suggest it is installed on all platforms - not just Cygwin and Solaris. It would give one more item which is fixed, and so less need to worry if someone's problem might be their version of iconv is  too old or broken in some way. 


Dave


---

Comment by drkirkby created at 2010-01-31 05:31:01

Note, SPKG.txt has:

### gdmodule-0.56.p5 (Mike Hansen, October 27th, 2009)
 * Make gdmodule work on Cygwin.

### gdmodule-0.56.p5 (Michael Abshoff)
 * add .hgignore, SPKG.txt
 * clean up patches directory
 * build gdmodule against libpng12 instead of libpng (#5289)

with no entry for a p6 or p7. So this needs a bit of work, but even then, I'm unable to test on Cygwin, so you would need another reviewer too.


---

Comment by drkirkby created at 2010-01-31 05:31:01

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-02-05 10:35:35

As I stated above, R also needs iconv on Solaris now - the R developers have now disabled the option to not use iconv. I've created #8191 to create an iconv package. This seems the most logical way. I can't see any possible workaround with R. 

Dave


---

Comment by drkirkby created at 2010-02-15 14:35:21

#8191 now has an iconv package, awaiting review, so there should be no need for Mike to create an iconv package.


---

Comment by drkirkby created at 2010-03-01 01:44:20

#8191 now has positive review, so iconv should soon be in Sage.


---

Comment by drkirkby created at 2010-03-19 22:27:04

Can this ticket be closed, given there is now an iconv package as a standard .spkg file in Sage? 

dave


---

Comment by mhansen created at 2010-03-19 23:17:22

I'm not sure since the spkg here has other changes to it.  I'll double check.


---

Comment by mhansen created at 2010-04-06 18:18:43

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-04-06 18:18:43

There is an spkg at http://sage.math.washington.edu/home/mhansen/cygwin_port/gdmodule-0.56.p7.spkg that should be used.  This still needs a review.


---

Comment by drkirkby created at 2010-04-07 13:12:39

Has this been tested on at least one Linux, Solaris and OS X system? There are quite a few non-trivial changes here, and I am aware iconv and gd have caused problems recently, so I think we need to be especially careful this is very well tested. 

Dave


---

Comment by mhansen created at 2010-04-07 17:31:03

I've tested it on Cygwin and Linux.  The only change is Cygwin-specific and does not happen on any other platform.  The rest of the last commit was just checking in files to the repo that should have been but were not.


---

Comment by was created at 2010-04-27 00:08:30

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-29 05:04:54

Resolution: fixed


---

Comment by was created at 2010-06-02 02:26:15

I'm having trouble with this on Cygwin now:

```

E_LIBFONTCONFIG -I/home/wstein/sage-4.4.3.alpha1/local/include -I/usr/include -I/usr/include/X11 -I/home/wstein/sage-4.4.3.al
 -c _gdmodule.c -o build/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o
_gdmodule.c:152: warning: function declaration isn’t a prototype
_gdmodule.c:169: warning: function declaration isn’t a prototype
_gdmodule.c: In function ‘image_string’:
_gdmodule.c:993: warning: pointer targets in passing argument 5 of ‘gdImageString’ differ in signedness
_gdmodule.c: In function ‘image_string16’:
_gdmodule.c:1008: warning: passing argument 5 of ‘gdImageString16’ from incompatible pointer type
_gdmodule.c: In function ‘image_stringup’:
_gdmodule.c:1022: warning: pointer targets in passing argument 5 of ‘gdImageStringUp’ differ in signedness
_gdmodule.c: In function ‘image_stringup16’:
_gdmodule.c:1037: warning: passing argument 5 of ‘gdImageStringUp16’ from incompatible pointer type
gcc -shared -Wl,--enable-auto-image-base build/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o -L/home/wstein/sage-4.4.3.alpha1/local/
1 -L/home/wstein/sage-4.4.3.alpha1/local/lib/python2.6/config -lgd -lpng12 -lz -lfreetype -liconv -lfontconfig -lpython2.6 -o
-2.6/_gd.dll
build/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o: In function `write_file':
/home/wstein/sage-4.4.3.alpha1/spkg/build/gdmodule-0.56.p7/src/_gdmodule.c:248: undefined reference to `_gdImagePngPtr'
/home/wstein/sage-4.4.3.alpha1/spkg/build/gdmodule-0.56.p7/src/_gdmodule.c:250: undefined reference to `_gdImagePng'
build/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o:_gdmodule.c:(.rdata+0x7e4): undefined reference to `_gdImageCreateFromPng'
build/temp.cygwin-1.7.1-i686-2.6/_gdmodule.o:_gdmodule.c:(.rdata+0x824): undefined reference to `_gdImageCreateFromPngCtx'
collect2: ld returned 1 exit status
error: command 'gcc' failed with exit status 1
Failure to build gdmodule

real    0m3.434s
user    0m0.760s
sys     0m1.991s
sage: An error occurred while installing gdmodule-0.56.p7

```

