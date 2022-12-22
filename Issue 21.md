# Issue 21: command line option parsing

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 23:21:18

Assignee: somebody

CC:  kini saraedum iandrus

`sage -br -notebook` doesn't start the notebook but it should


---

Comment by was created at 2007-01-13 01:56:18

no -- you can't combine command line options like that.  this isn't a bug
but a not implemented yet issue.


---

Comment by was created at 2007-01-13 01:56:18

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2007-09-11 02:11:39

This should be fixable, but the long term goal is to do a proper rewrite of the command line options.

Cheers,

Michael


---

Comment by gfurnish created at 2008-03-16 07:59:18

Changing assignee from somebody to gfurnish.


---

Comment by gfurnish created at 2008-03-16 07:59:18

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-04-04 19:55:55

Changing component from basic arithmetic to interfaces.


---

Comment by mabshoff created at 2008-09-24 02:59:36

See also #180 for a bunch of related failures due to the option parsing being dumb :o

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-24 02:59:36

Changing status from assigned to new.


---

Comment by mabshoff created at 2008-09-24 02:59:36

Changing assignee from gfurnish to mabshoff.


---

Comment by mabshoff created at 2008-09-24 02:59:46

Changing status from new to assigned.


---

Comment by kcrisman created at 2009-12-30 05:15:23

Note that sage -bn now builds, then does notebook, though of course it doesn't fix the issue here.


---

Comment by jhpalmieri created at 2010-03-19 15:41:48

the file SAGE_ROOT/makefile


---

Attachment


---

Attachment

extcode repo


---

Attachment

sagenb repo


---

Attachment

Here are patches.  After applying "trac_21-scripts.patch", you may need to make "SAGE_ROOT/local/bin/sage-sage.py" executable.  The build process works for me with these patches.  For the standard packages, the third line in

```
if [ "$SAGE_LOCAL" = "" ]; then
   echo "SAGE_LOCAL undefined ... exiting";
   echo "Maybe run 'sage -sh'?"
   exit 1
fi
```

should be changed to "Maybe run 'sage --sh'?", but this doesn't affect the functioning of the packages, and otherwise, they don't need changing.  I haven't looked at optional packages.

This approaches uses Python's optparse to parse command-line options.  If someone wants to write a version using [shflags](http://code.google.com/p/shflags/) or some other package, go ahead.

I propose the following approach, whether using these patches or other ones:

 - first, we include new command-line options but don't turn them on  by default, instead printing a message like this one when you type "sage [...]" with a nonempty argument: 

```
    Note: Using old-style Sage command-line options. 

    To try out Sage's experimental GNU/Posix-style command-line options 
    (for example, 'sage --notebook' instead of 'sage -notebook'), set the 
    environment variable $SAGE_NEW_OPTIONS to something nonempty. 
    To bypass this message, set the environment variable 
    $SAGE_SKIP_OPTIONS_MESSAGE to something nonempty. 
```

 Running "sage" (with no arguments) would not trigger this message.  (Perhaps we could only turn this on in prerelease (alpha and rc) versions?  Alternatively, a change like this could go with the version 5.0 release.) 

 - after a while, we switch this to 

```
    Warning: Using old-style Sage command-line options. 

    Sage is changing to use conventional GNU/Posix-style command-line options 
    (for example, 'sage --notebook instead of 'sage -notebook).  This change will 
    become the default soon.  Meanwhile, to use this new style (and therefore 
    to avoid seeing this message), set the environment variable 
    $SAGE_NEW_OPTIONS to something nonempty. 
```

 perhaps with no easy way of disabling this message while using old-style options. 

 - finally, we turn on the new options, perhaps with an environment variable $SAGE_OLD_OPTIONS to use the old ones, with the understanding that any changes in command-line options may not be maintained for the old version. 

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/de30143ec073f31?tvc=2) for some discussion.


---

Comment by jhpalmieri created at 2010-03-19 15:50:37

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-03-19 15:50:47

Changing priority from minor to critical.


---

Comment by jhpalmieri created at 2010-03-19 20:25:24

I've marked this as "needs review", but it might need work.  In the previously cited thread from sage-devel, there was the following suggestion:

```
Another possibility might be to first check for "--gp", "--gap", etc., 
and do those before doing the general option parsing.   I.e., just do 
what you already planned, but with one optimization to deal with this 
use case. 
```

This is to speed up access to these programs: do a check like this in a shell script, and then pass the rest of the arguments to Python's optparse using the script included in this patch, or one like it.  Then you avoid the slight delay involved in starting up Python if you want to run "gp".  It would be nice to have a shell script which had a list of strings "gp", "gap", etc., checked to see if the first(?) argument was "--STR" for STR in this list, and if so, run the appropriate program from SAGE_LOCAL/lib, passing the rest of the line as arguments.  Having one list containing all of these strings would make it easy to customize.


