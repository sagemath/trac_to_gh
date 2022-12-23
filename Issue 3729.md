# Issue 3729: [with patch; needs review] Only overwrite RHOME environment variable when it is unset

archive/issues_003729.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen using my Debian Sage package, \"import rpy\" fails because Sage is overwriting the RHOME environment variable.  I could install a symlink to the right place in $SAGE_LOCAL/lib/R, but I think it's cleaner for Sage to only replace RHOME if it isn't already set (and then the Debian Sage wrapper script would set it correctly).  I've attached a patch to do this.\n\nThere are several uncommitted changes in spkg/base/sage-env, so my patch is a normal patch (rather than an hg one).\n\nIssue created by migration from https://trac.sagemath.org/ticket/3729\n\n",
    "created_at": "2008-07-26T17:28:35Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] Only overwrite RHOME environment variable when it is unset",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3729",
    "user": "tabbott"
}
```
Assignee: mabshoff

When using my Debian Sage package, "import rpy" fails because Sage is overwriting the RHOME environment variable.  I could install a symlink to the right place in $SAGE_LOCAL/lib/R, but I think it's cleaner for Sage to only replace RHOME if it isn't already set (and then the Debian Sage wrapper script would set it correctly).  I've attached a patch to do this.

There are several uncommitted changes in spkg/base/sage-env, so my patch is a normal patch (rather than an hg one).

Issue created by migration from https://trac.sagemath.org/ticket/3729





---

archive/issue_comments_026476.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-26T17:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3729#issuecomment-26476",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_026477.json:
```json
{
    "body": "Hi Tim,\n\nthis patch is problematic and I would prefer if you carried it in a Debian specific patch. We did begin setting RHOME since certain distributions like Gentoo set it when R was installed in the system. Then that R would be run which leads to problems, so setting it conditionally will reintroduce the same issues.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-27T01:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3729#issuecomment-26477",
    "user": "mabshoff"
}
```

Hi Tim,

this patch is problematic and I would prefer if you carried it in a Debian specific patch. We did begin setting RHOME since certain distributions like Gentoo set it when R was installed in the system. Then that R would be run which leads to problems, so setting it conditionally will reintroduce the same issues.

Cheers,

Michael



---

archive/issue_comments_026478.json:
```json
{
    "body": "How about we change it to test whether an environment variable with a different name is set, e.g.\n\nif [ -z \"$SAGE_USE_SYSTEM_RHOME\" ];\n     RHOME=\"SAGE_LOCAL\"/local/lib/R && export RHOME\nfi\n\nThis I think should be pretty unlikely to bring those issues back, but still gives packagers a hook to set RHOME themselves.",
    "created_at": "2008-07-27T01:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3729#issuecomment-26478",
    "user": "tabbott"
}
```

How about we change it to test whether an environment variable with a different name is set, e.g.

if [ -z "$SAGE_USE_SYSTEM_RHOME" ];
     RHOME="SAGE_LOCAL"/local/lib/R && export RHOME
fi

This I think should be pretty unlikely to bring those issues back, but still gives packagers a hook to set RHOME themselves.



---

archive/issue_comments_026479.json:
```json
{
    "body": "Hi Tim,\n\nReplying to [comment:2 tabbott]:\n> How about we change it to test whether an environment variable with a different name is set, e.g.\n> \n> if [ -z \"$SAGE_USE_SYSTEM_RHOME\" ];\n>      RHOME=\"SAGE_LOCAL\"/local/lib/R && export RHOME\n> fi\n> \n> This I think should be pretty unlikely to bring those issues back, but still gives packagers a hook to set RHOME themselves.\n\nWell, the problem I see here is that this way we have to set it in Sage somewhere before sourcing sage-env. We could do it in the sage script itself, but that is meant to do only the minimal number of things to get running and then sage-env deals with the environment. What I would prefer is something the other way around, i.e. distributions wishing to use the installed \"system\" set something in env that sage-env tests for and if SAGE_USE_SYSTEM_RHOME equaled \"no\" we would not set RHOME.\n\nThoughts\"\n\nCheers,\n\nMichael",
    "created_at": "2008-07-27T11:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3729#issuecomment-26479",
    "user": "mabshoff"
}
```

Hi Tim,

Replying to [comment:2 tabbott]:
> How about we change it to test whether an environment variable with a different name is set, e.g.
> 
> if [ -z "$SAGE_USE_SYSTEM_RHOME" ];
>      RHOME="SAGE_LOCAL"/local/lib/R && export RHOME
> fi
> 
> This I think should be pretty unlikely to bring those issues back, but still gives packagers a hook to set RHOME themselves.

Well, the problem I see here is that this way we have to set it in Sage somewhere before sourcing sage-env. We could do it in the sage script itself, but that is meant to do only the minimal number of things to get running and then sage-env deals with the environment. What I would prefer is something the other way around, i.e. distributions wishing to use the installed "system" set something in env that sage-env tests for and if SAGE_USE_SYSTEM_RHOME equaled "no" we would not set RHOME.

Thoughts"

Cheers,

Michael



---

archive/issue_comments_026480.json:
```json
{
    "body": "I think the code snippet I offered has the semantics you describe (the code will set RHOME if and only if SAGE_USE_SYSTEM_RHOME is not set, and distributions would set it to \"yes\" to cause Sage to not change RHOME).  Maybe the variable needs a clearer name, like SAGE_DONT_SET_RHOME, but by \"system rhome\" I meant that Sage should not it, and that's what the code does.",
    "created_at": "2008-07-27T17:40:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3729#issuecomment-26480",
    "user": "tabbott"
}
```

I think the code snippet I offered has the semantics you describe (the code will set RHOME if and only if SAGE_USE_SYSTEM_RHOME is not set, and distributions would set it to "yes" to cause Sage to not change RHOME).  Maybe the variable needs a clearer name, like SAGE_DONT_SET_RHOME, but by "system rhome" I meant that Sage should not it, and that's what the code does.



---

archive/issue_comments_026481.json:
```json
{
    "body": "Yes, I was not as awake as I should have been when I reviewed the patch. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-31T00:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3729#issuecomment-26481",
    "user": "mabshoff"
}
```

Yes, I was not as awake as I should have been when I reviewed the patch. Positive review.

Cheers,

Michael



---

archive/issue_comments_026482.json:
```json
{
    "body": "Merged in Sage 3.1.alpha0",
    "created_at": "2008-07-31T00:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3729#issuecomment-26482",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha0



---

archive/issue_comments_026483.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-31T00:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3729#issuecomment-26483",
    "user": "mabshoff"
}
```

Resolution: fixed
