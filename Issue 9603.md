# Issue 9603: Force iconv to build on HP-UX in addition to Solaris and Cygwin.

Issue created by migration from https://trac.sagemath.org/ticket/9603

Original creator: drkirkby

Original creation time: 2010-07-26 13:33:05

Assignee: GeorgSWeber

CC:  pjeremy mvngu mpatel

Currently iconv builds only on Solaris and Cygwin, as it caused problems on some linux distributions. 

It would be good if this would build on HP-UX too, as then some other packages could be checked on HP-UX to aid testing on different platforms. This ticket makes 3 changes. 

* Changes `#!/bin/bash` to `#!/usr/bin/env bash` in spkg-check. This in in conformance with the [Sage Developers Guide](http://www.sagemath.org/doc/developer/producing_spkgs.html#creating-a-new-spkg) and is necessary on HP-UX as 'bash' is not installed in /bin.


```
-#!/bin/bash
+#!/usr/bin/env bash
```


* Force install on HP-UX, instead of just Cygwin and Solaris. The relevant bit of the patch is:

```
-# Only build iconv on Solaris and Cygwin
-if [ "x$UNAME" != xSunOS ] && [ "x$UNAME" != xCYGWIN ] ; then  
+# Only build iconv on Solaris, HP-UX and Cygwin
+if [ "x$UNAME" != xSunOS ] && [ "x$UNAME" != xHP-UX ] && [ "x$UNAME" != xCYGWIN ] ; then
```

* Force iconv to be checked only HP-UX, in addition to Solaris and Cygwin on which it was previously checked. 

```
-if [ "x$UNAME" != xSunOS ] && [ "x$UNAME" != xCYGWIN ] ; then  
+if [ "x$UNAME" != xSunOS ] && [ "x$UNAME" != xHP-UX ] && [ "x$UNAME" != xCYGWIN ] ; then
```


* Print all tests have pass if they have done. The relevant bit of the patch is 


```
+echo "All the tests for iconv passed"
+exit 0 
```



---

Comment by drkirkby created at 2010-07-26 14:06:45

Here we can see all tests pass on HP-UX. It should also be clear the changes only effect HP-UX and will have no effect on other platforms. 


```
-bash-4.0$ uname -a
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license

-bash-4.0$ ./sage -f iconv-1.13.1.p3

<snip>

./check-translit . Quotes UTF-8 ASCII
./check-translit . Translit1 ISO-8859-1 ASCII
./check-translitfailure . TranslitFail1 ISO-8859-1 ASCII
./check-subst
./test-shiftseq
make[1]: Leaving directory `/home/drkirkby/sage-4.5.2.alpha0/spkg/build/iconv-1.13.1.p3/src/tests'
All the tests for iconv passed
Now cleaning up tmp files.
```



---

Comment by drkirkby created at 2010-07-26 14:10:02

Mercurial patch to force iconv to build on HP-UX  in addition to the Solaris and Cygwin it currently builds on. iconv passes all tests on HP-UX. The changes will have no effect on other platforms.


---

Attachment


---

Comment by drkirkby created at 2010-07-26 21:27:39

The package may be found here. 

http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg

I'd appreciate a review. I realise not many people have access to HP-UX, but it should be apparent this will affect no other platform. 

Dave


---

Comment by drkirkby created at 2010-07-26 21:27:39

Changing status from new to needs_review.


---

Comment by pjeremy created at 2010-07-26 23:49:34

I am unable to test on HP-UX but visual inspection of the diffs between iconv-1.13.1.p2.spkg and http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg looks correct.  Running both spkg-install and spkg-check on FreeBSD behave as expected.


---

Comment by drkirkby created at 2010-07-27 09:48:13

Replying to [comment:5 pjeremy]:
> I am unable to test on HP-UX but visual inspection of the diffs between iconv-1.13.1.p2.spkg and http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg looks correct.  Running both spkg-install and spkg-check on FreeBSD behave as expected.

Thank you Peter. 

I'm attaching a log of an install on HP-UX. 

I also noticed that the message saying it was being installed since the OS was Solaris or Cygwin. I changed that message to:


```
Installing iconv as the operating system is Cygwin, HP-UX or Solaris
```


Dave


---

Comment by drkirkby created at 2010-07-27 09:49:24

Improve a message as the package installed, to mention HP-UX too.


---

Attachment

Build log from a HP C3600 running HP-UX. Note SAGE_CHECK was set to "yes" so the self tests were run. They all pass


---

Attachment


---

Comment by drkirkby created at 2010-07-27 18:23:48

Changing assignee from GeorgSWeber to drkirkby.


---

Comment by leif created at 2010-07-27 19:41:19

Style-wise, I would invert the test to something like:

```sh
if [ "$UNAME" = SunOS -o "$UNAME" = CYGWIN -o "$UNAME" = HP-UX ]; then

    # install spkg/run test suite, check exit code, ...

else

    # print message that iconv will not be installed/tested
    # because *the system's* one is/will be used (rather than
    # the one shipped with Sage), exit 0

fi
```

(I.e., clarifying the messages a bit, too.)


Dave, you're right, I do not have access to an HP-UX system, but I don't think that's necessary to give it a positive review.


I'll later take a look at the whole...


-Leif

P.S.: Peter is (already) listed as reviewer, should I than delete him in case I give it positive review (and if he hasn't yet)?


---

Comment by leif created at 2010-07-27 20:03:27


```
...
Now cleaning up tmp files.
rm: directory /home/drkirkby/sage-4.5.2.alpha0/spkg/build/iconv-1.13.1.p3 not removed.  Cannot remove current directory
Making Sage/Python scripts relocatable...
...
```


Yet another `sage-spkg` bug... :|


---

Comment by drkirkby created at 2010-07-27 21:51:52

Replying to [comment:8 leif]:
> Style-wise, I would invert the test to something like:
> {{{
> #!sh
> if [ "$UNAME" = SunOS -o "$UNAME" = CYGWIN -o "$UNAME" = HP-UX ]; then
> 
>     # install spkg/run test suite, check exit code, ...
> 
> else
> 
>     # print message that iconv will not be installed/tested
>     # because *the system's* one is/will be used (rather than
>     # the one shipped with Sage), exit 0
> 
> fi
> }}}
> (I.e., clarifying the messages a bit, too.)
> 
> 
> Dave, you're right, I do not have access to an HP-UX system, but I don't think that's necessary to give it a positive review.
> 
> 
> I'll later take a look at the whole...
> 
> 
> -Leif
> 
> P.S.: Peter is (already) listed as reviewer, should I than delete him in case I give it positive review (and if he hasn't yet)?

I try to write my scripts as portable as I possibly can. I've tended to ask on [comp.unix.shell](http://groups.google.com/group/comp.unix.shell/topics) where some shell scripting wizards hang out. I've just asked [for comment on -o vs ||](http://groups.google.com/group/comp.unix.shell/browse_thread/thread/4081999fef86b878#)

It's true that for the bash shell, either `-o` or `||` will work, but there are a number of older shells which don't behave well in such circumstances. `||` is more portable than `-o`, and `&&` is more portable than `-a`. Likewise testing for `""` causes problems with some shells. I think the problems usually occur if there is more than one -o or -a on a line, which is what is needed here. I try to write my scripts which will work with any shell, though I stick `#!/usr/bin/env bash` at the top to be consistent with the rest of Sage. 

Changing the style introduces risks that I'd rather not introduce. The risk of introducing a bug increases the more changes one makes to the script. I would not be very popular if I tried to implement something for HP-UX that happens to break on some Linux system! At the moment the script does work reliably, so I'd prefer to limit the changes that are necessary to achieve the aim. 

I've tested this on Solaris, HP-UX and Linux. Peter has checked it on FreeBSD. If the style of the script is changed, so that testing needs to be repeated. 

The top of spkg-install has a description of what it is doing, and a link to the ticket which resulted in the decision to make iconv install only on Solaris and Cygwing, so I'm not really sure there is need for further explanation. 

If you feel there needs to be some more comments in the code, I will add them. But I do not feel changing the style is a good idea. It introduces unnecessary risks. 

Perhaps Peter has some comments on this. 

There's no need to delete Peter as a reviewer, as he has provided valuable input. 

Dave


---

Comment by drkirkby created at 2010-07-27 21:58:05

Replying to [comment:9 leif]:
> {{{
> ...
> Now cleaning up tmp files.
> rm: directory /home/drkirkby/sage-4.5.2.alpha0/spkg/build/iconv-1.13.1.p3 not removed.  Cannot remove current directory
> Making Sage/Python scripts relocatable...
> ...
> }}}
> 
> Yet another `sage-spkg` bug... :|

Yes, I've seen endless messages about being unable to delete the current directory. This is another instance where one would need to be very careful in changing things. Fixing the bug might actually introduce a bug. Adding a -f just hides the problem. I don't really know the answer to this. 

I see this on both Solaris and HP-UX - can't recall if that warning is printed on Linux or not. 

Dave


---

Comment by leif created at 2010-07-27 22:12:20

Replying to [comment:11 drkirkby]:
> Replying to [comment:9 leif]:

```
...
Now cleaning up tmp files.
rm: directory /home/drkirkby/sage-4.5.2.alpha0/spkg/build/iconv-1.13.1.p3 not removed.  Cannot remove current directory
Making Sage/Python scripts relocatable...
...
```

> > 
> > Yet another `sage-spkg` bug... :|
> 
> Yes, I've seen endless messages about being unable to delete the current directory.

This *must* happen on any system...

> This is another instance where one would need to be very careful in changing things. Fixing the bug might actually introduce a bug. Adding a -f just hides the problem. I don't really know the answer to this.

No, the fix is harmless. The solution is not to add `-f` (it is already `-rf` btw), but to `cd ..` before doing so. (It seems somebody added the `cd $BASEDIR` later without looking at all the code below it.)

> I see this on both Solaris and HP-UX - can't recall if that warning is printed on Linux or not. 

See above, it's a "must have" :)


---

Comment by leif created at 2010-07-27 22:17:57

Replying to [comment:12 leif]:
> See above, it's a "must have" :)

Oh, I think I lied. The `-f` seems to suppress the message on Linux.


---

Comment by leif created at 2010-07-27 22:47:53

Replying to [comment:10 drkirkby]:
> Replying to [comment:8 leif]:
> > P.S.: Peter is (already) listed as reviewer, should I than delete him in case I give it positive review (and if he hasn't yet)?

I completely missed his comment at that time, and did not notice he added his name himself there, sorry for that. (Though most tickets only list those as reviewers who actually gave _positive_ review... - not a very good practice IMO.)

> I try to write my scripts as portable as I possibly can. I've tended to ask on [comp.unix.shell](http://groups.google.com/group/comp.unix.shell/topics) where some shell scripting wizards hang out. I've just asked [for comment on -o vs ||](http://groups.google.com/group/comp.unix.shell/browse_thread/thread/4081999fef86b878#)

Of course a bit funny to both require `bash` and then try to be as portable as possible with respect to the shell (though `test` is actually a _program_, too), but I don't mind.

> Changing the style introduces risks that I'd rather not introduce. The risk of introducing a bug increases the more changes one makes to the script. I would not be very popular if I tried to implement something for HP-UX that happens to break on some Linux system! At the moment the script does work reliably, so I'd prefer to limit the changes that are necessary to achieve the aim.

Hmm, my main intention was to just invert the test, because it's bad style (and inefficient and I think more error-prone) as it is now.

Of course you can use `[ ... ] || [ ... ] || ...` as well, though this invokes more instances of `test` if it's not a shell built-in.

> The top of spkg-install has a description of what it is doing, and a link to the ticket which resulted in the decision to make iconv install only on Solaris and Cygwing, so I'm not really sure there is need for further explanation.
> If you feel there needs to be some more comments in the code, I will add them.

I meant just the _messages_ visible to the user. 

> But I do not feel changing the style is a good idea. It introduces unnecessary risks.

See above. Every code change of course carries some risk (cf. the garbage in PARI's `spkg-install`), but if tickets were always reviewed properly, such things would (or will) not happen. In my opinion cleaning up "grown" code is important, too. (And sometimes it's even better to rewrite things from scratch.)


-Leif


---

Comment by jhpalmieri created at 2010-07-27 22:50:18

> No, the fix is harmless. The solution is not to add -f (it is already -rf btw), but to cd .. before doing so.

See #9444.


---

Comment by drkirkby created at 2010-07-28 00:38:09

Change the style of the tests, in the light of comments from the reviewer.


---

Attachment

I've changed the style of the tests somewhat, which will hopefully make the logic clearer. 

http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg

I've checked it on Solaris and Linux. It installs and passes the tests on Solaris, but does not install on Linux. On Linux it correctly reports that the tests will not be run. 

Is that better? 

Dave


---

Comment by leif created at 2010-07-28 01:57:54

Replying to [comment:16 drkirkby]:
> I've changed the style of the tests somewhat, which will hopefully make the logic clearer.

Yes, I like that. (Mike will perhaps not be amused by testing for HP-UX prior to Cygwin in `spkg-install`... ;-) )

There are some typos/grammatical flaws in the comments and messages.

I'd prefer using `$UNAME` all the time (instead of in addition ``uname``).

`CFLAGS` are overwritten when `$SAGE64=yes`.

I'd use `$MAKE` instead of `make` (in both `spkg-check` and `spkg-install`). If parallel make should be disabled in some cases, I would then either do `$MAKE -j1 [target]` or `export MAKE="$MAKE -j1" ; ... $MAKE [target]`.

I've still not looked at the whole; I think I'll do tomorrow...


---

Comment by drkirkby created at 2010-07-29 10:09:37

Replying to [comment:17 leif]:

> There are some typos/grammatical flaws in the comments and messages.
> 
> I'd prefer using `$UNAME` all the time (instead of in addition ``uname``).
> 
> `CFLAGS` are overwritten when `$SAGE64=yes`.
> 
> I'd use `$MAKE` instead of `make` (in both `spkg-check` and `spkg-install`). If parallel make should be disabled in some cases, I would then either do `$MAKE -j1 [target]` or `export MAKE="$MAKE -j1" ; ... $MAKE [target]`.
> 
> I've still not looked at the whole; I think I'll do tomorrow...

Did you get a chance to look at this? I'd rather fix all the problems at once. 

Dave


---

Comment by leif created at 2010-07-29 18:18:27

Replying to [comment:18 drkirkby]:
> Replying to [comment:17 leif]:
> > I've still not looked at the whole; I think I'll do tomorrow...
> Did you get a chance to look at this?

No, I'm sorry, not yet. It'll most probably get Saturday or Sunday.

> I'd rather fix all the problems at once. 

Yes, I understand that.


---

Comment by drkirkby created at 2010-08-07 22:27:25

Replying to [comment:19 leif]:
> Replying to [comment:18 drkirkby]:
> > Replying to [comment:17 leif]:
> > > I've still not looked at the whole; I think I'll do tomorrow...
> > Did you get a chance to look at this?
> 
> No, I'm sorry, not yet. It'll most probably get Saturday or Sunday.
> 
> > I'd rather fix all the problems at once. 
> 
> Yes, I understand that.

Any chance of you looking at this? I'd like to get it reviewed and out of the way. What was originally the change of about 50 bytes has now taken a long time! 

Dave


---

Comment by leif created at 2010-08-10 14:51:31

Unfortunately, I'd make _a lot_ of changes (besides those I already mentioned), in different "categories", but most of them more or less important or of cosmetic nature.

The only actual change _to the code_ is quoting all instances of `$SAGE_LOCAL`, for (far) future support of spaces in `$SAGE_ROOT`. (In addition, one _could_ test if spaces in it would break `configure` or `make` etc.)

In random order:

 * Remove trailing whitespace (and a superfluous semicolon in `spkg-install` and `spkg-check`).
   (I really hate such changes, since they make [cumulative] patches unreadable.)
 * `s/== iconv ==/= iconv =/` since it is the top-level heading.
 * Add blank lines below section headings. (I think this is common practice, and makes the plain text more readable.)
 * Move _"For more details ..."_ to (new) _"Upstream Contact"_ section.
 * The following is perhaps (partly) obsolete, but currently completely misleading:
     _"spkg-install removes ALL files installed by iconv - man pages, docs, etc etc. If iconv gets updated, check these still remove all traces of iconv._

     _The sizes of the docs and man pages is small, so they are not work removing from the package, as they potentially risk breaking the install."_
   (In fact *nothing* is removed *after* `make install`. I don't think something has been removed from the upstream source tree; at least in `spkg-install` nothing gets removed ("patched") from that, and `configure` doesn't get any `--without-...` options or alike. In short, when updating the package, one should make sure all traces of _previous installations_ of iconv still get removed _prior to [re]installation_. Otherwise some code has to be added to remove "useless" parts of iconv _from the Sage installation_ *after* `make install`.)
 * One could add the usual _"Building a 64-bit version of ..."_ message.
 * Some messages and comments need clean-up (punctuation, grammar/typos, and IMHO formulation; some messages perhaps also "layout")...

I've looked at the package yesterday, but I don't think I've forgotten something... ;-)


---

Comment by leif created at 2010-08-10 14:57:43

P.S.: I tried to mark this ticket `# long time`, but that didn't work.

(Sorry I had lots of other things to do, with really higher priority. Also, not every day can be a Sage Day, and HP-UX support isn't on top of my Sage TODO list... ;-) )


---

Comment by drkirkby created at 2010-08-10 15:15:51

Replying to [comment:21 leif]:
> Unfortunately, I'd make _a lot_ of changes (besides those I already mentioned), in different "categories", but most of them more or less important or of cosmetic nature.

But those lots of changes should be on another ticket. They have nothing to do with fixing the HP-UX issue! 

As you know, I am quite keen to improve the quality of Sage, so I will make them. But be aware I've tried to get people to make more important changes before, and William has overruled, saying that the patch fixes the problem it aims to fix, and that other changes should be on another ticket. 

I'll produce a new package in a day or so. 

> The only actual change _to the code_ is quoting all instances of `$SAGE_LOCAL`, for (far) future support of spaces in `$SAGE_ROOT`. (In addition, one _could_ test if spaces in it would break `configure` or `make` etc.)


I'll try to make all changes. 
 
> In random order:
> 
>  * Remove trailing whitespace (and a superfluous semicolon in `spkg-install` and `spkg-check`).
>    (I really hate such changes, since they make [cumulative] patches unreadable.)
>  * `s/== iconv ==/= iconv =/` since it is the top-level heading.
>  * Add blank lines below section headings. (I think this is common practice, and makes the plain text more readable.)
>  * Move _"For more details ..."_ to (new) _"Upstream Contact"_ section.
>  * The following is perhaps (partly) obsolete, but currently completely misleading:
>      _"spkg-install removes ALL files installed by iconv - man pages, docs, etc etc. If iconv gets updated, check these still remove all traces of iconv._

The point of that is that if you run `make install`, then run the package for a second time, it will clean out all the files made on a previous build. You can't do `make distclean` at that point as there's no makefile. But I'll remove that. 
 
>      _The sizes of the docs and man pages is small, so they are not work removing from the package, as they potentially risk breaking the install."_
>    (In fact *nothing* is removed *after* `make install`. I don't think something has been removed from the upstream source tree; at least in `spkg-install` nothing gets removed ("patched") from that, and `configure` doesn't get any `--without-...` options or alike. In short, when updating the package, one should make sure all traces of _previous installations_ of iconv still get removed _prior to [re]installation_. Otherwise some code has to be added to remove "useless" parts of iconv _from the Sage installation_ *after* `make install`.)

Nothing is removed. It was just a remark. I can remove it if you feel it causes confusion. 

>  * One could add the usual _"Building a 64-bit version of ..."_ message.

No problem. 

>  * Some messages and comments need clean-up (punctuation, grammar/typos, and IMHO formulation; some messages perhaps also "layout")...

I'll try, but lets hope there are not too many itterations of this! 
 
> I've looked at the package yesterday, but I don't think I've forgotten something... ;-)


---

Comment by drkirkby created at 2010-08-10 15:25:07

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-08-10 15:25:07

Replying to [comment:22 leif]:
> P.S.: I tried to mark this ticket `# long time`, but that didn't work.

I'm not sure of what you mean there. 

> (Sorry I had lots of other things to do, with really higher priority. Also, not every day can be a Sage Day, and HP-UX support isn't on top of my Sage TODO list... ;-) )

I realise that. Thanks for looking at the ticket - it's hard to get anyone to look at HP-UX tickets! 

HP-UX can be useful, since where there are problems on one platform but not another, it helps to get a third perspective of it. I'm not convinced there will ever be a complete HP-UX port. 

Dave


---

Comment by leif created at 2010-08-10 16:15:57

Replying to [comment:23 drkirkby]:
> Replying to [comment:21 leif]:
> > Unfortunately, I'd make _a lot_ of changes (besides those I already mentioned), in different "categories", but most of them more or less important or of cosmetic nature.
> 
> But those lots of changes should be on another ticket. They have nothing to do with fixing the HP-UX issue!

If you don't emphasize/focus on HP-UX (i.e. e.g. add _"improve iconv package"_), perhaps more people will take a look at this ticket. :)

> As you know, I am quite keen to improve the quality of Sage, so I will make them. But be aware I've tried to get people to make more important changes before, and William has overruled, saying that the patch fixes the problem it aims to fix, and that other changes should be on another ticket.

Perhaps sometimes [this](http://en.wikipedia.org/wiki/Procrastination). But it really depends on whether the changes are to the Sage library or spkgs, and - more important - on the type of the changes. If major bugs have to be fixed, doing so shouldn't be delayed by cosmetic improvements. Other code changes carry the risk of introducing new issues, so it might be appropriate to separate them. Others are better done at the same time, especially to avoid conflicting patches/tickets, and I think we don't want to create lots of new spkgs in sequence fixing "minor" things step by step.

_Either_ change 10 _or_ 10000 bytes..., i.e. fix a single issue _and open a follow-up ticket_ (with instructions) for _all_ the rest, or do the whole job. My opinion. (Almost nobody will open a ticket to fix a single typo, and people seem unlikely to review "cosmetic" tickets. Similar to the apparently ever-lasting documentation problem.)

> I'll produce a new package in a day or so. 

Or just upload one (or more) patch(es) prior to creating a new spkg.

> >  * The following is perhaps (partly) obsolete, but currently completely misleading:
> >      _"spkg-install removes ALL files installed by iconv - man pages, docs, etc etc. If iconv gets updated, check these still remove all traces of iconv._
> 
> The point of that is that if you run `make install`, then run the package for a second time, it will clean out all the files made on a previous build. You can't do `make distclean` at that point as there's no makefile. But I'll remove that.

I'd simply clarify that. (And emphasize somehow this is unrelated to the next sentence/paragraph:)

> >      _The sizes of the docs and man pages is small, so they are not work removing from the package, as they potentially risk breaking the install."_

> Nothing is removed. It was just a remark. I can remove it if you feel it causes confusion.

(See above.) Perhaps make this an explicit, _separate_ suggestion (_"TODO:"_) to avoid confusion.

> >  * Some messages and comments need clean-up (punctuation, grammar/typos, and IMHO formulation; some messages perhaps also "layout")...
> 
> I'll try, but lets hope there are not too many itterations of this!

:) I fear that, too. Perhaps create a _separate_ patch for that (or omit it in the first place), and let Peter or me create a reviewer patch on top of the other changes.


---

Attachment

Correct unquoted "$SAGE_LOCAL" and a bit of a cosmetic cleanup.


---

Comment by drkirkby created at 2010-08-10 20:21:01

I've attached a patch, and also updated the .spkg at 

http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg

Hopefully that is to your liking - it not, make a reviewer patch. 

I think I'll open a few "clean-up" packages when I want to sneak in an HP-UX patch. 

Dave


---

Comment by drkirkby created at 2010-08-10 20:21:01

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-08-26 00:58:38

Replying to [comment:22 leif]:
> P.S.: I tried to mark this ticket `# long time`, but that didn't work.
> 
> (Sorry I had lots of other things to do, with really higher priority. Also, not every day can be a Sage Day, and HP-UX support isn't on top of my Sage TODO list... ;-) )

I realise HP-UX is not top of your priority list (it is not mine either), but this ticket could have been very simple, but it has now been open for more than a month. The original patch just added the following:

`&& [ "x$UNAME" != xHP-UX ]`

in a couple of files.

Since then you have asked me to make many changes to the `iconv` package that are unrelated to the HP-UX patch. I've done them, though I think it is fair to say that the `iconv` package was already one of the cleaner ones - compare it to Singular, Pari, ATLAS and many others! 

But the ticket has now been open a month, and it is two weeks since you last commented. If you don't feel you will be able to review it within the next few days, please let me know and I'll consider trying to find another reviewer. 


Dave


---

Comment by leif created at 2010-08-26 11:52:53

Well, meanwhile iconv was buried rather deep in one of my stacks of notes...

The latest patch looks quite fine, so my reviewer patch will be fairly small. :)

Can you confirm that _reinstalling_ iconv still works, since you also dropped _the code_ that removed the traces of previous iconv installations?

(I only meant _the remarks in `SPKG.txt`_ were confusing, especially the second - perhaps unrelated - paragraph; see my [comment above](http://trac.sagemath.org/sage_trac/ticket/9603#comment:21). I suggested replacing this by _"When updating the package, one should make sure all traces of previous installations of iconv still get removed prior to [re]installation."_, unless this has become obsolete now, which I don't know.)

Also, can you check if using `$MAKE` instead of `make` in both `spkg-install` and `spkg-check` (especially when doing a parallel build, i.e. with multiple `make` jobs) would work?

(You haven't [yet] changed that, but we should _always_ use `$MAKE` instead of `make`, since the user might have set it to something else, not limited to e.g. `"make -j"`. As noted above, in case parallel build/check doesn't work, we should use `$MAKE -j1 ...`.)


---

Comment by leif created at 2010-08-26 11:52:53

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2010-08-26 13:07:49

Replying to [comment:29 leif]:
> Well, meanwhile iconv was buried rather deep in one of my stacks of notes...
> 
> The latest patch looks quite fine, so my reviewer patch will be fairly small. :)

Relief!! 
 
> Can you confirm that _reinstalling_ iconv still works, since you also dropped _the code_ that removed the traces of previous iconv installations?

Yes, it is OK

Although I added the code originally to delete previous parts of the install, I think it is perhaps not wise. It's simply going to be impossible to do this accurately all the time. The best we could do it to get it working for most people most of the time. It might be feasible if a package only installs a few files, but when many files are installed, and the installed files will probably change with operating system, it is hard to do well. I think it's best simply to not try at all. In any case, few if any other Sage packages do this. I can't think of one in fact. 
 
> Also, can you check if using `$MAKE` instead of `make` in both `spkg-install` and `spkg-check` (especially when doing a parallel build, i.e. with multiple `make` jobs) would work?

I will do. 

> (You haven't [yet] changed that, but we should _always_ use `$MAKE` instead of `make`, since the user might have set it to something else, not limited to e.g. `"make -j"`. As noted above, in case parallel build/check doesn't work, we should use `$MAKE -j1 ...`.)
 
I realise this. However, I am well aware that making changes like that are well outside the scope of the original ticket, and potentially more risky. 

If I get a ticket merged with the title *Force iconv to build + install on HP-UX. Currently it is only installed on Solaris and Cygwin* and that screws up a build on Linux, I am not going to be a very popular person that is for sure! Enabling parallel builds is easy to do, but difficult to test thoroughly. 

Thankfully, iconv is only installed on Solaris and Cygwin, so hopefully this wont cause too many guns to be fired at me if it goes wrong! This ticket has been changed from one that was very safe (adding `&& [ "x$UNAME" != xHP-UX ]` in a couple of places), into one which has major changes to the structure, style and possibly the inclusion of parallel builds. Really I feel those changes should have been on another ticket.  

I think I'm going to change the title. And you can be sure I will deflect some of the blame at you if it goes wrong!!! 

I'll check to *needs review* once I've tested this. 

Dave


---

Comment by leif created at 2010-08-26 14:21:10

Replying to [comment:30 drkirkby]:
> Replying to [comment:29 leif]:
> > Can you confirm that _reinstalling_ iconv still works, since you also dropped _the code_ that removed the traces of previous iconv installations?
> 
> Yes, it is OK
> 
> Although I added the code originally to delete previous parts of the install, I think it is perhaps not wise. It's simply going to be impossible to do this accurately all the time. The best we could do it to get it working for most people most of the time. It might be feasible if a package only installs a few files, but when many files are installed, and the installed files will probably change with operating system, it is hard to do well. I think it's best simply to not try at all. In any case, few if any other Sage packages do this. I can't think of one in fact.

I thought it was some iconv flaw that previously broke reinstallations; in that case, we could perhaps as well have patched the upstream installation procedure.

 
> > Also, can you check if using `$MAKE` instead of `make` in both `spkg-install` and `spkg-check` (especially when doing a parallel build, i.e. with multiple `make` jobs) would work?
> 
> I will do. 
> 
> > (You haven't [yet] changed that, but we should _always_ use `$MAKE` instead of `make`, since the user might have set it to something else, not limited to e.g. `"make -j"`. As noted above, in case parallel build/check doesn't work, we should use `$MAKE -j1 ...`.)
>  
> I realise this. However, I am well aware that making changes like that are well outside the scope of the original ticket, and potentially more risky.

Perhaps ask Mike if this would currently cause any issues on Cygwin.


> If I get a ticket merged with the title *Force iconv to build + install on HP-UX. Currently it is only installed on Solaris and Cygwin* and that screws up a build on Linux, I am not going to be a very popular person that is for sure! Enabling parallel builds is easy to do, but difficult to test thoroughly. 
> 
> Thankfully, iconv is only installed on Solaris and Cygwin, so hopefully this wont cause too many guns to be fired at me if it goes wrong!

:)

> This ticket has been changed from one that was very safe (adding `&& [ "x$UNAME" != xHP-UX ]` in a couple of places), into one which has major changes to the structure, style and possibly the inclusion of parallel builds. Really I feel those changes should have been on another ticket.  
> 
> I think I'm going to change the title. And you can be sure I will deflect some of the blame at you if it goes wrong!!! 

I thought "HP-UX" already went into a footnote to attract more reviewers... ;-)

(It's now actually a clean-up ticket, too.)

 
> I'll check to *needs review* once I've tested this. 

Ok.


---

Comment by leif created at 2010-08-26 14:25:52

P.S.: Using `make` could in fact fail for people who [have to] set `MAKE` to e.g. `gmake` or `/some/strange/path/to/functional/make`.


---

Comment by drkirkby created at 2010-08-26 22:25:10

I've tested this in parallel on my Sun Ultra 27 running OpenSolaris 127 times. It builds and passes all iconv's tests every time. 

My machine is under a *very* heavy load at the minute as I'm running `make ptestlong` 100 times in a loop! Needless to say `iconv` takes a while to install. But with `MAKE` to to `make -j12`, the time to just install (not run the tests), is


```
real	1m59.844s
user	0m19.226s
sys	0m9.280s
Successfully installed iconv-1.13.1.p3
```


So the total CPU time is 28.5 seconds, and the installation time 1m59s for a parallel build with 12 threads on this 4-core, hyperthreaded machine. (1 physical PCU, 4 cores, 8 threads). 

With `MAKE` unset, so a serial build, the installation time rose to 3m:49s


```
real	3m46.106s
user	0m19.233s
sys	0m9.788s
Successfully installed iconv-1.13.1.p3
```


The parallel build is faster by a factor of around 1.9. The actual CPU time used remained virtually unchanged. So the parallel install seems worthwhile. 

I'll repeat this on `t2.math` for as long as my patience permits. That has a lot more cores, but is very slow overall. I doubt I'll test as extensively. I'll then ask Mike to test on Cygwin. 

I've not updated the package yet. I'll do that when I'm finished more testing. 

I've changed the title, so I don't get quite as much **** thrown at me if this goes wrong! The content of the HP-UX changes are now about 1% I think!

Dave


---

Comment by drkirkby created at 2010-08-27 18:32:45

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-08-27 18:32:45

OK, I'm happy with 

http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg

now. Mike Hansen has said it OK on Cygwin:


```
On Fri, Aug 27, 2010 at 3:21 AM, Dr. David Kirkby
<david.kirkby@onetel.net> wrote:
> > http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg
> >
> > I don't believe there will be any issues with Cygwin, but it would be nice
> > to know.
Looks good to me.

--Mike
```


and I've personally tested it with parallel builds many times. 

 * 127 times on OpenSolaris using my Sun Ultra 27 with 12 threads. 
 * 50 times on Solaris 10 (t2.math) with 128 threads. 
 * 13 times on HP-UX. Single threaded only - this is a uni-processor machine. 

In each case, all iconv's tests pass. 

Perhaps Leif could add a reviewer patch for anything else he feels needs addressing, as it should be very minor now. 

Dave


---

Comment by drkirkby created at 2010-08-27 18:44:19

Replaces 'make' by '$MAKE'. Hopefully the last patch needed!


---

Attachment

I'm marking this as needs work, since another problem with iconv (#9718) on some 64-bit Solaris systems has been solved by the libtool developer Ralf Wildenhues. It makes sense to fix that issue at the same time. 

I'll address this later. 

Dave


---

Comment by drkirkby created at 2010-08-29 11:52:37

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-08-29 16:17:25

I'm now marking this as needs review.

I've changed the priority from minor to major, as this resolves a problem (#9718) on 64-bit Solaris, and there is a concerted effort to now get Sage to build on 64-bit Solaris and OpenSolaris. Prior to this, the ticket was originally to build iconv on HP-UX, which was a minor issue.


---

Comment by drkirkby created at 2010-08-29 16:17:25

Changing priority from minor to major.


---

Comment by drkirkby created at 2010-08-29 16:17:25

Changing status from needs_work to needs_review.


---

Attachment

Change the place where the flag for 64-bit builds is inserted from CFLAGS to CC.


---

Comment by leif created at 2010-09-08 12:09:37


```
## Special Update/Build Instructions
 * [...] anyone updating this package should be familiar with how
   to write shell scripts.
```

Can we paste this into *every* `SPKG.txt`? :D :D :D

I'll commit your latest changes in your name...


---

Attachment

SPKG patch. Apply on top of other patches. (Consistently use `"$UNAME"`; clean-up.)


---

Comment by drkirkby created at 2010-09-08 16:24:59

Replying to [comment:37 leif]:
> {{{
> == Special Update/Build Instructions ==
>  * [...] anyone updating this package should be familiar with how
>    to write shell scripts.
> }}}
> Can we paste this into *every* `SPKG.txt`? :D :D :D

Yes, but then nothing would ever get updated I guess. 

Do you want me to create a new .spkg or are you intending to? I note the filename includes `first_reviewer_patch`. Can I expect more reviewer patches? 

Dave


---

Comment by leif created at 2010-09-08 16:44:41

Replying to [comment:38 drkirkby]:
> Replying to [comment:37 leif]:

```
## Special Update/Build Instructions
 * [...] anyone updating this package should be familiar with how
   to write shell scripts.
```

> > Can we paste this into *every* `SPKG.txt`? :D :D :D
> 
> Yes, but then nothing would ever get updated I guess. 

And we (still) have spkgs with (only) Python scripts, too.

If no new patches have to be applied (or old ones removed), and no configuration changes are necessary, replacing the contents of `src/` shouldn't be a big deal. (Though some people copy the whole spkg folder to a new one omitting "hidden" files, i.e. the Mercurial repository! ;-) )

> Do you want me to create a new .spkg or are you intending to? I note the filename includes `first_reviewer_patch`. Can I expect more reviewer patches? 

I'm currently preparing a second, _optional_ reviewer patch with stylistic changes to `spkg-install` and `spkg-check` as a suggestion, for "review". I wonder if such would cause further excessive testing, so I consider it optional.

I could upload one or two new spkgs soon, too. At your taste.


---

Comment by drkirkby created at 2010-09-08 16:51:39

Replying to [comment:39 leif]:

> If no new patches have to be applied (or old ones removed), and no configuration changes are necessary, replacing the contents of `src/` shouldn't be a big deal. (Though some people copy the whole spkg folder to a new one omitting "hidden" files, i.e. the Mercurial repository! ;-) )

Yes, I think I've seen this. 

> > Do you want me to create a new .spkg or are you intending to? I note the filename includes `first_reviewer_patch`. Can I expect more reviewer patches? 
> 
> I'm currently preparing a second, _optional_ reviewer patch with stylistic changes to `spkg-install` and `spkg-check` as a suggestion, for "review". I wonder if such would cause further excessive testing, so I consider it optional.

I'm keen to see the back of this ticket. The quicker it gets a positive review, the more chance it is of getting into an early 4.6 alpha. 
 
> I could upload one or two new spkgs soon, too. At your taste.

Let me look at your "optional" patch, but I'm not keen on making unnecessary changes now. 

Dave


---

Comment by leif created at 2010-09-08 16:57:00

P.S.: I also wonder if we should really drop the removal of previous iconv installations. Doing so can potentially cause trouble, while (properly) attempting to remove old traces shouldn't [hurt].

(My comment regarding that only referred to the confusing description in `SPKG.txt`, not to the code or the removal in general.)


---

Comment by drkirkby created at 2010-09-08 17:10:47

I think doing this in practice will be fraught with difficulty. The actual files installed might even depend on platform. (For example, shared libraries on HP-UX are .sl not .so). In general the files might depend on the value of environment variables. I think it's just best to not try to do that. I think it was a bad idea of mine, and one not worth revisiting. 

Dave


---

Comment by leif created at 2010-09-08 17:52:30

Optional SPKG patch. Apply on top of first reviewer patch. (Stylistic change.))


---

Attachment

Replying to [comment:42 drkirkby]:
> I think doing this in practice will be fraught with difficulty. The actual files installed might even depend on platform. (For example, shared libraries on HP-UX are .sl not .so). In general the files might depend on the value of environment variables. I think it's just best to not try to do that.

Well, we have `rm -f` and (not only) filename globbing. In case we later run into problems (e.g. when upstream gets updated), _you_ 're to blame (and you'll have to solve it)... So I won't mind omitting it now. ;-)

> I think it was a bad idea of mine, and one not worth revisiting.

Most spkgs do that.

----

I've attached my second reviewer patch which I would really like to see merged, too. :-)

----

I'll set this to "positive review" if you (and Peter) are ok with my changes (either both or just my first reviewer patch).


---

Comment by drkirkby created at 2010-09-08 19:08:28

The package I reference at 

http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg

has a couple of changes that are not checked in. However, I have a copy with all changes checked in here - I failed to upload it.

When I apply your patches to that, so I get a reject. Can you create a complete package and provide a link. Then I'll check it.

I'll go with your second reviewer patch too, though is there not a mistake on line 21 of `spkg-check` ? 

Dave


---

Comment by leif created at 2010-09-08 21:53:53

Replying to [comment:44 drkirkby]:
> The package I reference at 
> 
> http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg
> 
> has a couple of changes that are not checked in. 

I mentioned that somewhere above. I've committed your changes in your name (these were only those related to #9718 - hopefully).

> When I apply your patches to that, so I get a reject.

Ooops? Don't know why; should not happen... 8|

> Can you create a complete package and provide a link. Then I'll check it.

Yes, I already have it (actually two), just have to upload one of them.

> I'll go with your second reviewer patch too,

Fine, thanks.

> though is there not a mistake on line 21 of `spkg-check` ? 

You mean `;&`? That's "the opposite" of `;;` ("break"), i.e. fall-through.


---

Comment by leif created at 2010-09-08 21:59:16

Replying to [comment:45 leif]:
> Replying to [comment:44 drkirkby]:
> > The package I reference at 
> > 
> > http://boxen.math.washington.edu/home/kirkby/patches/iconv-1.13.1.p3.spkg
> > 
> > has a couple of changes that are not checked in. 
> 
> I mentioned that somewhere above. I've committed your changes in your name (these were only those related to #9718 - hopefully).
> 
> > When I apply your patches to that, so I get a reject.
> 
> Ooops? Don't know why; should not happen... 8|


```
changeset:   11:7ffde08f86a0
tag:         tip
user:        Leif Leonhardy <not.really@online.de>
date:        Wed Sep 08 19:39:14 2010 +0200
files:       SPKG.txt spkg-check spkg-install
description:
#9603: Stylistic change: Use 'case' statements for $UNAME case distinctions.


changeset:   10:e5178b991bd2
user:        Leif Leonhardy <not.really@online.de>
date:        Wed Sep 08 17:58:58 2010 +0200
files:       SPKG.txt spkg-check spkg-install
description:
#9603: Consistently use "$UNAME"; more comments, corrections & cosmetic changes.


changeset:   9:ceb9cde565c1
user:        David Kirkby <david.kirkby@onetel.net>
date:        Wed Sep 08 14:18:58 2010 +0200
files:       SPKG.txt spkg-install
description:
#9718/#9603 Set the compiler flag for building 64-bit binaries in CC not CFLAGS


changeset:   8:db6e4a8c74d8
user:        David Kirkby <david.kirkby@onetel.net>
date:        Thu Aug 26 23:36:08 2010 +0100
files:       SPKG.txt spkg-check spkg-install
description:
#9603 Use $MAKE instead of 'make' to speed up parallel builds.


changeset:   7:c91f30ba571d
user:        David Kirkby <david.kirkby@onetel.net>
date:        Tue Aug 10 20:47:59 2010 +0100
files:       SPKG.txt spkg-check spkg-install
description:
#9603 Address more reviewer comments. Mainly cosmetic, but also fix the fact $SAGE_LOCAL was not quoted.


changeset:   6:745799a814dd
user:        David Kirkby <david.kirkby@onetel.net>
date:        Wed Jul 28 01:35:01 2010 +0100
files:       SPKG.txt spkg-check spkg-install
description:
#9603 Clean up spkg-install and spkg-check in the light of reviewer comments.


changeset:   5:3fe4fc14de91
user:        David Kirkby <david.kirkby@onetel.net>
date:        Tue Jul 27 10:36:47 2010 +0100
files:       spkg-install
description:
#9603 Corrected an informative message about the operating system this is installed on. A trivial change, but it might as well be right.


changeset:   4:31960cb87501
user:        David Kirkby <david.kirkby@onetel.net>
date:        Mon Jul 26 14:36:15 2010 +0100
files:       SPKG.txt spkg-check spkg-install
description:
#9603 Force iconv to build on HP-UX in addition to the previous Solaris and Cygwin.


changeset:   3:32e7f7a36cea
user:        J. H. Palmieri <palmieri@math.washington.edu>
date:        Wed Mar 31 18:35:42 2010 -0700
files:       SPKG.txt spkg-check
description:
spkg-check: only run on Solaris or Cygwin

...
```

(I've committed changeset 9 for you.)


---

Comment by drkirkby created at 2010-09-08 22:01:45

OK, where's the .spkg I can test? 

Dave


---

Comment by drkirkby created at 2010-09-08 22:25:48

Thank you for the link to a .spkg file. I'll test the package and let you know. 

Dave


---

Comment by drkirkby created at 2010-09-08 22:30:24

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-09-08 22:30:24

No, there's a problem if SPKG_CHECK is set to "yes" on `sage.math`. It happens to be on the bit of code I was suspicious of - i.e. line 21 of `spkg-check`


```
iconv will not be installed, as we only need to build it on
Solaris, HP-UX and Cygwin, as the system's iconv will be used
on other platforms, rather than the one shipped with Sage.
See:
    http://trac.sagemath.org/sage_trac/ticket/8567
    http://trac.sagemath.org/sage_trac/ticket/9603

real	0m0.005s
user	0m0.000s
sys	0m0.000s
Successfully installed iconv-1.13.1.p3
Running the test suite.
./spkg-check: line 21: syntax error near unexpected token `;'
./spkg-check: line 21: `    ;&'
*************************************
Error testing package ** iconv-1.13.1.p3 **
*************************************
sage: An error occurred while testing iconv-1.13.1.p3
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/kirkby/sage-4.5.3.rc0/install.log.  Describe your computer, operating system, etc.
```



---

Comment by leif created at 2010-09-08 22:58:10

Replying to [comment:50 drkirkby]:
> No, there's a problem if SPKG_CHECK is set to "yes" on `sage.math`.

Argh... Update to 10.04 LTS! (Again trouble with dead old bashes... :/ )

Ok, I'll upload a patch fixing that.


---

Attachment

SPKG patch. Apply on top of second reviewer patch. (Fixes use of `;&`, which old `bash`es don't understand.)


---

Comment by leif created at 2010-09-08 23:13:09

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-09-08 23:13:09

Replying to [comment:51 leif]:
> Ok, I'll upload a patch fixing that.

Done.


---

Comment by leif created at 2010-09-08 23:22:38

Dave, do you want to apply the patch and upload a new spkg to `sage.math`?

(Or I can replace the one at googlecode, but that's a bit odd since afaik those files are under revision control somehow, and that's not nice for binary / compressed files. It's "only" 3.7 MB though.)


---

Comment by drkirkby created at 2010-09-08 23:27:59

I'd rather you apply the patch and give me a .spkg to test. 

Can you not do it on sage.math, and leave the package there? It will be much faster all around if the package can be on the uni network. 

Dave


---

Comment by leif created at 2010-09-08 23:43:24

Replying to [comment:54 drkirkby]:
> I'd rather you apply the patch and give me a .spkg to test.

I've *deleted* the old one and am currently uploading the new one with all my patches (i.e. including the third) applied. Takes a moment... (I'll update the md5sum in the description then.)

> Can you not do it on sage.math, and leave the package there?

I don't have an account.

> It will be much faster all around if the package can be on the uni network. 

I suspect Google is faster... ;-) (Though using spkg-upload is a bit tedious.)


---

Comment by drkirkby created at 2010-09-09 01:00:12

I'm happy with that. I assume you  are too. 

You may feel it more appropriate to put us both as authors and both as reviewers. That would seem most logical to me. Leave Peter as a reviewer too, since he did make a comment before that the code looked OK, though he was unable to test it. 

Perhaps I can wake up and see "positive review". Luckily I don't have any heart problems - otherwise the shock would probably kill me!

I've checked it on both platforms where it installs (Solaris, HP-UX) and where it does not (Linux). It behaves as expected. 

Dave


---

Comment by leif created at 2010-09-09 05:21:25

Shocked by positive review?


---

Comment by leif created at 2010-09-09 05:21:25

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-09-09 07:34:28

Replying to [comment:58 leif]:
> Shocked by positive review?

Yes, a bit! 

But seriously, I do not think it is appropriate to try to force your style of coding on someone else. I try to write code in a way that will work with virtually any Bourne shell - anyone can take code I write and it will run with almost any shell. As we see here, your stylistic changes resulted in something that would not work with the bash on `sage.math`, as that was too old. 

Anyway, thank you for the work you have done on the ticket. 

Dave


---

Comment by mpatel created at 2010-09-16 00:48:49

Resolution: fixed
