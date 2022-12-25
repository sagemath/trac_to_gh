# Issue 9606: local/bin/sage-sage assumes 'sh' is bash

archive/issues_009606.json:
```json
{
    "body": "Assignee: @peterjeremy\n\nCC:  stephen\n\n\"sage -sh\" is intended to start a subshell of the user's preference (as per $SHELL) with the local Sage environment configured in it.\n\nIn order to prevent the environment being altered by the user's shell RC scripts, local/bin/sage-sage passes an argument to $SHELL which is intended to disable RC processing.  Unfortunately, it assumes that 'sh' is 'bash' and passes '--norc' - which is not legal for POSIX shells.\n\nWhilst this appears to be ignored by Solaris /bin/sh and /usr/xpg4/bin/sh (which is at variance to the man page), it is rejected by FreeBSD /bin/sh - which reports \"Illegal option --\".\n\nThe fix is not clear because Cygwin, Linux and OpenSolaris (at least) all install bash as /bin/sh - though experiments show that at least bash-4.1.7 will not run any RC script when invoked as sh.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9606\n\n",
    "closed_at": "2013-01-17T10:03:30Z",
    "created_at": "2010-07-26T23:42:53Z",
    "labels": [
        "component: porting: bsd",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "local/bin/sage-sage assumes 'sh' is bash",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9606",
    "user": "https://github.com/peterjeremy"
}
```
Assignee: @peterjeremy

CC:  stephen

"sage -sh" is intended to start a subshell of the user's preference (as per $SHELL) with the local Sage environment configured in it.

In order to prevent the environment being altered by the user's shell RC scripts, local/bin/sage-sage passes an argument to $SHELL which is intended to disable RC processing.  Unfortunately, it assumes that 'sh' is 'bash' and passes '--norc' - which is not legal for POSIX shells.

Whilst this appears to be ignored by Solaris /bin/sh and /usr/xpg4/bin/sh (which is at variance to the man page), it is rejected by FreeBSD /bin/sh - which reports "Illegal option --".

The fix is not clear because Cygwin, Linux and OpenSolaris (at least) all install bash as /bin/sh - though experiments show that at least bash-4.1.7 will not run any RC script when invoked as sh.

Issue created by migration from https://trac.sagemath.org/ticket/9606





---

archive/issue_comments_092896.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2012-04-19T21:06:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9606#issuecomment-92896",
    "user": "https://github.com/nexttime"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_092897.json:
```json
{
    "body": "Is this still an issue?\n\n(The script btw. has meanwhile been renamed / moved to `$SAGE_ROOT/spkg/bin/sage`.)",
    "created_at": "2012-04-19T21:06:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9606#issuecomment-92897",
    "user": "https://github.com/nexttime"
}
```

Is this still an issue?

(The script btw. has meanwhile been renamed / moved to `$SAGE_ROOT/spkg/bin/sage`.)



---

archive/issue_comments_092898.json:
```json
{
    "body": "The relevant part of the script says\n\n```sh\n        sh)\n            # We don't really know which shell \"sh\" is (it could be\n            # bash, but this is not guaranteed), so we don't set\n            # SHELL_OPTS.\n            if [ \"$color_prompt\" = yes ] ; then\n                PS1=\"$(tput rev)(sage-sh)$(tput sgr0) $USER@`hostname -s`:\\${PWD##*/}$ \"\n            else\n                PS1=\"(sage-sh) $USER@`hostname -s`:\\${PWD}$ \"\n            fi\n            export PS1\n            ;;\n```\nSo it doesn't look like this ticket is relevant any more.",
    "created_at": "2012-04-19T23:03:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9606#issuecomment-92898",
    "user": "https://github.com/jhpalmieri"
}
```

The relevant part of the script says

```sh
        sh)
            # We don't really know which shell "sh" is (it could be
            # bash, but this is not guaranteed), so we don't set
            # SHELL_OPTS.
            if [ "$color_prompt" = yes ] ; then
                PS1="$(tput rev)(sage-sh)$(tput sgr0) $USER@`hostname -s`:\${PWD##*/}$ "
            else
                PS1="(sage-sh) $USER@`hostname -s`:\${PWD}$ "
            fi
            export PS1
            ;;
```
So it doesn't look like this ticket is relevant any more.



---

archive/issue_comments_092899.json:
```json
{
    "body": "`@`Stephen M-S:  If you have time, can you check that `./sage -sh` works from `SAGE_ROOT`?   That would confirm what John and Leif point out here - but it would be nice to have it actually tested, since stranger things have happened.",
    "created_at": "2013-01-16T01:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9606#issuecomment-92899",
    "user": "https://github.com/kcrisman"
}
```

`@`Stephen M-S:  If you have time, can you check that `./sage -sh` works from `SAGE_ROOT`?   That would confirm what John and Leif point out here - but it would be nice to have it actually tested, since stranger things have happened.



---

archive/issue_comments_092900.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2013-01-16T01:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9606#issuecomment-92900",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_events_023937.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2013-01-16T01:21:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9606",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9606#event-23937"
}
```



---

archive/issue_comments_092901.json:
```json
{
    "body": "I can confirm that ./sage -sh works from SAGE_ROOT, even when SHELL=/bin/sh.",
    "created_at": "2013-01-16T02:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9606#issuecomment-92901",
    "user": "https://trac.sagemath.org/admin/accounts/users/stephen"
}
```

I can confirm that ./sage -sh works from SAGE_ROOT, even when SHELL=/bin/sh.



---

archive/issue_comments_092902.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-16T02:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9606#issuecomment-92902",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092903.json:
```json
{
    "body": "Great, thank you!",
    "created_at": "2013-01-16T02:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9606#issuecomment-92903",
    "user": "https://github.com/kcrisman"
}
```

Great, thank you!



---

archive/issue_events_023938.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-17T10:03:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9606",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9606#event-23938"
}
```



---

archive/issue_comments_092904.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-01-17T10:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9606#issuecomment-92904",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
