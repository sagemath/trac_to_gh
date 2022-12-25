# Issue 9026: Issues preventing 64-bit builds on various flavors of Solaris.

archive/issues_009026.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @dimpase @jaapspies mvngu @jhpalmieri robertw @williamstein\n\nThe following is list of the issues that are currently preventing Sage build on either\n\n* OpenSolaris (aka Solaris 11) on Intel/AMD x64. (e.g. 'disk')\n* Solaris 10 on Intel/AMD (e.g. 'fulva')\n* Solaris 10 on SPARC (e.g. 't2')\n\nThe list can be added as new problems are found, making what William calls a 'metaticket' \n\nPlease put \n* \"yes\" if the trac ticket is known, or one might reasonably expect it to cause a problem on a particular platform.\n* \"no\" if one knows the problem does not exist on that platform, or one reasonably expect it will not be an issue. \n* \"unknow\" if one can not determine if it will be an issue. \n\nAlthough OpenSolaris can run on the SPARC platform, very few people run it, so there is little to be gained by tracking issues on that platform. (David Kirkby does not have OpenSolaris installed on any of his SPARC systems)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9026\n\n",
    "created_at": "2010-05-24T00:14:01Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Issues preventing 64-bit builds on various flavors of Solaris.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9026",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @dimpase @jaapspies mvngu @jhpalmieri robertw @williamstein

The following is list of the issues that are currently preventing Sage build on either

* OpenSolaris (aka Solaris 11) on Intel/AMD x64. (e.g. 'disk')
* Solaris 10 on Intel/AMD (e.g. 'fulva')
* Solaris 10 on SPARC (e.g. 't2')

The list can be added as new problems are found, making what William calls a 'metaticket' 

Please put 
* "yes" if the trac ticket is known, or one might reasonably expect it to cause a problem on a particular platform.
* "no" if one knows the problem does not exist on that platform, or one reasonably expect it will not be an issue. 
* "unknow" if one can not determine if it will be an issue. 

Although OpenSolaris can run on the SPARC platform, very few people run it, so there is little to be gained by tracking issues on that platform. (David Kirkby does not have OpenSolaris installed on any of his SPARC systems)


Issue created by migration from https://trac.sagemath.org/ticket/9026





---

archive/issue_comments_083377.json:
```json
{
    "body": "As part of this project, we should update the \"supported platforms\" information, wherever it appears.  For example, in the installation guide, it says\n\n```\nComplete compilation of Sage is currently not supported on Solaris\n```\n\nAccording to the \"search_doc\" function, the main occurrences of the string \"Solaris\" are in the file \"devel/sage/doc/en/installation/source.rst\", so that's the only part of the docs that we need to fix.  The file SAGE_ROOT/README.txt says that Solaris on sparc is officially supported, but not Solaris on x86_64.  I'm guessing that this is still accurate.  There are probably assorted wiki pages about supported platforms, too. In any case, it would be good to maintain a single official list of supported platforms, instead of having conflicting information in different locations.",
    "created_at": "2010-07-12T23:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9026#issuecomment-83377",
    "user": "https://github.com/jhpalmieri"
}
```

As part of this project, we should update the "supported platforms" information, wherever it appears.  For example, in the installation guide, it says

```
Complete compilation of Sage is currently not supported on Solaris
```

According to the "search_doc" function, the main occurrences of the string "Solaris" are in the file "devel/sage/doc/en/installation/source.rst", so that's the only part of the docs that we need to fix.  The file SAGE_ROOT/README.txt says that Solaris on sparc is officially supported, but not Solaris on x86_64.  I'm guessing that this is still accurate.  There are probably assorted wiki pages about supported platforms, too. In any case, it would be good to maintain a single official list of supported platforms, instead of having conflicting information in different locations.



---

