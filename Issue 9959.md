# Issue 9959: require SAGE_CHECK to be "yes"

Issue created by migration from https://trac.sagemath.org/ticket/9960

Original creator: jhpalmieri

Original creation time: 2010-09-21 16:39:37

Assignee: was

CC:  drkirkby kcrisman leif mpatel jdemeyer

Right now, setting SAGE_CHECK to any nonempty string (e.g., "no") runs the test suite.  The documentation actually says that SAGE_CHECK should be "yes" for this to happen.  Fix this.

While we're at it, fix something else: in the script SAGE_ROOT/local/bin/sage-env, SAGE64 is required to be "yes", "no", or unset:

```
if [ "$SAGE64" != "yes" -a "$SAGE64" != "no" ]; then
    echo "The environment variable SAGE64 (=$SAGE64) must be either unset, yes or no."
    exit 1
fi
```

The problem is, whenever sage-env is run, output is redirected to /dev/null, so this error message isn't printed.  So for example:

```
$ export SAGE64='maybe'
$ sage
$
```

Sage fails to run and is completely silent as to why.  Fix this, too.


---

Comment by jhpalmieri created at 2010-09-21 16:41:59

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-09-21 16:46:19

By the way, if you look at sage-env, it rarely produces any output, so I don't see any reason to redirect it to /dev/null.  The lines

```
. $SAGE_ROOT/local/bin/sage-env   1>/dev/null 2>/dev/null

if [ $? -ne 0 ]; then
   echo "Error setting environment variables by running $SAGE_ROOT/local/bin/sage-env; possibly contact sage-devel (see http://groups.google.com/group/sage-devel)."
fi
```

from the sage-sage script don't actually seem to print the warning message; I'm not sure why.  But it's clearer if it says

```
$ export SAGE64=dlkjdf
$ sage
The environment variable SAGE64 (=dlkjdf) must be either unset, yes or no.
```



---

Comment by leif created at 2010-09-21 17:01:08

I commented on this _somewhere_ where I uploaded the "first aid" patch for spaces in `SAGE_ROOT`.

Redirecting the output of `sage-env` is really bad, and the test of `$?` is almost useless, since `sage-env` is (and must be) sourced, so it must not `exit` [some value].

The `SAGE_CHECK` issue (interpreting everything except "no" as "yes") is AFAIK a historical relict; some spkgs might still run the test suite from `spkg-install` if `SAGE_CHECK` is set and set to anything but "no".


---

Comment by leif created at 2010-09-21 17:16:28

Replacing every occurrence of `exit` in `sage-env` by `return` should work (then testing `$?` makes sense); I wonder why Sage is started even if `sage-env` failed though. (I think _there_ an `exit 1` is missing.)

And we should quote all occurrences of `SAGE_ROOT`...


---

Comment by leif created at 2010-09-21 17:22:43

Any idea why `sage-build` doesn't *source* `sage-env`?!?


---

Comment by leif created at 2010-09-21 17:31:17

Replying to [comment:4 leif]:
> I commented on this _somewhere_ where I uploaded the "first aid" patch for spaces in `SAGE_ROOT`.

#9644 (There' also a patch, including one to `sage-sage`.)


---

Comment by jhpalmieri created at 2010-09-21 19:04:43

Replying to [comment:4 leif]:
> Redirecting the output of `sage-env` is really bad,

I agree.

> and the test of `$?` is almost useless, since `sage-env` is (and must be) sourced, so it must not `exit` [some value].

Okay.

> The `SAGE_CHECK` issue (interpreting everything except "no" as "yes") is AFAIK a historical relict; some spkgs might still run the test suite from `spkg-install` if `SAGE_CHECK` is set and set to anything but "no".

I ran "grep" after unpacking all of the spkg's, and found SAGE_CHECK used in cliquer and mpir.  In both cases, it checks whether it's "yes".  (In the case of cliquer, this is done in spkg-install, but there is no spkg-check.  So it does the right thing -- running the test suite once if SAGE_CHECK is "yes", just not in the right way.  In the case of mpir, if SAGE_CHECK is yes, then the test suite gets run twice, once because of the main sage-spkg script, and once more in mpir's spkg-install script.  I thought there was a ticket for this, but I can't find it right now.)

