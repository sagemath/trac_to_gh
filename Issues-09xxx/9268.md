# Issue 9268: Notebook Server replies to Plot3d-Data-Request with Status 301

archive/issues_009268.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @kcrisman @jhpalmieri\n\nKeywords: notebook java jmol black\n\nThis issue has long caused problems, although many people managed to get it fixed without actually knowing what caused it. As discussed in all detail in the following thread\n\nhttp://groups.google.com/group/sage-notebook/browse_thread/thread/9191e031224a3ce9\n\nJMol requests the data for the plot3d from the Sage backend. When it does so, on some occasions it receives a 301 Moved Permanently which Java is not following but interprets as 200 and parses the content - which then causes the error.\n\nThis is partly a client-side Java problem as Java should perhaps follow the 301 to the new location and then pass the data transparently but also Sage shouldn't provide a 301'd location in the first place.\n\nFurther details, such as the fact that this does not happen for applets which are part of a published worksheet can be found in the thread.\n\nCan be fixed by making JMol pointing to the correct location or make Sage transparently return the data instead of a 301.\n\nThis problem occurs with both, the open IcedTea (OpenJDK) and propritary Sun Java in Firefox 3.6 on Ubuntu 10.4LTS.\n\nOn a sidenote, I assume that other people do not have this problem because they might have additional packages installed which compensate for the 301.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9268\n\n",
    "closed_at": "2020-03-28T20:45:33Z",
    "created_at": "2010-06-18T20:57:52Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Notebook Server replies to Plot3d-Data-Request with Status 301",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9268",
    "user": "https://trac.sagemath.org/admin/accounts/users/ManDay"
}
```
Assignee: jason, was

CC:  @kcrisman @jhpalmieri

Keywords: notebook java jmol black

This issue has long caused problems, although many people managed to get it fixed without actually knowing what caused it. As discussed in all detail in the following thread

http://groups.google.com/group/sage-notebook/browse_thread/thread/9191e031224a3ce9

JMol requests the data for the plot3d from the Sage backend. When it does so, on some occasions it receives a 301 Moved Permanently which Java is not following but interprets as 200 and parses the content - which then causes the error.

This is partly a client-side Java problem as Java should perhaps follow the 301 to the new location and then pass the data transparently but also Sage shouldn't provide a 301'd location in the first place.

Further details, such as the fact that this does not happen for applets which are part of a published worksheet can be found in the thread.

Can be fixed by making JMol pointing to the correct location or make Sage transparently return the data instead of a 301.

This problem occurs with both, the open IcedTea (OpenJDK) and propritary Sun Java in Firefox 3.6 on Ubuntu 10.4LTS.

On a sidenote, I assume that other people do not have this problem because they might have additional packages installed which compensate for the 301.

Issue created by migration from https://trac.sagemath.org/ticket/9268





---

archive/issue_comments_087158.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-03-28T20:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9268#issuecomment-87158",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_events_022837.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-03-28T20:36:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9268",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9268#event-22837"
}
```



---

archive/issue_comments_087159.json:
```json
{
    "body": "ancient ticket about deprecated sagenb, can we close ?",
    "created_at": "2020-03-28T20:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9268#issuecomment-87159",
    "user": "https://github.com/fchapoton"
}
```

ancient ticket about deprecated sagenb, can we close ?



---

archive/issue_comments_087160.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-03-28T20:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9268#issuecomment-87160",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087161.json:
```json
{
    "body": "There were a number of wonky things like this we never saw often enough to diagnose, true.",
    "created_at": "2020-03-28T20:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9268#issuecomment-87161",
    "user": "https://github.com/kcrisman"
}
```

There were a number of wonky things like this we never saw often enough to diagnose, true.



---

archive/issue_events_022838.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-03-28T20:45:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9268",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9268#event-22838"
}
```



---

archive/issue_comments_087162.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-28T20:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9268#issuecomment-87162",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_comments_087163.json:
```json
{
    "body": "thx",
    "created_at": "2020-03-28T20:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9268",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9268#issuecomment-87163",
    "user": "https://github.com/fchapoton"
}
```

thx
