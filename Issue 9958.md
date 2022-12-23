# Issue 9958: Get Pari to stop starting automatically

archive/issues_009958.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mpatel jdemeyer leif\n\nI still am getting the known behavior below when exiting Sage.\n\n```\nExiting Sage (CPU time 0m0.74s, Wall time 11m11.95s). \nExiting spawned GP/PARI interpreter process. \n```\n\nIt's not exactly a bug, but it's also annoying and potentially \nconfusing to a non-Pari user.  We should stop it.\n\nThis is with 4.6.alpha1.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9959\n\n",
    "created_at": "2010-09-21T13:36:14Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "Get Pari to stop starting automatically",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9958",
    "user": "kcrisman"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/9959





---

archive/issue_comments_099625.json:
```json
{
    "body": "Oh, I thought you just meant \"GP/PARI\" should read \"PARI/GP\"...",
    "created_at": "2010-09-21T14:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99625",
    "user": "leif"
}
```

Oh, I thought you just meant "GP/PARI" should read "PARI/GP"...



---

archive/issue_comments_099626.json:
```json
{
    "body": "So how do we manage this?\n\nRewrite the class `sage.interfaces.gp.Gp` to lazily start the interpreter, or initialize `sage.interfaces.gp.gp` to `None` and explicitly do `gp = Gp()` everywhere it is used unless `gp != None`?",
    "created_at": "2010-09-21T14:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99626",
    "user": "leif"
}
```

So how do we manage this?

Rewrite the class `sage.interfaces.gp.Gp` to lazily start the interpreter, or initialize `sage.interfaces.gp.gp` to `None` and explicitly do `gp = Gp()` everywhere it is used unless `gp != None`?



---

archive/issue_comments_099627.json:
```json
{
    "body": "I believe this in `Gp.__init__` is the culprit:\n\n```\n# gp starts up with this set to 1, which makes pexpect hang: \nself.set_default('breakloop',0)\n```\n\n\nIf this is the case, an easy solution is to add a patch to the pari spkg to set breakloop to 0 by default.",
    "created_at": "2010-09-21T20:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99627",
    "user": "jdemeyer"
}
```

I believe this in `Gp.__init__` is the culprit:

```
# gp starts up with this set to 1, which makes pexpect hang: 
self.set_default('breakloop',0)
```


If this is the case, an easy solution is to add a patch to the pari spkg to set breakloop to 0 by default.



---

archive/issue_comments_099628.json:
```json
{
    "body": "Replying to [comment:1 leif]:\n> Oh, I thought you just meant \"GP/PARI\" should read \"PARI/GP\"...\nThis should also be changed.",
    "created_at": "2010-09-21T20:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99628",
    "user": "jdemeyer"
}
```

Replying to [comment:1 leif]:
> Oh, I thought you just meant "GP/PARI" should read "PARI/GP"...
This should also be changed.



---

archive/issue_comments_099629.json:
```json
{
    "body": "Replying to [comment:3 jdemeyer]:\n> I believe this in `Gp.__init__` is the culprit:\n\n```\n# gp starts up with this set to 1, which makes pexpect hang: \nself.set_default('breakloop',0)\n```\n\n\nGood catch. I read this a dozen times without noticing that this actually calls `gp`... 8/\n\n> If this is the case, an easy solution is to add a patch to the pari spkg to set breakloop to 0 by default.\n\nTry it...",
    "created_at": "2010-09-21T20:21:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99629",
    "user": "leif"
}
```

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

archive/issue_comments_099630.json:
```json
{
    "body": "Attachment\n\nRenames \"GP/PARI\" to \"PARI/GP\"",
    "created_at": "2010-09-21T21:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99630",
    "user": "jdemeyer"
}
```

Attachment

Renames "GP/PARI" to "PARI/GP"



---

archive/issue_comments_099631.json:
```json
{
    "body": "New spkg for testing: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p8.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p8.spkg)",
    "created_at": "2010-09-21T21:51:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99631",
    "user": "jdemeyer"
}
```

New spkg for testing: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p8.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p8.spkg)



---

archive/issue_comments_099632.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-21T22:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99632",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099633.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-09-21T22:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99633",
    "user": "jdemeyer"
}
```

Changing priority from major to minor.



---

