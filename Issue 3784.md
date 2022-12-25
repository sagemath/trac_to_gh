# Issue 3784: add support for SAGE_PYTHONPATH

archive/issues_003784.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\n>\n> > On Aug 6, 9:33 am, Rupert <rupert.n...@gmail.com> wrote:\n> >> Hello there,\n>\n> > Hi Rupert,\n>\n> >> I installed sage this morning and am doing some testing. I noticed\n> >> that sage was ignoring some python modules that live in a directory on\n> >> my PYTHONPATH environment variable.\n>\n> >> Looking in $SAGE_ROOT/local/bin/sage-env, I see that it completely\n> >> overrides my $PYTHONPATH, rather than prepending its own directories.\n>\n> > Yes, we do that on purpose.\n\nHi,\n\n> I propose offering a workaround, e.g.,\n>         SAGE_PYTHONPATH\n> which *does* get appended to PYTHONPATH\n> on startup.\n\nThat sounds reasonable to me.\n\n> Note that this is for picking up *user* code, so\n> it makes a huge amount of sense to support this.\n> It's not an issue of system-wide python being\n> different than Sage's at all.\n\nWell, people will use it to have Sage pick up the extensions of the\nsystem Python, but then I get to tell you \"I told you so\" :)\n```\n\n\nAdd something to sage-env that does what is described above.\nAlso add something to the README.txt that documents this behavior.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3784\n\n",
    "created_at": "2008-08-06T23:48:53Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "add support for SAGE_PYTHONPATH",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3784",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty


```
>
> > On Aug 6, 9:33 am, Rupert <rupert.n...@gmail.com> wrote:
> >> Hello there,
>
> > Hi Rupert,
>
> >> I installed sage this morning and am doing some testing. I noticed
> >> that sage was ignoring some python modules that live in a directory on
> >> my PYTHONPATH environment variable.
>
> >> Looking in $SAGE_ROOT/local/bin/sage-env, I see that it completely
> >> overrides my $PYTHONPATH, rather than prepending its own directories.
>
> > Yes, we do that on purpose.

Hi,

> I propose offering a workaround, e.g.,
>         SAGE_PYTHONPATH
> which *does* get appended to PYTHONPATH
> on startup.

That sounds reasonable to me.

> Note that this is for picking up *user* code, so
> it makes a huge amount of sense to support this.
> It's not an issue of system-wide python being
> different than Sage's at all.

Well, people will use it to have Sage pick up the extensions of the
system Python, but then I get to tell you "I told you so" :)
```


Add something to sage-env that does what is described above.
Also add something to the README.txt that documents this behavior.

Issue created by migration from https://trac.sagemath.org/ticket/3784





---

archive/issue_comments_026839.json:
```json
{
    "body": "This would be very nice for SageTeX, so that the user could put sagetex.py somewhere and use $SAGE_PYTHONPATH to help Sage automatically find the module.",
    "created_at": "2008-12-17T04:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26839",
    "user": "https://github.com/dandrake"
}
```

This would be very nice for SageTeX, so that the user could put sagetex.py somewhere and use $SAGE_PYTHONPATH to help Sage automatically find the module.



---

archive/issue_comments_026840.json:
```json
{
    "body": "Attachment [trac_3784.patch](tarball://root/attachments/some-uuid/ticket3784/trac_3784.patch) by @dandrake created at 2008-12-17 04:55:59\n\npatch for $SAGE_ROOT/local/bin/sage-env",
    "created_at": "2008-12-17T04:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26840",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_3784.patch](tarball://root/attachments/some-uuid/ticket3784/trac_3784.patch) by @dandrake created at 2008-12-17 04:55:59

patch for $SAGE_ROOT/local/bin/sage-env



---

archive/issue_comments_026841.json:
```json
{
    "body": "patch for README.txt in $SAGE_ROOT",
    "created_at": "2008-12-17T04:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26841",
    "user": "https://github.com/dandrake"
}
```

patch for README.txt in $SAGE_ROOT



---

archive/issue_comments_026842.json:
```json
{
    "body": "Attachment [trac_3784_README.patch](tarball://root/attachments/some-uuid/ticket3784/trac_3784_README.patch) by @dandrake created at 2008-12-17 04:57:06",
    "created_at": "2008-12-17T04:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26842",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_3784_README.patch](tarball://root/attachments/some-uuid/ticket3784/trac_3784_README.patch) by @dandrake created at 2008-12-17 04:57:06



---

archive/issue_comments_026843.json:
```json
{
    "body": "I would highly recommend to append PYTHONPATH instead of prepending it. That way if someone has a duplicate python package installed somewhere else, i.e. the system, the Sage packages get preferred treatment. Other people might disagree, so in that case we should take it to sage-devel. So \"needs work\" for now.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-21T12:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26843",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I would highly recommend to append PYTHONPATH instead of prepending it. That way if someone has a duplicate python package installed somewhere else, i.e. the system, the Sage packages get preferred treatment. Other people might disagree, so in that case we should take it to sage-devel. So "needs work" for now.

Cheers,

Michael



---

archive/issue_comments_026844.json:
```json
{
    "body": "This is already the SAGE_PATH variable that is supposed to be for this purpose.",
    "created_at": "2009-10-19T17:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26844",
    "user": "https://github.com/mwhansen"
}
```

This is already the SAGE_PATH variable that is supposed to be for this purpose.



---

archive/issue_comments_026845.json:
```json
{
    "body": "Does the `SAGE_PATH` variable provide all the functionality requested here? (IMHO, it does.)\n\nIn that case, I suggest we close this ticket. There is already a ticket to document the environment variables used by Sage, #8263. I added a comment mentioning `SAGE_PATH` there.",
    "created_at": "2010-05-24T17:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26845",
    "user": "https://github.com/burcin"
}
```

Does the `SAGE_PATH` variable provide all the functionality requested here? (IMHO, it does.)

In that case, I suggest we close this ticket. There is already a ticket to document the environment variables used by Sage, #8263. I added a comment mentioning `SAGE_PATH` there.



---

archive/issue_comments_026846.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2012-03-20T19:21:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26846",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_026847.json:
```json
{
    "body": "Should this be closed? As Burcin says, `SAGE_PATH` solves the problem.",
    "created_at": "2012-03-20T19:21:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26847",
    "user": "https://github.com/jhpalmieri"
}
```

Should this be closed? As Burcin says, `SAGE_PATH` solves the problem.



---

archive/issue_comments_026848.json:
```json
{
    "body": "I think this can be closed.",
    "created_at": "2014-10-21T12:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26848",
    "user": "https://github.com/fchapoton"
}
```

I think this can be closed.



---

archive/issue_comments_026849.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2014-10-21T12:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26849",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_026850.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-10-21T18:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26850",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_026851.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2014-10-27T16:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26851",
    "user": "https://github.com/vbraun"
}
```

Resolution: invalid
