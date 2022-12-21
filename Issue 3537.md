# Issue 3537: [with patch, needs review] sage-env breaks makefile RM

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-06-30 03:24:02

Assignee: mabshoff

CC:  mabshoff snark drkirkby jdemeyer

The env variable RM is set to rm instead of rm -rf.  This breaks some functionality of make (such as compiling .l files) which breaks the ability to compile M2 with sage-env sourced.


---

Attachment


---

Comment by gfurnish created at 2008-06-30 03:28:37

Changing assignee from mabshoff to gfurnish.


---

Comment by gfurnish created at 2008-06-30 03:28:37

Changing status from new to assigned.


---

Comment by ghtdak created at 2008-06-30 03:57:42

The intent of -f is to avoid errors for the conditions cited as a problem.


---

Comment by mabshoff created at 2008-06-30 04:45:17

Changing priority from blocker to major.


---

Comment by mabshoff created at 2008-06-30 04:45:17

I am not convinced yet that this is the right thing to do and it is rather likely that this will break something else in the tree. The solution to M2's problem is to unset RM in spkg-install and then to set RM to some value you desire.

And this is definitely not a blocker for 3.0.4.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-01 04:40:38

If M2 depends on the default behavior of RM in its Makefiles it should set RM in its top level makefile. I see no reason to change Sage's behavior and as is if someone sets RM outside of sage-env it is propagated anyway. So this is wontfix.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-01 04:40:38

Resolution: wontfix


---

Comment by vbraun created at 2010-12-11 11:58:59

Changing status from closed to new.


---

Comment by vbraun created at 2010-12-11 11:58:59

I'm reopening this bug since people keep tripping over this issue. We need to fix this or we'll end up with every spkg working around the `RM=rm` issue. As the spkg maintainer/author, I know that `cddlib` and `TOPCOM` both need to `unset RM` or they won't build. In #10285 it was noted a few days ago that Boehm GC 7.2 also trips over this issue. More and more packages will fail because of this issue as soon as upsteam re-runs autotools...

For the record, gfurnish's patch applies cleanly on Sage-4.6.1.alpha3 (apply to the $SAGE_LOCAL/bin repo)

I'd be happy to give this a positive review. Maybe mabshoff can reconsider his objections?


---

Comment by vbraun created at 2010-12-11 11:58:59

Resolution changed from wontfix to 


---

Comment by vbraun created at 2010-12-11 12:07:39

Changing status from new to needs_review.


---

Comment by leif created at 2010-12-17 15:54:32

Replying to [comment:5 vbraun]:
> I'm reopening this bug since people keep tripping over this issue. We need to fix this or we'll end up with every spkg working around the `RM=rm` issue.

Well, is this a bug? 

> More and more packages will fail because of this issue as soon as upsteam re-runs autotools...

That's IMHO a problem of autotools. `$RM` is in general not supposed to _not return an error_ on non-existing files; if autotools were a bit smarter, they would just add `-f` or whatever might be appropriate. If they redefine the meaning of `RM`, that's not Sage's problem in the first place; of course spkg maintainers would have to `unset RM` for upstream packages using (newer) autotools.


> I'd be happy to give this a positive review. Maybe mabshoff can reconsider his objections?

Michael has quit a while ago, though he perhaps still reads trac notifications... ;-)


Note that redefining `RM` in `sage-env` could actually break other parts of Sage, not necessarily limited to spkgs, since e.g. removing a file which is expected to exist, but doesn't, without raising an error might hide other errors and cause arbitrary behavior.

Also, as Michael said, changing the default value in `sage-env` doesn't help if `RM` was already defined (intentionally or not) by the user, so w.r.t. autotools really _won't fix_. We have to `unset RM` (or add an appropriate flag to force deletion if it's not already contained) in `spkg-install`s of such packages anyway to be safe.


I think we should prominently document this issue, and close this ticket again.


---

Comment by jdemeyer created at 2010-12-17 16:00:28

Why does `RM` need to be defined at all?


---

Comment by leif created at 2010-12-17 17:53:11

Replying to [comment:8 jdemeyer]:
> Why does `RM` need to be defined at all?

Because

```sh
${RM} some_file
```

will (hopefully) fail if `RM` is not set or empty?

Imagine `some_file` was executable in that case...




It would be a bit odd to test and eventually set all such variables individually in every script that uses some of these, therefore we have `sage-env`.

Though `CP`, `RM` etc. are meanwhile hardly used within Sage; perhaps because setting them isn't necessary on any proper OS...

Instead, it would be better to have e.g. `EGREP`, (POSIX-conformant) `GREP` etc., detected / set by Sage's `configure`.


---

Comment by vbraun created at 2010-12-17 20:04:28

I seriously doubt that anybody uses the "destructive existence test" `$RM filename || ...` :-)

