# Issue 9487: Have an acurate description of what "supported platforms" are, and have one list - not numerous different ones.

archive/issues_009487.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @jhpalmieri @rlmill mariah georgsweber @peterjeremy @nexttime @mkoeppe @slel\n\nAs has been noted several times before, the list of \"supported platforms\" for Sage varies very depending on what particular file/web-page you read. Different sources which include a list of supported platforms include:\n\n* README.txt\n* http://www.sagemath.org/doc/installation/source.html\n* http://wiki.sagemath.org/SupportedPlatforms\n\nA proposal of mine is at \n\nhttp://wiki.sagemath.org/suggested-for-supported-platforms\n\nwhich is based on the method used by Mathworks for MATLAB in their list of [System Requirements for Linux](http://www.mathworks.com/support/sysreq/current_release/linux.html). Mathworks break \"supported\" into two lists. \n* List systems which MATLAB is tested on, and so they can give good support. (In this case, exact version numbers are listed e.g. Ubuntu 8.04, 8.10, 9.04, and 9.10) \n* List systems on which MATLAB should work, but which they don't test. \n\nI generalised that to four for Sage, \n\n* Fully supported (Sage is always tested on **every** system in this list before a release is made) \n* Expected to work \n* Probably will not work, but porting is ongoing \n* Will not work and porting will require substantial effort \n\nThe first two are basically the same as Mathworks use. The last two are applicable to Sage, but not for a closed source system like MATLAB. \n\nIt would be good if the list could be maintained in such a way that there are not several different sources giving a different list of \"supported\" systems. \n\n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9487\n\n",
    "created_at": "2010-07-12T23:58:20Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Have an acurate description of what \"supported platforms\" are, and have one list - not numerous different ones.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9487",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: mvngu

CC:  @jhpalmieri @rlmill mariah georgsweber @peterjeremy @nexttime @mkoeppe @slel

As has been noted several times before, the list of "supported platforms" for Sage varies very depending on what particular file/web-page you read. Different sources which include a list of supported platforms include:

* README.txt
* http://www.sagemath.org/doc/installation/source.html
* http://wiki.sagemath.org/SupportedPlatforms

A proposal of mine is at 

http://wiki.sagemath.org/suggested-for-supported-platforms

which is based on the method used by Mathworks for MATLAB in their list of [System Requirements for Linux](http://www.mathworks.com/support/sysreq/current_release/linux.html). Mathworks break "supported" into two lists. 
* List systems which MATLAB is tested on, and so they can give good support. (In this case, exact version numbers are listed e.g. Ubuntu 8.04, 8.10, 9.04, and 9.10) 
* List systems on which MATLAB should work, but which they don't test. 

I generalised that to four for Sage, 

* Fully supported (Sage is always tested on **every** system in this list before a release is made) 
* Expected to work 
* Probably will not work, but porting is ongoing 
* Will not work and porting will require substantial effort 

The first two are basically the same as Mathworks use. The last two are applicable to Sage, but not for a closed source system like MATLAB. 

It would be good if the list could be maintained in such a way that there are not several different sources giving a different list of "supported" systems. 


Dave

Issue created by migration from https://trac.sagemath.org/ticket/9487





---

archive/issue_comments_090937.json:
```json
{
    "body": "Did anyone have any comments on this? Several people have added themselves to the 'cc' list, but so far I have had little or no feedback.",
    "created_at": "2010-07-18T22:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9487#issuecomment-90937",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Did anyone have any comments on this? Several people have added themselves to the 'cc' list, but so far I have had little or no feedback.



---

archive/issue_comments_090938.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9487#issuecomment-90938",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "" to "sd32".



---

archive/issue_events_023523.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9487#event-23523"
}
```



---

archive/issue_events_023524.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9487#event-23524"
}
```



---

archive/issue_events_023525.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9487#event-23525"
}
```



---

archive/issue_events_023526.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9487#event-23526"
}
```



---

archive/issue_events_023527.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9487#event-23527"
}
```



---

archive/issue_events_023528.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9487#event-23528"
}
```



---

archive/issue_events_023529.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9487#event-23529"
}
```



---

archive/issue_events_023530.json:
```json
{
    "actor": "https://github.com/slel",
    "created_at": "2021-04-03T09:53:08Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9487#event-23530"
}
```



---

archive/issue_events_023531.json:
```json
{
    "actor": "https://github.com/slel",
    "created_at": "2021-04-03T09:53:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "milestone": "sage-9.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9487#event-23531"
}
```



---

archive/issue_comments_090939.json:
```json
{
    "body": "I think we can close this ticket as outdated. `README.md` and the installation manual are in good shape; and since version 9.0, the release tours have a section in the end that talk about the version-specific details of tested platforms.",
    "created_at": "2021-04-03T18:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9487#issuecomment-90939",
    "user": "https://github.com/mkoeppe"
}
```

I think we can close this ticket as outdated. `README.md` and the installation manual are in good shape; and since version 9.0, the release tours have a section in the end that talk about the version-specific details of tested platforms.



---

archive/issue_events_023532.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-04-03T18:16:50Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "milestone": "sage-9.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9487#event-23532"
}
```



---

archive/issue_events_023533.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-04-03T18:16:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9487#event-23533"
}
```



---

archive/issue_comments_090940.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-04-03T18:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9487#issuecomment-90940",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090941.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2022-05-13T09:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9487#issuecomment-90941",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_023534.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2022-05-13T09:17:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9487#event-23534"
}
```



---

archive/issue_comments_090942.json:
```json
{
    "body": "ok, closing",
    "created_at": "2022-05-13T09:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9487#issuecomment-90942",
    "user": "https://github.com/fchapoton"
}
```

ok, closing
