# Issue 3121: @interact grid control

archive/issues_003121.json:
```json
{
    "body": "Assignee: boothby\n\nMake a grid control for `@`interact\n\nWith the patch, this is possible:\n\n\n```\n@interact\ndef _(M=input_grid(3,3, default=identity_matrix(3).list(), input_type=MatrixSpace(RDF,3,3))):\n    decomp = M.SVD()\n    matrices=[latex(mat) for mat in [M,decomp[0],decomp[1],decomp[2].transpose()]]\n    print jsmath(\"%s=%s%s%s\"%(matrices[0], matrices[1], matrices[2], matrices[3]))\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3121\n\n",
    "created_at": "2008-05-07T08:40:04Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "@interact grid control",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3121",
    "user": "jason"
}
```
Assignee: boothby

Make a grid control for `@`interact

With the patch, this is possible:


```
@interact
def _(M=input_grid(3,3, default=identity_matrix(3).list(), input_type=MatrixSpace(RDF,3,3))):
    decomp = M.SVD()
    matrices=[latex(mat) for mat in [M,decomp[0],decomp[1],decomp[2].transpose()]]
    print jsmath("%s=%s%s%s"%(matrices[0], matrices[1], matrices[2], matrices[3]))
```



Issue created by migration from https://trac.sagemath.org/ticket/3121





---

archive/issue_comments_021617.json:
```json
{
    "body": "The current patch needs to be cleaned up and doctests fixed.  I'm putting it up so that people can play with it if they want and also to backup the work.  I plan to clean it up fairly soon.",
    "created_at": "2008-05-07T08:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3121#issuecomment-21617",
    "user": "jason"
}
```

The current patch needs to be cleaned up and doctests fixed.  I'm putting it up so that people can play with it if they want and also to backup the work.  I plan to clean it up fairly soon.



---

archive/issue_comments_021618.json:
```json
{
    "body": "With the updated patch, the following two examples work beautifully:\n\n\n```\n\n@interact\ndef _(v=input_grid(1,3,default=[[1,2,3]], to_value=lambda x: vector(flatten(x)), width=1),\nw=input_grid(1,3,default=[[1,0,3]], to_value=lambda x: vector(flatten(x)), width=1)):\n    print jsmath(\"%s \\cdot %s = %s\"%(latex(v), latex(w), latex(v*w)))\n\n\n```\n\n\n\n\n```\n@interact\ndef _(M=input_grid(3,3, default=identity_matrix(3).rows(), to_value=MatrixSpace(RDF,3,3))):\n    decomp = M.SVD()\n    matrices=[latex(mat) for mat in [M,decomp[0],decomp[1],decomp[2].transpose()]]\n    print jsmath(\"%s=%s%s%s\"%(matrices[0], matrices[1], matrices[2], matrices[3]))\n```\n",
    "created_at": "2008-05-07T12:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3121#issuecomment-21618",
    "user": "jason"
}
```

With the updated patch, the following two examples work beautifully:


```

@interact
def _(v=input_grid(1,3,default=[[1,2,3]], to_value=lambda x: vector(flatten(x)), width=1),
w=input_grid(1,3,default=[[1,0,3]], to_value=lambda x: vector(flatten(x)), width=1)):
    print jsmath("%s \cdot %s = %s"%(latex(v), latex(w), latex(v*w)))


```




```
@interact
def _(M=input_grid(3,3, default=identity_matrix(3).rows(), to_value=MatrixSpace(RDF,3,3))):
    decomp = M.SVD()
    matrices=[latex(mat) for mat in [M,decomp[0],decomp[1],decomp[2].transpose()]]
    print jsmath("%s=%s%s%s"%(matrices[0], matrices[1], matrices[2], matrices[3]))
