# Issue 3537: [with patch, needs review] sage-env breaks makefile RM

archive/issues_003537.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  mabshoff snark drkirkby @jdemeyer\n\nThe env variable RM is set to rm instead of rm -rf.  This breaks some functionality of make (such as compiling .l files) which breaks the ability to compile M2 with sage-env sourced.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3537\n\n",
    "created_at": "2008-06-30T03:24:02Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "[with patch, needs review] sage-env breaks makefile RM",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3537",
    "user": "@garyfurnish"
}
```
Assignee: mabshoff

CC:  mabshoff snark drkirkby @jdemeyer

The env variable RM is set to rm instead of rm -rf.  This breaks some functionality of make (such as compiling .l files) which breaks the ability to compile M2 with sage-env sourced.

Issue created by migration from https://trac.sagemath.org/ticket/3537





---

archive/issue_comments_024960.json:
```json
{
    "body": "Attachment [trac_3537_scripts.patch](tarball://root/attachments/some-uuid/ticket3537/trac_3537_scripts.patch) by @garyfurnish created at 2008-06-30 03:27:30",
    "created_at": "2008-06-30T03:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24960",
    "user": "@garyfurnish"
}
```

Attachment [trac_3537_scripts.patch](tarball://root/attachments/some-uuid/ticket3537/trac_3537_scripts.patch) by @garyfurnish created at 2008-06-30 03:27:30



---

archive/issue_comments_024961.json:
```json
{
    "body": "Changing assignee from mabshoff to @garyfurnish.",
    "created_at": "2008-06-30T03:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24961",
    "user": "@garyfurnish"
}
```

Changing assignee from mabshoff to @garyfurnish.



---

archive/issue_comments_024962.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-30T03:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24962",
    "user": "@garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024963.json:
```json
{
    "body": "The intent of -f is to avoid errors for the conditions cited as a problem.",
    "created_at": "2008-06-30T03:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24963",
    "user": "ghtdak"
}
```

The intent of -f is to avoid errors for the conditions cited as a problem.



---

archive/issue_comments_024964.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2008-06-30T04:45:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24964",
    "user": "mabshoff"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_024965.json:
```json
{
    "body": "I am not convinced yet that this is the right thing to do and it is rather likely that this will break something else in the tree. The solution to M2's problem is to unset RM in spkg-install and then to set RM to some value you desire.\n\nAnd this is definitely not a blocker for 3.0.4.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-30T04:45:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24965",
    "user": "mabshoff"
}
```

I am not convinced yet that this is the right thing to do and it is rather likely that this will break something else in the tree. The solution to M2's problem is to unset RM in spkg-install and then to set RM to some value you desire.

And this is definitely not a blocker for 3.0.4.

Cheers,

Michael



---

archive/issue_comments_024966.json:
```json
{
    "body": "If M2 depends on the default behavior of RM in its Makefiles it should set RM in its top level makefile. I see no reason to change Sage's behavior and as is if someone sets RM outside of sage-env it is propagated anyway. So this is wontfix.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-01T04:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24966",
    "user": "mabshoff"
}
```

If M2 depends on the default behavior of RM in its Makefiles it should set RM in its top level makefile. I see no reason to change Sage's behavior and as is if someone sets RM outside of sage-env it is propagated anyway. So this is wontfix.

Cheers,

Michael



---

archive/issue_comments_024967.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-07-01T04:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24967",
    "user": "mabshoff"
}
```

Resolution: wontfix



---