---

Attachment

the file SAGE_ROOT/sage


---

Attachment

Replying to [comment:10 jhpalmieri]:
> I've marked this as "needs review", but it might need work.  In the previously cited thread from sage-devel, there was the following suggestion:

```
Another possibility might be to first check for "--gp", "--gap", etc., 
and do those before doing the general option parsing.   I.e., just do 
what you already planned, but with one optimization to deal with this 
use case. 
```


Okay, here's a new version which does this: it adds a file sage-sage-quickstart which gets run first, implementing the above idea.  Then if SAGE_NEW_OPTIONS is nonempty, it calls sage-sage.py, the Python/optparse version with GNU/Posix standard command-line options.  Otherwise, it calls the old parser sage-sage.

For the record, the commands in sage-sage-quickstart are: axiom, ecl/lisp, gap, gp, hg, ipython, maxima, mwrank, python, R, singular.  Are any others particularly sensitive to startup times?  (Using python adds something less than .1 second on my two-year old iMac, so we're not talking about a lot of time, in any case.)


---

Comment by jhpalmieri created at 2010-05-07 19:06:03

Note that Python 2.7 will include the [argparse](http://docs.python.org/dev/library/argparse.html) module, which might be easier to use than optparse.


---

Comment by was created at 2010-06-03 04:33:02

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-06-03 04:33:02

Wow, this is really fantastic.


---

Comment by was created at 2010-06-03 04:36:19

Changing status from positive_review to needs_work.


---

Comment by was created at 2010-06-03 04:37:18

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-06-03 04:37:18

I'm changing this back to needs review.  I realized when trying to apply it that I had got confused about how to even apply this.

John, can you please post clear directions about how to use the patches attached to this ticket?


```

sage: hg_scripts.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/21/trac_21-scripts.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/21/trac_21-scripts.patch
Loading: [..........]
cd "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/bin" && hg status
cd "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/bin" && hg status
cd "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/bin" && hg import   "/scratch/wstein/sage/temp/sage.math.washington.edu/22653/tmp_0.patch"
applying /scratch/wstein/sage/temp/sage.math.washington.edu/22653/tmp_0.patch
patching file sage-pkg
Hunk #1 FAILED at 40
Hunk #2 FAILED at 63
2 out of 2 hunks FAILED -- saving rejects to file sage-pkg.rej
patching file sage-run
Hunk #1 FAILED at 17
1 out of 1 hunks FAILED -- saving rejects to file sage-run.rej
patching file sage-sage
Hunk #2 FAILED at 34
Hunk #3 FAILED at 196
Hunk #4 FAILED at 212
Hunk #5 FAILED at 424
Hunk #6 FAILED at 450
Hunk #8 FAILED at 608
Hunk #9 FAILED at 744
Hunk #10 FAILED at 767
Hunk #11 succeeded at 894 with fuzz 1 (offset 0 lines).
8 out of 11 hunks FAILED -- saving rejects to file sage-sage.rej
abort: patch failed to apply
```



---

Comment by jhpalmieri created at 2010-06-03 06:02:38

scripts repo


---

Attachment

sage repo


---

Attachment

> John, can you please post clear directions about how to use the patches attached to this ticket?

Sorry, some parts needed rebasing.  I think it's okay now.  I've modified the summary with instructions for how to apply the patches.


---

Comment by ohanar created at 2010-11-11 19:54:30

It appears like sage-sage.py managed to get itself into 4.4.3 (William, could this have happened when you were trying to apply it). Also, sage-apply-ticket has greatly changed since the patches were posted, so I am changing this back to needs work.


---

Comment by ohanar created at 2010-11-11 19:54:30

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-11-11 20:08:59

As far as I know, the file sage-sage.py was accidentally added in 4.4.3, but the release manager should probably delete it: it's not used anywhere.

I don't have the time to rebase it right now, so if anyone else wants to work it, that would be great.


---

Attachment

scripts repo, rebased on 4.6.1.alpha1


---

Comment by ohanar created at 2010-11-12 11:01:28

I've uploaded a patch rebased on 4.6.1.alpha1 (I also added in #8654 while I was at it). One thing I noted during rebasing it is that -tp no longer works (and hence -btp which was added since 4.4.3), I don't know optparse well enough to come up with a solution (if we want to provide one). The documentation patches will need to be rebased as well.

For anyone who wants to apply this, make sure to remove sage-sage.py before applying, the file is currently just hanging around not doing anything - mercurial doesn't even know about it.


---

Comment by kini created at 2011-11-01 14:49:12

ohanar mentioned on #8654 that this should be rewritten (or modified) to use argparse as optparse is deprecated in Python 2.7, so I'm adding #9958 to the dependencies because argparse is shipped with 2.7. Alternatively we could make an spkg for argparse.


---

Comment by jhpalmieri created at 2011-11-02 01:27:23

I think waiting until 2.7 is fine.


---

Comment by kini created at 2011-11-13 10:39:14

Can we edit the title and description of this ticket to reflect what we're actually trying to do here? (I would, but preferably someone who has been working on it should do it.) The goal is to completely replace the command line handler (currently a shell script) with a Python script which uses argparse for extensibility, right?


---

Comment by kini created at 2012-01-19 12:14:37

People CC'd to this ticket probably already know this, but the above mentioned #9958 is merged, so we can use Python 2.7 default modules such as argparse now.


---

Comment by ohanar created at 2012-01-24 17:20:32

Replying to [comment:26 kini]:
> People CC'd to this ticket probably already know this, but the above mentioned #9958 is merged, so we can use Python 2.7 default modules such as argparse now.

Yup, I've started working on this, but its going to take awhile... :)


---

Comment by kini created at 2012-01-24 17:34:26

Capital! :) As it's a large project maybe you could post WIPs once in a while?

I was planning on diving into the scripts dir myself and trying to work on this, but I guess it should be an order of magnitude easier for you, haha. Still, let me know if I can help with anything.


---

Comment by ohanar created at 2012-01-26 10:15:07

Replying to [comment:28 kini]:
> Capital! :) As it's a large project maybe you could post WIPs once in a while?

