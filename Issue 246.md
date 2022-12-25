# Issue 246: height of a notebook cell

archive/issues_000246.json:
```json
{
    "body": "Assignee: boothby\n\nWhen I paste a huge string into a notebook cell, the height of the cell\ndoesn't increase appropriately and scrolling through the string using\nmy cursor and maneuvering the tiny scroll bar are painful.\n\nI was wondering if there is any way to increase the height of cells in the\nSAGE notebook. If the answer is negative, it should be a todo.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/246\n\n",
    "created_at": "2007-02-06T17:45:31Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "height of a notebook cell",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/246",
    "user": "https://trac.sagemath.org/admin/accounts/users/ifti"
}
```
Assignee: boothby

When I paste a huge string into a notebook cell, the height of the cell
doesn't increase appropriately and scrolling through the string using
my cursor and maneuvering the tiny scroll bar are painful.

I was wondering if there is any way to increase the height of cells in the
SAGE notebook. If the answer is negative, it should be a todo.


Issue created by migration from https://trac.sagemath.org/ticket/246





---

archive/issue_comments_001083.json:
```json
{
    "body": "It would be nice if I could type in the number of lines in the notebook of a cell text area. I'm finding that I want this now.\n\ncell.py\n\n```\n480 <textarea class=\"%s\" rows=%s cols=100000 columns=100000\n481 id = 'cell_input_%s'\n482 onKeyPress = 'return input_keypress(%s,event);'\n483 oninput = 'cell_input_resize(this);'\n484 onFocus = 'return cell_focus(%s)'\n485 onBlur = 'return cell_blur(%s)'\n486 >%s</textarea> \n```\n\n\nThere is a javascript app for this at http://www.peterbe.com/Changing-textarea-size.",
    "created_at": "2007-03-02T18:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/246#issuecomment-1083",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

It would be nice if I could type in the number of lines in the notebook of a cell text area. I'm finding that I want this now.

cell.py

```
480 <textarea class="%s" rows=%s cols=100000 columns=100000
481 id = 'cell_input_%s'
482 onKeyPress = 'return input_keypress(%s,event);'
483 oninput = 'cell_input_resize(this);'
484 onFocus = 'return cell_focus(%s)'
485 onBlur = 'return cell_blur(%s)'
486 >%s</textarea> 
```


There is a javascript app for this at http://www.peterbe.com/Changing-textarea-size.



---

archive/issue_comments_001084.json:
```json
{
    "body": "This ticket has been fixed based on the current behavior of the notebook since the cell doesn't scroll and instead wraps the text down to the next line.",
    "created_at": "2008-04-15T07:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/246#issuecomment-1084",
    "user": "https://github.com/mwhansen"
}
```

This ticket has been fixed based on the current behavior of the notebook since the cell doesn't scroll and instead wraps the text down to the next line.



---

archive/issue_events_000260.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-04-15T07:25:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/246",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/246#event-260"
}
```



---

archive/issue_comments_001085.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T07:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/246#issuecomment-1085",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