archive/issue_comments_024968.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-12-11T11:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24968",
    "user": "@vbraun"
}
```

Changing status from closed to new.



---

archive/issue_comments_024969.json:
```json
{
    "body": "I'm reopening this bug since people keep tripping over this issue. We need to fix this or we'll end up with every spkg working around the `RM=rm` issue. As the spkg maintainer/author, I know that `cddlib` and `TOPCOM` both need to `unset RM` or they won't build. In #10285 it was noted a few days ago that Boehm GC 7.2 also trips over this issue. More and more packages will fail because of this issue as soon as upsteam re-runs autotools...\n\nFor the record, gfurnish's patch applies cleanly on Sage-4.6.1.alpha3 (apply to the $SAGE_LOCAL/bin repo)\n\nI'd be happy to give this a positive review. Maybe mabshoff can reconsider his objections?",
    "created_at": "2010-12-11T11:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24969",
    "user": "@vbraun"
}
```

I'm reopening this bug since people keep tripping over this issue. We need to fix this or we'll end up with every spkg working around the `RM=rm` issue. As the spkg maintainer/author, I know that `cddlib` and `TOPCOM` both need to `unset RM` or they won't build. In #10285 it was noted a few days ago that Boehm GC 7.2 also trips over this issue. More and more packages will fail because of this issue as soon as upsteam re-runs autotools...

For the record, gfurnish's patch applies cleanly on Sage-4.6.1.alpha3 (apply to the $SAGE_LOCAL/bin repo)

I'd be happy to give this a positive review. Maybe mabshoff can reconsider his objections?



---

archive/issue_comments_024970.json:
```json
{
    "body": "Resolution changed from wontfix to ",
    "created_at": "2010-12-11T11:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24970",
    "user": "@vbraun"
}
```

Resolution changed from wontfix to 



---

archive/issue_comments_024971.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-12-11T12:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24971",
    "user": "@vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_024972.json:
```json
{
    "body": "Replying to [comment:5 vbraun]:\n> I'm reopening this bug since people keep tripping over this issue. We need to fix this or we'll end up with every spkg working around the `RM=rm` issue.\n\nWell, is this a bug? \n\n> More and more packages will fail because of this issue as soon as upsteam re-runs autotools...\n\nThat's IMHO a problem of autotools. `$RM` is in general not supposed to *not return an error* on non-existing files; if autotools were a bit smarter, they would just add `-f` or whatever might be appropriate. If they redefine the meaning of `RM`, that's not Sage's problem in the first place; of course spkg maintainers would have to `unset RM` for upstream packages using (newer) autotools.\n\n\n> I'd be happy to give this a positive review. Maybe mabshoff can reconsider his objections?\n\nMichael has quit a while ago, though he perhaps still reads trac notifications... ;-)\n\n\nNote that redefining `RM` in `sage-env` could actually break other parts of Sage, not necessarily limited to spkgs, since e.g. removing a file which is expected to exist, but doesn't, without raising an error might hide other errors and cause arbitrary behavior.\n\nAlso, as Michael said, changing the default value in `sage-env` doesn't help if `RM` was already defined (intentionally or not) by the user, so w.r.t. autotools really *won't fix*. We have to `unset RM` (or add an appropriate flag to force deletion if it's not already contained) in `spkg-install`s of such packages anyway to be safe.\n\n\nI think we should prominently document this issue, and close this ticket again.",
    "created_at": "2010-12-17T15:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24972",
    "user": "@nexttime"
}
```

Replying to [comment:5 vbraun]:
> I'm reopening this bug since people keep tripping over this issue. We need to fix this or we'll end up with every spkg working around the `RM=rm` issue.

Well, is this a bug? 

> More and more packages will fail because of this issue as soon as upsteam re-runs autotools...

That's IMHO a problem of autotools. `$RM` is in general not supposed to *not return an error* on non-existing files; if autotools were a bit smarter, they would just add `-f` or whatever might be appropriate. If they redefine the meaning of `RM`, that's not Sage's problem in the first place; of course spkg maintainers would have to `unset RM` for upstream packages using (newer) autotools.


> I'd be happy to give this a positive review. Maybe mabshoff can reconsider his objections?

Michael has quit a while ago, though he perhaps still reads trac notifications... ;-)


Note that redefining `RM` in `sage-env` could actually break other parts of Sage, not necessarily limited to spkgs, since e.g. removing a file which is expected to exist, but doesn't, without raising an error might hide other errors and cause arbitrary behavior.

Also, as Michael said, changing the default value in `sage-env` doesn't help if `RM` was already defined (intentionally or not) by the user, so w.r.t. autotools really *won't fix*. We have to `unset RM` (or add an appropriate flag to force deletion if it's not already contained) in `spkg-install`s of such packages anyway to be safe.


I think we should prominently document this issue, and close this ticket again.



---

archive/issue_comments_024973.json:
```json
{
    "body": "Why does `RM` need to be defined at all?",
    "created_at": "2010-12-17T16:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24973",
    "user": "@jdemeyer"
}
```

Why does `RM` need to be defined at all?



---

archive/issue_comments_024974.json:
```json
{
    "body": "Replying to [comment:8 jdemeyer]:\n> Why does `RM` need to be defined at all?\n\nBecause\n\n```sh\n${RM} some_file\n```\n\nwill (hopefully) fail if `RM` is not set or empty?\n\nImagine `some_file` was executable in that case...\n\n\n\n\nIt would be a bit odd to test and eventually set all such variables individually in every script that uses some of these, therefore we have `sage-env`.\n\nThough `CP`, `RM` etc. are meanwhile hardly used within Sage; perhaps because setting them isn't necessary on any proper OS...\n\nInstead, it would be better to have e.g. `EGREP`, (POSIX-conformant) `GREP` etc., detected / set by Sage's `configure`.",
    "created_at": "2010-12-17T17:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24974",
    "user": "@nexttime"
}
```

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

archive/issue_comments_024975.json:
```json
{
    "body": "I seriously doubt that anybody uses the \"destructive existence test\" `$RM filename || ...` :-)\n\nAutomake has an official list of variables that it looks at. Perhaps it is a bug that `RM` is on the list, but its still our problem and I doubt upstream will change because some guys from Sage have a variable name collision. See also http://www.gnu.org/software/automake/manual/make/Implicit-Variables.html",
    "created_at": "2010-12-17T20:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24975",
    "user": "@vbraun"
}
```

I seriously doubt that anybody uses the "destructive existence test" `$RM filename || ...` :-)

Automake has an official list of variables that it looks at. Perhaps it is a bug that `RM` is on the list, but its still our problem and I doubt upstream will change because some guys from Sage have a variable name collision. See also http://www.gnu.org/software/automake/manual/make/Implicit-Variables.html



---

archive/issue_comments_024976.json:
```json
{
    "body": "Replying to [comment:9 leif]:\n> Because\n> {{{\n> #!sh\n> ${RM} some_file\n> }}}\n> will (hopefully) fail if `RM` is not set or empty?\n\nWhere is such code used?  My guess: nowhere.",
    "created_at": "2010-12-18T13:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24976",
    "user": "@jdemeyer"
}
```

Replying to [comment:9 leif]:
> Because
> {{{
> #!sh
> ${RM} some_file
> }}}
> will (hopefully) fail if `RM` is not set or empty?

Where is such code used?  My guess: nowhere.



---

archive/issue_comments_024977.json:
```json
{
    "body": "Replying to [comment:11 jdemeyer]:\n> Replying to [comment:9 leif]:\n> > Because\n\n```sh\n${RM} some_file\n```\n\n> > will (hopefully) fail if `RM` is not set or empty?\n> \n> Where is such code used?  My guess: nowhere.\n\nE.g. Singular's `spkg-install` does. (It actually does `$RM -f ...`.)\n\nI wouldn't base such changes on guesses... ;-)",
    "created_at": "2010-12-26T18:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24977",
    "user": "@nexttime"
}
```

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

archive/issue_comments_024978.json:
```json
{
    "body": "For the record:\n\n```\n[vbraun@volker-desktop spkg-unpacked]$ grep '\\$RM' */*\ngap-4.4.12.p4/SPKG.txt: * #7873 Remove references to $LN, $MKIDR and $RM and replace\nmercurial-1.6.4.p0/SPKG.txt: * Changes occurrences of $RM to 'rm', $CP to 'cp' and similar.\nsage_scripts-4.6.1.alpha3.p0/sage-env:if [ \"$RM\" = \"\" ]; then\nsingular-3-1-1-4.p3/spkg-install:        $RM -f LIB\nsingular-3-1-1-4.p3/spkg-install:    $RM -f Singular singular\nsingular-3-1-1-4.p3/spkg-install:        $RM -f Singular-1-0-2   # remove previous version of Singular.\n```\n",
    "created_at": "2010-12-26T19:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24978",
    "user": "@vbraun"
}
```

For the record:

```
[vbraun@volker-desktop spkg-unpacked]$ grep '\$RM' */*
gap-4.4.12.p4/SPKG.txt: * #7873 Remove references to $LN, $MKIDR and $RM and replace
mercurial-1.6.4.p0/SPKG.txt: * Changes occurrences of $RM to 'rm', $CP to 'cp' and similar.
sage_scripts-4.6.1.alpha3.p0/sage-env:if [ "$RM" = "" ]; then
singular-3-1-1-4.p3/spkg-install:        $RM -f LIB
singular-3-1-1-4.p3/spkg-install:    $RM -f Singular singular
singular-3-1-1-4.p3/spkg-install:        $RM -f Singular-1-0-2   # remove previous version of Singular.
```




---

archive/issue_comments_024979.json:
```json
{
    "body": "Replying to [comment:13 vbraun]:\n> For the record:\n\n```sh\n[vbraun@volker-desktop spkg-unpacked]$ grep '\\$RM' */*\n```\n\n\nRedo for `${RM}`, too? (Also `$(RM)` in Makefiles.)\n\nNot sure if there are some \"deeper\" instances as well.",
    "created_at": "2010-12-26T22:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24979",
    "user": "@nexttime"
}
```

