# Issue 1760: on osx make a symlink sage.command --> sage

archive/issues_001760.json:
```json
{
    "body": "Assignee: was\n\nCC:  iandrus\n\n\n```\nWell, perhaps this is know, but apropos the petition to make steps\n4--6 of installation in OS X nicer, there are a very easy way. Simply\nrename the sage script to sage.command. This way if you double-click\nover it from finder it will be automatically launched inside a\nTerminal session.\n\nSaludos,\nRafa\n\nP.D. I'm not a OSX guru, only a /bin/sh user in OSX landscape ;-)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1760\n\n",
    "created_at": "2008-01-11T22:20:11Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "on osx make a symlink sage.command --> sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1760",
    "user": "was"
}
```
Assignee: was

CC:  iandrus


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

archive/issue_comments_011102.json:
```json
{
    "body": "One way to implement this is make it so sage -bdist on osx, in addition to just making  dmg, also does\n\n```\n ln -s sage sage.command\n```\n\nin SAGE_ROOT right before making the dmg file.   This should just involve\nadding one line to SAGE_ROOT/local/bin/sage-bdist",
    "created_at": "2008-01-11T22:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11102",
    "user": "was"
}
```

One way to implement this is make it so sage -bdist on osx, in addition to just making  dmg, also does

```
 ln -s sage sage.command
```

in SAGE_ROOT right before making the dmg file.   This should just involve
adding one line to SAGE_ROOT/local/bin/sage-bdist



---

archive/issue_comments_011103.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-16T04:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11103",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011104.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2008-09-16T04:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11104",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_011105.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11105",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_011106.json:
```json
{
    "body": "Wow, I can't believe this ticket eluded detection for all this time.  Do we really need this now that we have the app bundle (even made all the time, thanks Jeroen!)?",
    "created_at": "2011-06-02T04:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11106",
    "user": "kcrisman"
}
```

Wow, I can't believe this ticket eluded detection for all this time.  Do we really need this now that we have the app bundle (even made all the time, thanks Jeroen!)?



---

archive/issue_comments_011107.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-07-07T04:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11107",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_011108.json:
```json
{
    "body": "Bye-bye.  Not that it isn't fun to have a symlink, but anyone who really needs this will either\n   * download the app because they don't know how to do this\n   * make a symlink themselves because they do.",
    "created_at": "2012-07-07T04:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11108",
    "user": "kcrisman"
}
```

Bye-bye.  Not that it isn't fun to have a symlink, but anyone who really needs this will either
   * download the app because they don't know how to do this
   * make a symlink themselves because they do.



---

archive/issue_comments_011109.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-07-07T04:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11109",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_011110.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2012-08-01T12:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1760",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1760#issuecomment-11110",
    "user": "jdemeyer"
}
```

Resolution: wontfix
