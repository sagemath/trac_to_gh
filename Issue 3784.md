# Issue 3784: add support for SAGE_PYTHONPATH

archive/issues_003784.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\n>\n> > On Aug 6, 9:33 am, Rupert <rupert.n...@gmail.com> wrote:\n> >> Hello there,\n>\n> > Hi Rupert,\n>\n> >> I installed sage this morning and am doing some testing. I noticed\n> >> that sage was ignoring some python modules that live in a directory on\n> >> my PYTHONPATH environment variable.\n>\n> >> Looking in $SAGE_ROOT/local/bin/sage-env, I see that it completely\n> >> overrides my $PYTHONPATH, rather than prepending its own directories.\n>\n> > Yes, we do that on purpose.\n\nHi,\n\n> I propose offering a workaround, e.g.,\n>         SAGE_PYTHONPATH\n> which *does* get appended to PYTHONPATH\n> on startup.\n\nThat sounds reasonable to me.\n\n> Note that this is for picking up *user* code, so\n> it makes a huge amount of sense to support this.\n> It's not an issue of system-wide python being\n> different than Sage's at all.\n\nWell, people will use it to have Sage pick up the extensions of the\nsystem Python, but then I get to tell you \"I told you so\" :)\n```\n\n\nAdd something to sage-env that does what is described above.\nAlso add something to the README.txt that documents this behavior.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3784\n\n",
    "created_at": "2008-08-06T23:48:53Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "add support for SAGE_PYTHONPATH",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3784",
    "user": "was"
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

archive/issue_comments_026897.json:
```json
{
    "body": "This would be very nice for SageTeX, so that the user could put sagetex.py somewhere and use $SAGE_PYTHONPATH to help Sage automatically find the module.",
    "created_at": "2008-12-17T04:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26897",
    "user": "ddrake"
}
```

This would be very nice for SageTeX, so that the user could put sagetex.py somewhere and use $SAGE_PYTHONPATH to help Sage automatically find the module.



---

archive/issue_comments_026898.json:
```json
{
    "body": "Attachment [trac_3784.patch](tarball://root/attachments/some-uuid/ticket3784/trac_3784.patch) by ddrake created at 2008-12-17 04:55:59\n\npatch for $SAGE_ROOT/local/bin/sage-env",
    "created_at": "2008-12-17T04:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26898",
    "user": "ddrake"
}
```

Attachment [trac_3784.patch](tarball://root/attachments/some-uuid/ticket3784/trac_3784.patch) by ddrake created at 2008-12-17 04:55:59

patch for $SAGE_ROOT/local/bin/sage-env



---

archive/issue_comments_026899.json:
```json
{
    "body": "patch for README.txt in $SAGE_ROOT",
    "created_at": "2008-12-17T04:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26899",
    "user": "ddrake"
}
```

patch for README.txt in $SAGE_ROOT



---

archive/issue_comments_026900.json:
```json
{
    "body": "Attachment [trac_3784_README.patch](tarball://root/attachments/some-uuid/ticket3784/trac_3784_README.patch) by ddrake created at 2008-12-17 04:57:06",
    "created_at": "2008-12-17T04:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26900",
    "user": "ddrake"
}
```

Attachment [trac_3784_README.patch](tarball://root/attachments/some-uuid/ticket3784/trac_3784_README.patch) by ddrake created at 2008-12-17 04:57:06



---

archive/issue_comments_026901.json:
```json
{
    "body": "I would highly recommend to append PYTHONPATH instead of prepending it. That way if someone has a duplicate python package installed somewhere else, i.e. the system, the Sage packages get preferred treatment. Other people might disagree, so in that case we should take it to sage-devel. So \"needs work\" for now.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-21T12:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26901",
    "user": "mabshoff"
}
```

I would highly recommend to append PYTHONPATH instead of prepending it. That way if someone has a duplicate python package installed somewhere else, i.e. the system, the Sage packages get preferred treatment. Other people might disagree, so in that case we should take it to sage-devel. So "needs work" for now.

Cheers,

Michael



---

archive/issue_comments_026902.json:
```json
{
    "body": "This is already the SAGE_PATH variable that is supposed to be for this purpose.",
    "created_at": "2009-10-19T17:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26902",
    "user": "mhansen"
}
```

This is already the SAGE_PATH variable that is supposed to be for this purpose.



---

archive/issue_comments_026903.json:
```json
{
    "body": "Does the `SAGE_PATH` variable provide all the functionality requested here? (IMHO, it does.)\n\nIn that case, I suggest we close this ticket. There is already a ticket to document the environment variables used by Sage, #8263. I added a comment mentioning `SAGE_PATH` there.",
    "created_at": "2010-05-24T17:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26903",
    "user": "burcin"
}
```

Does the `SAGE_PATH` variable provide all the functionality requested here? (IMHO, it does.)

In that case, I suggest we close this ticket. There is already a ticket to document the environment variables used by Sage, #8263. I added a comment mentioning `SAGE_PATH` there.



---

archive/issue_comments_026904.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2012-03-20T19:21:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26904",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_026905.json:
```json
{
    "body": "Should this be closed? As Burcin says, `SAGE_PATH` solves the problem.",
    "created_at": "2012-03-20T19:21:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26905",
    "user": "jhpalmieri"
}
```

Should this be closed? As Burcin says, `SAGE_PATH` solves the problem.



---

archive/issue_comments_026906.json:
```json
{
    "body": "I think this can be closed.",
    "created_at": "2014-10-21T12:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26906",
    "user": "chapoton"
}
```

I think this can be closed.



---

archive/issue_comments_026907.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2014-10-21T12:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26907",
    "user": "chapoton"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_026908.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-10-21T18:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26908",
    "user": "aapitzsch"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_026909.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2014-10-27T16:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3784#issuecomment-26909",
    "user": "vbraun"
}
```

Resolution: invalid
