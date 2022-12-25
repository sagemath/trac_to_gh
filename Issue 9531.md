# Issue 9531: spkg-check for gsl does not cause an exit on errors.

archive/issues_009531.json:
```json
{
    "body": "Assignee: drkirkby\n\nThe `spkg-check` file for [GNU Scientific Library (GSL)](http://www.gnu.org/software/gsl/) consists of:\n\n\n```/usr/bin/env bash\n\ncd src\n\nmake check\n\nif [ $? -ne 0 ]; then\n   echo \"Error: make check for GSL failed\"\nfi\n```\n\n\nso the Sage build does not exit if `make check` fails. This is in contrast to virtually all other `spkg-check` files, where they would have:\n\n\n```\nmake check\n\nif [ $? -ne 0 ]; then\n   echo \"Error: make check for GSL failed\"\n   exit 1\nfi\n\n```\n\n\nThe version of GSL in Sage happens to be almost 3 years old too. \n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/9531\n\n",
    "created_at": "2010-07-17T16:39:59Z",
    "labels": [
        "component: spkg-check",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "spkg-check for gsl does not cause an exit on errors.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9531",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

The `spkg-check` file for [GNU Scientific Library (GSL)](http://www.gnu.org/software/gsl/) consists of:


```/usr/bin/env bash

cd src

make check

if [ $? -ne 0 ]; then
   echo "Error: make check for GSL failed"
fi
```


so the Sage build does not exit if `make check` fails. This is in contrast to virtually all other `spkg-check` files, where they would have:


```
make check

if [ $? -ne 0 ]; then
   echo "Error: make check for GSL failed"
   exit 1
fi

```


The version of GSL in Sage happens to be almost 3 years old too. 

Dave 

Issue created by migration from https://trac.sagemath.org/ticket/9531





---

archive/issue_comments_091605.json:
```json
{
    "body": "I've created #9533 to update the version of GSL and to fix the spkg-check issues at the same time. When #9533 is merged, this ticket can be closed.",
    "created_at": "2010-07-18T22:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9531#issuecomment-91605",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've created #9533 to update the version of GSL and to fix the spkg-check issues at the same time. When #9533 is merged, this ticket can be closed.



---

archive/issue_events_009679.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-08-15T02:03:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9531",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9531#event-9679"
}
```



---

archive/issue_comments_091606.json:
```json
{
    "body": "I'm closing this as a \"duplicate\" of #9533.",
    "created_at": "2010-08-15T02:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9531#issuecomment-91606",
    "user": "https://github.com/qed777"
}
```

I'm closing this as a "duplicate" of #9533.



---

archive/issue_comments_091607.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-08-15T02:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9531#issuecomment-91607",
    "user": "https://github.com/qed777"
}
```

Resolution: duplicate