> Replacing every occurrence of exit in sage-env by return should work (then testing $? makes sense); I wonder why Sage is started even if sage-env failed though. (I think there an exit 1 is missing.)

When do you see Sage starting if sage-env fails?

I'll also take a look at #9644.  If I can give that a positive review, I'll change the patch here to make it depend on #9644.  (I may do that anyway...)  As far as changing sage-build to source sage-env, could that break things?  The other changes here are pretty inocuous.


---

Comment by jhpalmieri created at 2010-09-21 19:05:55

Ah, the mpir issue is covered by #9522 and #8664.


---

Comment by leif created at 2010-09-21 19:34:43

Replying to [comment:8 jhpalmieri]:
> Replying to [comment:4 leif]:
> > The `SAGE_CHECK` issue (interpreting everything except "no" as "yes") is AFAIK a historical relict; some spkgs might still run the test suite from `spkg-install` if `SAGE_CHECK` is set and set to anything but "no".
> 
> I ran "grep" after unpacking all of the spkg's, and found SAGE_CHECK used in cliquer and mpir.  In both cases, it checks whether it's "yes".

Ok. Maybe we already corrected the others.

> > Replacing every occurrence of exit in sage-env by return should work (then testing $? makes sense); I wonder why Sage is started even if sage-env failed though. (I think there an exit 1 is missing.)
> 
> When do you see Sage starting if sage-env fails?

My bad. I think this happened _after_ I had replaced `exit` by `return` in `sage-env` (screen buffer):

```
Error setting environment variables by running /home/leif/Sage/sage-4.6.alpha1-final/local/bin/sage-env; possibly contact sage-devel (see http://groups.google.com/group/sage-devel).
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage:
```

| Sage Version 4.6.alpha1, Release Date: 2010-09-18                  |
| Type notebook() for the GUI, and license() for information.        |
(But the same happens if `source` itself fails, e.g. because `sage-env` isn't found, likewise when `SAGE_ROOT` contains spaces.)

But if the error message ever gets printed, Sage shouldn't start. We currently have:

```sh
. $SAGE_ROOT/local/bin/sage-env   1>/dev/null 2>/dev/null

if [ $? -ne 0 ]; then
   echo "Error setting environment variables by running $SAGE_ROOT/local/bin/sage-env; possibly cont
act sage-devel (see http://groups.google.com/group/sage-devel)."
fi

...

sage() {
    sage_setup
    sage-ipython "$@" -i
}

if [ $# -eq 0 ]; then
    sage
    exit $?
fi

```



> As far as changing sage-build to source sage-env, could that break things?  The other changes here are pretty inocuous.

I guess that's just an old flaw; calling it is of little use (will only _check_ some things, but doesn't change the environment at all).

So give it a try and see what happens... ;-)

(It _shouldn't_<sup>TM</sup> break anything.)


---

Comment by leif created at 2010-09-21 19:49:22

Since `sage-build` is (or should be) called from `sage-sage`, we can either source it again or completely omit the (second) call.


---

Comment by leif created at 2010-09-21 19:57:39

Replying to [comment:11 leif]:
> Since `sage-build` is (or should be) called from `sage-sage`, we can either source it again or completely omit the (second) call.

_Sourcing it_ / _calling it_ referred to `sage-env`.


---

Comment by drkirkby created at 2010-09-21 20:01:17

Replying to [comment:8 jhpalmieri]:

> I'll also take a look at #9644.  If I can give that a positive review, I'll change the patch here to make it depend on #9644.  (I may do that anyway...)  As far as changing sage-build to source sage-env, could that break things?  The other changes here are pretty inocuous.

I agree. 

John's changes are safe - the others may be desirable, but introduce extra risk. It would be a shame if this change got bounced out because larger changes were added to the ticket. Leif can always create another ticket to fix the other issues. 

I'm keen we improve the code in Sage, but I don't think making lots of changes to a package every time someone wants to make a minor change, is a good idea. Leif knows I was pulling my hair out when all I wanted to do was get iconv to build on HP-UX on #9603. 

One point John, if you do change this patch, there's no need to quote xyes. Since you are absolutely 100% sure that the string xyes has no spaces in it, there's no need to quote it. It's different for a variable like $FOOBAR, where you don't know if it might have a space or not. 

To my knowledge there's nothing in Sage which checks if SAGE64 is "no". The only value actually tested for is "yes", so it's a bit pointless permitting "no". 

Dave


---

Comment by leif created at 2010-09-21 20:13:36

There are already other tickets around touching at least some of the patched files, too.

I'd say adding the quotes around `SAGE_ROOT`, adding the `exit 1` if sourcing failed, and perhaps replacing `exit` by `return` in `sage-env` should be mandatory.

If we always postpone fixes, we'll never get far (and if one opens a new ticket for every "minor" thing at all, we'll most probably just increase the number of open tickets, with lots of rebasing being necessary if some of them finally get merged).