```




---

archive/issue_comments_021619.json:
```json
{
    "body": "REFEREE REPORT:\n\nWow, this totally rocks!  Great work!\n\nSome minor comments.\n\n* the docstrings have sage.server.notebook.interact.input_grid( but should just have input_grid( since it is defined in all.py\n\n* The docstring for input_grid? should have an example that gets me going using input_grid, i.e., that actually uses interact.  Here's a nice example\n\n```\n@interact\ndef _(a = input_grid(2,2, default = [[1,7],[3,4]], label='M', width=10), \n      v = input_grid(2,1, default=[[1],[2]], label='v', width=10)):\n    m = matrix(a); v = matrix(v)\n    try: x = m\\v\n    except: x = \"(no solution)\"\n    html('$$%s %s = %s$$'%(latex(m), latex(x), latex(v)))\n```\n\n\n* I would like it if input_grid(2,2, default = [1,2,3,4]) worked, where the default gets filled into the input_grid in rows (just like in the matrix constructor). \n\n* In this docstring maybe use ... to omit some of the output?\n\n```\n\t            sage: sage.server.notebook.interact.InputGrid('M', 1,2).render() \n \t661\t            '<table><tr><td><input type=\\'text\\' value=\\'None\\' onchange=\\'interact(0, \"sage.server.notebook.interact.update(0, \\\\\"M\\\\\", 27, sage.server.notebook.interact.standard_b64decode(\\\\\"\"+encode64( \"[[\"+jQuery(this).parents(\"table\").eq(0).find(\"tr\").map(function(){return jQuery(this).find(\"input\").map(function() {return jQuery(this).val();}).get().join(\",\");}).get().join(\"],[\")+\"]]\" )+\"\\\\\"), globals())\")\\'></input></td><td><input type=\\'text\\' value=\\'None\\' onchange=\\'interact(0, \"sage.server.notebook.interact.update(0, \\\\\"M\\\\\", 27, sage.server.notebook.interact.standard_b64decode(\\\\\"\"+encode64( \"[[\"+jQuery(this).parents(\"table\").eq(0).find(\"tr\").map(function(){return jQuery(this).find(\"input\").map(function() {return jQuery(this).val();}).get().join(\",\");}).get().join(\"],[\")+\"]]\" )+\"\\\\\"), globals())\")\\'></input></td></tr></table>' \n```\n\n\n* I get one doctest failure:\n\n```\nteragon-2:sage-3.0.1 was$ ./sage -t devel/sage/sage/server/notebook/interact.py \nsage -t  devel/sage/sage/server/notebook/interact.py        **********************************************************************\nFile \"/Users/was/build/build/sage-3.0.1/tmp/interact.py\", line 660:\n    sage: sage.server.notebook.interact.InputGrid('M', 1,2).render()\nExpected:\n    '<table><tr><td><input type=\\'text\\' value=\\'None\\' onchange=\\'interact(0, \"sage.server.notebook.interact.update(0, \\\\\"M\\\\\", 27, sage.server.notebook.interact.standard_b64decode(\\\\\"\"+encode64( \"[[\"+jQuery(this).parents(\"table\").eq(0).find(\"tr\").map(function(){return jQuery(this).find(\"input\").map(function() {return jQuery(this).val();}).get().join(\",\");}).get().join(\"],[\")+\"]]\" )+\"\\\\\"), globals())\")\\'></input></td><td><input type=\\'text\\' value=\\'None\\' onchange=\\'interact(0, \"sage.server.notebook.interact.update(0, \\\\\"M\\\\\", 27, sage.server.notebook.interact.standard_b64decode(\\\\\"\"+encode64( \"[[\"+jQuery(this).parents(\"table\").eq(0).find(\"tr\").map(function(){return jQuery(this).find(\"input\").map(function() {return jQuery(this).val();}).get().join(\",\");}).get().join(\"],[\")+\"]]\" )+\"\\\\\"), globals())\")\\'></input></td></tr></table>'\nGot:\n    '<table><tr><td><input type=\\'text\\' value=\\'None\\' size=\\'None\\' onchange=\\'interact(0, \"sage.server.notebook.interact.update(0, \\\\\"M\\\\\", 27, sage.server.notebook.interact.standard_b64decode(\\\\\"\"+encode64( \"[[\"+jQuery(this).parents(\"table\").eq(0).find(\"tr\").map(function(){return jQuery(this).find(\"input\").map(function() {return jQuery(this).val();}).get().join(\",\");}).get().join(\"],[\")+\"]]\" )+\"\\\\\"), globals())\")\\'></input></td><td><input type=\\'text\\' value=\\'None\\' size=\\'None\\' onchange=\\'interact(0, \"sage.server.notebook.interact.update(0, \\\\\"M\\\\\", 27, sage.server.notebook.interact.standard_b64decode(\\\\\"\"+encode64( \"[[\"+jQuery(this).parents(\"table\").eq(0).find(\"tr\").map(function(){return jQuery(this).find(\"input\").map(function() {return jQuery(this).val();}).get().join(\",\");}).get().join(\"],[\")+\"]]\" )+\"\\\\\"), globals())\")\\'></input></td></tr></table>'\n**********************************************************************\n1 items had failures:\n   1 of   2 in __main__.example_36\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/was/build/build/sage-3.0.1/tmp/.doctest_interact.py\n\t [4.2 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  devel/sage/sage/server/notebook/interact.py\nTotal time for all tests: 4.2 seconds\nteragon-2:sage-3.0.1 was$ \n```\n",
    "created_at": "2008-05-07T16:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3121#issuecomment-21619",
    "user": "was"
}
```

REFEREE REPORT:

Wow, this totally rocks!  Great work!

Some minor comments.

* the docstrings have sage.server.notebook.interact.input_grid( but should just have input_grid( since it is defined in all.py

* The docstring for input_grid? should have an example that gets me going using input_grid, i.e., that actually uses interact.  Here's a nice example

```
@interact
def _(a = input_grid(2,2, default = [[1,7],[3,4]], label='M', width=10), 
      v = input_grid(2,1, default=[[1],[2]], label='v', width=10)):
    m = matrix(a); v = matrix(v)
    try: x = m\v
    except: x = "(no solution)"
    html('$$%s %s = %s$$'%(latex(m), latex(x), latex(v)))
