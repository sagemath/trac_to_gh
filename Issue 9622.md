# Issue 9622: Check SPKGs more vigorously for common problems

archive/issues_009622.json:
```json
{
    "body": "Assignee: tbd\n\nWhen we build new or updated Sage packages (spkgs), `SAGE_LOCAL/bin/sage-pkg` runs a few checks for common problems.  For example,\n\n\n```sh\n$ sage -pkg foo/\nCreating Sage package foo/\nWarning: no version number detected\n\nCreated package foo.spkg.\n\n    NAME: foo\n VERSION:\n    SIZE: 17.8M\n HG REPO: Good\nSPKG.txt: Good\n\nPlease test this package using\n[...]\n```\n\n\nBut we could add several new, more detailed tests for `spkg-install`, etc.  Or put them in a `sage-spkg-{check,checker,lint}` script.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9622\n\n",
    "created_at": "2010-07-28T08:42:37Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Check SPKGs more vigorously for common problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9622",
    "user": "@qed777"
}
```
Assignee: tbd

When we build new or updated Sage packages (spkgs), `SAGE_LOCAL/bin/sage-pkg` runs a few checks for common problems.  For example,


```sh
$ sage -pkg foo/
Creating Sage package foo/
Warning: no version number detected

Created package foo.spkg.

    NAME: foo
 VERSION:
    SIZE: 17.8M
 HG REPO: Good
SPKG.txt: Good

Please test this package using
[...]
```


But we could add several new, more detailed tests for `spkg-install`, etc.  Or put them in a `sage-spkg-{check,checker,lint}` script.

Issue created by migration from https://trac.sagemath.org/ticket/9622





---

