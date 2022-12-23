# Issue 9528: #8306 completely breaks "sage -upgrade"

Issue created by migration from https://trac.sagemath.org/ticket/9528

Original creator: was

Original creation time: 2010-07-17 12:24:55

Assignee: GeorgSWeber

If you have any version of sage < version 4.5, and you try to upgrade to sage-4.5, the addition of a file pipestatus in #8306 means that your upgrade will instantly and totally break.


---

Comment by was created at 2010-07-17 12:43:24

My first idea to fix this is to modify the script `spkg/install`, which *does* get updated on "sage -upgrade" so that it checks for the file pipestatus, and if it isn't there, then it downloads it. 

Unfortunately, `install` is a shell script, not a python script, so grabbing a file is harder.  But it could call python.

This is going to be a little ugly though.


---

Comment by leif created at 2010-07-17 12:56:39

Or just *create* `pipestatus` in `spkg-install`; it's an almost trivial script, unlikely to change, and we can check for the bash version number *once* inside `spkg-install` and write only the appropriate branch to `pipestatus`.


---

Comment by leif created at 2010-07-17 12:58:48

The only reason for `pipestatus` was that we did not want to rely on bash version >=3.0.


---

Comment by was created at 2010-07-17 13:14:42

Replying to [comment:2 leif]:
> Or just *create* `pipestatus` in `spkg-install`; 

This will not work.   The problem is that spkg-install isn't run until after pipestatus is needed. 

> it's an almost trivial script,

I disagree -- It's 33 lines long, and  I read it for 2 minutes and didn't fully understand it.


---

Attachment

Bash script to create specific version of "pipestatus" in $SAGE_ROOT/spkg


---

Comment by leif created at 2010-07-17 14:10:25

William, perhaps you can paste the attached shell script (i.e. part of it, removing the first line) into some other script that is run at the right moment in the upgrade process.

