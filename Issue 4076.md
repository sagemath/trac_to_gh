# Issue 4076: notebook -- <$> ... </$> and <$$> ... </$$> don't work in the notebook as the help page claims

archive/issues_004076.json:
```json
{
    "body": "Assignee: boothby\n\nHelp page claims:\n\n```\nBegin an input block with %html and it will be output as HTML. Use the <sage>...</sage> tag to do computations in an HTML block and have the typeset output inserted. Use <$>...</$> and <$$>...</$$> to insert typeset math in the HTML block. This does not require latex.\n```\n\n\n\nThe html function clearly doesn't properly deal with the < and >. \n\n```\nsage: html(r'let <$>K = \\mathbb{Q} 17 (\\sqrt{-2})</$>')\n<html><font color='black'>let <<span class=\"math\">>K = \\mathbb{Q} 17 (\\sqrt{-2})</</span>></font></html>\n\nsage: html(r'let <$$>K = \\mathbb{Q} 17 (\\sqrt{-2})</$$>')\n<html><font color='black'>let <<div class=\"math\">>K = \\mathbb{Q} 17 (\\sqrt{-2})</</div>></font></html>\n```\n\n\nThe output should be the same as \n\n```\nsage: html(r'let $K = \\mathbb{Q} 17 (\\sqrt{-2})$')\n<html><font color='black'>let <span class=\"math\">K = \\mathbb{Q} 17 (\\sqrt{-2})</span></font></html>\n\nsage: html(r'let $$K = \\mathbb{Q} 17 (\\sqrt{-2})$$')\n<html><font color='black'>let <div class=\"math\">K = \\mathbb{Q} 17 (\\sqrt{-2})</div></font></html>\n```\n\n\nThis is based on the bug report given on 8/25/08 by john.perry`@`usm.edu available at http://spreadsheets.google.com/pub?key=pCwvGVwSMxTzT6E2xNdo5fA\n\nIssue created by migration from https://trac.sagemath.org/ticket/4076\n\n",
    "created_at": "2008-09-08T12:38:54Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- <$> ... </$> and <$$> ... </$$> don't work in the notebook as the help page claims",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4076",
    "user": "TimothyClemans"
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

archive/issue_comments_029415.json:
```json
{
    "body": "Attachment [sage-4076_1.patch](tarball://root/attachments/some-uuid/ticket4076/sage-4076_1.patch) by TimothyClemans created at 2008-09-08 13:27:15",
    "created_at": "2008-09-08T13:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29415",
    "user": "TimothyClemans"
}
```

Attachment [sage-4076_1.patch](tarball://root/attachments/some-uuid/ticket4076/sage-4076_1.patch) by TimothyClemans created at 2008-09-08 13:27:15



---

archive/issue_comments_029416.json:
```json
{
    "body": "Isn't the right fix to correct the documentation instead?  I don't see why we'd want to support <$>, etc.",
    "created_at": "2008-09-08T14:10:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29416",
    "user": "mhansen"
}
```

Isn't the right fix to correct the documentation instead?  I don't see why we'd want to support <$>, etc.



---

archive/issue_comments_029417.json:
```json
{
    "body": "I thought about that doing that, but decided to be back compatible with old documentation.",
    "created_at": "2008-09-08T18:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29417",
    "user": "TimothyClemans"
}
```

I thought about that doing that, but decided to be back compatible with old documentation.



---

archive/issue_comments_029418.json:
```json
{
    "body": "I think the documentation fix is the correct one since there's no real reason to support <$> and <$$> and it's just more cruft to carry around.",
    "created_at": "2008-09-09T01:41:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29418",
    "user": "mhansen"
}
```

I think the documentation fix is the correct one since there's no real reason to support <$> and <$$> and it's just more cruft to carry around.



---

archive/issue_comments_029419.json:
```json
{
    "body": "Attachment [sage-4076_2.patch](tarball://root/attachments/some-uuid/ticket4076/sage-4076_2.patch) by TimothyClemans created at 2008-09-09 14:03:47\n\nPatch sage-4076_2.patch fixes the documentation.",
    "created_at": "2008-09-09T14:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29419",
    "user": "TimothyClemans"
}
```

Attachment [sage-4076_2.patch](tarball://root/attachments/some-uuid/ticket4076/sage-4076_2.patch) by TimothyClemans created at 2008-09-09 14:03:47

Patch sage-4076_2.patch fixes the documentation.



---

archive/issue_comments_029420.json:
```json
{
    "body": "I'm confused; am I just supposed to use sage-4076_2.patch and ignore sage-4076_1.patch?  If so, this gets a positive review -- it's a simple change to the notebook help page.",
    "created_at": "2008-10-17T23:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29420",
    "user": "jhpalmieri"
}
```

I'm confused; am I just supposed to use sage-4076_2.patch and ignore sage-4076_1.patch?  If so, this gets a positive review -- it's a simple change to the notebook help page.



---

archive/issue_comments_029421.json:
```json
{
    "body": "I'm giving **sage-4076_2.patch** a positive review; it should be merged.  As far as I can tell, **sage-4076_1.patch** is not needed, and should be discarded.",
    "created_at": "2008-10-24T17:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29421",
    "user": "jhpalmieri"
}
```

I'm giving **sage-4076_2.patch** a positive review; it should be merged.  As far as I can tell, **sage-4076_1.patch** is not needed, and should be discarded.



---

archive/issue_comments_029422.json:
```json
{
    "body": "I think sage-4076_1.patch is still needed. \n\nTimothy: can you comment?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T13:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29422",
    "user": "mabshoff"
}
```

I think sage-4076_1.patch is still needed. 

Timothy: can you comment?

Cheers,

Michael



---

archive/issue_comments_029423.json:
```json
{
    "body": "I don't think the first one is needed.",
    "created_at": "2008-10-26T18:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29423",
    "user": "TimothyClemans"
}
```

I don't think the first one is needed.



---

archive/issue_comments_029424.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-27T02:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29424",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha1



---

archive/issue_comments_029425.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-27T02:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4076#issuecomment-29425",
    "user": "mabshoff"
}
```

Resolution: fixed
