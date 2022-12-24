# Issue 2580: [with patch, needs review] Implement backends for graphs

archive/issues_002580.json:
```json
{
    "body": "Assignee: rlm\n\nThis abstracts the layer between NetworkX and Sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2580\n\n",
    "created_at": "2008-03-18T01:56:35Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Implement backends for graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2580",
    "user": "rlm"
}
```
Assignee: rlm

This abstracts the layer between NetworkX and Sage.

Issue created by migration from https://trac.sagemath.org/ticket/2580





---

archive/issue_comments_017648.json:
```json
{
    "body": "Attachment [2580-graph_backends.patch](tarball://root/attachments/some-uuid/ticket2580/2580-graph_backends.patch) by rlm created at 2008-03-18 02:00:07",
    "created_at": "2008-03-18T02:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2580#issuecomment-17648",
    "user": "rlm"
}
```

Attachment [2580-graph_backends.patch](tarball://root/attachments/some-uuid/ticket2580/2580-graph_backends.patch) by rlm created at 2008-03-18 02:00:07



---

archive/issue_comments_017649.json:
```json
{
    "body": "Attachment [2580-graph_backends_added_files.patch](tarball://root/attachments/some-uuid/ticket2580/2580-graph_backends_added_files.patch) by rlm created at 2008-03-18 02:01:14\n\nMake sure to apply both patches before building. :)",
    "created_at": "2008-03-18T02:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2580#issuecomment-17649",
    "user": "rlm"
}
```

Attachment [2580-graph_backends_added_files.patch](tarball://root/attachments/some-uuid/ticket2580/2580-graph_backends_added_files.patch) by rlm created at 2008-03-18 02:01:14

Make sure to apply both patches before building. :)



---

archive/issue_comments_017650.json:
```json
{
    "body": "Also,\n`./sage -t -long sage/graphs`\npasses all tests after these patches...",
    "created_at": "2008-03-18T02:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2580#issuecomment-17650",
    "user": "rlm"
}
```

Also,
`./sage -t -long sage/graphs`
passes all tests after these patches...



---

archive/issue_comments_017651.json:
```json
{
    "body": "Applies, passes tests, and looks good to me.  I'm not too concerned about the doctests in the new file.",
    "created_at": "2008-03-18T10:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2580#issuecomment-17651",
    "user": "mhansen"
}
```

Applies, passes tests, and looks good to me.  I'm not too concerned about the doctests in the new file.



---

archive/issue_comments_017652.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-18T11:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2580#issuecomment-17652",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017653.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-18T11:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2580#issuecomment-17653",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha0
