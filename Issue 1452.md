# Issue 1452: GAP - id120.z file missing (?)

archive/issues_001452.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  wdj\n\nRunning doctests on permgroup.py complains that file `id120.z` is missing. Indeed it is!\n\nIssue created by migration from https://trac.sagemath.org/ticket/1452\n\n",
    "created_at": "2007-12-10T19:29:19Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "GAP - id120.z file missing (?)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1452",
    "user": "rlm"
}
```
Assignee: mhansen

CC:  wdj

Running doctests on permgroup.py complains that file `id120.z` is missing. Indeed it is!

Issue created by migration from https://trac.sagemath.org/ticket/1452





---

archive/issue_comments_009348.json:
```json
{
    "body": "Related to #950",
    "created_at": "2007-12-11T17:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9348",
    "user": "rlm"
}
```

Related to #950



---

archive/issue_comments_009349.json:
```json
{
    "body": "NOTE!\n\nI forgot to mention, but this particular code has **HORRIBLE** memory leaks, and so in general it is a **very bad** idea to link this particular code in dynamically. Its executable files should be called directly, so that the leaks are gone as soon as it is finished. So I suppose this needs some more autoconf work...",
    "created_at": "2007-12-19T06:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9349",
    "user": "rlm"
}
```

NOTE!

I forgot to mention, but this particular code has **HORRIBLE** memory leaks, and so in general it is a **very bad** idea to link this particular code in dynamically. Its executable files should be called directly, so that the leaks are gone as soon as it is finished. So I suppose this needs some more autoconf work...



---

archive/issue_comments_009350.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-22T01:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9350",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_009351.json:
```json
{
    "body": "This is a dupe of #2641 which also updates Guava to the 3.3 release.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T01:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9351",
    "user": "mabshoff"
}
```

This is a dupe of #2641 which also updates Guava to the 3.3 release.

Cheers,

Michael



---

archive/issue_comments_009352.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2008-03-30T18:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9352",
    "user": "rlm"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_009353.json:
```json
{
    "body": "Changing component from combinatorics to coding theory.",
    "created_at": "2008-03-30T18:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9353",
    "user": "rlm"
}
```

Changing component from combinatorics to coding theory.



---

archive/issue_comments_009354.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-03-30T18:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9354",
    "user": "rlm"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_009355.json:
```json
{
    "body": "Actually, #2641 doesn't seem to quite fix the problem. Although the compiler outputs the line:\n\n```\ngcc -O2 -o desauto \\\n\t  desauto.o addsgen.o bitmanp.o cdesauto.o chbase.o cmatauto.o \\\n\t  code.o compcrep.o compsg.o copy.o cparstab.o cstborb.o cstrbas.o \\\n\t  errmesg.o essentia.o factor.o field.o inform.o matrix.o new.o \\\n\t  oldcopy.o optsvec.o orbit.o orbrefn.o partn.o permgrp.o permut.o \\\n\t  primes.o ptstbref.o randgrp.o randschr.o readdes.o readgrp.o \\\n\t  readper.o rprique.o storage.o token.o util.o\n```\n\nThe output must be getting clobbered somewhere. I'm looking for it now...",
    "created_at": "2008-03-30T18:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9355",
    "user": "rlm"
}
```

Actually, #2641 doesn't seem to quite fix the problem. Although the compiler outputs the line:

```
gcc -O2 -o desauto \
	  desauto.o addsgen.o bitmanp.o cdesauto.o chbase.o cmatauto.o \
	  code.o compcrep.o compsg.o copy.o cparstab.o cstborb.o cstrbas.o \
	  errmesg.o essentia.o factor.o field.o inform.o matrix.o new.o \
	  oldcopy.o optsvec.o orbit.o orbrefn.o partn.o permgrp.o permut.o \
	  primes.o ptstbref.o randgrp.o randschr.o readdes.o readgrp.o \
	  readper.o rprique.o storage.o token.o util.o
```

The output must be getting clobbered somewhere. I'm looking for it now...



---

archive/issue_comments_009356.json:
```json
{
    "body": "If I run `./configure` in the `src` directory, and then `./configure` and `make` in the guava directory, then the appropriate files show up.\n\n(A separate issue I notice is that other programs in Leon's code aren't compiled, such as `setstab`, and none of the `.sh` routines are moved anywhere.)",
    "created_at": "2008-03-30T18:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9356",
    "user": "rlm"
}
```

If I run `./configure` in the `src` directory, and then `./configure` and `make` in the guava directory, then the appropriate files show up.

(A separate issue I notice is that other programs in Leon's code aren't compiled, such as `setstab`, and none of the `.sh` routines are moved anywhere.)



---

archive/issue_comments_009357.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2008-03-30T18:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9357",
    "user": "rlm"
}
```

