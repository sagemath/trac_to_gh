# Issue 5360: Redeading of #4927 convert sage.server.* docstrings to Sphinx

Issue created by migration from https://trac.sagemath.org/ticket/5360

Original creator: hivert

Original creation time: 2009-02-24 18:09:05

Assignee: tba

CC:  mhansen

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




---

Comment by mabshoff created at 2009-03-04 19:36:36

Is anybody working on a patch here?

Cheers,

Michael


---

Comment by mpatel created at 2009-08-10 10:08:04

After the merge of #5653, it seems that ```, ```, and ```` render properly in the notebook. Try, e.g.,

```
sage.server.notebook.worksheet.Worksheet.edit_save?
sage.server.notebook.worksheet.Worksheet.edit_text?
sage.server.notebook.notebook.Notebook.import_worksheet?
```



---

Attachment


---

Comment by mpatel created at 2009-08-10 13:51:52

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

Attachment

New version.  Apply only this patch.


---

Comment by mpatel created at 2009-08-10 13:59:44

Changing keywords from "sphinx transform." to "".


---

Comment by mpatel created at 2009-08-10 13:59:44

Changing priority from critical to major.


---

Comment by mpatel created at 2009-08-30 10:32:27

Ticket #6840 also affects `notebook.py` and has a similar goal.  Most of the changes here are in other files, so I could move part of v2 there.


---

Comment by mpatel created at 2009-08-30 18:03:45

Tim Dumol has kindly merged v2 with #6840's v1.  Please close this ticket when #6840 merges.


---

Comment by mvngu created at 2009-08-31 12:12:45

Closing this ticket as a duplicate of #6840.


---

Comment by mvngu created at 2009-08-31 12:12:45

Resolution: duplicate
