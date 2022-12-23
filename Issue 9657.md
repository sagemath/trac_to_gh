# Issue 9657: cvxopt 0.9 does not compile on Solaris with gcc 4.5 or later.

Issue created by migration from https://trac.sagemath.org/ticket/9657

Original creator: drkirkby

Original creation time: 2010-08-01 03:21:39

Assignee: drkirkby

CC:  jhpalmieri dimpase jsp mpatel

There's a problem with cvxopt not building on gcc versions 4.5.0 or later. This has become especially critical lately, as only gcc 4.5.0 is available on Skynet, so this effecitvely means Sage can not be built on any Skynet computer running Solaris (_mark_, _mark2_ or _fulvia_)

Here's an example with OpenSolaris with gcc 4.5.0, though the same problem occurs on Solaris 10 SPARC and Solaris 10 x86. 


```
drkirkby@hawk:~/sage-4.5.1$ ./sage -f cvxopt-0.9.p8

<snip>

gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -O3 -m64 -Wall -Wstrict-prototypes -fPIC -I/export/home/drkirkby/sage-4.5.1/local/include/python2.6 -c C/base.c -o build/temp.solaris-2.11-i86pc-2.6/C/base.o
In file included from C/cvxopt.h:30:0,
                 from C/base.c:23:
C/sun_complex.h:9:0: warning: ignoring #pragma ident 
C/sun_complex.h:30:32: error: expected identifier or '(' before '_Imaginary'
error: command 'gcc' failed with exit status 1

real	0m0.131s
user	0m0.080s
sys	0m0.042s
sage: An error occurred while installing cvxopt-0.9.p8
```


This is ultimately due to `_Complex_I` being undefined - exactly the same problem which was observed in the Sage library several months ago - see #7932. 

This patch defines `_Complex_I` to be `1j` on Solaris with gcc versions prior to 4.5.0. 

With this change, cvxopt builds properly 


```
running install_egg_info
Removing /export/home/drkirkby/sage-4.5.1/local/lib/python2.6/site-packages/cvxopt-0.9-py2.6.egg-info
Writing /export/home/drkirkby/sage-4.5.1/local/lib/python2.6/site-packages/cvxopt-0.9-py2.6.egg-info

real	0m45.306s
user	0m40.395s
sys	0m3.786s
Successfully installed cvxopt-0.9.p9
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.5.1/spkg/build/cvxopt-0.9.p9
Making Sage/Python scripts relocatable...
Making script relocatable
```


*The patch is only applied on Solaris, so is very safe.*


---

Attachment

Mercurial patch to allow cvxopt to build with gcc 4.5.0 and later


---

Comment by drkirkby created at 2010-08-01 07:47:21

A copy of the package may be found here 

http://boxen.math.washington.edu/home/kirkby/patches/cvxopt-0.9.p9.spkg

An update of cvxopt be made (#6456), that is waiting on a new upstream release, so it will not be  practical, as this is critical but very small fix. 

Dave


---

Comment by drkirkby created at 2010-08-01 08:02:24

Changing status from new to needs_review.


---

Comment by leif created at 2010-08-01 14:51:44

So the bug has been fixed in gcc 4.5.0, but not the "more recent" gcc versions 4.4.4 and 4.3.5? (I see you've tested the patch successfully with gcc 4.4.4 on OpenSolaris, and

```C
        #if __GNUC__ < 4  || ( __GNUC__ == 4 && __GNUC_MINOR__ < 5   )
```

obviously holds for that version.)


---

Comment by drkirkby created at 2010-08-01 15:25:03

Replying to [comment:6 leif]:
> So the bug has been fixed in gcc 4.5.0, but not the "more recent" gcc versions 4.4.4 and 4.3.5? 

Yes, it has not been backported to the 4.3 or 4.4 series. Whether it ever will or not is another matter, but so far it has not. 

http://gcc.gnu.org/bugzilla/show_bug.cgi?id=42753

> (I see you've tested the patch successfully with gcc 4.4.4 on OpenSolaris, and
> {{{
> #!C
>         #if __GNUC__ < 4  || ( __GNUC__ == 4 && __GNUC_MINOR__ < 5   )
> }}}
> obviously holds for that version.)

I also tested on gcc 4.4.1 on 't2.math' - i.e. Solaris 10. 

At http://trac.sagemath.org/sage_trac/ticket/6456#comment:85 

I show the results from compiling a test program on a wide range (11 different bits of hardware) under about 25 different conditions (compiler versions). In each case, the bug is see in the 4.3 and 4.4 series, but not in 4.5. 


Dave


---

Comment by leif created at 2010-08-01 17:03:42

Ok, I was just wondering...

I think somebody more involved with SunOS should give this positive review though. ;-)


---

Comment by drkirkby created at 2010-08-01 17:08:45

Replying to [comment:8 leif]:
> Ok, I was just wondering...
> 
> I think somebody more involved with SunOS should give this positive review though. ;-)
> 
> 

Perhaps John can try 

http://boxen.math.washington.edu/home/kirkby/patches/cvxopt-0.9.p9.spkg

I could attach build logs if it would convince you more! 

Dave


---

Comment by jhpalmieri created at 2010-08-01 17:16:04

I'm currently trying to build on mark, mark2, fulvia, and t2 (and also on a few non-solaris machines just to be safe, although I can't see how this patch would have any effect on those machines).  I'm building sage-4.5.2.rc0 from scratch using this spkg, so it will take a while.


---

Comment by leif created at 2010-08-01 17:25:48

Replying to [comment:9 drkirkby]:
> I could attach build logs if it would convince you more! 

It's not that I wasn't convinced this will work, but others are more competent here.

I see "workhorse John" is already at reviewing it... :)


---

Comment by jhpalmieri created at 2010-08-02 04:33:02

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-08-02 04:33:02

This builds successfully on t2, mark, mark2, and fulvia (both 32-bit and 64-bit, as far as I can tell).  The patch clearly only makes a difference on Solaris machines.


---

Comment by mpatel created at 2010-08-02 08:46:39

Changing priority from critical to blocker.


---

Comment by mpatel created at 2010-08-04 02:10:33

Resolution: fixed
