# Issue 8773: GCC-4.5.0 breaks GAP -- the workspace is broken, hence gap('2+2') fails.

archive/issues_008773.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @wjp\n\nIf you build GAP as part of sage-4.4 with GCC-4.5.0 (on lena):\n\n```\n[wstein@lena sage-4.4]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: gap('2+3')\nA workspace appears to have been corrupted... automatically rebuilding (this is harmless).\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n| Sage Version 4.4, Release Date: 2010-04-24                         |\n| Type notebook() for the GUI, and license() for information.        |\n/home/wstein/screen/lena/sage-4.4/<ipython console> in <module>()\n\n/home/wstein/screen/lena/sage-4.4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)\n   1030\n   1031         if isinstance(x, basestring):\n-> 1032             return cls(self, x, name=name)\n   1033         try:\n   1034             return self._coerce_from_special_method(x)\n\n/home/wstein/screen/lena/sage-4.4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)\n   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:\n   1450                 self._session_number = -1\n-> 1451                 raise TypeError, x\n   1452         self._session_number = parent._session_number\n   1453\n\nTypeError: Unable to start gap\nsage: gap('2+3')\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/wstein/screen/lena/sage-4.4/<ipython console> in <module>()\n\n/home/wstein/screen/lena/sage-4.4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)\n   1030\n   1031         if isinstance(x, basestring):\n-> 1032             return cls(self, x, name=name)\n   1033         try:\n   1034             return self._coerce_from_special_method(x)\n\n/home/wstein/screen/lena/sage-4.4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)\n   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:\n   1450                 self._session_number = -1\n-> 1451                 raise TypeError, x\n   1452         self._session_number = parent._session_number\n   1453\n\nTypeError: Unable to start gap\n```\n\n\nExactly the same thing works fine with Sage-4.3.3 built using GCC-4.4.x on lena:\n\n```\n[wstein@lena sage-4.4]$ ../sage-4.3.3/sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: gap('2+3')\n5\n```\n\n| Sage Version 4.3.3, Release Date: 2010-02-21                       |\n| Type notebook() for the GUI, and license() for information.        |\nDeleting workspaces, etc., doesn't help.   The GAP spkg is unchanged between these two versions of Sage.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8773\n\n",
    "created_at": "2010-04-26T22:28:45Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "GCC-4.5.0 breaks GAP -- the workspace is broken, hence gap('2+2') fails.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8773",
    "user": "https://github.com/williamstein"
}
```
Assignee: GeorgSWeber

CC:  @wjp

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


Issue created by migration from https://trac.sagemath.org/ticket/8773





---

archive/issue_comments_080165.json:
```json
{
    "body": "We've had this sort of problem (many times) before...\n\n1. The first obvious thing to try is to rebuild with optimization off.\n\n2. Then try to fix and simultaneously email Steve Linton.",
    "created_at": "2010-04-26T22:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80165",
    "user": "https://github.com/williamstein"
}
```

We've had this sort of problem (many times) before...

1. The first obvious thing to try is to rebuild with optimization off.

2. Then try to fix and simultaneously email Steve Linton.



---

archive/issue_comments_080166.json:
```json
{
    "body": "I tried building without -O2, and the problem vanishes.   I did this by *brutally* deleting -O2 everywhere in the src tree (!).   Then I built and now suddenly GAP works:\n\n```\n[wstein@lena sage-4.4]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: gap('2+2')\n4\n```\n",
    "created_at": "2010-04-26T23:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80166",
    "user": "https://github.com/williamstein"
}
```

I tried building without -O2, and the problem vanishes.   I did this by *brutally* deleting -O2 everywhere in the src tree (!).   Then I built and now suddenly GAP works:

```
[wstein@lena sage-4.4]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: gap('2+2')
4
```




---

archive/issue_comments_080167.json:
```json
{
    "body": "The issue here seems to be that gap is returning a `StructInitInfo*` from `SyFindOrLinkGapRootFile` inside a char buffer. In the process of extracting the pointer again in `READ_GAP_ROOT`, gap might be breaking strict aliasing rules.\n\nI think that ideally this method of returning values should be removed entirely (since it seems to serve no purpose), and `SyFindOrLinkGapRootFile` should just get an extra argument of type `StructInitInfo**` for returning this pointer.\n\n\nIncidentally gcc 4.5.0 also complains about a similar issue in `SaveDouble`, `LoadDouble`. Although that seems to be currently working, using a union there might be safer than casting directly.",
    "created_at": "2010-04-28T00:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80167",
    "user": "https://github.com/wjp"
}
```

The issue here seems to be that gap is returning a `StructInitInfo*` from `SyFindOrLinkGapRootFile` inside a char buffer. In the process of extracting the pointer again in `READ_GAP_ROOT`, gap might be breaking strict aliasing rules.

I think that ideally this method of returning values should be removed entirely (since it seems to serve no purpose), and `SyFindOrLinkGapRootFile` should just get an extra argument of type `StructInitInfo**` for returning this pointer.


Incidentally gcc 4.5.0 also complains about a similar issue in `SaveDouble`, `LoadDouble`. Although that seems to be currently working, using a union there might be safer than casting directly.



---

archive/issue_comments_080168.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-28T16:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80168",
    "user": "https://github.com/wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080169.json:
```json
{
    "body": "Building on Dima's new p2 from #8774, I created a p3 that avoids the strict aliasing problems by cleaning up some of the code. I also un-pre-applied saveload.patch in src/, and cleaned up a number of files in src/tst/ (including the large `src/tst/GAP\\ 4\\ PPC`) which were somehow copied from src/.\n\nNew spkg at:\n\nhttp://www.math.leidenuniv.nl/~wpalenst/sage/gap-4.4.12.p3.spkg",
    "created_at": "2010-04-28T16:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80169",
    "user": "https://github.com/wjp"
}
```

Building on Dima's new p2 from #8774, I created a p3 that avoids the strict aliasing problems by cleaning up some of the code. I also un-pre-applied saveload.patch in src/, and cleaned up a number of files in src/tst/ (including the large `src/tst/GAP\ 4\ PPC`) which were somehow copied from src/.

New spkg at:

http://www.math.leidenuniv.nl/~wpalenst/sage/gap-4.4.12.p3.spkg



---

archive/issue_comments_080170.json:
```json
{
    "body": "Replying to [comment:5 wjp]:\n> Building on Dima's new p2 from #8774, I created a p3 that avoids the strict aliasing problems by cleaning up some of the code. I also un-pre-applied saveload.patch in src/, and cleaned up a number of files in src/tst/ (including the large `src/tst/GAP\\ 4\\ PPC`) which were somehow copied from src/.\n> \n> New spkg at:\n> \n> http://www.math.leidenuniv.nl/~wpalenst/sage/gap-4.4.12.p3.spkg\n\nthis needs to be tested on every platform Sage supports, (itaniums, macs, sparcs...).\n\nThis is quite a drastic change, and there is no telling how older versions of gcc would cope!\nI think it should get seen by real GAP kernel folks before we start even think of shipping this.\n\nShould I post this on GAP-support, of which I happen to be a member?\n\nFinally, I do not understand why it is a blocker. Is 4.4.1 going to support gcc-4.5.0 ?!\nI would say that attempting to support gcc-***.0 is a waste of time.\nLet it ripe to at least .1 or better .2...\nI therefore lower the priority of this to major.\n\nI would also propose another way to get it in Sage:   make these new patches conditional on gcc version >=4.5.\n \nDima",
    "created_at": "2010-04-28T16:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80170",
    "user": "https://github.com/dimpase"
}
```

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

archive/issue_comments_080171.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-28T16:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80171",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080172.json:
```json
{
    "body": "Replying to [comment:6 dimpase]:\n> this needs to be tested on every platform Sage supports, (itaniums, macs, sparcs...).\n> \n> This is quite a drastic change, and there is no telling how older versions of gcc would cope!\n\nNot so drastic, really. The changes are very much localised, and the new code is *far* less risky than the current version. Older versions of gcc should have no problem with it.I agree it needs testing on more platforms, of course.\n\n> I think it should get seen by real GAP kernel folks before we start even think of shipping this.\n> \n> Should I post this on GAP-support, of which I happen to be a member?\n\nIf you could, that would be great. Thanks.\n\n\n> I would also propose another way to get it in Sage:   make these new patches conditional on gcc version >=4.5.\n\nIn my opinion writing such a check would cause more potential for trouble than the changes.\n\n-Willem Jan",
    "created_at": "2010-04-28T16:52:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80172",
    "user": "https://github.com/wjp"
}
```

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

archive/issue_comments_080173.json:
```json
{
    "body": "P.S. The patch I added to this spkg likely doesn't satisfy gap's formatting/documentation/code conventions. It's intended as the least invasive way to fix the immediate problem, rather than as a way to clean up the offending code properly.",
    "created_at": "2010-04-28T17:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80173",
    "user": "https://github.com/wjp"
}
```

P.S. The patch I added to this spkg likely doesn't satisfy gap's formatting/documentation/code conventions. It's intended as the least invasive way to fix the immediate problem, rather than as a way to clean up the offending code properly.



---

archive/issue_comments_080174.json:
```json
{
    "body": "Replying to [comment:7 wjp]:\n[...]\n> > I would also propose another way to get it in Sage:   make these new patches conditional on gcc version >=4.5.\n> \n> In my opinion writing such a check would cause more potential for trouble than the changes.\n\nHoezo, Willem Jan? :-)\n\nYou don't need to do #if 's in the code...\nGet gcc version in spkg-install, and only apply new patches in case you get right version.\nAnd print a warning that it's a new, not quite tested, stuff.\nA couple lines of shell code...\n\nDima\n\n> \n> -Willem Jan",
    "created_at": "2010-04-28T17:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80174",
    "user": "https://github.com/dimpase"
}
```

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

archive/issue_comments_080175.json:
```json
{
    "body": "Replying to [comment:6 dimpase]:\n> Replying to [comment:5 wjp]:\n> > Building on Dima's new p2 from #8774, I created a p3 that avoids the strict aliasing problems by cleaning up some of the code. I also un-pre-applied saveload.patch in src/, and cleaned up a number of files in src/tst/ (including the large `src/tst/GAP\\ 4\\ PPC`) which were somehow copied from src/.\n> > \n> > New spkg at:\n> > \n> > http://www.math.leidenuniv.nl/~wpalenst/sage/gap-4.4.12.p3.spkg\n> \n> this needs to be tested on every platform Sage supports, (itaniums, macs, sparcs...).\n> \n> This is quite a drastic change, and there is no telling how older versions of gcc would cope!\n> I think it should get seen by real GAP kernel folks before we start even think of shipping this.\n> \n> Should I post this on GAP-support, of which I happen to be a member?\n> \n> Finally, I do not understand why it is a blocker. Is 4.4.1 going to support gcc-4.5.0 ?!\n\nYes.\n\n> I would say that attempting to support gcc-***.0 is a waste of time.\n\nNot if it's what our clients want.",
    "created_at": "2010-04-28T17:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80175",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_080176.json:
```json
{
    "body": "Replying to [comment:9 dimpase]:\n> Replying to [comment:7 wjp]:\n> [...]\n> > > I would also propose another way to get it in Sage:   make these new patches conditional on gcc version >=4.5.\n> > \n> > In my opinion writing such a check would cause more potential for trouble than the changes.\n>\n> You don't need to do #if 's in the code...\n> Get gcc version in spkg-install, and only apply new patches in case you get right version.\n> And print a warning that it's a new, not quite tested, stuff.\n> A couple lines of shell code...\n\nLet me rephrase it: I don't think the changes are risky enough to justify having two separate versions of the code.",
    "created_at": "2010-04-28T18:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80176",
    "user": "https://github.com/wjp"
}
```

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

archive/issue_comments_080177.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-28T18:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80177",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080178.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-28T18:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80178",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080179.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-28T18:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80179",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_080180.json:
```json
{
    "body": "From upstream, which approves:\n\n```\nWell done Willem. The diagnosis looks correct. This is old code and clearly the nice solution is to use a suitable union type so as to be more honest with the C compiler about what is actually being passed back and forth. Is there an easy way to pass me the proposed patch and I'll either apply it to GAP development branch or send you a preferred version if I want to do it a little differently.\n\nSaveDouble/LoadDouble can probably also be handled correctly with unions, so long as, in\n\nunion { char bytes[sizeof(double)], double d};\n\n\none can rely on bytes including all the data of double. Does anyone know anything about this? Otherwise might be better to use void * and memcopy or something like that.\n\n       Steve\n```\n",
    "created_at": "2010-04-28T19:15:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80180",
    "user": "https://github.com/williamstein"
}
```

From upstream, which approves:

```
Well done Willem. The diagnosis looks correct. This is old code and clearly the nice solution is to use a suitable union type so as to be more honest with the C compiler about what is actually being passed back and forth. Is there an easy way to pass me the proposed patch and I'll either apply it to GAP development branch or send you a preferred version if I want to do it a little differently.

