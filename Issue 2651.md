# Issue 2651: rewrite matrix() constructor

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-03-22 22:58:36

Assignee: was

Currently the code in matrix() is pretty convoluted.  This patch is an attempt to make that code much more organized and make it easier to tackle adding features to matrix() and fixing bugs.

Additionally, this patch has quite a few more doctests testing corner casesof matrix().

I am going to run testall on this to make sure that it doesn't mess anything major up.  Right now it should pretty much be a drop-in replacement, except that some corner cases are handled more consistently.




---

Attachment


---

Comment by malb created at 2008-03-25 19:49:36

On [sage-devel] Jason wrote:
> More specifically, for sr.py, matrix() is called from lines 1775 and
> 1779 with a list of lists.  The code appears to flatten "l" into a flat
> list, but the flatten command on the preceding lines specifies to only
> flatten Vector_modn_dense things, so the list "l" is not flattened.

The attached patch `sr_matrix.patch` should fix that issue.


---

Comment by jason created at 2008-03-25 21:17:23

apply instead of previous matrix-refactor.patch patches


---

Attachment

matrix-refactor.3.patch is ready to be reviewed.  sr_matrix.patch should be also applied to fix lots of doctests since the new matrix() is a bit stricter on syntax.

There is an issue remaining with transform.pyx (line 44) calling matrix(3,1,elts), where elts is a list containing a RDF vector of 3 elements instead of elts being a list of 3 RDF numbers.  I'm opening another ticket for this bug.


---

Comment by jason created at 2008-03-25 21:26:45

The transform.pyx bug is now #2667.


---

Comment by jason created at 2008-03-25 21:29:20

One question I have for the patch: Should I be passing back ValueError when I do?  Or should it be TypeError or some other error?


---

Comment by rhinton created at 2008-03-26 17:02:42

This is a good change!

I'm no Python expert, but I like your choice of ValueError over TypeError.  I think the paragraph "The entries" in the INPUT: section could be revised a little to improve clarity.

In your example

```
sage: m=matrix(QQ,3,{(1,1): 2}); m; m.parent() 
[0 0]
[0 2]
[0 0]
...
```

I expected to see a 3x3 matrix.  Your other examples that have only one size input produce square matrices (particularly the empty-dict input argument!).  I'm not sure what the "right" behavior is, but I wanted to make sure you are.

I don't see any examples/tests of passing in a Sage object and using the _matrix_() attribute to get a matrix.


---

Comment by jason created at 2008-03-26 18:16:59

* the matrix(3,{(1,1): 2}) example is posted to sage-devel for a vote.
 * v=vector; matrix(v) is an example of passing a sage object.  We probably ought to have another one, maybe a graph?  Do you want to post a quick patch?

sage: g=graphs.CycleGraph(4)
sage: matrix(g)

or something like that, maybe?


---

Attachment

Apply on top of latest matrix-refactor.patch.  Contains doc rewording, extra doctest matrix(graph), redefines matrix(int,dict) according to sage-devel vote.


---

Comment by rlm created at 2008-03-29 01:11:13

Note:

Part of the end patches for this ticket should revert the second patch on #2597, since it is a quick fix.


---

Comment by rhinton created at 2008-03-29 05:00:35

Apply on top of other patches.  Fixes doctests that fail due to semantic change in call to matrix(int, dict).  (Semantic change voted +2, -0 on sage-devel.)


---

Attachment

Along with the patch for #2667, a "sage -t -long devel/sage/sage" passes with no failures for me.  I think this patch is ready as soon as someone can review my changes.


---

Comment by jason created at 2008-03-29 22:34:12

The patches above all apply cleanly and all doctests (-long) pass if the patch at #2667 is applied as well.  I positively review the additional patches (and mine too :).  Since rhinton positively reviewed the core patch, I'm going to change the title to positive review.


---

Attachment

Changes a comment to reflect current documentation.


---

Comment by jason created at 2008-03-31 14:19:06

To clarify, apply all the patches above in order and also apply the patch at #2667.


---

Comment by dfdeshom created at 2008-03-31 19:02:43

Patch looks good and passes doctests in sage 2.11. This rewrite was much needed!


---

Comment by mabshoff created at 2008-03-31 19:15:31

Resolution: fixed


---

Comment by mabshoff created at 2008-03-31 19:15:31

Merged all five patches in Sage 3.0.alpha0