Just my 2 cents.


---

Comment by drkirkby created at 2010-09-21 20:38:56

Replying to [comment:14 leif]:
> There are already other tickets around touching at least some of the patched files, too.
> 
> I'd say adding the quotes around `SAGE_ROOT`, adding the `exit 1` if sourcing failed, and 

I won't argue with the `SAGE_ROOT`. I don't suppose John will. I've not looked at the exit, but that sounds sensible. 

> perhaps replacing `exit` by `return` in `sage-env` should be mandatory.

It adds extra risk. 

> If we always postpone fixes, we'll never get far (and if one opens a new ticket for every "minor" thing at all, we'll most probably just increase the number of open tickets, with lots of rebasing being necessary if some of them finally get merged).
> 
> Just my 2 cents.

You will just frustrate people if you expect them to make many changes to fix a minor issue. Tickets will get left. John has kindly picked up on something that's not hurting his work, but he knows is wrong. Make it too difficult, and people will in general just give up and not bother with such tickets any more. 

There's nothing wrong with having a cleanup ticket, where you can make all the changes you want - for example the Cliquer one #9870. 

Dave


---

Comment by leif created at 2010-09-21 20:54:54

Replacing `exit` by `return` adds no risk if we *do* exit when `$? -ne 0`.

Note that John's initial patch also did more than necessary for the ticket (or announced by its title).

So IMHO one should either do just what's necessary to address a specific issue (and not touch other files), or do "the whole", i.e. fix most of the open issues with the files you touch, at least the "trivial" ones that do not require extraordinary testing (e.g. on all platforms).

There's e.g. still

```sh
   cd "$SAGE_ROOT/devel/sage/sage"
   echo "*** TOUCHING ALL CYTHON (.pyx) FILES ***"
   touch */*.pyx */*/*.pyx */*/*/*.pyx */*/*/*/*.pyx */*/*/*/*/*.pyx */*/*/*/*/*.pyx  */*/*/*/*/*/*.
pyx 2> /dev/null
```

in `sage-build`, too. (Count the asterisks!)


---

Comment by jhpalmieri created at 2010-09-21 21:13:44

Leif: just to clarify, are you suggesting changing _every_ instance of `exit` to `return` in sage-env, or just changing the one relevant to SAGE64?

As far as suppressing output from sage-env, it turns out that there is one bad instance: the output from sage-check-64.  If this is not suppressed, then you can get behavior like this on a 64-bit OS X machine:

```
$ sage -hg status
Building Sage on OS X in 64-bit mode
...
$ sage
Building Sage on OS X in 64-bit mode
...
$ sage -pkg ...
Building Sage on OS X in 64-bit mode
...
```

This is confusing since nothing is actually being built.  It is also not necessary to print this every time any script in local/bin runs, so right now I'm suppressing output from it in sage-env.  Output from it is not suppressed in sage-build.  Perhaps the right place to print this message would be somewhere in sage-spkg?

I'm attaching a new patch.


---

Attachment

scripts repo: depends on #9644


---

