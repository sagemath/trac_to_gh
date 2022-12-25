# Issue 4076: notebook -- <$> ... </$> and <$$> ... </$$> don't work in the notebook as the help page claims

archive/issues_004076.json:
```json
{
    "body": "Assignee: boothby\n\nHelp page claims:\n\n```\nBegin an input block with %html and it will be output as HTML. Use the <sage>...</sage> tag to do computations in an HTML block and have the typeset output inserted. Use <$>...</$> and <$$>...</$$> to insert typeset math in the HTML block. This does not require latex.\n```\n\n\n\nThe html function clearly doesn't properly deal with the < and >. \n\n```\nsage: html(r'let <$>K = \\mathbb{Q} 17 (\\sqrt{-2})</$>')\n<html><font color='black'>let <<span class=\"math\">>K = \\mathbb{Q} 17 (\\sqrt{-2})</</span>></font></html>\n\nsage: html(r'let <$$>K = \\mathbb{Q} 17 (\\sqrt{-2})</$$>')\n<html><font color='black'>let <<div class=\"math\">>K = \\mathbb{Q} 17 (\\sqrt{-2})</</div>></font></html>\n```\n\n\nThe output should be the same as \n\n```\nsage: html(r'let $K = \\mathbb{Q} 17 (\\sqrt{-2})$')\n<html><font color='black'>let <span class=\"math\">K = \\mathbb{Q} 17 (\\sqrt{-2})</span></font></html>\n\nsage: html(r'let $$K = \\mathbb{Q} 17 (\\sqrt{-2})$$')\n<html><font color='black'>let <div class=\"math\">K = \\mathbb{Q} 17 (\\sqrt{-2})</div></font></html>\n```\n\n\nThis is based on the bug report given on 8/25/08 by john.perry`@`usm.edu available at http://spreadsheets.google.com/pub?key=pCwvGVwSMxTzT6E2xNdo5fA\n\nIssue created by migration from https://trac.sagemath.org/ticket/4076\n\n",
    "created_at": "2008-09-08T12:38:54Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "notebook -- <$> ... </$> and <$$> ... </$$> don't work in the notebook as the help page claims",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4076",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: boothby

Help page claims:

```
Begin an input block with %html and it will be output as HTML. Use the <sage>...</sage> tag to do computations in an HTML block and have the typeset output inserted. Use <$>...</$> and <$$>...</$$> to insert typeset math in the HTML block. This does not require latex.
```



The html function clearly doesn't properly deal with the < and >. 

```
sage: html(r'let <$>K = \mathbb{Q} 17 (\sqrt{-2})</$>')
<html><font color='black'>let <<span class="math">>K = \mathbb{Q} 17 (\sqrt{-2})</</span>></font></html>

sage: html(r'let <$$>K = \mathbb{Q} 17 (\sqrt{-2})</$$>')
<html><font color='black'>let <<div class="math">>K = \mathbb{Q} 17 (\sqrt{-2})</</div>></font></html>
```


The output should be the same as 

```
sage: html(r'let $K = \mathbb{Q} 17 (\sqrt{-2})$')
<html><font color='black'>let <span class="math">K = \mathbb{Q} 17 (\sqrt{-2})</span></font></html>

sage: html(r'let $$K = \mathbb{Q} 17 (\sqrt{-2})$$')
<html><font color='black'>let <div class="math">K = \mathbb{Q} 17 (\sqrt{-2})</div></font></html>
```


This is based on the bug report given on 8/25/08 by john.perry`@`usm.edu available at http://spreadsheets.google.com/pub?key=pCwvGVwSMxTzT6E2xNdo5fA

Issue created by migration from https://trac.sagemath.org/ticket/4076





---

archive/issue_comments_029356.json:
```json
{
    "body": "Attachment [sage-4076_1.patch](tarball://root/attachments/some-uuid/ticket4076/sage-4076_1.patch) by TimothyClemans created at 2008-09-08 13:27:15",
    "created_at": "2008-09-08T13:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29356",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-4076_1.patch](tarball://root/attachments/some-uuid/ticket4076/sage-4076_1.patch) by TimothyClemans created at 2008-09-08 13:27:15



---

archive/issue_comments_029357.json:
```json
{
    "body": "Isn't the right fix to correct the documentation instead?  I don't see why we'd want to support <$>, etc.",
    "created_at": "2008-09-08T14:10:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29357",
    "user": "https://github.com/mwhansen"
}
```

Isn't the right fix to correct the documentation instead?  I don't see why we'd want to support <$>, etc.



---

archive/issue_comments_029358.json:
```json
{
    "body": "I thought about that doing that, but decided to be back compatible with old documentation.",
    "created_at": "2008-09-08T18:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29358",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I thought about that doing that, but decided to be back compatible with old documentation.



---

archive/issue_comments_029359.json:
```json
{
    "body": "I think the documentation fix is the correct one since there's no real reason to support <$> and <$$> and it's just more cruft to carry around.",
    "created_at": "2008-09-09T01:41:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29359",
    "user": "https://github.com/mwhansen"
}
```

I think the documentation fix is the correct one since there's no real reason to support <$> and <$$> and it's just more cruft to carry around.



---

archive/issue_comments_029360.json:
```json
{
    "body": "Attachment [sage-4076_2.patch](tarball://root/attachments/some-uuid/ticket4076/sage-4076_2.patch) by TimothyClemans created at 2008-09-09 14:03:47\n\nPatch sage-4076_2.patch fixes the documentation.",
    "created_at": "2008-09-09T14:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29360",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-4076_2.patch](tarball://root/attachments/some-uuid/ticket4076/sage-4076_2.patch) by TimothyClemans created at 2008-09-09 14:03:47

Patch sage-4076_2.patch fixes the documentation.



---

archive/issue_comments_029361.json:
```json
{
    "body": "I'm confused; am I just supposed to use sage-4076_2.patch and ignore sage-4076_1.patch?  If so, this gets a positive review -- it's a simple change to the notebook help page.",
    "created_at": "2008-10-17T23:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29361",
    "user": "https://github.com/jhpalmieri"
}
```

I'm confused; am I just supposed to use sage-4076_2.patch and ignore sage-4076_1.patch?  If so, this gets a positive review -- it's a simple change to the notebook help page.



---

archive/issue_comments_029362.json:
```json
{
    "body": "I'm giving **sage-4076_2.patch** a positive review; it should be merged.  As far as I can tell, **sage-4076_1.patch** is not needed, and should be discarded.",
    "created_at": "2008-10-24T17:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29362",
    "user": "https://github.com/jhpalmieri"
}
```

I'm giving **sage-4076_2.patch** a positive review; it should be merged.  As far as I can tell, **sage-4076_1.patch** is not needed, and should be discarded.



---

archive/issue_comments_029363.json:
```json
{
    "body": "I think sage-4076_1.patch is still needed. \n\nTimothy: can you comment?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T13:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29363",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I think sage-4076_1.patch is still needed. 

Timothy: can you comment?

Cheers,

Michael



---

archive/issue_comments_029364.json:
```json
{
    "body": "I don't think the first one is needed.",
    "created_at": "2008-10-26T18:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29364",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I don't think the first one is needed.



---

archive/issue_comments_029365.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-27T02:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29365",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha1



---

archive/issue_events_004314.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-10-27T02:11:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4076#event-4314"
}
```



---

archive/issue_comments_029366.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-27T02:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29366",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