No problem, once I have something of any real substance, I'll be sure to post it somewhere.

> I was planning on diving into the scripts dir myself and trying to work on this, but I guess it should be an order of magnitude easier for you, haha. Still, let me know if I can help with anything.

Well, I'm just starting and have had a busy week with other stuff, so you would probably be in about as good of position as myself, especially since we need to rebase this off of the 5.0 dev builds, which changed a lot of that stuff anyway.

I'm finding myself annoyed at spkg/script, and all the little special cases that we have. I really just want to rip that out and try to have a (more) unified design to our parsing. My current fancy is to introduce a bunch of subcommands, like mercurial or aptitude. Some of the ones I've thought about:

```
% sage ARGS # this would be for running sage scripts, or a couple of oddball arguments
% sage notebook ARGS
% sage pkg ARGS # this would include spkg stuff
% sage pkg install # since install has some special flags like -f or -s
% sage test ARGS
% sage build ARGS
% sage {python,sqlite3,R,gp,...} ARGS # we can consider these programs as subcommands of sage
```

I haven't fully worked out what this would look like with all the arguments (such as debugging), but IMO it would greatly clean up our command line tools. Also, this would simplify many aspects of the implementation, although some hacking of argparse will still have to be done (it currently doesn't support optional subparsers, see [http://bugs.python.org/issue9253](http://bugs.python.org/issue9253)).

I probably should bring this up on the devel list, but I'm tired and should go to bed before I have to be up in the morning :/.


---

Comment by kini created at 2012-05-25 20:16:23

We're going to try to get this in as a Sage 6.0 goal along with #13015.


---

Comment by kini created at 2012-05-25 23:06:21

patchbot: apply 21-scripts-4.6.1.alpha1.patch

(this doesn't actually work but at least this way the patchbot won't try to apply the other stuff, and even crash, apparently)


---

Comment by jdemeyer created at 2013-01-24 13:30:48

Going with `argparse` is probably a good idea, but I would still like a special "pre-parser" in `bash` to handle to options

```
sage --sh
sage -i
sage -f
```

(or whatever version they will become)

I think these must be available from the start, before Python has been built.


---

Comment by jdemeyer created at 2013-01-24 13:30:48

Changing assignee from mabshoff to jdemeyer.


---

Comment by kini created at 2013-01-24 17:39:13

ohanar and I talked about this a bit at SD40.5. What do you think about having a totally separate executable (rather than a preparser) called `sage-sh`? Stuff like the current `sage -gap` could be called rapidly with `sage-sh -c gap`, or slowly via python with `sage gap` or what-have-you.


---

Comment by jhpalmieri created at 2013-01-24 18:33:18

William, among others, as alluded to [comment:11 above], was pretty insistent that commands like `sage --gp` execute quickly, without the overhead that starting Python entails. Hence the approach in my patches on this ticket. If you want to insist that people use `sage-sh -c gp` instead, I don't think it can get a positive review unless the approach gets a positive response on sage-devel.


---

Comment by kini created at 2013-01-24 18:44:15

Rather than building on your patches on this ticket, we're proposing completely rewriting the command line interface of Sage, and that includes changing invocation methods. That's why we've set the milestone to sage-6.0 - the idea is to tie it with the layout restructuring and new development interface that will come with the git transition (#13015). We figured that the git transition is a big enough change to warrant a major version bump (though that might end up being sage-7.0 or whatever, depending on the timeline).

So, of course, this will all go through sage-devel in time, once we figure out exactly what we're proposing.


---

Comment by jhpalmieri created at 2013-01-24 18:57:09

Oh, I understood that you were starting from scratch. I was responding to your proposal about `sage-sh`, suggesting that not all users would be happy with that solution.


---

Comment by jdemeyer created at 2013-01-24 19:09:34

If you need a separate `bash` script anyway to parse some options like `--sh`, then it's a trivial exercise to parse more options (like `--gp`) in that same script.


---

Comment by kini created at 2013-01-24 19:27:35

jdemeyer: I think you misunderstand. Currently, `sage` is a bash script, which checks some options, then starts up Python to handle the rest (separately in various different code branches, no less). What we're proposing is the following scenario:

`sage` is a Python script. `sage-sh` is a bash script. `sage-sh` does not parse any arguments - it just sources sage-env, does whatever other setup required, and dumps you in a shell. Any arguments to `sage-sh` are just passed to that shell. As such, `-c` would allow you to specify a command to execute in the Sage shell, such as `gap` or `gp`. `sage-sh` does not load Python unless you happen to give it `-c python` as an argument. 

`sage` is directly run by Python because it is a python script. `sage --sh` (or probably `sage sh` because of ohanar's subcommands idea) will cause Python to start up, parse the arguments, and then exec the bash script `sage-sh` (i.e. be very slow).

The argument would be that if you need something to happen fast and want to avoid starting up Python, or are the release manager and are doing things with Sage in a state where Python doesn't exist, you're probably writing scripts anyway and can afford to write out `sage-sh -c sage-pkg` (or whatever the package manager command ends up being) inside your script, or make an alias in your shell. If you're a normal user just typing on the command line, you won't care that Python had to start up just to parse your command line arguments.

The benefit of doing this is that the entire normal startup chain of Sage can be made pure Python, which is easier to maintain and might be more portable (?).


---

Comment by jdemeyer created at 2013-01-24 20:08:44

Doesn't this contradict?

Replying to [comment:35 jhpalmieri]:
> William, among others, as alluded to [comment:11 above], was pretty insistent that commands like `sage --gp` execute quickly, without the overhead that starting Python entails.

Replying to [comment:39 kini]:
> `sage` is a Python script.


---

Comment by kini created at 2013-01-24 20:13:02

1) That comment is 3 years old and I imagine it's up for discussion by now.

2) Replace `sage --gp` with `sage-sh -c gp` and all is well. I doubt William, among others, is talking about the exact command `sage --gp`; as long as there is a good way to start up Sage's gp quickly without loading Python, we should be fine (?).


---

Comment by jdemeyer created at 2013-01-24 20:29:27

OK I see.  So we would have two "top-level" scripts then:
`./sage` (Python-based) and `./sage-sh` (`bash`-based).  Yes, that would be fine for me.

But what about `sage-env` then?  That's needed by `sage-sh`, so it cannot be Python-based.


---

Comment by ohanar created at 2013-01-24 21:50:00

Replying to [comment:42 jdemeyer]:
> But what about `sage-env` then?  That's needed by `sage-sh`, so it cannot be Python-based.
Definitely short term I don't think it is realistic to make the entire startup entirely python because we don't have any python module to setup a suitable environment, however I think it would be good to still make separate out sage-sh:

Specifically I would have the root level sage script be (more or less)


```/usr/bin/env sh

"$0-sh" -c "sage $*"
```


and have `SAGE_LOCAL/bin/sage` be a pure python script.


---

Comment by jdemeyer created at 2013-01-24 22:02:54

Given that part of the startup needs to be `bash` anyway (I actually think `bash` is a good language to implement `sage-env`), perhaps the two-pass argument parsing (as proposed in the comments of 3 years ago) would be best.  Have a small `sage` script written in `bash` which processes just a few options and when options aren't recognized, run all the Python `argparse` machinery.  What could be the problem with that?


---

Comment by kini created at 2013-01-24 22:25:56

Replying to [comment:42 jdemeyer]:
> But what about `sage-env` then?  That's needed by `sage-sh`, so it cannot be Python-based.

