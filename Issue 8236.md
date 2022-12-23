# Issue 8236: installing spkg from remote location must leave a spkg (placeholder) in spkg/

Issue created by migration from https://trac.sagemath.org/ticket/8236

Original creator: dimpase

Original creation time: 2010-02-11 05:41:08

Assignee: GeorgSWeber

Keywords: spkg, installation

When one does sage -f (or -i) from a remote location, the
spkg file is not stored locally in the appropriate place,
even if an upgrade of a standard spkg has taken place.
As a result, the script spkg/standard/newest_version may fail
to detect that the upgrade has taken place.

As a solution, one can either store the full downloaded spkg, or
just a placeholder with (almost) the same name as the spkg file.

Or, perhaps, sage -i (-f) can call spkg/standard/newest_version to see if an upgrade is happening, and act accordingly.

This bug has cost me and wdj hours of wasted time, see #8229.


---

Comment by dimpase created at 2010-03-29 10:11:31

This issue was discussed here:
[http://groups.google.com/group/sage-devel/browse_thread/thread/89dfb53b34153fbe/605960774d6efa77?#605960774d6efa77](http://groups.google.com/group/sage-devel/browse_thread/thread/89dfb53b34153fbe/605960774d6efa77?#605960774d6efa77)

in a nutshell, newest_version should not be used for these tasks, 
and a new script has to be written.


---

Comment by dimpase created at 2010-03-29 10:11:31

Changing status from new to needs_info.


---

Comment by jdemeyer created at 2013-12-29 23:32:28

Changing status from needs_info to needs_review.


---

Comment by jdemeyer created at 2013-12-29 23:32:28

It's not exactly clear what this bug is about, but given the many changes to `sage-spkg`, it's a good bet to assume that it's fixed.


---

Comment by jdemeyer created at 2013-12-29 23:33:28

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-01-04 02:39:06

Resolution: wontfix