Automake has an official list of variables that it looks at. Perhaps it is a bug that `RM` is on the list, but its still our problem and I doubt upstream will change because some guys from Sage have a variable name collision. See also http://www.gnu.org/software/automake/manual/make/Implicit-Variables.html


---

Comment by jdemeyer created at 2010-12-18 13:19:41

Replying to [comment:9 leif]:
> Because
> {{{
> #!sh
> ${RM} some_file
> }}}
> will (hopefully) fail if `RM` is not set or empty?

Where is such code used?  My guess: nowhere.


---

Comment by leif created at 2010-12-26 18:33:20

Replying to [comment:11 jdemeyer]:
> Replying to [comment:9 leif]:
> > Because

```sh
${RM} some_file
```

> > will (hopefully) fail if `RM` is not set or empty?
> 
> Where is such code used?  My guess: nowhere.

E.g. Singular's `spkg-install` does. (It actually does `$RM -f ...`.)

I wouldn't base such changes on guesses... ;-)


---

Comment by vbraun created at 2010-12-26 19:16:57

For the record:

```
[vbraun`@`volker-desktop spkg-unpacked]$ grep '\$RM' */*
gap-4.4.12.p4/SPKG.txt: * #7873 Remove references to $LN, $MKIDR and $RM and replace
mercurial-1.6.4.p0/SPKG.txt: * Changes occurrences of $RM to 'rm', $CP to 'cp' and similar.
sage_scripts-4.6.1.alpha3.p0/sage-env:if [ "$RM" = "" ]; then
singular-3-1-1-4.p3/spkg-install:        $RM -f LIB
singular-3-1-1-4.p3/spkg-install:    $RM -f Singular singular
singular-3-1-1-4.p3/spkg-install:        $RM -f Singular-1-0-2   # remove previous version of Singular.
```



---

Comment by leif created at 2010-12-26 22:23:40

Replying to [comment:13 vbraun]:
> For the record:

```sh
[vbraun`@`volker-desktop spkg-unpacked]$ grep '\$RM' */*
```


Redo for `${RM}`, too? (Also `$(RM)` in Makefiles.)

Not sure if there are some "deeper" instances as well.


---

Comment by vbraun created at 2010-12-26 22:51:26


```
[vbraun`@`volker-desktop spkg-unpacked]$ grep '\$.RM' */*
singular-3-1-1-4.p3/install-sh:rmprog="${RMPROG-rm}"
```

and

```
[vbraun`@`volker-desktop spkg-unpacked]$ grep '\$.*RM' */*
gap-4.4.12.p4/SPKG.txt: * #7873 Remove references to $LN, $MKIDR and $RM and replace
mercurial-1.6.4.p0/SPKG.txt: * Changes occurrences of $RM to 'rm', $CP to 'cp' and similar.
sage_scripts-4.6.1.alpha3.p0/sage-check-64:		case $CONFIRM in
sage_scripts-4.6.1.alpha3.p0/sage-env:if [ "$RM" = "" ]; then
singular-3-1-1-4.p3/install-sh:rmprog="${RMPROG-rm}"
singular-3-1-1-4.p3/spkg-install:        $RM -f LIB
singular-3-1-1-4.p3/spkg-install:    $RM -f Singular singular
singular-3-1-1-4.p3/spkg-install:        $RM -f Singular-1-0-2   # remove previous version of Singular.
```



---

Comment by jhpalmieri created at 2011-03-26 17:02:28