Replying to [comment:13 vbraun]:
> For the record:

```sh
[vbraun@volker-desktop spkg-unpacked]$ grep '\$RM' */*
```


Redo for `${RM}`, too? (Also `$(RM)` in Makefiles.)

Not sure if there are some "deeper" instances as well.



---

archive/issue_comments_024980.json:
```json
{
    "body": "\n```\n[vbraun@volker-desktop spkg-unpacked]$ grep '\\$.RM' */*\nsingular-3-1-1-4.p3/install-sh:rmprog=\"${RMPROG-rm}\"\n```\n\nand\n\n```\n[vbraun@volker-desktop spkg-unpacked]$ grep '\\$.*RM' */*\ngap-4.4.12.p4/SPKG.txt: * #7873 Remove references to $LN, $MKIDR and $RM and replace\nmercurial-1.6.4.p0/SPKG.txt: * Changes occurrences of $RM to 'rm', $CP to 'cp' and similar.\nsage_scripts-4.6.1.alpha3.p0/sage-check-64:\t\tcase $CONFIRM in\nsage_scripts-4.6.1.alpha3.p0/sage-env:if [ \"$RM\" = \"\" ]; then\nsingular-3-1-1-4.p3/install-sh:rmprog=\"${RMPROG-rm}\"\nsingular-3-1-1-4.p3/spkg-install:        $RM -f LIB\nsingular-3-1-1-4.p3/spkg-install:    $RM -f Singular singular\nsingular-3-1-1-4.p3/spkg-install:        $RM -f Singular-1-0-2   # remove previous version of Singular.\n```\n",
    "created_at": "2010-12-26T22:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24980",
    "user": "@vbraun"
}
```


```
[vbraun@volker-desktop spkg-unpacked]$ grep '\$.RM' */*
singular-3-1-1-4.p3/install-sh:rmprog="${RMPROG-rm}"
```

and

```
[vbraun@volker-desktop spkg-unpacked]$ grep '\$.*RM' */*
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

