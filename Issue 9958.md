# Issue 9958: Get Pari to stop starting automatically

Issue created by migration from https://trac.sagemath.org/ticket/9959

Original creator: kcrisman

Original creation time: 2010-09-21 13:36:14

Assignee: tbd

CC:  mpatel jdemeyer leif

I still am getting the known behavior below when exiting Sage.

```
Exiting Sage (CPU time 0m0.74s, Wall time 11m11.95s). 
Exiting spawned GP/PARI interpreter process. 
```

It's not exactly a bug, but it's also annoying and potentially 
confusing to a non-Pari user.  We should stop it.

This is with 4.6.alpha1.


---

Comment by leif created at 2010-09-21 14:14:39

Oh, I thought you just meant "GP/PARI" should read "PARI/GP"...


---

Comment by leif created at 2010-09-21 14:50:10

So how do we manage this?

Rewrite the class `sage.interfaces.gp.Gp` to lazily start the interpreter, or initialize `sage.interfaces.gp.gp` to `None` and explicitly do `gp = Gp()` everywhere it is used unless `gp != None`?


---

Comment by jdemeyer created at 2010-09-21 20:05:30

I believe this in `Gp.__init__` is the culprit:

```
# gp starts up with this set to 1, which makes pexpect hang: 
self.set_default('breakloop',0)
```


If this is the case, an easy solution is to add a patch to the pari spkg to set breakloop to 0 by default.


---

Comment by jdemeyer created at 2010-09-21 20:06:08

Replying to [comment:1 leif]:
> Oh, I thought you just meant "GP/PARI" should read "PARI/GP"...
This should also be changed.


---

Comment by leif created at 2010-09-21 20:21:17

Replying to [comment:3 jdemeyer]:
> I believe this in `Gp.__init__` is the culprit:

```
# gp starts up with this set to 1, which makes pexpect hang: 
self.set_default('breakloop',0)
```


Good catch. I read this a dozen times without noticing that this actually calls `gp`... 8/

> If this is the case, an easy solution is to add a patch to the pari spkg to set breakloop to 0 by default.

Try it...


---

Attachment

Renames "GP/PARI" to "PARI/GP"


---

Comment by jdemeyer created at 2010-09-21 21:51:46

New spkg for testing: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p8.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p8.spkg)


---

Comment by jdemeyer created at 2010-09-21 22:15:28

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-09-21 22:15:28

Changing priority from major to minor.


---

Comment by leif created at 2010-09-21 22:50:11

Wow, _a lot_ of places where "GP/PARI" had to be changed... (well done)

We have two similar instances in the scripts repo:

```
local/bin/sage-sage:    echo "  -gp <..>      -- run Sage's GP (Pari) with given arguments"
local/bin/sage-sage.py:                     help="run Sage's GP (Pari), passing it all remaining arguments")
```

But I think we don't need to change these on this ticket.

Patches look fine, will test them later (with the new spkg of course).


---

Comment by leif created at 2010-09-22 17:28:44

The spkg's changelog entry (and `patches/README.txt`) could describe the reason for patching `default.c` a bit more. (The ticket number is only in the commit message.)


---

Comment by leif created at 2010-09-22 17:30:34

s|and|and/or|


---

Comment by cremona created at 2010-09-22 20:47:55

OK, so I was the one who put in those two breakloop calls, which I only did since otherwise things did not work properly -- but in the testing I just did I found it only necessary to delete the brealoop call in `__init__`, while keeping the one in `_start`.  Are you both sure that it is safe to delete the one in `_start` as well?  Does that not cause gp to enter the breakloop on encountering an error, which is not what you want?

If you are right (and I assumed that you did test this!) then I am wondering what else has changed, since when we started the pari upgrade it was definitely necessary to deal with this.

And by the way, the *only* reason I created a `_start` function for Gp different from the default one in PExpect was to add this line in `_start`;  so if that line is not needed, you can probably delete the while `_start` function for class Gp.


---

Comment by leif created at 2010-09-22 21:24:36

I haven't come to testing yet... (including a closer look at the relevant PARI sources).

It should at least not hurt to keep the second `set_default('breakloop',0)` in `Gp._start()`.


---

Comment by leif created at 2010-09-22 22:20:33

Replying to [comment:12 leif]:
> It should at least not hurt to keep the second `set_default('breakloop',0)` in `Gp._start()`.

As far as I can see, we don't need it there, since `gp` will of course (re)start with the hard-coded defaults whenever `_start()` is called.

