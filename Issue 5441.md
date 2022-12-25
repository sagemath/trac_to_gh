# Issue 5441: preparser_ipython edit

archive/issues_005441.json:
```json
{
    "body": "Assignee: cwitty\n\nIn the function prepare_ipython, in the block:\n \n if interface_name == 'magma' and magma_colon_equals:\n\nI suggest changing:\n\nline = line.replace(':=','=').replace('=',':=')\n\nto\n\nline = line.replace('=',':=').replace('::=',':=').replace(':=:=','=')\n\nin sage/misc/preparser_ipython.py.\n\nThis will almost never be used (except by me), \nbut in principal allows one to write x == y to \nget a magma relation (x = y) while preserving \nthe hack (= -> :=). \n\nAlso, in the block:\n\nif interface_name in ['gap', 'magma', 'kash', 'singular']:\n\nI also suggest deleting the lines:\n\nif not line.endswith(';'):                          \n    line += ';'\n\nsince the call to interface.eval() should handle this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5441\n\n",
    "created_at": "2009-03-05T16:34:20Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "preparser_ipython edit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5441",
    "user": "https://trac.sagemath.org/admin/accounts/users/kohel"
}
```
Assignee: cwitty

In the function prepare_ipython, in the block:
 
 if interface_name == 'magma' and magma_colon_equals:

I suggest changing:

line = line.replace(':=','=').replace('=',':=')

to

line = line.replace('=',':=').replace('::=',':=').replace(':=:=','=')

in sage/misc/preparser_ipython.py.

This will almost never be used (except by me), 
but in principal allows one to write x == y to 
get a magma relation (x = y) while preserving 
the hack (= -> :=). 

Also, in the block:

if interface_name in ['gap', 'magma', 'kash', 'singular']:

I also suggest deleting the lines:

if not line.endswith(';'):                          
    line += ';'

since the call to interface.eval() should handle this.

Issue created by migration from https://trac.sagemath.org/ticket/5441


