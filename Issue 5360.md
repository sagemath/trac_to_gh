# Issue 5360: Redeading of #4927 convert sage.server.* docstrings to Sphinx

archive/issues_005360.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @mwhansen\n\nKeywords: sphinx transform.\n\n## File: sage/server/introspect.py\n\n* Some pairs of single quote are transformed to double quote\n\n```\n- sage: nb.add_user('Mark','password','',force=True) \n+ sage: nb.add_user('Mark','password',\",force=True)\n```\n\n```\n- sage: C = sage.server.notebook.cell.Cell(0, 'plot(sin(x),0,5)', '', W) \n+ sage: C = sage.server.notebook.cell.Cell(0, 'plot(sin(x),0,5)', \", W) \n```\nIt looks like a bad Idea...\n\nI probably miss some so that a systematic replace `,\",` by `,'',` should solve the problem.    \n\n\n* Also in edit_text. the transformation\n\n```\nReturns a plain-text version of the worksheet with \\{\\{\\{\\}\\}\\} wiki-formatting,\n```\ninto \n\n```\nReturns a plain-text version of the worksheet with `` \n```\nlooks suspicious to me. \n\n* function edit_save: lost ` {{{` }}}:\n\n```\nignore_ids -- bool (default: False); if True ignore all the \n              id's in the `` code block. \n```\nis now:\n\n```\n-  ``ignore_ids`` - bool (default: False); if True \n   ignore all the id's in the code block. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5360\n\n",
    "created_at": "2009-02-24T18:09:05Z",
    "labels": [
        "component: documentation",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Redeading of #4927 convert sage.server.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5360",
    "user": "https://github.com/hivert"
}
```
Assignee: tba

CC:  @mwhansen

Keywords: sphinx transform.

## File: sage/server/introspect.py

* Some pairs of single quote are transformed to double quote

```
- sage: nb.add_user('Mark','password','',force=True) 
+ sage: nb.add_user('Mark','password',",force=True)
```

```
- sage: C = sage.server.notebook.cell.Cell(0, 'plot(sin(x),0,5)', '', W) 
+ sage: C = sage.server.notebook.cell.Cell(0, 'plot(sin(x),0,5)', ", W) 
```
It looks like a bad Idea...

I probably miss some so that a systematic replace `,",` by `,'',` should solve the problem.    


* Also in edit_text. the transformation

```
Returns a plain-text version of the worksheet with \{\{\{\}\}\} wiki-formatting,
```
into 

```
Returns a plain-text version of the worksheet with `` 
```
looks suspicious to me. 

* function edit_save: lost ` {{{` }}}:

```
ignore_ids -- bool (default: False); if True ignore all the 
              id's in the `` code block. 
```
is now:

```
-  ``ignore_ids`` - bool (default: False); if True 
   ignore all the id's in the code block. 
```


Issue created by migration from https://trac.sagemath.org/ticket/5360





---