Changing status from reopened to new.



---

archive/issue_comments_009358.json:
```json
{
    "body": "Changing assignee from mhansen to rlm.",
    "created_at": "2008-03-30T18:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9358",
    "user": "rlm"
}
```

Changing assignee from mhansen to rlm.



---

archive/issue_comments_009359.json:
```json
{
    "body": "I think two things need to happen.\n\n1. Either Guava should be updated to compile all of Leon, or Leon should be made its own spkg (in non-dynamic mode for now), since maybe some of Leon's functionality isn't specific to coding theory.\n\n2. Either way, the `spkg-install` for gap-4.4.10 needs to be updated to copy the pieces of Leon that do get compiled to the corresponding place in `$SAGE_LOCAL/lib`.",
    "created_at": "2008-03-30T19:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9359",
    "user": "rlm"
}
```

I think two things need to happen.

1. Either Guava should be updated to compile all of Leon, or Leon should be made its own spkg (in non-dynamic mode for now), since maybe some of Leon's functionality isn't specific to coding theory.

2. Either way, the `spkg-install` for gap-4.4.10 needs to be updated to copy the pieces of Leon that do get compiled to the corresponding place in `$SAGE_LOCAL/lib`.



---

archive/issue_comments_009360.json:
```json
{
    "body": "I'd be happy to make a new version of GUAVA which modifies the configure file so that \"all of Leon\" is compiled. \nI don't see why this is a defect though. Not trying to argue, just wondering what's the deal?\nAlso, I'm wondering if there is anything preventing Leon's (compiled) code from being used in SAGE as it is. At one point, there was an argument that the memory leaks barred this. With Brouwer's patch, perhaps this is fixed now?",
    "created_at": "2008-03-30T19:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9360",
    "user": "wdj"
}
```

I'd be happy to make a new version of GUAVA which modifies the configure file so that "all of Leon" is compiled. 
I don't see why this is a defect though. Not trying to argue, just wondering what's the deal?
Also, I'm wondering if there is anything preventing Leon's (compiled) code from being used in SAGE as it is. At one point, there was an argument that the memory leaks barred this. With Brouwer's patch, perhaps this is fixed now?



---

archive/issue_comments_009361.json:
```json
{
    "body": "Why was this reopened? The Guava ticket covers this problem.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-30T19:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9361",
    "user": "mabshoff"
}
```

Why was this reopened? The Guava ticket covers this problem.

Cheers,

Michael



---

archive/issue_comments_009362.json:
```json
{
    "body": "Because there are substantial parts of Leon's programs missing from the install. Will post spkg later tonight.",
    "created_at": "2008-03-30T20:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9362",
    "user": "rlm"
}
```

Because there are substantial parts of Leon's programs missing from the install. Will post spkg later tonight.



---

archive/issue_comments_009363.json:
```json
{
    "body": "OK, here's the full deal:\n\n1. `Makefile.in` in `gap-4.4.10.p3/src/pkg/guava3.3` lists only the programs `desauto` and `wtdist`, while the `Makefile` in `gap-4.4.10.p3/src/pkg/guava3.3/src/leon/src` contains instructions and dependencies for all the programs, including `setstab` (set stabilizer), `cent` (centralizer and conjugacy), etc.\n\n2. There are a number of `.sh` files in `gap-4.4.10.p3/src/pkg/guava3.3/src/leon/src` which make calling the other programs for more questions easy.\n\n3. The issue of memory leaks prevented Leon being used as a dynamically linked library. Compiling them as they are here is perfectly fine, since the process quits as soon as the computation is done. The only problem is overhead.\n\n4. There are also certain no-no's which I figured out the better way to do when linking Leon in dynamically, but that never made it back to Guava proper. For example, in `Makefile.in`, mentioned above, there is the line `DEFINES = -DINT_SIZE=32`, when obviously the right way to do this is to get configure to tell you.\n\nWith David's permission, I'd like to fix all of these up for Guava 3.3.1, or 3.4 or something. In addition, I'd like to fix up the spkg-install to make all of Leon's programs a little more easily accessible from Sage.",
    "created_at": "2008-03-30T22:40:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9363",
    "user": "rlm"
}
```

OK, here's the full deal:

1. `Makefile.in` in `gap-4.4.10.p3/src/pkg/guava3.3` lists only the programs `desauto` and `wtdist`, while the `Makefile` in `gap-4.4.10.p3/src/pkg/guava3.3/src/leon/src` contains instructions and dependencies for all the programs, including `setstab` (set stabilizer), `cent` (centralizer and conjugacy), etc.