archive/issue_comments_099634.json:
```json
{
    "body": "Wow, *a lot* of places where \"GP/PARI\" had to be changed... (well done)\n\nWe have two similar instances in the scripts repo:\n\n```\nlocal/bin/sage-sage:    echo \"  -gp <..>      -- run Sage's GP (Pari) with given arguments\"\nlocal/bin/sage-sage.py:                     help=\"run Sage's GP (Pari), passing it all remaining arguments\")\n```\n\nBut I think we don't need to change these on this ticket.\n\nPatches look fine, will test them later (with the new spkg of course).",
    "created_at": "2010-09-21T22:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99634",
    "user": "leif"
}
```

Wow, *a lot* of places where "GP/PARI" had to be changed... (well done)

We have two similar instances in the scripts repo:

```
local/bin/sage-sage:    echo "  -gp <..>      -- run Sage's GP (Pari) with given arguments"
local/bin/sage-sage.py:                     help="run Sage's GP (Pari), passing it all remaining arguments")
```

But I think we don't need to change these on this ticket.

Patches look fine, will test them later (with the new spkg of course).



---

archive/issue_comments_099635.json:
```json
{
    "body": "The spkg's changelog entry (and `patches/README.txt`) could describe the reason for patching `default.c` a bit more. (The ticket number is only in the commit message.)",
    "created_at": "2010-09-22T17:28:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99635",
    "user": "leif"
}
```

The spkg's changelog entry (and `patches/README.txt`) could describe the reason for patching `default.c` a bit more. (The ticket number is only in the commit message.)



---

archive/issue_comments_099636.json:
```json
{
    "body": "s|and|and/or|",
    "created_at": "2010-09-22T17:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99636",
    "user": "leif"
}
```

s|and|and/or|



---

archive/issue_comments_099637.json:
```json
{
    "body": "OK, so I was the one who put in those two breakloop calls, which I only did since otherwise things did not work properly -- but in the testing I just did I found it only necessary to delete the brealoop call in `__init__`, while keeping the one in `_start`.  Are you both sure that it is safe to delete the one in `_start` as well?  Does that not cause gp to enter the breakloop on encountering an error, which is not what you want?\n\nIf you are right (and I assumed that you did test this!) then I am wondering what else has changed, since when we started the pari upgrade it was definitely necessary to deal with this.\n\nAnd by the way, the *only* reason I created a `_start` function for Gp different from the default one in PExpect was to add this line in `_start`;  so if that line is not needed, you can probably delete the while `_start` function for class Gp.",
    "created_at": "2010-09-22T20:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99637",
    "user": "cremona"
}
```

OK, so I was the one who put in those two breakloop calls, which I only did since otherwise things did not work properly -- but in the testing I just did I found it only necessary to delete the brealoop call in `__init__`, while keeping the one in `_start`.  Are you both sure that it is safe to delete the one in `_start` as well?  Does that not cause gp to enter the breakloop on encountering an error, which is not what you want?

If you are right (and I assumed that you did test this!) then I am wondering what else has changed, since when we started the pari upgrade it was definitely necessary to deal with this.

And by the way, the *only* reason I created a `_start` function for Gp different from the default one in PExpect was to add this line in `_start`;  so if that line is not needed, you can probably delete the while `_start` function for class Gp.



---

archive/issue_comments_099638.json:
```json
{
    "body": "I haven't come to testing yet... (including a closer look at the relevant PARI sources).\n\nIt should at least not hurt to keep the second `set_default('breakloop',0)` in `Gp._start()`.",
    "created_at": "2010-09-22T21:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99638",
    "user": "leif"
}
```

I haven't come to testing yet... (including a closer look at the relevant PARI sources).

It should at least not hurt to keep the second `set_default('breakloop',0)` in `Gp._start()`.



---

archive/issue_comments_099639.json:
```json
{
    "body": "Replying to [comment:12 leif]:\n> It should at least not hurt to keep the second `set_default('breakloop',0)` in `Gp._start()`.\n\nAs far as I can see, we don't need it there, since `gp` will of course (re)start with the hard-coded defaults whenever `_start()` is called.\n\n(This is different to setting it \"manually\" from the Expect interface each time `gp` is [re]started.) \n\nSo we can IMHO drop `Gp._start()` completely, as John noted.",
    "created_at": "2010-09-22T22:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99639",
    "user": "leif"
}
```

Replying to [comment:12 leif]:
> It should at least not hurt to keep the second `set_default('breakloop',0)` in `Gp._start()`.

As far as I can see, we don't need it there, since `gp` will of course (re)start with the hard-coded defaults whenever `_start()` is called.

(This is different to setting it "manually" from the Expect interface each time `gp` is [re]started.) 

So we can IMHO drop `Gp._start()` completely, as John noted.



---

archive/issue_comments_099640.json:
```json
{
    "body": "Replying to [comment:11 cremona]:\n> Are you both sure that it is safe to delete the one in `_start` as well?  Does that not cause gp to enter the breakloop on encountering an error, which is not what you want?\n\nThe new spkg patches the `gp` source code to disable the breakloop by default, so we can remove all references to `breakloop` from Sage.  Note also that the patch [attachment:9959_gp_error_doctest.patch] actually acts a doctest to check this.",
    "created_at": "2010-09-23T07:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99640",
    "user": "jdemeyer"
}
```

Replying to [comment:11 cremona]:
> Are you both sure that it is safe to delete the one in `_start` as well?  Does that not cause gp to enter the breakloop on encountering an error, which is not what you want?

The new spkg patches the `gp` source code to disable the breakloop by default, so we can remove all references to `breakloop` from Sage.  Note also that the patch [attachment:9959_gp_error_doctest.patch] actually acts a doctest to check this.



---

archive/issue_comments_099641.json:
```json
{
    "body": "Don't set the 'breakloop' default in Sage",
    "created_at": "2010-09-23T07:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99641",
    "user": "jdemeyer"
}
```

Don't set the 'breakloop' default in Sage



---

archive/issue_comments_099642.json:
```json
{
    "body": "Attachment\n\nAdd doctest for error recovery",
    "created_at": "2010-09-23T07:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99642",
    "user": "jdemeyer"
}
```

Attachment

Add doctest for error recovery



---

archive/issue_comments_099643.json:
```json
{
    "body": "Replying to [comment:11 cremona]:\n> And by the way, the *only* reason I created a `_start` function for Gp different from the default one in PExpect was to add this line in `_start`;  so if that line is not needed, you can probably delete the while `_start` function for class Gp.\n\nDone",
    "created_at": "2010-09-23T07:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99643",
    "user": "jdemeyer"
}
```

Replying to [comment:11 cremona]:
> And by the way, the *only* reason I created a `_start` function for Gp different from the default one in PExpect was to add this line in `_start`;  so if that line is not needed, you can probably delete the while `_start` function for class Gp.

Done



---

archive/issue_comments_099644.json:
```json
{
    "body": "It's a pity that we had to patch the gp source code -- clearly that was an option right from the start, and what I did was to avoid that.  Best (in my opinion) would be if gp had a command-line option to turn off the breakloop default, since Sage could easily use that.  It might be worth suggesting that possibility upstream.",
    "created_at": "2010-09-23T08:27:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99644",
    "user": "cremona"
}
```

It's a pity that we had to patch the gp source code -- clearly that was an option right from the start, and what I did was to avoid that.  Best (in my opinion) would be if gp had a command-line option to turn off the breakloop default, since Sage could easily use that.  It might be worth suggesting that possibility upstream.



---

archive/issue_comments_099645.json:
```json
{
    "body": "Attachment\n\nPatch for the PARI spkg .p7 to .p8 (for review)",
    "created_at": "2010-09-23T08:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99645",
    "user": "jdemeyer"
}
```

Attachment

Patch for the PARI spkg .p7 to .p8 (for review)



---

archive/issue_comments_099646.json:
```json
{
    "body": "Replying to [comment:16 cremona]:\n> It's a pity that we had to patch the gp source code -- clearly that was an option right from the start, and what I did was to avoid that.  Best (in my opinion) would be if gp had a command-line option to turn off the breakloop default, since Sage could easily use that.  It might be worth suggesting that possibility upstream.\n\nIf one would add an option to `gp`, add an option for non-interactive (script) use which would also disable `breakloop` by default.  I remember I proposed this (a long time ago) to the PARI/GP developers without much success.",
    "created_at": "2010-09-23T08:49:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99646",
    "user": "jdemeyer"
}
```

Replying to [comment:16 cremona]:
> It's a pity that we had to patch the gp source code -- clearly that was an option right from the start, and what I did was to avoid that.  Best (in my opinion) would be if gp had a command-line option to turn off the breakloop default, since Sage could easily use that.  It might be worth suggesting that possibility upstream.

If one would add an option to `gp`, add an option for non-interactive (script) use which would also disable `breakloop` by default.  I remember I proposed this (a long time ago) to the PARI/GP developers without much success.



---

archive/issue_comments_099647.json:
```json
{
    "body": "Replying to [comment:17 jdemeyer]:\n> Replying to [comment:16 cremona]:\n> > It's a pity that we had to patch the gp source code -- clearly that was an option right from the start, and what I did was to avoid that.  Best (in my opinion) would be if gp had a command-line option to turn off the breakloop default, since Sage could easily use that.  It might be worth suggesting that possibility upstream.\n> \n> If one would add an option to `gp`, add an option for non-interactive (script) use which would also disable `breakloop` by default.  I remember I proposed this (a long time ago) to the PARI/GP developers without much success.\n\nI suppose that from their point of view it makes no sense to use gp non-interactively, since gp is the interactive interface to the pari library!",
    "created_at": "2010-09-23T08:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99647",
    "user": "cremona"
}
```

Replying to [comment:17 jdemeyer]:
> Replying to [comment:16 cremona]:
> > It's a pity that we had to patch the gp source code -- clearly that was an option right from the start, and what I did was to avoid that.  Best (in my opinion) would be if gp had a command-line option to turn off the breakloop default, since Sage could easily use that.  It might be worth suggesting that possibility upstream.
> 
> If one would add an option to `gp`, add an option for non-interactive (script) use which would also disable `breakloop` by default.  I remember I proposed this (a long time ago) to the PARI/GP developers without much success.

I suppose that from their point of view it makes no sense to use gp non-interactively, since gp is the interactive interface to the pari library!



---

archive/issue_comments_099648.json:
```json
{
    "body": "**Alternative solution**:\n\nWhen `gp` starts, it reads a configuration file (by default, `$HOME/.gprc`).  If the environment variable `$GPRC` is set, it uses that as a filename for the `.gprc` file.  We could create a file `$HOME/.sage/gp/gprc` similarly to `$HOME/.sage/ipyhton/ipythonrc` and have Sage set `$GPRC` to that location.\n\nThen, the file `$HOME/.sage/gp/gprc` should contain a line:\n\n```\nbreakloop =  0\n```\n",
    "created_at": "2010-09-23T09:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99648",
    "user": "jdemeyer"
}
```

**Alternative solution**:

When `gp` starts, it reads a configuration file (by default, `$HOME/.gprc`).  If the environment variable `$GPRC` is set, it uses that as a filename for the `.gprc` file.  We could create a file `$HOME/.sage/gp/gprc` similarly to `$HOME/.sage/ipyhton/ipythonrc` and have Sage set `$GPRC` to that location.

Then, the file `$HOME/.sage/gp/gprc` should contain a line:

```
breakloop =  0
```




---

archive/issue_comments_099649.json:
```json
{
    "body": "Replying to [comment:18 cremona]:\n> I suppose that from their point of view it makes no sense to use gp non-interactively, since gp is the interactive interface to the pari library!\n\nGood point :-)",
    "created_at": "2010-09-23T09:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99649",
    "user": "jdemeyer"
}
```

Replying to [comment:18 cremona]:
> I suppose that from their point of view it makes no sense to use gp non-interactively, since gp is the interactive interface to the pari library!

Good point :-)



---

archive/issue_comments_099650.json:
```json
{
    "body": "Replying to [comment:19 jdemeyer]:\n> **Alternative solution**:\n> \n> When `gp` starts, it reads a configuration file (by default, `$HOME/.gprc`).  If the environment variable `$GPRC` is set, it uses that as a filename for the `.gprc` file.  We could create a file `$HOME/.sage/gp/gprc` similarly to `$HOME/.sage/ipyhton/ipythonrc` and have Sage set `$GPRC` to that location.\n> \n> Then, the file `$HOME/.sage/gp/gprc` should contain a line:\n\n```\nbreakloop =  0\n```\n\n\nI was just going to suggest that, too.\n\nNote that we should have two of them, one for the interactive `gp` provided by Sage, and one for the `pexpect` interface.",
    "created_at": "2010-09-23T09:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99650",
    "user": "leif"
}
```

Replying to [comment:19 jdemeyer]:
> **Alternative solution**:
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

archive/issue_comments_099651.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-23T09:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99651",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099652.json:
```json
{
    "body": "Replying to [comment:21 leif]:\n> Note that we should have two of them, one for the interactive `gp` provided by Sage, and one for the `pexpect` interface.\n\nI think we need only one, for the pexpect interface.  I would prefer `sage -gp` to use my `$HOME/.gprc`.\n\nSetting this to needs_work to implement the alternative solution.",
    "created_at": "2010-09-23T09:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99652",
    "user": "jdemeyer"
}
```

Replying to [comment:21 leif]:
> Note that we should have two of them, one for the interactive `gp` provided by Sage, and one for the `pexpect` interface.

I think we need only one, for the pexpect interface.  I would prefer `sage -gp` to use my `$HOME/.gprc`.

Setting this to needs_work to implement the alternative solution.



---

archive/issue_comments_099653.json:
```json
{
    "body": "Replying to [comment:17 jdemeyer]:\n> If one would add an option to `gp`, add an option for non-interactive (script) use which would also disable `breakloop` by default.  I remember I proposed this (a long time ago) to the PARI/GP developers without much success.\n\nPerhaps they meanwhile chnaged their minds.. ;-)\n\nThere's some stuff in it for using `gp` from Emacs or TeXmacs, but only as a *compile time* option IIRC. Also some kind of \"non-interactive\" `gp` use.",
    "created_at": "2010-09-23T09:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99653",
    "user": "leif"
}
```

Replying to [comment:17 jdemeyer]:
> If one would add an option to `gp`, add an option for non-interactive (script) use which would also disable `breakloop` by default.  I remember I proposed this (a long time ago) to the PARI/GP developers without much success.

Perhaps they meanwhile chnaged their minds.. ;-)

There's some stuff in it for using `gp` from Emacs or TeXmacs, but only as a *compile time* option IIRC. Also some kind of "non-interactive" `gp` use.



---

archive/issue_comments_099654.json:
```json
{
    "body": "Replying to [comment:22 jdemeyer]:\n> Replying to [comment:21 leif]:\n> > Note that we should have two of them, one for the interactive `gp` provided by Sage, and one for the `pexpect` interface.\n> \n> I think we need only one, for the pexpect interface.  I would prefer `sage -gp` to use my `$HOME/.gprc`.\n\nRight, but we should take care not to use the other one (i.e. by setting `GPRC` and therefore overriding `$HOME/.gprc`) if we start the interactive `gp`.",
    "created_at": "2010-09-23T09:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99654",
    "user": "leif"
}
```

Replying to [comment:22 jdemeyer]:
> Replying to [comment:21 leif]:
> > Note that we should have two of them, one for the interactive `gp` provided by Sage, and one for the `pexpect` interface.
> 
> I think we need only one, for the pexpect interface.  I would prefer `sage -gp` to use my `$HOME/.gprc`.

Right, but we should take care not to use the other one (i.e. by setting `GPRC` and therefore overriding `$HOME/.gprc`) if we start the interactive `gp`.



---

archive/issue_comments_099655.json:
```json
{
    "body": "Anybody happens to know where is the code to deal with `$DOT_SAGE`, to populate it with files?",
    "created_at": "2010-09-23T10:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99655",
    "user": "jdemeyer"
}
```

Anybody happens to know where is the code to deal with `$DOT_SAGE`, to populate it with files?



---

archive/issue_comments_099656.json:
```json
{
    "body": "Use $SAGE_ROOT/local/etc/gprc.expect as .gprc file",
    "created_at": "2010-09-24T13:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99656",
    "user": "jdemeyer"
}
```

Use $SAGE_ROOT/local/etc/gprc.expect as .gprc file



---

archive/issue_comments_099657.json:
```json
{
    "body": "Attachment\n\nNew spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg).  This is based on **p7** (not p8) and adds the `gprc.expect` file.  So installing the new spkg and applying all 4 patches should do it.",
    "created_at": "2010-09-24T14:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99657",
    "user": "jdemeyer"
}
```

Attachment

New spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg).  This is based on **p7** (not p8) and adds the `gprc.expect` file.  So installing the new spkg and applying all 4 patches should do it.



---

archive/issue_comments_099658.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-24T14:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99658",
    "user": "leif"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099659.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-24T14:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99659",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099660.json:
```json
{
    "body": "Doesn't work yet, stupid mistake.",
    "created_at": "2010-09-24T14:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99660",
    "user": "jdemeyer"
}
```

Doesn't work yet, stupid mistake.



---

archive/issue_comments_099661.json:
```json
{
    "body": "`sage.math.washington.edu` seems much slower than usual today...",
    "created_at": "2010-09-24T14:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99661",
    "user": "jdemeyer"
}
```

`sage.math.washington.edu` seems much slower than usual today...



---

archive/issue_comments_099662.json:
```json
{
    "body": "Does `gp` expand `$SAGE_ROOT` in the `gprc.expect` file, or does Sage do that before it starts `gp`?",
    "created_at": "2010-09-24T14:52:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99662",
    "user": "leif"
}
```

Does `gp` expand `$SAGE_ROOT` in the `gprc.expect` file, or does Sage do that before it starts `gp`?



---

archive/issue_comments_099663.json:
```json
{
    "body": "Replying to [comment:30 leif]:\n> Does `gp` expand `$SAGE_ROOT` in the `gprc.expect` file, or does Sage do that before it starts `gp`?\n\n`gp` does that.",
    "created_at": "2010-09-24T14:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99663",
    "user": "jdemeyer"
}
```

Replying to [comment:30 leif]:
> Does `gp` expand `$SAGE_ROOT` in the `gprc.expect` file, or does Sage do that before it starts `gp`?

`gp` does that.



---

archive/issue_comments_099664.json:
```json
{
    "body": ".gprc file for the Gp() interface",
    "created_at": "2010-09-24T15:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99664",
    "user": "jdemeyer"
}
```

.gprc file for the Gp() interface



---

archive/issue_comments_099665.json:
```json
{
    "body": "Attachment\n\nPatch for the PARI spkg .p7 to .p9 (for review)",
    "created_at": "2010-09-24T17:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99665",
    "user": "jdemeyer"
}
```

Attachment

Patch for the PARI spkg .p7 to .p9 (for review)



---

archive/issue_comments_099666.json:
```json
{
    "body": "Fixed spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg)",
    "created_at": "2010-09-24T17:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99666",
    "user": "jdemeyer"
}
```

Fixed spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg)



---

archive/issue_comments_099667.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-24T17:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99667",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099668.json:
```json
{
    "body": "Attachment\n\nAll 4 sagelib patches combined",
    "created_at": "2010-09-26T17:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99668",
    "user": "jdemeyer"
}
```

Attachment

All 4 sagelib patches combined



---

archive/issue_comments_099669.json:
```json
{
    "body": "Changing priority from minor to blocker.",
    "created_at": "2010-10-09T14:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99669",
    "user": "mpatel"
}
```

Changing priority from minor to blocker.



---

archive/issue_comments_099670.json:
```json
{
    "body": "The sagelib patch looks good to me.\n\nFor review, please could you give instructions for the simple-minded as to how to apply the patch which converts .p7 to .p9?  And then how to rebuild?  Thanks.\n\nOf course, someone else who knows how to do this reliably is welcome to get in first with a review.",
    "created_at": "2010-10-09T17:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99670",
    "user": "cremona"
}
```

The sagelib patch looks good to me.

For review, please could you give instructions for the simple-minded as to how to apply the patch which converts .p7 to .p9?  And then how to rebuild?  Thanks.

Of course, someone else who knows how to do this reliably is welcome to get in first with a review.



---

archive/issue_comments_099671.json:
```json
{
    "body": "Replying to [comment:35 cremona]:\n> The sagelib patch looks good to me.\n> \n> For review, please could you give instructions for the simple-minded as to how to apply the patch which converts .p7 to .p9?\n\nWell, the easiest is to install the new spkg:\n\n```\nsage -i http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg\n```\n\n\n> And then how to rebuild?\nI personally do not know the most reliable way to rebuild a complete Sage installation.  One thing which works for sure is the following:\n* download sage-4.6.alpha3.tar and extract it so we have a clean, uncompiled sage-4.6.alpha3.\n* rm spkg/standard/pari-*.spkg\n* download [ttp://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p9.spkg] and and put it in spkg/standard\n* now `make` Sage as usual",
    "created_at": "2010-10-09T18:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99671",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_099672.json:
```json
{
    "body": "THanks -- I am doing that, will do a complete new build (with the sagelib patch too of course) and report back.",
    "created_at": "2010-10-09T19:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99672",
    "user": "cremona"
}
```

THanks -- I am doing that, will do a complete new build (with the sagelib patch too of course) and report back.



---

archive/issue_comments_099673.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-09T20:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99673",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099674.json:
```json
{
    "body": "I made a freshly unpacked 4.6.alpha3, and replaced its pari spkg with the p9 version;  then built all Sage;  then applied the sagelib patch on this ticket;  then tested the whole library.\n\nAll passed, so here's a positive review.",
    "created_at": "2010-10-09T20:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99674",
    "user": "cremona"
}
```

I made a freshly unpacked 4.6.alpha3, and replaced its pari spkg with the p9 version;  then built all Sage;  then applied the sagelib patch on this ticket;  then tested the whole library.

All passed, so here's a positive review.



---

archive/issue_comments_099675.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-21T08:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9958",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9958#issuecomment-99675",
    "user": "mpatel"
}
```

Resolution: fixed
