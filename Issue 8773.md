# Issue 8773: GCC-4.5.0 breaks GAP -- the workspace is broken, hence gap('2+2') fails.

Issue created by migration from https://trac.sagemath.org/ticket/8773

Original creator: was

Original creation time: 2010-04-26 22:28:45

Assignee: GeorgSWeber

CC:  wjp

If you build GAP as part of sage-4.4 with GCC-4.5.0 (on lena):

```
[wstein@lena sage-4.4]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: gap('2+3')
A workspace appears to have been corrupted... automatically rebuilding (this is harmless).
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.4, Release Date: 2010-04-24                         |
| Type notebook() for the GUI, and license() for information.        |
/home/wstein/screen/lena/sage-4.4/<ipython console> in <module>()

/home/wstein/screen/lena/sage-4.4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1030
   1031         if isinstance(x, basestring):
-> 1032             return cls(self, x, name=name)
   1033         try:
   1034             return self._coerce_from_special_method(x)

/home/wstein/screen/lena/sage-4.4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1450                 self._session_number = -1
-> 1451                 raise TypeError, x
   1452         self._session_number = parent._session_number
   1453

TypeError: Unable to start gap
sage: gap('2+3')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/wstein/screen/lena/sage-4.4/<ipython console> in <module>()

/home/wstein/screen/lena/sage-4.4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1030
   1031         if isinstance(x, basestring):
-> 1032             return cls(self, x, name=name)
   1033         try:
   1034             return self._coerce_from_special_method(x)

/home/wstein/screen/lena/sage-4.4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1450                 self._session_number = -1
-> 1451                 raise TypeError, x
   1452         self._session_number = parent._session_number
   1453

TypeError: Unable to start gap
```


Exactly the same thing works fine with Sage-4.3.3 built using GCC-4.4.x on lena:

```
[wstein@lena sage-4.4]$ ../sage-4.3.3/sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: gap('2+3')
5
```

| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
Deleting workspaces, etc., doesn't help.   The GAP spkg is unchanged between these two versions of Sage.



---

Comment by was created at 2010-04-26 22:29:37

We've had this sort of problem (many times) before...

1. The first obvious thing to try is to rebuild with optimization off.

2. Then try to fix and simultaneously email Steve Linton.


---

Comment by was created at 2010-04-26 23:38:17

I tried building without -O2, and the problem vanishes.   I did this by *brutally* deleting -O2 everywhere in the src tree (!).   Then I built and now suddenly GAP works:

```
[wstein@lena sage-4.4]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: gap('2+2')
4
```



---

Comment by wjp created at 2010-04-28 00:40:29

The issue here seems to be that gap is returning a `StructInitInfo*` from `SyFindOrLinkGapRootFile` inside a char buffer. In the process of extracting the pointer again in `READ_GAP_ROOT`, gap might be breaking strict aliasing rules.

I think that ideally this method of returning values should be removed entirely (since it seems to serve no purpose), and `SyFindOrLinkGapRootFile` should just get an extra argument of type `StructInitInfo**` for returning this pointer.


Incidentally gcc 4.5.0 also complains about a similar issue in `SaveDouble`, `LoadDouble`. Although that seems to be currently working, using a union there might be safer than casting directly.


---

Comment by wjp created at 2010-04-28 16:00:38

Changing status from new to needs_review.


---

Comment by wjp created at 2010-04-28 16:00:38

Building on Dima's new p2 from #8774, I created a p3 that avoids the strict aliasing problems by cleaning up some of the code. I also un-pre-applied saveload.patch in src/, and cleaned up a number of files in src/tst/ (including the large `src/tst/GAP\ 4\ PPC`) which were somehow copied from src/.

New spkg at:

http://www.math.leidenuniv.nl/~wpalenst/sage/gap-4.4.12.p3.spkg


---

Comment by dimpase created at 2010-04-28 16:42:41

Changing priority from blocker to major.


---

Comment by dimpase created at 2010-04-28 16:42:41

Replying to [comment:5 wjp]:
> Building on Dima's new p2 from #8774, I created a p3 that avoids the strict aliasing problems by cleaning up some of the code. I also un-pre-applied saveload.patch in src/, and cleaned up a number of files in src/tst/ (including the large `src/tst/GAP\ 4\ PPC`) which were somehow copied from src/.
> 
> New spkg at:
> 
> http://www.math.leidenuniv.nl/~wpalenst/sage/gap-4.4.12.p3.spkg

this needs to be tested on every platform Sage supports, (itaniums, macs, sparcs...).

This is quite a drastic change, and there is no telling how older versions of gcc would cope!
I think it should get seen by real GAP kernel folks before we start even think of shipping this.

Should I post this on GAP-support, of which I happen to be a member?

Finally, I do not understand why it is a blocker. Is 4.4.1 going to support gcc-4.5.0 ?!
I would say that attempting to support gcc-***.0 is a waste of time.
Let it ripe to at least .1 or better .2...
I therefore lower the priority of this to major.

I would also propose another way to get it in Sage:   make these new patches conditional on gcc version >=4.5.
 
Dima


---

Comment by dimpase created at 2010-04-28 16:42:41