Comment by jhpalmieri created at 2010-09-21 21:15:59

> One point John, if you do change this patch, there's no need to quote xyes.

Okay.  I think it's a little more readable if it's quoted, especially the way my editor colorizes things, so I'm leaving it quoted.


---

Comment by leif created at 2010-09-21 21:42:27

Replying to [comment:17 jhpalmieri]:
> Leif: just to clarify, are you suggesting changing _every_ instance of `exit` to `return` in sage-env, or just changing the one relevant to SAGE64?

Yes, every. If you exit in a sourced file, the sourcing shell exits.

(We should then test the return code when/whereever `sage-env` is sourced.)

> As far as suppressing output from sage-env, it turns out that there is one bad instance: the output from sage-check-64.  If this is not suppressed, then you can get behavior like this on a 64-bit OS X machine:

```
$ sage -hg status
Building Sage on OS X in 64-bit mode
...
$ sage
Building Sage on OS X in 64-bit mode
...
$ sage -pkg ...
Building Sage on OS X in 64-bit mode
...
```

> This is confusing since nothing is actually being built.

The `sage-check-64` script is a bit funny...

> It is also not necessary to print this every time any script in local/bin runs, so right now I'm suppressing output from it in sage-env.

We should echo _warning and error messages_ in `sage-env` to `stderr`, then we can redirect `stdout` ("informative" messages) to `/dev/null` in the usual case.

> Output from it is not suppressed in sage-build.  Perhaps the right place to print this message would be somewhere in sage-spkg?

`sage -b` doesn't call `sage-spkg`. We could call `sage-check-64` there, though its use isn't very clear. I either set `SAGE64` or leave it; I don't think there needs to be some extra file which sets it if it ever has been set before. Perhaps Dave can explain the use of that.


---

Comment by leif created at 2010-09-21 22:29:44

What about removing `sage-check-64` from `sage-env` and directly sourcing it in the scripts that actually (attempt to) build something?

Btw, setting `SAGE64=no` should perhaps delete the "flag" file. But if one started with one setting and switched to another, a `make clean` or whatever would be required anyway (interpreting `SAGE64` _not set_ as "use default / previous setting", which seems to be the [undocumented?] current logic).


---

Comment by drkirkby created at 2010-09-21 22:33:43

Replying to [comment:20 leif]:
> What about removing `sage-check-64` from `sage-env` and directly sourcing it in the scripts that actually (attempt to) build something?
> 
> Btw, setting `SAGE64=no` should perhaps delete the "flag" file. But if one started with one setting and switched to another, a `make clean` or whatever would be required anyway (interpreting `SAGE64` _not set_ as "use default / previous setting", which seems to be the [undocumented?] current logic).

What about creating another ticket for that?


---

Comment by drkirkby created at 2010-09-21 22:43:28

I've given positive review to #9644, based on 

 * John was happy with Leif's changes
 * I'm happy with John's changes to the documentation. 

I'll look at this ticket when I have more time, as I'm not sure of the effect of changing the exits to returns. 

I don't know how John feels, but I think we need to stop the ticket dragging on like #9603 did.


---

Comment by drkirkby created at 2010-09-21 23:00:51

It seems to me that by replacing the exits by returns, you are now forcing another file to check the return code. Can anyone explain what we have gained by changing the exits to returns?


---

Comment by jhpalmieri created at 2010-09-21 23:09:21

As far as I understand it, the problem is the code in [an earlier comment](http://trac.sagemath.org/sage_trac/ticket/9960#comment:3): if you use "exit", then do

```
. sage-env

if [ $? -ne 0 ]; then
    ...
```

the exit code for sage-env won't be available, so the code inside the "if" block is never executed.


---

Comment by leif created at 2010-09-21 23:23:17

Exactly. And you'll never see any error message in case you redirected the output to `/dev/null`.

If we only redirect `stdout` when sourcing `sage-env`, and its error messages are printed to `stderr`, we could leave the `exit`s in `sage-env`, but that's in general bad, since the sourcing script might want to do something else or in addition in case of errors.


---

Comment by drkirkby created at 2010-09-21 23:39:57

OK. I'll apply both patches later today (it's 0038 here). Then review it. I'm out most of tomorrow, so it will be late UK time before I can look at it. 


