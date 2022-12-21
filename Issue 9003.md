# Issue 9003: Doctest failure on Mac PPC in free_module.py

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-05-21 00:04:26

Assignee: tbd

On Mac PPC G4 with 10.4:

```
sage -t  "devel/sage/sage/modules/free_module.py"           
**********************************************************************
    sage: V.base_extend(QQ)
Expected:
    Vector space of dimension 7 over Rational Field
Got:
    V
**********************************************************************
```




---

Comment by justin created at 2010-05-21 14:06:59

I have the same failure testing sage 4.4.2 (32-bit) on Mac OS X, 10.5.8, on a Mac Pro (Dual Quad Xeon).


---

Comment by GeorgSWeber created at 2010-05-21 16:24:14

The same occurs for Sage-4.4.2 on 32bit MacIntel OS X 10.4.

On that very system, Sage-4.4.2.rc0 did *not* show this error.


---

Comment by kcrisman created at 2010-05-21 16:36:59

So on 10.4 and 10.5, but not on OS X 10.6.  Very interesting.  I don't have time to look at this now, but will be happy to test.  Given that the changes from rc0 to final [http://groups.google.com/group/sage-release/msg/45369d3053275b58?](http://groups.google.com/group/sage-release/msg/45369d3053275b58?)  are all in documentation, this seems strange.


---

Comment by fwclarke created at 2010-05-22 09:14:18

I *don't* get this failure with 32 bit 4.4 built from source on a  1.8 GHz PowerPC G5 running Mac OS X 10.5.8


---

Comment by GeorgSWeber created at 2010-05-22 20:28:59

Guys, this problem is *by far* worse than I ever thought! I changed the lines 1124ff in question in "modules/free_module.py" to:

```
            sage: V = ZZ^7; V
            Ambient free module of rank 7 over the principal ideal domain Integer Ring
            sage: W = V.base_extend(QQ)
            sage: W._repr_()
            'Vector space of dimension 7 over Rational Field'
            sage: W
            Vector space of dimension 7 over Rational Field
```


and this is the one failing doctest I get when running "sage -t -verbose "devel/sage/sage/modules/free_module.py"":

```
Trying:
    set_random_seed(0L)
Expecting nothing
ok
Trying:
    change_warning_output(sys.stdout)
Expecting nothing
ok
Trying:
    V = ZZ**Integer(7); V###line 1124:_sage_    >>> V = ZZ^7; V
Expecting:
    Ambient free module of rank 7 over the principal ideal domain Integer Ring
ok
Trying:
    W = V.base_extend(QQ)###line 1126:_sage_    >>> W = V.base_extend(QQ)
Expecting nothing
ok
Trying:
    W._repr_()###line 1127:_sage_    >>> W._repr_()
Expecting:
    'Vector space of dimension 7 over Rational Field'
ok
Trying:
    W###line 1129:_sage_    >>> W
Expecting:
    Vector space of dimension 7 over Rational Field
**********************************************************************
File "/Users/Shared/sage/test/sage-4.4.2/devel/sage/sage/modules/free_module.py", line 924, in __main__.example_23
Failed example:
    W###line 1129:_sage_    >>> W
Expected:
    Vector space of dimension 7 over Rational Field
Got:
    V
```

Unbelievable!

The problem seems to lie within the doctest framework ... does anybody has experience with that? I think I stumbled once upon a time over temporary files from doctests, does anyone remember where these are stored?


---

Comment by GeorgSWeber created at 2010-05-22 20:35:02

Oh, I should add that from within Sage (command line/interpreter), everything is OK ...


---

Comment by klee created at 2010-05-25 15:18:09

My system is Mac Pro, Quad-core Intel Xeon 64bit, Snow Leopard. With Sage 4.4.2, I don't have this doctest failure. But strangely enough, if I apply a patch for other purpose, I have the doctest failure. It is reproducible. The patch mainly touches sage/rings/polynomial/term_order.py, and is now attached to the ticket #6922.


---

Comment by kcrisman created at 2010-05-25 15:48:09

Thanks, klee, hopefully this will help us track it down.

Replying to [comment:3 kcrisman]:
> So on 10.4 and 10.5, but not on OS X 10.6.  Very interesting.  I don't have time to look at this now, but will be happy to test.  Given that the changes from rc0 to final [http://groups.google.com/group/sage-release/msg/45369d3053275b58?](http://groups.google.com/group/sage-release/msg/45369d3053275b58?)  are all in documentation, this seems strange.