archive/issue_comments_093206.json:
```json
{
    "body": "Possibilities, some of which could simply give warnings or reminders:\n\n* Check for `spkg-check` and `spkg-install` and that they're executable.\n* Check the first line of scripts for `#!/usr/bin/env` (cf. #9597).\n* Check for an unfinished Mercurial patch queue.\n* Check for the presence of `set -e`.\n* Check for the presence of $MAKE and other important variables.\n* Check for Python scripts and whether Python is a dependency in `spkg/standard/deps` (cf. #9435, #9507).\n\nI'm sure there are others!",
    "created_at": "2010-07-28T08:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9622#issuecomment-93206",
    "user": "@qed777"
}
```

Possibilities, some of which could simply give warnings or reminders:

* Check for `spkg-check` and `spkg-install` and that they're executable.
* Check the first line of scripts for `#!/usr/bin/env` (cf. #9597).
* Check for an unfinished Mercurial patch queue.
* Check for the presence of `set -e`.
* Check for the presence of $MAKE and other important variables.
* Check for Python scripts and whether Python is a dependency in `spkg/standard/deps` (cf. #9435, #9507).

I'm sure there are others!



---

archive/issue_comments_093207.json:
```json
{
    "body": "Yep, but two comments:\n\n* I wonder how many people actually use `sage-pkg` to create spkgs (rather than just use `tar`).\n\n* In a perfect world, the reviewer(s) would do this job (i.e. look at the code e.g., too, not just try to install a new package and then give positive review, or sometimes the other way around).\n\nI was thinking of a good spkg template (`-install`, `-check`, `SPKG.txt`), too. And perhaps some minimalistic shell programming guide targeted at Sage scripts.",
    "created_at": "2010-07-28T12:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9622#issuecomment-93207",
    "user": "@nexttime"
}
```

Yep, but two comments:

* I wonder how many people actually use `sage-pkg` to create spkgs (rather than just use `tar`).

* In a perfect world, the reviewer(s) would do this job (i.e. look at the code e.g., too, not just try to install a new package and then give positive review, or sometimes the other way around).

I was thinking of a good spkg template (`-install`, `-check`, `SPKG.txt`), too. And perhaps some minimalistic shell programming guide targeted at Sage scripts.



---

archive/issue_comments_093208.json:
```json
{
    "body": "I've created a (vaguely) related ticket:\n\n  *Update and extend \"SPKG Tracking\" Wiki page*, #9626.\n\n(`sage-pkg` could spit out some reminder...)\n\nComments there welcome.",
    "created_at": "2010-07-28T18:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9622#issuecomment-93208",
    "user": "@nexttime"
}
```

I've created a (vaguely) related ticket:

  *Update and extend "SPKG Tracking" Wiki page*, #9626.

(`sage-pkg` could spit out some reminder...)

Comments there welcome.



---

archive/issue_comments_093209.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-07-28T18:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9622#issuecomment-93209",
    "user": "@nexttime"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_093210.json:
```json
{
    "body": "We could also formalize/code some aspects of `SPKG.txt`'s *Special Update/Build Instructions*, e.g. in (a) new (optional) script(s) like `spkg-cleanup-upstream` (deleting parts not needed by Sage, upstream repo files, etc.), contained in the spkg itself, and perhaps run automatically.\n\nSome upstream managers also tend to copy files without preserving mtime, so we could more or less automatically check for files like `configure`, make sure they are newer than their sources, and if not, touch them before preparing the spkg.\n\nThe application of patches to the upstream source tree (i.e. currently *copying of patched files*) could also be \"normalized\", allowing to perform some spkg sanity checks automatically, too, and to simplify `spkg-install`s.",
    "created_at": "2010-07-28T19:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9622#issuecomment-93210",
    "user": "@nexttime"
}
```

We could also formalize/code some aspects of `SPKG.txt`'s *Special Update/Build Instructions*, e.g. in (a) new (optional) script(s) like `spkg-cleanup-upstream` (deleting parts not needed by Sage, upstream repo files, etc.), contained in the spkg itself, and perhaps run automatically.

Some upstream managers also tend to copy files without preserving mtime, so we could more or less automatically check for files like `configure`, make sure they are newer than their sources, and if not, touch them before preparing the spkg.

The application of patches to the upstream source tree (i.e. currently *copying of patched files*) could also be "normalized", allowing to perform some spkg sanity checks automatically, too, and to simplify `spkg-install`s.



---

archive/issue_comments_093211.json:
```json
{
    "body": "Replying to [comment:2 leif]:\n>  * I wonder how many people actually use `sage-pkg` to create spkgs (rather than just use `tar`).\n\nGood question.  I usually use `sage -spkg`, an alias of `sage -pkg`.\n\n>  * In a perfect world, the reviewer(s) would do this job (i.e. look at the code e.g., too, not just try to install a new package and then give positive review, or sometimes the other way around).\n\nJust a quick thought:  We could also run the spkg checks, or a subset of them, during installation.",
    "created_at": "2010-07-29T07:19:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9622#issuecomment-93211",
    "user": "@qed777"
}
```

Replying to [comment:2 leif]:
>  * I wonder how many people actually use `sage-pkg` to create spkgs (rather than just use `tar`).

Good question.  I usually use `sage -spkg`, an alias of `sage -pkg`.

>  * In a perfect world, the reviewer(s) would do this job (i.e. look at the code e.g., too, not just try to install a new package and then give positive review, or sometimes the other way around).

Just a quick thought:  We could also run the spkg checks, or a subset of them, during installation.



---

archive/issue_comments_093212.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> Possibilities, some of which could simply give warnings or reminders:\n> \n>  * Check for `spkg-check` and `spkg-install` and that they're executable.\n\nGood idea\n\n>  * Check the first line of scripts for `#!/usr/bin/env` (cf. #9597).\n\nYes. \n\n>  * Check for an unfinished Mercurial patch queue.\n\nYes \n\n>  * Check for the presence of `set -e`.\n\nWilliam will not have that. He is very against the use of set -e. \n\n>  * Check for the presence of $MAKE and other important variables.\n\nWhat's important in one package is not in another. That might be difficult to do. \n\n>  * Check for Python scripts and whether Python is a dependency in `spkg/standard/deps` (cf. #9435, #9507).\n> \n> I'm sure there are others!\n\nIf the package is called foobar-x.y.z, then SPKG.txt should have the string foobar.x.y.z somewhere in it. Many times commits get made, with no entry in SPKG.txt\n\nDave",
    "created_at": "2010-07-29T10:43:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9622#issuecomment-93212",
    "user": "drkirkby"
}
```

Replying to [comment:1 mpatel]:
> Possibilities, some of which could simply give warnings or reminders:
> 
>  * Check for `spkg-check` and `spkg-install` and that they're executable.

Good idea

>  * Check the first line of scripts for `#!/usr/bin/env` (cf. #9597).

Yes. 

>  * Check for an unfinished Mercurial patch queue.

Yes 

>  * Check for the presence of `set -e`.

William will not have that. He is very against the use of set -e. 

>  * Check for the presence of $MAKE and other important variables.

What's important in one package is not in another. That might be difficult to do. 

>  * Check for Python scripts and whether Python is a dependency in `spkg/standard/deps` (cf. #9435, #9507).
> 
> I'm sure there are others!

If the package is called foobar-x.y.z, then SPKG.txt should have the string foobar.x.y.z somewhere in it. Many times commits get made, with no entry in SPKG.txt

Dave



---

archive/issue_comments_093213.json:
```json
{
    "body": "One other thing, make sure all the required sections from SPKG.txt exist. i.e. none are missing. Even if there are no special build instructions, the section should exist and simply say \"none\". \n\nOne could also check that entries in SPKG.txt have something in each section. But this could get a lot of work.",
    "created_at": "2010-07-29T10:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9622#issuecomment-93213",
    "user": "drkirkby"
}
```

One other thing, make sure all the required sections from SPKG.txt exist. i.e. none are missing. Even if there are no special build instructions, the section should exist and simply say "none". 

One could also check that entries in SPKG.txt have something in each section. But this could get a lot of work.



---

archive/issue_comments_093214.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-10-29T08:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9622#issuecomment-93214",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093215.json:
```json
{
    "body": "Close because we no longer use spkgs.",
    "created_at": "2014-10-29T08:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9622#issuecomment-93215",
    "user": "@jdemeyer"
}
```

Close because we no longer use spkgs.



---

archive/issue_comments_093216.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-10-29T08:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9622#issuecomment-93216",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093217.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2014-10-29T22:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9622#issuecomment-93217",
    "user": "@vbraun"
}
```

Resolution: invalid
