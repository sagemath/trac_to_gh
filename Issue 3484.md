# Issue 3484: [with patch, needs review] extend sage_eval (in preparation for sage_input)

archive/issues_003484.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  ncalexan wstein\n\nThis patch creates some new functionality in sage_eval: the preparser can be disabled; a sequence of commands can be specified, which will be run before the string is evaluated; and there are new calling conventions that take a tuple instead of a string.\n\nThese new calling conventions are useful for the proposed sage_input function (so that `sage_eval(sage_input(...))` works); but the other new functionality is generally useful, so I think it's reasonable to review and apply this patch even though sage_input is not ready for submission.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3484\n\n",
    "created_at": "2008-06-20T08:01:48Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] extend sage_eval (in preparation for sage_input)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3484",
    "user": "cwitty"
}
```
Assignee: cwitty

CC:  ncalexan wstein

This patch creates some new functionality in sage_eval: the preparser can be disabled; a sequence of commands can be specified, which will be run before the string is evaluated; and there are new calling conventions that take a tuple instead of a string.

These new calling conventions are useful for the proposed sage_input function (so that `sage_eval(sage_input(...))` works); but the other new functionality is generally useful, so I think it's reasonable to review and apply this patch even though sage_input is not ready for submission.

Issue created by migration from https://trac.sagemath.org/ticket/3484





---

archive/issue_comments_024554.json:
```json
{
    "body": "Attachment [trac3484-sage_eval.patch](tarball://root/attachments/some-uuid/ticket3484/trac3484-sage_eval.patch) by cwitty created at 2008-06-20 08:02:44",
    "created_at": "2008-06-20T08:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3484#issuecomment-24554",
    "user": "cwitty"
}
```

Attachment [trac3484-sage_eval.patch](tarball://root/attachments/some-uuid/ticket3484/trac3484-sage_eval.patch) by cwitty created at 2008-06-20 08:02:44



---

archive/issue_comments_024555.json:
```json
{
    "body": "I will ping somebody to review this patch and #3485 soon.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T10:59:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3484#issuecomment-24555",
    "user": "mabshoff"
}
```

I will ping somebody to review this patch and #3485 soon.

Cheers,

Michael



---

archive/issue_comments_024556.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-07-06T10:59:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3484#issuecomment-24556",
    "user": "mabshoff"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_024557.json:
```json
{
    "body": "REFEREE DISCUSSION (irc log):\n\n\n```\n22:36 < wstein-3764> cwitty -- ping\n22:36 < cwitty> Yo.\n22:36 < wstein-3764> this gives an error as it should:\n22:36 < wstein-3764> sage: sage_eval('z=5', locals=vars)\n22:37 < wstein-3764> this doesn't give an error:\n22:37 < wstein-3764> sage: sage_eval('z=5', cmd='y=3', locals=vars)\n22:37 < wstein-3764> I guess that's ok, but just wanted to get your feedback.\n22:37 < wstein-3764> The point is that the expression being evaluated can be a statement \n22:37 < wstein-3764> without error in case of giving the optional cmd.\n22:38 < cwitty> Let me look at the code for a minute.\n22:39 < wstein-3764> the docstrings for #3484 are really good.\n22:40 < cwitty> IMHO it's not worth fixing.  (I'm not sure even how it could be fixed... I guess we could try to parse the \n                expression.)\n22:40 < cwitty> Thanks!\n22:40 < wstein-3764> OK, i just wanted to check with you.\n22:40 < wstein-3764> I'm not that worried about something just accidently working...\n22:43 -!- mabshoff [n=michaela@wclient1.irmacs.sfu.ca] has quit [Read error: 104 (Connection reset by peer)]\n22:46 < wstein-3764> cwitty -- this sets of an alarm bell for me:\n22:46 < wstein-3764> raise SyntaxError, \"%s\\nError using SAGE to evaluate '%s'\"%(msg, cmd_seq if len(cmds) else source) \n22:46 < wstein-3764> Here's why -- many many times I've been bit by error messages that innocently\n22:47 < wstein-3764> include a %s in them.   This is for two reasons:\n22:47 < wstein-3764> (1) the error message could easily be massive, and (2) [much much worse], an\n22:47 < wstein-3764> exception can get raised in the normal course of a computation, and it can\n22:48 < wstein-3764> be very bad when the exception takes vastly longer to raise than the whole computation.\n22:48 < wstein-3764> cwitty -- ping\n22:48 < cwitty> Yes, I'm thinking.\n22:49 < wstein-3764> So I prefer to change the message to:\n22:49 < wstein-3764> raise SyntaxError\n22:49 < wstein-3764> SyntaxError, \"invalid syntax\"\n22:49 < wstein-3764> That's what Python does.\n22:50 < cwitty> OK, I guess.\n22:50 < wstein-3764> i'll change it.\n22:51 < cwitty> I don't think your 2) is an issue in this case, because both %s will be substituting strings.\n22:51 < wstein-3764> true.\n22:51 < wstein-3764> But changing to \"invalid syntax\" is perhaps more consistent with python...\n22:52 < wstein-3764> Also there is another exception just above in the code and it looks like this:\n22:52 < wstein-3764> raise TypeError, \"source must be a string.\" \n22:52 < wstein-3764> It doesn't say what the string is.\n22:52 < wstein-3764> or the source.\n22:52 < cwitty> If that's what Python does, then probably msg is already \"invalid syntax\", so we could just skip the whole \n                try/except.\n22:53 -!- mabshoff [n=michaela@wclient1.irmacs.sfu.ca] has joined #sage-devel\n22:53 < wstein-3764> good point!\n22:54 < wstein-3764> can you actually do this and put in a doctest to illustrate it, so I can referee #3485?\n22:54 < cwitty> You added that try/except in July 2006.\n22:54 < wstein-3764> I know.  It's really my fault.\n22:54 < wstein-3764> I'm just trying to trick you into doing something :-)\n22:54 < cwitty> Sure, I can do that.\n22:55 < wstein-3764> thanks!\n```\n\n\nPositive review when there is a patch that gets rid of that try/except block and adds\na doctest illustrating a syntax error.",
    "created_at": "2008-08-10T05:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3484#issuecomment-24557",
    "user": "was"
}
```

REFEREE DISCUSSION (irc log):


```
22:36 < wstein-3764> cwitty -- ping
22:36 < cwitty> Yo.
22:36 < wstein-3764> this gives an error as it should:
22:36 < wstein-3764> sage: sage_eval('z=5', locals=vars)
22:37 < wstein-3764> this doesn't give an error:
22:37 < wstein-3764> sage: sage_eval('z=5', cmd='y=3', locals=vars)
22:37 < wstein-3764> I guess that's ok, but just wanted to get your feedback.
22:37 < wstein-3764> The point is that the expression being evaluated can be a statement 
22:37 < wstein-3764> without error in case of giving the optional cmd.
22:38 < cwitty> Let me look at the code for a minute.
22:39 < wstein-3764> the docstrings for #3484 are really good.
22:40 < cwitty> IMHO it's not worth fixing.  (I'm not sure even how it could be fixed... I guess we could try to parse the 
                expression.)
