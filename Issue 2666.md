# Issue 2666: ncalexan's enhancements to emacs sage mode

archive/issues_002666.json:
```json
{
    "body": "Assignee: was\n\nCC:  iandrus\n\nncalexan has been talking about his sage-mode.el enhancements---it'd be great to include his great wizardry into the sage distribution.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2666\n\n",
    "created_at": "2008-03-25T20:43:45Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "title": "ncalexan's enhancements to emacs sage mode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2666",
    "user": "jason"
}
```
Assignee: was

CC:  iandrus

ncalexan has been talking about his sage-mode.el enhancements---it'd be great to include his great wizardry into the sage distribution.

Issue created by migration from https://trac.sagemath.org/ticket/2666





---

archive/issue_comments_018341.json:
```json
{
    "body": "Apparently Nick is distributing this as an spkg now.  See http://wiki.sagemath.org/sage-mode  Should this ticket be closed, then?  Is that spkg in at least the optional repository, if not the standard repository?",
    "created_at": "2009-02-12T00:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18341",
    "user": "jason"
}
```

Apparently Nick is distributing this as an spkg now.  See http://wiki.sagemath.org/sage-mode  Should this ticket be closed, then?  Is that spkg in at least the optional repository, if not the standard repository?



---

archive/issue_comments_018342.json:
```json
{
    "body": "Replying to [comment:1 jason]:\n> Apparently Nick is distributing this as an spkg now.  See http://wiki.sagemath.org/sage-mode  Should this ticket be closed, then?  Is that spkg in at least the optional repository, if not the standard repository?\n\nThere is still the plan to make this part of standard Sage, just like SageTeX, so I am changing the summary to reflect this even though this was not the original motivation for this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-12T00:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18342",
    "user": "mabshoff"
}
```

Replying to [comment:1 jason]:
> Apparently Nick is distributing this as an spkg now.  See http://wiki.sagemath.org/sage-mode  Should this ticket be closed, then?  Is that spkg in at least the optional repository, if not the standard repository?

There is still the plan to make this part of standard Sage, just like SageTeX, so I am changing the summary to reflect this even though this was not the original motivation for this ticket.

Cheers,

Michael



---

archive/issue_comments_018343.json:
```json
{
    "body": "Changing assignee from was to ncalexan.",
    "created_at": "2009-02-12T00:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18343",
    "user": "mabshoff"
}
```

Changing assignee from was to ncalexan.



---

archive/issue_comments_018344.json:
```json
{
    "body": "I have been using Nick Alexander's Sage Emacs mode package for months now. My only pet peeve is that the status bar at the bottom says \"SAGE\" instead of \"Sage\". We have moved beyond that acronym. Now \"Sage\" is the name of the game :-)",
    "created_at": "2009-08-12T16:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18344",
    "user": "mvngu"
}
```

I have been using Nick Alexander's Sage Emacs mode package for months now. My only pet peeve is that the status bar at the bottom says "SAGE" instead of "Sage". We have moved beyond that acronym. Now "Sage" is the name of the game :-)



---

archive/issue_comments_018345.json:
```json
{
    "body": "Just FYI, sage-mode is in the meantime at least an optional spkg.  See also:\n* [the optional spkg list](http://sagemath.org/packages/optional/)\n* [the sage-mode on the wiki](http://wiki.sagemath.org/sage-mode)\n* [sage-mode on bitbucket](https://bitbucket.org/ncalexan/sage-mode)\n\nI think that Ivan Andrus is currently taking over for sage-mode responsibilities?",
    "created_at": "2012-06-28T13:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18345",
    "user": "kcrisman"
}
```