archive/issue_comments_024981.json:
```json
{
    "body": "So right now, singular is the only place this is used, and it consistently uses \"$RM -f\", right?  Given this, rather than set `RM=\"rm -f\"`, it seems better to leave it as is and document it in the developer's guide (in the section on producing new spkg's), and perhaps also in the installation guide (in the section on environment variables).  Here's a patch doing that; what do you think?",
    "created_at": "2011-03-26T17:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24981",
    "user": "@jhpalmieri"
}
```

So right now, singular is the only place this is used, and it consistently uses "$RM -f", right?  Given this, rather than set `RM="rm -f"`, it seems better to leave it as is and document it in the developer's guide (in the section on producing new spkg's), and perhaps also in the installation guide (in the section on environment variables).  Here's a patch doing that; what do you think?



---

archive/issue_comments_024982.json:
```json
{
    "body": "Attachment [trac_3537-doc.patch](tarball://root/attachments/some-uuid/ticket3537/trac_3537-doc.patch) by @jhpalmieri created at 2011-03-26 17:04:47",
    "created_at": "2011-03-26T17:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24982",
    "user": "@jhpalmieri"
}
```

Attachment [trac_3537-doc.patch](tarball://root/attachments/some-uuid/ticket3537/trac_3537-doc.patch) by @jhpalmieri created at 2011-03-26 17:04:47



---

archive/issue_comments_024983.json:
```json
{
    "body": "My opinion still is that `RM` should simply be left unset (of course, a few install scripts will have to be changed).",
    "created_at": "2011-03-26T18:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24983",
    "user": "@jdemeyer"
}
```

My opinion still is that `RM` should simply be left unset (of course, a few install scripts will have to be changed).



---

archive/issue_comments_024984.json:
```json
{
    "body": "Replying to [comment:18 jdemeyer]:\n> My opinion still is that `RM` should simply be left unset (of course, a few install scripts will have to be changed).\n\nI agree 100%. \n\nI can understand the logic of variables like $CC, $CXX, $MAKE, but not $RM. I don't know of any system where one might want to specify what version of `rm` gets used, so I don't see the point in having a variable for it. If some dump package needs `$RM` defined, then either try to fix the code so it is not so dumb, or add `$RM` to `dump_package.spkg`. \n\nBTW, take a look at\n\nhttp://boxen.math.washington.edu/home/kirkby/bad-code/sympow-1.018.1.p7/src/Configure\n\nwhere you will find some *interesting* use of variable names. A script which starts \n\n`#!/bin/sh`\n\nhas a function \n\n`whichexe()`\n\nThis function makes use of a non-POSIX command `which`, so there's no reason for `which` to exist. Then `whichexe()` function sets variables for things like SH, RM, SED, whilst checking if the commands (including `sh`) exist. If not the script exits. An abbreviated version is below. \n\n\n```/bin/sh\nwhichexe() {\n    if [ -f /bin/$1 ]; then\n        echo /bin/$1\n        return;\n    fi;\n    if [ -f /usr/bin/$1 ]; then\n        echo /usr/bin/$1\n        return;\n    fi;\n    if [ -f /usr/local/bin/$1 ]; then\n        echo /usr/local/bin/$1\n        return;\n    fi;\n    echo `which $1`\n}\nRM=`whichexe rm`\nGREP=`whichexe grep` && echo \"#define GREP \\\"$GREP\\\"\" >> $CONFIG\nSED=`whichexe sed` && echo \"#define SED \\\"$SED\\\"\" >> $CONFIG\nSH=`whichexe sh` && echo \"#define SH \\\"$SH\\\"\" >> $CONFIG\nif [ -z \"$SH\" ]; then\n  echo \"**ERROR**: Could not find sh\"; exit 1;\nelse\n  echo \"SH = $SH\"\nfi\n```\n\n\nI might have cleaned this up, so the current version in Sage might not be quite so dumb. \n\nDave",
    "created_at": "2011-03-26T18:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24984",
    "user": "drkirkby"
}
```

Replying to [comment:18 jdemeyer]:
> My opinion still is that `RM` should simply be left unset (of course, a few install scripts will have to be changed).

I agree 100%. 

I can understand the logic of variables like $CC, $CXX, $MAKE, but not $RM. I don't know of any system where one might want to specify what version of `rm` gets used, so I don't see the point in having a variable for it. If some dump package needs `$RM` defined, then either try to fix the code so it is not so dumb, or add `$RM` to `dump_package.spkg`. 

BTW, take a look at

http://boxen.math.washington.edu/home/kirkby/bad-code/sympow-1.018.1.p7/src/Configure

where you will find some *interesting* use of variable names. A script which starts 

`#!/bin/sh`

