# Issue 9559: *generalized* canonical generation in Cython

archive/issues_009559.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  boothby @nathanncohen @kini @dimpase\n\nRight now this ticket is for organization, so I'm leaving it as \"new\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/9559\n\n",
    "created_at": "2010-07-21T08:27:52Z",
    "labels": [
        "component: group theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.7",
    "title": "*generalized* canonical generation in Cython",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9559",
    "user": "https://github.com/rlmill"
}
```
Assignee: joyner

CC:  boothby @nathanncohen @kini @dimpase

Right now this ticket is for organization, so I'm leaving it as "new".

Issue created by migration from https://trac.sagemath.org/ticket/9559





---

archive/issue_comments_091991.json:
```json
{
    "body": "Changing assignee from joyner to @rlmill.",
    "created_at": "2010-07-21T08:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9559#issuecomment-91991",
    "user": "https://github.com/rlmill"
}
```

Changing assignee from joyner to @rlmill.



---

archive/issue_events_023801.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2011-05-17T04:18:01Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9559#event-23801"
}
```



---

archive/issue_comments_091992.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-18T04:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9559#issuecomment-91992",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091993.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-22T00:54:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9559#issuecomment-91993",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091994.json:
```json
{
    "body": "\n```\n477c477,478\n< groups/perm_gps/partn_ref/refinement_graphs.pyx: 100% (8 of 8)\n---\n> groups/perm_gps/partn_ref/refinement_graphs.pyx: 100% (10 of 10)\n> groups/perm_gps/partn_ref/refinement_sets.pyx: 100% (3 of 3)\n1299,1300c1300,1301\n< Total number of functions:  28567\n< We need 1110 more function to get to 90% coverage.\n---\n> Total number of functions:  28572\n> We need 1109 more function to get to 90% coverage.\n```\n",
    "created_at": "2012-01-22T01:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9559#issuecomment-91994",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```


```
477c477,478
< groups/perm_gps/partn_ref/refinement_graphs.pyx: 100% (8 of 8)
---
> groups/perm_gps/partn_ref/refinement_graphs.pyx: 100% (10 of 10)
> groups/perm_gps/partn_ref/refinement_sets.pyx: 100% (3 of 3)
1299,1300c1300,1301
< Total number of functions:  28567
< We need 1110 more function to get to 90% coverage.
---
> Total number of functions:  28572
> We need 1109 more function to get to 90% coverage.
```




---

archive/issue_comments_091995.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-01-23T22:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9559#issuecomment-91995",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_091996.json:
```json
{
    "body": "The commit message needs to be fixed, it certainly should not contain \"[mq]\".\n\nNewly added files should conform to the template at [http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files](http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files).\n\nNew documentation strings should conform to [http://sagemath.org/doc/developer/conventions.html#documentation-strings](http://sagemath.org/doc/developer/conventions.html#documentation-strings).",
    "created_at": "2012-01-23T22:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9559#issuecomment-91996",
    "user": "https://github.com/jdemeyer"
}
```

The commit message needs to be fixed, it certainly should not contain "[mq]".

Newly added files should conform to the template at [http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files](http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files).

New documentation strings should conform to [http://sagemath.org/doc/developer/conventions.html#documentation-strings](http://sagemath.org/doc/developer/conventions.html#documentation-strings).



---

archive/issue_comments_091997.json:
```json
{
    "body": "Attachment [trac_9559.patch](tarball://root/attachments/some-uuid/ticket9559/trac_9559.patch) by @rlmill created at 2013-01-17 04:39:26",
    "created_at": "2013-01-17T04:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9559#issuecomment-91997",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_9559.patch](tarball://root/attachments/some-uuid/ticket9559/trac_9559.patch) by @rlmill created at 2013-01-17 04:39:26



---

archive/issue_comments_091998.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-01-17T04:39:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9559#issuecomment-91998",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_091999.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-17T04:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9559#issuecomment-91999",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092000.json:
```json
{
    "body": "Tests pass, formatting updated as requested by jdemeyer.",
    "created_at": "2013-01-17T04:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9559#issuecomment-92000",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Tests pass, formatting updated as requested by jdemeyer.



---

archive/issue_events_023802.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-17T07:30:34Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9559#event-23802"
}
```



---

archive/issue_events_023803.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-17T07:30:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "milestone": "sage-5.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9559#event-23803"
}
```



---

archive/issue_events_023804.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-21T21:07:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9559#event-23804"
}
```



---

archive/issue_comments_092001.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-01-21T21:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9559#issuecomment-92001",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
