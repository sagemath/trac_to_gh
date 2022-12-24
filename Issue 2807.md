# Issue 2807: line 26 of c_lib/src/interrupt.c is probably wrong

archive/issues_002807.json:
```json
{
    "body": "Assignee: cwitty\n\nLine 26 of c_lib/src/interrupt.c says:\n\n\n```\n if ( _signals.mpio && 1 ) {\n```\n\n\nit should probably be\n\n\n```\nif ( _signals.mpio & 1 ) {\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2807\n\n",
    "created_at": "2008-04-05T14:50:26Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "line 26 of c_lib/src/interrupt.c is probably wrong",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2807",
    "user": "dmharvey"
}
```
Assignee: cwitty

Line 26 of c_lib/src/interrupt.c says:


```
 if ( _signals.mpio && 1 ) {
```


it should probably be


```
if ( _signals.mpio & 1 ) {
```



Issue created by migration from https://trac.sagemath.org/ticket/2807





---

archive/issue_comments_019270.json:
```json
{
    "body": "Attachment [2807.patch](tarball://root/attachments/some-uuid/ticket2807/2807.patch) by dmharvey created at 2008-04-05 15:01:56",
    "created_at": "2008-04-05T15:01:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2807#issuecomment-19270",
    "user": "dmharvey"
}
```

Attachment [2807.patch](tarball://root/attachments/some-uuid/ticket2807/2807.patch) by dmharvey created at 2008-04-05 15:01:56



---

archive/issue_comments_019271.json:
```json
{
    "body": "I've made a patch, have no idea if it will work.\n\n\n```\n[10:45am] dmharvey: that's #2807\n[10:46am] mabshoff: Well, let's hope we close more tickets today than we open.\n[10:46am] dmharvey: I can easily close that one, but I wonder if it will introduce strange bugs....\n[10:46am] malb: this line means: we always use Sage's signal handler\n[10:47am] malb: which isn't too bad apparently if it handles all the signals we come across ;-)\n[10:47am] malb: it probably won't change much\n[10:47am] dmharvey: i will make a patch\n```\n",
    "created_at": "2008-04-05T15:03:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2807#issuecomment-19271",
    "user": "dmharvey"
}
```

I've made a patch, have no idea if it will work.


```
[10:45am] dmharvey: that's #2807
[10:46am] mabshoff: Well, let's hope we close more tickets today than we open.
[10:46am] dmharvey: I can easily close that one, but I wonder if it will introduce strange bugs....
[10:46am] malb: this line means: we always use Sage's signal handler
[10:47am] malb: which isn't too bad apparently if it handles all the signals we come across ;-)
[10:47am] malb: it probably won't change much
[10:47am] dmharvey: i will make a patch
```




---

archive/issue_comments_019272.json:
```json
{
    "body": "Patch is correct and passes doctests. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-05T15:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2807#issuecomment-19272",
    "user": "mabshoff"
}
```

Patch is correct and passes doctests. Positive review.

Cheers,

Michael



---

archive/issue_comments_019273.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-05T15:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2807#issuecomment-19273",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019274.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-05T15:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2807#issuecomment-19274",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2