Just FYI, sage-mode is in the meantime at least an optional spkg.  See also:
* [the optional spkg list](http://sagemath.org/packages/optional/)
* [the sage-mode on the wiki](http://wiki.sagemath.org/sage-mode)
* [sage-mode on bitbucket](https://bitbucket.org/ncalexan/sage-mode)

I think that Ivan Andrus is currently taking over for sage-mode responsibilities?



---

archive/issue_comments_018346.json:
```json
{
    "body": "Changing keywords from \"\" to \"sage-mode\".",
    "created_at": "2012-06-28T13:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18346",
    "user": "kcrisman"
}
```

Changing keywords from "" to "sage-mode".



---

archive/issue_comments_018347.json:
```json
{
    "body": "Also, the current version on the wiki and bitbucket is 0.7, but it is 0.6 on the optional spkg list.  This should be dealt with.\n\nThis could still become a standard spkg, in theory (though I don't see the point), so maybe that would be another ticket.  If so, SPKG.txt should be changed a little so it's not just a copy of the wiki page (since all the `attachment:` directives make no sense.  In fact, that should be done for any upgrade anyway.",
    "created_at": "2012-06-28T13:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18347",
    "user": "kcrisman"
}
```

Also, the current version on the wiki and bitbucket is 0.7, but it is 0.6 on the optional spkg list.  This should be dealt with.

This could still become a standard spkg, in theory (though I don't see the point), so maybe that would be another ticket.  If so, SPKG.txt should be changed a little so it's not just a copy of the wiki page (since all the `attachment:` directives make no sense.  In fact, that should be done for any upgrade anyway.



---

archive/issue_comments_018348.json:
```json
{
    "body": "Changing component from interfaces to user interface.",
    "created_at": "2012-06-28T13:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18348",
    "user": "kcrisman"
}
```

Changing component from interfaces to user interface.



---

archive/issue_comments_018349.json:
```json
{
    "body": "Ok, I've opened #13176 to upgrade, so this is separate for making it standard.\n\nSee also #1861.",
    "created_at": "2012-06-28T13:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18349",
    "user": "kcrisman"
}
```

Ok, I've opened #13176 to upgrade, so this is separate for making it standard.

See also #1861.



---

archive/issue_comments_018350.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2012-06-28T16:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18350",
    "user": "kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_018351.json:
```json
{
    "body": "Why should this be a standard package? I think it fits very well as optional package.",
    "created_at": "2013-06-13T12:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18351",
    "user": "jdemeyer"
}
```

Why should this be a standard package? I think it fits very well as optional package.



---

archive/issue_comments_018352.json:
```json
{
    "body": "There was some discussion of this [on sage-devel](https://groups.google.com/forum/?fromgroups#!topic/sage-devel/2AOjLX0brQ8) a while ago.  IIRC it was not a clear win either way.  Personally, I slightly prefer optional, but mostly I just want it to be updated to the latest version (see #13182).   :-)",
    "created_at": "2013-06-13T17:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18352",
    "user": "iandrus"
}
```

There was some discussion of this [on sage-devel](https://groups.google.com/forum/?fromgroups#!topic/sage-devel/2AOjLX0brQ8) a while ago.  IIRC it was not a clear win either way.  Personally, I slightly prefer optional, but mostly I just want it to be updated to the latest version (see #13182).   :-)



---

archive/issue_comments_018353.json:
```json
{
    "body": "I think we should just close this.  I read the discussion on sage-devel again, and I think there's no reason to make it standard.  I've been maintaining it for a while now and don't plan on stopping in the next few years.",
    "created_at": "2014-06-10T06:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18353",
    "user": "iandrus"
}
```

I think we should just close this.  I read the discussion on sage-devel again, and I think there's no reason to make it standard.  I've been maintaining it for a while now and don't plan on stopping in the next few years.



---

archive/issue_comments_018354.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-06-10T06:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18354",
    "user": "iandrus"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_018355.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-06-10T17:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18355",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_018356.json:
```json
{
    "body": "I think that based on how people are using it (and I've seen a lot of activity over the years) this is fine to keep optional.",
    "created_at": "2014-06-10T17:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18356",
    "user": "kcrisman"
}
```

I think that based on how people are using it (and I've seen a lot of activity over the years) this is fine to keep optional.



---

archive/issue_comments_018357.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-06-14T13:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2666#issuecomment-18357",
    "user": "vbraun"
}
```

Resolution: wontfix