Right, we might have a very thin bash wrapper that loads `sage-env` (which will be a bash script) before the main Python script. Or, since `sage-env` ideally should just set up environment variables and do nothing else (right?), we could turn it into a config file that was read independently by `sage-sh` and by `sage`. This would also allow us to rely less on environment variables for random things seemingly unrelated to the shell.

The problem with having two-pass argument parsing is that it separates the processing of arguments into multiple areas, making the architecture of the startup process needlessly complex. It is also pretty ugly to actually do this in the standard option parsing way because either you start to want to enforce arbitrary argument orders like we currently do (`sage -tp` works and `sage -pt` doesn't, `sage -br` works and `sage -rb` doesn't, etc.), or now the bash script needs to basically reimplement optparse/argparse in bash in order to correctly read the flags it's looking for.

In any case, if I as a new Sage developer want to know or modify what option `--foo` does, there should be one obvious place to look for it. Making `sage-sh` parse arguments also means that we are shadowing arguments that could be passed on to the shell, etc. etc. Splitting argument parsing into two places is just generally a nasty design IMHO.

Why does part of the startup need to be bash, other than because of `sage-env`?


---

Comment by ohanar created at 2013-01-25 02:33:20

Replying to [comment:45 kini]:
> Right, we might have a very thin bash wrapper that loads `sage-env` (which will be a bash script) before the main Python script. Or, since `sage-env` ideally should just set up environment variables and do nothing else (right?), we could turn it into a config file that was read independently by `sage-sh` and by `sage`. This would also allow us to rely less on environment variables for random things seemingly unrelated to the shell.

Are you saying that a configuration file should store the current environment? And that anytime it is changed (such as if the root directory of sage is moved) that this should be updated?
> 
> The problem with having two-pass argument parsing is that it separates the processing of arguments into multiple areas, making the architecture of the startup process needlessly complex. It is also pretty ugly to actually do this in the standard option parsing way because either you start to want to enforce arbitrary argument orders like we currently do (`sage -tp` works and `sage -pt` doesn't, `sage -br` works and `sage -rb` doesn't, etc.), or now the bash script needs to basically reimplement optparse/argparse in bash in order to correctly read the flags it's looking for.

Also
 * argparse/optparse handles help functionality (consistent formatting), so all pre-parsed commands would still need stubs in argparse/optparse (and -1 for code duplication)
 * argparse (and maybe optparse) matches subcommands so long as they are not ambiguous. So if (for instance) sage only had the subcommands foo and bar then `sage f [args]` would be expanded to `sage foo [args]`. (this is fairly standard for software with subcommands) This functionality would be inconsistent if there were any pre-parsed commands.
> In any case, if I as a new Sage developer want to know or modify what option `--foo` does, there should be one obvious place to look for it. Making `sage-sh` parse arguments also means that we are shadowing arguments that could be passed on to the shell, etc. etc. Splitting argument parsing into two places is just generally a nasty design IMHO.
+1

> Why does part of the startup need to be bash, other than because of `sage-env`?

For one of two reasons:

 * python may not be in `PATH` because python is not currently a dependency
 * even if python is in `PATH`, sage may not work with the default python


---

Comment by kini created at 2013-01-25 07:10:02

Replying to [comment:46 ohanar]:
> Replying to [comment:45 kini]:
> > Right, we might have a very thin bash wrapper that loads `sage-env` (which will be a bash script) before the main Python script. Or, since `sage-env` ideally should just set up environment variables and do nothing else (right?), we could turn it into a config file that was read independently by `sage-sh` and by `sage`. This would also allow us to rely less on environment variables for random things seemingly unrelated to the shell.
> 
> Are you saying that a configuration file should store the current environment? And that anytime it is changed (such as if the root directory of sage is moved) that this should be updated?

It should store the current startup environment. It would change if the root directory of Sage is moved, for example, yes. But if a user decided to change an environment variable in a Sage session with `os.environ` that wouldn't become reflected in the file, of course.

> > Why does part of the startup need to be bash, other than because of `sage-env`?
> 
> For one of two reasons:
> 
>  * python may not be in `PATH` because python is not currently a dependency
>  * even if python is in `PATH`, sage may not work with the default python

Oh, right, of course. So then yes, `sage` should be bootstrapped in the way you described [comment:43 above].


---

Comment by jdemeyer created at 2013-01-25 07:35:11

Replying to [comment:45 kini]:
> Or, since `sage-env` ideally should just set up environment variables and do nothing else
Well, some of these environment variables are conditional, so it's not that easy to have a file which works both from bash and from Python.  And I certainly don't see it as a problem that `sage-env` remains in `bash` as it is now.

