# Issue 9461: Doctest failures with sage -t -randorder=X

archive/issues_009461.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @jm58660\n\nStart with a build of 4.5.alpha4 for which all long doctests pass.  Run, e.g.,\n\n```sh\n$ ./sage -t -long -sagenb -randorder=12345 devel/sage\n```\n\nMany tests fail.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9461\n\n",
    "created_at": "2010-07-09T05:28:56Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.3",
    "title": "Doctest failures with sage -t -randorder=X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9461",
    "user": "https://github.com/qed777"
}
```
Assignee: mvngu

CC:  @jm58660

Start with a build of 4.5.alpha4 for which all long doctests pass.  Run, e.g.,

```sh
$ ./sage -t -long -sagenb -randorder=12345 devel/sage
```

Many tests fail.

Issue created by migration from https://trac.sagemath.org/ticket/9461





---

archive/issue_comments_090590.json:
```json
{
    "body": "[Here](http://sage.math.washington.edu/home/mpatel/trac/9461) are raw test logs from parallel testing on sage.math.  I made these with, e.g.,\n\n```sh\n$ nohup nice -n 19 ./sage -tp 22 -long -sagenb -randorder=X devel/sage  > ptestlong_randorderX.log &\n```\n",
    "created_at": "2010-07-09T05:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9461#issuecomment-90590",
    "user": "https://github.com/qed777"
}
```

[Here](http://sage.math.washington.edu/home/mpatel/trac/9461) are raw test logs from parallel testing on sage.math.  I made these with, e.g.,

```sh
$ nohup nice -n 19 ./sage -tp 22 -long -sagenb -randorder=X devel/sage  > ptestlong_randorderX.log &
```




---

archive/issue_events_023430.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9461",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9461#event-23430"
}
```



---

archive/issue_events_023431.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9461",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9461#event-23431"
}
```



---

archive/issue_events_023432.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9461",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9461#event-23432"
}
```



---

archive/issue_events_023433.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9461",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9461#event-23433"
}
```



---

archive/issue_events_023434.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9461",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9461#event-23434"
}
```



---

archive/issue_events_023435.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9461",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9461#event-23435"
}
```



---

archive/issue_events_023436.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9461",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9461#event-23436"
}
```



---

archive/issue_events_023437.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2016-07-24T09:37:06Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9461",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9461#event-23437"
}
```



---

archive/issue_events_023438.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2016-07-24T09:37:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9461",
    "milestone": "sage-7.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9461#event-23438"
}
```



---

archive/issue_comments_090591.json:
```json
{
    "body": "I suggest that for a while we use keyword \"random_test_failure\" for these.\n\nVolker suggested adding `# seed0` tag to tests that should not be run when `--randorder` is not zero (i.e. the default). I guess that it is a good idea, but maybe we should see some examples first. #21054 is clearly an error; #21080 fails in a line with comment \"needed until #19269 is fixed\"; `src/sage/graphs/base/graph_backends.pyx` gives a deprecation warning.",
    "created_at": "2016-07-25T06:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9461#issuecomment-90591",
    "user": "https://github.com/jm58660"
}
```

I suggest that for a while we use keyword "random_test_failure" for these.

Volker suggested adding `# seed0` tag to tests that should not be run when `--randorder` is not zero (i.e. the default). I guess that it is a good idea, but maybe we should see some examples first. #21054 is clearly an error; #21080 fails in a line with comment "needed until #19269 is fixed"; `src/sage/graphs/base/graph_backends.pyx` gives a deprecation warning.
