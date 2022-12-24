# Issue 6146: [with patch, needs review] the detection of SAGE_ROOT in $SAGE_ROOT/sage script should expand symlinks recursively (fix this on systems that do *NOT* support readlink -f)

archive/issues_006146.json:
```json
{
    "body": "Assignee: cwitty\n\nSee #5852.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6146\n\n",
    "created_at": "2009-05-28T07:00:10Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] the detection of SAGE_ROOT in $SAGE_ROOT/sage script should expand symlinks recursively (fix this on systems that do *NOT* support readlink -f)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6146",
    "user": "was"
}
```
Assignee: cwitty

See #5852.

Issue created by migration from https://trac.sagemath.org/ticket/6146





---

archive/issue_comments_049060.json:
```json
{
    "body": "test implementation of realpath in bash for systems which don't support realpath/readlink -f",
    "created_at": "2009-07-02T00:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6146#issuecomment-49060",
    "user": "tornaria"
}
```

test implementation of realpath in bash for systems which don't support realpath/readlink -f



---

archive/issue_comments_049061.json:
```json
{
    "body": "Attachment [sage-realpath-test.tar.gz](tarball://root/attachments/some-uuid/ticket6146/sage-realpath-test.tar.gz) by tornaria created at 2009-07-02 00:09:49\n\nI've attached a proof-of-concept of a bash script which correctly computes the SAGE_ROOT as a fully canonicalized path. This is a tarball which includes the script itself, and a bunch of symlinks to the same script in different configurations, plus a test script which shows the result of the computation of SAGE_ROOT in the different cases.\n\nTo test, untar, `cd sage-realpath-test` and run `./test`. Sample output:\n\n```\n==========================================================\nThe following lines of output should all be identical, and\npoint to the canonicalized path of directory sage_root\n==========================================================\n\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\nSAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:\n```\n\nThis is a correct run, because all the runs gave the same canonical path (which is the correct canonical path).\n\nThe script uses `realpath`, then `readlink -f`, and fall back to a bash function; but for testing purposes, the fallback to bash function is always tried.\n\nI've successfully tested this on:\n- linux with no realpath, but readlink -f works (my laptop)\n- linux with realpath (sage.math)\n- mac with fink (which supports readlink -f)\n- mac with fink disabled (remove it from path)\n- t2 (trying this found out some gnuisms or non-sunisms which I had to fix)\n\nMaybe somebody can try this on the build farm to check that it is safe... Assuming what we really want is for SAGE_ROOT to be the fully canonicalized path (see the last comments in #5852).\n\nBTW, this already gives an absolute path, so there would be no need to `cd $SAGE_ROOT` here and `cd $CUR` back in sage-sage (ugly hack).",
    "created_at": "2009-07-02T00:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6146#issuecomment-49061",
    "user": "tornaria"
}
```

