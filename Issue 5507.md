# Issue 5507: fix sage-sage script

archive/issues_005507.json:
```json
{
    "body": "Assignee: was\n\nKeywords: sage-sage\n\nI think there is a superfluous \"shift\" in the \"sage-sage\" script, because this works:\n\n    $ sage -sh -c -c \"echo hi there\"\n\n    Starting subshell with Sage environment variables set.\n    Be sure to exit when you are done and do not do anything\n    with other copies of Sage!\n\n    Bypassing shell configuration files ...\n\n    hi there\n    Exited Sage subshell.\n\nbut this doesn't:\n\n    $ sage -sh -c \"echo hi there\"\n\n    Starting subshell with Sage environment variables set.\n    Be sure to exit when you are done and do not do anything\n    with other copies of Sage!\n\n    Bypassing shell configuration files ...\n\n    bash: echo hi there: No such file or directory\n    Exited Sage subshell.\n\n\n--\n\n$ sage --version\n| Sage Version 3.2.2, Release Date: 2008-12-18                       |\n\nIssue created by migration from https://trac.sagemath.org/ticket/5507\n\n",
    "created_at": "2009-03-13T03:04:47Z",
    "labels": [
        "user interface",
        "minor",
        "bug"
    ],
    "title": "fix sage-sage script",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5507",
    "user": "dangrayson"
}
```
Assignee: was

Keywords: sage-sage

I think there is a superfluous "shift" in the "sage-sage" script, because this works:

    $ sage -sh -c -c "echo hi there"

    Starting subshell with Sage environment variables set.
    Be sure to exit when you are done and do not do anything
    with other copies of Sage!

    Bypassing shell configuration files ...

    hi there
    Exited Sage subshell.

but this doesn't:

    $ sage -sh -c "echo hi there"

    Starting subshell with Sage environment variables set.
    Be sure to exit when you are done and do not do anything
    with other copies of Sage!

    Bypassing shell configuration files ...

    bash: echo hi there: No such file or directory
    Exited Sage subshell.


--

$ sage --version
| Sage Version 3.2.2, Release Date: 2008-12-18                       |

Issue created by migration from https://trac.sagemath.org/ticket/5507





---

archive/issue_comments_042764.json:
```json
{
    "body": "The patch at #4644 fixes this problem, according to this thread: http://groups.google.com/group/sage-devel/browse_thread/thread/384d4fe7dabb722c/",
    "created_at": "2009-09-28T23:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5507#issuecomment-42764",
    "user": "ddrake"
}
```

The patch at #4644 fixes this problem, according to this thread: http://groups.google.com/group/sage-devel/browse_thread/thread/384d4fe7dabb722c/



---

archive/issue_comments_042765.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-02T06:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5507#issuecomment-42765",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_042766.json:
```json
{
    "body": "With Sage 4.3.2.alpha1, I get:\n\n```\n[mvngu@mod sage-4.3.2.alpha1]$ ./sage -version\n* Warning: this is a prerelease version, and it may be unstable.     *\n[mvngu@mod sage-4.3.2.alpha1]$ ./sage -sh -c -c \"echo hi there\"\n| Sage Version 4.3.2.alpha1, Release Date: 2010-01-31                |\nStarting subshell with Sage environment variables set.\nBe sure to exit when you are done and do not do anything\nwith other copies of Sage!\n\nBypassing shell configuration files ...\n\nhi there\nExited Sage subshell.\n[mvngu@mod sage-4.3.2.alpha1]$ ./sage -sh -c \"echo hi there\"\n\nStarting subshell with Sage environment variables set.\nBe sure to exit when you are done and do not do anything\nwith other copies of Sage!\n\nBypassing shell configuration files ...\n\nhi there\nExited Sage subshell.\n```\n\nI'm closing this ticket as fixed by #4644.",
    "created_at": "2010-02-02T06:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5507#issuecomment-42766",
    "user": "mvngu"
}
```

With Sage 4.3.2.alpha1, I get:

```
[mvngu@mod sage-4.3.2.alpha1]$ ./sage -version
* Warning: this is a prerelease version, and it may be unstable.     *
[mvngu@mod sage-4.3.2.alpha1]$ ./sage -sh -c -c "echo hi there"
| Sage Version 4.3.2.alpha1, Release Date: 2010-01-31                |
Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

Bypassing shell configuration files ...

hi there
Exited Sage subshell.
[mvngu@mod sage-4.3.2.alpha1]$ ./sage -sh -c "echo hi there"

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

Bypassing shell configuration files ...

hi there
Exited Sage subshell.
```

I'm closing this ticket as fixed by #4644.
