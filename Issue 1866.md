# Issue 1866: bug in doctesting -- long time not respected in some contexts

archive/issues_001866.json:
```json
{
    "body": "Assignee: failure\n\nCC:  @orlitzky\n\n\n```\nOn Jan 20, 2008 7:28 AM, Lars Fischer <> wrote:\n> \n> Hello,\n> \n> I think I have found a bug:\n> chapter 2.4.1 of the Programming guide states, that comments like \"#\n> long time (!)\"  prevents the example from being tested.\n\nYep, that is a bug.  I've made it. \n\n> \n> But:\n> sage -t quadratic-modules.sage\n> sage -t  quadratic-modules.sage\n> Example 13 (line 433)\n> TIMEOUT!!\n> IN:\n>  phi.level()\n>  phi = fqmodule([11,33]);\n>  phi.tau_invariant()\n>  phi = fqmodule([11,33]); # long time (!)\n>  phi.sigma_invariant()    # long time (!)\n> OUT:\n> \n> \n> This applies to sage 2.10.\n> \n> I think the reason is:\n> sage -t calls\n> sage-sage and then\n> sage-test, which in turns calls\n> sage-doctest_tex, if extension is \".sage\" instead of sage-doctest.\n> \n> At least sage-doctest looks for \"long time\" inside comment_modifiers()\n> and sage-doctest_tex doesnot.\n> \n> With best regards,\n> Lars Fischer\n\n```\n\n\nMy first thought on reading the above is \"get rid of handling .sage files in a special way in order to automatically fix all such issues\".   That's what I did with .tex files a while ago. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1866\n\n",
    "created_at": "2008-01-20T16:47:15Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in doctesting -- long time not respected in some contexts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1866",
    "user": "https://github.com/williamstein"
}
```
Assignee: failure

CC:  @orlitzky


```
On Jan 20, 2008 7:28 AM, Lars Fischer <> wrote:
> 
> Hello,
> 
> I think I have found a bug:
> chapter 2.4.1 of the Programming guide states, that comments like "#
> long time (!)"  prevents the example from being tested.

Yep, that is a bug.  I've made it. 

> 
> But:
> sage -t quadratic-modules.sage
> sage -t  quadratic-modules.sage
> Example 13 (line 433)
> TIMEOUT!!
> IN:
>  phi.level()
>  phi = fqmodule([11,33]);
>  phi.tau_invariant()
>  phi = fqmodule([11,33]); # long time (!)
>  phi.sigma_invariant()    # long time (!)
> OUT:
> 
> 
> This applies to sage 2.10.
> 
> I think the reason is:
> sage -t calls
> sage-sage and then
> sage-test, which in turns calls
> sage-doctest_tex, if extension is ".sage" instead of sage-doctest.
> 
> At least sage-doctest looks for "long time" inside comment_modifiers()
> and sage-doctest_tex doesnot.
> 
> With best regards,
> Lars Fischer

```


My first thought on reading the above is "get rid of handling .sage files in a special way in order to automatically fix all such issues".   That's what I did with .tex files a while ago. 

Issue created by migration from https://trac.sagemath.org/ticket/1866





---

archive/issue_comments_011787.json:
```json
{
    "body": "I think the issue has been fixed in Sage 3.2.x since we no longer treat .sage files special. Can you verify this?\n\nCheers,\n\nMichael",
    "created_at": "2008-12-10T07:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1866#issuecomment-11787",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I think the issue has been fixed in Sage 3.2.x since we no longer treat .sage files special. Can you verify this?

Cheers,

Michael



---

archive/issue_comments_011788.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-12-14T20:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1866#issuecomment-11788",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_011789.json:
```json
{
    "body": "This is fixed. A simple test case:\n\n\n```\n$ cat sage_extension_tests.sage \nr\"\"\"\n\nA test case for *.sage files.\n\n::\n\n    sage: 1\n    1\n\n::\n\n    sage: 2 # long time\n    2\n\n::\n\n    sage: 3\n    3\n\n\"\"\"\n```\n\n\nI see that the long test is skipped normally:\n\n\n```\n$ sage -t -verbose sage_extension_tests.sage\n...\n5 passed and 0 failed.\n```\n\n\nAnd executed when -long is passed:\n\n\n```\n$ sage -t -verbose -long sage_extension_tests.sage\n...\n6 passed and 0 failed.\n```\n",
    "created_at": "2011-12-14T20:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1866#issuecomment-11789",
    "user": "https://github.com/orlitzky"
}
```

This is fixed. A simple test case:


```
$ cat sage_extension_tests.sage 
r"""

A test case for *.sage files.

::

    sage: 1
    1

::

    sage: 2 # long time
    2

::

    sage: 3
    3

"""
```


I see that the long test is skipped normally:


```
$ sage -t -verbose sage_extension_tests.sage
...
5 passed and 0 failed.
```


And executed when -long is passed:


```
$ sage -t -verbose -long sage_extension_tests.sage
...
6 passed and 0 failed.
```




---

archive/issue_comments_011790.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2011-12-17T20:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1866#issuecomment-11790",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_002024.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2011-12-17T20:08:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1866",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1866#event-2024"
}
```
