# Issue 2887: notebook -- greatly optimize by implementing a cached version of get_element

archive/issues_002887.json:
```json
{
    "body": "Assignee: boothby\n\nTom Boothby just did this and here's his code. \n\n```\nvar cell_element_cache = [];\nfunction get_cell2(id) {\n   var v = cell_element_cache[id];\n   if(v == undefined)\n       v = cell_element_cache[id] = get_cell(id)\n   return v;\n}\n\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2887\n\n",
    "created_at": "2008-04-12T00:20:11Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "notebook -- greatly optimize by implementing a cached version of get_element",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2887",
    "user": "@williamstein"
}
```
Assignee: boothby

Tom Boothby just did this and here's his code. 

```
var cell_element_cache = [];
function get_cell2(id) {
   var v = cell_element_cache[id];
   if(v == undefined)
       v = cell_element_cache[id] = get_cell(id)
   return v;
}

```



Issue created by migration from https://trac.sagemath.org/ticket/2887





---

archive/issue_comments_019854.json:
```json
{
    "body": "I saw benchmarks that show a 5 times speedup for something.  I don't know if\nthis will be user-visible, but it might be on some machines.  The code itself\nworks fine and looks good.  I say apply.",
    "created_at": "2008-04-12T04:00:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2887#issuecomment-19854",
    "user": "@williamstein"
}
```

I saw benchmarks that show a 5 times speedup for something.  I don't know if
this will be user-visible, but it might be on some machines.  The code itself
works fine and looks good.  I say apply.



---

archive/issue_comments_019855.json:
```json
{
    "body": "Attachment [sage-2887.patch](tarball://root/attachments/some-uuid/ticket2887/sage-2887.patch) by mabshoff created at 2008-04-12 09:58:26\n\nMerged in Sage 3.0.alpha4",
    "created_at": "2008-04-12T09:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2887#issuecomment-19855",
    "user": "mabshoff"
}
```

Attachment [sage-2887.patch](tarball://root/attachments/some-uuid/ticket2887/sage-2887.patch) by mabshoff created at 2008-04-12 09:58:26

Merged in Sage 3.0.alpha4



---

archive/issue_comments_019856.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-12T09:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2887#issuecomment-19856",
    "user": "mabshoff"
}
```

Resolution: fixed
