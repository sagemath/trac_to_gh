# Issue 7784: sagenb -- either include setup.cfg if it is human-written or put it in the .hgignore file

archive/issues_007784.json:
```json
{
    "body": "Assignee: was\n\nCC:  mvngu robert.marik\n\nObserve in sagenb-0.4.8:\n\n```\nflat:src wstein$ hg status\nM setup.py\n? release_notes.txt\n? setup.cfg\nflat:src wstein$ more setup.cfg\n[egg_info]\ntag_build =\ntag_date = 0\ntag_svn_revision = 0\n```\n\n\n\nThis makes me think it is human written?  http://www.python.org/doc/2.1.3/dist/setup-config.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/7784\n\n",
    "created_at": "2009-12-29T08:26:16Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "sagenb -- either include setup.cfg if it is human-written or put it in the .hgignore file",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7784",
    "user": "was"
}
```
Assignee: was

CC:  mvngu robert.marik

Observe in sagenb-0.4.8:

```
flat:src wstein$ hg status
M setup.py
? release_notes.txt
? setup.cfg
flat:src wstein$ more setup.cfg
[egg_info]
tag_build =
tag_date = 0
tag_svn_revision = 0
```



This makes me think it is human written?  http://www.python.org/doc/2.1.3/dist/setup-config.html

Issue created by migration from https://trac.sagemath.org/ticket/7784





---

archive/issue_comments_067122.json:
```json
{
    "body": "Update .hgignore.",
    "created_at": "2010-01-25T03:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67122",
    "user": "mpatel"
}
```

Update .hgignore.



---

archive/issue_comments_067123.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-01-25T03:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67123",
    "user": "mpatel"
}
```

Changing priority from major to minor.



---

archive/issue_comments_067124.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-25T03:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67124",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067125.json:
```json
{
    "body": "Attachment\n\nIn the patch, I've added `setup.cfg` and `release_notes.txt` and attempted to remove unnecessary entries.  Please feel free to go further.",
    "created_at": "2010-01-25T03:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67125",
    "user": "mpatel"
}
```

Attachment

In the patch, I've added `setup.cfg` and `release_notes.txt` and attempted to remove unnecessary entries.  Please feel free to go further.



---

archive/issue_comments_067126.json:
```json
{
    "body": "I think I should restore `push` and `pull`.",
    "created_at": "2010-01-25T04:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67126",
    "user": "mpatel"
}
```

I think I should restore `push` and `pull`.



---

archive/issue_comments_067127.json:
```json
{
    "body": "Attachment\n\nInclude `pull` and `push`.  Replaces previous.",
    "created_at": "2010-01-25T04:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67127",
    "user": "mpatel"
}
```

Attachment

Include `pull` and `push`.  Replaces previous.



---

archive/issue_comments_067128.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> I think I should restore `push` and `pull`.\nV2 does this.",
    "created_at": "2010-01-25T04:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67128",
    "user": "mpatel"
}
```

Replying to [comment:3 mpatel]:
> I think I should restore `push` and `pull`.
V2 does this.



---

archive/issue_comments_067129.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2010-02-01T03:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67129",
    "user": "mpatel"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_067130.json:
```json
{
    "body": "Changing priority from minor to critical.",
    "created_at": "2010-02-01T03:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67130",
    "user": "mpatel"
}
```

Changing priority from minor to critical.



---

archive/issue_comments_067131.json:
```json
{
    "body": "Attachment\n\nAdd Makefile; update .hgignore and spkg-related files.  Apply only this patch.",
    "created_at": "2010-02-01T03:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67131",
    "user": "mpatel"
}
```

Attachment

Add Makefile; update .hgignore and spkg-related files.  Apply only this patch.



---

archive/issue_comments_067132.json:
```json
{
    "body": "The [attachment:trac_7784-sagenb_spkg_files.patch new patch] cleans up some build-related files.  This \"blocks\" #8051.",
    "created_at": "2010-02-01T03:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67132",
    "user": "mpatel"
}
```

The [attachment:trac_7784-sagenb_spkg_files.patch new patch] cleans up some build-related files.  This "blocks" #8051.