Here they are:

```
#8915: Mike Zabrocki: improve documentation on combinat.dyck_words [Reviewed by Minh Van Nguyen, Sébastien Labbé] 
#8919: William Laffin: documetation error in super_categories for Sets [Reviewed by Minh Van Nguyen] 
#8964: Jason Grout: Two small typos [Reviewed by Francis Clarke] 
#8979: André-Patrick Bubel: spelling mistake in sage/gsl/ode.pyx [Reviewed by Minh Van Nguyen] 
#8990: Georg S. Weber: update MPIR 1.2.2 license information as requested by upstream [Reviewed by Minh Van Nguyen] 
#8991: Rob Beezer: Adjust developer walkthrough for two changes to mercurial queues syntax [Reviewed by Arthur Lubovsky] 
```

I'll try to revert some of these and see if that helps track it down.


---

Comment by kcrisman created at 2010-05-26 02:57:24

After much testing, I am pretty certain that the error is caused by revision 14321.  You may ask what that revision looks like.  

```
changeset:   14321:1451c00a8d44
tag:         tip
user:        Minh Van Nguyen <nguyenminh2`@`gmail.com>
date:        Wed May 19 00:55:29 2010 -0700
summary:     4.4.2

diff -r 26a4be28b4ef -r 1451c00a8d44 sage/version.py
--- a/sage/version.py   Wed May 19 00:55:29 2010 -0700
+++ b/sage/version.py   Wed May 19 00:55:29 2010 -0700
`@``@` -1,2 +1,2 `@``@`
 """nodoctests"""
-version='4.4.2.rc0'; date='2010-05-12'
+version='4.4.2'; date='2010-05-19'

```

WHAT???

But on my OSX 10.4.11 PPC G4 at 1.25 GHz, that very last change to get to Sage 4.4.2 is what does it.   Combine that with klee's report, and I am totally baffled.  Is it possible that some weird cumulative change could cause a weird overflow or something along the lines of what GeorgSWeber is suggesting?


---

Comment by craigcitro created at 2010-05-26 06:38:38

I haven't been following this ticket (or the sage-release thread), but just a random idea to throw out there: is there any chance that one or more of those quote characters is actually in a different character set, or something else like that?


---

Comment by wjp created at 2010-05-26 09:24:03

Replying to [comment:5 GeorgSWeber]:
> The problem seems to lie within the doctest framework ... does anybody has experience with that? I think I stumbled once upon a time over temporary files from doctests, does anyone remember where these are stored?

In this case, it should be `~/.sage/tmp/.doctest_free_module.py`. It's only kept after failing tests, I believe.


---

Comment by leif created at 2010-05-26 12:16:05

Replying to [comment:10 craigcitro]:
> I haven't been following this ticket (or the sage-release thread), but just a random idea to throw out there: is there any chance that one or more of those quote characters is actually in a different character set, or something else like that? 

(At least) `version.py` does not contain any non-ASCII characters.


---

Comment by GeorgSWeber created at 2010-05-26 15:15:08

To add to the confusion (or is this enlightening for somebody?), here is what happened when I revisited the issue, freshly firing up Sage-4.4.2:

```
georg-webers-computer:~ georgweber$ cd ../Shared/sage/sage-4.4.2
georg-webers-computer:/Users/Shared/sage/sage-4.4.2 georgweber$ ./sage -t devel/sage/sage/modules/free_module.py
sage -t  "devel/sage/sage/modules/free_module.py"           
         [60.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 60.5 seconds
georg-webers-computer:/Users/Shared/sage/sage-4.4.2 georgweber$ ./sage -t devel/sage/sage/modules/free_module.py
sage -t  "devel/sage/sage/modules/free_module.py"           
**********************************************************************
File "/Users/Shared/sage/test/sage-4.4.2/devel/sage/sage/modules/free_module.py", line 1129:
    sage: W
Expected:
    Vector space of dimension 7 over Rational Field
Got:
    V
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_23
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/georgweber/.sage//tmp/.doctest_free_module.py
         [34.7 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/modules/free_module.py"
Total time for all tests: 34.7 seconds
```

