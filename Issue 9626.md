# Issue 9626: Update and extend "SPKG Tracking" Wiki page

Issue created by migration from Trac.

Original creator: leif

Original creation time: 2010-07-28 17:38:06

Assignee: mvngu, schilly

CC:  slelievre

Keywords: SPKG.txt spkgs documentation version release

The information given at http://wiki.sagemath.org/Sage_Spkg_Tracking is fairly out of date (and incomplete).

Perhaps we could add updating this page to the [release manager's task/check list](http://wiki.sagemath.org/devel/ReleaseManagement) (in case a new release includes updated spkgs).

I also consider adding a column "Upcoming" which people creating/updating spkgs can fill with the next version and, if appropriate, a link to the corresponding ticket. An alternative is to add a second _row_ for each upcoming spkg, just below the main row for that package, i.e. its current version within Sage.

Another useful column would be something like "Valid of", containing the date and/or Sage version each entry (row) has been updated last.

The column "Latest stable (upstream) release" is subject to change more or less frequently, independent of Sage releases; so if we keep it, it should perhaps continually be updated by the spkg maintainers, or at least carry a date, indicating when this information was entered.


---

Comment by leif created at 2010-07-28 17:39:12

Changing component from website/wiki to packages.


---

Comment by leif created at 2010-07-28 17:39:12

Changing status from new to needs_info.


---

Comment by mkoeppe created at 2020-07-08 16:35:15

Outdated, should be closed


---

Comment by mkoeppe created at 2020-07-08 16:35:15

Changing status from needs_info to needs_review.


---

Comment by @mwageringel created at 2020-08-13 20:25:45

Changing status from needs_review to positive_review.


---

Comment by slelievre created at 2020-08-14 00:54:07

Resolution: wontfix


---

Comment by slelievre created at 2020-08-14 00:54:07

The page http://wiki.sagemath.org/Sage_Spkg_Tracking
now redirects to http://wiki.sagemath.org/spkg
so this can indeed be closed.