(The "harder" part of `pipestatus` is obviously non-trivial to understand, therefore it contains a reference to its explanation, [shortcut](http://www.unix.com/302265010-post3.html). It's actually suited for _many_ Bourne shells, not just bash <3.0.)


---

Comment by was created at 2010-07-17 14:29:57

Lief -- many thanks for posting this, which I *greatly* appreciate.


---

Comment by leif created at 2010-07-17 14:34:14

Btw, you can drop the parentheses in the >=3.0 version, since we don't have to set `pipefail` in a subshell (it's a stand-alone script).


---

Comment by leif created at 2010-07-17 14:40:30

And `pipestatus`'s

```sh
if [ -z "$1" ]; then
  # usage error ...
```

should be

```sh
if [ $# -ne 2 ]; then
  # usage error ...
```



---

Attachment

this should be put as SAGE_ROOT/spkg/install


---

Attachment

Creates a slightly improved version of pipestatus, no changes to the script code itself


---

Comment by was created at 2010-07-17 15:01:02

Hi,

I rewrote a script based on your idea (but not using your code).  I tested it by:

 (1) taking sage-4.5 and move spkg/pipestatus to spkg/pipestatus.orig
 (2) typed "make", then control-c in a few seconds
 (3) Do diff spkg/pipestatus spkg/pipestatus.orig and observe that the diff is just a single blank line.

Please review.  Since spkg/install is pulled in by SAGE_ROOT/local/bin/spkg-update, this should fix the problem.


---

Comment by was created at 2010-07-17 15:01:02

Changing status from new to needs_review.


---

Comment by leif created at 2010-07-17 15:57:02

Replying to [comment:9 was]:
> Please review.  Since spkg/install is pulled in by SAGE_ROOT/local/bin/spkg-update, this should fix the problem.

I just noticed I had written `spkg-install` instead of `spkg/install`... :/

Of course I prefer generating a version-specific `pipestatus`, but if it is a temporary solution, I'm ok with omitting it.

I'd though at least fix `pipestatus`'s parameter checking as I did in my second version:

```sh
...
  cat > pipestatus <<EOF
#!/usr/bin/env bash

if [ \$# -ne 2 -o -z "\$1" -o -z "\$2" ]; then
    echo "Run two commands in a pipeline 'CMD1 | CMD2' and exit"
    echo "with the exit status of CMD1, *not* that of CMD2."
    echo "\$0 cmd1 cmd2"
    exit
fi
...
```


Dropping the parentheses around `(set -o pipefail; eval "\$1 | \$2")` is optional, but you should remove `-n` from the `echo` in your `install`.

We cannot yet test upgrading from e.g. 4.4.4 though, can we?

(I've tried your `install` there, it's ok when `deps` etc. get updated, too.)

In any case, add a

```sh
    chmod +x pipestatus
```

after the `cat`...


---

Comment by leif created at 2010-07-17 17:48:25

Replying to [comment:9 was]:
>  (3) Do diff spkg/pipestatus spkg/pipestatus.orig and observe that the diff is just a single blank line.

Unfortunately, the blank line is in the wrong place. `#!` *must* be the first characters in the file, otherwise strange things happen...


---

Comment by mpatel created at 2010-07-17 21:17:27

Remove blank line, add chmod.  Updated `spkg/install` based on "4.5"


---

Attachment

Diff of `spkg/install` vs "4.5".


---

Comment by mpatel created at 2010-07-17 21:28:30

I apologize for not testing `sage -upgrade` (and other problems not yet found!).  Thanks very much for working on a fix.

Following Leif's suggestions, I've attached a slightly updated `install` that I'm testing now.  Since we've already tested `pipestatus` on several platforms, I suggest making changes to it in a separate ticket.  Perhaps we could remove it altogether, in favor of always auto-generating it?


---

Comment by mpatel created at 2010-07-17 22:30:49

Upgrading from 4.4.4 to 4.5 works for me on sage.math with [attachment:install.2].  The long doctests pass.  This is with `MAKE="-j12"` and `SAGE_PARALLEL_SPKG_BUILD="yes"`.  A separate, completely serial upgrade with MAKE unset is still running.

Starting with "4.5" on sage.math, I copied [attachment:install.2] to `spkg/` and made a new source distribution with `sage -sdist 4.5.1`.  This builds with `MAKE="-j20"` and `SAGE_PARALLEL_SPKG_BUILD="yes"`.  The long doctests pass.  Another build with just `MAKE="-j16"` is still running.

Thanks again for fixing this.


---

Comment by mpatel created at 2010-07-18 01:36:20

Replying to [comment:13 mpatel]:
> Upgrading from 4.4.4 to 4.5 works for me on sage.math with [attachment:install.2].  The long doctests pass.  This is with `MAKE="-j12"` and `SAGE_PARALLEL_SPKG_BUILD="yes"`.  A separate, completely serial upgrade with MAKE unset is still running.

> Starting with "4.5" on sage.math, I copied [attachment:install.2] to `spkg/` and made a new source distribution with `sage -sdist 4.5.1`.  This builds with `MAKE="-j20"` and `SAGE_PARALLEL_SPKG_BUILD="yes"`.  The long doctests pass.  Another build with just `MAKE="-j16"` is still running.

Those builds' long doctests also pass, as do those for a completely serial build of "4.5.1" from scratch on sage.math.

I'm attempting to upgrade from a 4.3.0.1 binary on t2.  I'm also building 4.4.4 on bsd.math so that I can test `sage -upgrade`.

But so far, my review is positive.


---

Comment by mpatel created at 2010-07-18 08:06:08

Upgrading from 4.4.4 also works for me on bsd.math.

On t2:  It seems the 4.3.0.1 binary is too old to upgrade.  (LinBox doesn't build, possibly because part of the toolchain has changed since 4.3.0.1 was built.)  But upgrading from "4.5" to "4.5.1" works, after deleting the former's `pipestatus`.

I'm still building 4.4.4 on t2, but I think we're ready for the real 4.5.

Can someone check that the small changes made from `install` to `install.2` are OK?


---

Comment by mpatel created at 2010-07-18 10:24:43

Replying to [comment:15 mpatel]:
> I'm still building 4.4.4 on t2, but I think we're ready for the real 4.5.

The upgrade from 4.4.4 to "4.5.1" on t2 is now working on Singular --- the Sage and Gap packages remain.  No problems so far.  I need to sleep soon; I'll report again as soon as possible.

Also, "4.5.1" also builds from scratch on bsd.math.  The long doctests pass.


---

Comment by was created at 2010-07-18 13:35:27

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-07-18 13:35:27

Looks very good.  Thanks guys!!


---

Comment by leif created at 2010-07-18 15:59:00

Replying to [comment:15 mpatel]:
> Can someone check that the small changes made from `install` to `install.2` are OK?

Yes. Positive review, too.


---

Comment by leif created at 2010-07-18 16:03:09

In the long run, we should use something like `pipestatus` in `$SAGE_ROOT/makefile`, too.


---

Comment by mpatel created at 2010-07-18 16:39:37

Replying to [comment:15 mpatel]:
> I'm still building 4.4.4 on t2, but I think we're ready for the real 4.5.

Upgrading from 4.4.4 to "4.5.1" works on t2.  The long doctests pass.


---

Comment by rlm created at 2010-07-19 11:20:55

Resolution: fixed
