# Issue 9574: Ignore zope-testrunner in the scripts repository

archive/issues_009574.json:
```json
{
    "body": "Assignee: @jasongrout\n\nIn the forthcoming 4.5.2.alpha0, I get\n\n```sh\n$ cd sage-4.5.2.alpha0/local/bin\n$ hg stat\n? zope-testrunner\n```\nin the scripts repository.\n\nShould we add `zope-testrunner` to `.hgignore`?\n\nIssue created by migration from https://trac.sagemath.org/ticket/9574\n\n",
    "closed_at": "2010-07-26T01:18:22Z",
    "created_at": "2010-07-22T05:10:00Z",
    "labels": [
        "component: misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Ignore zope-testrunner in the scripts repository",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9574",
    "user": "https://github.com/qed777"
}
```
Assignee: @jasongrout

In the forthcoming 4.5.2.alpha0, I get

```sh
$ cd sage-4.5.2.alpha0/local/bin
$ hg stat
? zope-testrunner
```
in the scripts repository.

Should we add `zope-testrunner` to `.hgignore`?

Issue created by migration from https://trac.sagemath.org/ticket/9574





---

archive/issue_comments_092312.json:
```json
{
    "body": "On OS X, I also see:\n\n```\ndrake@bsd:~/sage-4.5.2.alpha0/local/bin$ hg stat\n? gfortran\n? gfortran-4.0\n? gfortran-4.2\n? gfortran-64\n? gfortran-uninstall\n? i686-apple-darwin8-gfortran-4.2\n? powerpc-apple-darwin8-gfortran-4.2\n? zope-testrunner\n```",
    "created_at": "2010-07-22T06:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9574#issuecomment-92312",
    "user": "https://github.com/dandrake"
}
```

On OS X, I also see:

```
drake@bsd:~/sage-4.5.2.alpha0/local/bin$ hg stat
? gfortran
? gfortran-4.0
? gfortran-4.2
? gfortran-64
? gfortran-uninstall
? i686-apple-darwin8-gfortran-4.2
? powerpc-apple-darwin8-gfortran-4.2
? zope-testrunner
```



---

archive/issue_comments_092313.json:
```json
{
    "body": "add files to .hgignore for scripts repo",
    "created_at": "2010-07-23T03:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9574#issuecomment-92313",
    "user": "https://github.com/dandrake"
}
```

add files to .hgignore for scripts repo



---

archive/issue_comments_092314.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-23T03:13:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9574#issuecomment-92314",
    "user": "https://github.com/dandrake"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092315.json:
```json
{
    "body": "Attachment [trac_9574_add_files_to_scripts_hgignore.patch](tarball://root/attachments/some-uuid/ticket9574/trac_9574_add_files_to_scripts_hgignore.patch) by @dandrake created at 2010-07-23 03:13:55\n\nI've attached a patch that adds all the above files to the .hgignore file.",
    "created_at": "2010-07-23T03:13:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9574#issuecomment-92315",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_9574_add_files_to_scripts_hgignore.patch](tarball://root/attachments/some-uuid/ticket9574/trac_9574_add_files_to_scripts_hgignore.patch) by @dandrake created at 2010-07-23 03:13:55

I've attached a patch that adds all the above files to the .hgignore file.



---

archive/issue_comments_092316.json:
```json
{
    "body": "This works for me on {bsd,sage}.math.",
    "created_at": "2010-07-23T07:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9574#issuecomment-92316",
    "user": "https://github.com/qed777"
}
```

This works for me on {bsd,sage}.math.



---

archive/issue_comments_092317.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-23T07:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9574#issuecomment-92317",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092318.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-26T01:18:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9574#issuecomment-92318",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_events_023832.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-26T01:18:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9574",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9574#event-23832"
}
```