> The problem with having two-pass argument parsing is that it separates the processing of arguments into multiple areas, making the architecture of the startup process needlessly complex. It is also pretty ugly to actually do this in the standard option parsing way because either you start to want to enforce arbitrary argument orders like we currently do (`sage -tp` works and `sage -pt` doesn't, `sage -br` works and `sage -rb` doesn't, etc.), or now the bash script needs to basically reimplement optparse/argparse in bash in order to correctly read the flags it's looking for.
All these arguments are essentially irrelevant if the first pass needs to support just very few options.  Things like `./sage -tp` or `./sage -pt` would be handled anyway by the `argparse` script.

Of course it's bad design to have two-pass argument parsing, but it would be so nice to keep `./sage -i` and `./sage --sh` working.

> Why does part of the startup need to be bash, other than because of `sage-env`?
I think `sage-env` is the main reason.


---

Comment by kcrisman created at 2014-11-20 13:33:25

The command line interface continues to evolve; can someone (who cares) give a summary of what still would be needed?  comment:24 still hasn't been resolved, and comment:33 (as well as quick, non-Python-starting, use of `sage -maxima` and friends) seems quite relevant.


---

Comment by jdemeyer created at 2015-06-23 13:45:35

Changing component from interfaces to user interface.


---

Comment by embray created at 2017-06-01 14:55:00

Still reading up on this ticket, and don't have any comments to add yet to the existing discussion.  But one question I have in general: Is anyone opposed at all to the idea of creating a new sub-command based interface, more like git, than the slightly unusual interface that uses single-character flags for subcommands?  E.g. replace `sage -t` with `sage test`.  Yes, it's more to type, but only by two characters, and is much less unusual.  The old `-t` could still be supported very easily for backwards compatibility, but perhaps with a deprecation warning.


---

Comment by jhpalmieri created at 2017-06-01 17:32:59

William Stein and I were just talking about this idea yesterday. Something like this?

```
sage FILE.[sage|py|spyx]

sage help
sage help --advanced?

sage -c <CMD>

sage package config
sage package name <TARBALL>
sage package list
sage package list standard
sage package list optional
sage package list experimental
sage package apropos
sage package download
sage package update
sage package fix-checksum
sage package create

sage install <PKGS>
  options: [-f, --force] [-c, --check] [-d, --download] [-s, --save]
   [-y, --yes] [-n, --no] [--no-dependency] [-i, --info]

sage pip

sage gap
sage gap3
sage gp
sage maxima
sage python
sage python3
sage ipython
sage ipython3 (not yet implemented)
sage R
sage singular
sage git
sage cython
sage cleaner
sage ecl
sage gdb
sage kash
sage lisp
sage M2
sage mwrank
sage polymake
sage scons
sage sqlite3
sage twistd

sage shell

sage notebook=[default|ssagenb|jupyter|export|jupyterlab|ipython]
  options: --log=...

sage notebook rst2ipynb ...
sage notebook rst2txt ...
sage notebook rst2sws ...
sage notebook sws2rst ...

sage test FILES
sage test --all
  options: --long, --verbose, --optional, --sagenb, --help,
  [-p|--parallel], --randorder[=seed], --new, --initial, --debug,
  --failed, --warn-long [timeout]

sage preparse <FILE>
sage startuptime
sage coverage [-a, --all]
sage search? search_src? search_doc? grep? grep_doc?

sage sdist
sage valgrind [--cacherind] [--callgrind] [--massif] [--memcheck] [--omega]

sage docbuild
  options: (run sage --docbuild --help to see)

sage --nodotsage
sage --root
sage -q
sage --min
sage [-v, --version]
sage dumpversion?

sage fixdoctests ...

sage build
sage build --force
sage build test?  (currently sage -bt ...)
sage build run?  (currently sage -br)
```

Maybe some of these can be removed. Maybe some can be consolidated: do we need separate commands for gap, gp, maxima, ecl, R, etc., or can they be combined under a single command, like "sage run <PROGRAM>"? There is endless bikeshedding available.


---

Comment by embray created at 2017-06-02 08:22:20

Yes, something quite like that.

And I was thinking of writing up some kind of declarative list(s) of subcommands.  In particular I was thinking two separate lists:

1. One list of sage-specific sub-commands (such as `sage package` in your example above), which would automatically be translated to running individual scripts that implement them that would be named `sage-<subcommand>`. This is mostly how `git` works as well.

