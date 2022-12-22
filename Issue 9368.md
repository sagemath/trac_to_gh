# Issue 9368: sage_fortran ignores SAGE64 except on Solaris/OpenSolaris

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-06-28 23:25:39

Assignee: GeorgSWeber

CC:  justin mpatel jhpalmieri

#9346 which corrects a problem with the variable has a problem, because SAGE64 is ignored on any plaform other than OS X. 

This needs correcting urgently. 

Dave


---

Comment by drkirkby created at 2010-06-28 23:44:22

Mercurial patch which hopefully finally fixes this fortran issue. (Long-term, it would be good to get rid of files like sage_fortran)


---

Comment by drkirkby created at 2010-06-28 23:46:42

Changing status from new to needs_review.


---

Attachment

A new package can be found at 

http://boxen.math.washington.edu/home/kirkby/patches/fortran-20100629.spkg

Note, this is just a tar file, not a compressed tar file, as compressing the contents, which are already compressed, just makes the package bigger and need more CPU time to process


---

Comment by jhpalmieri created at 2010-06-29 15:58:12

The change makes sense to me, but I'm not sure I can referee it properly: I don't have any problem with fortran on my Mac OS X box.  This is OS X 10.6 on a 64-bit machine.  No matter how I set SAGE64, the file sage_fortran always says

```/bin/bash
gfortran -m64 "$`@`"
```

In fact, the lines which get changed by the patch occur in the function `install_SAGE_FORTRAN`, which should only get run if the environment variable `SAGE_FORTRAN` is set.  I don't know why anyone on OS X should set this.


---

Comment by rlm created at 2010-06-29 16:14:37

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-29 16:15:07

Resolution: fixed


---

Comment by drkirkby created at 2010-06-29 20:52:51

Replying to [comment:5 jhpalmieri]:
> The change makes sense to me, but I'm not sure I can referee it properly: I don't have any problem with fortran on my Mac OS X box.  This is OS X 10.6 on a 64-bit machine.  No matter how I set SAGE64, the file sage_fortran always says
> {{{
> #!/bin/bash
> gfortran -m64 "$`@`"
> }}}
> In fact, the lines which get changed by the patch occur in the function `install_SAGE_FORTRAN`, which should only get run if the environment variable `SAGE_FORTRAN` is set.  I don't know why anyone on OS X should set this.

I'm pretty sure I've seen it written that one can do this on OS X if you want to use a different compiler. I guess with Apple shipping 4.0.1, it is not surprising some people are using more recent compilers. 

Sorry for the mess up!

Dave


---

Comment by was created at 2010-07-15 12:22:55

Changing status from closed to needs_work.


---

Comment by was created at 2010-07-15 12:22:55

I'm re-opening this ticket because the fortran-20100629.spkg is broken.  On OS X, it installs g95 now, whereas the previous fortran spkg (the one in sage-4.4.4) installs gfortran.      Somebody was a bit sloppy.  

When this package is properly updated for OS X, make sure to type

  ./sage -sh
   local/bin/sage_fortran.bin --version

and ensure that you've actually got gfortran installed, not g95.  The gfortran binary for OS X is quad-architecture -- it covers 32 and 64-bit on both ppc and intel.


---

Comment by was created at 2010-07-15 12:23:18

I'm also moving this to sage-4.5.1, so that the release manager can release sage-4.5.


---

Comment by was created at 2010-07-15 12:23:18

Changing priority from blocker to critical.


---

Comment by drkirkby created at 2010-07-15 12:38:38

Replying to [comment:9 was]:
> I'm re-opening this ticket because the fortran-20100629.spkg is broken.  On OS X, it installs g95 now, whereas the previous fortran spkg (the one in sage-4.4.4) installs gfortran.      Somebody was a bit sloppy.  
> 
> When this package is properly updated for OS X, make sure to type
> 
>   ./sage -sh
>    local/bin/sage_fortran.bin --version
> 
> and ensure that you've actually got gfortran installed, not g95.  The gfortran binary for OS X is quad-architecture -- it covers 32 and 64-bit on both ppc and intel.    

Since I created it, I guess you are saying I was sloppy. It is hard to know how I can check this any more, given it builds for me on OS X (bsd.math) using 
 * My normal environment
 * Your script. 

It also builds for everyone else. There are numerous reports of successful builds on OS X. 

Would it be sensible to remove 'g95' from the package, and ensure that the packages assumes 'gfortran' - then the perl script can be removed. 

Dave


---

Comment by was created at 2010-07-15 12:47:32

> Since I created it, I guess you are saying I was sloppy. It is hard to know how I can check 
> this any more, given it builds for me on OS X (bsd.math) using

I wrote the spkg and most of the script in the first place, and looking it over, I think now it would be more accurate to conclude that I'm saying that *I* was sloppy.    As penance, I'll move this back to sage-4.5, and try to improve the sloppiness.


---

Comment by drkirkby created at 2010-07-15 12:51:24

Replying to [comment:12 was]:
> > Since I created it, I guess you are saying I was sloppy. It is hard to know how I can check 
> > this any more, given it builds for me on OS X (bsd.math) using
> 
> I wrote the spkg and most of the script in the first place, and looking it over, I think now it would be more accurate to conclude that I'm saying that *I* was sloppy.    As penance, I'll move this back to sage-4.5, and try to improve the sloppiness.  

Thank you. 

Dave


---

Comment by was created at 2010-07-15 13:14:41

OK, I've found the problem.  The build script is written in Python.  Thus the fortran spkg *depends* on Python.   However, for me, when I built the fortran spkg, it got built before Python, hence some random system-wide wrong python was used, and this broke the build.  This was a problem that could have happened on many different systems in weird ways, so it's very good that Robert Miller and I persisted and tracked this down, instead of brushing it off. 

