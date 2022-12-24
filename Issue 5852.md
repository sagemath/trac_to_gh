# Issue 5852: [with patch, needs review] the detection of SAGE_ROOT in $SAGE_ROOT/sage script should expand symlinks recursively

archive/issues_005852.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @nexttime @kini\n\nCurrently, `$SAGE_ROOT/sage` uses (first among other alternate methods) `readlink -n` to detect the directory where the script lives (that's $SAGE_ROOT), but it should use `readlink -nf` to expand symlinks recursively.\n\nOtherwise, the symlink expansion may not be completely done, and `$SAGE_ROOT` could end up with a non-canonical dirname, which leads to issues with testing.\n\nHere's a way to reproduce an issue with the current script. For the example, my sage-3.4 installation lives in `/home/sage/sage-3.4`, and here's what happened to me:\n\n```\n/home/sage$ md5sum sage-3.4/sage\n4153919efe1edcd34ad7fa193122d679  sage-3.4/sage\n/home/sage$ ln -s sage-3.4 sage-3.4-symlink\n/home/sage$ ln -sf /home/sage/sage-3.4-symlink/sage /home/tornaria/bin/sage\n/home/sage$ type sage\nsage is hashed (/home/tornaria/bin/sage)\n/home/sage$ readlink `type -p sage`\n/home/sage/sage-3.4-symlink/sage\n/home/sage$ readlink -f `type -p sage`\n/home/sage/sage-3.4/sage\n```\n\n\nAs you can see, `readlink -n` expands once but doesn't cannonicalize the path to the `sage` script. And here's the symptom:\n\n```\n/home/sage$ sage -t sage-3.4/devel/sage-main/sage/all.py\nsage -t  \"sage-3.4/devel/sage-main/sage/all.py\"             \n  File \"./all.py\", line 18\n    from sage-3.4/devel/sage-main/sage/all import *\n             ^\nSyntaxError: invalid syntax\n\n\t [0.3 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  \"sage-3.4/devel/sage-main/sage/all.py\"\nTotal time for all tests: 0.3 seconds\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5852\n\n",
    "created_at": "2009-04-22T12:39:58Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "[with patch, needs review] the detection of SAGE_ROOT in $SAGE_ROOT/sage script should expand symlinks recursively",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5852",
    "user": "@tornaria"
}
```
Assignee: tbd

CC:  @nexttime @kini

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


Issue created by migration from https://trac.sagemath.org/ticket/5852





---

archive/issue_comments_046176.json:
```json
{
    "body": "Changing assignee from tbd to @tornaria.",
    "created_at": "2009-04-22T12:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46176",
    "user": "@tornaria"
}
```

Changing assignee from tbd to @tornaria.



---

archive/issue_comments_046177.json:
```json
{
    "body": "Changing component from algebra to misc.",
    "created_at": "2009-04-22T12:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46177",
    "user": "@tornaria"
}
```

Changing component from algebra to misc.



---

archive/issue_comments_046178.json:
```json
{
    "body": "Patching `$SAGE_ROOT/sage` with this:\n\n```\n--- sage-3.4/sage.orig\t2009-04-22 01:45:48.000000000 -0300\n+++ sage-3.4/sage\t2009-04-22 09:37:27.000000000 -0300\n@@ -14,6 +14,7 @@\n fi\n \n if [ \"$SAGE_ROOT\" = \".....\" ];  then\n+    SAGE_ROOT=`readlink -nf \"$0\" 2> /dev/null` || \\\n     SAGE_ROOT=`readlink -n \"$0\" 2> /dev/null` || \\\n     SAGE_ROOT=`realpath    \"$0\" 2> /dev/null` || \\\n     SAGE_ROOT=\"$0\"\n```\n\nfixes the issue, since now `$SAGE_ROOT` is correct.\n\nAccording to mabshoff, `readlink -f` doesn't work on some BSD; that's why I left the `readlink -n` test in the second line, but this should of course be tested on those BSD to make sure it doesn't cause a regression.",
    "created_at": "2009-04-22T12:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46178",
    "user": "@tornaria"
}
```

Patching `$SAGE_ROOT/sage` with this:

```
--- sage-3.4/sage.orig	2009-04-22 01:45:48.000000000 -0300
+++ sage-3.4/sage	2009-04-22 09:37:27.000000000 -0300
@@ -14,6 +14,7 @@
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

archive/issue_comments_046179.json:
```json
{
    "body": "On systems where \"readlink -f\" is supported, use that so the path for $SAGE_ROOT is fully canonicalized",
    "created_at": "2009-04-25T02:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46179",
    "user": "@tornaria"
}
```

On systems where "readlink -f" is supported, use that so the path for $SAGE_ROOT is fully canonicalized



---

