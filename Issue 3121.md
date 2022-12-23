# Issue 3121: @interact grid control

Issue created by migration from https://trac.sagemath.org/ticket/3121

Original creator: jason

Original creation time: 2008-05-07 08:40:04

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




---

Comment by jason created at 2008-05-07 08:43:40

The current patch needs to be cleaned up and doctests fixed.  I'm putting it up so that people can play with it if they want and also to backup the work.  I plan to clean it up fairly soon.


---

Comment by jason created at 2008-05-07 12:01:21

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

Comment by was created at 2008-05-07 16:02:18

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

Comment by jason created at 2008-05-08 01:30:27

The patch has been updated to address all of William's comments and is ready to be reviewed again.


---

Comment by was created at 2008-05-08 15:53:05

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

Comment by was created at 2008-05-08 15:56:19

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

Comment by was created at 2008-05-08 16:17:26

Changing the once instance of svalue to value fixes points 1 and 3 above. 

Just add something to the docstring for interact? and this will be done.


---

Attachment

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

Comment by was created at 2008-05-11 02:54:30

this cleans up the docs a little bit and adds some consistency.  apply after the other patch


---

Attachment

I'm OK with this if Jason is ok with sage-3121-part2_doc.patch


---

Comment by jason created at 2008-05-11 03:09:36

Looks good to me.  William's patch also fixes a few other unrelated documentation things with interact.


---

Comment by mabshoff created at 2008-05-11 09:59:38

Resolution: fixed


---

Comment by mabshoff created at 2008-05-11 09:59:38

Merged both patches in Sage 3.0.2.alpha0
