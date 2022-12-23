# Issue 306: switch running branches without building

archive/issues_000306.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: run build\n\nremember that devel conversation some time ago? the request is that\n$sage -r <branch>\nwill switch the running repo to <branch> without building, and just run.\n\nIssue created by migration from https://trac.sagemath.org/ticket/306\n\n",
    "created_at": "2007-03-03T23:47:13Z",
    "labels": [
        "user interface",
        "minor",
        "enhancement"
    ],
    "title": "switch running branches without building",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/306",
    "user": "rlm"
}
```
Assignee: somebody

Keywords: run build

remember that devel conversation some time ago? the request is that
$sage -r <branch>
will switch the running repo to <branch> without building, and just run.

Issue created by migration from https://trac.sagemath.org/ticket/306





---

archive/issue_comments_001456.json:
```json
{
    "body": "Patch submitted by ncalexan to was.\n\nThis patch will not be applied completely, due to problems with modifications to sage-sage (changeset 959a56a4bea4).\n\n\n```\nsage: hg_scripts.incoming('/Users/nalexand/Devel/sage/devel/ncalexan-scripts-clone.hg')\ncd \"/Users/nalexand/Devel/sage/local/bin\" && hg incoming  \"bundle:///Users/nalexand/Devel/sage/devel/ncalexan-scripts-clone.hg\"\nsearching for changes\nchangeset:   190:36ac68b56b85\nparent:      179:f2073346a87c\nuser:        Nick Alexander <ncalexander@gmail.com>\ndate:        Fri Feb 23 17:29:07 2007 -0800\nsummary:     Rework internals to support --quiet and --debugtest; and tests.\n\nchangeset:   191:ebed03fdc467\nuser:        Nick Alexander <ncalexander@gmail.com>\ndate:        Fri Feb 23 17:33:35 2007 -0800\nsummary:     Change test_clone to return an exit code; rework __main__\n\nchangeset:   192:7eb1253a8c34\nuser:        Nick Alexander <ncalexander@gmail.com>\ndate:        Fri Feb 23 18:06:57 2007 -0800\nsummary:     Update docs, suppress sub-command output when --quiet is set, fix a bug in building.\n\nchangeset:   193:4e11c49a3831\nuser:        Nick Alexander <ncalexander@gmail.com>\ndate:        Fri Feb 23 18:29:39 2007 -0800\nsummary:     Move sage-clone to sage_clone.py to expose the interface to Python/SAGE code.\n\nchangeset:   194:42f3fa101edb\nuser:        Nick Alexander <ncalexander@gmail.com>\ndate:        Fri Feb 23 18:32:35 2007 -0800\nsummary:     Revert sage-python to correct argument passing.\n\nchangeset:   195:7b116e34bd14\nuser:        Nick Alexander <ncalexander@gmail.com>\ndate:        Fri Feb 23 18:34:58 2007 -0800\nsummary:     Fix argument passing: $* should be \"$@\".\n\nchangeset:   196:f8c0e970f652\nparent:      179:f2073346a87c\nuser:        Tom Boothby <boothby@u.washington.edu>\ndate:        Mon Feb 19 11:17:19 2007 -0800\nsummary:     Enabled a -cc option to change clone without building.\n\nchangeset:   197:de87709116dc\nuser:        Tom Boothby <boothby@u.washington.edu>\ndate:        Mon Feb 19 11:37:24 2007 -0800\nsummary:     Made sage -cc print a helpful message.\n\nchangeset:   198:dadb937b912a\nparent:      195:7b116e34bd14\nuser:        Nick Alexander <ncalexander@gmail.com>\ndate:        Fri Feb 23 18:53:20 2007 -0800\nsummary:     Update tests to reflect build fix.\n\nchangeset:   199:d931e90fc983\nuser:        Nick Alexander <ncalexander@gmail.com>\ndate:        Fri Feb 23 19:56:13 2007 -0800\nsummary:     Move parsing and printing of current mercurial branch to sage_setup.\n\nchangeset:   200:959a56a4bea4\nuser:        Nick Alexander <ncalexander@gmail.com>\ndate:        Sat Feb 24 18:06:34 2007 -0800\nsummary:     Clean sage-sage: remove darcs option, reorganize, rework 'execute standard software' parsing and execution.\n\nchangeset:   201:b182f94f74c2\nuser:        Nick Alexander <ncalexander@gmail.com>\ndate:        Sat Feb 24 18:23:00 2007 -0800\nsummary:     Address ticket #267: add -bt and -btnew options to sage-sage.\n\nchangeset:   202:61d417011cb4\nparent:      201:b182f94f74c2\nparent:      197:de87709116dc\nuser:        Nick Alexander <ncalexander@gmail.com>\ndate:        Sat Feb 24 18:29:48 2007 -0800\nsummary:     Merged in Tom Boothby's change clone patch.  New option is '-r' for (switch-and-) run.\n\nchangeset:   203:91a624088e1e\nuser:        Nick Alexander <ncalexander@gmail.com>\ndate:        Sat Feb 24 18:35:08 2007 -0800\nsummary:     sage-clone existing-branch now calls sage-chclone if you try to clone over an existing branch.\n\nchangeset:   204:09f187237eed\ntag:         tip\nuser:        Nick Alexander <ncalexander@gmail.com>\ndate:        Sat Feb 24 18:36:30 2007 -0800\nsummary:     Added tag 2.1.4 for changeset f2073346a87c\n```\n",
    "created_at": "2007-03-07T18:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/306#issuecomment-1456",
    "user": "ncalexan"
}
```

Patch submitted by ncalexan to was.

This patch will not be applied completely, due to problems with modifications to sage-sage (changeset 959a56a4bea4).


```
sage: hg_scripts.incoming('/Users/nalexand/Devel/sage/devel/ncalexan-scripts-clone.hg')
cd "/Users/nalexand/Devel/sage/local/bin" && hg incoming  "bundle:///Users/nalexand/Devel/sage/devel/ncalexan-scripts-clone.hg"
searching for changes
changeset:   190:36ac68b56b85
parent:      179:f2073346a87c
user:        Nick Alexander <ncalexander@gmail.com>
date:        Fri Feb 23 17:29:07 2007 -0800
summary:     Rework internals to support --quiet and --debugtest; and tests.