archive/issue_comments_046180.json:
```json
{
    "body": "Attachment [trac_5852.patch](tarball://root/attachments/some-uuid/ticket5852/trac_5852.patch) by @nthiery created at 2009-04-28 00:18:36\n\nReplying to [comment:1 tornaria]:\n> Patching `$SAGE_ROOT/sage` with this:\n> {{{\n> --- sage-3.4/sage.orig\t2009-04-22 01:45:48.000000000 -0300\n> +++ sage-3.4/sage\t2009-04-22 09:37:27.000000000 -0300\n> `@``@` -14,6 +14,7 `@``@`\n>  fi\n>  \n>  if [ \"$SAGE_ROOT\" = \".....\" ];  then\n> +    SAGE_ROOT=`readlink -nf \"$0\" 2> /dev/null` || \\\n>      SAGE_ROOT=`readlink -n \"$0\" 2> /dev/null` || \\\n>      SAGE_ROOT=`realpath    \"$0\" 2> /dev/null` || \\\n>      SAGE_ROOT=\"$0\"\n> }}}\n> fixes the issue, since now `$SAGE_ROOT` is correct.\n> \n> According to mabshoff, `readlink -f` doesn't work on some BSD; that's why I left the `readlink -n` test in the second line, but this should of course be tested on those BSD to make sure it doesn't cause a regression.\n\nI can confirm that it does not work on MacOS X.10.4.11 (e.g. Anne Schilling's machine)\n\nA fix would be most welcome, as this makes sage -t make false reports of broken test files.",
    "created_at": "2009-04-28T00:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46180",
    "user": "@nthiery"
}
```

Attachment [trac_5852.patch](tarball://root/attachments/some-uuid/ticket5852/trac_5852.patch) by @nthiery created at 2009-04-28 00:18:36

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

archive/issue_comments_046181.json:
```json
{
    "body": "The readlink -f workaround is better than nothing, and should not make things worst for systems like BSD. I would vote for including it now, in waiting for a better solution.\nShould I set a positive review?\n\nBesides, what about adding a switch to sage -t to specify manually that the given file is inside or outside the sage source tree?\n\nThis would make a workaround for MacOX X, and also be occasionally be useful. For example, I often run tests from one sage source tree with another sage to compare the results.",
    "created_at": "2009-05-04T16:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46181",
    "user": "@nthiery"
}
```

The readlink -f workaround is better than nothing, and should not make things worst for systems like BSD. I would vote for including it now, in waiting for a better solution.
Should I set a positive review?

Besides, what about adding a switch to sage -t to specify manually that the given file is inside or outside the sage source tree?

This would make a workaround for MacOX X, and also be occasionally be useful. For example, I often run tests from one sage source tree with another sage to compare the results.



---

archive/issue_comments_046182.json:
```json
{
    "body": "Is there some equivalent of `readlink -f` that works in MacOS X?",
    "created_at": "2009-05-17T03:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46182",
    "user": "@tornaria"
}
```

Is there some equivalent of `readlink -f` that works in MacOS X?



---

archive/issue_comments_046183.json:
```json
{
    "body": "Note that the version of `readlink` which is included in fink (in package `debianutils`) supports the `-f` switch, so a mac with fink doesn't suffer from this issue (asuming `/sw/sbin` is before `/usr/bin` in the search PATH).",
    "created_at": "2009-05-17T03:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46183",
    "user": "@tornaria"
}
```

Note that the version of `readlink` which is included in fink (in package `debianutils`) supports the `-f` switch, so a mac with fink doesn't suffer from this issue (asuming `/sw/sbin` is before `/usr/bin` in the search PATH).



---

archive/issue_comments_046184.json:
```json
{
    "body": "See #6146 for fixing this on systems that don't support readlink -f.",
    "created_at": "2009-05-28T07:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46184",
    "user": "@williamstein"
}
```

See #6146 for fixing this on systems that don't support readlink -f.



---

archive/issue_comments_046185.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-28T07:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46185",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_046186.json:
```json
{
    "body": "Merged in 4.0.rc1.",
    "created_at": "2009-05-28T07:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46186",
    "user": "@mwhansen"
}
```

Merged in 4.0.rc1.



---

archive/issue_comments_046187.json:
```json
{
    "body": "Question.  Does \n\n```\nreadlink -n sage\n```\n\nwork on any platform?!  It gives an error on *both* OS X and Linux.  Why is it even there?!\n\n```\nOS X\nub243101:s wstein$ readlink -n sage\nub243101:s wstein$ echo $?\n1\n\nLinux:\nwstein@boxen:~/sage$ readlink -n sage\nwstein@boxen:~/sage$ echo $?\n1\n```\n\n\nI wonder who wrote this weird SAGE_ROOT code in the first place?  I wrote something a long time ago, but it bears no resemblance to the current code.\n\n\nBy the way, I've had reports of major failures caused by using `readlink -nf` by one user who has a symlink + nfs mount setup.  Their problems are solved by deleting the `readlink -nf` line.   Why don't we use realpath first and only if that doesn't work use something else?  It seems like realpath is the right choice, since it's supposed to \" converts each filename argument to an absolute pathname, which has no components that are symbolic links or the special\n       .  or ..  directory entries...  Please note that mostly the same functionality is provided by the \u2018-f\u2019 option.\"\n\nThere is no realpath on OS X, but that is ok since readlink doesn't work ever on OS X anyways, so no loss. \n\n -- William",
    "created_at": "2009-07-01T11:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46187",
    "user": "@williamstein"
}
```

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
wstein@boxen:~/sage$ readlink -n sage
wstein@boxen:~/sage$ echo $?
1
```


I wonder who wrote this weird SAGE_ROOT code in the first place?  I wrote something a long time ago, but it bears no resemblance to the current code.


By the way, I've had reports of major failures caused by using `readlink -nf` by one user who has a symlink + nfs mount setup.  Their problems are solved by deleting the `readlink -nf` line.   Why don't we use realpath first and only if that doesn't work use something else?  It seems like realpath is the right choice, since it's supposed to " converts each filename argument to an absolute pathname, which has no components that are symbolic links or the special
       .  or ..  directory entries...  Please note that mostly the same functionality is provided by the ‘-f’ option."

