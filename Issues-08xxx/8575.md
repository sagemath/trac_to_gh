# Issue 8575: Sphinx should raise warning in case of ill formated enumerated lists

archive/issues_008575.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @jhpalmieri @qed777\n\nKeywords: Sphinx, warning\n\nIn some cases, for example when an enumerated list is ill formated, in text mode ouput sphinx returns silently an empty string. It should at least raise some warning. See #8572 for an instance of the problem.\nAt this point, I don't know if it's a bug of sphinx or the way we call it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8575\n\n",
    "closed_at": "2011-04-05T16:00:07Z",
    "created_at": "2010-03-22T09:50:40Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sphinx should raise warning in case of ill formated enumerated lists",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8575",
    "user": "https://github.com/hivert"
}
```
Assignee: mvngu

CC:  @jhpalmieri @qed777

Keywords: Sphinx, warning

In some cases, for example when an enumerated list is ill formated, in text mode ouput sphinx returns silently an empty string. It should at least raise some warning. See #8572 for an instance of the problem.
At this point, I don't know if it's a bug of sphinx or the way we call it.

Issue created by migration from https://trac.sagemath.org/ticket/8575





---

archive/issue_comments_077543.json:
```json
{
    "body": "There is a very good chance that this is a bug of sphinx. I asked it on\nsphinx-dev. I'm waiting for their answer.\n\nFor the info, here is a ReST file that triggers the problem:\n\n```\n**************************\nList Bug Triggering Module\n**************************\n\n    - list item 1 -- this item is correctly formated. So that there should be\n      no problem with it..\n\n    - list item 2 -- this item is ill formated. Sphinx should raise a warning\n       when typesetting in in text mode.\n```\n\nFlorent",
    "created_at": "2010-03-22T14:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8575#issuecomment-77543",
    "user": "https://github.com/hivert"
}
```

There is a very good chance that this is a bug of sphinx. I asked it on
sphinx-dev. I'm waiting for their answer.

For the info, here is a ReST file that triggers the problem:

```
**************************
List Bug Triggering Module
**************************

    - list item 1 -- this item is correctly formated. So that there should be
      no problem with it..

    - list item 2 -- this item is ill formated. Sphinx should raise a warning
       when typesetting in in text mode.
```

Florent



---

archive/issue_comments_077544.json:
```json
{
    "body": "This is indeed a bug of sphinx (see [this Sphinx-dev thread](http://groups.google.com/group/sphinx-dev/t/c65dcb4b8a057d04)). Georg Brandl answered:\n\n   The behavior is clearly a bug, and I've now fixed it in changeset `93ae46825651`\n   in the 0.6 branch.  It will be part of the next bugfix release.\n\nI'm not sure what to do now with this ticket... Should we back port the bugfix or wait for the next release ? Should this ticket be left open ? \n\nFlorent",
    "created_at": "2010-04-06T08:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8575#issuecomment-77544",
    "user": "https://github.com/hivert"
}
```

This is indeed a bug of sphinx (see [this Sphinx-dev thread](http://groups.google.com/group/sphinx-dev/t/c65dcb4b8a057d04)). Georg Brandl answered:

   The behavior is clearly a bug, and I've now fixed it in changeset `93ae46825651`
   in the 0.6 branch.  It will be part of the next bugfix release.

I'm not sure what to do now with this ticket... Should we back port the bugfix or wait for the next release ? Should this ticket be left open ? 

Florent



---

archive/issue_comments_077545.json:
```json
{
    "body": "Replying to [comment:3 hivert]:\n> I'm not sure what to do now with this ticket... Should we back port the bugfix or wait for the next release ? Should this ticket be left open ? \n\n\nI would think wait for the next release, as that is (maybe) much easier than backporting. If you can backport, then by all means do so. Until the issue is fixed by upgrading to the new release with the bug fixed, or backporting, this ticket would remain open.",
    "created_at": "2010-04-06T21:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8575#issuecomment-77545",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:3 hivert]:
> I'm not sure what to do now with this ticket... Should we back port the bugfix or wait for the next release ? Should this ticket be left open ? 


I would think wait for the next release, as that is (maybe) much easier than backporting. If you can backport, then by all means do so. Until the issue is fixed by upgrading to the new release with the bug fixed, or backporting, this ticket would remain open.



---

archive/issue_comments_077546.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-04-07T07:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8575#issuecomment-77546",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_077547.json:
```json
{
    "body": "Replying to [comment:4 mvngu]:\n> I would think wait for the next release, as that is (maybe) much easier than backporting. If you can backport, then by all means do so. Until the issue is fixed by upgrading to the new release with the bug fixed, or backporting, this ticket would remain open.\n\n\nAccording to Georg Brandl, Sphinx should make a new bugfix release \"soon\"... So I'm in favor of waiting for it.",
    "created_at": "2010-04-07T07:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8575#issuecomment-77547",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:4 mvngu]:
> I would think wait for the next release, as that is (maybe) much easier than backporting. If you can backport, then by all means do so. Until the issue is fixed by upgrading to the new release with the bug fixed, or backporting, this ticket would remain open.


According to Georg Brandl, Sphinx should make a new bugfix release "soon"... So I'm in favor of waiting for it.



---

archive/issue_comments_077548.json:
```json
{
    "body": "This ticket should be closed since sage uses now sphinx 1.0.4\n\n```\n(WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n```\n\nI set this to positive review.",
    "created_at": "2011-04-04T16:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8575#issuecomment-77548",
    "user": "https://github.com/hivert"
}
```

This ticket should be closed since sage uses now sphinx 1.0.4

```
(WARNING/2) Bullet list ends without a blank line; unexpected unindent.
```

I set this to positive review.



---

archive/issue_comments_077549.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-04-04T16:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8575#issuecomment-77549",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_077550.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-04T16:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8575#issuecomment-77550",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_020700.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-05T16:00:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8575",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8575#event-20700"
}
```



---

archive/issue_comments_077551.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-04-05T16:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8575#issuecomment-77551",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_020701.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-05T16:00:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8575",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8575#event-20701"
}
```
