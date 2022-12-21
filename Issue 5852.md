# Issue 5852: [with patch, needs review] the detection of SAGE_ROOT in $SAGE_ROOT/sage script should expand symlinks recursively

Issue created by migration from Trac.

Original creator: tornaria

Original creation time: 2009-04-22 12:39:58

Assignee: tbd

CC:  leif kini

Currently, `$SAGE_ROOT/sage` uses (first among other alternate methods) `readlink -n` to detect the directory where the script lives (that's $SAGE_ROOT), but it should use `readlink -nf` to expand symlinks recursively.

Otherwise, the symlink expansion may not be completely done, and `$SAGE_ROOT` could end up with a non-canonical dirname, which leads to issues with testing.

Here's a way to reproduce an issue with the current script. For the example, my sage-3.4 installation lives in `/home/sage/sage-3.4`, and here's what happened to me:

```
/home/sage$ md5sum sage-3.4/sage
4153919efe1edcd34ad7fa193122d679  sage-3.4/sage
/home/sage$ ln -s sage-3.4 sage-3.4-symlink
/home/sage$ ln -sf /home/sage/sage-3.4-symlink/sage /home/tornaria/bin/sage
/home/sage$ type sage
sage is hashed (/home/tornaria/bin/sage)
/home/sage$ readlink `type -p sage`
/home/sage/sage-3.4-symlink/sage
/home/sage$ readlink -f `type -p sage`
/home/sage/sage-3.4/sage
```


As you can see, `readlink -n` expands once but doesn't cannonicalize the path to the `sage` script. And here's the symptom:

```
/home/sage$ sage -t sage-3.4/devel/sage-main/sage/all.py
sage -t  "sage-3.4/devel/sage-main/sage/all.py"             
  File "./all.py", line 18
    from sage-3.4/devel/sage-main/sage/all import *
             ^
SyntaxError: invalid syntax

	 [0.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "sage-3.4/devel/sage-main/sage/all.py"
Total time for all tests: 0.3 seconds
```



---

Comment by tornaria created at 2009-04-22 12:46:06

Changing assignee from tbd to tornaria.


---

Comment by tornaria created at 2009-04-22 12:46:06

Changing component from algebra to misc.


---

Comment by tornaria created at 2009-04-22 12:46:06

Patching `$SAGE_ROOT/sage` with this:

```
--- sage-3.4/sage.orig	2009-04-22 01:45:48.000000000 -0300
+++ sage-3.4/sage	2009-04-22 09:37:27.000000000 -0300
`@``@` -14,6 +14,7 `@``@`
 fi
 
 if [ "$SAGE_ROOT" = "....." ];  then
+    SAGE_ROOT=`readlink -nf "$0" 2> /dev/null` || \
     SAGE_ROOT=`readlink -n "$0" 2> /dev/null` || \
     SAGE_ROOT=`realpath    "$0" 2> /dev/null` || \
     SAGE_ROOT="$0"
```

fixes the issue, since now `$SAGE_ROOT` is correct.

According to mabshoff, `readlink -f` doesn't work on some BSD; that's why I left the `readlink -n` test in the second line, but this should of course be tested on those BSD to make sure it doesn't cause a regression.


---

Comment by tornaria created at 2009-04-25 02:02:27

On systems where "readlink -f" is supported, use that so the path for $SAGE_ROOT is fully canonicalized


---

Attachment

Replying to [comment:1 tornaria]:
> Patching `$SAGE_ROOT/sage` with this:
> {{{
> --- sage-3.4/sage.orig	2009-04-22 01:45:48.000000000 -0300
> +++ sage-3.4/sage	2009-04-22 09:37:27.000000000 -0300
> `@``@` -14,6 +14,7 `@``@`
>  fi
>  
>  if [ "$SAGE_ROOT" = "....." ];  then
> +    SAGE_ROOT=`readlink -nf "$0" 2> /dev/null` || \
>      SAGE_ROOT=`readlink -n "$0" 2> /dev/null` || \
>      SAGE_ROOT=`realpath    "$0" 2> /dev/null` || \
>      SAGE_ROOT="$0"
> }}}
> fixes the issue, since now `$SAGE_ROOT` is correct.
> 
> According to mabshoff, `readlink -f` doesn't work on some BSD; that's why I left the `readlink -n` test in the second line, but this should of course be tested on those BSD to make sure it doesn't cause a regression.

I can confirm that it does not work on MacOS X.10.4.11 (e.g. Anne Schilling's machine)

A fix would be most welcome, as this makes sage -t make false reports of broken test files.


---

Comment by nthiery created at 2009-05-04 16:16:06

The readlink -f workaround is better than nothing, and should not make things worst for systems like BSD. I would vote for including it now, in waiting for a better solution.
Should I set a positive review?

Besides, what about adding a switch to sage -t to specify manually that the given file is inside or outside the sage source tree?

This would make a workaround for MacOX X, and also be occasionally be useful. For example, I often run tests from one sage source tree with another sage to compare the results.


---

Comment by tornaria created at 2009-05-17 03:02:28

Is there some equivalent of `readlink -f` that works in MacOS X?


---

Comment by tornaria created at 2009-05-17 03:17:57

Note that the version of `readlink` which is included in fink (in package `debianutils`) supports the `-f` switch, so a mac with fink doesn't suffer from this issue (asuming `/sw/sbin` is before `/usr/bin` in the search PATH).


---

Comment by was created at 2009-05-28 07:00:31

See #6146 for fixing this on systems that don't support readlink -f.


---

Comment by mhansen created at 2009-05-28 07:04:07

Resolution: fixed


---

Comment by mhansen created at 2009-05-28 07:04:07

Merged in 4.0.rc1.


---

Comment by was created at 2009-07-01 11:25:00

Question.  Does 

```
readlink -n sage
```

work on any platform?!  It gives an error on *both* OS X and Linux.  Why is it even there?!

```
OS X
ub243101:s wstein$ readlink -n sage
ub243101:s wstein$ echo $?
1

Linux:
wstein`@`boxen:~/sage$ readlink -n sage
wstein`@`boxen:~/sage$ echo $?
1
```


I wonder who wrote this weird SAGE_ROOT code in the first place?  I wrote something a long time ago, but it bears no resemblance to the current code.


By the way, I've had reports of major failures caused by using `readlink -nf` by one user who has a symlink + nfs mount setup.  Their problems are solved by deleting the `readlink -nf` line.   Why don't we use realpath first and only if that doesn't work use something else?  It seems like realpath is the right choice, since it's supposed to " converts each filename argument to an absolute pathname, which has no components that are symbolic links or the special
       .  or ..  directory entries...  Please note that mostly the same functionality is provided by the ‘-f’ option."

There is no realpath on OS X, but that is ok since readlink doesn't work ever on OS X anyways, so no loss. 

 -- William


---

Comment by tornaria created at 2009-07-01 13:00:03

Replying to [comment:8 was]:
> Question.  Does 
> {{{
> readlink -n sage
> }}}
> work on any platform?!

Yes it does: it reads the content of a symbolic link. It succeeds if and only if the argument is actually a symbolic link, e.g.

```
~/sandbox$ ls -l
total 0
~/sandbox$ mkdir sage1
~/sandbox$ readlink sage1 ; echo $?  ## fails b/c sage1 is not a symlink
1
~/sandbox$ ln -s sage1 sage2
~/sandbox$ readlink sage2 ; echo $?  ## ok b/c sage2 is actually a symlink
sage1
0
```

The option `-n` means to not print a trainling newline character; I don't think it really make a difference due to bash usual escaping rules.

>  It gives an error on *both* OS X and Linux.  Why is it even there?!

It was there before the patch in this ticket, so that if `$0` (the path to the script one is running) is actually a symlink to the real path of the sage script, the detection of `SAGE_ROOT` works. On systems that support `-f`, that is a more complete solution, but the fallback was left for the benefit of systems where `readlink -f` does not work (e.g. OS X).

Following my example above, here's an example where `-f` is needed:

```
~/sandbox$ ln -s sage2 sage3
tornaria`@`bip:~/sandbox$ readlink -n sage3
sage2tornaria`@`bip:~/sandbox$ readlink sage3
sage2
tornaria`@`bip:~/sandbox$ readlink -f sage3
/home/tornaria/sandbox/sage1
```


The other major case is when there are symlinks in some of the components of the path, those get canonicalized by `readlink -f`, but not by plain `readlink` (this leads to failures as shown in the description).


> By the way, I've had reports of major failures caused by using `readlink -nf` by one user who has a symlink + nfs mount setup.  Their problems are solved by deleting the `readlink -nf` line.   Why don't we use realpath first and only if that doesn't work use something else?  It seems like realpath is the right choice, since it's supposed to " converts each filename argument to an absolute pathname, which has no components that are symbolic links or the special
>        .  or ..  directory entries...  Please note that mostly the same functionality is provided by the ‘-f’ option."

Can you give a pointer to those? Not using `readlink -f` leads to major failures in testing, as described in the description of the ticket.

Do you actually know that in those cases `realpath` works? It seems to me that both are implemented using `realpath(3)`, so they should be the same unless I'm missing something.

> There is no realpath on OS X, but that is ok since readlink doesn't work ever on OS X anyways, so no loss. 

There is no `realpath` in most systems I have access to (other than sage.math). In fact, `readlink` is pretty much standard (possibly POSIX), although `-f` option is not (a GNUism?). For GNU systems (e.g. linux), it comes bundled in coreutils, which means it will be available everywhere. OTOH, `realpath` comes in _optional_ package `realpath`. Do you know of a system where `readlink -f` doesn't work but `realpath(1)` is available?

OTOH, realpath(3) seems to be a POSIX standard, and it seems to be available on OS X:

```
$ nm /usr/lib/libc.dylib | grep realpath
/usr/lib/libc.dylib(realpath.So):
9003f1f0 T _realpath
```

so an alternative would be to compile our own `realpath` binary and somehow use it from the startup script. But we need a path to SAGE_ROOT so we can find SAGE_ROOT/local/bin/realpath... auch... (doesn't need to be canonical, though.... so we could use readlink a few times to get a path to the actual sage script, and then run `realpath` from there).


---

Comment by was created at 2009-07-01 23:32:30

It's possible that this ticket should be reverted until a major bug it causes is fixed.   

The reason for this ticket in the first place was the following, as given in the ticket description:

```
/home/sage$ md5sum sage-3.4/sage
4153919efe1edcd34ad7fa193122d679  sage-3.4/sage
/home/sage$ ln -s sage-3.4 sage-3.4-symlink
/home/sage$ ln -sf /home/sage/sage-3.4-symlink/sage /home/tornaria/bin/sage
/home/sage$ type sage
```


Notice the symlink of the Sage script

```
/home/sage$ ln -sf /home/sage/sage-3.4-symlink/sage /home/tornaria/bin/sage
```


For the record, this is *not* how I meant the sage script is meant to be used.  I bet this isn't documented, but it should be.  The script should never be used that way.  Instead one should do

```
/home/sage$ cp /home/sage/sage-3.4-symlink/sage /home/tornaria/bin/sage
```

and then edit the copied script to explicitly point to the ROOT.   It was never my intention for somebody to run the sage script unmodified outside of SAGE_ROOT.    Me not intending this means that elsewhere in the Sage build/test system this assumption is made, and the workaround on this ticket actually seriously breaks things for some users. 

The change in this ticket causes serious breakage for people whose home directory is NFS mounted, and for which their Sage build is on another volume that is symlinked from their home directory. i.e., this sort of setup:

```
    cd ~wstein    # my home directory is NFS mounted.
    mkdir /tmp/wstein       # /tmp is a local disk
    ln -s /tmp/wstein sage-build
    cd sage-build    # 
    # build sage here, doctesting fails completely
```


I'm doing a test build for myself to confirm that this happens, and if so and I can't figure out how to fix this promptly (maybe I will be able to), then we have to revert this change, and document that one can't just symlink the sage script out.


---

Comment by tornaria created at 2009-07-01 23:58:20

Replying to [comment:10 was]:
> It's possible that this ticket should be reverted until a major bug it causes is fixed.
> [...]
> For the record, this is *not* how I meant the sage script is meant to be used.  I bet this isn't documented, but it should be.  The script should never be used that way.  Instead one should do
> {{{
> /home/sage$ cp /home/sage/sage-3.4-symlink/sage /home/tornaria/bin/sage
> }}}
> and then edit the copied script to explicitly point to the ROOT.   It was never my intention for somebody to run the sage script unmodified outside of SAGE_ROOT.    Me not intending this means that elsewhere in the Sage build/test system this assumption is made, and the workaround on this ticket actually seriously breaks things for some users. 

If you only use the script in *that* way, then the

```
if [ "$SAGE_ROOT" = "....." ];  then
```

branch would never be taken, and as the patch in this ticket only touches this branch, it can't break anything.

In practice, it is much more convenient to just use a symlink to the script, if it can be worked out. Before this patch, it turned out that the real, canonical path for SAGE_ROOT could be identified incorrectly, and *this* causes doctesting to fail.

> The change in this ticket causes serious breakage for people whose home directory is NFS mounted, and for which their Sage build is on another volume that is symlinked from their home directory. i.e., this sort of setup:
> {{{
>     cd ~wstein    # my home directory is NFS mounted.
>     mkdir /tmp/wstein       # /tmp is a local disk
>     ln -s /tmp/wstein sage-build
>     cd sage-build    # 
>     # build sage here, doctesting fails completely
> }}}
> 
> I'm doing a test build for myself to confirm that this happens, and if so and I can't figure out how to fix this promptly (maybe I will be able to), then we have to revert this change, and document that one can't just symlink the sage script out. 

This sort of setup is *exactly* what used to cause breakage for me, because the `SAGE_ROOT` was incorrectly computed (to a non-canonical path). What would you expect `SAGE_ROOT` to be computed to, other than the canonical path? e.g., continuing your example above:

```
    cd ~wstein/sage-build
    tar xvf sage-nnn.tar
    cd sage-nnn
    ./sage -sh
    echo "$SAGE_ROOT"
```

Are you expecting SAGE_ROOT above to be "/home/wstein/sage-build/sage-nnn/", or "/tmp/wstein/sage-nnn" ?

Before the patch, it was the former, non canonical path; after the patch, it is the latter, which is IMO the correct canonical path. When SAGE_ROOT is non-canonical, running doctests for files in the sage library fails b/c they are not recognized as part of the sage library, etc.
    
I don't see how the fact that this is NFS mounted could be relevant to the issue.


---

Comment by was created at 2009-07-04 11:43:26

The problem with this patch isn't that it is "wrong" (which is what you're arguing with me about above).  It is that it seriously breaks Sage, hence it must be reverted or the problem it causes must be fixed.  I had a look, and the problem is here in local/bin/sage-doctest:

```
        library_code = True
        ext = os.path.splitext(argv[1])[1]
        if ext in ['.spyx', '.sage'] or \
                 not (SAGE_ROOT.strip('/') + '/devel' in os.path.abspath(argv[1])):
            library_code = False
```

The problem is that the library_code variable is being set to False for all the code that *is* in the library.   It is being set to false because if one does

```
   sage -t "/home/wstein/sage-build/sage-nnn/..."
```

then argv[1] is not first canonicalized, which messes everything up completely.

So for this ticket to be in (which I agree with at some point), one needs to factor out this path caonicalization, and make sure it is applied everywhere (e.g,. in sage-doctest).  There could be many other places where subtle problems arise -- I don't know. 

For now, this needs to be reverted.


---

Comment by rlm created at 2009-07-04 19:57:42

I have reverted this patch in sage-4.1.rc0, and I'm reopening the ticket.


---

Comment by rlm created at 2009-07-04 19:57:42

Changing component from misc to distribution.


---

Comment by rlm created at 2009-07-04 19:57:42

Resolution changed from fixed to 


---

Comment by rlm created at 2009-07-04 19:57:42

Changing status from closed to reopened.


---

Comment by jhpalmieri created at 2011-08-19 03:46:08

Has the issue with `sage-doctest` been resolved?  The code now says

```python
        dev_path = os.path.realpath(os.path.join(SAGE_ROOT, 'devel'))
        our_path = os.path.realpath(argv[1])

        if not force_lib and (ext in ['.spyx', '.sage'] or
                              not dev_path in our_path):
            library_code = False
```

Since `os.path.realpath` is used twice, shouldn't this be okay?  If not, another option is to use [os.path.samefile](http://docs.python.org/library/os.path.html#os.path.samefile).


---

Attachment

Shell script replacement for "readlink -f"


---

Comment by jdemeyer created at 2011-08-23 09:14:28

Changing assignee from tornaria to jdemeyer.


---

Comment by jdemeyer created at 2011-08-23 09:14:28

Why do we set `SAGE_ROOT` inside `sage-env`?  Given that `sage-env` is only ever called when we already know `SAGE_ROOT` (i.e. we do `source $SAGE_ROOT/local/bin/sage-env`).


---

Comment by jdemeyer created at 2011-08-23 09:24:49

Replying to [comment:19 jdemeyer]:
> Why do we set `SAGE_ROOT` inside `sage-env`?  Given that `sage-env` is only ever called when we already know `SAGE_ROOT` (i.e. we do `source $SAGE_ROOT/local/bin/sage-env`).

Okay, I did find one counterexamples (I only looked in local/bin before):
 - The top-level Makefile calls `sage-env` without first setting `SAGE_ROOT`.

I also noticed that `data/extcode/sage/ext/mac-app/start-sage.sh` has its own `SAGE_ROOT`-detecting code but it probably shouldn't and should use `sage-env` instead.


---

Attachment

Shell script replacement for "readlink -f"


---

Comment by jdemeyer created at 2011-08-23 13:15:26

Changing status from needs_work to needs_review.


---

Comment by leif created at 2011-08-29 10:13:47

Replying to [comment:20 jdemeyer]:
> I also noticed that `data/extcode/sage/ext/mac-app/start-sage.sh` has its own `SAGE_ROOT`-detecting code but it probably shouldn't and should use `sage-env` instead.

It seems the MacOS X app wants just the opposite, i.e. to *not* resolve symbolic links, since the absolute, canonicalized path may frequently change.

Therefore it always creates (on start-up) the same, "constant" symbolic link from `/tmp/sage-mac-app` to the current, volatile `$SAGE_ROOT`, which can only work if the application is also actually _always_ built in (a real directory) `/tmp/sage-mac-app/` (such that no change of hardcoded paths is necessary).

Cf. #11755. In that case, the app should also define some special environment variable, such that `sage-env` (and perhaps also `sage`) can treat this specifically, namely not canonicalize `$SAGE_ROOT`.


---

Comment by jdemeyer created at 2011-09-19 08:52:59

Replying to [comment:25 leif]:
> Replying to [comment:20 jdemeyer]:
> > I also noticed that `data/extcode/sage/ext/mac-app/start-sage.sh` has its own `SAGE_ROOT`-detecting code but it probably shouldn't and should use `sage-env` instead.
> 
> It seems the MacOS X app wants just the opposite, i.e. to *not* resolve symbolic links, since the absolute, canonicalized path may frequently change.
> 
> Therefore it always creates (on start-up) the same, "constant" symbolic link from `/tmp/sage-mac-app` to the current, volatile `$SAGE_ROOT`, which can only work if the application is also actually _always_ built in (a real directory) `/tmp/sage-mac-app/` (such that no change of hardcoded paths is necessary).

The question is: why are things done this way?  It seems to me that the `/tmp/sage-mac-app` symlink is an ugly hack around a problem which can probably be solved in a better way.


---

Comment by jdemeyer created at 2011-10-29 18:43:34

Changing component from distribution to scripts.


---

Comment by leif created at 2011-10-30 05:58:21

What sense does it make to first call `resolvelinks()` and then finally do

```sh
SAGE_ROOT=`cd "$SAGE_ROOT" && pwd -P`
```

?

Also, why use all of `[ "x$foo" != "x" ]` (causing eye cancer), `[ -n "$foo" ]` and `[ "$foo" != "" ]`?

For `sage` at least, or any script that's run by `bash`, `[This is the Trac macro *-n $foo * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#-n $foo -macro)` or `[This is the Trac macro *$foo != "" * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#$foo != "" -macro)` does the job, and is by the way both safer and faster.


---

Comment by jdemeyer created at 2011-10-30 13:00:39

Replying to [comment:31 leif]:
> What sense does it make to first call `resolvelinks()` and then finally do
> {{{
> #!sh
> SAGE_ROOT=`cd "$SAGE_ROOT" && pwd -P`
> }}}
> ?
Because `resolvelinks` resolves symbolic links in the `sage` executable name, which is not a directory (so the `cd && pwd` trick does not work).


---

Attachment

Patch for $SAGE_ROOT/sage, SAGE_ROOT repository


---

Attachment

Patch for local/bin/sage-env, SCRIPTS repository


---

Comment by leif created at 2011-10-30 15:19:11

Replying to [comment:32 jdemeyer]:
> Replying to [comment:31 leif]:
> > What sense does it make to first call `resolvelinks()` and then finally do

```sh
SAGE_ROOT=`cd "$SAGE_ROOT" && pwd -P`
```

> > ?
> Because `resolvelinks` resolves symbolic links in the `sage` executable name, which is not a directory (so the `cd && pwd` trick does not work).

Of course it does.  You just have to
 * strip the program name, and
 * if no path remains after that, it's the current working directory, i.e. path=".".
 * `cd` to that path and do `pwd -P`.  Doesn't matter whether the path was relative or absolute.


---

Comment by jdemeyer created at 2011-10-30 17:03:56

Replying to [comment:33 leif]:
> You just have to
>  * strip the program name, and
>  * if no path remains after that, it's the current working directory, i.e. path=".".
>  * `cd` to that path and do `pwd -P`.  Doesn't matter whether the path was relative or absolute.
Again, this does not work if the executable itself is a symbolic link.

It could very well be that my solution is too complicated, but your solution is certainly too simple.


---

Comment by jdemeyer created at 2011-11-03 16:14:43

Milestone sage-4.7.3 deleted


---

Comment by jhpalmieri created at 2011-11-17 18:18:13

How widely available is `pwd -P`?  The GNU version of `pwd` does not recognize the `-P` option, but its man page says

```
       NOTE:  your shell may have its own version of pwd, which usually super‐
       sedes the version described here.  Please refer to your  shell’s  docu‐
       mentation for details about the options it supports.
```

This is what it says on sage.math, for example.  I use bash there, and the built-in pwd supports the `-P` option.  But do we need to worry about systems where there is no built-in pwd, and it is relying on the GNU version?  I have access to one such machine, and `pwd -P` doesn't work there, but I've never tried to build Sage on it.


---

Comment by jhpalmieri created at 2011-11-17 18:19:56

(Part of the problem is that on that other machine, I'm using tcsh and it doesn't let me run 'chsh'.)


---

Comment by jhpalmieri created at 2011-11-17 20:00:10

Has this been tested on OS X 10.4?  I believe that uses an older version of bash, and so we should make sure that it has the features used in the modifications to the `sage` shell script.


---

Comment by jhpalmieri created at 2011-11-17 23:11:10

This seems to work for me on various platforms.  If someone can test on OS X 10.4, I think we can give it a positive review.  (The Changelog I saw for bash doesn't discuss changes for expansions like `${pattern%word}` between versions 2 and 3 of bash, so I think it should work.)


---

Comment by jdemeyer created at 2011-11-18 08:28:37

Replying to [comment:39 jhpalmieri]:
> Has this been tested on OS X 10.4?
Yes, it works.

You are right that `/bin/pwd` does not always support `-P`, even on sage.math:

```
jdemeyer`@`sage:~$ /bin/pwd -P
/bin/pwd: invalid option -- P
Try `/bin/pwd --help' for more information.
```


But it seems `bash` always supports `pwd -P` as shell builtin, so we are safe.


---

Attachment


---

Comment by jdemeyer created at 2011-11-18 09:09:49

Added documentation patch [attachment:5852_doc.patch]


---

Comment by jhpalmieri created at 2011-11-23 17:49:57

This looks good to me.  I'm attaching a referee patch for the documentation part.  If that's okay, this can be changed to "positive review".


---

Attachment

main sage repo


---

Comment by jdemeyer created at 2011-11-23 20:59:31

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-11-26 10:31:33

Resolution: fixed
