# Issue 5414: notebook help: the live documentation list are broken after the doc removal

archive/issues_005414.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  mhansen jhpalmieri\n\nThe notebook help screen has links to the reference manual and so on. Those links point to the doc repo where the static html lives. Once #5410 is done those links should be fixed to point to the new static html.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5414\n\n",
    "created_at": "2009-03-01T21:17:39Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "title": "notebook help: the live documentation list are broken after the doc removal",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5414",
    "user": "mabshoff"
}
```
Assignee: boothby

CC:  mhansen jhpalmieri

The notebook help screen has links to the reference manual and so on. Those links point to the doc repo where the static html lives. Once #5410 is done those links should be fixed to point to the new static html.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5414





---

archive/issue_comments_041869.json:
```json
{
    "body": "The documentation links mostly work once the needed html documentation has been created, i.e.\n\n```\n./sage -docbuild reference html\n./sage -docbuild tutorial html\n./sage -docbuild developer html\n./sage -docbuild constructions html\n```\n\nThe only thing not working after that is the \"Fast Static Versions of the Documentation\" link from the main help page.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-09T19:48:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5414#issuecomment-41869",
    "user": "mabshoff"
}
```

The documentation links mostly work once the needed html documentation has been created, i.e.

```
./sage -docbuild reference html
./sage -docbuild tutorial html
./sage -docbuild developer html
./sage -docbuild constructions html
```

The only thing not working after that is the "Fast Static Versions of the Documentation" link from the main help page.

Cheers,

Michael



---

archive/issue_comments_041870.json:
```json
{
    "body": "Attachment [trac_5414-install.diff](tarball://root/attachments/some-uuid/ticket5414/trac_5414-install.diff) by mhansen created at 2009-03-11 05:11:22",
    "created_at": "2009-03-11T05:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5414#issuecomment-41870",
    "user": "mhansen"
}
```

Attachment [trac_5414-install.diff](tarball://root/attachments/some-uuid/ticket5414/trac_5414-install.diff) by mhansen created at 2009-03-11 05:11:22



---

archive/issue_comments_041871.json:
```json
{
    "body": "Attachment [trac_5414.patch](tarball://root/attachments/some-uuid/ticket5414/trac_5414.patch) by mhansen created at 2009-03-11 05:18:20",
    "created_at": "2009-03-11T05:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5414#issuecomment-41871",
    "user": "mhansen"
}
```

Attachment [trac_5414.patch](tarball://root/attachments/some-uuid/ticket5414/trac_5414.patch) by mhansen created at 2009-03-11 05:18:20



---

archive/issue_comments_041872.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-11T05:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5414#issuecomment-41872",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041873.json:
```json
{
    "body": "Changing assignee from boothby to mhansen.",
    "created_at": "2009-03-11T05:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5414#issuecomment-41873",
    "user": "mhansen"
}
```

Changing assignee from boothby to mhansen.



---

archive/issue_comments_041874.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-11T05:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5414#issuecomment-41874",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_041875.json:
```json
{
    "body": "Attachment [trac_5414-scripts.patch](tarball://root/attachments/some-uuid/ticket5414/trac_5414-scripts.patch) by mhansen created at 2009-03-11 05:40:35",
    "created_at": "2009-03-11T05:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5414#issuecomment-41875",
    "user": "mhansen"
}
```

Attachment [trac_5414-scripts.patch](tarball://root/attachments/some-uuid/ticket5414/trac_5414-scripts.patch) by mhansen created at 2009-03-11 05:40:35



---

archive/issue_comments_041876.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-11T06:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5414#issuecomment-41876",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041877.json:
```json
{
    "body": "Merged all three patches in Sage 3.4.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-11T06:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5414#issuecomment-41877",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.4.final.

Cheers,

Michael



---

archive/issue_comments_041878.json:
```json
{
    "body": "Does this depend on another ticket?  If not, trac_5414-install.diff has the line \n\n```\n\"$SAGE_LOCAL/bin\"/sage-docbuild --jsmath all html\n```\n\nand I don't see a file sage-docbuild anywhere.  Should it be \"sage -docbuild\"?",
    "created_at": "2009-03-11T17:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5414#issuecomment-41878",
    "user": "jhpalmieri"
}
```

Does this depend on another ticket?  If not, trac_5414-install.diff has the line 

```
"$SAGE_LOCAL/bin"/sage-docbuild --jsmath all html
```

and I don't see a file sage-docbuild anywhere.  Should it be "sage -docbuild"?



---

archive/issue_comments_041879.json:
```json
{
    "body": "Hi John,\n\nActually, mabshoff and I fixed that bit in person so that it does the right thing.  But, you're right, it should be \"$SAGE_ROOT\"/sage -dodbuild.  We'll post the actual diff here in a sec.\n\n--Mike",
    "created_at": "2009-03-11T17:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5414#issuecomment-41879",
    "user": "mhansen"
}
```

Hi John,

Actually, mabshoff and I fixed that bit in person so that it does the right thing.  But, you're right, it should be "$SAGE_ROOT"/sage -dodbuild.  We'll post the actual diff here in a sec.

--Mike