There is no realpath on OS X, but that is ok since readlink doesn't work ever on OS X anyways, so no loss. 

 -- William



---

archive/issue_comments_046188.json:
```json
{
    "body": "Replying to [comment:8 was]:\n> Question.  Does \n> {{{\n> readlink -n sage\n> }}}\n> work on any platform?!\n\nYes it does: it reads the content of a symbolic link. It succeeds if and only if the argument is actually a symbolic link, e.g.\n\n```\n~/sandbox$ ls -l\ntotal 0\n~/sandbox$ mkdir sage1\n~/sandbox$ readlink sage1 ; echo $?  ## fails b/c sage1 is not a symlink\n1\n~/sandbox$ ln -s sage1 sage2\n~/sandbox$ readlink sage2 ; echo $?  ## ok b/c sage2 is actually a symlink\nsage1\n0\n```\n\nThe option `-n` means to not print a trainling newline character; I don't think it really make a difference due to bash usual escaping rules.\n\n>  It gives an error on *both* OS X and Linux.  Why is it even there?!\n\nIt was there before the patch in this ticket, so that if `$0` (the path to the script one is running) is actually a symlink to the real path of the sage script, the detection of `SAGE_ROOT` works. On systems that support `-f`, that is a more complete solution, but the fallback was left for the benefit of systems where `readlink -f` does not work (e.g. OS X).\n\nFollowing my example above, here's an example where `-f` is needed:\n\n```\n~/sandbox$ ln -s sage2 sage3\ntornaria@bip:~/sandbox$ readlink -n sage3\nsage2tornaria@bip:~/sandbox$ readlink sage3\nsage2\ntornaria@bip:~/sandbox$ readlink -f sage3\n/home/tornaria/sandbox/sage1\n```\n\n\nThe other major case is when there are symlinks in some of the components of the path, those get canonicalized by `readlink -f`, but not by plain `readlink` (this leads to failures as shown in the description).\n\n\n> By the way, I've had reports of major failures caused by using `readlink -nf` by one user who has a symlink + nfs mount setup.  Their problems are solved by deleting the `readlink -nf` line.   Why don't we use realpath first and only if that doesn't work use something else?  It seems like realpath is the right choice, since it's supposed to \" converts each filename argument to an absolute pathname, which has no components that are symbolic links or the special\n>        .  or ..  directory entries...  Please note that mostly the same functionality is provided by the \u2018-f\u2019 option.\"\n\nCan you give a pointer to those? Not using `readlink -f` leads to major failures in testing, as described in the description of the ticket.\n\nDo you actually know that in those cases `realpath` works? It seems to me that both are implemented using `realpath(3)`, so they should be the same unless I'm missing something.\n\n> There is no realpath on OS X, but that is ok since readlink doesn't work ever on OS X anyways, so no loss. \n\nThere is no `realpath` in most systems I have access to (other than sage.math). In fact, `readlink` is pretty much standard (possibly POSIX), although `-f` option is not (a GNUism?). For GNU systems (e.g. linux), it comes bundled in coreutils, which means it will be available everywhere. OTOH, `realpath` comes in *optional* package `realpath`. Do you know of a system where `readlink -f` doesn't work but `realpath(1)` is available?\n\nOTOH, realpath(3) seems to be a POSIX standard, and it seems to be available on OS X:\n\n```\n$ nm /usr/lib/libc.dylib | grep realpath\n/usr/lib/libc.dylib(realpath.So):\n9003f1f0 T _realpath\n```\n\nso an alternative would be to compile our own `realpath` binary and somehow use it from the startup script. But we need a path to SAGE_ROOT so we can find SAGE_ROOT/local/bin/realpath... auch... (doesn't need to be canonical, though.... so we could use readlink a few times to get a path to the actual sage script, and then run `realpath` from there).",
    "created_at": "2009-07-01T13:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46188",
    "user": "@tornaria"
}
```

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
tornaria@bip:~/sandbox$ readlink -n sage3
sage2tornaria@bip:~/sandbox$ readlink sage3
sage2
tornaria@bip:~/sandbox$ readlink -f sage3
/home/tornaria/sandbox/sage1
```


The other major case is when there are symlinks in some of the components of the path, those get canonicalized by `readlink -f`, but not by plain `readlink` (this leads to failures as shown in the description).


> By the way, I've had reports of major failures caused by using `readlink -nf` by one user who has a symlink + nfs mount setup.  Their problems are solved by deleting the `readlink -nf` line.   Why don't we use realpath first and only if that doesn't work use something else?  It seems like realpath is the right choice, since it's supposed to " converts each filename argument to an absolute pathname, which has no components that are symbolic links or the special
>        .  or ..  directory entries...  Please note that mostly the same functionality is provided by the ‘-f’ option."

Can you give a pointer to those? Not using `readlink -f` leads to major failures in testing, as described in the description of the ticket.

Do you actually know that in those cases `realpath` works? It seems to me that both are implemented using `realpath(3)`, so they should be the same unless I'm missing something.

> There is no realpath on OS X, but that is ok since readlink doesn't work ever on OS X anyways, so no loss. 

There is no `realpath` in most systems I have access to (other than sage.math). In fact, `readlink` is pretty much standard (possibly POSIX), although `-f` option is not (a GNUism?). For GNU systems (e.g. linux), it comes bundled in coreutils, which means it will be available everywhere. OTOH, `realpath` comes in *optional* package `realpath`. Do you know of a system where `readlink -f` doesn't work but `realpath(1)` is available?

