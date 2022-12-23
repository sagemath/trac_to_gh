# Issue 4073: disable colors in sage0

archive/issues_004073.json:
```json
{
    "body": "Assignee: was\n\nCC:  mhansen\n\nThis is related to #4072\n\n\n```\n[20:42] <mhansen> malb: How do you have your ipython colors set up?\n[20:43] <malb> I had: colors LightBG \n[20:43] <malb> now I have colors NoColor\n[20:43] <mhansen> And it sage0 fails with them and passes without them?\n[20:44] <malb> yep\n[20:44] <malb> I think the child process should be started with some option not to use colors\n[20:44] <mhansen> Yep\n[20:44] <malb> maybe by passing in an alternative ipythonrc\n[20:45] <mhansen> I think you can also do it by just evaluating something at the command line.\n[20:46] <malb> %colors NoColor\n[20:47] <malb> I'll open a ticket\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4073\n\n",
    "created_at": "2008-09-07T19:51:57Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "disable colors in sage0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4073",
    "user": "malb"
}
```
Assignee: was

CC:  mhansen

This is related to #4072


```
[20:42] <mhansen> malb: How do you have your ipython colors set up?
[20:43] <malb> I had: colors LightBG 
[20:43] <malb> now I have colors NoColor
[20:43] <mhansen> And it sage0 fails with them and passes without them?
[20:44] <malb> yep
[20:44] <malb> I think the child process should be started with some option not to use colors
[20:44] <mhansen> Yep
[20:44] <malb> maybe by passing in an alternative ipythonrc
[20:45] <mhansen> I think you can also do it by just evaluating something at the command line.
[20:46] <malb> %colors NoColor
[20:47] <malb> I'll open a ticket
```


Issue created by migration from https://trac.sagemath.org/ticket/4073





---

archive/issue_comments_029393.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-09-07T19:59:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4073#issuecomment-29393",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_029394.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-07T22:40:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4073#issuecomment-29394",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_029395.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-07T23:01:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4073#issuecomment-29395",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc1



---

archive/issue_comments_029396.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-07T23:01:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4073#issuecomment-29396",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029397.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-05-26T08:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4073#issuecomment-29397",
    "user": "ddrake"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_029398.json:
```json
{
    "body": "I hate to reopen this, but...the problem has returned in 4.0.alpha0 and 4.0.rc0 (and possibly earlier; I haven't checked). I have exactly the same problem that malb did, but the `'%colors NoColor'` bit isn't working. I had Expect make a logfile, and here's what I get in the logfile when colors are enabled:\n\n```\nLoading Sage library.\nsage: import cPickle\n%colors NoColor\nimport cPickle\nsage: sage0=cPickle.load(open(\"/home/drake/.sage//temp/klee/24661//interface//tmp24661\"))\nprint sage0\n%colors NoColor\n```\n\nBoth \"`sage: `\" prompts are colored. Without color in my ipythonrc file, I get this logfile:\n\n```\nLoading Sage library.\nsage: import cPickle\nimport cPickle\nsage: %colors NoColor\n%colors NoColor\nsage: sage0=cPickle.load(open(\"/home/drake/.sage//temp/klee/25347//interface//tmp25347\"))\n<en(\"/home/drake/.sage//temp/klee/25347//interface//tmp25347\"))              \nsage: print sage0\nprint sage0\n3\n```\n\nIn both cases, I did \"`s = Sage()`\" and \"`a = s(3)`\" in my Sage session. It looks like with color, Expect isn't correctly detecting the prompt.",
    "created_at": "2009-05-26T08:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4073#issuecomment-29398",
    "user": "ddrake"
}
```

I hate to reopen this, but...the problem has returned in 4.0.alpha0 and 4.0.rc0 (and possibly earlier; I haven't checked). I have exactly the same problem that malb did, but the `'%colors NoColor'` bit isn't working. I had Expect make a logfile, and here's what I get in the logfile when colors are enabled:

```
Loading Sage library.
sage: import cPickle
%colors NoColor
import cPickle
sage: sage0=cPickle.load(open("/home/drake/.sage//temp/klee/24661//interface//tmp24661"))
print sage0
%colors NoColor
```

Both "`sage: `" prompts are colored. Without color in my ipythonrc file, I get this logfile:

```
Loading Sage library.
sage: import cPickle
import cPickle
sage: %colors NoColor
%colors NoColor
sage: sage0=cPickle.load(open("/home/drake/.sage//temp/klee/25347//interface//tmp25347"))
<en("/home/drake/.sage//temp/klee/25347//interface//tmp25347"))              
sage: print sage0
print sage0
3
```

In both cases, I did "`s = Sage()`" and "`a = s(3)`" in my Sage session. It looks like with color, Expect isn't correctly detecting the prompt.



---

archive/issue_comments_029399.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-05-26T08:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4073#issuecomment-29399",
    "user": "ddrake"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_029400.json:
```json
{
    "body": "Please don't reopen fixed tickets if the bug has reappeared, even if it seems to be the same bug. Instead open a new ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-26T14:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4073#issuecomment-29400",
    "user": "mabshoff"
}
```

Please don't reopen fixed tickets if the bug has reappeared, even if it seems to be the same bug. Instead open a new ticket.

Cheers,

Michael



---

archive/issue_comments_029401.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-26T14:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4073#issuecomment-29401",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029402.json:
```json
{
    "body": "Replying to [comment:5 mabshoff]:\n> Please don't reopen fixed tickets if the bug has reappeared, even if it seems to be the same bug. Instead open a new ticket.\n\nThe new ticket is #6135.",
    "created_at": "2009-05-26T23:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4073#issuecomment-29402",
    "user": "ddrake"
}
```

Replying to [comment:5 mabshoff]:
> Please don't reopen fixed tickets if the bug has reappeared, even if it seems to be the same bug. Instead open a new ticket.

The new ticket is #6135.
