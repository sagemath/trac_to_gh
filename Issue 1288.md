# Issue 1288: misformating of some of the reference manual in live version; also out of date

archive/issues_001288.json:
```json
{
    "body": "Assignee: tba\n\nSee below.  I suspect that the best solution is to remove this stuff about \"sage -advanced\" from the reference manual entirely, since it is always going to get out of date, hence be misleading.  It's much better to just described how \"sage -advanced\" works, and suggest that the user try it out, then improve the output of \"sage -advanced\". \n\n\n\n```\nReading 2.3 of the Reference Manual from the Notebook interface, I find that this \"live\" version has turned the lines:\n\n\\item\n\\verb+-advanced+ Lists additional options:\n\n\\begin{verbatim}\n$ sage -advanced\nin devel/doc-main/ref/options.tex into\n\n<li><code>-advanced</code> Lists additional options:\n\n<p>\n<div class=\"verbatim\"><pre><span class=\"math\"> sage -advanced\n\nin localhost:8000/doc/live/ref/node7.html , which, of course, completely wrecks the formatting.  There seems to be no problem with the pre-built  devel/doc-main/html/ref/node7.html , where latex2html has correctly turned the TeX into\n\n<LI><code>-advanced</code> Lists additional options:\n\n<P>\n<div class=\"verbatim\"><pre>\n$ sage -advanced\n\n\nMoreover, the list of options given in options.tex is considerably different from those currently produced by sage -advanced .\n\n\nMac OS X 10.4.11\nSage 2.8.14\n\n-- \n\nFrancis Clarke\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1288\n\n",
    "created_at": "2007-11-27T14:09:36Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "misformating of some of the reference manual in live version; also out of date",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1288",
    "user": "https://github.com/williamstein"
}
```
Assignee: tba

See below.  I suspect that the best solution is to remove this stuff about "sage -advanced" from the reference manual entirely, since it is always going to get out of date, hence be misleading.  It's much better to just described how "sage -advanced" works, and suggest that the user try it out, then improve the output of "sage -advanced". 



```
Reading 2.3 of the Reference Manual from the Notebook interface, I find that this "live" version has turned the lines:

\item
\verb+-advanced+ Lists additional options:

\begin{verbatim}
$ sage -advanced
in devel/doc-main/ref/options.tex into

<li><code>-advanced</code> Lists additional options:

<p>
<div class="verbatim"><pre><span class="math"> sage -advanced

in localhost:8000/doc/live/ref/node7.html , which, of course, completely wrecks the formatting.  There seems to be no problem with the pre-built  devel/doc-main/html/ref/node7.html , where latex2html has correctly turned the TeX into

<LI><code>-advanced</code> Lists additional options:

<P>
<div class="verbatim"><pre>
$ sage -advanced


Moreover, the list of options given in options.tex is considerably different from those currently produced by sage -advanced .


Mac OS X 10.4.11
Sage 2.8.14

-- 

Francis Clarke
```


Issue created by migration from https://trac.sagemath.org/ticket/1288





---

archive/issue_comments_008064.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T21:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1288#issuecomment-8064",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008065.json:
```json
{
    "body": "Changing assignee from tba to @mwhansen.",
    "created_at": "2007-12-06T21:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1288#issuecomment-8065",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from tba to @mwhansen.



---

archive/issue_events_003384.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2007-12-08T05:25:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1288",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1288#event-3384"
}
```



---

archive/issue_comments_008066.json:
```json
{
    "body": "Attachment [1288-doc.patch](tarball://root/attachments/some-uuid/ticket1288/1288-doc.patch) by @mwhansen created at 2007-12-08 05:25:22",
    "created_at": "2007-12-08T05:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1288#issuecomment-8066",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1288-doc.patch](tarball://root/attachments/some-uuid/ticket1288/1288-doc.patch) by @mwhansen created at 2007-12-08 05:25:22



---

archive/issue_comments_008067.json:
```json
{
    "body": "Looks good to me. Initially I was confused about this since it seemed to only remove content until I read William's comments.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-09T10:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1288#issuecomment-8067",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me. Initially I was confused about this since it seemed to only remove content until I read William's comments.

Cheers,

Michael



---

archive/issue_comments_008068.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-09T10:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1288#issuecomment-8068",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003385.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-09T10:40:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1288",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1288#event-3385"
}
```



---

archive/issue_comments_008069.json:
```json
{
    "body": "Merged in 2.9.alpha2.",
    "created_at": "2007-12-09T10:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1288#issuecomment-8069",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.alpha2.
