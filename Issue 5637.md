# Issue 5637: [with patch, needs review] allow \[ and \] to delimit math in %html blocks

archive/issues_005637.json:
```json
{
    "body": "Assignee: boothby\n\nWithout the patch,\n\n```\n%html\ntest\n\\[ x^2 \\]\n```\n\nis not typeset with `x^2` in math mode.  With the patch, the above is treated just like \n\n```\n%html\ntest\n$$ x^2 $$\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5637\n\n",
    "created_at": "2009-03-30T00:57:53Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch, needs review] allow \\[ and \\] to delimit math in %html blocks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5637",
    "user": "jhpalmieri"
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

archive/issue_comments_044021.json:
```json
{
    "body": "Attachment [html-math-delimiters.patch](tarball://root/attachments/some-uuid/ticket5637/html-math-delimiters.patch) by jhpalmieri created at 2009-03-30 00:58:05",
    "created_at": "2009-03-30T00:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5637#issuecomment-44021",
    "user": "jhpalmieri"
}
```

Attachment [html-math-delimiters.patch](tarball://root/attachments/some-uuid/ticket5637/html-math-delimiters.patch) by jhpalmieri created at 2009-03-30 00:58:05



---

archive/issue_comments_044022.json:
```json
{
    "body": "Changing assignee from boothby to jhpalmieri.",
    "created_at": "2009-03-30T01:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5637#issuecomment-44022",
    "user": "jhpalmieri"
}
```

Changing assignee from boothby to jhpalmieri.



---

archive/issue_comments_044023.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-30T01:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5637#issuecomment-44023",
    "user": "jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044024.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-06-15T19:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5637#issuecomment-44024",
    "user": "ncalexan"
}
```

Looks good to me.



---

archive/issue_comments_044025.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T10:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5637#issuecomment-44025",
    "user": "rlm"
}
```

Resolution: fixed
