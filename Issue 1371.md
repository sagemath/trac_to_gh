# Issue 1371: hg_sage.pull/push() to non-default server with multiple branches

Issue created by migration from Trac.

Original creator: jonhanke

Original creation time: 2007-12-02 14:40:45

Assignee: was

Keywords: push, mercurial, branches

I noticed that the push() method was missing in sage-2.8.14, so here is a
patch.  I also added current_branch() and list_branches() for the
convenience of those who may want to manage multiple branches
simultaneously.

I was also interested in being able to have a separate default outgoing
repository for convenient backups, but there is an organizational issue here
-- SAGE has hardcoded its default branch (on the server) as sage-main, so if
one wanted to manage multiple branches from the same repository (as might
happen if there were several branches being simultaneously pulled/pushed to
on the same server) they will break the default scheme.  So I forced the
hardcoded default server to use only the "main" branch (and updated the
hardcoded server to be sagemath.org instead of sage.math.washington.edu).

For example, suppose one wants to have a server with two branches: sage-main
and sage-other on the non-default server math.awesome.edu.  Then the way
things are coded now, sage-main would update from sage-main, and
sage-other would update from sage-other.  If we were connecting to the
default sagemath.org, then both branches would update from sage-main.
(WARNING TO MAINTAINER: This means that if the default server is changed,
one must also explicitly change the DEFAULT_SERVER variable in
BRANCH_PATH/sage/misc/hg.py)

If a non-default outgoing server is set, then commands like hg_sage.bundle() will use it for determining the relevant changesets, so a bundle to commit to sagemath.org would meet to specify the incoming server explicity.  For example, this bundle was created with:

    hg_sage.bundle("push_bundle--Dec_2_2007", url=hg_sage.pull_url())

Finally, I didn't really understand where the default_server was set, so I
added support to set them from shell variables SAGE_INCOMING_SERVER and
SAGE_OUTGOING_SERVER (with no trailing '/', in mercurial path format to the
'...../devel' directory).  However I was careful to preserve the default
behavior when no settings are present.  Any comments are appreciated! 




---

Attachment

Changesets


---

Comment by ncalexan created at 2008-01-22 18:56:03

This should be applied, assuming that it does not change the default behaviour.  (It should not.)  It does look like there is an incorrectly indented line, but compiling should catch that.

I do worry about the copyright change, though -- I thought we agreed to give all the copyright's to William Stein, to ease future license changes.  We should check if Jon Hanke is okay with that?


---

Comment by was created at 2008-01-22 22:13:41

> I do worry about the copyright change, though -- I thought we agreed 
> to give all the copyright's to William Stein, to ease future license 
> changes. We should check if Jon Hanke is okay with that?

We did not agree to do that.  Some people did, but it is completely
optional.  The key requirement is that all code in the core Sage library 
be licensed  "GPL V2 or greater". The copyright holder can be anybody.


---

Comment by ncalexan created at 2008-02-09 03:42:27

After discussion with William at SD7, this should be applied.


---

Comment by mabshoff created at 2008-02-10 01:12:49

Resolution: fixed


---

Comment by mabshoff created at 2008-02-10 01:12:49

Merged in Sage 2.10.2.alpha0