So the very first attempt was successful! However it took much time. I think this is due to the fact that quite some libraries have to be loaded to memory, which is not anymore the case for the subsequent tests (where the needed libraries are already present). After this first successful run, *all* directly following runs fail (I just tried a couple of times, only the first one is attached above). Note that I did let run the tests without doing any changes to code in between (you might notice that I had let run the doctest on file like I had changed it); I just used "arrow up" in the terminal to get the last command and re-issued it, immediately after the first one.

So if anybody is doing tests w.r.t. this issue, please keep in mind that the "history" does seem to matter, i.e. whether the system was just started up, or whether already test have been running!

Since Kwankyu Lee reported above that he could "get" this issue on OS X 64bit (with Sage-4.4.2, after applying a seemingly totally unrelated patch to it) also, I altered the title line a bit.


---

Comment by GeorgSWeber created at 2010-05-26 15:50:25

Karl-Dieter, I can confirm your finding. More precisely, on a fresh clone made in Sage-4.4.2, I did "hg update -r 14320", i.e. reverting only the last change in version.py. Then I did "sage -b", and (only) version.py got updated.

And then, doctesting "free_module.py" succeeds (I tried it several times)!

Double-check: Doing "hg update -r 14321" (and then "sage -b", which touches only version.py), and after that --- doctesting "free_module.py" fails again (I also tested several times) ... 

BTW, thanks for the tip w.r.t. the "dot" doctest files --- I found it exactly there, under "~/.sage/tmp/.doctest_free_module.py". It looks totally innocent to me, however (the failing doctest is "example_23").


---

Comment by wjp created at 2010-05-26 15:59:03

That is really bizarre... is it the change to version or to date in version.py that breaks it? Does it depend on the length of the date and/or version strings, or the content?


---

Comment by GeorgSWeber created at 2010-05-26 16:06:23

Some more tapping around in the dark:

```
        EXAMPLES::
        
            sage: testname = ZZ^7
            sage: testname.base_extend(QQ)
            Vector space of dimension 7 over Rational Field
```

gives:

```
**********************************************************************
File "/Users/Shared/sage/test/sage-4.4.2/devel/sage/sage/modules/free_module.py", line 1125:
    sage: testname.base_extend(QQ)
Expected:
    Vector space of dimension 7 over Rational Field
Got:
    V
**********************************************************************
```

Amazing. Now try a bit "Eau de Cologne":

```
        EXAMPLES::
        
            sage: testname = ZZ^4711
            sage: testname.base_extend(QQ)
            Vector space of dimension 4711 over Rational Field
```

and this gives (repeatedly, several times):

```
sage -t  "devel/sage/sage/modules/free_module.py"           
         [35.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 35.3 seconds
```

Hmm, I've got to stop here for today, but the next thing one might check, is whether in (the doctest file of) free_module.py, somewhere there is *another* "ZZ^7" lurking with the name of "V", getting loaded/dumped or something like that ...


---

Comment by GeorgSWeber created at 2010-05-26 16:08:10

Ups, I meant to write "ZZ to the power of seven" ...


---

Comment by leif created at 2010-05-26 16:10:52

And keep in mind this error seems to only occur on MacOS...


---

Comment by wjp created at 2010-05-26 16:19:02

Replying to [comment:16 GeorgSWeber]:
>
> Hmm, I've got to stop here for today, but the next thing one might check, is whether in (the doctest file of) free_module.py, somewhere there is *another* `"ZZ^7"` lurking with the name of "V", getting loaded/dumped or something like that ...

That sounds like a very good idea.

Elsewhere in the file is an example renaming `QQ^7` to V...


---

Comment by GeorgSWeber created at 2010-05-26 21:21:39

Ah, I should have worked on a different project, but just couldn't.
Currently, I know the following:

 * There is a line `V = QQ^7` elsewhere in the same doctest
 * Sage stores free modules of some rank over some ring only once, see free_module.py/factory.pyx
 * so if `testname = ZZ^7`, then `testname.base_extend(QQ)` will refer to the same object as V before (!), albeit there is some "weakref" magic I don't understand
 * in this factory.pyx and weakref magic, the version number of Sage plays some role unclear to me (but at least there is some hint to from where the difference comes)
 * if the Sage version reads '4.4.2', then this object above has during the evalution in the doctest an attribute "`__custom_name`" set to the string "V", so this is why "V" is printed (as is clear from "sage_object.pyx", see `__repr__()` there)
 * after the *only* change making the Sage version to be '4.4.2.rc0' (note that the item after the last dot is not a number ...), then this object during evaluation of the doctest does not have this attribute "`__custom_name`" (direct evaluation now gives an AttributeError)