(This is different to setting it "manually" from the Expect interface each time `gp` is [re]started.) 

So we can IMHO drop `Gp._start()` completely, as John noted.


---

Comment by jdemeyer created at 2010-09-23 07:45:54

Replying to [comment:11 cremona]:
> Are you both sure that it is safe to delete the one in `_start` as well?  Does that not cause gp to enter the breakloop on encountering an error, which is not what you want?

The new spkg patches the `gp` source code to disable the breakloop by default, so we can remove all references to `breakloop` from Sage.  Note also that the patch [attachment:9959_gp_error_doctest.patch] actually acts a doctest to check this.


---

Comment by jdemeyer created at 2010-09-23 07:47:31

Don't set the 'breakloop' default in Sage


---

Attachment

Add doctest for error recovery


---

Comment by jdemeyer created at 2010-09-23 07:48:38

Replying to [comment:11 cremona]:
> And by the way, the *only* reason I created a `_start` function for Gp different from the default one in PExpect was to add this line in `_start`;  so if that line is not needed, you can probably delete the while `_start` function for class Gp.

Done


---

Comment by cremona created at 2010-09-23 08:27:59

It's a pity that we had to patch the gp source code -- clearly that was an option right from the start, and what I did was to avoid that.  Best (in my opinion) would be if gp had a command-line option to turn off the breakloop default, since Sage could easily use that.  It might be worth suggesting that possibility upstream.


---

Attachment

Patch for the PARI spkg .p7 to .p8 (for review)


---

Comment by jdemeyer created at 2010-09-23 08:49:54

Replying to [comment:16 cremona]:
> It's a pity that we had to patch the gp source code -- clearly that was an option right from the start, and what I did was to avoid that.  Best (in my opinion) would be if gp had a command-line option to turn off the breakloop default, since Sage could easily use that.  It might be worth suggesting that possibility upstream.

If one would add an option to `gp`, add an option for non-interactive (script) use which would also disable `breakloop` by default.  I remember I proposed this (a long time ago) to the PARI/GP developers without much success.


---

Comment by cremona created at 2010-09-23 08:58:18

Replying to [comment:17 jdemeyer]:
> Replying to [comment:16 cremona]:
> > It's a pity that we had to patch the gp source code -- clearly that was an option right from the start, and what I did was to avoid that.  Best (in my opinion) would be if gp had a command-line option to turn off the breakloop default, since Sage could easily use that.  It might be worth suggesting that possibility upstream.
> 
> If one would add an option to `gp`, add an option for non-interactive (script) use which would also disable `breakloop` by default.  I remember I proposed this (a long time ago) to the PARI/GP developers without much success.

I suppose that from their point of view it makes no sense to use gp non-interactively, since gp is the interactive interface to the pari library!


---

Comment by jdemeyer created at 2010-09-23 09:01:02

*Alternative solution*:

When `gp` starts, it reads a configuration file (by default, `$HOME/.gprc`).  If the environment variable `$GPRC` is set, it uses that as a filename for the `.gprc` file.  We could create a file `$HOME/.sage/gp/gprc` similarly to `$HOME/.sage/ipyhton/ipythonrc` and have Sage set `$GPRC` to that location.

Then, the file `$HOME/.sage/gp/gprc` should contain a line:

```
breakloop =  0
```



---

Comment by jdemeyer created at 2010-09-23 09:01:51

Replying to [comment:18 cremona]:
> I suppose that from their point of view it makes no sense to use gp non-interactively, since gp is the interactive interface to the pari library!

Good point :-)


---

Comment by leif created at 2010-09-23 09:07:13

Replying to [comment:19 jdemeyer]:
> *Alternative solution*:
> 
> When `gp` starts, it reads a configuration file (by default, `$HOME/.gprc`).  If the environment variable `$GPRC` is set, it uses that as a filename for the `.gprc` file.  We could create a file `$HOME/.sage/gp/gprc` similarly to `$HOME/.sage/ipyhton/ipythonrc` and have Sage set `$GPRC` to that location.
> 
> Then, the file `$HOME/.sage/gp/gprc` should contain a line:

```
breakloop =  0
```


I was just going to suggest that, too.

Note that we should have two of them, one for the interactive `gp` provided by Sage, and one for the `pexpect` interface.


---

Comment by jdemeyer created at 2010-09-23 09:11:17

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-09-23 09:11:17

Replying to [comment:21 leif]:
> Note that we should have two of them, one for the interactive `gp` provided by Sage, and one for the `pexpect` interface.

