# Issue 1293: sage is too big!

archive/issues_001293.json:
```json
{
    "body": "Assignee: mabshoff\n\nI was told that SAGE did use less memory than Maple or Mathematica. I did check on sage.math.washington.edu:\n\n```\nzimmerma@sage:~$ du -s /usr/local/maple10\n388908  /usr/local/maple10\n\nzimmerma@sage:~$ du -s /usr/local/mathematica-5.2\n641016  /usr/local/mathematica-5.2\n\nsage:/tmp/zimmerma/sage-2.8.14> make install DESTDIR=/tmp/zimmerma/sage-2.8.14-\\\ninstall\nsage:/tmp/zimmerma/sage-2.8.14> du -s /tmp/zimmerma/sage-2.8.14-install\n1237280 /tmp/zimmerma/sage-2.8.14-install\n```\n\nI can understand that the SAGE developers need all the source and binaries installed, but I wish a minimal\nversion for the simple user that would use at most the same amount of memory than Maple or Mathematica,\nnot 2 times or 3 times more!\n\nIssue created by migration from https://trac.sagemath.org/ticket/1293\n\n",
    "created_at": "2007-11-27T17:40:01Z",
    "labels": [
        "component: distribution"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage is too big!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1293",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: mabshoff

I was told that SAGE did use less memory than Maple or Mathematica. I did check on sage.math.washington.edu:

```
zimmerma@sage:~$ du -s /usr/local/maple10
388908  /usr/local/maple10

zimmerma@sage:~$ du -s /usr/local/mathematica-5.2
641016  /usr/local/mathematica-5.2