22:40 < cwitty> Thanks!
22:40 < wstein-3764> OK, i just wanted to check with you.
22:40 < wstein-3764> I'm not that worried about something just accidently working...
22:43 -!- mabshoff [n=michaela@wclient1.irmacs.sfu.ca] has quit [Read error: 104 (Connection reset by peer)]
22:46 < wstein-3764> cwitty -- this sets of an alarm bell for me:
22:46 < wstein-3764> raise SyntaxError, "%s\nError using SAGE to evaluate '%s'"%(msg, cmd_seq if len(cmds) else source) 
22:46 < wstein-3764> Here's why -- many many times I've been bit by error messages that innocently
22:47 < wstein-3764> include a %s in them.   This is for two reasons:
22:47 < wstein-3764> (1) the error message could easily be massive, and (2) [much much worse], an
22:47 < wstein-3764> exception can get raised in the normal course of a computation, and it can
22:48 < wstein-3764> be very bad when the exception takes vastly longer to raise than the whole computation.
22:48 < wstein-3764> cwitty -- ping
22:48 < cwitty> Yes, I'm thinking.
22:49 < wstein-3764> So I prefer to change the message to:
22:49 < wstein-3764> raise SyntaxError
22:49 < wstein-3764> SyntaxError, "invalid syntax"
22:49 < wstein-3764> That's what Python does.
22:50 < cwitty> OK, I guess.
22:50 < wstein-3764> i'll change it.
22:51 < cwitty> I don't think your 2) is an issue in this case, because both %s will be substituting strings.
22:51 < wstein-3764> true.
22:51 < wstein-3764> But changing to "invalid syntax" is perhaps more consistent with python...
22:52 < wstein-3764> Also there is another exception just above in the code and it looks like this:
22:52 < wstein-3764> raise TypeError, "source must be a string." 
22:52 < wstein-3764> It doesn't say what the string is.
22:52 < wstein-3764> or the source.
22:52 < cwitty> If that's what Python does, then probably msg is already "invalid syntax", so we could just skip the whole 
                try/except.
22:53 -!- mabshoff [n=michaela@wclient1.irmacs.sfu.ca] has joined #sage-devel
22:53 < wstein-3764> good point!
22:54 < wstein-3764> can you actually do this and put in a doctest to illustrate it, so I can referee #3485?
22:54 < cwitty> You added that try/except in July 2006.
22:54 < wstein-3764> I know.  It's really my fault.
22:54 < wstein-3764> I'm just trying to trick you into doing something :-)
22:54 < cwitty> Sure, I can do that.
22:55 < wstein-3764> thanks!
```


Positive review when there is a patch that gets rid of that try/except block and adds
a doctest illustrating a syntax error.



---

archive/issue_comments_024558.json:
```json
{
    "body": "Attachment [trac3484-sage_eval-review-response.patch](tarball://root/attachments/some-uuid/ticket3484/trac3484-sage_eval-review-response.patch) by was created at 2008-08-10 06:28:37\n\nAWESOME.",
    "created_at": "2008-08-10T06:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3484#issuecomment-24558",
    "user": "was"
}
```

Attachment [trac3484-sage_eval-review-response.patch](tarball://root/attachments/some-uuid/ticket3484/trac3484-sage_eval-review-response.patch) by was created at 2008-08-10 06:28:37

AWESOME.



---

archive/issue_comments_024559.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-10T08:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3484#issuecomment-24559",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024560.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-10T08:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3484#issuecomment-24560",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha1
