# Issue 9798: Running "make" in SAGE_ROOT returns the wrong exit code, leading to all kinds of confusion

Issue created by migration from https://trac.sagemath.org/ticket/9799

Original creator: was

Original creation time: 2010-08-25 01:01:15

Assignee: GeorgSWeber

CC:  leif jdemeyer drkirkby fbissey

This line in SAGE_ROOT/make

```
cd spkg && ./install all 2>&1 | tee -a ../install.log
```

will *always* return an exit status of 0, even if the build fails miserably.  This leads to much confusion down the line, as explained in this sage-devel post:
    
   
The fix is probably to do what is described here:

 
      http://www.unix.com/shell-programming-scripting/92163-command-does-not-return-exit-status-due-tee.html


---

Comment by mpatel created at 2010-08-25 02:52:33

I think we already have nearly all we need in

`SAGE_ROOT/spkg/pipestatus`

which we use often in 

`SAGE_ROOT/spkg/standard/deps`

For upgrades from Sage versions without `pipestatus`:  What if we create `pipestatus` in the `makefile` instead of in `spkg/install`?

Leif mentioned using `pipestatus` or the equivalent in the `makefile` [comment:ticket:9528:19 here].


---

Comment by jhpalmieri created at 2010-08-25 04:31:03

Well, if we could merge #9433, then I think that pipestatus would get installed through the upgrade process.


---

Comment by jhpalmieri created at 2010-09-13 05:43:30

> For upgrades from Sage versions without pipestatus: What if we create pipestatus in the makefile instead of in spkg/install?

I may be wrong about this, but if you run "sage -upgrade", then I don't think "makefile" gets upgraded.  So if we just modify makefile, we can assume that we have pipestatus available to us: people upgrading won't get the new makefile, and people building from scratch will have spkg/pipestatus.

So I'm attaching a new makefile and corresponding makefile.diff.  I'm far from an expert at writing makefiles, so there are probably cleaner ways to do this.


---

Comment by jhpalmieri created at 2010-09-13 05:43:30

Changing status from new to needs_review.


---

Attachment


---

Comment by leif created at 2010-09-13 09:36:27

Not yet tested, but the changes so far look ok to me.

I'd add dependencies on `spkg/pipestatus`, and perhaps a rule / receipt that makes sure it is (present and) executable. (More of such dependencies could be added as well.)

Perhaps substitute

```sh
        cd spkg && ./pipestatus "./install all 2>&1" "tee -a ../install.log"
```

by

```sh
        spkg/pipestatus "cd spkg && ./install all 2>&1" "tee -a install.log"
```

and, optionally, use a Make variable for `spkg/pipestatus`.

Some changes we should also make:
 * `distclean` should *depend* on `clean`, not *call* `make` (if at all, `$(MAKE)`).
 * The dependency of `all` on `build` is redundant.
 * `s/Deleted/Deleting/g` or move those messages. 
 * `makefile` is not a phony target.
 * `./sage -b` is not consistently performed, and btw. *after* the documentation has been built / updated. Another target and dependency on that would be better.
 * Targets `testoptional` (logfile `testall.log`) and `ptestall` (logfile `ptest.log`!) are inconsistent.


---

Attachment

Revised version of John's Makefile, with many of the other changes I mentioned.


---

Comment by leif created at 2010-09-13 15:06:39

Diff between John's and my Makefile.


---

Attachment

I've attached a modified version of John's Makefile, and a corresponding diff.

Not yet _very much_ tested, but _should_ work... ;-)

Ceterum censeo makefile esse renominandum[?] (i.e. *M*akefile)


---

Comment by leif created at 2010-09-13 16:07:19

Oh, `testall` and `ptestoptional` should also be added to the phony targets.

(I only added `ptest`, which was missing, and removed `makefile`.)


---

Comment by jhpalmieri created at 2010-09-13 18:06:42

I've tested this a little bit, and it basically seems to work for me.  I also have no objections to renaming it `Makefile`.  (If it does get renamed, then #9433 will need to be changed accordingly.)  I'm attaching version 3; this just adds Leif's requested phony targets, plus changes some tabs to spaces.  With the tabs, I see this at the start of the build:

```
(sage-4.5.3) [10:58]$ make
# Note that (currently) "tee" will be run in the directory cd'ed to
# in pipestatus' first argument, i.e. "spkg/": 
spkg/pipestatus "cd spkg && ./install all 2>&1" "tee -a ../install.log"
```

With spaces instead, the lines starting with "#" do not appear.


---

Comment by leif created at 2010-09-13 18:33:05

Replying to [comment:8 jhpalmieri]:
> I've tested this a little bit, and it basically seems to work for me.  I also have no objections to renaming it `Makefile`.

Fine.

> (If it does get renamed, then #9433 will need to be changed accordingly.)

Yes, that's already recorded there.

> I'm attaching version 3; this just adds Leif's requested phony targets,

Thanks.

> plus changes some tabs to spaces.  With the tabs, I see this at the start of the build:

```
(sage-4.5.3) [10:58]$ make
# Note that (currently) "tee" will be run in the directory cd'ed to
# in pipestatus' first argument, i.e. "spkg/": 
spkg/pipestatus "cd spkg && ./install all 2>&1" "tee -a ../install.log"
```


Well, that's (just) informational and does no harm... ;-)

> With spaces instead, the lines starting with "#" do not appear.

I'm currently not that sure that would be very portable; instead, you could also prepend ``@`` (to `#`, and leave the tabs). The comments were actually _shell_ comments (i.e., part of the receipt) rather than Makefile comments.


---

Comment by jhpalmieri created at 2010-09-13 18:50:05

> Well, that's (just) informational and does no harm... ;-

I think it could be a little confusing: it looks like it should be informational, but it won't mean much to some users, and so they might be concerned or worried or puzzled.  If we skip it, then the first printed line looks like something technical which therefore be safely ignored by uninterested people...

I'm attaching new versions with "`@`#".


---

Comment by jhpalmieri created at 2010-09-13 18:52:11

(I'm assuming that "interested" people will start browsing through the Makefile, so will see the comment...)


---

Comment by leif created at 2010-09-13 19:24:37

Replying to [comment:10 jhpalmieri]:
> > Well, that's (just) informational and does no harm... ;-
> 
> I think it could be a little confusing [...]

Agreed.


---

Comment by jhpalmieri created at 2010-09-13 19:41:26

version 3 of the makefile (or Makefile)


---

Attachment

Diff between v2 and v3


---

Comment by jhpalmieri created at 2010-09-13 19:44:04

I changed one more "#" to "`@`#": without the "`@`", `make test` print this possibly confusing message:

```
# . local/bin/sage-env && sage-starts && (also) puts sage-maketest into the path
```

It reads better as a comment, with no evaluation of the variable:

```
     @# $(TESTPRELIMS) (also) puts sage-maketest into the path
```



---

Comment by mpatel created at 2010-09-13 22:38:36

Replying to [comment:4 jhpalmieri]:
> > For upgrades from Sage versions without pipestatus: What if we create pipestatus in the makefile instead of in spkg/install?
> 
> I may be wrong about this, but if you run "sage -upgrade", then I don't think "makefile" gets upgraded.  So if we just modify makefile, we can assume that we have pipestatus available to us: people upgrading won't get the new makefile, and people building from scratch will have spkg/pipestatus.

You're right.  Your idea is simpler and better.

I can't test V3 right now, but here or elsewhere, should we rewrite the `test` target so it works like the other testing targets?

On renaming `makefile`:  Does any platform (Windows?) require the current name?


---

Comment by jdemeyer created at 2010-10-19 08:37:18

What is the status of this ticket?  It looks like there are some good ideas here, let's not waste this effort...  Is this related to #9896 or is it independent of that?


---

Comment by leif created at 2010-10-19 11:13:52

Replying to [comment:16 jdemeyer]:
> What is the status of this ticket?  It looks like there are some good ideas here, let's not waste this effort...  Is this related to #9896 or is it independent of that?

This one is rather unrelated (or even better, afaik _independent_ of #9896).

Feel free to improve the Makefile further, or review what we have so far... ;-) (See some comments above.)

The (or a) "concurrent" ticket to this (and #9896) is _"Put more files under revision control"_, #9433, which I'd like to see merged in 4.6.1.

(Also related: #9811, which is I guess caused by `tee`ing without `pipestatus` as well.)


---

Comment by leif created at 2010-10-19 12:19:40

Something to review... ;-)


---

Comment by jdemeyer created at 2010-10-19 21:10:26

Complete patch from the makefile in sage-4.6.alpha3


---

Comment by jdemeyer created at 2010-10-19 21:11:02

Changing keywords from "" to "makefile".


---

Attachment

I have read the patch and it looks okay to me, but perhaps somebody who is more familiar with the Sage build process should have a second look.  I am currently doing a full build from scratch with the new `Makefile` (with capital).  I have a few comments (which you're free to ignore...).

Why not leave

```
all: build doc 
```

as it is?  I agree that "build" is superfluous, but I think it adds clarity.  It is also more robust in case other parts of the makefile are changed.

the same for

```
doc-html: build # (already) indirectly depends on $(PIPE)
```


About the comments: I think it more common to put them outside the make rules, so instead of

```
build:  $(PIPE)
    @# Note that (currently) "tee" will be run in the directory cd'ed to 
    @# in pipestatus' first argument, i.e. "spkg/":  
    $(PIPE) "cd spkg && ./install all 2>&1" "tee -a ../install.log" 
```

why not write

```
# Note that (currently) "tee" will be run in the directory cd'ed to
# in pipestatus' first argument, i.e. "spkg/":
build:  $(PIPE)
    $(PIPE) "cd spkg && ./install all 2>&1" "tee -a ../install.log" 
```



---

Comment by leif created at 2010-10-19 21:45:22

Replying to [comment:19 jdemeyer]:
> Why not leave

```
all: build doc 
```

> as it is?  I agree that "build" is superfluous, but I think it adds clarity.

A matter of taste, though I think making just `doc` an explicit prerequisite of `all` is more clear here, since it is rather uncommon that the documentation depends on compiling all of the code. (For `spkg/standard/deps`, I prefer at least _some_ redundancy because it's partially obscure what depends on what. Especially omitting true direct dependencies because they're already accomplished through deep indirect dependencies is quite error-prone, since in fact _there_ dependencies are more likely to change than here. Analogous to the new Fedora library dependency scheme.)

> It is also more robust in case other parts of the makefile are changed.

See above; I don't think that's the case here, since the dependencies are rather trivial and clear from the context. ;-) 

> the same for

```
doc-html: build # (already) indirectly depends on $(PIPE)
```


I agree on adding `$(PIPE)`, saves some characters (the comment) anyway. ;-)

> About the comments: I think it more common to put them outside the make rules, so instead of

```
build:  $(PIPE)
    @# Note that (currently) "tee" will be run in the directory cd'ed to 
    @# in pipestatus' first argument, i.e. "spkg/":  
    $(PIPE) "cd spkg && ./install all 2>&1" "tee -a ../install.log" 
```

> why not write

```
# Note that (currently) "tee" will be run in the directory cd'ed to
# in pipestatus' first argument, i.e. "spkg/":
build:  $(PIPE)
    $(PIPE) "cd spkg && ./install all 2>&1" "tee -a ../install.log" 
```


Well, the comment actually refers solely to the single shell command line, not the rule. Just imagine there were more of them...


---

Comment by jdemeyer created at 2010-10-20 15:27:13

Installing with the patched Makefile worked fine, also tried to see what happens if `make`, `make doc` or `make ptest` fails.  This does return an error code as it should.  So positive_review.


---

Comment by jdemeyer created at 2010-10-20 15:27:13

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-10-20 15:50:16

Replying to [comment:23 jdemeyer]:

And the reason for this is that files like *M*akefile and README etc. (should) appear first in directory listings, therefore uppercase.

Btw, I wonder if we should at all let the mixed-up output appear on the screen (i.e., `stdout`) when doing _parallel_ builds. This isn't _that_ easy to handle, because the "decision" to actually perform a parallel build is currently (IMHO unnecessarily) made in `spkg/install`. If we want to change that (I'd prefer having just _"Building package xy..."_, _"Successfully installed package xy"_ / _"Error installing package xy"_ on the screen and in the main log, `$SAGE_ROOT/install.log`), this should of course be addressed on another ticket.

It's currently hard to see which package actually failed to install after getting _"Error building Sage."_; grepping for "Error" gives a lot of harmless lines.


---

Comment by leif created at 2010-10-20 15:59:27

Replying to [comment:24 leif]:
> It's currently hard to see which package actually failed to install after getting _"Error building Sage."_; grepping for "Error" gives a lot of harmless lines.

We could at least (on errors) print a summary at the end, analogous to doctesting (_"The following packages failed to build/install: ..."_). This would currently be a bit easier to implement (by keeping track of which packages are to be built, and at the end checking if they were successfully built).


---

Comment by mpatel created at 2010-10-20 23:12:16

Replying to [comment:24 leif]:
> Btw, I wonder if we should at all let the mixed-up output appear on the screen (i.e., `stdout`) when doing _parallel_ builds. This isn't _that_ easy to handle, because the "decision" to actually perform a parallel build is currently (IMHO unnecessarily) made in `spkg/install`. If we want to change that (I'd prefer having just _"Building package xy..."_, _"Successfully installed package xy"_ / _"Error installing package xy"_ on the screen and in the main log, `$SAGE_ROOT/install.log`), this should of course be addressed on another ticket.

Would using, e.g.,

```
        @echo '  ACTION  ' $@; command that does the action
```

in `Makefile` and `deps` and replacing "pipestatus/tee" with ">>" in `deps` help?  Is there any way to keep recording a big, multiplexed log in the background, if we still want it?


---

Comment by leif created at 2010-10-21 00:50:05

Replying to [comment:26 mpatel]:
> Replying to [comment:24 leif]:
> > Btw, I wonder if we should at all let the mixed-up output appear on the screen (i.e., `stdout`) when doing _parallel_ builds. This isn't _that_ easy to handle, because the "decision" to actually perform a parallel build is currently (IMHO unnecessarily) made in `spkg/install`. If we want to change that (I'd prefer having just _"Building package xy..."_, _"Successfully installed package xy"_ / _"Error installing package xy"_ on the screen and in the main log, `$SAGE_ROOT/install.log`), this should of course be addressed on another ticket.
> 
> Would using, e.g.,

```
        @echo '  ACTION  ' $@; command that does the action
```

> in `Makefile` and `deps` and replacing "pipestatus/tee" with ">>" in `deps` help?  Is there any way to keep recording a big, multiplexed log in the background, if we still want it?

I was thinking of _conditionally_ `tee`ing (at least) in the top-level Makefile (just _redirecting_ stdout on parallel builds) and checking the exit status inside the receipts to print appropriate messages to some other file descriptor than stdout in `deps`.