```


* I would like it if input_grid(2,2, default = [1,2,3,4]) worked, where the default gets filled into the input_grid in rows (just like in the matrix constructor). 

* In this docstring maybe use ... to omit some of the output?

```
	            sage: sage.server.notebook.interact.InputGrid('M', 1,2).render() 
 	661	            '<table><tr><td><input type=\'text\' value=\'None\' onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"M\\", 27, sage.server.notebook.interact.standard_b64decode(\\""+encode64( "[["+jQuery(this).parents("table").eq(0).find("tr").map(function(){return jQuery(this).find("input").map(function() {return jQuery(this).val();}).get().join(",");}).get().join("],[")+"]]" )+"\\"), globals())")\'></input></td><td><input type=\'text\' value=\'None\' onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"M\\", 27, sage.server.notebook.interact.standard_b64decode(\\""+encode64( "[["+jQuery(this).parents("table").eq(0).find("tr").map(function(){return jQuery(this).find("input").map(function() {return jQuery(this).val();}).get().join(",");}).get().join("],[")+"]]" )+"\\"), globals())")\'></input></td></tr></table>' 
```


* I get one doctest failure:

```
teragon-2:sage-3.0.1 was$ ./sage -t devel/sage/sage/server/notebook/interact.py 
sage -t  devel/sage/sage/server/notebook/interact.py        **********************************************************************
File "/Users/was/build/build/sage-3.0.1/tmp/interact.py", line 660:
    sage: sage.server.notebook.interact.InputGrid('M', 1,2).render()
Expected:
    '<table><tr><td><input type=\'text\' value=\'None\' onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"M\\", 27, sage.server.notebook.interact.standard_b64decode(\\""+encode64( "[["+jQuery(this).parents("table").eq(0).find("tr").map(function(){return jQuery(this).find("input").map(function() {return jQuery(this).val();}).get().join(",");}).get().join("],[")+"]]" )+"\\"), globals())")\'></input></td><td><input type=\'text\' value=\'None\' onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"M\\", 27, sage.server.notebook.interact.standard_b64decode(\\""+encode64( "[["+jQuery(this).parents("table").eq(0).find("tr").map(function(){return jQuery(this).find("input").map(function() {return jQuery(this).val();}).get().join(",");}).get().join("],[")+"]]" )+"\\"), globals())")\'></input></td></tr></table>'
Got:
    '<table><tr><td><input type=\'text\' value=\'None\' size=\'None\' onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"M\\", 27, sage.server.notebook.interact.standard_b64decode(\\""+encode64( "[["+jQuery(this).parents("table").eq(0).find("tr").map(function(){return jQuery(this).find("input").map(function() {return jQuery(this).val();}).get().join(",");}).get().join("],[")+"]]" )+"\\"), globals())")\'></input></td><td><input type=\'text\' value=\'None\' size=\'None\' onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"M\\", 27, sage.server.notebook.interact.standard_b64decode(\\""+encode64( "[["+jQuery(this).parents("table").eq(0).find("tr").map(function(){return jQuery(this).find("input").map(function() {return jQuery(this).val();}).get().join(",");}).get().join("],[")+"]]" )+"\\"), globals())")\'></input></td></tr></table>'