The fix:  change the deps file, and make sure to include a comment in the deps file explaining this dependency.

One could also add a check that $SAGE_LOCAL/bin/python exists in this spkg-install script. 

Another good idea, would be to change the sage build system, so that when if spkg-install is a Python script, but Python hasn't been built yet, then an error is immediately raised.  This would keep this problem from ever happening again.  I've opened a ticket: #9507.


---

Comment by rlm created at 2010-07-15 13:18:58

Re-closing this ticket :)


---

Attachment


---

Comment by rlm created at 2010-07-15 13:23:31

Looks good!

```
471,472c471
< # Do not remove PYTHON below -- see trac 9368
< $(INST)/$(FORTRAN): $(BASE)  $(INST)/$(PYTHON)
---
> $(INST)/$(FORTRAN): $(BASE)
```



---

Comment by drkirkby created at 2010-07-15 22:45:24

Replying to [comment:14 was]:
> OK, I've found the problem.  The build script is written in Python.  Thus the fortran spkg *depends* on Python.   However, for me, when I built the fortran spkg, it got built before Python, hence some random system-wide wrong python was used, and this broke the build.  This was a problem that could have happened on many different systems in weird ways, so it's very good that Robert Miller and I persisted and tracked this down, instead of brushing it off. 

I'm afraid to say I don't share your confidence that you and Robert have tracked this down completely, though you have found a serious flaw. 

Clearly adding this dependency to `$SAGE_ROOT/spkg/standard/deps` is correct - the fortran package uses Python, so Python must be built first. I'm not arguing with that. 

However, I'm not convinced this was William's problem, as the `$SAGE_LOCAL/bin/sage_fortain` script *must* have been working at one point, otherwise ATLAS, Linpack, Numpy and other things that used Fortran would not have built. As I posted on sage-release, William's `install.log` had in it


```
sage_fortran -fPIC  -c lsame.f -o lsame.o
sage_fortran -fPIC  -c lsametst.f -o lsametst.o
sage_fortran  -o testlsame lsame.o lsametst.o
sage_fortran -fPIC  -c slamch.f -o slamch.o
sage_fortran -fPIC  -c slamchtst.f -o slamchtst.o
sage_fortran  -o testslamch slamch.o lsame.o slamchtst.o 
```


However, when I looked at William's $SAGE_LOCAL/bin/sage_fortran, it had only:


```/bin/sh
```


in it. There is *no way* that could have been used to compile ATLAS, Linbox, Numpy etc, all of which had built successfully. 

Hence I believe that something other than the fortran package later modified `$SAGE_LOCAL/bin/sage_fortran`. Unless I'm mistaken, the bug does not reside in the fortran package at all, but rather in something that was built after ATLAS, Numpy and Linbox. 

Comments? 

Dave


---

Comment by jhpalmieri created at 2010-07-15 22:55:06

> I'm afraid to say I don't share your confidence that you and Robert have tracked this down completely, though you have found a serious flaw. 

As you also say, the change to deps is clearly right, so since this seems to fix the problem, we should leave this ticket closed, but keep an eye on this issue.

(It would have been interesting to know the modification time of sage_fortran.  I can't imagine that anything else would have modified this; it seems more likely that something is broken in the ATLAS build, etc.  The broken build doesn't seem to be around anymore, though.)


---

Comment by rlm created at 2010-07-15 23:18:09

Replying to [comment:18 drkirkby]:
> I'm afraid to say I don't share your confidence that you and Robert have tracked this down completely, though you have found a serious flaw.

Of course you don't share the same confidence, you didn't trace the bug down to its source like we did. It was the configure script for the R spkg calling a very specific fortran command that made the build eventually fail. It is very easy to imagine that none of the other configure scripts called fortran in this way. In fact, they couldn't have or the build would have failed earlier.

> However, I'm not convinced this was William's problem, as the `$SAGE_LOCAL/bin/sage_fortain` script *must* have been working at one point, otherwise ATLAS, Linpack, Numpy and other things that used Fortran would not have built.

Define working.

> However, when I looked at William's $SAGE_LOCAL/bin/sage_fortran, it had only:
> 
> {{{
> #!/bin/sh
> }}}

As I pointed out earlier, this is just plain wrong!

> Unless I'm mistaken...

You are!


---

Comment by drkirkby created at 2010-07-15 23:25:25

I accept R could have called sage_fortran in a different way, which resulted in ATLAS, Linbox and Numpy building, but not R. 

But can you explain how ATLAS, Numpy and Linbox built, when I clearly see the sage_fortran script had in it


```/bin/sh
```


? 

I'm not wrong about the contents of the file. It *did* have that in it. 

Dave


---

Comment by drkirkby created at 2010-07-16 00:11:27

Replying to [comment:21 drkirkby]:

> But can you explain how ATLAS, Numpy and Linbox built, when I clearly see the sage_fortran script had in it
> 
> {{{
> #!/bin/sh
> }}}
> 
> ? 
> 
> I'm not wrong about the contents of the file. It *did* have that in it. 
> 
> Dave 

I realise I was mistaken here. Justin is almost certainly right when he says the lack of a new line in the file can fool the eye into believing that the contents of the file are just


```/bin/sh
}}}  

when in fact there is more to it. This is how it looks on my screen - it is easy to see that this could be confusing. 

{{{
drkirkby`@`hawk:~/sage-4.5.rc0$ cat local/bin/sage_fortran
#!/bin/sh 

/usr/local/gcc-4.4.4-multilib/bin/gfortran -m64 -fPIC $`@`drkirkby`@`hawk:~/sage-4.5.rc0$ 
}}}


I'm glad I was wrong about this. 

Dave
