# Issue 3017: invalid link after make install

archive/issues_003017.json:
```json
{
    "body": "Assignee: mabshoff\n\nAn invalid link is present in sage 3.0 (after make install):\n\n```\n[root@achille local]# ls -l ./sage-3.0/sage/local/lib/python2.5/site-packages/polybori/polybori\nlrwxrwxrwx 1 zimmerma cacao 39 2008-04-24 14:43 ./sage-3.0/sage/local/lib/python2.5/site-packages/polybori/polybori -> ../../../share/polybori/pyroot/polybori\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3017\n\n",
    "created_at": "2008-04-24T12:54:29Z",
    "labels": [
        "distribution",
        "minor",
        "bug"
    ],
    "title": "invalid link after make install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3017",
    "user": "zimmerma"
}
```
Assignee: mabshoff

An invalid link is present in sage 3.0 (after make install):

```
[root@achille local]# ls -l ./sage-3.0/sage/local/lib/python2.5/site-packages/polybori/polybori
lrwxrwxrwx 1 zimmerma cacao 39 2008-04-24 14:43 ./sage-3.0/sage/local/lib/python2.5/site-packages/polybori/polybori -> ../../../share/polybori/pyroot/polybori
```


Issue created by migration from https://trac.sagemath.org/ticket/3017





---

archive/issue_comments_020729.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-26T05:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3017#issuecomment-20729",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020730.json:
```json
{
    "body": "This link is actually pointing to hyperspace *before* make install and due to our spkg-install. It is easy to fix, so I am on it.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T05:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3017#issuecomment-20730",
    "user": "mabshoff"
}
```

This link is actually pointing to hyperspace *before* make install and due to our spkg-install. It is easy to fix, so I am on it.

Cheers,

Michael



---

archive/issue_comments_020731.json:
```json
{
    "body": "The updated spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.1/alpha0/polybori-0.3.1.p2.spkg\n\nfixes the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T05:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3017#issuecomment-20731",
    "user": "mabshoff"
}
```

The updated spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.1/alpha0/polybori-0.3.1.p2.spkg

fixes the issue.

Cheers,

Michael



---

archive/issue_comments_020732.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-26T06:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3017#issuecomment-20732",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_020733.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha0",
    "created_at": "2008-04-26T06:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3017#issuecomment-20733",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha0



---

archive/issue_comments_020734.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-26T06:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3017#issuecomment-20734",
    "user": "mabshoff"
}
```

Resolution: fixed