I think we need only one, for the pexpect interface.  I would prefer `sage -gp` to use my `$HOME/.gprc`.

Setting this to needs_work to implement the alternative solution.


---

Comment by leif created at 2010-09-23 09:12:51

Replying to [comment:17 jdemeyer]:
> If one would add an option to `gp`, add an option for non-interactive (script) use which would also disable `breakloop` by default.  I remember I proposed this (a long time ago) to the PARI/GP developers without much success.

Perhaps they meanwhile chnaged their minds.. ;-)

There's some stuff in it for using `gp` from Emacs or TeXmacs, but only as a _compile time_ option IIRC. Also some kind of "non-interactive" `gp` use.


---

Comment by leif created at 2010-09-23 09:18:44

Replying to [comment:22 jdemeyer]:
> Replying to [comment:21 leif]:
> > Note that we should have two of them, one for the interactive `gp` provided by Sage, and one for the `pexpect` interface.
> 
> I think we need only one, for the pexpect interface.  I would prefer `sage -gp` to use my `$HOME/.gprc`.

Right, but we should take care not to use the other one (i.e. by setting `GPRC` and therefore overriding `$HOME/.gprc`) if we start the interactive `gp`.


---

Comment by jdemeyer created at 2010-09-23 10:36:31

Anybody happens to know where is the code to deal with `$DOT_SAGE`, to populate it with files?


---

Comment by jdemeyer created at 2010-09-24 13:57:07

Use $SAGE_ROOT/local/etc/gprc.expect as .gprc file


---

Attachment

New spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg).  This is based on *p7* (not p8) and adds the `gprc.expect` file.  So installing the new spkg and applying all 4 patches should do it.


---

Comment by leif created at 2010-09-24 14:44:17

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-09-24 14:46:22

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-09-24 14:46:22

Doesn't work yet, stupid mistake.


---

Comment by jdemeyer created at 2010-09-24 14:47:07

`sage.math.washington.edu` seems much slower than usual today...


---

Comment by leif created at 2010-09-24 14:52:11

Does `gp` expand `$SAGE_ROOT` in the `gprc.expect` file, or does Sage do that before it starts `gp`?


---

Comment by jdemeyer created at 2010-09-24 14:57:21

Replying to [comment:30 leif]:
> Does `gp` expand `$SAGE_ROOT` in the `gprc.expect` file, or does Sage do that before it starts `gp`?

`gp` does that.


---

Comment by jdemeyer created at 2010-09-24 15:43:14

.gprc file for the Gp() interface


---

Attachment

Patch for the PARI spkg .p7 to .p9 (for review)


---

Comment by jdemeyer created at 2010-09-24 17:09:45

Fixed spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg)


---

Comment by jdemeyer created at 2010-09-24 17:09:45

Changing status from needs_work to needs_review.


---

Attachment

All 4 sagelib patches combined


---

Comment by mpatel created at 2010-10-09 14:47:06

Changing priority from minor to blocker.


---

Comment by cremona created at 2010-10-09 17:35:42

The sagelib patch looks good to me.

For review, please could you give instructions for the simple-minded as to how to apply the patch which converts .p7 to .p9?  And then how to rebuild?  Thanks.

Of course, someone else who knows how to do this reliably is welcome to get in first with a review.


---

Comment by jdemeyer created at 2010-10-09 18:39:32

Replying to [comment:35 cremona]:
> The sagelib patch looks good to me.
> 
> For review, please could you give instructions for the simple-minded as to how to apply the patch which converts .p7 to .p9?

Well, the easiest is to install the new spkg:

```
sage -i http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg
```


> And then how to rebuild?
I personally do not know the most reliable way to rebuild a complete Sage installation.  One thing which works for sure is the following:
 * download sage-4.6.alpha3.tar and extract it so we have a clean, uncompiled sage-4.6.alpha3.
 * rm spkg/standard/pari-*.spkg
 * download [ttp://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg] and and put it in spkg/standard
 * now `make` Sage as usual


---

Comment by cremona created at 2010-10-09 19:12:23

THanks -- I am doing that, will do a complete new build (with the sagelib patch too of course) and report back.


---

Comment by cremona created at 2010-10-09 20:15:31

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-10-09 20:15:31

I made a freshly unpacked 4.6.alpha3, and replaced its pari spkg with the p9 version;  then built all Sage;  then applied the sagelib patch on this ticket;  then tested the whole library.

All passed, so here's a positive review.


---

Comment by mpatel created at 2010-10-21 08:18:58

Resolution: fixed
