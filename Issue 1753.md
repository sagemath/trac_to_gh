# Issue 1753: install_scripts() conflict with make install

archive/issues_001753.json:
```json
{
    "body": "Assignee: cwitty\n\nWhen trying to run install_scripts()  (i.e. installing from an RPM), the desired installation directory is /usr/bin so that when the files are installed, they are available in the $PATH. This causes problems with the kash and M2 scripts. Since in order for the install_scripts() to detect those executables they have to be in the path (usually /usr/bin also), install_scripts() will try to overwrite those files with the script version. This is a problem. A possible improvement is to install the kash and M2 scripts as sage.kash or sage.M2 if install_scripts() detects that it will be overwriting the respective executables.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1753\n\n",
    "created_at": "2008-01-10T22:19:51Z",
    "labels": [
        "component: relocation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "install_scripts() conflict with make install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1753",
    "user": "https://trac.sagemath.org/admin/accounts/users/pgrinber"
}
```
Assignee: cwitty

When trying to run install_scripts()  (i.e. installing from an RPM), the desired installation directory is /usr/bin so that when the files are installed, they are available in the $PATH. This causes problems with the kash and M2 scripts. Since in order for the install_scripts() to detect those executables they have to be in the path (usually /usr/bin also), install_scripts() will try to overwrite those files with the script version. This is a problem. A possible improvement is to install the kash and M2 scripts as sage.kash or sage.M2 if install_scripts() detects that it will be overwriting the respective executables.

Issue created by migration from https://trac.sagemath.org/ticket/1753





---

archive/issue_events_004235.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-10T22:26:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "milestone": "sage-2.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1753#event-4235"
}
```



---

archive/issue_comments_011032.json:
```json
{
    "body": "Ok, this should be easy enough to fix. Axiom should probably also be installed as sage.axiom or something similar.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-15T20:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1753#issuecomment-11032",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, this should be easy enough to fix. Axiom should probably also be installed as sage.axiom or something similar.

Cheers,

Michael



---

archive/issue_events_004236.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "milestone": "sage-2.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1753#event-4236"
}
```



---

archive/issue_events_004237.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1753#event-4237"
}
```



---

archive/issue_events_004238.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1753#event-4238"
}
```



---

archive/issue_events_004239.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1753#event-4239"
}
```



---

archive/issue_events_004240.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1753#event-4240"
}
```



---

archive/issue_events_004241.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1753#event-4241"
}
```



---

archive/issue_events_004242.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1753#event-4242"
}
```



---

archive/issue_events_004243.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1753#event-4243"
}
```



---

archive/issue_comments_011033.json:
```json
{
    "body": "`make install` is no longer supported, see #1792.",
    "created_at": "2016-05-20T08:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1753#issuecomment-11033",
    "user": "https://github.com/jdemeyer"
}
```

`make install` is no longer supported, see #1792.



---

archive/issue_comments_011034.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-05-20T08:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1753#issuecomment-11034",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_events_004244.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2016-05-20T08:22:02Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1753#event-4244"
}
```



---

archive/issue_events_004245.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2016-05-20T08:22:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1753#event-4245"
}
```



---

archive/issue_comments_011035.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-05-20T08:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1753#issuecomment-11035",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_011036.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-06-12T12:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1753#issuecomment-11036",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_004246.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-06-12T12:02:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1753",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1753#event-4246"
}
```