archive/issue_comments_041217.json:
```json
{
    "body": "Is anybody working on a patch here?\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T19:36:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5360#issuecomment-41217",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Is anybody working on a patch here?

Cheers,

Michael



---

archive/issue_comments_041218.json:
```json
{
    "body": "After the merge of #5653, it seems that ```, ```, and ```` render properly in the notebook. Try, e.g.,\n\n```\nsage.server.notebook.worksheet.Worksheet.edit_save?\nsage.server.notebook.worksheet.Worksheet.edit_text?\nsage.server.notebook.notebook.Notebook.import_worksheet?\n```",
    "created_at": "2009-08-10T10:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5360#issuecomment-41218",
    "user": "https://github.com/qed777"
}
```

After the merge of #5653, it seems that ```, ```, and ```` render properly in the notebook. Try, e.g.,

```
sage.server.notebook.worksheet.Worksheet.edit_save?
sage.server.notebook.worksheet.Worksheet.edit_text?
sage.server.notebook.notebook.Notebook.import_worksheet?
```



---

archive/issue_comments_041219.json:
```json
{
    "body": "Attachment [trac_5360-sage_server_docstrings.patch](tarball://root/attachments/some-uuid/ticket5360/trac_5360-sage_server_docstrings.patch) by @qed777 created at 2009-08-10 10:16:36",
    "created_at": "2009-08-10T10:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5360#issuecomment-41219",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_5360-sage_server_docstrings.patch](tarball://root/attachments/some-uuid/ticket5360/trac_5360-sage_server_docstrings.patch) by @qed777 created at 2009-08-10 10:16:36



---

archive/issue_comments_041220.json:
```json
{
    "body": "The attached patch\n* Converts `, \",` to `, '',` for in `sage.server.*` dosctrings.\n* Fixes the `ignore_ids` omission mentioned above.  I don't know if there are other instances of this problem.\n\nAre there other problems?  Actually, yes.  See the next patch, which\n\n* Adds a few modules to `notebook.rst`.\n* Cleans up `interact.py`'s docstrings so they display nicely in the reference manual and notebook.\n* Cleans up, e.g., `EXAMPLES:`, in a few other modules.\n* Edits some modules' title strings.\n\nFeel free to make further changes.",
    "created_at": "2009-08-10T13:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5360#issuecomment-41220",
    "user": "https://github.com/qed777"
}
```

The attached patch
* Converts `, ",` to `, '',` for in `sage.server.*` dosctrings.
* Fixes the `ignore_ids` omission mentioned above.  I don't know if there are other instances of this problem.

Are there other problems?  Actually, yes.  See the next patch, which

* Adds a few modules to `notebook.rst`.
* Cleans up `interact.py`'s docstrings so they display nicely in the reference manual and notebook.
* Cleans up, e.g., `EXAMPLES:`, in a few other modules.
* Edits some modules' title strings.

Feel free to make further changes.



---

archive/issue_comments_041221.json:
```json
{
    "body": "Attachment [trac_5360-sage_server_docstrings_v2.patch](tarball://root/attachments/some-uuid/ticket5360/trac_5360-sage_server_docstrings_v2.patch) by @qed777 created at 2009-08-10 13:58:45\n\nNew version.  Apply only this patch.",
    "created_at": "2009-08-10T13:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5360#issuecomment-41221",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_5360-sage_server_docstrings_v2.patch](tarball://root/attachments/some-uuid/ticket5360/trac_5360-sage_server_docstrings_v2.patch) by @qed777 created at 2009-08-10 13:58:45

New version.  Apply only this patch.



---

archive/issue_comments_041222.json:
```json
{
    "body": "Changing keywords from \"sphinx transform.\" to \"\".",
    "created_at": "2009-08-10T13:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5360#issuecomment-41222",
    "user": "https://github.com/qed777"
}
```

Changing keywords from "sphinx transform." to "".



---

archive/issue_comments_041223.json:
```json
{
    "body": "Ticket #6840 also affects `notebook.py` and has a similar goal.  Most of the changes here are in other files, so I could move part of v2 there.",
    "created_at": "2009-08-30T10:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5360#issuecomment-41223",
    "user": "https://github.com/qed777"
}
```

Ticket #6840 also affects `notebook.py` and has a similar goal.  Most of the changes here are in other files, so I could move part of v2 there.



---

archive/issue_comments_041224.json:
```json
{
    "body": "Tim Dumol has kindly merged v2 with #6840's v1.  Please close this ticket when #6840 merges.",
    "created_at": "2009-08-30T18:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5360#issuecomment-41224",
    "user": "https://github.com/qed777"
}
```

Tim Dumol has kindly merged v2 with #6840's v1.  Please close this ticket when #6840 merges.



---

archive/issue_events_012498.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-31T12:12:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5360",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5360#event-12498"
}
```



---

archive/issue_events_012499.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-31T12:12:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5360",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5360#event-12499"
}
```



---

archive/issue_comments_041225.json:
```json
{
    "body": "Closing this ticket as a duplicate of #6840.",
    "created_at": "2009-08-31T12:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5360#issuecomment-41225",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Closing this ticket as a duplicate of #6840.



---

archive/issue_comments_041226.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-08-31T12:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5360#issuecomment-41226",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate
