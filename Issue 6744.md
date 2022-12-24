# Issue 6744: [with patch, needs review] install script stores start time of build

archive/issues_006744.json:
```json
{
    "body": "Assignee: tbd\n\nIn order to track the build progress, it is necessary to store the start time of the build process. (elapsed time, estimate of remaining time, ...) \n\nThis patch inserts a line in \"install\" which stores the seconds since 1970-1-1 in a hidden file `.BUILDSTART` in `%SAGE_ROOT` when the build process starts. This could also be useful for other applications. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6744\n\n",
    "created_at": "2009-08-14T09:58:17Z",
    "labels": [
        "distribution",
        "trivial",
        "enhancement"
    ],
    "title": "[with patch, needs review] install script stores start time of build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6744",
    "user": "schilly"
}
```
Assignee: tbd

In order to track the build progress, it is necessary to store the start time of the build process. (elapsed time, estimate of remaining time, ...) 

This patch inserts a line in "install" which stores the seconds since 1970-1-1 in a hidden file `.BUILDSTART` in `%SAGE_ROOT` when the build process starts. This could also be useful for other applications. 

Issue created by migration from https://trac.sagemath.org/ticket/6744





---

archive/issue_comments_055487.json:
```json
{
    "body": "Attachment [install_script_stores_start_time.patch](tarball://root/attachments/some-uuid/ticket6744/install_script_stores_start_time.patch) by schilly created at 2009-08-14 10:01:08",
    "created_at": "2009-08-14T10:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6744#issuecomment-55487",
    "user": "schilly"
}
```

Attachment [install_script_stores_start_time.patch](tarball://root/attachments/some-uuid/ticket6744/install_script_stores_start_time.patch) by schilly created at 2009-08-14 10:01:08



---

archive/issue_comments_055488.json:
```json
{
    "body": "The patch should be applied against the file `SAGE_ROOT/spkg/install`. That file is not under revision control, so one has to manually apply the patch.",
    "created_at": "2009-08-14T10:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6744#issuecomment-55488",
    "user": "mvngu"
}
```

The patch should be applied against the file `SAGE_ROOT/spkg/install`. That file is not under revision control, so one has to manually apply the patch.



---

archive/issue_comments_055489.json:
```json
{
    "body": "note: don't forget to update this file on the master-mirror, too! it lives in `sage`@`sagemath:~/www-files/packages/install`",
    "created_at": "2009-08-14T10:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6744#issuecomment-55489",
    "user": "schilly"
}
```

note: don't forget to update this file on the master-mirror, too! it lives in `sage`@`sagemath:~/www-files/packages/install`



---

archive/issue_comments_055490.json:
```json
{
    "body": "I don't see how this can hurt anything. Tried building anyways, no problem.",
    "created_at": "2009-08-30T18:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6744#issuecomment-55490",
    "user": "timdumol"
}
```

I don't see how this can hurt anything. Tried building anyways, no problem.



---

archive/issue_comments_055491.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-31T08:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6744#issuecomment-55491",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_055492.json:
```json
{
    "body": "Although this is marked as fixed, it should be noted that it makes use of a non-portable option to the `date` command so fails on some systems. See \n\nhttp://www.opengroup.org/onlinepubs/009695399/utilities/date.html\n\nfor a list of portable options. \n\nSince the file created is not actually used by anything it's not a big problem, but if anyone tried using it on a Unix system, it would likely fail. A better method is:\n\n\n```\n# Compute seconds since the Epoch.\n\n# Call 'date'. Note that\n# %Y = year including century\n# %j = day number (1-365)\n# %H = hour (0-23)\n# %M = minute (0-59)\n# %S = seconds (0-59)\n\nif type env >/dev/null 2>&1 ; then\n    set -- `env LC_ALL=C LC_TIME=C LANG=C date -u '+%Y %j %H %M %S'`\nelse\n    set -- `date -u '+%Y %j %H %M %S'`\nfi\n\n# $1 = year including century\n# $2 = day number (1-365)\n# $3 = hour (0-23)\n# $4 = minute (0-59)\n# $5 = seconds (0-59)\n\nif [ $? -ne 0 ] || [ $# -lt 5 ] ; then\n  TIME=\"Error computing seconds since the Epoch\"\nfi\n\nDAYS=`expr 365 \\* \\( $1 - 1970 \\) + \\( $1 - 1969 \\) / 4 + $2 - 1`\nTIME=`expr $5 + 60 \\* \\( $4 + 60 \\* \\( $3 + 24 \\* $DAYS \\) \\)`\necho $TIME\n```\n",
    "created_at": "2010-09-30T06:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6744#issuecomment-55492",
    "user": "drkirkby"
}
```

Although this is marked as fixed, it should be noted that it makes use of a non-portable option to the `date` command so fails on some systems. See 

http://www.opengroup.org/onlinepubs/009695399/utilities/date.html

for a list of portable options. 

Since the file created is not actually used by anything it's not a big problem, but if anyone tried using it on a Unix system, it would likely fail. A better method is:


```
# Compute seconds since the Epoch.

# Call 'date'. Note that
# %Y = year including century
# %j = day number (1-365)
# %H = hour (0-23)
# %M = minute (0-59)
# %S = seconds (0-59)

if type env >/dev/null 2>&1 ; then
    set -- `env LC_ALL=C LC_TIME=C LANG=C date -u '+%Y %j %H %M %S'`
else
    set -- `date -u '+%Y %j %H %M %S'`
fi

# $1 = year including century
# $2 = day number (1-365)
# $3 = hour (0-23)
# $4 = minute (0-59)
# $5 = seconds (0-59)

if [ $? -ne 0 ] || [ $# -lt 5 ] ; then
  TIME="Error computing seconds since the Epoch"
fi

DAYS=`expr 365 \* \( $1 - 1970 \) + \( $1 - 1969 \) / 4 + $2 - 1`
TIME=`expr $5 + 60 \* \( $4 + 60 \* \( $3 + 24 \* $DAYS \) \)`
echo $TIME
```