2. One list of programs installed in the Sage distribution (`sage sh`, `sage gap`, etc.) that can be launched from the interface.  In principle one could make this automatic but I think it's better to have a hard-coded list.  I don't think a `sage run` is really necessary.  `sage sh <whatever>` is essentially the same as this, but I think it's still convenient to have shortcuts for common programs included in the Sage distribution.

Although somewhat redundant, because it's common I would also have `sage --help` as an alias for `sage help` and `sage --help-advanced` for `sage help --advanced`, though one could bikeshed about whether those should do the exact same thing or not.

I might also hide more of the development-specific commands (`sage coverage`, `sage startuptime`, etc.) behind a sub-command.


---

Comment by embray created at 2017-06-02 08:23:08

(I should add, that's a very nice mock-up of what such an interface would look like, so thank you for that.)


---

Comment by jdemeyer created at 2017-06-02 13:01:28

Replying to [comment:55 embray]:
> E.g. replace `sage -t` with `sage test`.

What about `sage -btp`? I use that all the time. I would hate it if that would become
`sage buildtest -p` or worse, `make build && sage test -p`.


---

Comment by jdemeyer created at 2017-06-02 13:12:10

We should also think to what extent the build system should be exposed under the `sage` command. For example, we now have

```
make FOO         # Build dependencies of FOO + FOO
sage -i FOO      # Build toolchain + dependencies of FOO + FOO
sage -f FOO      # Build toolchain + dependencies of FOO + *rebuild* FOO
sage -p FOO      # Build FOO *without* dependencies
```

and

```
make sagelib     # Build Sage library with dependencies
sage -i sagelib  # Build Sage library with toolchain and dependencies
sage -b          # Build Sage library *without* dependencies
sage -f sagelib  # Rebuild all of the Sage library with toolchain and dependencies
sage -ba         # Rebuild all of the Sage library *without* dependencies
```


This is all for historical and accidental reasons, but this ticket should clean that up too.


---

Comment by jdemeyer created at 2017-06-02 13:13:22

Needless to say, many people don't even know the subtle differences between the above commands.


---

Comment by embray created at 2017-06-06 09:42:41

Replying to [comment:59 jdemeyer]:
> Replying to [comment:55 embray]:
> > E.g. replace `sage -t` with `sage test`.
> 
> What about `sage -btp`? I use that all the time. I would hate it if that would become
> `sage buildtest -p` or worse, `make build && sage test -p`.

I was actually thinking of allowing subcommands to be chained, like in `setup.py`.  So `sage build test`, where each can take optional flags if desired.


---

Comment by mkoeppe created at 2020-08-11 19:29:26

Strong -1 "wontfix" for the idea of making an incompatible change toward using "subcommands" after 14 years of the existence of the `sage` script.


---

Comment by embray created at 2020-08-31 15:42:10

I think the current interface of the `sage` script is pretty clumsy and dated by modern standards.  It can and should be made more user-friendly.  Just as one example of an advantage of subcommands is it makes the help documentation vastly more digestible.  I wouldn't propose changing it without maintaining backwards compatibility though.


---

Comment by was created at 2020-08-31 17:58:19

+1 from me to changing the sage script to support subcommands, especially if we can somehow do it in a way that preserves compatibility with the current parsing.  I wonder to what extent the following is possible:

 - 1. run the current shell script and if it "works" then done (with maybe some slight tightening)
 - 2. parse using subcommands.

Or something else, e.g,. if you do "sage [explicit list of subcommands]" uses the subcommand approach; otherwise, fall back to the current parser.

I wrote at least the first version of the current sage command line parser, and frankly I didn't know what I was doing at the time, and just sort of stupidly copied random bits and pieces of design from programs I had used.  Using python's subcommands support is a lot more systematic, and can also result in very nice modular code.


---

Comment by embray created at 2020-09-01 13:32:32

Since all of the sage script's current "subcommands" (e.g. `sage -b`, `sage -i`) all start with hyphens, and new subcommands with be non-hyphenated, I think it would work to support both without too much ambiguity but I'd be interested in a counter-example.  `sage <filename.{py,sage}>` would still work since no sub-command would be confused with a runnable script filename.


---

Comment by embray created at 2020-09-01 13:37:14

Replying to [comment:68 was]:
> Using python's subcommands support is a lot more systematic, and can also result in very nice modular code.

I might still just write it as a shell script.  Reason being, based on my experience implementing CLIs in Python, it tends to be much much slower to run a single command. At the very least I would do this for the top-level `sage` script.  Most subcommands would delegate to another program which might be another shell script, or could be written in Python (as is already the case).  For subcommands written in Python it's not always so bad as long as most operations you would do with that command are long enough to make the Python interpreter startup time negligible.  Those could also have further subcommands.


---

Comment by was created at 2020-09-01 13:39:59

> I might still just write it as a shell script.

+1

I should have just said "in my experience, structuring command line parsing code as subcommands (implemented in any language) can result in very nice modular code."


---

Comment by mkoeppe created at 2020-09-03 02:52:21

Changing priority from critical to minor.


---

Comment by nbruin created at 2020-09-04 16:17:04

Replying to [comment:68 was]:
> +1 from me to changing the sage script to support subcommands, 

One very frustrating part of subcommands is the failure of standard tab-completion to work with it:
for instance, for `jupyter notebook sheet.ipynb`. If there were just a command `jupyter-notebook`, it would be much easier and faster to type. Particularly with jupyter, which you nearly always use to start its notebook, it's rather frustrating. For git somehow it feels a little more natural, probably because there is naturally a larger variety of actions you want to take  through it. It also helps that most preconfigured bash tabcompletions are aware of git subcommands. (although still, distinct commands git-push, git-branch, git-pull would be faster)


---

Comment by jhpalmieri created at 2020-09-04 16:27:21

Replying to [comment:73 nbruin]:
> Replying to [comment:68 was]:
> > +1 from me to changing the sage script to support subcommands, 
> 
> One very frustrating part of subcommands is the failure of standard tab-completion to work with it:

The question so far has been (for example) `sage --notebook` vs. `sage notebook`, and tab-completion won't work with either. Are you suggesting adding `sage-notebook` and other scripts?


---

Comment by nbruin created at 2020-09-04 16:48:07

Replying to [comment:74 jhpalmieri]:

> The question so far has been (for example) `sage --notebook` vs. `sage notebook`, and tab-completion won't work with either. Are you suggesting adding `sage-notebook` and other scripts?

From a tab-completion point of view that would make sense, yes. (that, or learn how to extend the tab completion patterns). For this particular example, I'd use `jupyter notebook` anyway, with the sage kernel installed in the system jupyter server.

The traditional reason for having dashes in front of options/subcommands is to remove ambiguity from `sage notebook` (to run the file notebook) and `sage notebook` (to start the notebook). For that reason, I think we can only have subcommands for `sage` if `sage <file>` would have no meaning. I don't think we can discard this main function of `sage`. I think with jupyter, where there is one VERY common use, it's already a mistake to go with a subcommand design.

Extrapolating from that, I think that using subcommands for the `sage` script is also the wrong fit. It works well with `git`, but users really interact differently with git.


---

Comment by mkoeppe created at 2020-09-04 17:48:39

Replying to [comment:75 nbruin]:
> The traditional reason for having dashes in front of options/subcommands is to remove ambiguity from `sage notebook` (to run the file notebook) and `sage notebook` (to start the notebook). For that reason, I think we can only have subcommands for `sage` if `sage <file>` would have no meaning. I don't think we can discard this main function of `sage`. I think with jupyter, where there is one VERY common use, it's already a mistake to go with a subcommand design.
> 
> Extrapolating from that, I think that using subcommands for the `sage` script is also the wrong fit. It works well with `git`, but users really interact differently with git.

I fully agree.


---

Comment by kini created at 2020-09-04 18:00:40

Replying to [comment:75 nbruin]:
> (that, or learn how to extend the tab completion patterns).

FWIW, there are tools which can do this for you if your command line subcommands and options are all handled by argparse (rather than e.g. a top level bash script that calls out to python programs that use argparse for each subcommand, as embray suggested).

[argcomplete](https://github.com/kislyuk/argcomplete) will dynamically provide on-the-fly completion candidates by actually running the argument parsing logic from the `sage` program every time you hit tab in the shell. This is always accurate but could be slow if `sage` takes a long time to get to the line of code where the argument parser is run (e.g. if it has some heavy imports).

[shtab](https://github.com/iterative/shtab) also runs the argument parsing logic from the `sage` program, but it statically generates a bash completion script which you can then register with `bash-completion` by putting it in a relevant place (if you don't have root access, this can be `~/.local/share/bash-completion/completions/`). Then when you press tab in the shell, completions should be pretty instantaneous, but the completion script needs to be kept up to date with the command line interface of `sage`.

If you use a shell other than bash, it may be harder. zsh, at least, is supported by shtab and to some extent argcomplete as well.

I suggest that `shtab` be run as part of the build process of Sage and that the resulting bash completion script be installed as part of the installation process. That should give out-of-the-box completion functionality to the majority of users, which would be nice. (Again, though, this would only work if the top-level `sage` does argument parsing in Python with `argparse`, and I understand that might not end up being the case for other reasons.)