OTOH, realpath(3) seems to be a POSIX standard, and it seems to be available on OS X:

```
$ nm /usr/lib/libc.dylib | grep realpath
/usr/lib/libc.dylib(realpath.So):
9003f1f0 T _realpath
```

so an alternative would be to compile our own `realpath` binary and somehow use it from the startup script. But we need a path to SAGE_ROOT so we can find SAGE_ROOT/local/bin/realpath... auch... (doesn't need to be canonical, though.... so we could use readlink a few times to get a path to the actual sage script, and then run `realpath` from there).



---

archive/issue_comments_046189.json:
```json
{
    "body": "It's possible that this ticket should be reverted until a major bug it causes is fixed.   \n\nThe reason for this ticket in the first place was the following, as given in the ticket description:\n\n```\n/home/sage$ md5sum sage-3.4/sage\n4153919efe1edcd34ad7fa193122d679  sage-3.4/sage\n/home/sage$ ln -s sage-3.4 sage-3.4-symlink\n/home/sage$ ln -sf /home/sage/sage-3.4-symlink/sage /home/tornaria/bin/sage\n/home/sage$ type sage\n```\n\n\nNotice the symlink of the Sage script\n\n```\n/home/sage$ ln -sf /home/sage/sage-3.4-symlink/sage /home/tornaria/bin/sage\n```\n\n\nFor the record, this is *not* how I meant the sage script is meant to be used.  I bet this isn't documented, but it should be.  The script should never be used that way.  Instead one should do\n\n```\n/home/sage$ cp /home/sage/sage-3.4-symlink/sage /home/tornaria/bin/sage\n```\n\nand then edit the copied script to explicitly point to the ROOT.   It was never my intention for somebody to run the sage script unmodified outside of SAGE_ROOT.    Me not intending this means that elsewhere in the Sage build/test system this assumption is made, and the workaround on this ticket actually seriously breaks things for some users. \n\nThe change in this ticket causes serious breakage for people whose home directory is NFS mounted, and for which their Sage build is on another volume that is symlinked from their home directory. i.e., this sort of setup:\n\n```\n    cd ~wstein    # my home directory is NFS mounted.\n    mkdir /tmp/wstein       # /tmp is a local disk\n    ln -s /tmp/wstein sage-build\n    cd sage-build    # \n    # build sage here, doctesting fails completely\n```\n\n\nI'm doing a test build for myself to confirm that this happens, and if so and I can't figure out how to fix this promptly (maybe I will be able to), then we have to revert this change, and document that one can't just symlink the sage script out.",
    "created_at": "2009-07-01T23:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46189",
    "user": "@williamstein"
}
```

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

archive/issue_comments_046190.json:
```json
{
    "body": "Replying to [comment:10 was]:\n> It's possible that this ticket should be reverted until a major bug it causes is fixed.\n> [...]\n> For the record, this is *not* how I meant the sage script is meant to be used.  I bet this isn't documented, but it should be.  The script should never be used that way.  Instead one should do\n> {{{\n> /home/sage$ cp /home/sage/sage-3.4-symlink/sage /home/tornaria/bin/sage\n> }}}\n> and then edit the copied script to explicitly point to the ROOT.   It was never my intention for somebody to run the sage script unmodified outside of SAGE_ROOT.    Me not intending this means that elsewhere in the Sage build/test system this assumption is made, and the workaround on this ticket actually seriously breaks things for some users. \n\nIf you only use the script in *that* way, then the\n\n```\nif [ \"$SAGE_ROOT\" = \".....\" ];  then\n```\n\nbranch would never be taken, and as the patch in this ticket only touches this branch, it can't break anything.\n\nIn practice, it is much more convenient to just use a symlink to the script, if it can be worked out. Before this patch, it turned out that the real, canonical path for SAGE_ROOT could be identified incorrectly, and *this* causes doctesting to fail.\n\n> The change in this ticket causes serious breakage for people whose home directory is NFS mounted, and for which their Sage build is on another volume that is symlinked from their home directory. i.e., this sort of setup:\n> {{{\n>     cd ~wstein    # my home directory is NFS mounted.\n>     mkdir /tmp/wstein       # /tmp is a local disk\n>     ln -s /tmp/wstein sage-build\n>     cd sage-build    # \n>     # build sage here, doctesting fails completely\n> }}}\n> \n> I'm doing a test build for myself to confirm that this happens, and if so and I can't figure out how to fix this promptly (maybe I will be able to), then we have to revert this change, and document that one can't just symlink the sage script out. \n\nThis sort of setup is *exactly* what used to cause breakage for me, because the `SAGE_ROOT` was incorrectly computed (to a non-canonical path). What would you expect `SAGE_ROOT` to be computed to, other than the canonical path? e.g., continuing your example above:\n\n```\n    cd ~wstein/sage-build\n    tar xvf sage-nnn.tar\n    cd sage-nnn\n    ./sage -sh\n    echo \"$SAGE_ROOT\"\n```\n\nAre you expecting SAGE_ROOT above to be \"/home/wstein/sage-build/sage-nnn/\", or \"/tmp/wstein/sage-nnn\" ?\n\nBefore the patch, it was the former, non canonical path; after the patch, it is the latter, which is IMO the correct canonical path. When SAGE_ROOT is non-canonical, running doctests for files in the sage library fails b/c they are not recognized as part of the sage library, etc.\n    \nI don't see how the fact that this is NFS mounted could be relevant to the issue.",
    "created_at": "2009-07-01T23:58:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46190",
    "user": "@tornaria"
}
```

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

archive/issue_comments_046191.json:
```json
{
    "body": "The problem with this patch isn't that it is \"wrong\" (which is what you're arguing with me about above).  It is that it seriously breaks Sage, hence it must be reverted or the problem it causes must be fixed.  I had a look, and the problem is here in local/bin/sage-doctest:\n\n```\n        library_code = True\n        ext = os.path.splitext(argv[1])[1]\n        if ext in ['.spyx', '.sage'] or \\\n                 not (SAGE_ROOT.strip('/') + '/devel' in os.path.abspath(argv[1])):\n            library_code = False\n```\n\nThe problem is that the library_code variable is being set to False for all the code that *is* in the library.   It is being set to false because if one does\n\n```\n   sage -t \"/home/wstein/sage-build/sage-nnn/...\"\n```\n\nthen argv[1] is not first canonicalized, which messes everything up completely.\n\nSo for this ticket to be in (which I agree with at some point), one needs to factor out this path caonicalization, and make sure it is applied everywhere (e.g,. in sage-doctest).  There could be many other places where subtle problems arise -- I don't know. \n\nFor now, this needs to be reverted.",
    "created_at": "2009-07-04T11:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46191",
    "user": "@williamstein"
}
```

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

archive/issue_comments_046192.json:
```json
{
    "body": "I have reverted this patch in sage-4.1.rc0, and I'm reopening the ticket.",
    "created_at": "2009-07-04T19:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46192",
    "user": "@rlmill"
}
```

I have reverted this patch in sage-4.1.rc0, and I'm reopening the ticket.



---

archive/issue_comments_046193.json:
```json
{
    "body": "Changing component from misc to distribution.",
    "created_at": "2009-07-04T19:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46193",
    "user": "@rlmill"
}
```

Changing component from misc to distribution.



---

archive/issue_comments_046194.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-07-04T19:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46194",
    "user": "@rlmill"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_046195.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-07-04T19:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46195",
    "user": "@rlmill"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_046196.json:
```json
{
    "body": "Has the issue with `sage-doctest` been resolved?  The code now says\n\n```python\n        dev_path = os.path.realpath(os.path.join(SAGE_ROOT, 'devel'))\n        our_path = os.path.realpath(argv[1])\n\n        if not force_lib and (ext in ['.spyx', '.sage'] or\n                              not dev_path in our_path):\n            library_code = False\n```\n\nSince `os.path.realpath` is used twice, shouldn't this be okay?  If not, another option is to use [os.path.samefile](http://docs.python.org/library/os.path.html#os.path.samefile).",
    "created_at": "2011-08-19T03:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46196",
    "user": "@jhpalmieri"
}
```

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

archive/issue_comments_046197.json:
```json
{
    "body": "Attachment [realpath_bash.sh](tarball://root/attachments/some-uuid/ticket5852/realpath_bash.sh) by @jdemeyer created at 2011-08-19 17:31:34\n\nShell script replacement for \"readlink -f\"",
    "created_at": "2011-08-19T17:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46197",
    "user": "@jdemeyer"
}
```

Attachment [realpath_bash.sh](tarball://root/attachments/some-uuid/ticket5852/realpath_bash.sh) by @jdemeyer created at 2011-08-19 17:31:34

Shell script replacement for "readlink -f"



---

archive/issue_comments_046198.json:
```json
{
    "body": "Changing assignee from @tornaria to @jdemeyer.",
    "created_at": "2011-08-23T09:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46198",
    "user": "@jdemeyer"
}
```

Changing assignee from @tornaria to @jdemeyer.



---

archive/issue_comments_046199.json:
```json
{
    "body": "Why do we set `SAGE_ROOT` inside `sage-env`?  Given that `sage-env` is only ever called when we already know `SAGE_ROOT` (i.e. we do `source $SAGE_ROOT/local/bin/sage-env`).",
    "created_at": "2011-08-23T09:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46199",
    "user": "@jdemeyer"
}
```

Why do we set `SAGE_ROOT` inside `sage-env`?  Given that `sage-env` is only ever called when we already know `SAGE_ROOT` (i.e. we do `source $SAGE_ROOT/local/bin/sage-env`).



---

archive/issue_comments_046200.json:
```json
{
    "body": "Replying to [comment:19 jdemeyer]:\n> Why do we set `SAGE_ROOT` inside `sage-env`?  Given that `sage-env` is only ever called when we already know `SAGE_ROOT` (i.e. we do `source $SAGE_ROOT/local/bin/sage-env`).\n\nOkay, I did find one counterexamples (I only looked in local/bin before):\n- The top-level Makefile calls `sage-env` without first setting `SAGE_ROOT`.\n\nI also noticed that `data/extcode/sage/ext/mac-app/start-sage.sh` has its own `SAGE_ROOT`-detecting code but it probably shouldn't and should use `sage-env` instead.",
    "created_at": "2011-08-23T09:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46200",
    "user": "@jdemeyer"
}
```

Replying to [comment:19 jdemeyer]:
> Why do we set `SAGE_ROOT` inside `sage-env`?  Given that `sage-env` is only ever called when we already know `SAGE_ROOT` (i.e. we do `source $SAGE_ROOT/local/bin/sage-env`).

Okay, I did find one counterexamples (I only looked in local/bin before):
- The top-level Makefile calls `sage-env` without first setting `SAGE_ROOT`.

I also noticed that `data/extcode/sage/ext/mac-app/start-sage.sh` has its own `SAGE_ROOT`-detecting code but it probably shouldn't and should use `sage-env` instead.



---

archive/issue_comments_046201.json:
```json
{
    "body": "Attachment [resolvelinks.sh](tarball://root/attachments/some-uuid/ticket5852/resolvelinks.sh) by @jdemeyer created at 2011-08-23 12:01:55\n\nShell script replacement for \"readlink -f\"",
    "created_at": "2011-08-23T12:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46201",
    "user": "@jdemeyer"
}
```

Attachment [resolvelinks.sh](tarball://root/attachments/some-uuid/ticket5852/resolvelinks.sh) by @jdemeyer created at 2011-08-23 12:01:55

Shell script replacement for "readlink -f"



---

archive/issue_comments_046202.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-08-23T13:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46202",
    "user": "@jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_046203.json:
```json
{
    "body": "Replying to [comment:20 jdemeyer]:\n> I also noticed that `data/extcode/sage/ext/mac-app/start-sage.sh` has its own `SAGE_ROOT`-detecting code but it probably shouldn't and should use `sage-env` instead.\n\nIt seems the MacOS X app wants just the opposite, i.e. to **not** resolve symbolic links, since the absolute, canonicalized path may frequently change.\n\nTherefore it always creates (on start-up) the same, \"constant\" symbolic link from `/tmp/sage-mac-app` to the current, volatile `$SAGE_ROOT`, which can only work if the application is also actually *always* built in (a real directory) `/tmp/sage-mac-app/` (such that no change of hardcoded paths is necessary).\n\nCf. #11755. In that case, the app should also define some special environment variable, such that `sage-env` (and perhaps also `sage`) can treat this specifically, namely not canonicalize `$SAGE_ROOT`.",
    "created_at": "2011-08-29T10:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46203",
    "user": "@nexttime"
}
```

Replying to [comment:20 jdemeyer]:
> I also noticed that `data/extcode/sage/ext/mac-app/start-sage.sh` has its own `SAGE_ROOT`-detecting code but it probably shouldn't and should use `sage-env` instead.

It seems the MacOS X app wants just the opposite, i.e. to **not** resolve symbolic links, since the absolute, canonicalized path may frequently change.

Therefore it always creates (on start-up) the same, "constant" symbolic link from `/tmp/sage-mac-app` to the current, volatile `$SAGE_ROOT`, which can only work if the application is also actually *always* built in (a real directory) `/tmp/sage-mac-app/` (such that no change of hardcoded paths is necessary).

Cf. #11755. In that case, the app should also define some special environment variable, such that `sage-env` (and perhaps also `sage`) can treat this specifically, namely not canonicalize `$SAGE_ROOT`.



---

archive/issue_comments_046204.json:
```json
{
    "body": "Replying to [comment:25 leif]:\n> Replying to [comment:20 jdemeyer]:\n> > I also noticed that `data/extcode/sage/ext/mac-app/start-sage.sh` has its own `SAGE_ROOT`-detecting code but it probably shouldn't and should use `sage-env` instead.\n> \n> It seems the MacOS X app wants just the opposite, i.e. to **not** resolve symbolic links, since the absolute, canonicalized path may frequently change.\n> \n> Therefore it always creates (on start-up) the same, \"constant\" symbolic link from `/tmp/sage-mac-app` to the current, volatile `$SAGE_ROOT`, which can only work if the application is also actually *always* built in (a real directory) `/tmp/sage-mac-app/` (such that no change of hardcoded paths is necessary).\n\nThe question is: why are things done this way?  It seems to me that the `/tmp/sage-mac-app` symlink is an ugly hack around a problem which can probably be solved in a better way.",
    "created_at": "2011-09-19T08:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46204",
    "user": "@jdemeyer"
}
```

Replying to [comment:25 leif]:
> Replying to [comment:20 jdemeyer]:
> > I also noticed that `data/extcode/sage/ext/mac-app/start-sage.sh` has its own `SAGE_ROOT`-detecting code but it probably shouldn't and should use `sage-env` instead.
> 
> It seems the MacOS X app wants just the opposite, i.e. to **not** resolve symbolic links, since the absolute, canonicalized path may frequently change.
> 
> Therefore it always creates (on start-up) the same, "constant" symbolic link from `/tmp/sage-mac-app` to the current, volatile `$SAGE_ROOT`, which can only work if the application is also actually *always* built in (a real directory) `/tmp/sage-mac-app/` (such that no change of hardcoded paths is necessary).

The question is: why are things done this way?  It seems to me that the `/tmp/sage-mac-app` symlink is an ugly hack around a problem which can probably be solved in a better way.



---

archive/issue_comments_046205.json:
```json
{
    "body": "Changing component from distribution to scripts.",
    "created_at": "2011-10-29T18:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46205",
    "user": "@jdemeyer"
}
```

Changing component from distribution to scripts.



---

archive/issue_comments_046206.json:
```json
{
    "body": "What sense does it make to first call `resolvelinks()` and then finally do\n\n```sh\nSAGE_ROOT=`cd \"$SAGE_ROOT\" && pwd -P`\n```\n\n?\n\nAlso, why use all of `[ \"x$foo\" != \"x\" ]` (causing eye cancer), `[ -n \"$foo\" ]` and `[ \"$foo\" != \"\" ]`?\n\nFor `sage` at least, or any script that's run by `bash`, `[This is the Trac macro *-n $foo * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#-n $foo -macro)` or `[This is the Trac macro *$foo != \"\" * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#$foo != \"\" -macro)` does the job, and is by the way both safer and faster.",
    "created_at": "2011-10-30T05:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46206",
    "user": "@nexttime"
}
```

What sense does it make to first call `resolvelinks()` and then finally do

```sh
SAGE_ROOT=`cd "$SAGE_ROOT" && pwd -P`
```

?

Also, why use all of `[ "x$foo" != "x" ]` (causing eye cancer), `[ -n "$foo" ]` and `[ "$foo" != "" ]`?

For `sage` at least, or any script that's run by `bash`, `[This is the Trac macro *-n $foo * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#-n $foo -macro)` or `[This is the Trac macro *$foo != "" * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#$foo != "" -macro)` does the job, and is by the way both safer and faster.



---

archive/issue_comments_046207.json:
```json
{
    "body": "Replying to [comment:31 leif]:\n> What sense does it make to first call `resolvelinks()` and then finally do\n> {{{\n> #!sh\n> SAGE_ROOT=`cd \"$SAGE_ROOT\" && pwd -P`\n> }}}\n> ?\nBecause `resolvelinks` resolves symbolic links in the `sage` executable name, which is not a directory (so the `cd && pwd` trick does not work).",
    "created_at": "2011-10-30T13:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46207",
    "user": "@jdemeyer"
}
```

Replying to [comment:31 leif]:
> What sense does it make to first call `resolvelinks()` and then finally do
> {{{
> #!sh
> SAGE_ROOT=`cd "$SAGE_ROOT" && pwd -P`
> }}}
> ?
Because `resolvelinks` resolves symbolic links in the `sage` executable name, which is not a directory (so the `cd && pwd` trick does not work).



---

archive/issue_comments_046208.json:
```json
{
    "body": "Attachment [5852_sage_root.patch](tarball://root/attachments/some-uuid/ticket5852/5852_sage_root.patch) by @jdemeyer created at 2011-10-30 13:08:20\n\nPatch for $SAGE_ROOT/sage, SAGE_ROOT repository",
    "created_at": "2011-10-30T13:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46208",
    "user": "@jdemeyer"
}
```

Attachment [5852_sage_root.patch](tarball://root/attachments/some-uuid/ticket5852/5852_sage_root.patch) by @jdemeyer created at 2011-10-30 13:08:20

Patch for $SAGE_ROOT/sage, SAGE_ROOT repository



---

archive/issue_comments_046209.json:
```json
{
    "body": "Attachment [5852_scripts.patch](tarball://root/attachments/some-uuid/ticket5852/5852_scripts.patch) by @jdemeyer created at 2011-10-30 13:08:29\n\nPatch for local/bin/sage-env, SCRIPTS repository",
    "created_at": "2011-10-30T13:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46209",
    "user": "@jdemeyer"
}
```

Attachment [5852_scripts.patch](tarball://root/attachments/some-uuid/ticket5852/5852_scripts.patch) by @jdemeyer created at 2011-10-30 13:08:29

Patch for local/bin/sage-env, SCRIPTS repository



---

archive/issue_comments_046210.json:
```json
{
    "body": "Replying to [comment:32 jdemeyer]:\n> Replying to [comment:31 leif]:\n> > What sense does it make to first call `resolvelinks()` and then finally do\n\n```sh\nSAGE_ROOT=`cd \"$SAGE_ROOT\" && pwd -P`\n```\n\n> > ?\n> Because `resolvelinks` resolves symbolic links in the `sage` executable name, which is not a directory (so the `cd && pwd` trick does not work).\n\nOf course it does.  You just have to\n* strip the program name, and\n* if no path remains after that, it's the current working directory, i.e. path=\".\".\n* `cd` to that path and do `pwd -P`.  Doesn't matter whether the path was relative or absolute.",
    "created_at": "2011-10-30T15:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46210",
    "user": "@nexttime"
}
```

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

archive/issue_comments_046211.json:
```json
{
    "body": "Replying to [comment:33 leif]:\n> You just have to\n>  * strip the program name, and\n>  * if no path remains after that, it's the current working directory, i.e. path=\".\".\n>  * `cd` to that path and do `pwd -P`.  Doesn't matter whether the path was relative or absolute.\nAgain, this does not work if the executable itself is a symbolic link.\n\nIt could very well be that my solution is too complicated, but your solution is certainly too simple.",
    "created_at": "2011-10-30T17:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46211",
    "user": "@jdemeyer"
}
```

Replying to [comment:33 leif]:
> You just have to
>  * strip the program name, and
>  * if no path remains after that, it's the current working directory, i.e. path=".".
>  * `cd` to that path and do `pwd -P`.  Doesn't matter whether the path was relative or absolute.
Again, this does not work if the executable itself is a symbolic link.

It could very well be that my solution is too complicated, but your solution is certainly too simple.



---

archive/issue_comments_046212.json:
```json
{
    "body": "Milestone sage-4.7.3 deleted",
    "created_at": "2011-11-03T16:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46212",
    "user": "@jdemeyer"
}
```

Milestone sage-4.7.3 deleted



---

archive/issue_comments_046213.json:
```json
{
    "body": "How widely available is `pwd -P`?  The GNU version of `pwd` does not recognize the `-P` option, but its man page says\n\n```\n       NOTE:  your shell may have its own version of pwd, which usually super\u2010\n       sedes the version described here.  Please refer to your  shell\u2019s  docu\u2010\n       mentation for details about the options it supports.\n```\n\nThis is what it says on sage.math, for example.  I use bash there, and the built-in pwd supports the `-P` option.  But do we need to worry about systems where there is no built-in pwd, and it is relying on the GNU version?  I have access to one such machine, and `pwd -P` doesn't work there, but I've never tried to build Sage on it.",
    "created_at": "2011-11-17T18:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46213",
    "user": "@jhpalmieri"
}
```

How widely available is `pwd -P`?  The GNU version of `pwd` does not recognize the `-P` option, but its man page says

```
       NOTE:  your shell may have its own version of pwd, which usually super‐
       sedes the version described here.  Please refer to your  shell’s  docu‐
       mentation for details about the options it supports.
