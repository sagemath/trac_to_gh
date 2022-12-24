# Issue 2894: notebook -- cache elements to improve the speed of get_cell()

archive/issues_002894.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe following code takes .004ms/call, which is about 5 times faster than the existing get_cell():\n\n\n```\nvar cell_element_cache = [];\nfunction get_cell2(id) {\n    var v = cell_element[id];\n    if(v == undefined)\n        v = cell_element[id] = get_cell(id)\n    return v;\n}\n```\n\n\nIt follows that we should update get_cell to the 5-times faster version, since get_cell is called  quite frequently in the notebook code.\n\nas tested with\n\n\n```\nvar t0;\nvar e;\nvar n = cell_id_list[cell_id_list.length-1];\nvar N = 100000.;\nt0 = time_now();\nfor(i=0;i<N;i++)\n   e = get_cell(n);\nt1 = time_now();\nalert((t1-t0)/N);\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2894\n\n",
    "created_at": "2008-04-12T07:51:42Z",
    "labels": [
        "Cygwin",
        "major",
        "bug"
    ],
    "title": "notebook -- cache elements to improve the speed of get_cell()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2894",
    "user": "boothby"
}
```
Assignee: mabshoff

The following code takes .004ms/call, which is about 5 times faster than the existing get_cell():


```
var cell_element_cache = [];
function get_cell2(id) {
    var v = cell_element[id];
    if(v == undefined)
        v = cell_element[id] = get_cell(id)
    return v;
}
```


It follows that we should update get_cell to the 5-times faster version, since get_cell is called  quite frequently in the notebook code.

as tested with


```
var t0;
var e;
var n = cell_id_list[cell_id_list.length-1];
var N = 100000.;
t0 = time_now();
for(i=0;i<N;i++)
   e = get_cell(n);
t1 = time_now();
alert((t1-t0)/N);
```


Issue created by migration from https://trac.sagemath.org/ticket/2894





---

archive/issue_comments_019904.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-04-12T07:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19904",
    "user": "boothby"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_019905.json:
```json
{
    "body": "Changing component from Cygwin to notebook.",
    "created_at": "2008-04-12T07:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19905",
    "user": "boothby"
}
```

Changing component from Cygwin to notebook.



---

archive/issue_comments_019906.json:
```json
{
    "body": "Changing assignee from mabshoff to boothby.",
    "created_at": "2008-04-12T07:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19906",
    "user": "boothby"
}
```

Changing assignee from mabshoff to boothby.



---

archive/issue_comments_019907.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-04-12T07:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19907",
    "user": "boothby"
}
```

Changing priority from major to minor.



---

archive/issue_comments_019908.json:
```json
{
    "body": "Attachment [2894-notebookperformance.patch](tarball://root/attachments/some-uuid/ticket2894/2894-notebookperformance.patch) by boothby created at 2008-04-12 07:55:26",
    "created_at": "2008-04-12T07:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19908",
    "user": "boothby"
}
```

Attachment [2894-notebookperformance.patch](tarball://root/attachments/some-uuid/ticket2894/2894-notebookperformance.patch) by boothby created at 2008-04-12 07:55:26



---

archive/issue_comments_019909.json:
```json
{
    "body": "Hi Tom,\n\nthis patch is identical to #2887 where William posted your code except for the added comment by you. Since #2887 has been credited to you I will merge the extra comment and close this as fixed.\n\nThought?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-12T12:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19909",
    "user": "mabshoff"
}
```

Hi Tom,

this patch is identical to #2887 where William posted your code except for the added comment by you. Since #2887 has been credited to you I will merge the extra comment and close this as fixed.

Thought?

Cheers,

Michael



---

archive/issue_comments_019910.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-12T12:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19910",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019911.json:
```json
{
    "body": "Since #2887 was merged only merge the extra comment from the previous patch",
    "created_at": "2008-04-12T12:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19911",
    "user": "mabshoff"
}
```

Since #2887 was merged only merge the extra comment from the previous patch



---

archive/issue_comments_019912.json:
```json
{
    "body": "Attachment [trac_2887-comment-from-2894.patch](tarball://root/attachments/some-uuid/ticket2894/trac_2887-comment-from-2894.patch) by mabshoff created at 2008-04-12 12:51:23\n\nMerged trac_2887-comment-from-2894.patch in Sage 3.0.alpha4",
    "created_at": "2008-04-12T12:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19912",
    "user": "mabshoff"
}
```

Attachment [trac_2887-comment-from-2894.patch](tarball://root/attachments/some-uuid/ticket2894/trac_2887-comment-from-2894.patch) by mabshoff created at 2008-04-12 12:51:23

Merged trac_2887-comment-from-2894.patch in Sage 3.0.alpha4