Changing status from needs_review to needs_work.


---

Comment by wjp created at 2010-04-28 16:52:11

Replying to [comment:6 dimpase]:
> this needs to be tested on every platform Sage supports, (itaniums, macs, sparcs...).
> 
> This is quite a drastic change, and there is no telling how older versions of gcc would cope!

Not so drastic, really. The changes are very much localised, and the new code is *far* less risky than the current version. Older versions of gcc should have no problem with it.I agree it needs testing on more platforms, of course.

> I think it should get seen by real GAP kernel folks before we start even think of shipping this.
> 
> Should I post this on GAP-support, of which I happen to be a member?

If you could, that would be great. Thanks.


> I would also propose another way to get it in Sage:   make these new patches conditional on gcc version >=4.5.

In my opinion writing such a check would cause more potential for trouble than the changes.

-Willem Jan


---

Comment by wjp created at 2010-04-28 17:07:22

P.S. The patch I added to this spkg likely doesn't satisfy gap's formatting/documentation/code conventions. It's intended as the least invasive way to fix the immediate problem, rather than as a way to clean up the offending code properly.


---

Comment by dimpase created at 2010-04-28 17:41:15

Replying to [comment:7 wjp]:
[...]
> > I would also propose another way to get it in Sage:   make these new patches conditional on gcc version >=4.5.
> 
> In my opinion writing such a check would cause more potential for trouble than the changes.

Hoezo, Willem Jan? :-)

You don't need to do #if 's in the code...
Get gcc version in spkg-install, and only apply new patches in case you get right version.
And print a warning that it's a new, not quite tested, stuff.
A couple lines of shell code...

Dima

> 
> -Willem Jan


---

Comment by was created at 2010-04-28 17:50:49

Replying to [comment:6 dimpase]:
> Replying to [comment:5 wjp]:
> > Building on Dima's new p2 from #8774, I created a p3 that avoids the strict aliasing problems by cleaning up some of the code. I also un-pre-applied saveload.patch in src/, and cleaned up a number of files in src/tst/ (including the large `src/tst/GAP\ 4\ PPC`) which were somehow copied from src/.
> > 
> > New spkg at:
> > 
> > http://www.math.leidenuniv.nl/~wpalenst/sage/gap-4.4.12.p3.spkg
> 
> this needs to be tested on every platform Sage supports, (itaniums, macs, sparcs...).
> 
> This is quite a drastic change, and there is no telling how older versions of gcc would cope!
> I think it should get seen by real GAP kernel folks before we start even think of shipping this.
> 
> Should I post this on GAP-support, of which I happen to be a member?
> 
> Finally, I do not understand why it is a blocker. Is 4.4.1 going to support gcc-4.5.0 ?!

Yes.

> I would say that attempting to support gcc-***.0 is a waste of time.

Not if it's what our clients want.


---

Comment by wjp created at 2010-04-28 18:08:25

Replying to [comment:9 dimpase]:
> Replying to [comment:7 wjp]:
> [...]
> > > I would also propose another way to get it in Sage:   make these new patches conditional on gcc version >=4.5.
> > 
> > In my opinion writing such a check would cause more potential for trouble than the changes.
>
> You don't need to do #if 's in the code...
> Get gcc version in spkg-install, and only apply new patches in case you get right version.
> And print a warning that it's a new, not quite tested, stuff.
> A couple lines of shell code...

Let me rephrase it: I don't think the changes are risky enough to justify having two separate versions of the code.


---

Comment by was created at 2010-04-28 18:55:28

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-04-28 18:55:37

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-28 18:57:43

Resolution: fixed


---

Comment by was created at 2010-04-28 19:15:24

From upstream, which approves:

```
Well done Willem. The diagnosis looks correct. This is old code and clearly the nice solution is to use a suitable union type so as to be more honest with the C compiler about what is actually being passed back and forth. Is there an easy way to pass me the proposed patch and I'll either apply it to GAP development branch or send you a preferred version if I want to do it a little differently.

SaveDouble/LoadDouble can probably also be handled correctly with unions, so long as, in

union { char bytes[sizeof(double)], double d};


one can rely on bytes including all the data of double. Does anyone know anything about this? Otherwise might be better to use void * and memcopy or something like that.

       Steve
```



---

Comment by was created at 2010-04-28 19:16:47

More readable:
"Well done Willem. The diagnosis looks correct. This is old code and clearly the nice solution is to use a suitable union type so as to be more honest with the C compiler about what is actually being passed back and forth. Is there an easy way to pass me the proposed patch and I'll either apply it to GAP development branch or send you a preferred version if I want to do it a little differently.

SaveDouble/LoadDouble can probably also be handled correctly with unions, so long as, in

```
union { char bytes[sizeof(double)], double d};
```


one can rely on bytes including all the data of double. Does anyone know anything about this? Otherwise might be better to use void * and memcopy or something like that.

       Steve"


---

Comment by dimpase created at 2010-05-01 12:27:29

for the record:

the saveload.patch is still needed on ia64 (Itanium).
The symptom (corrupt GAP workspace names created
by GAP's SaveWorkspace) reappears if I unapply it, 
so the problem didn't go away after the strict aliases patch.
