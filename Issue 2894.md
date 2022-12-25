# Issue 2894: [with patch, posititve] notebook -- cache elements to improve the speed of get_cell()

archive/issues_002894.json:
```json
{
    "body": "Assignee: boothby\n\nThe following code takes .004ms/call, which is about 5 times faster than the existing get_cell():\n\n```\nvar cell_element_cache = [];\nfunction get_cell2(id) {\n    var v = cell_element[id];\n    if(v == undefined)\n        v = cell_element[id] = get_cell(id)\n    return v;\n}\n```\n\nIt follows that we should update get_cell to the 5-times faster version, since get_cell is called  quite frequently in the notebook code.\n\nas tested with\n\n```\nvar t0;\nvar e;\nvar n = cell_id_list[cell_id_list.length-1];\nvar N = 100000.;\nt0 = time_now();\nfor(i=0;i<N;i++)\n   e = get_cell(n);\nt1 = time_now();\nalert((t1-t0)/N);\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2894\n\n",
    "closed_at": "2008-04-12T12:44:38Z",
    "created_at": "2008-04-12T07:51:42Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, posititve] notebook -- cache elements to improve the speed of get_cell()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2894",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: boothby

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

archive/issue_comments_019863.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-04-12T07:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19863",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_019864.json:
```json
{
    "body": "Changing component from Cygwin to notebook.",
    "created_at": "2008-04-12T07:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19864",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing component from Cygwin to notebook.



---

archive/issue_comments_019865.json:
```json
{
    "body": "Changing assignee from mabshoff to boothby.",
    "created_at": "2008-04-12T07:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19865",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing assignee from mabshoff to boothby.



---

archive/issue_comments_019866.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-04-12T07:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19866",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing priority from major to minor.



---

archive/issue_comments_019867.json:
```json
{
    "body": "Attachment [2894-notebookperformance.patch](tarball://root/attachments/some-uuid/ticket2894/2894-notebookperformance.patch) by boothby created at 2008-04-12 07:55:26",
    "created_at": "2008-04-12T07:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19867",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [2894-notebookperformance.patch](tarball://root/attachments/some-uuid/ticket2894/2894-notebookperformance.patch) by boothby created at 2008-04-12 07:55:26



---

archive/issue_events_006624.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-12T12:44:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2894#event-6624"
}
```



---

archive/issue_comments_019868.json:
```json
{
    "body": "Hi Tom,\n\nthis patch is identical to #2887 where William posted your code except for the added comment by you. Since #2887 has been credited to you I will merge the extra comment and close this as fixed.\n\nThought?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-12T12:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19868",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Tom,

this patch is identical to #2887 where William posted your code except for the added comment by you. Since #2887 has been credited to you I will merge the extra comment and close this as fixed.

Thought?

Cheers,

Michael



---

archive/issue_comments_019869.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-12T12:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19869",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006625.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-12T12:44:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2894#event-6625"
}
```



---

archive/issue_comments_019870.json:
```json
{
    "body": "Since #2887 was merged only merge the extra comment from the previous patch",
    "created_at": "2008-04-12T12:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19870",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Since #2887 was merged only merge the extra comment from the previous patch



---

archive/issue_comments_019871.json:
```json
{
    "body": "Attachment [trac_2887-comment-from-2894.patch](tarball://root/attachments/some-uuid/ticket2894/trac_2887-comment-from-2894.patch) by mabshoff created at 2008-04-12 12:51:23\n\nMerged trac_2887-comment-from-2894.patch in Sage 3.0.alpha4",
    "created_at": "2008-04-12T12:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2894",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2894#issuecomment-19871",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2887-comment-from-2894.patch](tarball://root/attachments/some-uuid/ticket2894/trac_2887-comment-from-2894.patch) by mabshoff created at 2008-04-12 12:51:23

Merged trac_2887-comment-from-2894.patch in Sage 3.0.alpha4