archive/issue_comments_083378.json:
```json
{
    "body": "Replying to [comment:24 jhpalmieri]:\n> As part of this project, we should update the \"supported platforms\" information, wherever it appears.  For example, in the installation guide, it says\n> {{{\n> Complete compilation of Sage is currently not supported on Solaris\n> }}}\n> According to the \"search_doc\" function, the main occurrences of the string \"Solaris\" are in the file \"devel/sage/doc/en/installation/source.rst\", so that's the only part of the docs that we need to fix.  The file SAGE_ROOT/README.txt says that Solaris on sparc is officially supported, but not Solaris on x86_64.  I'm guessing that this is still accurate. \n\nYes, that is still true. \n\n> There are probably assorted wiki pages about supported platforms, too. In any case, it would be good to maintain a single official list of supported platforms, instead of having conflicting information in different locations.\n\nI agree, though that is a different issue to this ticket, which is for build problems on 64-bit Solaris. The supported platforms issue needs resolving for Solaris, as it does for Linux, OS X and Windows. I created  #9487 to cover this.\n\nDave",
    "created_at": "2010-07-13T00:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9026#issuecomment-83378",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:24 jhpalmieri]:
> As part of this project, we should update the "supported platforms" information, wherever it appears.  For example, in the installation guide, it says
> {{{
> Complete compilation of Sage is currently not supported on Solaris
> }}}
> According to the "search_doc" function, the main occurrences of the string "Solaris" are in the file "devel/sage/doc/en/installation/source.rst", so that's the only part of the docs that we need to fix.  The file SAGE_ROOT/README.txt says that Solaris on sparc is officially supported, but not Solaris on x86_64.  I'm guessing that this is still accurate. 

Yes, that is still true. 

> There are probably assorted wiki pages about supported platforms, too. In any case, it would be good to maintain a single official list of supported platforms, instead of having conflicting information in different locations.

I agree, though that is a different issue to this ticket, which is for build problems on 64-bit Solaris. The supported platforms issue needs resolving for Solaris, as it does for Linux, OS X and Windows. I created  #9487 to cover this.

Dave



---

archive/issue_comments_083379.json:
```json
{
    "body": "John, \nI see you updated the table to include #9358. Note however note the comments above.\n\nPlease put\n* \"yes\" if the trac ticket is known, or one might reasonably expect it to cause a problem on a particular platform.\n* \"no\" if one knows the problem does not exist on that platform, or one reasonably expect it will not be an issue.\n* \"unknown\" if one can not determine if it will be an issue. \n\nSo the znpoly issue should have a \"yes\" in the first column. I've also tried to keep them in order of trac number, though that's not a big deal. \n\nPerhaps changing \"yes\" -> Bug and No->OK might be sensible, as I can see this could be confusing. That would be trivial to change with a sed script. What do you think of that, or can you think of a better, less confusing solution? \n\nDave",
    "created_at": "2010-08-02T22:22:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9026#issuecomment-83379",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

John, 
I see you updated the table to include #9358. Note however note the comments above.

Please put
* "yes" if the trac ticket is known, or one might reasonably expect it to cause a problem on a particular platform.
* "no" if one knows the problem does not exist on that platform, or one reasonably expect it will not be an issue.
* "unknown" if one can not determine if it will be an issue. 

So the znpoly issue should have a "yes" in the first column. I've also tried to keep them in order of trac number, though that's not a big deal. 

Perhaps changing "yes" -> Bug and No->OK might be sensible, as I can see this could be confusing. That would be trivial to change with a sed script. What do you think of that, or can you think of a better, less confusing solution? 

Dave



---

archive/issue_comments_083380.json:
```json
{
    "body": "Well, znpoly builds fine on t2, so shouldn't there be a \"no\" in the first column?  It has problems 64-bit on t2, so \"yes\" in the second column.  The third column is the only one I should probably change, to \"unknown\", since I don't know how znpoly behaves on OpenSolaris.  Maybe you know about that, though?",
    "created_at": "2010-08-02T22:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9026#issuecomment-83380",
    "user": "https://github.com/jhpalmieri"
}
```

Well, znpoly builds fine on t2, so shouldn't there be a "no" in the first column?  It has problems 64-bit on t2, so "yes" in the second column.  The third column is the only one I should probably change, to "unknown", since I don't know how znpoly behaves on OpenSolaris.  Maybe you know about that, though?



---

archive/issue_comments_083381.json:
```json
{
    "body": "Oh, I see the whole ticket is 64-bit specific.  Never mind.",
    "created_at": "2010-08-02T22:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9026#issuecomment-83381",
    "user": "https://github.com/jhpalmieri"
}
```

Oh, I see the whole ticket is 64-bit specific.  Never mind.



---

archive/issue_comments_083382.json:
```json
{
    "body": "Replying to [comment:30 jhpalmieri]:\n> Oh, I see the whole ticket is 64-bit specific.  Never mind.\n\nWe could add a couple of columns, for 32-bit OpenSolaris and 32-bit Solaris 10 x86. I wanted to avoid having. Obviously the title would need changing, but that is no big deal. What do you think to that - put them all on one ticket?",
    "created_at": "2010-08-02T23:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9026#issuecomment-83382",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:30 jhpalmieri]:
> Oh, I see the whole ticket is 64-bit specific.  Never mind.

We could add a couple of columns, for 32-bit OpenSolaris and 32-bit Solaris 10 x86. I wanted to avoid having. Obviously the title would need changing, but that is no big deal. What do you think to that - put them all on one ticket?



---

archive/issue_comments_083383.json:
```json
{
    "body": "Replying to [comment:31 drkirkby]:\n> Replying to [comment:30 jhpalmieri]:\n> > Oh, I see the whole ticket is 64-bit specific.  Never mind.\n> \n> We could add a couple of columns, for 32-bit OpenSolaris and 32-bit Solaris 10 x86. I wanted to avoid having.\n\nI did not finish that sentence. Just forget it. It seems to me adding a couple of columns might be sensible. \n\nDave",
    "created_at": "2010-08-02T23:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9026#issuecomment-83383",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:31 drkirkby]:
> Replying to [comment:30 jhpalmieri]:
> > Oh, I see the whole ticket is 64-bit specific.  Never mind.
> 
> We could add a couple of columns, for 32-bit OpenSolaris and 32-bit Solaris 10 x86. I wanted to avoid having.

I did not finish that sentence. Just forget it. It seems to me adding a couple of columns might be sensible. 

Dave



---

archive/issue_events_022083.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9026#event-22083"
}
```



---

archive/issue_events_022084.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9026#event-22084"
}
```



