# Issue 8388: pickle the paths of Rauzy diagrams

archive/issues_008388.json:
```json
{
    "body": "Assignee: @videlec\n\nCC:  sage-combinat tmonteil\n\nKeywords: pickle of a nested class\n\nThere is a pickle error with the nested class RauzyDiagram.Path in sage.combinat.iet.template\n\n```\nsage: p = iet.Permutation('a b c','c b a')\nsage: r = p.rauzy_diagram()\nsage: g = r.path(p, 't', 'b')\nsage: dumps(g)\nPicklingError Traceback(most recent call last)\n...\nPicklingError: Can't pickle <class 'sage.combinat.iet.labelled.Path'>: attribute lookup sage.combinat.iet.labelled.Path failed\n```\n\nA __metaclass__ must be defined for RauzyDiagram.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8388\n\n",
    "created_at": "2010-02-27T16:55:51Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.13",
    "title": "pickle the paths of Rauzy diagrams",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8388",
    "user": "https://github.com/videlec"
}
```
Assignee: @videlec

CC:  sage-combinat tmonteil

Keywords: pickle of a nested class

There is a pickle error with the nested class RauzyDiagram.Path in sage.combinat.iet.template

```
sage: p = iet.Permutation('a b c','c b a')
sage: r = p.rauzy_diagram()
sage: g = r.path(p, 't', 'b')
sage: dumps(g)
PicklingError Traceback(most recent call last)
...
PicklingError: Can't pickle <class 'sage.combinat.iet.labelled.Path'>: attribute lookup sage.combinat.iet.labelled.Path failed
```

A __metaclass__ must be defined for RauzyDiagram.

Issue created by migration from https://trac.sagemath.org/ticket/8388





---

archive/issue_comments_074960.json:
```json
{
    "body": "Changing keywords from \"pickle of a nested class\" to \"pickle,  nested class\".",
    "created_at": "2010-02-27T17:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74960",
    "user": "https://github.com/videlec"
}
```

Changing keywords from "pickle of a nested class" to "pickle,  nested class".



---

archive/issue_comments_074961.json:
```json
{
    "body": "Replying to [comment:1 vdelecroix]:\nDo you want it to be reviewed (you didn't check need review). I'm volunteering to review it as soon as #8386 is reviewed.",
    "created_at": "2010-02-27T18:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74961",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:1 vdelecroix]:
Do you want it to be reviewed (you didn't check need review). I'm volunteering to review it as soon as #8386 is reviewed.



---

archive/issue_comments_074962.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-27T22:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74962",
    "user": "https://github.com/videlec"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074963.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2010-02-27T22:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74963",
    "user": "https://github.com/videlec"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_074964.json:
```json
{
    "body": "please add a commit message to your patch (using sage -hg qrefresh -e) starting with #8388 (to make the bot more happy)",
    "created_at": "2011-06-11T20:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74964",
    "user": "https://github.com/fchapoton"
}
```

please add a commit message to your patch (using sage -hg qrefresh -e) starting with #8388 (to make the bot more happy)



---

archive/issue_comments_074965.json:
```json
{
    "body": "Does it really depends on #8386 ? The buildbot was happier before I added this dependency.",
    "created_at": "2011-06-11T21:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74965",
    "user": "https://github.com/fchapoton"
}
```

Does it really depends on #8386 ? The buildbot was happier before I added this dependency.



---

archive/issue_comments_074966.json:
```json
{
    "body": "Hellooo !!!!\n\nThis ticket can be set to positive review after two changes :\n\n* That it be rebased against a recent version of Sage. The patch applies with a hunk right now\n* That the commit message be changed so as to contain the ticket's number, or the release manager will have to shout `:-D` \n\nNathann",
    "created_at": "2011-10-01T15:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74966",
    "user": "https://github.com/nathanncohen"
}
```

Hellooo !!!!

This ticket can be set to positive review after two changes :

* That it be rebased against a recent version of Sage. The patch applies with a hunk right now
* That the commit message be changed so as to contain the ticket's number, or the release manager will have to shout `:-D` 

Nathann



---

archive/issue_comments_074967.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-10-01T15:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74967",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074968.json:
```json
{
    "body": "Oh, and let me just add that I was glad to review this ticket : I had to learn what a metaclass was. Great explanation there :\n\nhttp://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python\n\nNathann",
    "created_at": "2011-10-01T15:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74968",
    "user": "https://github.com/nathanncohen"
}
```

Oh, and let me just add that I was glad to review this ticket : I had to learn what a metaclass was. Great explanation there :

http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python

Nathann



---

archive/issue_comments_074969.json:
```json
{
    "body": "Attachment [trac_8388_pickling_path.patch](tarball://root/attachments/some-uuid/ticket8388/trac_8388_pickling_path.patch) by @videlec created at 2012-03-13 00:56:34\n\nDepends on ticket 8386.",
    "created_at": "2012-03-13T00:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74969",
    "user": "https://github.com/videlec"
}
```

Attachment [trac_8388_pickling_path.patch](tarball://root/attachments/some-uuid/ticket8388/trac_8388_pickling_path.patch) by @videlec created at 2012-03-13 00:56:34

Depends on ticket 8386.



---

archive/issue_comments_074970.json:
```json
{
    "body": "The test error was due to 8386.",
    "created_at": "2012-04-29T19:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74970",
    "user": "https://github.com/videlec"
}
```

The test error was due to 8386.



---

archive/issue_comments_074971.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-04-29T19:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74971",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074972.json:
```json
{
    "body": "Please fill in your real name as Author.",
    "created_at": "2012-07-27T20:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74972",
    "user": "https://github.com/jdemeyer"
}
```

Please fill in your real name as Author.



---

archive/issue_comments_074973.json:
```json
{
    "body": "apply trac_8388_pickling_path.patch",
    "created_at": "2012-08-29T19:42:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74973",
    "user": "https://github.com/fchapoton"
}
```

apply trac_8388_pickling_path.patch



---

archive/issue_comments_074974.json:
```json
{
    "body": "apply trac_8388_pickling_path.v2.patch",
    "created_at": "2012-08-29T19:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74974",
    "user": "https://github.com/fchapoton"
}
```

apply trac_8388_pickling_path.v2.patch



---

archive/issue_comments_074975.json:
```json
{
    "body": "apply trac_8388_pickling_path.v2.patch",
    "created_at": "2013-05-23T20:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74975",
    "user": "https://github.com/fchapoton"
}
```

apply trac_8388_pickling_path.v2.patch



---

archive/issue_events_020114.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8388#event-20114"
}
```



---

archive/issue_comments_074976.json:
```json
{
    "body": "Attachment [trac_8388_pickling_path.v2.patch](tarball://root/attachments/some-uuid/ticket8388/trac_8388_pickling_path.v2.patch) by @fchapoton created at 2013-08-29 11:11:36",
    "created_at": "2013-08-29T11:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74976",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_8388_pickling_path.v2.patch](tarball://root/attachments/some-uuid/ticket8388/trac_8388_pickling_path.v2.patch) by @fchapoton created at 2013-08-29 11:11:36



---

archive/issue_comments_074977.json:
```json
{
    "body": "apply trac_8388_pickling_path.v2.patch",
    "created_at": "2013-08-29T11:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74977",
    "user": "https://github.com/fchapoton"
}
```

apply trac_8388_pickling_path.v2.patch



---

archive/issue_comments_074978.json:
```json
{
    "body": "ok, good enough for me",
    "created_at": "2013-09-15T14:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74978",
    "user": "https://github.com/fchapoton"
}
```

ok, good enough for me



---

archive/issue_comments_074979.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-09-15T14:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74979",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_020115.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-10-01T07:19:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8388#event-20115"
}
```



---

archive/issue_events_020116.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-10-01T07:19:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "milestone": "sage-5.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8388#event-20116"
}
```



---

archive/issue_events_020117.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-10-07T06:49:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8388#event-20117"
}
```



---

archive/issue_comments_074980.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-10-07T06:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-74980",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