sage:/tmp/zimmerma/sage-2.8.14> make install DESTDIR=/tmp/zimmerma/sage-2.8.14-\
install
sage:/tmp/zimmerma/sage-2.8.14> du -s /tmp/zimmerma/sage-2.8.14-install
1237280 /tmp/zimmerma/sage-2.8.14-install
```

I can understand that the SAGE developers need all the source and binaries installed, but I wish a minimal
version for the simple user that would use at most the same amount of memory than Maple or Mathematica,
not 2 times or 3 times more!

Issue created by migration from https://trac.sagemath.org/ticket/1293





---

archive/issue_comments_008092.json:
```json
{
    "body": "Well, your numbers are slighly inflated because \"make install\" is still experimental and copies fata not needed:\n\n```\nmabshoff@sage:/tmp/Work-mabshoff/size$ du -sch sage-2.8.13-use_this_on_sage_dot_math-x86_64-Linux\n802M    sage-2.8.13-use_this_on_sage_dot_math-x86_64-Linux\n```\n\nThe current 2.8.13 binary expands to 802 MB which is still too large, but somewhat smaller than the 1.2GB you had.\n\nBut it would be a good thing to slim down the installed Sage if it is possible.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-27T18:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1293#issuecomment-8092",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, your numbers are slighly inflated because "make install" is still experimental and copies fata not needed:

```
mabshoff@sage:/tmp/Work-mabshoff/size$ du -sch sage-2.8.13-use_this_on_sage_dot_math-x86_64-Linux
802M    sage-2.8.13-use_this_on_sage_dot_math-x86_64-Linux
```

The current 2.8.13 binary expands to 802 MB which is still too large, but somewhat smaller than the 1.2GB you had.

But it would be a good thing to slim down the installed Sage if it is possible.

Cheers,

Michael



---

archive/issue_comments_008093.json:
```json
{
    "body": "Some numbers:\n\n* a fresh *2.8.13* is **804M** (binary release, i.e. `spkg` is basically empty)\n* after *strip*ing all executable files + `*.so` we are down to **655M**\n* if we - as an experiment only, this shouldn't be done in real lift because it breaks updates etc. - also remove `*.a` we are down to **536M**\n* of this **149M** are in `devel` and **344M** are in `local`",
    "created_at": "2007-12-06T16:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1293#issuecomment-8093",
    "user": "https://github.com/malb"
}
```

Some numbers:

* a fresh *2.8.13* is **804M** (binary release, i.e. `spkg` is basically empty)
* after *strip*ing all executable files + `*.so` we are down to **655M**
* if we - as an experiment only, this shouldn't be done in real lift because it breaks updates etc. - also remove `*.a` we are down to **536M**
* of this **149M** are in `devel` and **344M** are in `local`



---

archive/issue_comments_008094.json:
```json
{
    "body": "Here are the brand new figures for sage-2.9 on a 64-bit computer (Opteron under Fedora7):\n\n```\nachille% du -s /usr/local/sage-2.9\n1517144 /usr/local/sage-2.9\n```\n\nIf the figures are comparable on sage.math (which I assume) this is 2.4 times larger than Mathematica and 3.9 times\nlarger than Maple.",
    "created_at": "2007-12-17T12:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1293#issuecomment-8094",
    "user": "https://github.com/zimmermann6"
}
```

Here are the brand new figures for sage-2.9 on a 64-bit computer (Opteron under Fedora7):

```
achille% du -s /usr/local/sage-2.9
1517144 /usr/local/sage-2.9
```

If the figures are comparable on sage.math (which I assume) this is 2.4 times larger than Mathematica and 3.9 times
larger than Maple.



---

archive/issue_comments_008095.json:
```json
{
    "body": "Some new datapoints:\n* 3.1.3.alpha1 is **1.7GB** after compilation (64-bit Linux),\n* it is safe to delete all spkgs in `$SAGE_ROOT/spkgs/standard`,\n* it is safe to strip executables,\n* it is safe to strip shared libraries with `-g -R .comment -R .note`,\n* one may delete all of `$SAGE_ROOT/devel/sage/build` except for the `sage` subdirectory.\n\nThe result is **1.1GB** which is still massive. I'm building with `-Os` now to see how much of a difference that makes.",
    "created_at": "2008-09-28T15:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1293#issuecomment-8095",
    "user": "https://github.com/malb"
}
```

Some new datapoints:
* 3.1.3.alpha1 is **1.7GB** after compilation (64-bit Linux),
* it is safe to delete all spkgs in `$SAGE_ROOT/spkgs/standard`,
* it is safe to strip executables,
* it is safe to strip shared libraries with `-g -R .comment -R .note`,
* one may delete all of `$SAGE_ROOT/devel/sage/build` except for the `sage` subdirectory.

The result is **1.1GB** which is still massive. I'm building with `-Os` now to see how much of a difference that makes.



---

archive/issue_comments_008096.json:
```json
{
    "body": "I think this should also be safe in `$SAGE_ROOT/devel/sage/sage/`\n\n\n```\nfor f in `find -name \"*.pyx\"`; do echo $f | sed \"s/\\.pyx/\\.c/\" | xargs rm; done\n```\n\n\n\n```\nfor f in `find -name \"*.pyx\"`; do echo $f | sed \"s/\\.pyx/\\.cpp/\" | xargs rm; done\n```\n\n\nto delete all autogenerated `.c` and `.cpp` files.\n\nThis seems to free ~ 80MB",
    "created_at": "2008-09-28T15:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1293#issuecomment-8096",
    "user": "https://github.com/malb"
}
```

I think this should also be safe in `$SAGE_ROOT/devel/sage/sage/`


```
for f in `find -name "*.pyx"`; do echo $f | sed "s/\.pyx/\.c/" | xargs rm; done
```



```
for f in `find -name "*.pyx"`; do echo $f | sed "s/\.pyx/\.cpp/" | xargs rm; done
```


to delete all autogenerated `.c` and `.cpp` files.

This seems to free ~ 80MB



---

archive/issue_comments_008097.json:
```json
{
    "body": "Actually, the result is smaller than **1.1GB** as I forgot to strip the Sage extensions. The result including the add-on above is **978M** but still fully functional, I believe.",
    "created_at": "2008-09-28T15:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1293#issuecomment-8097",
    "user": "https://github.com/malb"
}
```

Actually, the result is smaller than **1.1GB** as I forgot to strip the Sage extensions. The result including the add-on above is **978M** but still fully functional, I believe.



---

archive/issue_comments_008098.json:
```json
{
    "body": "I guess this issue won't be fixed, thus I close this ticket.",
    "created_at": "2010-02-05T20:31:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1293#issuecomment-8098",
    "user": "https://github.com/zimmermann6"
}
```

I guess this issue won't be fixed, thus I close this ticket.



---

archive/issue_comments_008099.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-02-05T20:31:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1293#issuecomment-8099",
    "user": "https://github.com/zimmermann6"
}
```

Resolution: wontfix



---

archive/issue_events_003391.json:
```json
{
    "actor": "https://github.com/zimmermann6",
    "created_at": "2010-02-05T20:31:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1293",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1293#event-3391"
}
```



---

archive/issue_comments_008100.json:
```json
{
    "body": "Resolution changed from wontfix to worksforme",
    "created_at": "2010-02-05T21:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1293#issuecomment-8100",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution changed from wontfix to worksforme



---

archive/issue_comments_008101.json:
```json
{
    "body": "Make sure you understand the procedure for closing tickets. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for more information.",
    "created_at": "2010-02-05T21:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1293#issuecomment-8101",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Make sure you understand the procedure for closing tickets. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for more information.



---

archive/issue_events_003392.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-05T21:13:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1293",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1293#event-3392"
}
```



---

archive/issue_comments_008102.json:
```json
{
    "body": "Sorry I didn't know I wasn't allowed to close tickets!\nIt would be better to remove the \"closed\" button for \"normal\" users.",
    "created_at": "2010-02-07T21:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1293#issuecomment-8102",
    "user": "https://github.com/zimmermann6"
}
```

Sorry I didn't know I wasn't allowed to close tickets!
It would be better to remove the "closed" button for "normal" users.