Dave


---

Comment by drkirkby created at 2010-09-21 23:41:26

I mean I'm out most of today (given its just gone midnight here). 



Dave


---

Comment by leif created at 2010-09-22 02:35:12

I've attached a patch to `sage-spkg` to apply on top of John's:
 * Quotes more environment variables.
 * Checks return code of `sage-env` and exits with an error message if non-zero.
 * Fixes successful test suite runs never getting logged.
 * Corrects one comment, adds some more (including on what could further be fixed on another ticket).

Sorry, just noticed the patch's name is wrong (patches `sage-spkg`, not `sage-sage`).


---

Comment by leif created at 2010-09-22 05:34:40

The only side-effect of _sourcing_ `sage-env` twice is that some variables (e.g. `LD_LIBRARY_PATH`) get redundant entries.

We _could_ in principle prevent such by an 

```C
#ifndef FOO
#define FOO
...
#endif
```

analogon. But IMHO a minor issue...


---

Comment by drkirkby created at 2010-09-22 21:32:32

Leif, it would be less confusing if you just deleted the patch, renamed it, then put it back with the right name. Click on the patch, then in the bottom left you should see "Delte". You should be able to delete your own patches. 

If you get a failure, then I can delete it for you, as I have admin rights on trac, but I believe you should be able to delete your own patches.

Let's not add any more changes to this ticket. Leif's changes look OK to me, though I feel they should have been on another ticket.

Dave


---

Comment by leif created at 2010-09-22 22:59:05

Replying to [comment:30 drkirkby]:
> Leif, it would be less confusing if you just deleted the patch, renamed it, then put it back

I would have done so if only I could... :)

> [...] I can delete it for you, as I have admin rights on trac, but I believe you should be able to delete your own patches.

No, there's not even a button to do so, so please delete it for me. (I've replaced the file with the wrong name by an almost empty file and re-uploaded the original with the correct name.)


---

Comment by drkirkby created at 2010-09-22 23:01:34

I've deleted the two files for you. I'm changing to "needs work" until such time as you have attached them. 

Dave


---

Comment by drkirkby created at 2010-09-22 23:01:34

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-09-22 23:05:01

Replying to [comment:30 drkirkby]:
> Let's not add any more changes to this ticket.

I didn't plan that; therefore I've also added comments on what has to get fixed on follow-up tickets.

> Leif's changes look OK to me, though I feel they should have been on another ticket.

Testing the "exit" code of `sage-env` had become necessary because of the other patch.

I'm happy you're happy (or ok) with my changes though. :-)


---

Comment by leif created at 2010-09-22 23:07:25

Replying to [comment:32 drkirkby]:
> I've deleted the two files for you. I'm changing to "needs work" until such time as you have attached them. 

Argh, "it" != both...

Uploading the patch with the correct name *again*.


---

Attachment

SCRIPTS REPO. Apply on top of John's patch.


---

Comment by leif created at 2010-09-22 23:09:43

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-11-06 22:40:49

Can we revive this one?  Dave, do you have any time soon to take a look at it?


---

Comment by drkirkby created at 2010-11-07 10:44:49

I'll try to look at this today - my wife wants me to do some painting, so that has to take priority!

The problem I have is that what was a reasonably easy ticket to understand, now has changes for which I don't know the full implication of them. Whilst I can see why exit was replaced with return, I would not be totally surprised if another part of Sage relies on the current behavior.


---

Comment by leif created at 2010-12-30 15:10:12

*Ping.*

Haven't tried yet, but I'm pretty sure the patches meanwhile need to be rebased...


---

Comment by leif created at 2010-12-30 16:28:52

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-12-30 16:28:52

Replying to [comment:38 leif]:
> Haven't tried yet, but I'm pretty sure the patches meanwhile need to be rebased...

Of course:

```
applying /home/leif/Sage/patches/trac_9960-scripts-SAGE_CHECK.patch
patching file sage-build
Hunk #1 FAILED at 0
Hunk #2 FAILED at 33
Hunk #3 FAILED at 44
3 out of 3 hunks FAILED -- saving rejects to file sage-build.rej
patching file sage-env
Hunk #4 succeeded at 222 (offset 24 lines).
Hunk #5 succeeded at 281 (offset 24 lines).
patching file sage-sage
Hunk #1 FAILED at 141
1 out of 1 hunks FAILED -- saving rejects to file sage-sage.rej
patching file sage-spkg
Hunk #1 succeeded at 368 (offset 10 lines).
abort: patch failed to apply
```

(Sage 4.6.1.rc0)


---

Attachment

SCRIPTS REPO. (Just) John's patch rebased to Sage 4.6.1.rc0.


---

Comment by leif created at 2010-12-30 17:13:38

I've attached a rebased version of John's patch; still have to rebase mine.


---

Attachment

SCRIPTS REPO. My previous patch rebased to Sage 4.6.1.rc0, with some more changes. Apply on top of John's (rebased one).


---

Comment by leif created at 2010-12-31 04:18:18

I've now also attached a rebased version of my "reviewer" patch, with some more changes:

_Besides cosmetic changes (formatting, tabs, some messages), I've only_

 * _added lots of comments (including TODOs/notes on future changes),_
 * _quoted all necessary environment variables,_
 * ''fixed a bug which caused a successful test suite run never getting
   logged (to 'spkg/installed/<package-name>').''

_So there are (still) lots of things to do, but on another ticket._

----

I can of course only review John's changes (which I already did, leading to my reviewer patch, so I'm in principle ok with his changes, although I haven't tested them recently); so someone else has to review mine. (I'm going to test them with 4.6.1.rc0 again though I don't expect new, undesired behavior.)

Additional changes (other than fixes of possible mistakes introduced here) should IMHO be made on follow-up tickets; as mentioned in the commit message (and comments in `sage-spkg`), there are quite a lot things to get fixed or improved.


---

Comment by leif created at 2010-12-31 04:18:18

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-12-31 05:00:57

