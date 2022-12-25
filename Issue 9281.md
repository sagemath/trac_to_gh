# Issue 9281: METATICKET - missing spkg-check files / OpenSolaris & Solaris 10 test results.

archive/issues_009281.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies @nexttime jpflori jakobkroeker @fchapoton\n\nThe purposes of this ticket are to\n\n* Identify what standard packages have an spkg-check file present. At the time the ticket was opened, only 19 packages had spkg-check files out of 98 packages. (Some don't need them, such as where the package just copies a database)\n* Document whether the package passes tests when Sage is built with SAGE_CHECK=\"yes\" on OpenSolaris x64. (Currently, neither Maxima or R build on OpenSolaris, and the resulting build is very unstable - segfaulting just trying to run it). \n* Document whether the package passes tests when Sage is built with SAGE_CHECK=\"yes\" on Solaris 10 on SPARC, compiled as 32-bit.\n* Document whether the package passes tests when Sage is built with SAGE_CHECK=\"yes\" on Solaris 10 on SPARC, compiled as 64-bit. (Currently, the 64-bit build of Sage needs various patches, and is rather unstable)\n* Add any **brief** notes - giving a reference to a ticket number if possible. \n\nThe aim of this ticket is not to give details about build issues for the packages. The aim is to show what packages have spkg-check files, and collect data on what the results from the tests are.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9281\n\n",
    "closed_at": "2020-04-01T14:22:15Z",
    "created_at": "2010-06-20T03:42:55Z",
    "labels": [
        "component: spkg-check",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "METATICKET - missing spkg-check files / OpenSolaris & Solaris 10 test results.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9281",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies @nexttime jpflori jakobkroeker @fchapoton

The purposes of this ticket are to

* Identify what standard packages have an spkg-check file present. At the time the ticket was opened, only 19 packages had spkg-check files out of 98 packages. (Some don't need them, such as where the package just copies a database)
* Document whether the package passes tests when Sage is built with SAGE_CHECK="yes" on OpenSolaris x64. (Currently, neither Maxima or R build on OpenSolaris, and the resulting build is very unstable - segfaulting just trying to run it). 
* Document whether the package passes tests when Sage is built with SAGE_CHECK="yes" on Solaris 10 on SPARC, compiled as 32-bit.
* Document whether the package passes tests when Sage is built with SAGE_CHECK="yes" on Solaris 10 on SPARC, compiled as 64-bit. (Currently, the 64-bit build of Sage needs various patches, and is rather unstable)
* Add any **brief** notes - giving a reference to a ticket number if possible. 

The aim of this ticket is not to give details about build issues for the packages. The aim is to show what packages have spkg-check files, and collect data on what the results from the tests are.


Issue created by migration from https://trac.sagemath.org/ticket/9281





---

archive/issue_comments_087285.json:
```json
{
    "body": "NB: It seems to me this ticket would fit better on the wiki since it is essentially a table.",
    "created_at": "2010-07-11T16:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87285",
    "user": "https://github.com/malb"
}
```

NB: It seems to me this ticket would fit better on the wiki since it is essentially a table.



---

archive/issue_comments_087286.json:
```json
{
    "body": "Replying to [comment:9 malb]:\n> NB: It seems to me this ticket would fit better on the wiki since it is essentially a table.\n\n\nHaving it on a ticket seems quite common for this sort of thing. William calls it a 'metaticket'.If it on the Wiki, one can't see when something has been fixed. \n\nDave",
    "created_at": "2010-07-11T21:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87286",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:9 malb]:
> NB: It seems to me this ticket would fit better on the wiki since it is essentially a table.


Having it on a ticket seems quite common for this sort of thing. William calls it a 'metaticket'.If it on the Wiki, one can't see when something has been fixed. 

Dave



---

archive/issue_comments_087287.json:
```json
{
    "body": "pari itself has a \"make test-all\" so there is no reason why we should not have a spkg-test in the pari spkg.",
    "created_at": "2010-07-16T16:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87287",
    "user": "https://github.com/JohnCremona"
}
```

pari itself has a "make test-all" so there is no reason why we should not have a spkg-test in the pari spkg.



---

archive/issue_comments_087288.json:
```json
{
    "body": "That's now #9281.",
    "created_at": "2010-07-16T17:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87288",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

That's now #9281.



---

archive/issue_comments_087289.json:
```json
{
    "body": "I think we should separate the *presence* of `spkg-check` from testsuite results, i.e. create a single platform-independent ticket that lists spkg improvement progress.\n\nIn addition, some packages might do self-tests during build unconditionally, others do not even have a `check` or `test` Make target or some equivalent. This should be recorded, too.\n\n---\n\nI strongly suggest extending `sage-spkg` s.t. Sage *build* failure on *testsuite* errors gets optional, and an option to continue with installation until all packages have been processed, then reporting in summary which packages were tested and which had failures, similar to the doctesting.\n\nMore complicated, but nice, would be to separate testsuite logs from install logs. (`spkg/installed/PKG_NAME` currently at least shows when a self-test was *successfully* performed, but if it failed, the file is of course removed, since this is considered a *build*/installation error.)",
    "created_at": "2010-07-16T19:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87289",
    "user": "https://github.com/nexttime"
}
```

I think we should separate the *presence* of `spkg-check` from testsuite results, i.e. create a single platform-independent ticket that lists spkg improvement progress.

In addition, some packages might do self-tests during build unconditionally, others do not even have a `check` or `test` Make target or some equivalent. This should be recorded, too.

---

I strongly suggest extending `sage-spkg` s.t. Sage *build* failure on *testsuite* errors gets optional, and an option to continue with installation until all packages have been processed, then reporting in summary which packages were tested and which had failures, similar to the doctesting.

More complicated, but nice, would be to separate testsuite logs from install logs. (`spkg/installed/PKG_NAME` currently at least shows when a self-test was *successfully* performed, but if it failed, the file is of course removed, since this is considered a *build*/installation error.)



---

archive/issue_comments_087290.json:
```json
{
    "body": "Replying to [comment:14 leif]:\n> (`spkg/installed/PKG_NAME` currently at least shows when a self-test was *successfully* performed, but if it failed, the file is of course removed, since this is considered a *build*/installation error.)\n\n\nOoops, due to a bug in `sage-spkg`, not even this information is kept. (It is echoed into `$BASEDIR/$PKG_NAME`, which is deleted later unless one does e.g. `sage -i -s ...`.)",
    "created_at": "2010-07-16T19:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87290",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:14 leif]:
> (`spkg/installed/PKG_NAME` currently at least shows when a self-test was *successfully* performed, but if it failed, the file is of course removed, since this is considered a *build*/installation error.)


Ooops, due to a bug in `sage-spkg`, not even this information is kept. (It is echoed into `$BASEDIR/$PKG_NAME`, which is deleted later unless one does e.g. `sage -i -s ...`.)



---

archive/issue_comments_087291.json:
```json
{
    "body": "Replying to [comment:14 leif]:\n> I think we should separate the *presence* of `spkg-check` from testsuite results, i.e. create a single platform-independent ticket that lists spkg improvement progress.\n\n\nFeel free. I would not argue with that. Either copy my list, or generate it yourself - all I did was list the packages in `$SAGE_ROOT/spkg/standard` and use an *awk* script to generate the table. I guess if you were clever, you could get the script to automatically put \"Yes\" or \"No\", depending on whether there was an spkg-check file present! I just did that bit manually. \n\nI just created this ticket, as a way to keep trac of the OpenSolaris issues. However, in order to have any sensible idea of progress on OpenSolaris, I needed to have a record of what packages had no self-checks. \n\n> In addition, some packages might do self-tests during build unconditionally, others do not even have a `check` or `test` Make target or some equivalent. This should be recorded, too.\n\n\nI seriously think we should consider running the self-tests unconditionally on packages where this takes very little time. Some packages take less than 10 seconds to run the self-tests. I think any package where the self-test take less than 30 or perhaps 60 s on sage.math, should have the self-tests run unconditionally. I posted this as a suggestion on sage-devel, but it got no response - there does not seem to be a huge appetite for testing Sage. I think there is less than a dozen people who really seem to put much effort into improving the testing of Sage. \n\n> I strongly suggest extending `sage-spkg` s.t. Sage *build* failure on *testsuite* errors gets optional, and an option to continue with installation until all packages have been processed, then reporting in summary which packages were tested and which had failures, similar to the doctesting.\n\n\nYes, that sounds logical. If you know something builds, you can run ` make -k` I guess, and continue past errors when testing. \n\n> More complicated, but nice, would be to separate testsuite logs from install logs. \n\n\nI would have thought that easier than producing a summary myself. I don't believe that can be rocket science.",
    "created_at": "2010-07-16T21:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87291",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:14 leif]:
> I think we should separate the *presence* of `spkg-check` from testsuite results, i.e. create a single platform-independent ticket that lists spkg improvement progress.


Feel free. I would not argue with that. Either copy my list, or generate it yourself - all I did was list the packages in `$SAGE_ROOT/spkg/standard` and use an *awk* script to generate the table. I guess if you were clever, you could get the script to automatically put "Yes" or "No", depending on whether there was an spkg-check file present! I just did that bit manually. 

I just created this ticket, as a way to keep trac of the OpenSolaris issues. However, in order to have any sensible idea of progress on OpenSolaris, I needed to have a record of what packages had no self-checks. 

> In addition, some packages might do self-tests during build unconditionally, others do not even have a `check` or `test` Make target or some equivalent. This should be recorded, too.


I seriously think we should consider running the self-tests unconditionally on packages where this takes very little time. Some packages take less than 10 seconds to run the self-tests. I think any package where the self-test take less than 30 or perhaps 60 s on sage.math, should have the self-tests run unconditionally. I posted this as a suggestion on sage-devel, but it got no response - there does not seem to be a huge appetite for testing Sage. I think there is less than a dozen people who really seem to put much effort into improving the testing of Sage. 

> I strongly suggest extending `sage-spkg` s.t. Sage *build* failure on *testsuite* errors gets optional, and an option to continue with installation until all packages have been processed, then reporting in summary which packages were tested and which had failures, similar to the doctesting.


Yes, that sounds logical. If you know something builds, you can run ` make -k` I guess, and continue past errors when testing. 

> More complicated, but nice, would be to separate testsuite logs from install logs. 


I would have thought that easier than producing a summary myself. I don't believe that can be rocket science.



---

archive/issue_comments_087292.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2010-07-16T21:40:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87292",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_087293.json:
```json
{
    "body": "Replying to [comment:16 drkirkby]:\n> Replying to [comment:14 leif]:\n> > In addition, some packages might do self-tests during build unconditionally, others do not even have a `check` or `test` Make target or some equivalent. This should be recorded, too.\n\n\nI meant tests unconditionally performed by upstream (i.e. implicitly, without \"make check\" or alike).\n\n> > I strongly suggest extending `sage-spkg` s.t. Sage *build* failure on *testsuite* errors gets optional, and an option to continue with installation until all packages have been processed, then reporting in summary which packages were tested and which had failures, similar to the doctesting.\n\n> \n> Yes, that sounds logical. If you know something builds, you can run ` make -k` I guess, and continue past errors when testing.\n\n\n;-) `sage-spkg` currently treats testsuite failures as build errors, so `make -k` would not get (much) further if other packages depend on the \"failed\" ones; rerunning `make` just *deletes* their previous builds, *again unpacks* these packages and starts *rebuilding them from scratch*(!) - again \"failing\", unless one **manually** touches `spkg/installed/$PKG_NAME`, which `sage-spkg` just has deleted...\n \n> > More complicated, but nice, would be to separate testsuite logs from install logs. \n\n> \n> I would have thought that easier than producing a summary myself. I don't believe that can be rocket science. \n\n\nIt's not rocket science (if you consider that complicated), but Sage's current build process is rather unsuited for such. Though one could of course *post*-process the spkg install logs, where also testsuite output ends up.\n\nIn contrast, \"ignoring\" testsuite failures (even if `SAGE_CHECK=yes`) and printing a summary report is almost trivial, the biggest \"problem\" being choosing new appropriate environment variable names or extending the \"range\" of existing ones with additional values (like `SAGE_CHECK_KEEP_GOING=yes` vs. `SAGE_CHECK=keepgoing`; `SAGE_CHECK=ignore` e.g. would be rather ambiguous, and we unfortunately have to keep some backwards compatibility).",
    "created_at": "2010-07-16T23:38:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87293",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:16 drkirkby]:
> Replying to [comment:14 leif]:
> > In addition, some packages might do self-tests during build unconditionally, others do not even have a `check` or `test` Make target or some equivalent. This should be recorded, too.


I meant tests unconditionally performed by upstream (i.e. implicitly, without "make check" or alike).

> > I strongly suggest extending `sage-spkg` s.t. Sage *build* failure on *testsuite* errors gets optional, and an option to continue with installation until all packages have been processed, then reporting in summary which packages were tested and which had failures, similar to the doctesting.

> 
> Yes, that sounds logical. If you know something builds, you can run ` make -k` I guess, and continue past errors when testing.


;-) `sage-spkg` currently treats testsuite failures as build errors, so `make -k` would not get (much) further if other packages depend on the "failed" ones; rerunning `make` just *deletes* their previous builds, *again unpacks* these packages and starts *rebuilding them from scratch*(!) - again "failing", unless one **manually** touches `spkg/installed/$PKG_NAME`, which `sage-spkg` just has deleted...
 
> > More complicated, but nice, would be to separate testsuite logs from install logs. 

> 
> I would have thought that easier than producing a summary myself. I don't believe that can be rocket science. 


It's not rocket science (if you consider that complicated), but Sage's current build process is rather unsuited for such. Though one could of course *post*-process the spkg install logs, where also testsuite output ends up.

In contrast, "ignoring" testsuite failures (even if `SAGE_CHECK=yes`) and printing a summary report is almost trivial, the biggest "problem" being choosing new appropriate environment variable names or extending the "range" of existing ones with additional values (like `SAGE_CHECK_KEEP_GOING=yes` vs. `SAGE_CHECK=keepgoing`; `SAGE_CHECK=ignore` e.g. would be rather ambiguous, and we unfortunately have to keep some backwards compatibility).



---

archive/issue_comments_087294.json:
```json
{
    "body": "Replying to [comment:18 leif]:\n> In contrast, \"ignoring\" testsuite failures (even if `SAGE_CHECK=yes`) and printing a summary report is almost trivial, the biggest \"problem\" being choosing new appropriate environment variable names or extending the \"range\" of existing ones with additional values (like `SAGE_CHECK_KEEP_GOING=yes` vs. `SAGE_CHECK=keepgoing`; `SAGE_CHECK=ignore` e.g. would be rather ambiguous, and we unfortunately have to keep some backwards compatibility).\n> \n\n\nIf it's trivial, then go for it - make a patch. Personally I think\n\n* `SAGE_CHECK=yes` (Same behavior as now, but issued a depreciated warning.)\n* `SAGE_CHECK=abort_on_failure`\n* `SAGE_CHECK=ignore_failures`",
    "created_at": "2010-07-16T23:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87294",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:18 leif]:
> In contrast, "ignoring" testsuite failures (even if `SAGE_CHECK=yes`) and printing a summary report is almost trivial, the biggest "problem" being choosing new appropriate environment variable names or extending the "range" of existing ones with additional values (like `SAGE_CHECK_KEEP_GOING=yes` vs. `SAGE_CHECK=keepgoing`; `SAGE_CHECK=ignore` e.g. would be rather ambiguous, and we unfortunately have to keep some backwards compatibility).
> 


If it's trivial, then go for it - make a patch. Personally I think

* `SAGE_CHECK=yes` (Same behavior as now, but issued a depreciated warning.)
* `SAGE_CHECK=abort_on_failure`
* `SAGE_CHECK=ignore_failures`



---

archive/issue_comments_087295.json:
```json
{
    "body": "Replying to [comment:19 drkirkby]:\n> If it's trivial, then go for it - make a patch.\n\nThe biggest problem more or less unpredictable (and embarrassing) interference with other tickets... ;-)\n\nBut I'll do.\n\n> Personally I think:\n* `SAGE_CHECK=yes` (Same behavior as now, but issued a depreciated warning.)\n* `SAGE_CHECK=abort_on_failure`\n* `SAGE_CHECK=ignore_failures`\n \nI'd suggest:\n* `SAGE_CHECK=yes` - yes, deprecation warning, equivalent to `abort_on_failure` I think\n* `SAGE_CHECK=abort_on_failure` - immediate build error\n* `SAGE_CHECK=keep_going` - treat them as (build) errors, but try finishing the build first\n* `SAGE_CHECK=ignore_failures` - really ignore, just give warnings, report *build* success\n* `SAGE_CHECK=no` - do not run testsuites at all (same as empty or unset?)",
    "created_at": "2010-07-17T00:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87295",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:19 drkirkby]:
> If it's trivial, then go for it - make a patch.

The biggest problem more or less unpredictable (and embarrassing) interference with other tickets... ;-)

But I'll do.

> Personally I think:
* `SAGE_CHECK=yes` (Same behavior as now, but issued a depreciated warning.)
* `SAGE_CHECK=abort_on_failure`
* `SAGE_CHECK=ignore_failures`
 
I'd suggest:
* `SAGE_CHECK=yes` - yes, deprecation warning, equivalent to `abort_on_failure` I think
* `SAGE_CHECK=abort_on_failure` - immediate build error
* `SAGE_CHECK=keep_going` - treat them as (build) errors, but try finishing the build first
* `SAGE_CHECK=ignore_failures` - really ignore, just give warnings, report *build* success
* `SAGE_CHECK=no` - do not run testsuites at all (same as empty or unset?)



---

archive/issue_events_022863.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2010-07-17T12:15:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9281#event-22863"
}
```



---

archive/issue_comments_087296.json:
```json
{
    "body": "Replying to [comment:14 leif]:\n> I think we should separate the *presence* of `spkg-check` from testsuite results, i.e. create a single platform-independent ticket that lists spkg improvement progress.\n\n\nI thought about this some more. I can't see what is wrong with using this ticket to have a simple yes/no whether the package has a `spkg-check` file. If not, just provide a trac number to where that particular spkg-check file is being discussed. For gsl for instance, we have \n\n\"Yes, but broken #9531\"\n\nSo people interested know that more details of the issue can be found at #9531.  \n\nIf you feel the need to have longer comments, or more columns devoted to the status of `spkg-check` then another ticket would be better. \n\nWhen you look at the `spkg-install` and `spkg-check` it is worrying how many simple ignore errors. Sometimes they get reported, but don't exit with 1. Other times they are just ignored. \n\nDave",
    "created_at": "2010-07-17T19:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87296",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:14 leif]:
> I think we should separate the *presence* of `spkg-check` from testsuite results, i.e. create a single platform-independent ticket that lists spkg improvement progress.


I thought about this some more. I can't see what is wrong with using this ticket to have a simple yes/no whether the package has a `spkg-check` file. If not, just provide a trac number to where that particular spkg-check file is being discussed. For gsl for instance, we have 

"Yes, but broken #9531"

So people interested know that more details of the issue can be found at #9531.  

If you feel the need to have longer comments, or more columns devoted to the status of `spkg-check` then another ticket would be better. 

When you look at the `spkg-install` and `spkg-check` it is worrying how many simple ignore errors. Sometimes they get reported, but don't exit with 1. Other times they are just ignored. 

Dave



---

archive/issue_comments_087297.json:
```json
{
    "body": "Replying to [comment:27 drkirkby]:\n> Replying to [comment:14 leif]:\n> > I think we should separate the *presence* of `spkg-check` from testsuite results, i.e. create a single platform-independent ticket that lists spkg improvement progress.\n\n> \n> I thought about this some more. I can't see what is wrong with using this ticket to have a simple yes/no whether the package has a `spkg-check` file.\n\n\nNo, you misunderstood me. There's nothing wrong with your ticket, I just thought we should *in addition* collect spkg information, e.g. on another ticket. I haven't opened a new one yet, though what you collected so far is already worth stealing.\n\n\n> When you look at the `spkg-install` and `spkg-check` it is worrying how many simple ignore errors. Sometimes they get reported, but don't exit with 1. Other times they are just ignored. \n\n\nIf it was only the spkgs' scripts... ;-)\n\n-Leif",
    "created_at": "2010-07-17T20:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87297",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:27 drkirkby]:
> Replying to [comment:14 leif]:
> > I think we should separate the *presence* of `spkg-check` from testsuite results, i.e. create a single platform-independent ticket that lists spkg improvement progress.

> 
> I thought about this some more. I can't see what is wrong with using this ticket to have a simple yes/no whether the package has a `spkg-check` file.


No, you misunderstood me. There's nothing wrong with your ticket, I just thought we should *in addition* collect spkg information, e.g. on another ticket. I haven't opened a new one yet, though what you collected so far is already worth stealing.


> When you look at the `spkg-install` and `spkg-check` it is worrying how many simple ignore errors. Sometimes they get reported, but don't exit with 1. Other times they are just ignored. 


If it was only the spkgs' scripts... ;-)

-Leif



---

archive/issue_comments_087298.json:
```json
{
    "body": "Should be closed as outdated.",
    "created_at": "2020-04-01T14:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87298",
    "user": "https://github.com/mkoeppe"
}
```

Should be closed as outdated.



---

archive/issue_comments_087299.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-04-01T14:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87299",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087300.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-04-01T14:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87300",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_comments_087301.json:
```json
{
    "body": "ok, agreed.",
    "created_at": "2020-04-01T14:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9281#issuecomment-87301",
    "user": "https://github.com/fchapoton"
}
```

ok, agreed.



---

archive/issue_events_022864.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-04-01T14:22:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9281",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9281#event-22864"
}
```