changeset:   191:ebed03fdc467
user:        Nick Alexander <ncalexander@gmail.com>
date:        Fri Feb 23 17:33:35 2007 -0800
summary:     Change test_clone to return an exit code; rework __main__

changeset:   192:7eb1253a8c34
user:        Nick Alexander <ncalexander@gmail.com>
date:        Fri Feb 23 18:06:57 2007 -0800
summary:     Update docs, suppress sub-command output when --quiet is set, fix a bug in building.

changeset:   193:4e11c49a3831
user:        Nick Alexander <ncalexander@gmail.com>
date:        Fri Feb 23 18:29:39 2007 -0800
summary:     Move sage-clone to sage_clone.py to expose the interface to Python/SAGE code.

changeset:   194:42f3fa101edb
user:        Nick Alexander <ncalexander@gmail.com>
date:        Fri Feb 23 18:32:35 2007 -0800
summary:     Revert sage-python to correct argument passing.

changeset:   195:7b116e34bd14
user:        Nick Alexander <ncalexander@gmail.com>
date:        Fri Feb 23 18:34:58 2007 -0800
summary:     Fix argument passing: $* should be "$@".

changeset:   196:f8c0e970f652
parent:      179:f2073346a87c
user:        Tom Boothby <boothby@u.washington.edu>
date:        Mon Feb 19 11:17:19 2007 -0800
summary:     Enabled a -cc option to change clone without building.

changeset:   197:de87709116dc
user:        Tom Boothby <boothby@u.washington.edu>
date:        Mon Feb 19 11:37:24 2007 -0800
summary:     Made sage -cc print a helpful message.

changeset:   198:dadb937b912a
parent:      195:7b116e34bd14
user:        Nick Alexander <ncalexander@gmail.com>
date:        Fri Feb 23 18:53:20 2007 -0800
summary:     Update tests to reflect build fix.

changeset:   199:d931e90fc983
user:        Nick Alexander <ncalexander@gmail.com>
date:        Fri Feb 23 19:56:13 2007 -0800
summary:     Move parsing and printing of current mercurial branch to sage_setup.

changeset:   200:959a56a4bea4
user:        Nick Alexander <ncalexander@gmail.com>
date:        Sat Feb 24 18:06:34 2007 -0800
summary:     Clean sage-sage: remove darcs option, reorganize, rework 'execute standard software' parsing and execution.

changeset:   201:b182f94f74c2
user:        Nick Alexander <ncalexander@gmail.com>
date:        Sat Feb 24 18:23:00 2007 -0800
summary:     Address ticket #267: add -bt and -btnew options to sage-sage.

changeset:   202:61d417011cb4
parent:      201:b182f94f74c2
parent:      197:de87709116dc
user:        Nick Alexander <ncalexander@gmail.com>
date:        Sat Feb 24 18:29:48 2007 -0800
summary:     Merged in Tom Boothby's change clone patch.  New option is '-r' for (switch-and-) run.

changeset:   203:91a624088e1e
user:        Nick Alexander <ncalexander@gmail.com>
date:        Sat Feb 24 18:35:08 2007 -0800
summary:     sage-clone existing-branch now calls sage-chclone if you try to clone over an existing branch.

changeset:   204:09f187237eed
tag:         tip
user:        Nick Alexander <ncalexander@gmail.com>
date:        Sat Feb 24 18:36:30 2007 -0800
summary:     Added tag 2.1.4 for changeset f2073346a87c
```




---

archive/issue_comments_001457.json:
```json
{
    "body": "Changing assignee from somebody to was.",
    "created_at": "2007-03-07T18:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/306#issuecomment-1457",
    "user": "ncalexan"
}
```

Changing assignee from somebody to was.



---

archive/issue_comments_001458.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-11T02:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/306#issuecomment-1458",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_001459.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-08T00:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/306#issuecomment-1459",
    "user": "rlm"
}
```

Resolution: duplicate



---

archive/issue_comments_001460.json:
```json
{
    "body": "Implemented in #1563.",
    "created_at": "2008-03-08T00:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/306#issuecomment-1460",
    "user": "rlm"
}
```

Implemented in #1563.