IMPORTANT NOTE: If one takes Sage-4.4.2.alpha0, and just alters in version.py the Sage version to read something with numbers only (e.g. "4.4.2"), then the bug becomes visible! So the problem must be in one of the patches in between Sage-4.4.1 and Sage-4.4.2.alpha0 --- and was only "shadowed" by the version number ending with a string (see factory.pyx lines 8 - 14 why this might be relevant --- I do not really know, why this hurts ... possibly garbage collection/weakref somehow acting differently, since the string "alpha0" (or "rc0") *is* being referenced?)


---

Comment by craigcitro created at 2010-05-27 06:59:30

Well, I can tell you _some_ of what's going on, but I don't know the whole story. First, here's an easy band-aid that doesn't fix the problem, but covers it up: in the doctest block for `rename` (around line 4440), add an extra doctest that changes the name back to the appropriate thing.

Here are some interesting facts:

 * the failure is coming from the code around line 4440, with the call to `V.rename('V')`. (Someone pointed this out above.) Sage knows that there's only one vector space over `QQ` of dimension 7, so it's keeping the same object around and returning it in both cases -- but it's been renamed in one case, so that shows up in the other one.
 * running `sage -t -verbose free_module.py` shows that even though the `rename` doctest comes later in the file than the `base_extend` one, it actually gets run before. This is because the generated functions get their doctests run in alphabetical order by name -- and `example_127` gets run before `example_23`. (Those are the numbers on my machine, anyway.) 
 * this also hints as to why it has something to do  with the version: as Georg noted above, the version gets used as part of the key for objects handled by the factory code. 
 * Deleting any whole doctest block above the `base_change` method seem to cover up the issue when running `sage -t`. 
 * It doesn't always cover it up with `sage -t -verbose` -- there are cases where `sage -t` succeeds, but `sage -t -verbose` fails. That's really fishy.

That said, I *totally* can't explain the whole story. I'd love to take some time to debug this, but I just don't have time right now -- if it's still sitting in a week or so, I'll try and dig further. The first thing I'd try next is to print the version in the factory `__call__` method, see if we can spot where it's not the value we expect. I also have no idea why applying the patches from #6922 changes this. 

I can't wait for someone to get to the bottom of this. `;)`


---

Comment by wjp created at 2010-05-27 21:56:32

I can't really think of anything other than seemingly unrelated things affecting the garbage collector somehow... I think avoiding renaming an object used in a different doctest should be a safe solution. (Patch attached.)


---

Attachment


---

Comment by wjp created at 2010-05-27 21:57:10

Changing status from new to needs_review.


---

Comment by leif created at 2010-05-27 22:07:48

Replying to [comment:22 wjp]:
> I can't really think of anything other than seemingly unrelated things affecting the garbage collector somehow... I think avoiding renaming an object used in a different doctest should be a safe solution. (Patch attached.)

Does this solve the problem, or just its symptoms? ;-)

I wonder if only the doctesting is affected...


---

Comment by wjp created at 2010-05-27 22:19:32

If I understand it correctly, the only reason that it works on other systems is that the garbage collector deletes an object (`QQ^7`) between the two doctests. I think it would be safer not to depend on that.


---

Comment by craigcitro created at 2010-05-27 22:36:25

Replying to [comment:25 wjp]:
> If I understand it correctly, the only reason that it works on other systems is that the garbage collector deletes an object (`QQ^7`) between the two doctests. I think it would be safer not to depend on that.

Actually, I don't know that it's the garbage collector:


```
sage: V = QQ^7
sage: V.rename('foo')
sage: V
foo
sage: del V
sage: import gc
sage: gc.collect()
54
sage: QQ^7
foo
```


Of course, maybe I'm tricking myself because something else is holding onto a non-weakref that prevents the stored `V` from being collected?

That said, I think the answer to Leif's question above is "yes and no." I think this *will* fix the issue for now, which is good. On the other hand, I think there still are weirdnesses lurking that should be investigated ... or at least explained to me if they're already understood. `;)`

