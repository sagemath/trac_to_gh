# Issue 240: in notebook when refresh browser or first get page cell update list isn't sent out with running cells

archive/issues_000240.json:
```json
{
    "body": "Assignee: boothby\n\nin notebook when refresh browser or first get page cell update list isn't sent out with running cells. This means that if cell x is in the middle of running, and you refresh your browser, it is *impossible* to see what cell x is outputing. \n\nHelena Verrill found this bug. \n\nIssue created by migration from https://trac.sagemath.org/ticket/240\n\n",
    "created_at": "2007-02-03T10:15:45Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "in notebook when refresh browser or first get page cell update list isn't sent out with running cells",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/240",
    "user": "was"
}
```
Assignee: boothby

in notebook when refresh browser or first get page cell update list isn't sent out with running cells. This means that if cell x is in the middle of running, and you refresh your browser, it is *impossible* to see what cell x is outputing. 

Helena Verrill found this bug. 

Issue created by migration from https://trac.sagemath.org/ticket/240





---

archive/issue_comments_001071.json:
```json
{
    "body": "\n```\nIt seems there are potentially a number of sources of the problem.\nAny ideas?     One hint is that if you comment out this line (1462 in js.py)\n \n         // active_cell_list = delete_from_array(active_cell_list, id);\n \nthen the problem mostly goes away.  Of course there are other problems then :-).\n \nAnyway, it seems as though the server is maybe returning 'd' when it shouldn't.\n }}}",
    "created_at": "2007-02-03T19:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/240#issuecomment-1071",
    "user": "was"
}
```


```
It seems there are potentially a number of sources of the problem.
Any ideas?     One hint is that if you comment out this line (1462 in js.py)
 
         // active_cell_list = delete_from_array(active_cell_list, id);
 
then the problem mostly goes away.  Of course there are other problems then :-).
 
Anyway, it seems as though the server is maybe returning 'd' when it shouldn't.
 }}}



---

archive/issue_comments_001072.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-19T02:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/240#issuecomment-1072",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_001073.json:
```json
{
    "body": "This is now fixed.",
    "created_at": "2007-08-19T02:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/240#issuecomment-1073",
    "user": "was"
}
```

This is now fixed.
