# Issue 1017: [with (partial) patch] add an option to solve to return a list of dictionaries instead of a list of lists of equations.

archive/issues_001017.json:
```json
{
    "body": "Assignee: @williamstein\n\nIt's terribly convenient to be able to write:\n\n```\nsolutions=solve([x^2+y^2 == 1, y^2 == x^3 + x + 1], x, y, solution_dict=True);\nfor solution in solutions: \n    print solution[x].n(digits=3), \",\", solution[y].n(digits=3)\n```\n\n\nto print out a list of the solutions or to refer back to the solved values.  This patch implements a naive approach to solution_dict.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1017\n\n",
    "created_at": "2007-10-28T04:02:22Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.10",
    "title": "[with (partial) patch] add an option to solve to return a list of dictionaries instead of a list of lists of equations.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1017",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

It's terribly convenient to be able to write:

```
solutions=solve([x^2+y^2 == 1, y^2 == x^3 + x + 1], x, y, solution_dict=True);
for solution in solutions: 
    print solution[x].n(digits=3), ",", solution[y].n(digits=3)
```


to print out a list of the solutions or to refer back to the solved values.  This patch implements a naive approach to solution_dict.



Issue created by migration from https://trac.sagemath.org/ticket/1017





---

archive/issue_comments_006219.json:
```json
{
    "body": "Attachment [solution_dict.patch](tarball://root/attachments/some-uuid/ticket1017/solution_dict.patch) by @jasongrout created at 2007-10-28 04:08:43\n\npatch is no longer a partial patch.\n\nI just noticed one modification.\n\n\n```\nsol_list_dict=blah\nreturn sol_list_dict\n```\n\ncould be shortened to\n\n```\nreturn blah\n```\n",
    "created_at": "2007-10-28T04:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1017#issuecomment-6219",
    "user": "https://github.com/jasongrout"
}
```

Attachment [solution_dict.patch](tarball://root/attachments/some-uuid/ticket1017/solution_dict.patch) by @jasongrout created at 2007-10-28 04:08:43

patch is no longer a partial patch.

I just noticed one modification.


```
sol_list_dict=blah
return sol_list_dict
```

could be shortened to

```
return blah
```




---

archive/issue_comments_006220.json:
```json
{
    "body": "I meant, in the last part of the patch:\n\n\n```\nsol_dict=blah\nreturn sol_dict\n```\n\ncould be shortened to\n\n```\nreturn blah\n```\n",
    "created_at": "2007-10-28T04:10:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1017#issuecomment-6220",
    "user": "https://github.com/jasongrout"
}
```

I meant, in the last part of the patch:


```
sol_dict=blah
return sol_dict
```

could be shortened to

```
return blah
```




---

archive/issue_comments_006221.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-28T18:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1017#issuecomment-6221",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: fixed



---

archive/issue_events_001141.json:
```json
{
    "actor": "cwitty",
    "created_at": "2007-10-28T18:38:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1017",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1017#event-1141"
}
```
