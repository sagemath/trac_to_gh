# Issue 9528: #8306 completely breaks "sage -upgrade"

archive/issues_009528.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nIf you have any version of sage < version 4.5, and you try to upgrade to sage-4.5, the addition of a file pipestatus in #8306 means that your upgrade will instantly and totally break.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9528\n\n",
    "created_at": "2010-07-17T12:24:55Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.1",
    "title": "#8306 completely breaks \"sage -upgrade\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9528",
    "user": "was"
}
```
Assignee: GeorgSWeber

If you have any version of sage < version 4.5, and you try to upgrade to sage-4.5, the addition of a file pipestatus in #8306 means that your upgrade will instantly and totally break.

Issue created by migration from https://trac.sagemath.org/ticket/9528





---

archive/issue_comments_091655.json:
```json
{
    "body": "My first idea to fix this is to modify the script `spkg/install`, which *does* get updated on \"sage -upgrade\" so that it checks for the file pipestatus, and if it isn't there, then it downloads it. \n\nUnfortunately, `install` is a shell script, not a python script, so grabbing a file is harder.  But it could call python.\n\nThis is going to be a little ugly though.",
    "created_at": "2010-07-17T12:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91655",
    "user": "was"
}
```

My first idea to fix this is to modify the script `spkg/install`, which *does* get updated on "sage -upgrade" so that it checks for the file pipestatus, and if it isn't there, then it downloads it. 

Unfortunately, `install` is a shell script, not a python script, so grabbing a file is harder.  But it could call python.

This is going to be a little ugly though.



---

archive/issue_comments_091656.json:
```json
{
    "body": "Or just **create** `pipestatus` in `spkg-install`; it's an almost trivial script, unlikely to change, and we can check for the bash version number **once** inside `spkg-install` and write only the appropriate branch to `pipestatus`.",
    "created_at": "2010-07-17T12:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91656",
    "user": "leif"
}
```

Or just **create** `pipestatus` in `spkg-install`; it's an almost trivial script, unlikely to change, and we can check for the bash version number **once** inside `spkg-install` and write only the appropriate branch to `pipestatus`.



---

archive/issue_comments_091657.json:
```json
{
    "body": "The only reason for `pipestatus` was that we did not want to rely on bash version >=3.0.",
    "created_at": "2010-07-17T12:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91657",
    "user": "leif"
}
```

The only reason for `pipestatus` was that we did not want to rely on bash version >=3.0.



---

archive/issue_comments_091658.json:
```json
{
    "body": "Replying to [comment:2 leif]:\n> Or just **create** `pipestatus` in `spkg-install`; \n\nThis will not work.   The problem is that spkg-install isn't run until after pipestatus is needed. \n\n> it's an almost trivial script,\n\nI disagree -- It's 33 lines long, and  I read it for 2 minutes and didn't fully understand it.",
    "created_at": "2010-07-17T13:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91658",
    "user": "was"
}
```

Replying to [comment:2 leif]:
> Or just **create** `pipestatus` in `spkg-install`; 

This will not work.   The problem is that spkg-install isn't run until after pipestatus is needed. 

> it's an almost trivial script,

I disagree -- It's 33 lines long, and  I read it for 2 minutes and didn't fully understand it.



---

archive/issue_comments_091659.json:
```json
{
    "body": "Attachment [create-pipestatus.sh](tarball://root/attachments/some-uuid/ticket9528/create-pipestatus.sh) by leif created at 2010-07-17 13:56:28\n\nBash script to create specific version of \"pipestatus\" in $SAGE_ROOT/spkg",
    "created_at": "2010-07-17T13:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91659",
    "user": "leif"
}
```

Attachment [create-pipestatus.sh](tarball://root/attachments/some-uuid/ticket9528/create-pipestatus.sh) by leif created at 2010-07-17 13:56:28

Bash script to create specific version of "pipestatus" in $SAGE_ROOT/spkg



---

archive/issue_comments_091660.json:
```json
{
    "body": "William, perhaps you can paste the attached shell script (i.e. part of it, removing the first line) into some other script that is run at the right moment in the upgrade process.\n\n(The \"harder\" part of `pipestatus` is obviously non-trivial to understand, therefore it contains a reference to its explanation, [shortcut](http://www.unix.com/302265010-post3.html). It's actually suited for *many* Bourne shells, not just bash <3.0.)",
    "created_at": "2010-07-17T14:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91660",
    "user": "leif"
}
```

William, perhaps you can paste the attached shell script (i.e. part of it, removing the first line) into some other script that is run at the right moment in the upgrade process.

(The "harder" part of `pipestatus` is obviously non-trivial to understand, therefore it contains a reference to its explanation, [shortcut](http://www.unix.com/302265010-post3.html). It's actually suited for *many* Bourne shells, not just bash <3.0.)



---

archive/issue_comments_091661.json:
```json
{
    "body": "Lief -- many thanks for posting this, which I *greatly* appreciate.",
    "created_at": "2010-07-17T14:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91661",
    "user": "was"
}
```

Lief -- many thanks for posting this, which I *greatly* appreciate.



---

archive/issue_comments_091662.json:
```json
{
    "body": "Btw, you can drop the parentheses in the >=3.0 version, since we don't have to set `pipefail` in a subshell (it's a stand-alone script).",
    "created_at": "2010-07-17T14:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91662",
    "user": "leif"
}
```

Btw, you can drop the parentheses in the >=3.0 version, since we don't have to set `pipefail` in a subshell (it's a stand-alone script).



---

archive/issue_comments_091663.json:
```json
{
    "body": "And `pipestatus`'s\n\n```sh\nif [ -z \"$1\" ]; then\n  # usage error ...\n```\n\nshould be\n\n```sh\nif [ $# -ne 2 ]; then\n  # usage error ...\n```\n",
    "created_at": "2010-07-17T14:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91663",
    "user": "leif"
}
```

And `pipestatus`'s

```sh
if [ -z "$1" ]; then
  # usage error ...
