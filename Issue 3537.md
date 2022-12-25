# Issue 3537: Change $RM in sage-env

archive/issues_003537.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCC:  mabshoff snark drkirkby @jdemeyer\n\nThe env variable RM is set to `rm` instead of `rm -f`. This breaks newer libtools, for example anything in Fedora 12 or later (libtool 2.2.6, autoconf 2.63, automake 1.11.1). They assume that `$RM` is either unset or `RM=\"rm -f\"`, that is, deleting non-existing files must not cause an error.\n\nOne of the symptoms of this breakage is that configure ends with\n\n```\nrm: cannot remove `libtoolT': No such file or directory\n```\nCompile will break later on...\n\n---\n\nThere are three approaches presented here:\n\n- change $RM from \"rm\" to \"rm -f\": [attachment:trac_3537_scripts.patch]\n- keep $RM as it is, but document it: [attachment:trac_3537-doc.patch] (needs_work)\n- don't set $RM at all: [attachment:trac_3537-unset-RM.patch]\n\nApply [attachment:trac_3537-unset-RM.patch]\n\nIssue created by migration from https://trac.sagemath.org/ticket/3537\n\n",
    "closed_at": "2011-05-17T08:47:22Z",
    "created_at": "2008-06-30T03:24:02Z",
    "labels": [
        "component: scripts",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "Change $RM in sage-env",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3537",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @garyfurnish

CC:  mabshoff snark drkirkby @jdemeyer

The env variable RM is set to `rm` instead of `rm -f`. This breaks newer libtools, for example anything in Fedora 12 or later (libtool 2.2.6, autoconf 2.63, automake 1.11.1). They assume that `$RM` is either unset or `RM="rm -f"`, that is, deleting non-existing files must not cause an error.

One of the symptoms of this breakage is that configure ends with

```
rm: cannot remove `libtoolT': No such file or directory
```
Compile will break later on...

---

There are three approaches presented here:

- change $RM from "rm" to "rm -f": [attachment:trac_3537_scripts.patch]
- keep $RM as it is, but document it: [attachment:trac_3537-doc.patch] (needs_work)
- don't set $RM at all: [attachment:trac_3537-unset-RM.patch]

Apply [attachment:trac_3537-unset-RM.patch]

Issue created by migration from https://trac.sagemath.org/ticket/3537





---

archive/issue_comments_024911.json:
```json
{
    "body": "Attachment [trac_3537_scripts.patch](tarball://root/attachments/some-uuid/ticket3537/trac_3537_scripts.patch) by @garyfurnish created at 2008-06-30 03:27:30",
    "created_at": "2008-06-30T03:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24911",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_3537_scripts.patch](tarball://root/attachments/some-uuid/ticket3537/trac_3537_scripts.patch) by @garyfurnish created at 2008-06-30 03:27:30



---

archive/issue_events_008073.json:
```json
{
    "actor": "https://github.com/garyfurnish",
    "created_at": "2008-06-30T03:28:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3537#event-8073"
}
```



---

archive/issue_comments_024912.json:
```json
{
    "body": "Changing assignee from mabshoff to @garyfurnish.",
    "created_at": "2008-06-30T03:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24912",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from mabshoff to @garyfurnish.



---

archive/issue_comments_024913.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-30T03:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24913",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024914.json:
```json
{
    "body": "The intent of -f is to avoid errors for the conditions cited as a problem.",
    "created_at": "2008-06-30T03:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24914",
    "user": "https://trac.sagemath.org/admin/accounts/users/ghtdak"
}
```

The intent of -f is to avoid errors for the conditions cited as a problem.



---

archive/issue_comments_024915.json:
```json
{
    "body": "I am not convinced yet that this is the right thing to do and it is rather likely that this will break something else in the tree. The solution to M2's problem is to unset RM in spkg-install and then to set RM to some value you desire.\n\nAnd this is definitely not a blocker for 3.0.4.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-30T04:45:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24915",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am not convinced yet that this is the right thing to do and it is rather likely that this will break something else in the tree. The solution to M2's problem is to unset RM in spkg-install and then to set RM to some value you desire.

And this is definitely not a blocker for 3.0.4.

Cheers,

Michael



---

archive/issue_comments_024916.json:
```json
{
    "body": "If M2 depends on the default behavior of RM in its Makefiles it should set RM in its top level makefile. I see no reason to change Sage's behavior and as is if someone sets RM outside of sage-env it is propagated anyway. So this is wontfix.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-01T04:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24916",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

If M2 depends on the default behavior of RM in its Makefiles it should set RM in its top level makefile. I see no reason to change Sage's behavior and as is if someone sets RM outside of sage-env it is propagated anyway. So this is wontfix.

Cheers,

Michael



---

archive/issue_comments_024917.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-07-01T04:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24917",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix



---

archive/issue_events_008074.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-01T04:40:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3537#event-8074"
}
```



---

archive/issue_events_008075.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-01T04:40:38Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3537#event-8075"
}
```



---

archive/issue_events_008076.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2010-12-11T11:58:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3537#event-8076"
}
```



---

archive/issue_comments_024918.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-12-11T11:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24918",
    "user": "https://github.com/vbraun"
}
```

Changing status from closed to new.



---

archive/issue_events_008077.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2010-12-11T11:58:59Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3537#event-8077"
}
```



---

archive/issue_comments_024919.json:
```json
{
    "body": "I'm reopening this bug since people keep tripping over this issue. We need to fix this or we'll end up with every spkg working around the `RM=rm` issue. As the spkg maintainer/author, I know that `cddlib` and `TOPCOM` both need to `unset RM` or they won't build. In #10285 it was noted a few days ago that Boehm GC 7.2 also trips over this issue. More and more packages will fail because of this issue as soon as upsteam re-runs autotools...\n\nFor the record, gfurnish's patch applies cleanly on Sage-4.6.1.alpha3 (apply to the $SAGE_LOCAL/bin repo)\n\nI'd be happy to give this a positive review. Maybe mabshoff can reconsider his objections?",
    "created_at": "2010-12-11T11:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24919",
    "user": "https://github.com/vbraun"
}
```

I'm reopening this bug since people keep tripping over this issue. We need to fix this or we'll end up with every spkg working around the `RM=rm` issue. As the spkg maintainer/author, I know that `cddlib` and `TOPCOM` both need to `unset RM` or they won't build. In #10285 it was noted a few days ago that Boehm GC 7.2 also trips over this issue. More and more packages will fail because of this issue as soon as upsteam re-runs autotools...

For the record, gfurnish's patch applies cleanly on Sage-4.6.1.alpha3 (apply to the $SAGE_LOCAL/bin repo)

I'd be happy to give this a positive review. Maybe mabshoff can reconsider his objections?



---

archive/issue_comments_024920.json:
```json
{
    "body": "Resolution changed from wontfix to ",
    "created_at": "2010-12-11T11:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24920",
    "user": "https://github.com/vbraun"
}
```

Resolution changed from wontfix to 



---

archive/issue_comments_024921.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-12-11T12:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24921",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_024922.json:
```json
{
    "body": "Replying to [comment:5 vbraun]:\n> I'm reopening this bug since people keep tripping over this issue. We need to fix this or we'll end up with every spkg working around the `RM=rm` issue.\n\n\nWell, is this a bug? \n\n> More and more packages will fail because of this issue as soon as upsteam re-runs autotools...\n\n\nThat's IMHO a problem of autotools. `$RM` is in general not supposed to *not return an error* on non-existing files; if autotools were a bit smarter, they would just add `-f` or whatever might be appropriate. If they redefine the meaning of `RM`, that's not Sage's problem in the first place; of course spkg maintainers would have to `unset RM` for upstream packages using (newer) autotools.\n\n\n> I'd be happy to give this a positive review. Maybe mabshoff can reconsider his objections?\n\n\nMichael has quit a while ago, though he perhaps still reads trac notifications... ;-)\n\n\nNote that redefining `RM` in `sage-env` could actually break other parts of Sage, not necessarily limited to spkgs, since e.g. removing a file which is expected to exist, but doesn't, without raising an error might hide other errors and cause arbitrary behavior.\n\nAlso, as Michael said, changing the default value in `sage-env` doesn't help if `RM` was already defined (intentionally or not) by the user, so w.r.t. autotools really *won't fix*. We have to `unset RM` (or add an appropriate flag to force deletion if it's not already contained) in `spkg-install`s of such packages anyway to be safe.\n\n\nI think we should prominently document this issue, and close this ticket again.",
    "created_at": "2010-12-17T15:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24922",
    "user": "https://github.com/nexttime"
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

archive/issue_comments_024923.json:
```json
{
    "body": "Why does `RM` need to be defined at all?",
    "created_at": "2010-12-17T16:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24923",
    "user": "https://github.com/jdemeyer"
}
```

Why does `RM` need to be defined at all?



---

archive/issue_comments_024924.json:
```json
{
    "body": "Replying to [comment:8 jdemeyer]:\n> Why does `RM` need to be defined at all?\n\n\nBecause\n\n```sh\n${RM} some_file\n```\nwill (hopefully) fail if `RM` is not set or empty?\n\nImagine `some_file` was executable in that case...\n\n\n\n\nIt would be a bit odd to test and eventually set all such variables individually in every script that uses some of these, therefore we have `sage-env`.\n\nThough `CP`, `RM` etc. are meanwhile hardly used within Sage; perhaps because setting them isn't necessary on any proper OS...\n\nInstead, it would be better to have e.g. `EGREP`, (POSIX-conformant) `GREP` etc., detected / set by Sage's `configure`.",
    "created_at": "2010-12-17T17:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24924",
    "user": "https://github.com/nexttime"
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

archive/issue_comments_024925.json:
```json
{
    "body": "I seriously doubt that anybody uses the \"destructive existence test\" `$RM filename || ...` :-)\n\nAutomake has an official list of variables that it looks at. Perhaps it is a bug that `RM` is on the list, but its still our problem and I doubt upstream will change because some guys from Sage have a variable name collision. See also http://www.gnu.org/software/automake/manual/make/Implicit-Variables.html",
    "created_at": "2010-12-17T20:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24925",
    "user": "https://github.com/vbraun"
}
```

I seriously doubt that anybody uses the "destructive existence test" `$RM filename || ...` :-)

Automake has an official list of variables that it looks at. Perhaps it is a bug that `RM` is on the list, but its still our problem and I doubt upstream will change because some guys from Sage have a variable name collision. See also http://www.gnu.org/software/automake/manual/make/Implicit-Variables.html



---

archive/issue_comments_024926.json:
```json
{
    "body": "Replying to [comment:9 leif]:\n> Because\n> \n> ```\n> #!sh\n> ${RM} some_file\n> ```\n> will (hopefully) fail if `RM` is not set or empty?\n\n\nWhere is such code used?  My guess: nowhere.",
    "created_at": "2010-12-18T13:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24926",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:9 leif]:
> Because
> 
> ```
> #!sh
> ${RM} some_file
> ```
> will (hopefully) fail if `RM` is not set or empty?


Where is such code used?  My guess: nowhere.



---

archive/issue_comments_024927.json:
```json
{
    "body": "Replying to [comment:11 jdemeyer]:\n> Replying to [comment:9 leif]:\n> > Because\n\n{{{#!sh\n${RM} some_file\n}}}\n> > will (hopefully) fail if `RM` is not set or empty?\n\n> \n> Where is such code used?  My guess: nowhere.\n\n\nE.g. Singular's `spkg-install` does. (It actually does `$RM -f ...`.)\n\nI wouldn't base such changes on guesses... ;-)",
    "created_at": "2010-12-26T18:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24927",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:11 jdemeyer]:
> Replying to [comment:9 leif]:
> > Because

{{{#!sh
${RM} some_file
}}}
> > will (hopefully) fail if `RM` is not set or empty?

> 
> Where is such code used?  My guess: nowhere.


E.g. Singular's `spkg-install` does. (It actually does `$RM -f ...`.)

I wouldn't base such changes on guesses... ;-)



---

archive/issue_comments_024928.json:
```json
{
    "body": "For the record:\n\n```\n[vbraun@volker-desktop spkg-unpacked]$ grep '\\$RM' */*\ngap-4.4.12.p4/SPKG.txt: * #7873 Remove references to $LN, $MKIDR and $RM and replace\nmercurial-1.6.4.p0/SPKG.txt: * Changes occurrences of $RM to 'rm', $CP to 'cp' and similar.\nsage_scripts-4.6.1.alpha3.p0/sage-env:if [ \"$RM\" = \"\" ]; then\nsingular-3-1-1-4.p3/spkg-install:        $RM -f LIB\nsingular-3-1-1-4.p3/spkg-install:    $RM -f Singular singular\nsingular-3-1-1-4.p3/spkg-install:        $RM -f Singular-1-0-2   # remove previous version of Singular.\n```",
    "created_at": "2010-12-26T19:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24928",
    "user": "https://github.com/vbraun"
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

archive/issue_comments_024929.json:
```json
{
    "body": "Replying to [comment:13 vbraun]:\n> For the record:\n\n{{{#!sh\n[vbraun`@`volker-desktop spkg-unpacked]$ grep '\\$RM' */*\n}}}\n\nRedo for `${RM}`, too? (Also `$(RM)` in Makefiles.)\n\nNot sure if there are some \"deeper\" instances as well.",
    "created_at": "2010-12-26T22:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24929",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:13 vbraun]:
> For the record:

{{{#!sh
[vbraun`@`volker-desktop spkg-unpacked]$ grep '\$RM' */*
}}}

Redo for `${RM}`, too? (Also `$(RM)` in Makefiles.)

Not sure if there are some "deeper" instances as well.



---

archive/issue_comments_024930.json:
```json
{
    "body": "```\n[vbraun@volker-desktop spkg-unpacked]$ grep '\\$.RM' */*\nsingular-3-1-1-4.p3/install-sh:rmprog=\"${RMPROG-rm}\"\n```\nand\n\n```\n[vbraun@volker-desktop spkg-unpacked]$ grep '\\$.*RM' */*\ngap-4.4.12.p4/SPKG.txt: * #7873 Remove references to $LN, $MKIDR and $RM and replace\nmercurial-1.6.4.p0/SPKG.txt: * Changes occurrences of $RM to 'rm', $CP to 'cp' and similar.\nsage_scripts-4.6.1.alpha3.p0/sage-check-64:\t\tcase $CONFIRM in\nsage_scripts-4.6.1.alpha3.p0/sage-env:if [ \"$RM\" = \"\" ]; then\nsingular-3-1-1-4.p3/install-sh:rmprog=\"${RMPROG-rm}\"\nsingular-3-1-1-4.p3/spkg-install:        $RM -f LIB\nsingular-3-1-1-4.p3/spkg-install:    $RM -f Singular singular\nsingular-3-1-1-4.p3/spkg-install:        $RM -f Singular-1-0-2   # remove previous version of Singular.\n```",
    "created_at": "2010-12-26T22:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24930",
    "user": "https://github.com/vbraun"
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

archive/issue_comments_024931.json:
```json
{
    "body": "So right now, singular is the only place this is used, and it consistently uses \"$RM -f\", right?  Given this, rather than set `RM=\"rm -f\"`, it seems better to leave it as is and document it in the developer's guide (in the section on producing new spkg's), and perhaps also in the installation guide (in the section on environment variables).  Here's a patch doing that; what do you think?",
    "created_at": "2011-03-26T17:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24931",
    "user": "https://github.com/jhpalmieri"
}
```

So right now, singular is the only place this is used, and it consistently uses "$RM -f", right?  Given this, rather than set `RM="rm -f"`, it seems better to leave it as is and document it in the developer's guide (in the section on producing new spkg's), and perhaps also in the installation guide (in the section on environment variables).  Here's a patch doing that; what do you think?



---

archive/issue_comments_024932.json:
```json
{
    "body": "Attachment [trac_3537-doc.patch](tarball://root/attachments/some-uuid/ticket3537/trac_3537-doc.patch) by @jhpalmieri created at 2011-03-26 17:04:47",
    "created_at": "2011-03-26T17:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24932",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_3537-doc.patch](tarball://root/attachments/some-uuid/ticket3537/trac_3537-doc.patch) by @jhpalmieri created at 2011-03-26 17:04:47



---

archive/issue_comments_024933.json:
```json
{
    "body": "My opinion still is that `RM` should simply be left unset (of course, a few install scripts will have to be changed).",
    "created_at": "2011-03-26T18:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24933",
    "user": "https://github.com/jdemeyer"
}
```

My opinion still is that `RM` should simply be left unset (of course, a few install scripts will have to be changed).



---

archive/issue_comments_024934.json:
```json
{
    "body": "Replying to [comment:18 jdemeyer]:\n> My opinion still is that `RM` should simply be left unset (of course, a few install scripts will have to be changed).\n\n\nI agree 100%. \n\nI can understand the logic of variables like $CC, $CXX, $MAKE, but not $RM. I don't know of any system where one might want to specify what version of `rm` gets used, so I don't see the point in having a variable for it. If some dump package needs `$RM` defined, then either try to fix the code so it is not so dumb, or add `$RM` to `dump_package.spkg`. \n\nBTW, take a look at\n\nhttp://boxen.math.washington.edu/home/kirkby/bad-code/sympow-1.018.1.p7/src/Configure\n\nwhere you will find some *interesting* use of variable names. A script which starts \n\n`#!/bin/sh`\n\nhas a function \n\n`whichexe()`\n\nThis function makes use of a non-POSIX command `which`, so there's no reason for `which` to exist. Then `whichexe()` function sets variables for things like SH, RM, SED, whilst checking if the commands (including `sh`) exist. If not the script exits. An abbreviated version is below. \n\n```/bin/sh\nwhichexe() {\n    if [ -f /bin/$1 ]; then\n        echo /bin/$1\n        return;\n    fi;\n    if [ -f /usr/bin/$1 ]; then\n        echo /usr/bin/$1\n        return;\n    fi;\n    if [ -f /usr/local/bin/$1 ]; then\n        echo /usr/local/bin/$1\n        return;\n    fi;\n    echo `which $1`\n}\nRM=`whichexe rm`\nGREP=`whichexe grep` && echo \"#define GREP \\\"$GREP\\\"\" >> $CONFIG\nSED=`whichexe sed` && echo \"#define SED \\\"$SED\\\"\" >> $CONFIG\nSH=`whichexe sh` && echo \"#define SH \\\"$SH\\\"\" >> $CONFIG\nif [ -z \"$SH\" ]; then\n  echo \"**ERROR**: Could not find sh\"; exit 1;\nelse\n  echo \"SH = $SH\"\nfi\n```\n\nI might have cleaned this up, so the current version in Sage might not be quite so dumb. \n\nDave",
    "created_at": "2011-03-26T18:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24934",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
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

archive/issue_comments_024935.json:
```json
{
    "body": "See #9497 for a patch to change \"$RM\" to \"rm\" in Singular's spkg-install script.",
    "created_at": "2011-03-26T23:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24935",
    "user": "https://github.com/jhpalmieri"
}
```

See #9497 for a patch to change "$RM" to "rm" in Singular's spkg-install script.



---

archive/issue_comments_024936.json:
```json
{
    "body": "When 50 percent or more of spkgs require $RM to be \"rm -f\" then\nchange $RM from \"rm\" to \"rm -f\".  Until then document.\n\nPositive review.",
    "created_at": "2011-05-12T14:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24936",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

When 50 percent or more of spkgs require $RM to be "rm -f" then
change $RM from "rm" to "rm -f".  Until then document.

Positive review.



---

archive/issue_comments_024937.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-12T14:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24937",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_024938.json:
```json
{
    "body": "Changing component from build to scripts.",
    "created_at": "2011-05-12T14:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24938",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from build to scripts.



---

archive/issue_comments_024939.json:
```json
{
    "body": "Singular's spkg-install no longer uses $RM, so the documentation is not up to date.",
    "created_at": "2011-05-12T14:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24939",
    "user": "https://github.com/jdemeyer"
}
```

Singular's spkg-install no longer uses $RM, so the documentation is not up to date.



---

archive/issue_events_008078.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-12T14:57:46Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3537#event-8078"
}
```



---

archive/issue_events_008079.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-12T14:57:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3537#event-8079"
}
```



---

archive/issue_comments_024940.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-05-12T14:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24940",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_024941.json:
```json
{
    "body": "Do not set $RM in sage-env",
    "created_at": "2011-05-12T14:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24941",
    "user": "https://github.com/jdemeyer"
}
```

Do not set $RM in sage-env



---

archive/issue_comments_024942.json:
```json
{
    "body": "Attachment [trac_3537-unset-RM.patch](tarball://root/attachments/some-uuid/ticket3537/trac_3537-unset-RM.patch) by mariah created at 2011-05-12 20:40:02\n\n[attachment:trac_3537-unset-RM.patch] applied to sage-4.7.rc2 tested on skynet/taurus with make testlong.  All tests passed.  Positive review.",
    "created_at": "2011-05-12T20:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24942",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Attachment [trac_3537-unset-RM.patch](tarball://root/attachments/some-uuid/ticket3537/trac_3537-unset-RM.patch) by mariah created at 2011-05-12 20:40:02

[attachment:trac_3537-unset-RM.patch] applied to sage-4.7.rc2 tested on skynet/taurus with make testlong.  All tests passed.  Positive review.



---

archive/issue_comments_024943.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-05-12T20:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24943",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_024944.json:
```json
{
    "body": "Replying to [comment:23 mariah]:\n> [attachment:trac_3537-unset-RM.patch] applied to sage-4.7.rc2 tested on skynet/taurus with make testlong.  All tests passed.  Positive review.\n\n\nDid you try building Sage from source with this patch applied?  Because this patch affects the Sage **build**, not the Sage library.",
    "created_at": "2011-05-12T20:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24944",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:23 mariah]:
> [attachment:trac_3537-unset-RM.patch] applied to sage-4.7.rc2 tested on skynet/taurus with make testlong.  All tests passed.  Positive review.


Did you try building Sage from source with this patch applied?  Because this patch affects the Sage **build**, not the Sage library.



---

archive/issue_comments_024945.json:
```json
{
    "body": "Apologies for not be clear.  I first applied the patch to the sage-4.7.rc2 source, then built the source, then did make testlong.",
    "created_at": "2011-05-13T13:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24945",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Apologies for not be clear.  I first applied the patch to the sage-4.7.rc2 source, then built the source, then did make testlong.



---

archive/issue_events_008080.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-17T08:47:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3537#event-8080"
}
```



---

archive/issue_comments_024946.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-17T08:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24946",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_024947.json:
```json
{
    "body": "I just checked all spkg-install scripts and `$RM` is used nowhere anymore.",
    "created_at": "2011-05-17T08:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3537#issuecomment-24947",
    "user": "https://github.com/jdemeyer"
}
```

I just checked all spkg-install scripts and `$RM` is used nowhere anymore.
