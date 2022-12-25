# Issue 1002: update clisp to 2.42

archive/issues_001002.json:
```json
{
    "body": "Assignee: @williamstein\n\nClisp 2.42 was released on October 16th.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1002\n\n",
    "created_at": "2007-10-26T09:07:30Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "update clisp to 2.42",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1002",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

Clisp 2.42 was released on October 16th.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1002





---

archive/issue_comments_006079.json:
```json
{
    "body": "clisp 2.43 is actually out already!\n\nCheers,\n\nMichael",
    "created_at": "2007-12-04T14:18:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1002#issuecomment-6079",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

clisp 2.43 is actually out already!

Cheers,

Michael



---

archive/issue_comments_006080.json:
```json
{
    "body": "Bill Page writes:\n\n```\nWell, so far I can confirm only that the following modified spkg:\n\n  http://sage.math.washington.edu/home/page/clisp-2.43-alpha.spkg\n\nwhich is based on clisp-2.43 as distributed by the clisp project,\ninstalls in Sage running on sage.math and it can re-build (-f ...)\nmaxima-5.13.0.p1, axiom4sage-0.3.1 and the full version of FriCAS\n(rev: 134).\n\nI did only a fairly mimimal change to 'clisp-2.43-alpha.spkg' to\neliminate all patches and adapt to the slightly changed build process\n(no intermediate makemake step necessary). FFI is automatically\nincluded. It it quite possible that this version may not build on OSX\netc. however I know that the clisp developers have made some\nsignificant improvements in the build since 2.41. I would be glad in\nanyone can try this 'clisp-2.43-alpha.spkg' and let me know what works\nand what doesn't. Also please feel free to take the above and run with\nit. ;-)\n\n```\n\n\nI build tested on OSX 10.5 and clisp as well as maxima builds, doctesting at the moment. I will also test on OSX 10.4 PPC.\n\nThe spkg is about 3 MB larger than the 2.41 one? Can we shrink the spkg?\n\nCheers,\n\nMichael",
    "created_at": "2007-12-05T21:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1002#issuecomment-6080",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Bill Page writes:

```
Well, so far I can confirm only that the following modified spkg:

  http://sage.math.washington.edu/home/page/clisp-2.43-alpha.spkg

which is based on clisp-2.43 as distributed by the clisp project,
installs in Sage running on sage.math and it can re-build (-f ...)
maxima-5.13.0.p1, axiom4sage-0.3.1 and the full version of FriCAS
(rev: 134).

I did only a fairly mimimal change to 'clisp-2.43-alpha.spkg' to
eliminate all patches and adapt to the slightly changed build process
(no intermediate makemake step necessary). FFI is automatically
included. It it quite possible that this version may not build on OSX
etc. however I know that the clisp developers have made some
significant improvements in the build since 2.41. I would be glad in
anyone can try this 'clisp-2.43-alpha.spkg' and let me know what works
and what doesn't. Also please feel free to take the above and run with
it. ;-)

```


I build tested on OSX 10.5 and clisp as well as maxima builds, doctesting at the moment. I will also test on OSX 10.4 PPC.

The spkg is about 3 MB larger than the 2.41 one? Can we shrink the spkg?

Cheers,

Michael



---

archive/issue_comments_006081.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-06T02:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1002#issuecomment-6081",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006082.json:
```json
{
    "body": "Merged in 2.9.alpha0.",
    "created_at": "2007-12-06T02:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1002#issuecomment-6082",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.alpha0.



---

archive/issue_comments_006083.json:
```json
{
    "body": "The spkg miscompiles with the current gcc from Debian testing x86. See\n\nhttp://sourceforge.net/tracker/index.php?func=detail&aid=1836142&group_id=1355&atid=101355\n\nIt is a known issue that so far is unresolved.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-06T17:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1002#issuecomment-6083",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg miscompiles with the current gcc from Debian testing x86. See

http://sourceforge.net/tracker/index.php?func=detail&aid=1836142&group_id=1355&atid=101355

It is a known issue that so far is unresolved.

Cheers,

Michael



---

archive/issue_comments_006084.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-06T17:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1002#issuecomment-6084",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_006085.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-06T17:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1002#issuecomment-6085",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_006086.json:
```json
{
    "body": "Carl Witty writes:\n\n```\nOn my Debian testing 32-bit x86 Linux laptop, the clisp build failed.\nThe last few lines of the build log were:\nrm -f dutch.lisp\nln -s /home/cwitty/sage-2.9.alpha0/spkg/build/clisp-2.43/src/src/\ndutch.lisp dutch.lisp\nrm -f deprecated.lisp\nln -s /home/cwitty/sage-2.9.alpha0/spkg/build/clisp-2.43/src/src/\ndeprecated.lisp deprecated.lisp\n./lisp.run -B . -N locale -E 1:1 -Efile UTF-8 -Eterminal UTF-8 -norc -\nm 1800KW -x \"(and (load \\\"init.lisp\\\") (sys::%saveinitmem)\n(ext::exit)) (ext::exit t)\"\nmake[2]: *** [interpreted.mem] Segmentation fault\nmake[2]: Leaving directory `/home/cwitty/sage-2.9.alpha0/spkg/build/\nclisp-2.43/build'\n\nRecompiling without optimization may have worked (the compiles of\nclisp and maxima have succeeded, but Sage as a whole isn't done\nbuilding yet, so I haven't tested).\n\nI did this by adding\n  export CFLAGS=-O0\nto spkg-install, before the call to configure; and editing src/src/\nmakemake.in to replace every instance of \"-O2\" with '-O0\".\n\n(I'm not sure if both of these changes were necessary.) \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-12-06T22:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1002#issuecomment-6086",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Carl Witty writes:

```
On my Debian testing 32-bit x86 Linux laptop, the clisp build failed.
The last few lines of the build log were:
rm -f dutch.lisp
ln -s /home/cwitty/sage-2.9.alpha0/spkg/build/clisp-2.43/src/src/
dutch.lisp dutch.lisp
rm -f deprecated.lisp
ln -s /home/cwitty/sage-2.9.alpha0/spkg/build/clisp-2.43/src/src/
deprecated.lisp deprecated.lisp
./lisp.run -B . -N locale -E 1:1 -Efile UTF-8 -Eterminal UTF-8 -norc -
m 1800KW -x "(and (load \"init.lisp\") (sys::%saveinitmem)
(ext::exit)) (ext::exit t)"
make[2]: *** [interpreted.mem] Segmentation fault
make[2]: Leaving directory `/home/cwitty/sage-2.9.alpha0/spkg/build/
clisp-2.43/build'

Recompiling without optimization may have worked (the compiles of
clisp and maxima have succeeded, but Sage as a whole isn't done
building yet, so I haven't tested).

I did this by adding
  export CFLAGS=-O0
to spkg-install, before the call to configure; and editing src/src/
makemake.in to replace every instance of "-O2" with '-O0".

(I'm not sure if both of these changes were necessary.) 
```


Cheers,

Michael



---

archive/issue_comments_006087.json:
```json
{
    "body": "There is now a 2.43.1 release that supposedly fixes the gcc 4.2 and 4.3 problems at\n\nhttp://www.haible.de/bruno/clisp/clisp-2.43.1.tar.gz\n\nCheers,\n\nMichael",
    "created_at": "2008-02-24T21:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1002#issuecomment-6087",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There is now a 2.43.1 release that supposedly fixes the gcc 4.2 and 4.3 problems at

http://www.haible.de/bruno/clisp/clisp-2.43.1.tar.gz

Cheers,

Michael



---

archive/issue_comments_006088.json:
```json
{
    "body": "2.44.1 is also out and it has the same fix as 2.43.1, so let's try to update to the latest version.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-01T22:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1002#issuecomment-6088",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

2.44.1 is also out and it has the same fix as 2.43.1, so let's try to update to the latest version.

Cheers,

Michael



---

archive/issue_comments_006089.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-05-01T14:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1002#issuecomment-6089",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix



---

archive/issue_comments_006090.json:
```json
{
    "body": "This will not happen due to problems of clisp 2.44.1 with gcc 4.2 and 4.3.\n\nWe will likely build Maxima on top of ecl in the near future.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-01T14:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1002#issuecomment-6090",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This will not happen due to problems of clisp 2.44.1 with gcc 4.2 and 4.3.

We will likely build Maxima on top of ecl in the near future.

Cheers,

Michael