It can't _just_ be the garbage collector -- the fact that the version strings were futzing with it means that it somehow has to intersect with weirdness related to pickling ... maybe because of the pickle jar? In any event, there's some weird behavior, and we should open a ticket to ferret out that weird behavior. Once that's open, I say positive review and merge Willem Jan's patch ...


---

Comment by wjp created at 2010-05-27 22:56:46

I think the ipython/sage output history might still be holding a ref there:


```
sage: V = QQ^7
sage: V.rename('foo')
sage: del V
sage: import gc
sage: gc.collect()
60
sage: QQ^7
Vector space of dimension 7 over Rational Field
sage: V = QQ^7
sage: V.rename('foo')
sage: V
foo
sage: import gc
sage: gc.collect()
9
sage: QQ^7
foo
```


(I left out printing V the first time.)


I don't understand the impact of the version either... It might just be affecting the GC algorithm in some subtle way due to different memory usage, but I realize that's next to impossible to verify.


---

Comment by craigcitro created at 2010-05-27 23:26:02

Replying to [comment:27 wjp]:
> I think the ipython/sage output history might still be holding a ref there:
> 

That's right, I think there's an IPython variable called `Out` -- but deleting the reference in there doesn't do it once it's been printed ... apparently something else is holding one, too. 

Even still, though, it's printed by the doctests -- so if whoever is holding on to it is part of Python and not just IPython, we'd still hit the same issue.


---

Comment by kcrisman created at 2010-06-14 13:58:31

What is the status of this - does it need review, or need work (the latter seems indicated by the last few comments)?


---

Comment by wjp created at 2010-06-14 14:36:41

As far as I'm concerned it still needs review.

Right now in one doctest `QQ^7` is renamed, and in another doctest we depend on `QQ^7` having its original name. I don't have any further ideas on how to exactly track down which aspect of the GC is responsible for the different behaviour on different systems, but at this point I have no reason to suspect a bug. Not depending on the GC behaviour at all by replacing one of the `QQ^7` by `QQ^37` as the patch I attached does still sounds like a good solution to me.


---

Attachment

apply instead (or additionally, but the first patch is not needed anymore with this one)


---

Comment by GeorgSWeber created at 2010-06-14 18:45:04

I think we all agree that a workaround will do, since finding the "real" root cause is both too difficult, and not bringing an advantage w.r.t. making the Sage Library more bugfree (since the root cause is not located within Sage).

Both patches are workarounds. But I feel that the latter from me is a bit closer to the root cause. Actually, the "rename" feature is used a handful of times in the `free_module.py` file, and any of these occurences had (before the latter patch) the potential to cause the failure seen (or a very similar one).
 
I tested that with the latter patch, the former is not needed anymore.


---

Comment by kcrisman created at 2010-08-05 20:21:26

> Both patches are workarounds. But I feel that the latter from me is a bit closer to the root cause. Actually, the "rename" feature is used a handful of times in the `free_module.py` file, and any of these occurences had (before the latter patch) the potential to cause the failure seen (or a very similar one).

This seems reasonable.  I'll try to check this later tonight.


---

Comment by kcrisman created at 2010-08-06 00:34:39

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-08-06 00:34:39

I feel like I can give this positive review based on the patch and passing tests, but my machine this occurred on only has room for one Sage install at a time, and I now have 4.5.2.rc1 rather than 4.4.2, and this failure does not occur even before the patch.  What do you all think?  

Maybe we would need to make this change in all such places, of which there are a fair number (esp. in `categories/modules_with_basis.py` and `modules/free_quadratic_module.py`; in `modular/abvar/abvar_ambient_jacobian.py` they clear the cache.

Incidentally, `reset_name()` is not doctested, and neither are a couple of other things in `structure/sage_object.pyx` related to this.  I don't think it's worth opening a ticket, though, since we still need several thousand functions doctested ;)

The author/reviewer things I filled in are just my best approximation; if someone disagrees, they can add themselves.


---

Comment by mpatel created at 2010-08-07 05:50:39

Should I merge _only_ [attachment:trac_9003_rename_doctest_alternate.patch]?


---

Comment by wjp created at 2010-08-07 09:21:03

Yes, only the alternate patch is fine.


---

Comment by mpatel created at 2010-08-09 09:49:38

Resolution: fixed