```

This is what it says on sage.math, for example.  I use bash there, and the built-in pwd supports the `-P` option.  But do we need to worry about systems where there is no built-in pwd, and it is relying on the GNU version?  I have access to one such machine, and `pwd -P` doesn't work there, but I've never tried to build Sage on it.



---

archive/issue_comments_046214.json:
```json
{
    "body": "(Part of the problem is that on that other machine, I'm using tcsh and it doesn't let me run 'chsh'.)",
    "created_at": "2011-11-17T18:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46214",
    "user": "@jhpalmieri"
}
```

(Part of the problem is that on that other machine, I'm using tcsh and it doesn't let me run 'chsh'.)



---

archive/issue_comments_046215.json:
```json
{
    "body": "Has this been tested on OS X 10.4?  I believe that uses an older version of bash, and so we should make sure that it has the features used in the modifications to the `sage` shell script.",
    "created_at": "2011-11-17T20:00:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46215",
    "user": "@jhpalmieri"
}
```

Has this been tested on OS X 10.4?  I believe that uses an older version of bash, and so we should make sure that it has the features used in the modifications to the `sage` shell script.



---

archive/issue_comments_046216.json:
```json
{
    "body": "This seems to work for me on various platforms.  If someone can test on OS X 10.4, I think we can give it a positive review.  (The Changelog I saw for bash doesn't discuss changes for expansions like `${pattern%word}` between versions 2 and 3 of bash, so I think it should work.)",
    "created_at": "2011-11-17T23:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46216",
    "user": "@jhpalmieri"
}
```

This seems to work for me on various platforms.  If someone can test on OS X 10.4, I think we can give it a positive review.  (The Changelog I saw for bash doesn't discuss changes for expansions like `${pattern%word}` between versions 2 and 3 of bash, so I think it should work.)



---

archive/issue_comments_046217.json:
```json
{
    "body": "Replying to [comment:39 jhpalmieri]:\n> Has this been tested on OS X 10.4?\nYes, it works.\n\nYou are right that `/bin/pwd` does not always support `-P`, even on sage.math:\n\n```\njdemeyer@sage:~$ /bin/pwd -P\n/bin/pwd: invalid option -- P\nTry `/bin/pwd --help' for more information.\n```\n\n\nBut it seems `bash` always supports `pwd -P` as shell builtin, so we are safe.",
    "created_at": "2011-11-18T08:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46217",
    "user": "@jdemeyer"
}
```

Replying to [comment:39 jhpalmieri]:
> Has this been tested on OS X 10.4?
Yes, it works.

You are right that `/bin/pwd` does not always support `-P`, even on sage.math:

```
jdemeyer@sage:~$ /bin/pwd -P
/bin/pwd: invalid option -- P
Try `/bin/pwd --help' for more information.
```