**********************************************************************
1 items had failures:
   1 of   2 in __main__.example_36
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/was/build/build/sage-3.0.1/tmp/.doctest_interact.py
	 [4.2 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  devel/sage/sage/server/notebook/interact.py
Total time for all tests: 4.2 seconds
teragon-2:sage-3.0.1 was$ 
```




---

archive/issue_comments_021620.json:
```json
{
    "body": "The patch has been updated to address all of William's comments and is ready to be reviewed again.",
    "created_at": "2008-05-08T01:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3121#issuecomment-21620",
    "user": "jason"
}
```

The patch has been updated to address all of William's comments and is ready to be reviewed again.



---

archive/issue_comments_021621.json:
```json
{
    "body": "I tried the example:\n\n```\n@interact\ndef _(a = input_grid(2,2, default = [[1,7],[3,4]], label='M', width=10), \n      v = input_grid(2,1, default=[[1],[2]], label='v', width=10)):\n    m = matrix(a); v = matrix(v)\n    try: x = m\\v\n    except: x = \"(no solution)\"\n    html('$$%s %s = %s$$'%(latex(m), latex(x), latex(v)))\n```\n\nbut now the defaults in the input form are all empty instead of containing\nthe defaults.",
    "created_at": "2008-05-08T15:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3121#issuecomment-21621",
    "user": "was"
}
```

I tried the example:

```
@interact
def _(a = input_grid(2,2, default = [[1,7],[3,4]], label='M', width=10), 
      v = input_grid(2,1, default=[[1],[2]], label='v', width=10)):
    m = matrix(a); v = matrix(v)
    try: x = m\v
    except: x = "(no solution)"
    html('$$%s %s = %s$$'%(latex(m), latex(x), latex(v)))
```

but now the defaults in the input form are all empty instead of containing
the defaults.



---

archive/issue_comments_021622.json:
```json
{
    "body": "NEW RREFEREE EPORT:\n\n1. Fix the fact that the default inputs don't get filled in.\n\n2. The docstring for interact? should list input_grid along with all the other interact controls, and also include an example that uses input_grid.\n\n3. A doctest still fails:\n\n```\nsage -t  devel/sage/sage/server/notebook/interact.py        **********************************************************************\nFile \"/Users/was/build/build/sage-3.0.1/tmp/interact.py\", line 676:\n    sage: sage.server.notebook.interact.InputGrid('M', 1,2).render()\nExpected:\n    '<table><tr><td><input type=\\'text\\' value=\\'None\\' ...\nGot:\n    '<table><tr><td><input type=\\'text\\' svalue=\\'None\\' size=\\'4\\' onchange=\\'interact(0, \"sage.server.notebook.interact.update(0, \\\\\"M\\\\\", 27, sage.server.notebook.interact.standard_b64decode(\\\\\"\"+encode64( \"[[\"+jQuery(this).parents(\"table\").eq(0).find(\"tr\").map(function(){return jQuery(this).find(\"input\").map(function() {return jQuery(this).val();}).get().join(\",\");}).get().join(\"],[\")+\"]]\" )+\"\\\\\"), globals())\")\\'></input></td><td><input type=\\'text\\' svalue=\\'None\\' size=\\'4\\' onchange=\\'interact(0, \"sage.server.notebook.interact.update(0, \\\\\"M\\\\\", 27, sage.server.notebook.interact.standard_b64decode(\\\\\"\"+encode64( \"[[\"+jQuery(this).parents(\"table\").eq(0).find(\"tr\").map(function(){return jQuery(this).find(\"input\").map(function() {return jQuery(this).val();}).get().join(\",\");}).get().join(\"],[\")+\"]]\" )+\"\\\\\"), globals())\")\\'></input></td></tr></table>'\n**********************************************************************\n1 items had failures:\n   1 of   2 in __main__.example_36\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/was/build/build/sage-3.0.1/tmp/.doctest_interact.py\n\t [4.2 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  devel/sage/sage/server/notebook/interact.py\nTotal time for all tests: 4.2 seconds\n```\n",
    "created_at": "2008-05-08T15:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3121#issuecomment-21622",
    "user": "was"
}
```

NEW RREFEREE EPORT:

1. Fix the fact that the default inputs don't get filled in.

2. The docstring for interact? should list input_grid along with all the other interact controls, and also include an example that uses input_grid.

3. A doctest still fails:

```
sage -t  devel/sage/sage/server/notebook/interact.py        **********************************************************************
File "/Users/was/build/build/sage-3.0.1/tmp/interact.py", line 676:
    sage: sage.server.notebook.interact.InputGrid('M', 1,2).render()
Expected:
    '<table><tr><td><input type=\'text\' value=\'None\' ...
Got:
    '<table><tr><td><input type=\'text\' svalue=\'None\' size=\'4\' onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"M\\", 27, sage.server.notebook.interact.standard_b64decode(\\""+encode64( "[["+jQuery(this).parents("table").eq(0).find("tr").map(function(){return jQuery(this).find("input").map(function() {return jQuery(this).val();}).get().join(",");}).get().join("],[")+"]]" )+"\\"), globals())")\'></input></td><td><input type=\'text\' svalue=\'None\' size=\'4\' onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"M\\", 27, sage.server.notebook.interact.standard_b64decode(\\""+encode64( "[["+jQuery(this).parents("table").eq(0).find("tr").map(function(){return jQuery(this).find("input").map(function() {return jQuery(this).val();}).get().join(",");}).get().join("],[")+"]]" )+"\\"), globals())")\'></input></td></tr></table>'
**********************************************************************
1 items had failures:
   1 of   2 in __main__.example_36
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/was/build/build/sage-3.0.1/tmp/.doctest_interact.py
	 [4.2 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  devel/sage/sage/server/notebook/interact.py
Total time for all tests: 4.2 seconds
```




---

archive/issue_comments_021623.json:
```json
{
    "body": "Changing the once instance of svalue to value fixes points 1 and 3 above. \n\nJust add something to the docstring for interact? and this will be done.",
    "created_at": "2008-05-08T16:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3121#issuecomment-21623",
    "user": "was"
}
```

Changing the once instance of svalue to value fixes points 1 and 3 above. 

Just add something to the docstring for interact? and this will be done.



---

archive/issue_comments_021624.json:
```json
{
    "body": "Attachment [trac-3121-input-grid.patch](tarball://root/attachments/some-uuid/ticket3121/trac-3121-input-grid.patch) by jason created at 2008-05-09 19:50:23\n\nI updated the patch again; sorry about not catching that typo (I apparently forgot to run sage -b before testing the last patch).  \n\nI also added an is_Matrix check to the automatic controls, so something like:\n\n\n```\n@interact\ndef _(A=matrix(3,3)):\n    print A\n```\n\n\ncreates the appropriate input_grid control.  I made my example in interact? use that method.\n\nThere are two patches above.  They are identical and one can be deleted.",
    "created_at": "2008-05-09T19:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3121#issuecomment-21624",
    "user": "jason"
}
```

Attachment [trac-3121-input-grid.patch](tarball://root/attachments/some-uuid/ticket3121/trac-3121-input-grid.patch) by jason created at 2008-05-09 19:50:23

I updated the patch again; sorry about not catching that typo (I apparently forgot to run sage -b before testing the last patch).  

I also added an is_Matrix check to the automatic controls, so something like:


```
@interact
def _(A=matrix(3,3)):
    print A
```


creates the appropriate input_grid control.  I made my example in interact? use that method.

There are two patches above.  They are identical and one can be deleted.



---

archive/issue_comments_021625.json:
```json
{
    "body": "this cleans up the docs a little bit and adds some consistency.  apply after the other patch",
    "created_at": "2008-05-11T02:54:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3121#issuecomment-21625",
    "user": "was"
}
```

this cleans up the docs a little bit and adds some consistency.  apply after the other patch



---

archive/issue_comments_021626.json:
```json
{
    "body": "Attachment [sage-3121-part2_doc.patch](tarball://root/attachments/some-uuid/ticket3121/sage-3121-part2_doc.patch) by was created at 2008-05-11 02:54:59\n\nI'm OK with this if Jason is ok with sage-3121-part2_doc.patch",
    "created_at": "2008-05-11T02:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3121#issuecomment-21626",
    "user": "was"
}
```

Attachment [sage-3121-part2_doc.patch](tarball://root/attachments/some-uuid/ticket3121/sage-3121-part2_doc.patch) by was created at 2008-05-11 02:54:59

I'm OK with this if Jason is ok with sage-3121-part2_doc.patch



---

archive/issue_comments_021627.json:
```json
{
    "body": "Looks good to me.  William's patch also fixes a few other unrelated documentation things with interact.",
    "created_at": "2008-05-11T03:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3121#issuecomment-21627",
    "user": "jason"
}
```

Looks good to me.  William's patch also fixes a few other unrelated documentation things with interact.



---

archive/issue_comments_021628.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T09:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3121#issuecomment-21628",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021629.json:
```json
{
    "body": "Merged both patches in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T09:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3121#issuecomment-21629",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.0.2.alpha0