2. There are a number of `.sh` files in `gap-4.4.10.p3/src/pkg/guava3.3/src/leon/src` which make calling the other programs for more questions easy.

3. The issue of memory leaks prevented Leon being used as a dynamically linked library. Compiling them as they are here is perfectly fine, since the process quits as soon as the computation is done. The only problem is overhead.

4. There are also certain no-no's which I figured out the better way to do when linking Leon in dynamically, but that never made it back to Guava proper. For example, in `Makefile.in`, mentioned above, there is the line `DEFINES = -DINT_SIZE=32`, when obviously the right way to do this is to get configure to tell you.

With David's permission, I'd like to fix all of these up for Guava 3.3.1, or 3.4 or something. In addition, I'd like to fix up the spkg-install to make all of Leon's programs a little more easily accessible from Sage.



---

archive/issue_comments_009364.json:
```json
{
    "body": "PS - I should mention that originally I wasn't finding desauto or wtdist at all, and they *are* actually put somewhere, but my \"spotlight\" did not find them. Now I am using Google desktop.......",
    "created_at": "2008-03-30T22:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9364",
    "user": "rlm"
}
```

PS - I should mention that originally I wasn't finding desauto or wtdist at all, and they *are* actually put somewhere, but my "spotlight" did not find them. Now I am using Google desktop.......



---

archive/issue_comments_009365.json:
```json
{
    "body": "Yes, please go ahead and fix all these, but please use 3.4 as the next version\nnumber instead of 3.3.1. Thanks! Let me know where the new tarball is so I can post it to the Guava webpage.",
    "created_at": "2008-03-30T22:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9365",
    "user": "wdj"
}
```

Yes, please go ahead and fix all these, but please use 3.4 as the next version
number instead of 3.3.1. Thanks! Let me know where the new tarball is so I can post it to the Guava webpage.



---

archive/issue_comments_009366.json:
```json
{
    "body": "Latest Guava tarball here:\n\nhttp://sage.math.washington.edu/home/rlmill/guava3.4.tar\n\nLatest GAP package here:\n\nhttp://sage.math.washington.edu/home/rlmill/gap-4.4.10.p4.spkg\n\nWithin Guava, this ensures that all of Leon's programs are compiled, and makes sure that they are available in `bin/leon`, together with the shell scripts. I have also left the desauto and wtdist execs where they were for backwards compatibility.\n\nThe latest GAP package (I checked in David's p3 changes to the hg repo, as well as my own changes) makes sure that all the binaries from Guava are copied to `$SAGE_LOCAL/lib/gap-4.4.10/pkg/guava-3.4/bin`. The guava tarball is not necessary for Sage - its contents are contained in the GAP spkg.",
    "created_at": "2008-03-31T02:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9366",
    "user": "rlm"
}
```

Latest Guava tarball here:

http://sage.math.washington.edu/home/rlmill/guava3.4.tar

Latest GAP package here:

http://sage.math.washington.edu/home/rlmill/gap-4.4.10.p4.spkg

Within Guava, this ensures that all of Leon's programs are compiled, and makes sure that they are available in `bin/leon`, together with the shell scripts. I have also left the desauto and wtdist execs where they were for backwards compatibility.

The latest GAP package (I checked in David's p3 changes to the hg repo, as well as my own changes) makes sure that all the binaries from Guava are copied to `$SAGE_LOCAL/lib/gap-4.4.10/pkg/guava-3.4/bin`. The guava tarball is not necessary for Sage - its contents are contained in the GAP spkg.



---

archive/issue_comments_009367.json:
```json
{
    "body": "Somebody has been adding crap files to the spkg again:\n\n```\n.hg\n._.hg\n.hgignore\n._.hgignore\npatches\n._patches\n._spkg-install\nspkg-install\n._SPKG.txt\nSPKG.txt\nsrc\n._src\n```\n\nI did skip the 1,200 others. But I will remove all those crap files.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-31T20:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9367",
    "user": "mabshoff"
}
```

Somebody has been adding crap files to the spkg again:

```
.hg
._.hg
.hgignore
._.hgignore
patches
._patches
._spkg-install
spkg-install
._SPKG.txt
SPKG.txt
src
._src
```

I did skip the 1,200 others. But I will remove all those crap files.

Cheers,

Michael



---

archive/issue_comments_009368.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-31T20:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9368",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009369.json:
```json
{
    "body": "Merged the cleaned up gap.spkg in Sage 3.0.alpha0",
    "created_at": "2008-03-31T20:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1452#issuecomment-9369",
    "user": "mabshoff"
}
```

Merged the cleaned up gap.spkg in Sage 3.0.alpha0
