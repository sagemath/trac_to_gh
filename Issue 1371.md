# Issue 1371: hg_sage.pull/push() to non-default server with multiple branches

archive/issues_001371.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: push, mercurial, branches\n\nI noticed that the push() method was missing in sage-2.8.14, so here is a\npatch.  I also added current_branch() and list_branches() for the\nconvenience of those who may want to manage multiple branches\nsimultaneously.\n\nI was also interested in being able to have a separate default outgoing\nrepository for convenient backups, but there is an organizational issue here\n-- SAGE has hardcoded its default branch (on the server) as sage-main, so if\none wanted to manage multiple branches from the same repository (as might\nhappen if there were several branches being simultaneously pulled/pushed to\non the same server) they will break the default scheme.  So I forced the\nhardcoded default server to use only the \"main\" branch (and updated the\nhardcoded server to be sagemath.org instead of sage.math.washington.edu).\n\nFor example, suppose one wants to have a server with two branches: sage-main\nand sage-other on the non-default server math.awesome.edu.  Then the way\nthings are coded now, sage-main would update from sage-main, and\nsage-other would update from sage-other.  If we were connecting to the\ndefault sagemath.org, then both branches would update from sage-main.\n(WARNING TO MAINTAINER: This means that if the default server is changed,\none must also explicitly change the DEFAULT_SERVER variable in\nBRANCH_PATH/sage/misc/hg.py)\n\nIf a non-default outgoing server is set, then commands like hg_sage.bundle() will use it for determining the relevant changesets, so a bundle to commit to sagemath.org would meet to specify the incoming server explicity.  For example, this bundle was created with:\n\n    hg_sage.bundle(\"push_bundle--Dec_2_2007\", url=hg_sage.pull_url())\n\nFinally, I didn't really understand where the default_server was set, so I\nadded support to set them from shell variables SAGE_INCOMING_SERVER and\nSAGE_OUTGOING_SERVER (with no trailing '/', in mercurial path format to the\n'...../devel' directory).  However I was careful to preserve the default\nbehavior when no settings are present.  Any comments are appreciated! \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1371\n\n",
    "created_at": "2007-12-02T14:40:45Z",
    "labels": [
        "component: interfaces",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "hg_sage.pull/push() to non-default server with multiple branches",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1371",
    "user": "https://github.com/jonhanke"
}
```
Assignee: @williamstein

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



Issue created by migration from https://trac.sagemath.org/ticket/1371





---

archive/issue_comments_008775.json:
```json
{
    "body": "Attachment [push_bundle--Dec_2_2007.hg](tarball://root/attachments/some-uuid/ticket1371/push_bundle--Dec_2_2007.hg) by @jonhanke created at 2007-12-02 14:41:35\n\nChangesets",
    "created_at": "2007-12-02T14:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1371#issuecomment-8775",
    "user": "https://github.com/jonhanke"
}
```

Attachment [push_bundle--Dec_2_2007.hg](tarball://root/attachments/some-uuid/ticket1371/push_bundle--Dec_2_2007.hg) by @jonhanke created at 2007-12-02 14:41:35

Changesets



---

archive/issue_events_003545.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-04T14:11:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1371",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1371#event-3545"
}
```



---

archive/issue_comments_008776.json:
```json
{
    "body": "This should be applied, assuming that it does not change the default behaviour.  (It should not.)  It does look like there is an incorrectly indented line, but compiling should catch that.\n\nI do worry about the copyright change, though -- I thought we agreed to give all the copyright's to William Stein, to ease future license changes.  We should check if Jon Hanke is okay with that?",
    "created_at": "2008-01-22T18:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1371#issuecomment-8776",
    "user": "https://github.com/ncalexan"
}
```

This should be applied, assuming that it does not change the default behaviour.  (It should not.)  It does look like there is an incorrectly indented line, but compiling should catch that.

I do worry about the copyright change, though -- I thought we agreed to give all the copyright's to William Stein, to ease future license changes.  We should check if Jon Hanke is okay with that?



---

archive/issue_comments_008777.json:
```json
{
    "body": "> I do worry about the copyright change, though -- I thought we agreed \n> to give all the copyright's to William Stein, to ease future license \n> changes. We should check if Jon Hanke is okay with that?\n\nWe did not agree to do that.  Some people did, but it is completely\noptional.  The key requirement is that all code in the core Sage library \nbe licensed  \"GPL V2 or greater\". The copyright holder can be anybody.",
    "created_at": "2008-01-22T22:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1371#issuecomment-8777",
    "user": "https://github.com/williamstein"
}
```

> I do worry about the copyright change, though -- I thought we agreed 
> to give all the copyright's to William Stein, to ease future license 
> changes. We should check if Jon Hanke is okay with that?

We did not agree to do that.  Some people did, but it is completely
optional.  The key requirement is that all code in the core Sage library 
be licensed  "GPL V2 or greater". The copyright holder can be anybody.



---

archive/issue_comments_008778.json:
```json
{
    "body": "After discussion with William at SD7, this should be applied.",
    "created_at": "2008-02-09T03:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1371#issuecomment-8778",
    "user": "https://github.com/ncalexan"
}
```

After discussion with William at SD7, this should be applied.



---

archive/issue_comments_008779.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-10T01:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1371#issuecomment-8779",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003546.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-10T01:12:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1371",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1371#event-3546"
}
```



---

archive/issue_comments_008780.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-10T01:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1371#issuecomment-8780",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha0
