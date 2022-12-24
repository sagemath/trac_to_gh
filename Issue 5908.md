# Issue 5908: [with patch; needs review] fix issues/bugs with load/attach

archive/issues_005908.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  mvngu\n\nFrom Rado\n\n```\nAlright, here is my first open-source project patch:\n\nhttp://www.math.uiuc.edu/~rkirov2/sage/11803.patch\n\nThe description in the patch file is short because vi is driving me\ninsane. I was going to add a better description in the .patch file\nwith gedit but wasn't sure if it is checksumed. Here is more detailed\ndescription of what the patch does:\n\n- for sage prompt, I added attached_files to the imported functions in\nsage.misc.all\n- for sage prompt, I added detach magic word (to mirror the build-in\nbehaviour in the notebook).\n- for notebook attach and load, I used shlex.split (shlex is a\nstandard python library for shell commands), instead of regular split.\nThis makes sure that if your file has spacebars you can still call it\nas long as it is enclosed by double-quotation marks i.e. \"file1\".\n- for notebook detach, there was a simple bug (I must be the first one\nto use it), where variable \"filename\" was referenced before being\ndefined.\n- for notebook I exposed the build in function \"attached_files()\", by\nadding it the preparser. This is a bit hacky, since it makes it look\nlike a function but it is not. Things like \"detach attached_files()\n[0]\" won't work in notebook.\n\nOne thing worth mentioning is that in sage prompt, load and attach\ncannot work with multiple files like in notebook. I figured that\nideally the prompt preparser should be unified with the notebook one\n(the notebook code for loading and attaching is quite different),\nwhich is a bigger project and should be well-thought out first.\n\nRado\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5908\n\n",
    "created_at": "2009-04-27T03:38:23Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch; needs review] fix issues/bugs with load/attach",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5908",
    "user": "@williamstein"
}
```
Assignee: cwitty

CC:  mvngu

From Rado

```
Alright, here is my first open-source project patch:

http://www.math.uiuc.edu/~rkirov2/sage/11803.patch

The description in the patch file is short because vi is driving me
insane. I was going to add a better description in the .patch file
with gedit but wasn't sure if it is checksumed. Here is more detailed
description of what the patch does:

- for sage prompt, I added attached_files to the imported functions in
sage.misc.all
- for sage prompt, I added detach magic word (to mirror the build-in
behaviour in the notebook).
- for notebook attach and load, I used shlex.split (shlex is a
standard python library for shell commands), instead of regular split.
This makes sure that if your file has spacebars you can still call it
as long as it is enclosed by double-quotation marks i.e. "file1".
- for notebook detach, there was a simple bug (I must be the first one
to use it), where variable "filename" was referenced before being
defined.
- for notebook I exposed the build in function "attached_files()", by
adding it the preparser. This is a bit hacky, since it makes it look
like a function but it is not. Things like "detach attached_files()
[0]" won't work in notebook.

One thing worth mentioning is that in sage prompt, load and attach
cannot work with multiple files like in notebook. I figured that
ideally the prompt preparser should be unified with the notebook one
(the notebook code for loading and attaching is quite different),
which is a bigger project and should be well-thought out first.

Rado
```


Issue created by migration from https://trac.sagemath.org/ticket/5908





---

archive/issue_comments_046695.json:
```json
{
    "body": "Attachment [11803.patch](tarball://root/attachments/some-uuid/ticket5908/11803.patch) by @ncalexan created at 2009-06-15 05:29:49\n\nThis has an eval in there that seems really bad to me.  And no doctests.  (I once added the machinery to doctest such things, did it ever get merged?)",
    "created_at": "2009-06-15T05:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5908#issuecomment-46695",
    "user": "@ncalexan"
}
```

Attachment [11803.patch](tarball://root/attachments/some-uuid/ticket5908/11803.patch) by @ncalexan created at 2009-06-15 05:29:49

This has an eval in there that seems really bad to me.  And no doctests.  (I once added the machinery to doctest such things, did it ever get merged?)



---

archive/issue_comments_046696.json:
```json
{
    "body": "I put eval, because I mimicked the code for \"attach\" that was already there. I can put some doctests, but is there a guide to doing proper doctests, especially doctests which create temp files and erase them after?",
    "created_at": "2009-06-18T00:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5908#issuecomment-46696",
    "user": "rkirov"
}
```

I put eval, because I mimicked the code for "attach" that was already there. I can put some doctests, but is there a guide to doing proper doctests, especially doctests which create temp files and erase them after?



---

archive/issue_comments_046697.json:
```json
{
    "body": "With the merge of #7514, should we close this ticket?",
    "created_at": "2010-01-16T19:37:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5908#issuecomment-46697",
    "user": "@qed777"
}
```

With the merge of #7514, should we close this ticket?



---

archive/issue_comments_046698.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-02-01T08:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5908#issuecomment-46698",
    "user": "mvngu"
}
```

Resolution: invalid



---

archive/issue_comments_046699.json:
```json
{
    "body": "Close as invalid. If you want to address any specific issue mentioned in the description of this ticket, please open a concise ticket addressing that one issue. I find the goal of the ticket too broad and the ticket's subject too vague.",
    "created_at": "2010-02-01T08:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5908#issuecomment-46699",
    "user": "mvngu"
}
```

Close as invalid. If you want to address any specific issue mentioned in the description of this ticket, please open a concise ticket addressing that one issue. I find the goal of the ticket too broad and the ticket's subject too vague.



---

archive/issue_comments_046700.json:
```json
{
    "body": "yeah, i tested and most of it was fixed. There is still an issue with spacebar in names and also \"attach\" and \"load\" work like \"print\" (in python <3.0) along with their functions. I will make a ticket for those when i have time. At least the notebook and prompt behavior is consistent.",
    "created_at": "2010-02-02T07:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5908#issuecomment-46700",
    "user": "rkirov"
}
```

yeah, i tested and most of it was fixed. There is still an issue with spacebar in names and also "attach" and "load" work like "print" (in python <3.0) along with their functions. I will make a ticket for those when i have time. At least the notebook and prompt behavior is consistent.