---

archive/issue_comments_067133.json:
```json
{
    "body": "I haven't decided yet what to do about `release_notes.txt`, so I haven't updated it.  If we can auto-generate it, that would be great.",
    "created_at": "2010-02-01T03:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67133",
    "user": "mpatel"
}
```

I haven't decided yet what to do about `release_notes.txt`, so I haven't updated it.  If we can auto-generate it, that would be great.



---

archive/issue_comments_067134.json:
```json
{
    "body": "Replying to [comment:7 mpatel]:\n> I haven't decided yet what to do about `release_notes.txt`, so I haven't updated it.  If we can auto-generate it, that would be great.\n\nI have been using the script at the following site to generate release notes for Sage:\n\nhttp://bitbucket.org/mvngu/rnotes/\n\nI think an option could be added to that script to generate release notes for sagenb. The current usage for the script is\n\n```\n./generate_release_notes sage-x.y.z\n```\n\nA possible option for generating sagenb specific release notes is\n\n```\n./generate_release_notes sage-x.y.z -sagenb\n```\n\nThis would generate a release note for all sagenb specific tickets closed in the Sage x.y.z milestone. It's possible that during a particular milestone, more than one version of sagenb is released and integrated into Sage. Another possibility is \n\n```\n./generate_release_notes sagenb-x.y.z\n```\n\nThis would generate a release note for sagenb x.y.z.",
    "created_at": "2010-02-01T04:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67134",
    "user": "mvngu"
}
```

Replying to [comment:7 mpatel]:
> I haven't decided yet what to do about `release_notes.txt`, so I haven't updated it.  If we can auto-generate it, that would be great.

I have been using the script at the following site to generate release notes for Sage:

http://bitbucket.org/mvngu/rnotes/

I think an option could be added to that script to generate release notes for sagenb. The current usage for the script is

```
./generate_release_notes sage-x.y.z
```

A possible option for generating sagenb specific release notes is

```
./generate_release_notes sage-x.y.z -sagenb
```

This would generate a release note for all sagenb specific tickets closed in the Sage x.y.z milestone. It's possible that during a particular milestone, more than one version of sagenb is released and integrated into Sage. Another possibility is 

```
./generate_release_notes sagenb-x.y.z
```

This would generate a release note for sagenb x.y.z.



---

archive/issue_comments_067135.json:
```json
{
    "body": "Changing assignee from was to mpatel.",
    "created_at": "2010-02-01T06:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67135",
    "user": "mpatel"
}
```

Changing assignee from was to mpatel.



---

archive/issue_comments_067136.json:
```json
{
    "body": "Thanks!  I'll definitely take a closer look (though not immediately).  I assume we'll make it separate ticket so we don't hold up this one.",
    "created_at": "2010-02-01T06:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67136",
    "user": "mpatel"
}
```

Thanks!  I'll definitely take a closer look (though not immediately).  I assume we'll make it separate ticket so we don't hold up this one.



---

archive/issue_comments_067137.json:
```json
{
    "body": "Changing assignee from mpatel to was.",
    "created_at": "2010-02-01T07:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67137",
    "user": "mpatel"
}
```

Changing assignee from mpatel to was.



---

archive/issue_comments_067138.json:
```json
{
    "body": "Looks good to me. Apply the attachment [trac_7784-sagenb_spkg_files.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7784/trac_7784-sagenb_spkg_files.patch) to [sagenb-0.7.2.spkg](http://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.2.spkg) under the directory `sagenb-0.7.2/src/sagenb`.",
    "created_at": "2010-02-02T23:26:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67138",
    "user": "mvngu"
}
```

Looks good to me. Apply the attachment [trac_7784-sagenb_spkg_files.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7784/trac_7784-sagenb_spkg_files.patch) to [sagenb-0.7.2.spkg](http://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.2.spkg) under the directory `sagenb-0.7.2/src/sagenb`.



---

archive/issue_comments_067139.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-02T23:26:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67139",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067140.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-03T02:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7784#issuecomment-67140",
    "user": "mpatel"
}
```

Resolution: fixed
