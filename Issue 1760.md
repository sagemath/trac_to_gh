# Issue 1760: on osx make a symlink sage.command --> sage

archive/issues_001760.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @gvol\n\n```\nWell, perhaps this is know, but apropos the petition to make steps\n4--6 of installation in OS X nicer, there are a very easy way. Simply\nrename the sage script to sage.command. This way if you double-click\nover it from finder it will be automatically launched inside a\nTerminal session.\n\nSaludos,\nRafa\n\nP.D. I'm not a OSX guru, only a /bin/sh user in OSX landscape ;-)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1760\n\n",
    "closed_at": "2012-08-01T12:26:28Z",
    "created_at": "2008-01-11T22:20:11Z",
    "labels": [
        "component: user interface"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "on osx make a symlink sage.command --> sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1760",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

CC:  @gvol

```
Well, perhaps this is know, but apropos the petition to make steps
4--6 of installation in OS X nicer, there are a very easy way. Simply
rename the sage script to sage.command. This way if you double-click
over it from finder it will be automatically launched inside a
Terminal session.

Saludos,
Rafa

P.D. I'm not a OSX guru, only a /bin/sh user in OSX landscape ;-)
```

Issue created by migration from https://trac.sagemath.org/ticket/1760





---

archive/issue_comments_011075.json:
```json
{
    "body": "One way to implement this is make it so sage -bdist on osx, in addition to just making  dmg, also does\n\n```\n ln -s sage sage.command\n```\nin SAGE_ROOT right before making the dmg file.   This should just involve\nadding one line to SAGE_ROOT/local/bin/sage-bdist",
    "created_at": "2008-01-11T22:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11075",
    "user": "https://github.com/williamstein"
}
```

One way to implement this is make it so sage -bdist on osx, in addition to just making  dmg, also does

```
 ln -s sage sage.command
```
in SAGE_ROOT right before making the dmg file.   This should just involve
adding one line to SAGE_ROOT/local/bin/sage-bdist



---

archive/issue_comments_011076.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-16T04:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11076",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011077.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-09-16T04:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11077",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_011078.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11078",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_011079.json:
```json
{
    "body": "Wow, I can't believe this ticket eluded detection for all this time.  Do we really need this now that we have the app bundle (even made all the time, thanks Jeroen!)?",
    "created_at": "2011-06-02T04:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11079",
    "user": "https://github.com/kcrisman"
}
```

Wow, I can't believe this ticket eluded detection for all this time.  Do we really need this now that we have the app bundle (even made all the time, thanks Jeroen!)?



---

archive/issue_comments_011080.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-07-07T04:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11080",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_events_004272.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2012-07-07T04:23:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1760#event-4272"
}
```



---

archive/issue_comments_011081.json:
```json
{
    "body": "Bye-bye.  Not that it isn't fun to have a symlink, but anyone who really needs this will either\n   * download the app because they don't know how to do this\n   * make a symlink themselves because they do.",
    "created_at": "2012-07-07T04:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11081",
    "user": "https://github.com/kcrisman"
}
```

Bye-bye.  Not that it isn't fun to have a symlink, but anyone who really needs this will either
   * download the app because they don't know how to do this
   * make a symlink themselves because they do.



---

archive/issue_comments_011082.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-07-07T04:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11082",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_004273.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-08-01T12:26:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1760#event-4273"
}
```



---

archive/issue_comments_011083.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2012-08-01T12:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11083",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: wontfix