SaveDouble/LoadDouble can probably also be handled correctly with unions, so long as, in

union { char bytes[sizeof(double)], double d};


one can rely on bytes including all the data of double. Does anyone know anything about this? Otherwise might be better to use void * and memcopy or something like that.

       Steve
```




---

archive/issue_comments_080181.json:
```json
{
    "body": "More readable:\n\"Well done Willem. The diagnosis looks correct. This is old code and clearly the nice solution is to use a suitable union type so as to be more honest with the C compiler about what is actually being passed back and forth. Is there an easy way to pass me the proposed patch and I'll either apply it to GAP development branch or send you a preferred version if I want to do it a little differently.\n\nSaveDouble/LoadDouble can probably also be handled correctly with unions, so long as, in\n\n```\nunion { char bytes[sizeof(double)], double d};\n```\n\n\none can rely on bytes including all the data of double. Does anyone know anything about this? Otherwise might be better to use void * and memcopy or something like that.\n\n       Steve\"",
    "created_at": "2010-04-28T19:16:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80181",
    "user": "https://github.com/williamstein"
}
```

More readable:
"Well done Willem. The diagnosis looks correct. This is old code and clearly the nice solution is to use a suitable union type so as to be more honest with the C compiler about what is actually being passed back and forth. Is there an easy way to pass me the proposed patch and I'll either apply it to GAP development branch or send you a preferred version if I want to do it a little differently.

SaveDouble/LoadDouble can probably also be handled correctly with unions, so long as, in

```
union { char bytes[sizeof(double)], double d};
```


one can rely on bytes including all the data of double. Does anyone know anything about this? Otherwise might be better to use void * and memcopy or something like that.

       Steve"



---

archive/issue_comments_080182.json:
```json
{
    "body": "for the record:\n\nthe saveload.patch is still needed on ia64 (Itanium).\nThe symptom (corrupt GAP workspace names created\nby GAP's SaveWorkspace) reappears if I unapply it, \nso the problem didn't go away after the strict aliases patch.",
    "created_at": "2010-05-01T12:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8773#issuecomment-80182",
    "user": "https://github.com/dimpase"
}
```

for the record:

the saveload.patch is still needed on ia64 (Itanium).
The symptom (corrupt GAP workspace names created
by GAP's SaveWorkspace) reappears if I unapply it, 
so the problem didn't go away after the strict aliases patch.