P.S.:

 * The odd messages from `sage-check-64` when sourcing `sage-env` are already addressed elsewhere (#10303, which unfortunately had to get unmerged from rc0), so John's patch _here_ intentionally (still) _does_ suppress _all_ messages from the former in `sage-env`, as a _temporary_ solution.

 * (Not) sourcing `sage-env` more than once is addressed at #10469.

 * The only scripts directly sourcing `sage-env` are `sage-sage` and `sage-spkg` (both patched here to check its "exit" code), so the changes turning `exit` into `return` there are safe.


---

Comment by leif created at 2010-12-31 05:40:46

*Positive review* from me *for John's patch(es).*

----

This ticket should also (temporarily) fix the doctests errors occurring when `SAGE64=yes`, caused by "_Building a 64-bit version of Sage_" messages.

(I've tested it on Linux only.)


---

Comment by drkirkby created at 2011-02-05 13:29:31

Replying to [comment:22 drkirkby]:

> I don't know how John feels, but I think we need to stop the ticket dragging on like #9603 did. 

Five months ago I wrote the above comment. I could see that if we were not careful, the ticket would drag on, as more and more changes were requested that had nothing to do solving the problem raised. 

John's changes did the job and were not risky. Now the ticket has dragged on and on, with endless other changes, but still no positive review. 

Dave


---

Attachment

replaces all previous patches


---

Comment by jhpalmieri created at 2011-03-24 23:41:00

Here is a new patch, replacing all previous ones.  This takes the crucial elements from my patch and Leif's, and omits everything else.  I've moved most of the rest of Leif's patch to #11021.

Since Leif gave my patch a positive review, and since the new patch consists of mine plus a simple error check (which I'm happy with), I'd like to give this a positive review.  Dave, any opinions?


---

Comment by iandrus created at 2011-03-25 00:35:30

I'm happy that this will obsolete #4029.  Also the rest of the code looks good.  Installing dot2tex with SAGE_CHECK=yes ran the test suite and with SAGE_CHECK=maybe didn't, so I give this a positive review.


---

Comment by iandrus created at 2011-03-25 00:35:30

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2011-03-25 05:45:13

At last!!! 

I still maintain some of these changes should have been on another ticket. John's patch 6-months ago fixed the problem. Had it been merged 6 months ago, Sage would have been better for it. I'm not denying the changes since are an improvement, but I think these improvements would have been better on another ticket. 

Dave


---

Comment by jhpalmieri created at 2011-03-25 14:44:19

Dave, you're probably right, and #4029 would probably have been the right place.  But I think it's done now...


---

Comment by jdemeyer created at 2011-03-27 10:03:10

I get an error when building sage from scratch (but I'm not entirely sure this patch is the cause):

```
Machine:
Linux sage.math.washington.edu 2.6.24-28-server #1 SMP Wed Aug 25 14:46:03 UTC 2010 x86_64 GNU/Linux
Deleting directories from past builds of previous/current versions of sage_scripts-4.7.alpha3
Extracting package /scratch/jdemeyer/merger/sage-4.7.alpha3/spkg/standard/sage_scripts-4.7.alpha3.spkg ...
-rw-r--r-- 1 jdemeyer jdemeyer 990291 2011-03-26 21:12 /scratch/jdemeyer/merger/sage-4.7.alpha3/spkg/standard/sage_scripts-4.7.alpha3.spkg
Finished extraction
****************************************************
Host system
uname -a:
Linux sage.math.washington.edu 2.6.24-28-server #1 SMP Wed Aug 25 14:46:03 UTC 2010 x86_64 GNU/Linux
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zl
ib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.2 --prog
ram-suffix=-4.2 --enable-clocale=gnu --enable-libstdcxx-debug --enable-objc-gc --enable-mpfr --enable-checking=release --build=x86_64-linu
x-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu4)
****************************************************

real    0m0.044s
user    0m0.020s
sys     0m0.020s
/scratch/jdemeyer/merger/sage-4.7.alpha3/local/bin/sage-spkg: line 436: syntax error near unexpected token `('
/scratch/jdemeyer/merger/sage-4.7.alpha3/local/bin/sage-spkg: line 436: `    echo "(cd '`pwd`' && '$SAGE_ROOT/sage' -sh)"'
make[1]: *** [installed/sage_scripts-4.7.alpha3] Error 2
make[1]: Leaving directory `/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.alpha3/spkg'
```



---

Comment by jdemeyer created at 2011-03-27 10:03:10

Changing status from positive_review to needs_work.


---

Comment by drkirkby created at 2011-03-27 14:03:38

Replying to [comment:53 jdemeyer]:
> I get an error when building sage from scratch (but I'm not entirely sure this patch is the cause):

And there was me thinking a very small patch John submitted 6 months ago was finally going to be merged!

I think Leif should *seriously* consider the implications of the endless changes he wants on tickets like this one - changes that are not related to the problem the ticket is supposed to address. 

In many ways I wish all sage developers were as fussy as Leif, as his approach does generally result in improved quality of code. Many of the bugs in Sage would not be there if more people were fussy about code that is written. I cringe at some of the stuff I see written. But Leif's endless requested changes are slowing Sage development to a crawl. 

#9603 took a couple of months to get a positive review on what was originally a 3 or 4 line patch that was only applied on AIX. 

The cliquer package is a complete mess, so I opened a ticket to clean it up (#9870), and another (#9871) to address an important single issue for a 64-bit Solaris port. The latter took ages, due to unrelated changes requested by Leif. Then Leif decided to take ownership of the cleanup patch (#9870), but has done nothing about it in 7 months, despite a couple of reminders from me. 

Not only do these endless changes take longer to implement for the author, but it makes review so much more difficult. Whereas I would have been happy to give a positive review to John's original patch, this has become so complex it is a nightmare reviewing it. 

Dave


---

Comment by drkirkby created at 2011-03-27 14:23:17

Replying to [comment:54 drkirkby]:
 
> #9603 took a couple of months to get a positive review on what was originally a 3 or 4 line patch that was only applied on AIX. 

> Dave 

Correction, #9603 was only applied on HP-UX. The point being a _safe_ change, that was only intended to effect Sage on an unsupported platform became overly complex and dragged on for a long time. 

IMHO, this sort of thing needs to stop. 

Dave


---

Comment by jhpalmieri created at 2011-03-27 15:29:03

Jeroen: The line cited by the error

```
/scratch/jdemeyer/merger/sage-4.7.alpha3/local/bin/sage-spkg: line 436: syntax error near unexpected token `('
/scratch/jdemeyer/merger/sage-4.7.alpha3/local/bin/sage-spkg: line 436: `    echo "(cd '`pwd`' && '$SAGE_ROOT/sage' -sh)"'
```

is not touched by this patch.  Did you run "sage -sdist ..." or just apply the patch to the scripts repo?  If you just applied it to the scripts repo, then the version of sage-spkg in the repo will not match with the version in spkg/base/, and I think that could cause an error like the one you saw.

I ran "sage -sdist ..." and then started building from the new tar file, and it's going fine: it's built around 50 of the spkgs, including sage_scripts, with no problems.


---

Comment by jhpalmieri created at 2011-03-28 18:48:42

Replying to [comment:53 jdemeyer]:
> I get an error when building sage from scratch (but I'm not entirely sure this patch is the cause)

My build completed just fine.  I just tried again: I took a vanilla copy of 4.7.alpha2, applied this patch, ran "sage -sdist ...", and then built from the resulting tar file.  It has started just fine, successfully installing sage_scripts and 40 more spkgs.  The build is still ongoing, but I'm not seeing the error you saw.

Since you're not sure that this patch caused it, what can I do to help resolve this?


---

Comment by jdemeyer created at 2011-03-28 19:30:46

Probably your original comment about `spkg/base` was correct.  But I will have a look at this later.

If you _really_ want to move forward, make sure that no files appear in duplicate places (like `local/bin` and `spkg/base` in this case).  This has caused trouble for me tons of times.  #9433 fixed a lot of these issues, but apparently there is still some work to do.  We should probably get rid of the `spkg/base` repository and use the `SAGE_ROOT` repository for this instead.


---

Comment by jhpalmieri created at 2011-03-28 19:53:44

Replying to [comment:58 jdemeyer]:
 
> If you _really_ want to move forward, make sure that no files appear in duplicate places (like `local/bin` and `spkg/base` in this case).  This has caused trouble for me tons of times.  #9433 fixed a lot of these issues, but apparently there is still some work to do.  We should probably get rid of the `spkg/base` repository and use the `SAGE_ROOT` repository for this instead.

I don't know how to avoid the duplication, but see #11073 for a ticket.


---

Comment by jhpalmieri created at 2011-04-12 16:54:26

I'm not sure why this depends on #11073; can you clarify?  (I have the same question for #11008.)


---

Comment by jdemeyer created at 2011-04-13 07:32:28

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-04-13 07:32:28

Replying to [comment:61 jhpalmieri]:
> I'm not sure why this depends on #11073; can you clarify?

Technically speaking, it doesn't depend on #11073.  But I would really like #11073 to be finished before merging any ticket which affects files in `spkg/base`.  If you insist, I could try to merge #9960 and #11008 anyway (before #11073).


---

Comment by jhpalmieri created at 2011-04-13 16:16:30

I'm concerned that #11073 is going to be complicated: it will touch files in the scripts repo, in the root repo, and (of course) in the base repo.  I'm not even sure what the right approach is for that ticket.  I'll post some questions there.

The fixes in #9960 and #11008 are pretty tame, comparatively.  I think you can just apply the patches on those two tickets and then run "sage -sdist" to make a new source distribution; that should move the changed files to spkg/base.  So I would _prefer_ that you merge those two.  But I'm not going to _insist_; you're the release manager, so if it makes your job much easier to wait, then wait.


---

Comment by jdemeyer created at 2011-05-12 20:27:20

Resolution: fixed