So right now, singular is the only place this is used, and it consistently uses "$RM -f", right?  Given this, rather than set `RM="rm -f"`, it seems better to leave it as is and document it in the developer's guide (in the section on producing new spkg's), and perhaps also in the installation guide (in the section on environment variables).  Here's a patch doing that; what do you think?


---

Attachment


---

Comment by jdemeyer created at 2011-03-26 18:03:41

My opinion still is that `RM` should simply be left unset (of course, a few install scripts will have to be changed).


---

Comment by drkirkby created at 2011-03-26 18:32:15

Replying to [comment:18 jdemeyer]:
> My opinion still is that `RM` should simply be left unset (of course, a few install scripts will have to be changed).

I agree 100%. 

I can understand the logic of variables like $CC, $CXX, $MAKE, but not $RM. I don't know of any system where one might want to specify what version of `rm` gets used, so I don't see the point in having a variable for it. If some dump package needs `$RM` defined, then either try to fix the code so it is not so dumb, or add `$RM` to `dump_package.spkg`. 

BTW, take a look at

http://boxen.math.washington.edu/home/kirkby/bad-code/sympow-1.018.1.p7/src/Configure

where you will find some _interesting_ use of variable names. A script which starts 

`#!/bin/sh`

has a function 

`whichexe()`

This function makes use of a non-POSIX command `which`, so there's no reason for `which` to exist. Then `whichexe()` function sets variables for things like SH, RM, SED, whilst checking if the commands (including `sh`) exist. If not the script exits. An abbreviated version is below. 

{{{#!/bin/sh
whichexe() {
    if [ -f /bin/$1 ]; then
        echo /bin/$1
        return;
    fi;
    if [ -f /usr/bin/$1 ]; then
        echo /usr/bin/$1
        return;
    fi;
    if [ -f /usr/local/bin/$1 ]; then
        echo /usr/local/bin/$1
        return;
    fi;
    echo `which $1`
}
RM=`whichexe rm`
GREP=`whichexe grep` && echo "#define GREP \"$GREP\"" >> $CONFIG
SED=`whichexe sed` && echo "#define SED \"$SED\"" >> $CONFIG
SH=`whichexe sh` && echo "#define SH \"$SH\"" >> $CONFIG
if [ -z "$SH" ]; then
  echo "**ERROR**: Could not find sh"; exit 1;
else
  echo "SH = $SH"
fi
```


I might have cleaned this up, so the current version in Sage might not be quite so dumb. 

Dave


---

Comment by jhpalmieri created at 2011-03-26 23:53:25

See #9497 for a patch to change "$RM" to "rm" in Singular's spkg-install script.


---

Comment by mariah created at 2011-05-12 14:30:01

When 50 percent or more of spkgs require $RM to be "rm -f" then
change $RM from "rm" to "rm -f".  Until then document.

Positive review.


---

Comment by mariah created at 2011-05-12 14:30:01

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-05-12 14:57:46

Changing component from build to scripts.


---

Comment by jdemeyer created at 2011-05-12 14:57:46

Singular's spkg-install no longer uses $RM, so the documentation is not up to date.


---

Comment by jdemeyer created at 2011-05-12 14:57:46

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-05-12 14:58:09

Do not set $RM in sage-env


---

Attachment

[attachment:trac_3537-unset-RM.patch] applied to sage-4.7.rc2 tested on skynet/taurus with make testlong.  All tests passed.  Positive review.


---

Comment by mariah created at 2011-05-12 20:40:02

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-05-12 20:47:58

Replying to [comment:23 mariah]:
> [attachment:trac_3537-unset-RM.patch] applied to sage-4.7.rc2 tested on skynet/taurus with make testlong.  All tests passed.  Positive review.

Did you try building Sage from source with this patch applied?  Because this patch affects the Sage *build*, not the Sage library.


---

Comment by mariah created at 2011-05-13 13:10:56

Apologies for not be clear.  I first applied the patch to the sage-4.7.rc2 source, then built the source, then did make testlong.


---

Comment by jdemeyer created at 2011-05-17 08:47:22

Resolution: fixed


---

Comment by jdemeyer created at 2011-05-17 08:47:22

I just checked all spkg-install scripts and `$RM` is used nowhere anymore.
