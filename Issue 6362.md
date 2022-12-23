# Issue 6362: [with spkg, needs review] Singular and GCC 4.4

Issue created by migration from https://trac.sagemath.org/ticket/6362

Original creator: aginiewicz

Original creation time: 2009-06-20 08:22:16

Assignee: tbd

CC:  malb

singular is last package that don't compile with latest GCC 4.4 for me, it's because of use of strchr function, see GCC 4.4 [porting guide](http://gcc.gnu.org/gcc-4.4/porting_to.html) part "Strict null-terminated sequence utilities" - there is used

char* strchr(const char*, int)

that silently cast-away const, simple explicit cast to char* removes the error during compilation for me so it's trivial to fix. The strchr function in this form is used twice. 

I made spkg that's fixed, wasn't creating patches/spkg for Sage for some time so I ask for strict review even if it's trivial fix :) I tried to remember about everything with spkg creation but something could still slip. There is spkg: [http://giniu.ravenlord.ws/singular-3-1-0-2-20090620.spkg](http://giniu.ravenlord.ws/singular-3-1-0-2-20090620.spkg).


---

Comment by craigcitro created at 2009-06-20 08:27:02

I'm adding Martin to the cc here, because I think he's going to be looking at the Singular spkg soon (for #6240).


---

Comment by was created at 2009-06-20 10:31:13

I sent an email to singular`@`mathematik.uni-kl.de about this ticket as well.


---

Comment by john_perry created at 2009-06-21 22:21:29

The spkg allowed me to compile sage on my machine, and it appears to be working. What would constitute a strict test?


---

Comment by aginiewicz created at 2009-06-21 22:39:19

There is problem that one cannot provide testcase... i.e. the issue is during compile time, if the compiler allows used syntax, that is casting away const trough strchr function, it still generates code that's safe because in this code the pointer isn't used in any malicious way, so if it compiles - with or without patch - one cannot tell the difference, probably even looking at assembler code. But on other hand, GCC 4.4 don't allow implicit const cast-away trough string manipulation functions (which is good thing in my opinion) so it fails to build without patch.


---

Comment by was created at 2009-06-23 13:04:50

I told upstream about this bug and they replied:

```
Thanks for the patch - we agree with it
and have integrated it into Singular.
 -- Hans Schoenemann
```


That's a positive review from the singular project director.


---

Comment by aginiewicz created at 2009-06-25 17:44:21

Hmm... so this is positive review for patch, or we wait for upstream to fix it to not create too many patches?


---

Comment by malb created at 2009-06-25 17:57:59

We should patch it, but the next Singular SPKG needs a couple of other fixes applied (and updated to 3-1-0-4) this is I guess why it is taking so long.

My current attempt is here:

  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090611.spkg

It needs a fix applied where the ring variables print without a space. Do you want to merge your patch with that SPKG?

Martin


---

Comment by aginiewicz created at 2009-06-25 20:14:55

Sure, I will try to merge tomorrow in my local copy


---

Comment by aginiewicz created at 2009-06-26 18:16:18

Hmm... so fix for #6360 is no longer needed with 3-1-0-4? I ask because I noticed in your spkg fix for it is erased from mercurial history, i.e. the change by Craig from 19'th?


---

Comment by malb created at 2009-06-26 18:23:39

Good catch. It is still needed I just forgot to apply it!


---

Comment by aginiewicz created at 2009-06-26 20:58:36

Will you provide new version with this change (rebased on top of #6360?) or should I merge both to that gcc one? Sorry if this should be obvious, long break still have it's effects


---

Comment by malb created at 2009-06-26 23:32:34

Sorry, I was not very clear. It would be nice if you could re-merge it as I am in the middle of another project. If you can't get around to do it, I'll do it eventually.


---

Comment by aginiewicz created at 2009-06-27 07:35:48

No problem, I will take care of it then


---

Comment by aginiewicz created at 2009-06-27 08:44:52

I merged the changes with Martins version (rebased actually) - there is spkg - http://giniu.ravenlord.ws/singular-3-1-0-4-20090620.spkg


---

Comment by was created at 2009-07-01 11:08:56

Changing priority from major to blocker.


---

Comment by john_perry created at 2009-07-03 05:44:36

I checked the changes (after some tutoring from was and jhpalmieri) against the default package included with 4.0.2, released 18 Jun and against the source included with the spkg.

Is there an error in line 725 of patches/mpr_complex.cc? The original source file src/kernel/mpr_complex.cc contains

```
          sprintf(out,"%s",currRing->parameter[0]);
```

but the patch contains

```
          sprintf(out,currRing->parameter[0]);
```

What happened to the "%s"? I thought that was required.

Everything else looks fine.


---

Comment by aginiewicz created at 2009-07-03 12:27:32

... it must have slipped by, i.e. it was probably change upstream that I didn't noticed when merge of mine and Martins packages. I will take care of it right now.


---

Comment by aginiewicz created at 2009-07-03 13:25:29

Ok, fixed it. New spkg is at http://giniu.ravenlord.ws/singular-3-1-0-4-20090703.spkg


---

Comment by john_perry created at 2009-07-03 15:00:28

Looks good to me.


---

Comment by aginiewicz created at 2009-07-03 15:28:03

Fixed description in ticked to make sure which one is latest, as with Johns review link to spkg got reverted to not latest version.


---

Comment by rlm created at 2009-07-03 16:20:50

The spkg causes several doctest failures when built on sage-4.1.alpha3:

```
        sage -t -long devel/sage/sage/rings/quotient_ring.py # 1 doctests failed
        sage -t -long devel/sage/sage/rings/quotient_ring_element.py # 1 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/term_order.py # 1 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/polynomial_singular_interface.py # 6 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/pbori.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 11 doctests failed
        sage -t -long devel/sage/sage/interfaces/singular.py # 10 doctests failed
```


These all seem to be just from the way Singular is printing things, e.g.:

```
**********************************************************************
File "/space/rlm/sage-4.1.alpha3/devel/sage-main/sage/interfaces/singular.py", line 975:
    sage: singular.current_ring()
Expected:
    //   characteristic : 127
    //   number of vars : 3
    //        block   1 : ordering rp
    //                  : names    x y z
    //        block   2 : ordering C
Got:
    //   characteristic : 127
    //   number of vars : 3
    //        block   1 : ordering rp
    //                  : names    xyz
    //        block   2 : ordering C
**********************************************************************
```


I assume this is nothing major. If someone wants to post a patch, I will gladly finish the review.


---

Comment by aginiewicz created at 2009-07-03 16:37:56

Hmm... this must be what Martin was talking about with his spkg in [comment 7](http://trac.sagemath.org/sage_trac/ticket/6362#comment:7) above... will look into it right now


---

Comment by aginiewicz created at 2009-07-03 17:01:17

Ok, I found that upstream changed in kernel/ring.cc:370 the "Print("%s ",r->names[i]);" into "PrintS(r->names[i]);", I reverted the change and now building/testing. Will post fixed spkg just as it finishes


---

Comment by aginiewicz created at 2009-07-03 17:31:07

Fixed, thanks for report. I replaced the file at http://giniu.ravenlord.ws/singular-3-1-0-4-20090703.spkg with new version.


---

Comment by rlm created at 2009-07-03 17:33:00

Wouldn't it make more sense to not change things upstream, and just fix the doctests?


---

Comment by aginiewicz created at 2009-07-03 17:39:12

I guess the change looks like it wasn't intended, they massively changed Print("%s", ...) (without space after %s) and Print(...) into PrintS(...), printing variable names without spaces or any other means of separation between them doesn't seem like something anyone wants...

also, what about:

```
S = singular.ring('real', '(xx,yy)', 'lp')
```

vs

```
R = singular.ring('real', '(x,xyy)', 'lp')
```

that looks same when variables are printed without separation?


---

Comment by rlm created at 2009-07-03 18:32:21

Resolution: fixed


---

Comment by malb created at 2009-07-04 13:23:40

Replying to [comment:26 aginiewicz]:
> I guess the change looks like it wasn't intended

Indeed, I talked to upstream about it and they consider this a bug (which they fixed in CVS).


---

Comment by GeorgSWeber created at 2009-07-06 19:38:33

As contained in Sage-4.1.rc0, singular-3-1-0-4-20090703.spkg does not even build on OS X, neither 10.4 nor 10.5. Changing the line 201 in /src/factory/GNUmakefile.in:

```
factoryobj :=   $(factorysrc:%.cc=%.o) $(factorysrc:%.y=%.o)
```

into the following two lines:

```
factoryobj :=   $(factorysrc:%.cc=%.o)
factoryobj :=   $(factoryobj:%.y=%.o)
```

made the resulting Singular spkg build on OS X 10.4. But after installing it into Sage-4.1.rc0, Sage doesn't even start, it fails with:

```
ImportError: dlopen(/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so, 2): Symbol not found: ___eprintf
  Referenced from: /Users/Shared/sage/sage-4.1.rc0/local/lib//libsingular.dylib
  Expected in: dynamic lookup
```

This might be due to the fact that I had dropped in the 3.1.0.2 Singular spkg before, so I am re-running the build from the start. (I doubt that it'll help, but let's see.)

For the record, skipping through the install logs, I spotted another error (this time "copy'n'paste") in the Singular 3.1.0.4 build scripts. In /src/libfac/Makefile.in, the two identical lines 157/158 read:

```
	-$(RANLIB) ${libdir}/libsingfac_g.a
	-$(RANLIB) ${libdir}/libsingfac_g.a
```

and it is obvious from the surrounding lines, that the line 158 should end with "..._p.a" instead of "..._g.a".

`@`Martin:
Would you please report the findings so far upstream?


---

Comment by aginiewicz created at 2009-07-06 19:50:25

Replying to [comment:29 GeorgSWeber]:
> As contained in Sage-4.1.rc0, singular-3-1-0-4-20090703.spkg does not even build on OS X, neither 10.4 nor 10.5. Changing the line 201 in /src/factory/GNUmakefile.in:
> {{{
> factoryobj :=   $(factorysrc:%.cc=%.o) $(factorysrc:%.y=%.o)
> }}}
> into the following two lines:
> {{{
> factoryobj :=   $(factorysrc:%.cc=%.o)
> factoryobj :=   $(factoryobj:%.y=%.o)
> }}}
> made the resulting Singular spkg build on OS X 10.4. But after installing it into Sage-4.1.rc0, Sage doesn't even start, it fails with:
> {{{
> ImportError: dlopen(/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so, 2): Symbol not found: ___eprintf
>   Referenced from: /Users/Shared/sage/sage-4.1.rc0/local/lib//libsingular.dylib
>   Expected in: dynamic lookup
> }}}
> This might be due to the fact that I had dropped in the 3.1.0.2 Singular spkg before, so I am re-running the build from the start. (I doubt that it'll help, but let's see.)
> 
> For the record, skipping through the install logs, I spotted another error (this time "copy'n'paste") in the Singular 3.1.0.4 build scripts. In /src/libfac/Makefile.in, the two identical lines 157/158 read:
> {{{
> 	-$(RANLIB) ${libdir}/libsingfac_g.a
> 	-$(RANLIB) ${libdir}/libsingfac_g.a
> }}}
> and it is obvious from the surrounding lines, that the line 158 should end with "..._p.a" instead of "..._g.a".
> 
> `@`Martin:
> Would you please report the findings so far upstream?

Oh, that's something already... but anyway, if I can suggest something, maybe [#6470](http://trac.sagemath.org/sage_trac/ticket/6470) would be better for continuation of this (closed) ticket? It will be better exposed that way I think


---

Comment by GeorgSWeber created at 2009-07-06 20:11:39

Yes, let's continue at #6470. Thanks for pointing out to me the new ticket!

Cheers,
gsw
