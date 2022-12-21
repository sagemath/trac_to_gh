# Issue 6429: [with patch; needs review] sagedoc: make search_src and friends less OS dependent

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-06-27 03:34:20

Assignee: jhpalmieri

CC:  ddrake craigcitro

As discussed in [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/603e2b5337993fc6?tvc=2) on sage-devel, the search_src, search_doc, and search_def functions use the unix 'find' command, and since there are different versions of the command which take incompatible arguments, there are problems with those functions.  The attached patch reworks all of these to use pure Python rather than 'find'.  It might be a little slower, but it should be more robust.

This patch also adds two new arguments to those functions.  From the docstring:

```
    - ``path_re`` (optional, default '') - regular expression which
      the filename (including the path) must match.

    - ``module`` (optional, default 'sage') - the module in which to
      search.  The default is 'sage', the entire Sage library.
```

(Actually, `module` doesn't make sense for search_doc, so it's not available there.)

For example:

```
search_src("matrix", module="sage.calculus")
```

with tab completion available as you type in "sage.calculus", or to accomplish essentially the same thing:

```
search_src("matrix", path_re="calc")
```



---

Comment by ddrake created at 2009-06-29 04:16:11

This looks good, but I do have two notes:

  * you should add yourself to the AUTHORS block, if nothing else so that anyone reading that doesn't think we are still using "find" for the `search_*` functions.
  * I thought it might be nice if the output included the line numbers where the match was found. I have a suggestion for how to do that which I am testing right now. If it seems to work, I'll upload a patch to do that.


---

Attachment

Okay, this new patch just adds my name to the AUTHORS block.  Line numbers would be nice -- good luck!


---

Comment by ddrake created at 2009-06-29 06:27:40

The trac server is not letting me upload patches, so you can get my line numbers patch from http://sage.math.washington.edu/home/drake/trac_6429_line_numbers.patch.

For the search functions, it includes line numbers just like "`grep -nH`":

```
combinat/yang_baxter_graph.py:530:    def __init__(self, partition):
```

with the line number between colons. For search_doc, this admittedly doesn't really make sense, but it does no harm to include it. When in the notebook, no line numbers are produced, since users will view the results with a web browser, and "jump to this line in the source code" is not a typical web browser feature. Fortunately, the `format_search_as_html` function worked without alteration. I did write up a way to include a list of line numbers in the notebook output, but since it's not so useful I ditched it.

With the line numbers, you could now automatically look up functions and docstrings; for example, in some kind of external editor, if you wanted functions related to set partitions, the editor could run

```
sage -c 'print search_def("partition", "set", interact=False)'
```

in a background shell, and then offer a menu with the resulting files, and be able to jump right to the correct location.

Your patch gets a positive review, although I've only tested it on sage.math and bsd.math (so, 64-bit Ubuntu and OS X 10.5)...but now that you're doing everything in Python, it's hard to see how this could fail on different platforms. (Famous last words?)  What do you think of the line numbers patch?


---

Attachment


---

Comment by ddrake created at 2009-06-29 23:51:40

Okay, trac was restarted and now the patch is available here.


---

Attachment

> What do you think of the line numbers patch?

Looks good except that line numbers are indexed starting at 0, and I think the first line of a file should be line 1, not line 0.  I've added a referee's patch to fix this.

Apply all three patches in this order: sagedoc_6429.patch, trac_6429_line_numbers.patch, trac_6429_ref.patch.


---

Comment by jhpalmieri created at 2009-06-30 16:08:10

Some timings (on an Intel iMac running OS X 10.5):

Before the patch:

```
sage: time s = search_src('matrix', interact=False)
CPU times: user 1.54 s, sys: 2.46 s, total: 4.00 s
Wall time: 4.50 s
```

After the patch:

```
sage: time s = search_src('matrix', interact=False)
CPU times: user 2.15 s, sys: 0.16 s, total: 2.31 s
Wall time: 2.31 s
```


On sage.math, it's also faster after the patch, but not by quite the same margin: Wall time 2.03 s before the patch, 1.42 s after.


---

Comment by ddrake created at 2009-06-30 23:54:34

I am working on some timings, but thanks for noting that the line numbers are off by one. Both vim and emacs start lines numbers from 1, so that seems like the proper thing to do.


---

Comment by ddrake created at 2009-07-01 07:26:32

Regarding testing, on an older machine that I tested, I saw a speedup similar to what you saw on sage.math -- nothing dramatic, but definitely faster. Nice work! 

(And to think, at #5806, I thought I should use find and grep because that would be faster than a pure Python solution...!)


---

Comment by rlm created at 2009-07-02 20:20:37

Resolution: fixed
