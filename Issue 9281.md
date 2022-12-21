# Issue 9281: METATICKET - missing spkg-check files / OpenSolaris test results.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-06-20 03:42:55

Assignee: tbd

CC:  jsp leif jpflori jakobkroeker chapoton

The purposes of this ticket are to 
 * Identify what standard packages have an spkg-check file present. At the time the ticket was opened, only 19 packages had spkg-check files out of 98 packages. (Some don't need them, such as where the package just copies a database)
 * Document whether the package builds on OpenSolaris x64
 * Document whether the package passes tests when Sage is built with SAGE_CHECK="yes" on OpenSolaris x64. 

The following lists: 

 * The standard packages in Sage
 * Whether the package builds on OpenSolaris x64
 * Whether the package has an spkg-check file
 * Test results when running 'make' while SAGE_CHECK="yes" on OpenSolaris x64
 * Notes, with ticket number if needed for resolving test issues.

The aim of this ticket is not to give details about build issues for the packages. For that, see #9026. The aim is to show what packages have spkg-check files, and collect data on what the results from the tests are. 



---

Comment by malb created at 2010-07-11 16:18:56

NB: It seems to me this ticket would fit better on the wiki since it is essentially a table.


---

Comment by drkirkby created at 2010-07-11 21:32:21

Replying to [comment:9 malb]:
> NB: It seems to me this ticket would fit better on the wiki since it is essentially a table.

Having it on a ticket seems quite common for this sort of thing. William calls it a 'metaticket'.If it on the Wiki, one can't see when something has been fixed. 

Dave


---

Comment by cremona created at 2010-07-16 16:39:24

pari itself has a "make test-all" so there is no reason why we should not have a spkg-test in the pari spkg.


---

Comment by drkirkby created at 2010-07-16 17:16:31

That's now #9281.


---

Comment by leif created at 2010-07-16 19:10:37

I think we should separate the _presence_ of `spkg-check` from testsuite results, i.e. create a single platform-independent ticket that lists spkg improvement progress.

In addition, some packages might do self-tests during build unconditionally, others do not even have a `check` or `test` Make target or some equivalent. This should be recorded, too.

----

I strongly suggest extending `sage-spkg` s.t. Sage _build_ failure on _testsuite_ errors gets optional, and an option to continue with installation until all packages have been processed, then reporting in summary which packages were tested and which had failures, similar to the doctesting.

More complicated, but nice, would be to separate testsuite logs from install logs. (`spkg/installed/PKG_NAME` currently at least shows when a self-test was _successfully_ performed, but if it failed, the file is of course removed, since this is considered a _build_/installation error.)


---

Comment by leif created at 2010-07-16 19:26:40

Replying to [comment:14 leif]:
> (`spkg/installed/PKG_NAME` currently at least shows when a self-test was _successfully_ performed, but if it failed, the file is of course removed, since this is considered a _build_/installation error.)

Ooops, due to a bug in `sage-spkg`, not even this information is kept. (It is echoed into `$BASEDIR/$PKG_NAME`, which is deleted later unless one does e.g. `sage -i -s ...`.)


---

Comment by drkirkby created at 2010-07-16 21:36:48

Replying to [comment:14 leif]:
> I think we should separate the _presence_ of `spkg-check` from testsuite results, i.e. create a single platform-independent ticket that lists spkg improvement progress.

Feel free. I would not argue with that. Either copy my list, or generate it yourself - all I did was list the packages in `$SAGE_ROOT/spkg/standard` and use an _awk_ script to generate the table. I guess if you were clever, you could get the script to automatically put "Yes" or "No", depending on whether there was an spkg-check file present! I just did that bit manually. 

I just created this ticket, as a way to keep trac of the OpenSolaris issues. However, in order to have any sensible idea of progress on OpenSolaris, I needed to have a record of what packages had no self-checks. 

> In addition, some packages might do self-tests during build unconditionally, others do not even have a `check` or `test` Make target or some equivalent. This should be recorded, too.

I seriously think we should consider running the self-tests unconditionally on packages where this takes very little time. Some packages take less than 10 seconds to run the self-tests. I think any package where the self-test take less than 30 or perhaps 60 s on sage.math, should have the self-tests run unconditionally. I posted this as a suggestion on sage-devel, but it got no response - there does not seem to be a huge appetite for testing Sage. I think there is less than a dozen people who really seem to put much effort into improving the testing of Sage. 

> I strongly suggest extending `sage-spkg` s.t. Sage _build_ failure on _testsuite_ errors gets optional, and an option to continue with installation until all packages have been processed, then reporting in summary which packages were tested and which had failures, similar to the doctesting.

Yes, that sounds logical. If you know something builds, you can run ` make -k` I guess, and continue past errors when testing. 

> More complicated, but nice, would be to separate testsuite logs from install logs. 

I would have thought that easier than producing a summary myself. I don't believe that can be rocket science.


---

Comment by drkirkby created at 2010-07-16 21:40:26

Changing assignee from tbd to drkirkby.


---

Comment by leif created at 2010-07-16 23:38:56

Replying to [comment:16 drkirkby]:
> Replying to [comment:14 leif]:
> > In addition, some packages might do self-tests during build unconditionally, others do not even have a `check` or `test` Make target or some equivalent. This should be recorded, too.

I meant tests unconditionally performed by upstream (i.e. implicitly, without "make check" or alike).

> > I strongly suggest extending `sage-spkg` s.t. Sage _build_ failure on _testsuite_ errors gets optional, and an option to continue with installation until all packages have been processed, then reporting in summary which packages were tested and which had failures, similar to the doctesting.
> 
> Yes, that sounds logical. If you know something builds, you can run ` make -k` I guess, and continue past errors when testing.

;-) `sage-spkg` currently treats testsuite failures as build errors, so `make -k` would not get (much) further if other packages depend on the "failed" ones; rerunning `make` just _deletes_ their previous builds, _again unpacks_ these packages and starts _rebuilding them from scratch_(!) - again "failing", unless one *manually* touches `spkg/installed/$PKG_NAME`, which `sage-spkg` just has deleted...
 
