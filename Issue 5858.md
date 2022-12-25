# Issue 5858: Octave library linking problems

archive/issues_005858.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: octave, library linking\n\nEmail from sage-support describes the problem and Michael Abshoff's comments about what needs to be done:\n\nOn Apr 22, 12:46 am, Ajay Rawat <ajay.rawa...`@`gmail.com> wrote:\n\n> Well i tried the command\n> sage:octave_version()\n> sage:3.0.0\n> but when i tried octave_console\n> it replied...................\n\n> octave:\n> /usr/local/sage-3.2.3-Ubuntu8.04LTS-64bit-Intel-x86_64-Linux/local/lib/l\\\n> ibz.so.1: no version information available (required by\n> /usr/lib/octave-3.0.0/liboctinterp.so)\n\nThe problem is that the libz shipped by Sage and the one used by the\nsystem (and which was linked by Octave) do not play nicely together.\n\nTo work around this write a script called octave (I assume that is the\nname of the octave start script/binary\n\n#!/bin/sh\nLD_LIBRARY_PATH=SAGE_ORIG_LD_LIBRARY_PATH; export LD_LIBRARY_PATH\nexec octave \"$`@`\"\n\nI didn't try this, so you might need to adjust something.\n\nTo fix this once and for all in sage we should use native execute -\nwould someone open a ticket since I am about to go offline for the\nnight :)\n\nCheers,\n\nMichael \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5858\n\n",
    "created_at": "2009-04-22T17:57:18Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Octave library linking problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5858",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: @williamstein

Keywords: octave, library linking

Email from sage-support describes the problem and Michael Abshoff's comments about what needs to be done:

On Apr 22, 12:46 am, Ajay Rawat <ajay.rawa...`@`gmail.com> wrote:

> Well i tried the command
> sage:octave_version()
> sage:3.0.0
> but when i tried octave_console
> it replied...................

> octave:
> /usr/local/sage-3.2.3-Ubuntu8.04LTS-64bit-Intel-x86_64-Linux/local/lib/l\
> ibz.so.1: no version information available (required by
> /usr/lib/octave-3.0.0/liboctinterp.so)

The problem is that the libz shipped by Sage and the one used by the
system (and which was linked by Octave) do not play nicely together.

To work around this write a script called octave (I assume that is the
name of the octave start script/binary

#!/bin/sh
LD_LIBRARY_PATH=SAGE_ORIG_LD_LIBRARY_PATH; export LD_LIBRARY_PATH
exec octave "$`@`"

I didn't try this, so you might need to adjust something.

To fix this once and for all in sage we should use native execute -
would someone open a ticket since I am about to go offline for the
night :)

Cheers,

Michael 


Issue created by migration from https://trac.sagemath.org/ticket/5858





---

archive/issue_comments_046197.json:
```json
{
    "body": "Patch",
    "created_at": "2009-09-11T04:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5858#issuecomment-46197",
    "user": "https://trac.sagemath.org/admin/accounts/users/jjh"
}
```

Patch



---

archive/issue_comments_046198.json:
```json
{
    "body": "Attachment [octave-native-execute.patch](tarball://root/attachments/some-uuid/ticket5858/octave-native-execute.patch) by jjh created at 2009-09-11 04:46:47",
    "created_at": "2009-09-11T04:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5858#issuecomment-46198",
    "user": "https://trac.sagemath.org/admin/accounts/users/jjh"
}
```

Attachment [octave-native-execute.patch](tarball://root/attachments/some-uuid/ticket5858/octave-native-execute.patch) by jjh created at 2009-09-11 04:46:47



---

archive/issue_comments_046199.json:
```json
{
    "body": "This seems to fix the problem. Octave passes all doctests on my machine.",
    "created_at": "2009-09-11T04:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5858#issuecomment-46199",
    "user": "https://trac.sagemath.org/admin/accounts/users/jjh"
}
```

This seems to fix the problem. Octave passes all doctests on my machine.



---

archive/issue_comments_046200.json:
```json
{
    "body": "The fix looks right, applies to my tree, and -optional doctests pass.",
    "created_at": "2009-09-15T04:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5858#issuecomment-46200",
    "user": "https://github.com/jasongrout"
}
```

The fix looks right, applies to my tree, and -optional doctests pass.



---

archive/issue_comments_046201.json:
```json
{
    "body": "(-optional on octave.py, that is).",
    "created_at": "2009-09-15T04:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5858#issuecomment-46201",
    "user": "https://github.com/jasongrout"
}
```

(-optional on octave.py, that is).



---

archive/issue_events_006114.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-15T23:28:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5858",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5858#event-6114"
}
```



---

archive/issue_comments_046202.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-15T23:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5858#issuecomment-46202",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