Attachment [sage-realpath-test.tar.gz](tarball://root/attachments/some-uuid/ticket6146/sage-realpath-test.tar.gz) by tornaria created at 2009-07-02 00:09:49

I've attached a proof-of-concept of a bash script which correctly computes the SAGE_ROOT as a fully canonicalized path. This is a tarball which includes the script itself, and a bunch of symlinks to the same script in different configurations, plus a test script which shows the result of the computation of SAGE_ROOT in the different cases.

To test, untar, `cd sage-realpath-test` and run `./test`. Sample output:

```
==========================================================
The following lines of output should all be identical, and
point to the canonicalized path of directory sage_root
==========================================================

SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
```

This is a correct run, because all the runs gave the same canonical path (which is the correct canonical path).

The script uses `realpath`, then `readlink -f`, and fall back to a bash function; but for testing purposes, the fallback to bash function is always tried.

I've successfully tested this on:
- linux with no realpath, but readlink -f works (my laptop)
- linux with realpath (sage.math)
- mac with fink (which supports readlink -f)
- mac with fink disabled (remove it from path)
- t2 (trying this found out some gnuisms or non-sunisms which I had to fix)

Maybe somebody can try this on the build farm to check that it is safe... Assuming what we really want is for SAGE_ROOT to be the fully canonicalized path (see the last comments in #5852).

BTW, this already gives an absolute path, so there would be no need to `cd $SAGE_ROOT` here and `cd $CUR` back in sage-sage (ugly hack).



---

archive/issue_comments_049062.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-19T18:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6146#issuecomment-49062",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_049063.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-05T16:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6146#issuecomment-49063",
    "user": "malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_049064.json:
```json
{
    "body": "This isn't a patch etc. so it cannot be reviewed yet. I'll change the status to `needs work`.",
    "created_at": "2010-04-05T16:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6146#issuecomment-49064",
    "user": "malb"
}
```

This isn't a patch etc. so it cannot be reviewed yet. I'll change the status to `needs work`.



---

archive/issue_comments_049065.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-08-18T21:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6146#issuecomment-49065",
    "user": "jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_comments_049066.json:
```json
{
    "body": "Replying to [comment:5 jdemeyer]:\n- resolution set to duplicate\n\nDuplicate of which ticket?\n\nFor convenience, here's a copy of the path-detection code in the tarball above. The tarball also contains a number of tests for different cases of symlinks in-the-path or in-the-script.\n\n\n```/usr/bin/env bash\n\nrealpath_bash()\n{\n    fname=\"${1%/}\" # strips trailing '/'\n    while [ -L \"$fname\" ] ; do\n        dir=\"$(dirname \"$fname\")\"\n        fname=\"$(command ls -l \"$fname\")\"\n        fname=\"${fname#*\\> }\"\n        if [ \"$fname\" = \".\" ] ; then\n            fname=\"$dir\"\n        elif echo \"$fname\" | grep -v '^/' > /dev/null ; then\n            fname=\"$dir/$fname\"\n        fi\n    done\n    pushd \"$(dirname \"$fname\")\" > /dev/null\n    echo \"$(pwd -P)/$(basename \"$fname\")\"\n    popd > /dev/null\n}\n\nSAGE_PATH=\"$(realpath \"$0\" 2> /dev/null)\" || \\\nSAGE_PATH=\"$(readlink -f \"$0\" 2> /dev/null)\" || \\\nSAGE_PATH=\"$(realpath_bash \"$0\" 2> /dev/null)\" || \\\nSAGE_PATH=\"$0\"\n\nSAGE_ROOT=\"$(dirname \"$SAGE_PATH\")\"\n\necho \"SAGE_ROOT:$SAGE_ROOT:\"\n```\n\n\nPlease see also the discussion in #5852, which is concerned with canonicalizing $SAGE_ROOT when readlink -f is available --- a fix that works for that case was merged in 4.0.rc1 and reverted in 4.1.rc0 because it caused a regression for somebody.\n\nThis ticket is concerned with how to portably canonicalize $SAGE_ROOT in general (when readlink -f is not available) and it was stalled because canonicalization (as done in #5852) caused other issues that weren't resolved. Once using a fully canonical $SAGE_ROOT is workable (using readlink -f) then we can expand the portability of the canonicalization using the solution proposed here (or any other solution).\n\n[see also #11707]",
    "created_at": "2011-08-19T01:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6146#issuecomment-49066",
    "user": "tornaria"
}
```

Replying to [comment:5 jdemeyer]:
- resolution set to duplicate

Duplicate of which ticket?

For convenience, here's a copy of the path-detection code in the tarball above. The tarball also contains a number of tests for different cases of symlinks in-the-path or in-the-script.


```/usr/bin/env bash

realpath_bash()
{
    fname="${1%/}" # strips trailing '/'
    while [ -L "$fname" ] ; do
        dir="$(dirname "$fname")"
        fname="$(command ls -l "$fname")"
        fname="${fname#*\> }"
        if [ "$fname" = "." ] ; then
            fname="$dir"
        elif echo "$fname" | grep -v '^/' > /dev/null ; then
            fname="$dir/$fname"
        fi
    done
    pushd "$(dirname "$fname")" > /dev/null
    echo "$(pwd -P)/$(basename "$fname")"
    popd > /dev/null
}

SAGE_PATH="$(realpath "$0" 2> /dev/null)" || \
SAGE_PATH="$(readlink -f "$0" 2> /dev/null)" || \
SAGE_PATH="$(realpath_bash "$0" 2> /dev/null)" || \
SAGE_PATH="$0"

SAGE_ROOT="$(dirname "$SAGE_PATH")"

echo "SAGE_ROOT:$SAGE_ROOT:"
```


Please see also the discussion in #5852, which is concerned with canonicalizing $SAGE_ROOT when readlink -f is available --- a fix that works for that case was merged in 4.0.rc1 and reverted in 4.1.rc0 because it caused a regression for somebody.

This ticket is concerned with how to portably canonicalize $SAGE_ROOT in general (when readlink -f is not available) and it was stalled because canonicalization (as done in #5852) caused other issues that weren't resolved. Once using a fully canonical $SAGE_ROOT is workable (using readlink -f) then we can expand the portability of the canonicalization using the solution proposed here (or any other solution).

[see also #11707]