```

should be

```sh
if [ $# -ne 2 ]; then
  # usage error ...
```




---

archive/issue_comments_091664.json:
```json
{
    "body": "Attachment [install](tarball://root/attachments/some-uuid/ticket9528/install) by was created at 2010-07-17 14:59:10\n\nthis should be put as SAGE_ROOT/spkg/install",
    "created_at": "2010-07-17T14:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91664",
    "user": "was"
}
```

Attachment [install](tarball://root/attachments/some-uuid/ticket9528/install) by was created at 2010-07-17 14:59:10

this should be put as SAGE_ROOT/spkg/install



---

archive/issue_comments_091665.json:
```json
{
    "body": "Attachment [create-pipestatus-v2.sh](tarball://root/attachments/some-uuid/ticket9528/create-pipestatus-v2.sh) by leif created at 2010-07-17 15:00:40\n\nCreates a slightly improved version of pipestatus, no changes to the script code itself",
    "created_at": "2010-07-17T15:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91665",
    "user": "leif"
}
```

Attachment [create-pipestatus-v2.sh](tarball://root/attachments/some-uuid/ticket9528/create-pipestatus-v2.sh) by leif created at 2010-07-17 15:00:40

Creates a slightly improved version of pipestatus, no changes to the script code itself



---

archive/issue_comments_091666.json:
```json
{
    "body": "Hi,\n\nI rewrote a script based on your idea (but not using your code).  I tested it by:\n\n (1) taking sage-4.5 and move spkg/pipestatus to spkg/pipestatus.orig\n (2) typed \"make\", then control-c in a few seconds\n (3) Do diff spkg/pipestatus spkg/pipestatus.orig and observe that the diff is just a single blank line.\n\nPlease review.  Since spkg/install is pulled in by SAGE_ROOT/local/bin/spkg-update, this should fix the problem.",
    "created_at": "2010-07-17T15:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91666",
    "user": "was"
}
```

Hi,

I rewrote a script based on your idea (but not using your code).  I tested it by:

 (1) taking sage-4.5 and move spkg/pipestatus to spkg/pipestatus.orig
 (2) typed "make", then control-c in a few seconds
 (3) Do diff spkg/pipestatus spkg/pipestatus.orig and observe that the diff is just a single blank line.

Please review.  Since spkg/install is pulled in by SAGE_ROOT/local/bin/spkg-update, this should fix the problem.



---

archive/issue_comments_091667.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-17T15:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91667",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091668.json:
```json
{
    "body": "Replying to [comment:9 was]:\n> Please review.  Since spkg/install is pulled in by SAGE_ROOT/local/bin/spkg-update, this should fix the problem.\n\nI just noticed I had written `spkg-install` instead of `spkg/install`... :/\n\nOf course I prefer generating a version-specific `pipestatus`, but if it is a temporary solution, I'm ok with omitting it.\n\nI'd though at least fix `pipestatus`'s parameter checking as I did in my second version:\n\n```sh\n...\n  cat > pipestatus <<EOF\n#!/usr/bin/env bash\n\nif [ \\$# -ne 2 -o -z \"\\$1\" -o -z \"\\$2\" ]; then\n    echo \"Run two commands in a pipeline 'CMD1 | CMD2' and exit\"\n    echo \"with the exit status of CMD1, *not* that of CMD2.\"\n    echo \"\\$0 cmd1 cmd2\"\n    exit\nfi\n...\n```\n\n\nDropping the parentheses around `(set -o pipefail; eval \"\\$1 | \\$2\")` is optional, but you should remove `-n` from the `echo` in your `install`.\n\nWe cannot yet test upgrading from e.g. 4.4.4 though, can we?\n\n(I've tried your `install` there, it's ok when `deps` etc. get updated, too.)\n\nIn any case, add a\n\n```sh\n    chmod +x pipestatus\n```\n\nafter the `cat`...",
    "created_at": "2010-07-17T15:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91668",
    "user": "leif"
}
```

Replying to [comment:9 was]:
> Please review.  Since spkg/install is pulled in by SAGE_ROOT/local/bin/spkg-update, this should fix the problem.

I just noticed I had written `spkg-install` instead of `spkg/install`... :/

Of course I prefer generating a version-specific `pipestatus`, but if it is a temporary solution, I'm ok with omitting it.

I'd though at least fix `pipestatus`'s parameter checking as I did in my second version:

```sh
...
  cat > pipestatus <<EOF
#!/usr/bin/env bash

if [ \$# -ne 2 -o -z "\$1" -o -z "\$2" ]; then
    echo "Run two commands in a pipeline 'CMD1 | CMD2' and exit"
    echo "with the exit status of CMD1, *not* that of CMD2."
    echo "\$0 cmd1 cmd2"
    exit
fi
...
```


Dropping the parentheses around `(set -o pipefail; eval "\$1 | \$2")` is optional, but you should remove `-n` from the `echo` in your `install`.

We cannot yet test upgrading from e.g. 4.4.4 though, can we?

(I've tried your `install` there, it's ok when `deps` etc. get updated, too.)

In any case, add a

```sh
    chmod +x pipestatus
```

after the `cat`...



---

archive/issue_comments_091669.json:
```json
{
    "body": "Replying to [comment:9 was]:\n>  (3) Do diff spkg/pipestatus spkg/pipestatus.orig and observe that the diff is just a single blank line.\n\nUnfortunately, the blank line is in the wrong place. `#!` **must** be the first characters in the file, otherwise strange things happen...",
    "created_at": "2010-07-17T17:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91669",
    "user": "leif"
}
```

Replying to [comment:9 was]:
>  (3) Do diff spkg/pipestatus spkg/pipestatus.orig and observe that the diff is just a single blank line.

Unfortunately, the blank line is in the wrong place. `#!` **must** be the first characters in the file, otherwise strange things happen...



---

archive/issue_comments_091670.json:
```json
{
    "body": "Remove blank line, add chmod.  Updated `spkg/install` based on \"4.5\"",
    "created_at": "2010-07-17T21:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91670",
    "user": "mpatel"
}
```

Remove blank line, add chmod.  Updated `spkg/install` based on "4.5"



---

archive/issue_comments_091671.json:
```json
{
    "body": "Attachment [install.diff](tarball://root/attachments/some-uuid/ticket9528/install.diff) by mpatel created at 2010-07-17 21:17:56\n\nDiff of `spkg/install` vs \"4.5\".",
    "created_at": "2010-07-17T21:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91671",
    "user": "mpatel"
}
```

Attachment [install.diff](tarball://root/attachments/some-uuid/ticket9528/install.diff) by mpatel created at 2010-07-17 21:17:56

Diff of `spkg/install` vs "4.5".



---

archive/issue_comments_091672.json:
```json
{
    "body": "I apologize for not testing `sage -upgrade` (and other problems not yet found!).  Thanks very much for working on a fix.\n\nFollowing Leif's suggestions, I've attached a slightly updated `install` that I'm testing now.  Since we've already tested `pipestatus` on several platforms, I suggest making changes to it in a separate ticket.  Perhaps we could remove it altogether, in favor of always auto-generating it?",
    "created_at": "2010-07-17T21:28:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91672",
    "user": "mpatel"
}
```

I apologize for not testing `sage -upgrade` (and other problems not yet found!).  Thanks very much for working on a fix.

Following Leif's suggestions, I've attached a slightly updated `install` that I'm testing now.  Since we've already tested `pipestatus` on several platforms, I suggest making changes to it in a separate ticket.  Perhaps we could remove it altogether, in favor of always auto-generating it?



---

archive/issue_comments_091673.json:
```json
{
    "body": "Upgrading from 4.4.4 to 4.5 works for me on sage.math with [attachment:install.2].  The long doctests pass.  This is with `MAKE=\"-j12\"` and `SAGE_PARALLEL_SPKG_BUILD=\"yes\"`.  A separate, completely serial upgrade with MAKE unset is still running.\n\nStarting with \"4.5\" on sage.math, I copied [attachment:install.2] to `spkg/` and made a new source distribution with `sage -sdist 4.5.1`.  This builds with `MAKE=\"-j20\"` and `SAGE_PARALLEL_SPKG_BUILD=\"yes\"`.  The long doctests pass.  Another build with just `MAKE=\"-j16\"` is still running.\n\nThanks again for fixing this.",
    "created_at": "2010-07-17T22:30:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91673",
    "user": "mpatel"
}
```

Upgrading from 4.4.4 to 4.5 works for me on sage.math with [attachment:install.2].  The long doctests pass.  This is with `MAKE="-j12"` and `SAGE_PARALLEL_SPKG_BUILD="yes"`.  A separate, completely serial upgrade with MAKE unset is still running.

Starting with "4.5" on sage.math, I copied [attachment:install.2] to `spkg/` and made a new source distribution with `sage -sdist 4.5.1`.  This builds with `MAKE="-j20"` and `SAGE_PARALLEL_SPKG_BUILD="yes"`.  The long doctests pass.  Another build with just `MAKE="-j16"` is still running.

Thanks again for fixing this.



---

archive/issue_comments_091674.json:
```json
{
    "body": "Replying to [comment:13 mpatel]:\n> Upgrading from 4.4.4 to 4.5 works for me on sage.math with [attachment:install.2].  The long doctests pass.  This is with `MAKE=\"-j12\"` and `SAGE_PARALLEL_SPKG_BUILD=\"yes\"`.  A separate, completely serial upgrade with MAKE unset is still running.\n\n> Starting with \"4.5\" on sage.math, I copied [attachment:install.2] to `spkg/` and made a new source distribution with `sage -sdist 4.5.1`.  This builds with `MAKE=\"-j20\"` and `SAGE_PARALLEL_SPKG_BUILD=\"yes\"`.  The long doctests pass.  Another build with just `MAKE=\"-j16\"` is still running.\n\nThose builds' long doctests also pass, as do those for a completely serial build of \"4.5.1\" from scratch on sage.math.\n\nI'm attempting to upgrade from a 4.3.0.1 binary on t2.  I'm also building 4.4.4 on bsd.math so that I can test `sage -upgrade`.\n\nBut so far, my review is positive.",
    "created_at": "2010-07-18T01:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91674",
    "user": "mpatel"
}
```

Replying to [comment:13 mpatel]:
> Upgrading from 4.4.4 to 4.5 works for me on sage.math with [attachment:install.2].  The long doctests pass.  This is with `MAKE="-j12"` and `SAGE_PARALLEL_SPKG_BUILD="yes"`.  A separate, completely serial upgrade with MAKE unset is still running.

> Starting with "4.5" on sage.math, I copied [attachment:install.2] to `spkg/` and made a new source distribution with `sage -sdist 4.5.1`.  This builds with `MAKE="-j20"` and `SAGE_PARALLEL_SPKG_BUILD="yes"`.  The long doctests pass.  Another build with just `MAKE="-j16"` is still running.

Those builds' long doctests also pass, as do those for a completely serial build of "4.5.1" from scratch on sage.math.

I'm attempting to upgrade from a 4.3.0.1 binary on t2.  I'm also building 4.4.4 on bsd.math so that I can test `sage -upgrade`.

But so far, my review is positive.



---

archive/issue_comments_091675.json:
```json
{
    "body": "Upgrading from 4.4.4 also works for me on bsd.math.\n\nOn t2:  It seems the 4.3.0.1 binary is too old to upgrade.  (LinBox doesn't build, possibly because part of the toolchain has changed since 4.3.0.1 was built.)  But upgrading from \"4.5\" to \"4.5.1\" works, after deleting the former's `pipestatus`.\n\nI'm still building 4.4.4 on t2, but I think we're ready for the real 4.5.\n\nCan someone check that the small changes made from `install` to `install.2` are OK?",
    "created_at": "2010-07-18T08:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91675",
    "user": "mpatel"
}
```

Upgrading from 4.4.4 also works for me on bsd.math.

On t2:  It seems the 4.3.0.1 binary is too old to upgrade.  (LinBox doesn't build, possibly because part of the toolchain has changed since 4.3.0.1 was built.)  But upgrading from "4.5" to "4.5.1" works, after deleting the former's `pipestatus`.

I'm still building 4.4.4 on t2, but I think we're ready for the real 4.5.

Can someone check that the small changes made from `install` to `install.2` are OK?



---

archive/issue_comments_091676.json:
```json
{
    "body": "Replying to [comment:15 mpatel]:\n> I'm still building 4.4.4 on t2, but I think we're ready for the real 4.5.\n\nThe upgrade from 4.4.4 to \"4.5.1\" on t2 is now working on Singular --- the Sage and Gap packages remain.  No problems so far.  I need to sleep soon; I'll report again as soon as possible.\n\nAlso, \"4.5.1\" also builds from scratch on bsd.math.  The long doctests pass.",
    "created_at": "2010-07-18T10:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91676",
    "user": "mpatel"
}
```

Replying to [comment:15 mpatel]:
> I'm still building 4.4.4 on t2, but I think we're ready for the real 4.5.

The upgrade from 4.4.4 to "4.5.1" on t2 is now working on Singular --- the Sage and Gap packages remain.  No problems so far.  I need to sleep soon; I'll report again as soon as possible.

Also, "4.5.1" also builds from scratch on bsd.math.  The long doctests pass.



---

archive/issue_comments_091677.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-18T13:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91677",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091678.json:
```json
{
    "body": "Looks very good.  Thanks guys!!",
    "created_at": "2010-07-18T13:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91678",
    "user": "was"
}
```

Looks very good.  Thanks guys!!



---

archive/issue_comments_091679.json:
```json
{
    "body": "Replying to [comment:15 mpatel]:\n> Can someone check that the small changes made from `install` to `install.2` are OK?\n\nYes. Positive review, too.",
    "created_at": "2010-07-18T15:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91679",
    "user": "leif"
}
```

Replying to [comment:15 mpatel]:
> Can someone check that the small changes made from `install` to `install.2` are OK?

Yes. Positive review, too.



---

archive/issue_comments_091680.json:
```json
{
    "body": "In the long run, we should use something like `pipestatus` in `$SAGE_ROOT/makefile`, too.",
    "created_at": "2010-07-18T16:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91680",
    "user": "leif"
}
```

In the long run, we should use something like `pipestatus` in `$SAGE_ROOT/makefile`, too.



---

archive/issue_comments_091681.json:
```json
{
    "body": "Replying to [comment:15 mpatel]:\n> I'm still building 4.4.4 on t2, but I think we're ready for the real 4.5.\n\nUpgrading from 4.4.4 to \"4.5.1\" works on t2.  The long doctests pass.",
    "created_at": "2010-07-18T16:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91681",
    "user": "mpatel"
}
```

Replying to [comment:15 mpatel]:
> I'm still building 4.4.4 on t2, but I think we're ready for the real 4.5.

Upgrading from 4.4.4 to "4.5.1" works on t2.  The long doctests pass.



---

archive/issue_comments_091682.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-19T11:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9528#issuecomment-91682",
    "user": "rlm"
}
```

Resolution: fixed