Verbosity levels for `sage-spkg` wouldn't be bad either, especially suppressing the verbose `tar` output is IMHO worth doing, since a lot of spkgs contain hundreds or thousands of files (while the actual build log is often only a few lines).

But I must admit I've already forgotten what exactly I'd planned yesterday... ;-)


---

Comment by drkirkby created at 2010-10-21 15:47:04

Replying to [comment:27 leif]:
 
> Verbosity levels for `sage-spkg` wouldn't be bad either, especially suppressing the verbose `tar` output is IMHO worth doing, since a lot of spkgs contain hundreds or thousands of files (while the actual build log is often only a few lines).

I think removing the 'v' option from tar output would be sensible. It would make the log files smaller & reduce disk I/O. It would also make finding things like "warnings" easier, as you could grep the log looking for warnings, and not find every file which has the name "warning" in it. 

In the absence of anyone writing a patch to control verbosity, just removing the 'v' would be a useful addition I think. The default action should not be to produce tons of unnecessary output. 

Dave


---

Comment by leif created at 2010-10-21 16:25:27

Replying to [comment:28 drkirkby]:
> In the absence of anyone writing a patch to control verbosity, just removing the 'v' would be a useful addition I think. The default action should not be to produce tons of unnecessary output. 

I can provide a patch for that. :) (Though there are currently a couple? of other tickets modifying `sage-spkg`.)

We can still fall back to the old behavoir if yet another undocumented environment variable (e.g. `SAGE_SPKG_VERBOSE` or `SAGE_SPKG_LIST_FILES`) is set, to not annoy people who heat their home with harddisks, or need more network traffic etc.

The advantage of verbose extraction is that you by chance see a lot of useless files that could or should be removed from an spkg. Take e.g. a look at the files in SageNB's Mercurial repository, currently also listed in `spkg/logs/sagenb-*` (it's about 22500 lines)... ;-)


---

Comment by mpatel created at 2010-10-21 20:55:38

I recently opened #10040 for not using `tar`'s `v` option (by default) when extracting packages.


---

Comment by jdemeyer created at 2010-11-01 10:04:35

Resolution: fixed


---

Comment by leif created at 2010-11-01 13:28:54

One more argument: ;-)

```sh
Successfully installed gnutls-2.2.1.p5
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
python: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)
Making script relocatable
Finished installing gnutls-2.2.1.p5.spkg
make[1]: Leaving directory `/home/leif/Sage/sage-4.6/spkg'

real	3m36.199s
user	10m5.250s
sys	2m8.140s
Error building Sage.
./sage -docbuild all html  2>&1 | tee -a dochtml.log
python: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)
python: can't open file '/home/leif/Sage/sage-4.6/devel/sage/doc/common/builder.py': [Errno 2] No such file or directory
. local/bin/sage-env && sage-starts && ./sage -tp 8 -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log
python: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)
Testing that Sage starts...
python: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)
python: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)
python: /home/leif/Sage/sage-4.6/local/lib/libz.so.1: no version information available (required by python)
Traceback (most recent call last):
  File "/home/leif/Sage/sage-4.6/local/bin/sage-eval", line 4, in <module>
    from sage.all import *
ImportError: No module named sage.all
Sage failed to startup.
make: *** [ptestlong] Error 1
```

