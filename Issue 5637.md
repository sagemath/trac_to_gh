# Issue 5637: [with patch, needs review] allow \[ and \] to delimit math in %html blocks

archive/issues_005637.json:
```json
{
    "body": "Assignee: boothby\n\nWithout the patch,\n\n```\n%html\ntest\n\\[ x^2 \\]\n```\n\nis not typeset with `x^2` in math mode.  With the patch, the above is treated just like \n\n```\n%html\ntest\n$$ x^2 $$\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5637\n\n",
    "created_at": "2009-03-30T00:57:53Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch, needs review] allow \\[ and \\] to delimit math in %html blocks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5637",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: boothby

Without the patch,

```
%html
test
\[ x^2 \]
```

is not typeset with `x^2` in math mode.  With the patch, the above is treated just like 

```
%html
test
$$ x^2 $$
```



Issue created by migration from https://trac.sagemath.org/ticket/5637





---

archive/issue_comments_043936.json:
```json
{
    "body": "Attachment [html-math-delimiters.patch](tarball://root/attachments/some-uuid/ticket5637/html-math-delimiters.patch) by @jhpalmieri created at 2009-03-30 00:58:05",
    "created_at": "2009-03-30T00:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5637#issuecomment-43936",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [html-math-delimiters.patch](tarball://root/attachments/some-uuid/ticket5637/html-math-delimiters.patch) by @jhpalmieri created at 2009-03-30 00:58:05



---

archive/issue_comments_043937.json:
```json
{
    "body": "Changing assignee from boothby to @jhpalmieri.",
    "created_at": "2009-03-30T01:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5637#issuecomment-43937",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from boothby to @jhpalmieri.



---

archive/issue_comments_043938.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-30T01:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5637#issuecomment-43938",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043939.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-06-15T19:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5637#issuecomment-43939",
    "user": "https://github.com/ncalexan"
}
```

Looks good to me.



---

archive/issue_comments_043940.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T10:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5637#issuecomment-43940",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_005878.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-06-24T10:07:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5637",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5637#event-5878"
}
```
