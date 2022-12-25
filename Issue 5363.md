# Issue 5363: Sage 3.4.alpha0: -sdist issue: MANIFEST.in needs to add the missing 186 files

archive/issues_005363.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @mwhansen\n\nFor 3.4.alpha0 -sdist does not include any of the new doc repo code, i.e. if one runs \"hg update -C\" in devel/sage after building you will see\n\n```\n 186 files updated, 0 files merged, 0 files removed, 0 files unresolved\n```\n\nI corrected this in the official 3.4.alpha0.tar, but this needs fixing before the final 3.4 release, so this is a blocker.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5363\n\n",
    "created_at": "2009-02-24T22:57:35Z",
    "labels": [
        "component: distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "Sage 3.4.alpha0: -sdist issue: MANIFEST.in needs to add the missing 186 files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5363",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @mwhansen

For 3.4.alpha0 -sdist does not include any of the new doc repo code, i.e. if one runs "hg update -C" in devel/sage after building you will see

```
 186 files updated, 0 files merged, 0 files removed, 0 files unresolved
```

I corrected this in the official 3.4.alpha0.tar, but this needs fixing before the final 3.4 release, so this is a blocker.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5363





---

archive/issue_comments_041237.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-01T04:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5363#issuecomment-41237",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041238.json:
```json
{
    "body": "Attachment [trac_5363.patch](tarball://root/attachments/some-uuid/ticket5363/trac_5363.patch) by mabshoff created at 2009-03-01 04:40:16",
    "created_at": "2009-03-01T04:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5363#issuecomment-41238",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5363.patch](tarball://root/attachments/some-uuid/ticket5363/trac_5363.patch) by mabshoff created at 2009-03-01 04:40:16



---

archive/issue_comments_041239.json:
```json
{
    "body": "I think we want to also include the html files under doc (for things like templates, etc.) and then just prune the doc/output directory.",
    "created_at": "2009-03-01T15:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5363#issuecomment-41239",
    "user": "https://github.com/mwhansen"
}
```

I think we want to also include the html files under doc (for things like templates, etc.) and then just prune the doc/output directory.



---

archive/issue_comments_041240.json:
```json
{
    "body": "Looks good to me!  Very nice.  Great to move it to multiple lines and add doc.",
    "created_at": "2009-03-01T16:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5363#issuecomment-41240",
    "user": "https://github.com/williamstein"
}
```

Looks good to me!  Very nice.  Great to move it to multiple lines and add doc.



---

archive/issue_comments_041241.json:
```json
{
    "body": "Replying to [comment:2 mhansen]:\n> I think we want to also include the html files under doc (for things like templates, etc.) and then just prune the doc/output directory.\n\nI don't think we want those files in the -sdist tarball, but I would like to see the html documentation installed centrally, i.e. #5410, so that -bdist picks it up.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T19:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5363#issuecomment-41241",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 mhansen]:
> I think we want to also include the html files under doc (for things like templates, etc.) and then just prune the doc/output directory.

I don't think we want those files in the -sdist tarball, but I would like to see the html documentation installed centrally, i.e. #5410, so that -bdist picks it up.

Cheers,

Michael



---

archive/issue_comments_041242.json:
```json
{
    "body": "Replying to [comment:5 mabshoff]:\n> I don't think we want those files in the -sdist tarball, but I would like to see the html documentation installed centrally, i.e. #5410, so that -bdist picks it up.\n\nThere is a non autogenerated HTML file which is part of the repo and should be included in doc/common/templates.  There will be more things like these (such as CSS files etc.) in the future as well.\n\n--Mike",
    "created_at": "2009-03-01T19:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5363#issuecomment-41242",
    "user": "https://github.com/mwhansen"
}
```

Replying to [comment:5 mabshoff]:
> I don't think we want those files in the -sdist tarball, but I would like to see the html documentation installed centrally, i.e. #5410, so that -bdist picks it up.

There is a non autogenerated HTML file which is part of the repo and should be included in doc/common/templates.  There will be more things like these (such as CSS files etc.) in the future as well.

--Mike



---

archive/issue_comments_041243.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-02T02:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5363#issuecomment-41243",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041244.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T02:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5363#issuecomment-41244",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael
