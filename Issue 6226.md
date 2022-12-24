# Issue 6226: developer's guide: sections on formatting docstrings and trac guidelines

archive/issues_006226.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: developer's guide\n\nWe need to add to the developer's guide some information about docstring formatting in ReST, and how to build the Sage standard documentation. The developer's guide also needs to document further detailed guidelines when working on tickets.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6226\n\n",
    "created_at": "2009-06-05T15:18:00Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "developer's guide: sections on formatting docstrings and trac guidelines",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6226",
    "user": "mvngu"
}
```
Assignee: tba

Keywords: developer's guide

We need to add to the developer's guide some information about docstring formatting in ReST, and how to build the Sage standard documentation. The developer's guide also needs to document further detailed guidelines when working on tickets.

Issue created by migration from https://trac.sagemath.org/ticket/6226





---

archive/issue_comments_049697.json:
```json
{
    "body": "based on Sage 4.0.1.rc1",
    "created_at": "2009-06-05T15:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6226#issuecomment-49697",
    "user": "mvngu"
}
```

based on Sage 4.0.1.rc1



---

archive/issue_comments_049698.json:
```json
{
    "body": "Attachment [trac_6226.patch](tarball://root/attachments/some-uuid/ticket6226/trac_6226.patch) by mvngu created at 2009-06-05 15:31:09\n\nThe patch `trac_6226.patch` fixes some typos in the developer's guide. It also adds sections on formatting documentation using ReST. The information on that is taken from the Sage wiki at\n\n\n\nhttp://wiki.sagemath.org/combinat/HelpOnTheDoc\n\n\n\nwritten by Florent Hivert. The patch also adds guidelines on the trac server and working on tickets. These guidelines were written by Michael Abshoff and can be found at \n\n\n\nhttp://wiki.sagemath.org/TracGuidelines\n\n\n\nSo authorship credit should be shared with Michael Abshoff and Florent Hivert.",
    "created_at": "2009-06-05T15:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6226#issuecomment-49698",
    "user": "mvngu"
}
```

Attachment [trac_6226.patch](tarball://root/attachments/some-uuid/ticket6226/trac_6226.patch) by mvngu created at 2009-06-05 15:31:09

The patch `trac_6226.patch` fixes some typos in the developer's guide. It also adds sections on formatting documentation using ReST. The information on that is taken from the Sage wiki at



http://wiki.sagemath.org/combinat/HelpOnTheDoc



written by Florent Hivert. The patch also adds guidelines on the trac server and working on tickets. These guidelines were written by Michael Abshoff and can be found at 



http://wiki.sagemath.org/TracGuidelines



So authorship credit should be shared with Michael Abshoff and Florent Hivert.



---

archive/issue_comments_049699.json:
```json
{
    "body": "Comments: very nice overall.  I have a second patch, to be applied on top of yours, which deals with a few small issues:\n\nin producing_patches.rst, `hg_sage.patch(...)` and `hg_sage.apply(...)` are not synonyms, and it sounds like that a bit.  Also, you've deleted one reference to the \"doc\" repository, but there's another (two lines after \"Sage includes these Mercuruial repositories\").\n\nin sage_manuals.rst: as far as I can tell, you don't need to run `sage -b` when producing new versions of any manual other than the reference manual: just edit the files and run `sage -docbuild tutorial html` or whatever.  There are a few typos, too.\n\nin trac.rst: I thought that a few of the lines from the wiki were more appropriate for a wiki page than a formal piece of documentation, so I removed them.\n\nI give your patch a positive review, so if you're happy with mine, the whole thing is ready to go.",
    "created_at": "2009-06-05T19:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6226#issuecomment-49699",
    "user": "jhpalmieri"
}
```

Comments: very nice overall.  I have a second patch, to be applied on top of yours, which deals with a few small issues:

in producing_patches.rst, `hg_sage.patch(...)` and `hg_sage.apply(...)` are not synonyms, and it sounds like that a bit.  Also, you've deleted one reference to the "doc" repository, but there's another (two lines after "Sage includes these Mercuruial repositories").

in sage_manuals.rst: as far as I can tell, you don't need to run `sage -b` when producing new versions of any manual other than the reference manual: just edit the files and run `sage -docbuild tutorial html` or whatever.  There are a few typos, too.

in trac.rst: I thought that a few of the lines from the wiki were more appropriate for a wiki page than a formal piece of documentation, so I removed them.

I give your patch a positive review, so if you're happy with mine, the whole thing is ready to go.



---

archive/issue_comments_049700.json:
```json
{
    "body": "Changing assignee from tba to mvngu.",
    "created_at": "2009-06-05T19:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6226#issuecomment-49700",
    "user": "jhpalmieri"
}
```

Changing assignee from tba to mvngu.



---

archive/issue_comments_049701.json:
```json
{
    "body": "Attachment [trac_6226_part2.patch](tarball://root/attachments/some-uuid/ticket6226/trac_6226_part2.patch) by jhpalmieri created at 2009-06-05 19:44:39",
    "created_at": "2009-06-05T19:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6226#issuecomment-49701",
    "user": "jhpalmieri"
}
```

Attachment [trac_6226_part2.patch](tarball://root/attachments/some-uuid/ticket6226/trac_6226_part2.patch) by jhpalmieri created at 2009-06-05 19:44:39



---

archive/issue_comments_049702.json:
```json
{
    "body": "Attachment [trac_6226-part3.patch](tarball://root/attachments/some-uuid/ticket6226/trac_6226-part3.patch) by mvngu created at 2009-06-05 20:57:24\n\nThe patch `trac_6226_part2.patch` looks good to me. After applying `trac_6226.patch` and `trac_6226_part2.patch` to Sage 4.0.1.rc2 and re-reading the developer's guide, I noticed more typos. These are fixed in `trac_6226-part3.patch`. If it gets positive review, then the patches on this ticket should be applied in the following order:\n1. `trac_6226.patch`\n2. `trac_6226_part2.patch`\n3. `trac_6226-part3.patch`",
    "created_at": "2009-06-05T20:57:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6226#issuecomment-49702",
    "user": "mvngu"
}
```

Attachment [trac_6226-part3.patch](tarball://root/attachments/some-uuid/ticket6226/trac_6226-part3.patch) by mvngu created at 2009-06-05 20:57:24

The patch `trac_6226_part2.patch` looks good to me. After applying `trac_6226.patch` and `trac_6226_part2.patch` to Sage 4.0.1.rc2 and re-reading the developer's guide, I noticed more typos. These are fixed in `trac_6226-part3.patch`. If it gets positive review, then the patches on this ticket should be applied in the following order:
1. `trac_6226.patch`
2. `trac_6226_part2.patch`
3. `trac_6226-part3.patch`



---

archive/issue_comments_049703.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T23:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6226#issuecomment-49703",
    "user": "ncalexan"
}
```

Resolution: fixed