---

archive/issue_events_022085.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9026#event-22085"
}
```



---

archive/issue_events_022086.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9026#event-22086"
}
```



---

archive/issue_events_022087.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9026#event-22087"
}
```



---

archive/issue_events_022088.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9026#event-22088"
}
```



---

archive/issue_events_022089.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9026#event-22089"
}
```



---

archive/issue_events_022090.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-04-01T14:09:35Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9026#event-22090"
}
```



---

archive/issue_events_022091.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-04-01T14:09:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9026#event-22091"
}
```



---

archive/issue_comments_083384.json:
```json
{
    "body": "Should be closed as outdated.",
    "created_at": "2020-04-01T14:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9026#issuecomment-83384",
    "user": "https://github.com/mkoeppe"
}
```

Should be closed as outdated.



---

archive/issue_comments_083385.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-04-01T14:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9026#issuecomment-83385",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083386.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-04-01T14:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9026#issuecomment-83386",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022092.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-04-01T14:48:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9026#event-22092"
}
```



---

archive/issue_comments_083387.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-04-01T14:48:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9026#issuecomment-83387",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_comments_083388.json:
```json
{
    "body": "agreed",
    "created_at": "2020-04-01T14:48:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9026#issuecomment-83388",
    "user": "https://github.com/fchapoton"
}
```

agreed
