# Issue 4617: Create a `test-dummy.spkg`

archive/issues_004617.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: dummy test package\n\nThis is related with ticket #4587\n\nFor doc-testing the installation of packages, there should be some `test-dummy.spkg`\n\nThe purpose of the package is to do *nothing*. William suggested to mark it `optional -- admin`, I am not sure what that means. [it means that it would only be tested when we do sage -t -only_optional=admin, where admin means \"tested by the admin who has write privileges to the sage install]\n\nAlso, there should be an easy way to get rid of `test-dummy.spkg` after installation.\n\nIdea:\n* `sage -i test-dummy.spkg` should simply result in an entry in the list of installed packages.\n* uninstalling it is done by removing the list entry and deleting the file `test-dummy.spkg`.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4617\n\n",
    "closed_at": "2014-11-07T16:49:58Z",
    "created_at": "2008-11-25T12:55:40Z",
    "labels": [
        "component: packages: standard",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Create a `test-dummy.spkg`",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4617",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: mabshoff

Keywords: dummy test package

This is related with ticket #4587

For doc-testing the installation of packages, there should be some `test-dummy.spkg`

The purpose of the package is to do *nothing*. William suggested to mark it `optional -- admin`, I am not sure what that means. [it means that it would only be tested when we do sage -t -only_optional=admin, where admin means "tested by the admin who has write privileges to the sage install]

Also, there should be an easy way to get rid of `test-dummy.spkg` after installation.

Idea:
* `sage -i test-dummy.spkg` should simply result in an entry in the list of installed packages.
* uninstalling it is done by removing the list entry and deleting the file `test-dummy.spkg`.



Issue created by migration from https://trac.sagemath.org/ticket/4617





---

archive/issue_comments_034588.json:
```json
{
    "body": "Replying to [ticket:4617 SimonKing]:\n> William suggested to mark it `optional -- admin`, I am not sure what that means. [it means that it would only be tested when we do sage -t -only_optional=admin, where admin means \"tested by the admin who has write privileges to the sage install]\n\n\nThanks! \n\n>  * uninstalling it is done by removing the list entry and deleting the file `test-dummy.spkg`.\n\n\n... which probably also requires admin privileges. So, the to-be-created doctests for #4587 will also be optional -- admin, right?",
    "created_at": "2008-11-25T20:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4617#issuecomment-34588",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [ticket:4617 SimonKing]:
> William suggested to mark it `optional -- admin`, I am not sure what that means. [it means that it would only be tested when we do sage -t -only_optional=admin, where admin means "tested by the admin who has write privileges to the sage install]


Thanks! 

>  * uninstalling it is done by removing the list entry and deleting the file `test-dummy.spkg`.


... which probably also requires admin privileges. So, the to-be-created doctests for #4587 will also be optional -- admin, right?



---

archive/issue_events_010489.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4617#event-10489"
}
```



---

archive/issue_events_010490.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4617#event-10490"
}
```



---

archive/issue_events_010491.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4617#event-10491"
}
```



---

archive/issue_events_010492.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4617#event-10492"
}
```



---

archive/issue_events_010493.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4617#event-10493"
}
```



---

archive/issue_events_010494.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4617#event-10494"
}
```



---

archive/issue_events_010495.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4617#event-10495"
}
```



---

archive/issue_comments_034589.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-11-06T15:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4617#issuecomment-34589",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_events_010496.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-11-06T15:57:48Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4617#event-10496"
}
```



---

archive/issue_events_010497.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-11-06T15:57:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4617#event-10497"
}
```



---

archive/issue_comments_034590.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-11-06T15:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4617#issuecomment-34590",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_034591.json:
```json
{
    "body": "Obsolete",
    "created_at": "2014-11-06T15:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4617#issuecomment-34591",
    "user": "https://github.com/jdemeyer"
}
```

Obsolete



---

archive/issue_comments_034592.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-11-07T16:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4617#issuecomment-34592",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix



---

archive/issue_events_010498.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-11-07T16:49:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4617",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4617#event-10498"
}
```
