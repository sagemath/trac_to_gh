# Issue 1707: add Carlo Hamalainen latin square stuff to Sage

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-01-07 07:51:28

Assignee: was

CC:  sage-combinat




---

Comment by mhansen created at 2008-01-07 07:52:07

Changing type from defect to enhancement.


---

Comment by mhansen created at 2008-01-07 07:52:07

Changing status from new to assigned.


---

Comment by mhansen created at 2008-01-07 07:52:07

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-01-07 07:52:07

Changing priority from major to minor.


---

Comment by mhansen created at 2008-01-07 07:52:07

Changing component from algebraic geometry to combinatorics.


---

Comment by wdj created at 2008-03-16 12:27:00

I'm willing to review this but since the patch was created 2 months ago(?), I am not sure what version of SAGe to apply it against. Looks very interesting.


---

Comment by wdj created at 2008-03-16 13:10:58

I've looked at this more. This is not a patch at all but simply some SAGE code. A lot of this seems like good code but a lot is missing for this to be acceptable for inclusion in SAGE - missing docstrings and doctests, and I think some functions should be methods for a (yet to be created and designed) LatinSquare class. 
Suggestion: This could all go into a subdirectory of combinat called matrices, since there is a wide subfield of combinatorics which deals with matrices of various types (eg, latin squares, Hadamard matrices, (0,1)-matrices, etc).


---

Comment by carlohamalainen created at 2008-03-21 07:52:33

Dancing links C++


---

Attachment

Dancing links C++ wrapper


---

Comment by carlohamalainen created at 2008-03-21 07:54:59

Updated latin squares code (lots of doctests), replaces latin.sage


---

Attachment

* The file dfs_latin.spyx can be removed, all functionality has been superseded by the C++ dancing links solver.

* Many doctests/docstrings added to latin.sage (see latin.2.sage attachment)


---

Comment by mabshoff created at 2008-03-21 08:38:16

Hi, 

I have deleted latin.sage and dfs_latin.spyx. As David did state earlier we now need to rename the files, add them to the build systems, add imports and finally turn this into a patch. Then hopefully somebody will review this quickly.

Anybody around who wants to help Carlo out?

Cheers,

Michael


---

Comment by wdj created at 2008-03-21 12:42:59

I can try to help in the beginning. However, I've forgotten how to add a new directory to the devel tree. Do you use hg_sage.add as well?


---

Comment by mabshoff created at 2008-03-21 12:47:26

Replying to [comment:7 wdj]:
> I can try to help in the beginning. However, I've forgotten how to add a new directory to the devel tree. Do you use hg_sage.add as well?

To the Sage repo? Just add it and add the new file to the repo. Somebody should add this to the development manual in case it isn't in there yet, i.e. "How do I add my code to the tree in case it is all new".

Cheers,

Michael


---

Attachment

patch against 2.11.alpha1, needs review


---

Comment by wdj created at 2008-03-23 19:18:16

This applies cleanly, but not not build without an addition to setup.py (in the top directory), since it adds a subdirectory "matrices" to combinat. With this change, it passes sage -testall, except for the plot.py failure (which has nothing to do with this patch).

I give this a positive review but leave some food for thought: In my opinion, at some point, possibly in a future version, some very minor changes to the docstring are worth considering:
1. "nauty?" should be replaced by "NICE?"
2. add REFERENCES section, with actual literature sources
3. allow base rings other than ZZ
4. discuss whether isotopism sould return a Permutation or a 
PermutationGroupElement with sage-devel


---

Comment by mhansen created at 2008-03-24 19:20:52

Hello,

I'll post a more in-depth review in awhile, but one thing that needs to be done is to make it so that doctests pass.

1) 'sage.combinat.matrices' has to be added in setup.py under 'sage.combinat.sf' (for example) so that Sage knows about the module.

2) All the doctests for functions which are not raised to the global namespace (via matrices.all) need to be explicitly imported in the doctest.  For example, "sage: from sage.combinat.matrices.latin import dlxcpp_find_completions".

--Mike


---

Attachment

Apply the last two patches: trac1707-combinat-matrices.patch and 1707-referee.patch


---

Comment by mabshoff created at 2008-03-25 14:33:09

Resolution: fixed


---

Comment by mabshoff created at 2008-03-25 14:33:09

Merged trac1707-combinat-matrices.patch and 1707-referee.patch in Sage 2.11.alpha2


---

Comment by gfurnish created at 2008-03-26 11:04:13

set file to C++ in pbuild


---

Attachment


---

Comment by mabshoff created at 2008-03-26 15:36:02

Merged trac_1707_pbuild.patch and trac_1707-dancing_links.pyx-doctestfix.patch in Sage 2.11.alpha2

Cheers,

Michael
