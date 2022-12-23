# Issue 6369: the sage cleaner should kill all notebook servers if sage that spawned them is killed

archive/issues_006369.json:
```json
{
    "body": "Assignee: boothby\n\nTry this:\n\n1. `sage -notebook foo`\n2. Find the pid of the sage -notebook process with `ps ax |grep \"sage -notebook\"`\n3. Kill that process with `kill -9 [pid]`\n4. The notebook server is still going.  And now the only way to kill it is with `ps ax |grep tracd` and start killing things until you hit the right one.\n\nSince people, especially new sage users, often kill the notebook server by, e.g., clicking kill in a terminal or some other silly means, it would be much better if the sage-cleaner could at least step in and kill the notebook server, so it gets shut down cleanly (saving its state), and doesn't stop the notebook from running in the future (if it is always running, it can't run again), hence confusing users.\n\nTo do all this is probably as simple as calling one little register function in sage.misc.cleaner.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6369\n\n",
    "created_at": "2009-06-20T15:34:43Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "the sage cleaner should kill all notebook servers if sage that spawned them is killed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6369",
    "user": "was"
}
```
Assignee: boothby

Try this:

1. `sage -notebook foo`
2. Find the pid of the sage -notebook process with `ps ax |grep "sage -notebook"`
3. Kill that process with `kill -9 [pid]`
4. The notebook server is still going.  And now the only way to kill it is with `ps ax |grep tracd` and start killing things until you hit the right one.

Since people, especially new sage users, often kill the notebook server by, e.g., clicking kill in a terminal or some other silly means, it would be much better if the sage-cleaner could at least step in and kill the notebook server, so it gets shut down cleanly (saving its state), and doesn't stop the notebook from running in the future (if it is always running, it can't run again), hence confusing users.

To do all this is probably as simple as calling one little register function in sage.misc.cleaner.

Issue created by migration from https://trac.sagemath.org/ticket/6369





---

archive/issue_comments_050942.json:
```json
{
    "body": "This seems to be fixed now. `kill [pid]` kills the notebook as well. SIG_KILL doesn't seem like it will allow sage-cleaner to kill the notebook since it will be killed immediately. Confirm and close?",
    "created_at": "2010-01-19T07:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6369#issuecomment-50942",
    "user": "timdumol"
}
```

This seems to be fixed now. `kill [pid]` kills the notebook as well. SIG_KILL doesn't seem like it will allow sage-cleaner to kill the notebook since it will be killed immediately. Confirm and close?



---

archive/issue_comments_050943.json:
```json
{
    "body": "This definitely kills the process but also definitely keeps the server going!  (And a number of other processes as well.)",
    "created_at": "2014-12-10T19:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6369#issuecomment-50943",
    "user": "kcrisman"
}
```

This definitely kills the process but also definitely keeps the server going!  (And a number of other processes as well.)



---

archive/issue_comments_050944.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6369#issuecomment-50944",
    "user": "boothby"
}
```

Resolution: invalid



---

archive/issue_comments_050945.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6369#issuecomment-50945",
    "user": "boothby"
}
```

Closing deprecated notebook tickets