has a function 

`whichexe()`

This function makes use of a non-POSIX command `which`, so there's no reason for `which` to exist. Then `whichexe()` function sets variables for things like SH, RM, SED, whilst checking if the commands (including `sh`) exist. If not the script exits. An abbreviated version is below. 


```/bin/sh
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

archive/issue_comments_024985.json:
```json
{
    "body": "See #9497 for a patch to change \"$RM\" to \"rm\" in Singular's spkg-install script.",
    "created_at": "2011-03-26T23:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24985",
    "user": "@jhpalmieri"
}
```

See #9497 for a patch to change "$RM" to "rm" in Singular's spkg-install script.



---

archive/issue_comments_024986.json:
```json
{
    "body": "When 50 percent or more of spkgs require $RM to be \"rm -f\" then\nchange $RM from \"rm\" to \"rm -f\".  Until then document.\n\nPositive review.",
    "created_at": "2011-05-12T14:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24986",
    "user": "mariah"
}
```

When 50 percent or more of spkgs require $RM to be "rm -f" then
change $RM from "rm" to "rm -f".  Until then document.

Positive review.



---

archive/issue_comments_024987.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-12T14:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24987",
    "user": "mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_024988.json:
```json
{
    "body": "Changing component from build to scripts.",
    "created_at": "2011-05-12T14:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24988",
    "user": "@jdemeyer"
}
```

Changing component from build to scripts.



---

archive/issue_comments_024989.json:
```json
{
    "body": "Singular's spkg-install no longer uses $RM, so the documentation is not up to date.",
    "created_at": "2011-05-12T14:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24989",
    "user": "@jdemeyer"
}
```

Singular's spkg-install no longer uses $RM, so the documentation is not up to date.



---

archive/issue_comments_024990.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-05-12T14:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24990",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_024991.json:
```json
{
    "body": "Do not set $RM in sage-env",
    "created_at": "2011-05-12T14:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24991",
    "user": "@jdemeyer"
}
```

Do not set $RM in sage-env



---

archive/issue_comments_024992.json:
```json
{
    "body": "Attachment [trac_3537-unset-RM.patch](tarball://root/attachments/some-uuid/ticket3537/trac_3537-unset-RM.patch) by mariah created at 2011-05-12 20:40:02\n\n[attachment:trac_3537-unset-RM.patch] applied to sage-4.7.rc2 tested on skynet/taurus with make testlong.  All tests passed.  Positive review.",
    "created_at": "2011-05-12T20:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24992",
    "user": "mariah"
}
```

Attachment [trac_3537-unset-RM.patch](tarball://root/attachments/some-uuid/ticket3537/trac_3537-unset-RM.patch) by mariah created at 2011-05-12 20:40:02

[attachment:trac_3537-unset-RM.patch] applied to sage-4.7.rc2 tested on skynet/taurus with make testlong.  All tests passed.  Positive review.



---

archive/issue_comments_024993.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-05-12T20:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24993",
    "user": "mariah"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_024994.json:
```json
{
    "body": "Replying to [comment:23 mariah]:\n> [attachment:trac_3537-unset-RM.patch] applied to sage-4.7.rc2 tested on skynet/taurus with make testlong.  All tests passed.  Positive review.\n\nDid you try building Sage from source with this patch applied?  Because this patch affects the Sage **build**, not the Sage library.",
    "created_at": "2011-05-12T20:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24994",
    "user": "@jdemeyer"
}
```

Replying to [comment:23 mariah]:
> [attachment:trac_3537-unset-RM.patch] applied to sage-4.7.rc2 tested on skynet/taurus with make testlong.  All tests passed.  Positive review.

Did you try building Sage from source with this patch applied?  Because this patch affects the Sage **build**, not the Sage library.



---

archive/issue_comments_024995.json:
```json
{
    "body": "Apologies for not be clear.  I first applied the patch to the sage-4.7.rc2 source, then built the source, then did make testlong.",
    "created_at": "2011-05-13T13:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24995",
    "user": "mariah"
}
```

Apologies for not be clear.  I first applied the patch to the sage-4.7.rc2 source, then built the source, then did make testlong.



---

archive/issue_comments_024996.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-17T08:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24996",
    "user": "@jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_024997.json:
```json
{
    "body": "I just checked all spkg-install scripts and `$RM` is used nowhere anymore.",
    "created_at": "2011-05-17T08:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24997",
    "user": "@jdemeyer"
}
```

I just checked all spkg-install scripts and `$RM` is used nowhere anymore.
