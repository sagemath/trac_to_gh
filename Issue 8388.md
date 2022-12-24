# Issue 8388: pickle the paths of Rauzy diagrams

archive/issues_008388.json:
```json
{
    "body": "Assignee: vdelecroix\n\nCC:  sage-combinat tmonteil\n\nKeywords: pickle of a nested class\n\nThere is a pickle error with the nested class RauzyDiagram.Path in sage.combinat.iet.template\n\n\n```\nsage: p = iet.Permutation('a b c','c b a')\nsage: r = p.rauzy_diagram()\nsage: g = r.path(p, 't', 'b')\nsage: dumps(g)\nPicklingError Traceback(most recent call last)\n...\nPicklingError: Can't pickle <class 'sage.combinat.iet.labelled.Path'>: attribute lookup sage.combinat.iet.labelled.Path failed\n```\n\n\nA __metaclass__ must be defined for RauzyDiagram.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8388\n\n",
    "created_at": "2010-02-27T16:55:51Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.13",
    "title": "pickle the paths of Rauzy diagrams",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8388",
    "user": "vdelecroix"
}
```
Assignee: vdelecroix

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

archive/issue_comments_075084.json:
```json
{
    "body": "Changing keywords from \"pickle of a nested class\" to \"pickle,  nested class\".",
    "created_at": "2010-02-27T17:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75084",
    "user": "vdelecroix"
}
```

Changing keywords from "pickle of a nested class" to "pickle,  nested class".



---

archive/issue_comments_075085.json:
```json
{
    "body": "Replying to [comment:1 vdelecroix]:\nDo you want it to be reviewed (you didn't check need review). I'm volunteering to review it as soon as #8386 is reviewed.",
    "created_at": "2010-02-27T18:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75085",
    "user": "hivert"
}
```

Replying to [comment:1 vdelecroix]:
Do you want it to be reviewed (you didn't check need review). I'm volunteering to review it as soon as #8386 is reviewed.



---

archive/issue_comments_075086.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-27T22:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75086",
    "user": "vdelecroix"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075087.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2010-02-27T22:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75087",
    "user": "vdelecroix"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_075088.json:
```json
{
    "body": "please add a commit message to your patch (using sage -hg qrefresh -e) starting with #8388 (to make the bot more happy)",
    "created_at": "2011-06-11T20:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75088",
    "user": "chapoton"
}
```

please add a commit message to your patch (using sage -hg qrefresh -e) starting with #8388 (to make the bot more happy)



---

archive/issue_comments_075089.json:
```json
{
    "body": "Does it really depends on #8386 ? The buildbot was happier before I added this dependency.",
    "created_at": "2011-06-11T21:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75089",
    "user": "chapoton"
}
```

Does it really depends on #8386 ? The buildbot was happier before I added this dependency.



---

archive/issue_comments_075090.json:
```json
{
    "body": "Hellooo !!!!\n\nThis ticket can be set to positive review after two changes :\n\n* That it be rebased against a recent version of Sage. The patch applies with a hunk right now\n* That the commit message be changed so as to contain the ticket's number, or the release manager will have to shout `:-D` \n\nNathann",
    "created_at": "2011-10-01T15:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75090",
    "user": "ncohen"
}
```

Hellooo !!!!

This ticket can be set to positive review after two changes :

* That it be rebased against a recent version of Sage. The patch applies with a hunk right now
* That the commit message be changed so as to contain the ticket's number, or the release manager will have to shout `:-D` 

Nathann



---

archive/issue_comments_075091.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-10-01T15:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75091",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075092.json:
```json
{
    "body": "Oh, and let me just add that I was glad to review this ticket : I had to learn what a metaclass was. Great explanation there :\n\nhttp://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python\n\nNathann",
    "created_at": "2011-10-01T15:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75092",
    "user": "ncohen"
}
```

Oh, and let me just add that I was glad to review this ticket : I had to learn what a metaclass was. Great explanation there :

http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python

Nathann



---

archive/issue_comments_075093.json:
```json
{
    "body": "Attachment [trac_8388_pickling_path.patch](tarball://root/attachments/some-uuid/ticket8388/trac_8388_pickling_path.patch) by vdelecroix created at 2012-03-13 00:56:34\n\nDepends on ticket 8386.",
    "created_at": "2012-03-13T00:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75093",
    "user": "vdelecroix"
}
```

Attachment [trac_8388_pickling_path.patch](tarball://root/attachments/some-uuid/ticket8388/trac_8388_pickling_path.patch) by vdelecroix created at 2012-03-13 00:56:34

Depends on ticket 8386.



---

archive/issue_comments_075094.json:
```json
{
    "body": "The test error was due to 8386.",
    "created_at": "2012-04-29T19:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75094",
    "user": "vdelecroix"
}
```

The test error was due to 8386.



---

archive/issue_comments_075095.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-04-29T19:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75095",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075096.json:
```json
{
    "body": "Please fill in your real name as Author.",
    "created_at": "2012-07-27T20:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75096",
    "user": "jdemeyer"
}
```

Please fill in your real name as Author.



---

archive/issue_comments_075097.json:
```json
{
    "body": "apply trac_8388_pickling_path.patch",
    "created_at": "2012-08-29T19:42:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75097",
    "user": "chapoton"
}
```

apply trac_8388_pickling_path.patch



---

archive/issue_comments_075098.json:
```json
{
    "body": "apply trac_8388_pickling_path.v2.patch",
    "created_at": "2012-08-29T19:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75098",
    "user": "chapoton"
}
```

apply trac_8388_pickling_path.v2.patch



---

archive/issue_comments_075099.json:
```json
{
    "body": "apply trac_8388_pickling_path.v2.patch",
    "created_at": "2013-05-23T20:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75099",
    "user": "chapoton"
}
```

apply trac_8388_pickling_path.v2.patch



---

archive/issue_comments_075100.json:
```json
{
    "body": "Attachment [trac_8388_pickling_path.v2.patch](tarball://root/attachments/some-uuid/ticket8388/trac_8388_pickling_path.v2.patch) by chapoton created at 2013-08-29 11:11:36",
    "created_at": "2013-08-29T11:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75100",
    "user": "chapoton"
}
```

Attachment [trac_8388_pickling_path.v2.patch](tarball://root/attachments/some-uuid/ticket8388/trac_8388_pickling_path.v2.patch) by chapoton created at 2013-08-29 11:11:36



---

archive/issue_comments_075101.json:
```json
{
    "body": "apply trac_8388_pickling_path.v2.patch",
    "created_at": "2013-08-29T11:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75101",
    "user": "chapoton"
}
```

apply trac_8388_pickling_path.v2.patch



---

archive/issue_comments_075102.json:
```json
{
    "body": "ok, good enough for me",
    "created_at": "2013-09-15T14:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75102",
    "user": "chapoton"
}
```

ok, good enough for me



---

archive/issue_comments_075103.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-09-15T14:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75103",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075104.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-10-07T06:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8388#issuecomment-75104",
    "user": "jdemeyer"
}
```

Resolution: fixed