But it seems `bash` always supports `pwd -P` as shell builtin, so we are safe.



---

archive/issue_comments_046218.json:
```json
{
    "body": "Attachment [5852_doc.patch](tarball://root/attachments/some-uuid/ticket5852/5852_doc.patch) by @jdemeyer created at 2011-11-18 09:09:12",
    "created_at": "2011-11-18T09:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46218",
    "user": "@jdemeyer"
}
```

Attachment [5852_doc.patch](tarball://root/attachments/some-uuid/ticket5852/5852_doc.patch) by @jdemeyer created at 2011-11-18 09:09:12



---

archive/issue_comments_046219.json:
```json
{
    "body": "Added documentation patch [attachment:5852_doc.patch]",
    "created_at": "2011-11-18T09:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46219",
    "user": "@jdemeyer"
}
```

Added documentation patch [attachment:5852_doc.patch]



---

archive/issue_comments_046220.json:
```json
{
    "body": "This looks good to me.  I'm attaching a referee patch for the documentation part.  If that's okay, this can be changed to \"positive review\".",
    "created_at": "2011-11-23T17:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46220",
    "user": "@jhpalmieri"
}
```

This looks good to me.  I'm attaching a referee patch for the documentation part.  If that's okay, this can be changed to "positive review".



---

archive/issue_comments_046221.json:
```json
{
    "body": "Attachment [trac_5852-doc-referee.patch](tarball://root/attachments/some-uuid/ticket5852/trac_5852-doc-referee.patch) by @jhpalmieri created at 2011-11-23 17:50:14\n\nmain sage repo",
    "created_at": "2011-11-23T17:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46221",
    "user": "@jhpalmieri"
}
```

Attachment [trac_5852-doc-referee.patch](tarball://root/attachments/some-uuid/ticket5852/trac_5852-doc-referee.patch) by @jhpalmieri created at 2011-11-23 17:50:14

main sage repo



---

archive/issue_comments_046222.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-11-23T20:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46222",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_046223.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-11-26T10:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5852#issuecomment-46223",
    "user": "@jdemeyer"
}
```

Resolution: fixed