> > More complicated, but nice, would be to separate testsuite logs from install logs. 
> 
> I would have thought that easier than producing a summary myself. I don't believe that can be rocket science. 

It's not rocket science (if you consider that complicated), but Sage's current build process is rather unsuited for such. Though one could of course _post_-process the spkg install logs, where also testsuite output ends up.

In contrast, "ignoring" testsuite failures (even if `SAGE_CHECK=yes`) and printing a summary report is almost trivial, the biggest "problem" being choosing new appropriate environment variable names or extending the "range" of existing ones with additional values (like `SAGE_CHECK_KEEP_GOING=yes` vs. `SAGE_CHECK=keepgoing`; `SAGE_CHECK=ignore` e.g. would be rather ambiguous, and we unfortunately have to keep some backwards compatibility).


---

Comment by drkirkby created at 2010-07-16 23:59:26

Replying to [comment:18 leif]:
> In contrast, "ignoring" testsuite failures (even if `SAGE_CHECK=yes`) and printing a summary report is almost trivial, the biggest "problem" being choosing new appropriate environment variable names or extending the "range" of existing ones with additional values (like `SAGE_CHECK_KEEP_GOING=yes` vs. `SAGE_CHECK=keepgoing`; `SAGE_CHECK=ignore` e.g. would be rather ambiguous, and we unfortunately have to keep some backwards compatibility).
> 

If it's trivial, then go for it - make a patch. Personally I think

 * `SAGE_CHECK=yes` (Same behavior as now, but issued a depreciated warning.)
 * `SAGE_CHECK=abort_on_failure`
 * `SAGE_CHECK=ignore_failures`


---

Comment by leif created at 2010-07-17 00:35:47

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
 * `SAGE_CHECK=ignore_failures` - really ignore, just give warnings, report _build_ success
 * `SAGE_CHECK=no` - do not run testsuites at all (same as empty or unset?)


---

Comment by drkirkby created at 2010-07-17 19:48:35

Replying to [comment:14 leif]:
> I think we should separate the _presence_ of `spkg-check` from testsuite results, i.e. create a single platform-independent ticket that lists spkg improvement progress.

I thought about this some more. I can't see what is wrong with using this ticket to have a simple yes/no whether the package has a `spkg-check` file. If not, just provide a trac number to where that particular spkg-check file is being discussed. For gsl for instance, we have 

"Yes, but broken #9531"

So people interested know that more details of the issue can be found at #9531.  

If you feel the need to have longer comments, or more columns devoted to the status of `spkg-check` then another ticket would be better. 

When you look at the `spkg-install` and `spkg-check` it is worrying how many simple ignore errors. Sometimes they get reported, but don't exit with 1. Other times they are just ignored. 

Dave


---

Comment by leif created at 2010-07-17 20:14:28

Replying to [comment:27 drkirkby]:
> Replying to [comment:14 leif]:
> > I think we should separate the _presence_ of `spkg-check` from testsuite results, i.e. create a single platform-independent ticket that lists spkg improvement progress.
> 
> I thought about this some more. I can't see what is wrong with using this ticket to have a simple yes/no whether the package has a `spkg-check` file.

No, you misunderstood me. There's nothing wrong with your ticket, I just thought we should _in addition_ collect spkg information, e.g. on another ticket. I haven't opened a new one yet, though what you collected so far is already worth stealing.


> When you look at the `spkg-install` and `spkg-check` it is worrying how many simple ignore errors. Sometimes they get reported, but don't exit with 1. Other times they are just ignored. 

If it was only the spkgs' scripts... ;-)

-Leif


---

Comment by mkoeppe created at 2020-04-01 14:09:06

Should be closed as outdated.


---

Comment by mkoeppe created at 2020-04-01 14:09:06

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-04-01 14:22:15

Resolution: invalid


---

Comment by chapoton created at 2020-04-01 14:22:15

ok, agreed.
