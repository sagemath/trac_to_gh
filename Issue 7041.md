# Issue 7041: GAP purposely unsets CC which screws up Sun Studio build.

archive/issues_007041.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @dimpase @ohanar\n\nKeywords: gap solaris cc\n\nThe spkg-install for gap-4.4.10.p12\n\necho \"*WARNING*: Unsetting CC since that tends to break GAP building\"\nunset CC\necho \"*WARNING*: Unsetting CXX since that tends to break GAP building\"\nunset CXX\n\nThis appears to be done by Michael Abshoff as SPKG.txt shows:\n\n### gap-4.4.10.p8 (Michael Abshoff, June 16th, 2008)\n* unset CC in spkg-install (work around for #2575)\n\n\nLooking at http://sagetrac.org/sage_trac/ticket/2575 I can't help feel there must be a better solution.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7041\n\n",
    "created_at": "2009-09-27T16:30:04Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.1",
    "title": "GAP purposely unsets CC which screws up Sun Studio build.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7041",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  @dimpase @ohanar

Keywords: gap solaris cc

The spkg-install for gap-4.4.10.p12

echo "*WARNING*: Unsetting CC since that tends to break GAP building"
unset CC
echo "*WARNING*: Unsetting CXX since that tends to break GAP building"
unset CXX

This appears to be done by Michael Abshoff as SPKG.txt shows:

### gap-4.4.10.p8 (Michael Abshoff, June 16th, 2008)
* unset CC in spkg-install (work around for #2575)


Looking at http://sagetrac.org/sage_trac/ticket/2575 I can't help feel there must be a better solution.

Issue created by migration from https://trac.sagemath.org/ticket/7041





---

archive/issue_comments_058287.json:
```json
{
    "body": "well, ignore that patch, wrong ticket (sometimes tab browsing hates you)",
    "created_at": "2012-02-06T23:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7041#issuecomment-58287",
    "user": "@ohanar"
}
```

well, ignore that patch, wrong ticket (sometimes tab browsing hates you)



---

archive/issue_comments_058288.json:
```json
{
    "body": "For the record, the GAP 4.4.12.p6 spkg still unsets these variables, for whatever reason (#2575 and #4161 might shed some light on that).\n\nHopefully someone will soon upgrade to GAP 4.5, which **might** solve potential issues with not unsetting them; haven't tested that (or looked at it) at all.",
    "created_at": "2012-03-22T14:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7041#issuecomment-58288",
    "user": "@nexttime"
}
```

For the record, the GAP 4.4.12.p6 spkg still unsets these variables, for whatever reason (#2575 and #4161 might shed some light on that).

Hopefully someone will soon upgrade to GAP 4.5, which **might** solve potential issues with not unsetting them; haven't tested that (or looked at it) at all.



---

archive/issue_comments_058289.json:
```json
{
    "body": "Changing keywords from \"gap solaris cc\" to \"gap solaris cc CXX compiler hardcoded hard-coded\".",
    "created_at": "2012-03-22T14:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7041#issuecomment-58289",
    "user": "@nexttime"
}
```

Changing keywords from "gap solaris cc" to "gap solaris cc CXX compiler hardcoded hard-coded".



---

archive/issue_comments_058290.json:
```json
{
    "body": "I'm currently preparing a GAP 4.4.12.p7 spkg fixing this issue (i.e., only unsetting `CC` and `CXX` if absolutely necessary), and cleaning up `SPKG.txt` and `spkg-install`.\n\nThere are still some open questions though; see e.g. my comments [comment:ticket:10825:14 here] (on #10825).",
    "created_at": "2012-03-22T17:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7041#issuecomment-58290",
    "user": "@nexttime"
}
```

I'm currently preparing a GAP 4.4.12.p7 spkg fixing this issue (i.e., only unsetting `CC` and `CXX` if absolutely necessary), and cleaning up `SPKG.txt` and `spkg-install`.

There are still some open questions though; see e.g. my comments [comment:ticket:10825:14 here] (on #10825).



---

archive/issue_comments_058291.json:
```json
{
    "body": "Replying to [comment:4 leif]:\n\n> There are still some open questions though; see e.g. my comments [comment:ticket:10825:14 here] (on #10825).\n\nI think what you did on #10825 is good.",
    "created_at": "2012-03-25T06:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7041#issuecomment-58291",
    "user": "@dimpase"
}
```

Replying to [comment:4 leif]:

> There are still some open questions though; see e.g. my comments [comment:ticket:10825:14 here] (on #10825).

I think what you did on #10825 is good.



---

archive/issue_comments_058292.json:
```json
{
    "body": "Excerpt from (the modified) `SPKG.txt`:\n\n## Dependencies\n\n* readline (according to spkg/standard/deps)\n* Sage (? also according to deps, \"so that gap_reset_workspace works\")\n\n## Special !Update/Build Instructions\n\n* TODO:\n  - Use `patch` instead of copying patched files.\n    (Then also add `patch` to the dependencies above.)\n  - \"Flatten\" (i.e. remove) the `build()` function.\n  - Perhaps check whether we can fix GAP's configure / build scripts\n    w.r.t. brokenness of multiple words in `CC` (and `CXX`?) and its\n    ignorance concerning `CFLAGS`, `CPPFLAGS` and `LDFLAGS`.\n    (Then also support `SAGE_DEBUG` in `spkg-install`, and probably\n    set up reasonable default `CFLAGS`.)\n\n* Do we really want to copy everything from the build directory???\n  (Cf. comment in `spkg-install`.)\n\n ...\n\n\nI'll perhaps address some of the TODOs (I added myself) later, in a p8, but I'd really like to get this spkg in soon.\n\nThe stated (probably obsolete?) dependency on Sage and the last point should be answered by some of **you**... ;-)",
    "created_at": "2012-04-09T12:12:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7041#issuecomment-58292",
    "user": "@nexttime"
}
```

Excerpt from (the modified) `SPKG.txt`:

## Dependencies

* readline (according to spkg/standard/deps)
* Sage (? also according to deps, "so that gap_reset_workspace works")

## Special !Update/Build Instructions

* TODO:
  - Use `patch` instead of copying patched files.
    (Then also add `patch` to the dependencies above.)
  - "Flatten" (i.e. remove) the `build()` function.
  - Perhaps check whether we can fix GAP's configure / build scripts
    w.r.t. brokenness of multiple words in `CC` (and `CXX`?) and its
    ignorance concerning `CFLAGS`, `CPPFLAGS` and `LDFLAGS`.
    (Then also support `SAGE_DEBUG` in `spkg-install`, and probably
    set up reasonable default `CFLAGS`.)

* Do we really want to copy everything from the build directory???
  (Cf. comment in `spkg-install`.)

 ...


I'll perhaps address some of the TODOs (I added myself) later, in a p8, but I'd really like to get this spkg in soon.

The stated (probably obsolete?) dependency on Sage and the last point should be answered by some of **you**... ;-)



---

archive/issue_comments_058293.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-04-09T12:12:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7041#issuecomment-58293",
    "user": "@nexttime"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058294.json:
```json
{
    "body": "Attachment [gap-4.4.12.p6-p7.diff](tarball://root/attachments/some-uuid/ticket7041/gap-4.4.12.p6-p7.diff) by @nexttime created at 2012-04-09 12:18:19\n\nDiff between the previous spkg in Sage and my new p7 spkg.  For reference / review only.",
    "created_at": "2012-04-09T12:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7041#issuecomment-58294",
    "user": "@nexttime"
}
```

Attachment [gap-4.4.12.p6-p7.diff](tarball://root/attachments/some-uuid/ticket7041/gap-4.4.12.p6-p7.diff) by @nexttime created at 2012-04-09 12:18:19

Diff between the previous spkg in Sage and my new p7 spkg.  For reference / review only.



---

archive/issue_comments_058295.json:
```json
{
    "body": "As usual, I've attached a diff of the spkg for easier reviewing.",
    "created_at": "2012-04-09T12:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7041#issuecomment-58295",
    "user": "@nexttime"
}
```

As usual, I've attached a diff of the spkg for easier reviewing.



---

archive/issue_comments_058296.json:
```json
{
    "body": "Changing assignee from tbd to @nexttime.",
    "created_at": "2012-04-09T12:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7041#issuecomment-58296",
    "user": "@nexttime"
}
```

Changing assignee from tbd to @nexttime.



---

archive/issue_comments_058297.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-28T11:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7041#issuecomment-58297",
    "user": "@ohanar"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058298.json:
```json
{
    "body": "Looks good and works well.",
    "created_at": "2012-05-28T11:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7041#issuecomment-58298",
    "user": "@ohanar"
}
```

Looks good and works well.



---

archive/issue_comments_058299.json:
```json
{
    "body": "Changing keywords from \"gap solaris cc CXX compiler hardcoded hard-coded\" to \"gap solaris cc CXX compiler hardcoded hard-coded sd40.5\".",
    "created_at": "2012-05-29T06:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7041#issuecomment-58299",
    "user": "@ohanar"
}
```

Changing keywords from "gap solaris cc CXX compiler hardcoded hard-coded" to "gap solaris cc CXX compiler hardcoded hard-coded sd40.5".



---

archive/issue_comments_058300.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-06-06T19:10:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7041#issuecomment-58300",
    "user": "@jdemeyer"
}
```

Resolution: fixed
