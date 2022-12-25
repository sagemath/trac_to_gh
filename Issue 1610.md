# Issue 1610: hg record / cherry picking -- add something to the programming guide

archive/issues_001610.json:
```json
{
    "body": "Assignee: tba\n\nThis tick will be *very* easy for somebody to close. \n\n\n```\n> I noticed that Mercurial 0.9.5 has a \"record\" extension that mimics the\n> darcs record functionality of interactively asking what changes you want\n> to commit out of a file.  I know there was discussion of this a while ago.\n>\n> Reference:\n>\n> http://www.selenic.com/pipermail/mercurial/2007-October/015150.html\n> under the New extensions heading.  See also\n> http://www.selenic.com/mercurial/wiki/index.cgi/RecordExtension\n>\n> Anyways, I'm just posting this as an FYI.  It might be nice to expose\n> this functionality to sage, if we haven't already.\n>\n\nCool!\n\nAnd, this is already in Sage.   Just put\n\n[extensions]\nrecord=\n\nin your .hgrc file, and do\n\n   hg record\n\nand you'll get to cherry pick.\n\nThis should be documented in the programming guide.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1610\n\n",
    "created_at": "2007-12-27T09:05:13Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "hg record / cherry picking -- add something to the programming guide",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1610",
    "user": "https://github.com/williamstein"
}
```
Assignee: tba

This tick will be *very* easy for somebody to close. 


```
> I noticed that Mercurial 0.9.5 has a "record" extension that mimics the
> darcs record functionality of interactively asking what changes you want
> to commit out of a file.  I know there was discussion of this a while ago.
>
> Reference:
>
> http://www.selenic.com/pipermail/mercurial/2007-October/015150.html
> under the New extensions heading.  See also
> http://www.selenic.com/mercurial/wiki/index.cgi/RecordExtension
>
> Anyways, I'm just posting this as an FYI.  It might be nice to expose
> this functionality to sage, if we haven't already.
>

Cool!

And, this is already in Sage.   Just put

[extensions]
record=

in your .hgrc file, and do

   hg record

and you'll get to cherry pick.

This should be documented in the programming guide.
```


Issue created by migration from https://trac.sagemath.org/ticket/1610





---

archive/issue_comments_010212.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-12-27T09:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1610#issuecomment-10212",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to minor.



---

archive/issue_comments_010213.json:
```json
{
    "body": "Ticket #8206 adds some pointers about \"hg record\". Maybe we could expand on that with the information here.",
    "created_at": "2010-02-09T03:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1610#issuecomment-10213",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Ticket #8206 adds some pointers about "hg record". Maybe we could expand on that with the information here.



---

archive/issue_comments_010214.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-09T04:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1610#issuecomment-10214",
    "user": "https://github.com/rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_010215.json:
```json
{
    "body": "Attachment [trac_1610_doc_cherry_picking.patch](tarball://root/attachments/some-uuid/ticket1610/trac_1610_doc_cherry_picking.patch) by @rbeezer created at 2010-02-09 04:51:20\n\nApply #8206 before applying the \"cherry picking\" patch.",
    "created_at": "2010-02-09T04:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1610#issuecomment-10215",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_1610_doc_cherry_picking.patch](tarball://root/attachments/some-uuid/ticket1610/trac_1610_doc_cherry_picking.patch) by @rbeezer created at 2010-02-09 04:51:20

Apply #8206 before applying the "cherry picking" patch.



---

archive/issue_comments_010216.json:
```json
{
    "body": "Looks good to me. The idea here is to provide pointers to *record as an advanced tool for patch management.",
    "created_at": "2010-02-14T15:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1610#issuecomment-10216",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Looks good to me. The idea here is to provide pointers to *record as an advanced tool for patch management.



---

archive/issue_comments_010217.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-14T15:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1610#issuecomment-10217",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_010218.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-15T03:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1610#issuecomment-10218",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_001769.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-15T03:45:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1610",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1610#event-1769"
}
```
