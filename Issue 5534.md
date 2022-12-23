# Issue 5534: sage.combinat.subword.smallest_positions modifying its input

Issue created by migration from https://trac.sagemath.org/ticket/5534

Original creator: nthiery

Original creation time: 2009-03-16 20:46:13

Assignee: mhansen

CC:  sage-combinat

I came across this function in Sage-Combinat,

sage.combinat.subword.smallest_positions(word, subword, pos=0)

Running this function not only returns the positions in "word" where
"subword" occurs, but it modifies "subword" to be this sequence of
positions.  Is there a reason for this?  It seems to me that it should
leave "subword" unchanged, but maybe I'm not thinking of something.

sage: w = ["a", "b", "c", "d"]
sage: ww = ["b", "d"]
sage: sage.combinat.subword.smallest_positions?
sage: sage.combinat.subword.smallest_positions(w, ww)
[1, 3]
sage: w
['a', 'b', 'c', 'd']
sage: ww
[1, 3]

Thanks,
Steve


---

Comment by hivert created at 2009-03-17 09:59:47

Fixed (see the attached patch):

Now:

```
sage: w = ["a", "b", "c", "d"]
sage: ww = ["b", "d"]
sage: sage.combinat.subword.smallest_positions(w, ww)
[1, 3]
sage: w
['a', 'b', 'c', 'd']
sage: ww
['b', 'd']
```


Note the patch only applies on top of #5200

Author : Florent Hivert


---

Comment by hivert created at 2009-03-17 09:59:47

Changing assignee from mhansen to hivert.


---

Comment by hivert created at 2009-03-19 17:00:50

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-03-25 07:01:50

This patch causes doctest failures in 

```
	sage -t -long devel/sage/sage/combinat/subword.py # 23 doctests failed
	sage -t -long devel/sage/sage/combinat/subset.py # 10 doctests failed
```

For example"

```
sage -t -long "devel/sage/sage/combinat/subset.py"          
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/combinat/subset.py", line 566:
    sage: [] in S
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_25[3]>", line 1, in <module>
        [] in S###line 566:
    sage: [] in S
      File "/scratch/mabshoff/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/subset.py", line 579, in __contains__
        return sorted(s) in subword.Subwords(self._s)
      File "/scratch/mabshoff/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/subword.py", line 130, in __contains__
        if smallest_positions(self.w, w) != False:
      File "/scratch/mabshoff/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/combinat/subword.py", line 315, in smallest_positions
        res = [None] * subword.length()
    AttributeError: 'list' object has no attribute 'length'
**********************************************************************
```


This is with #5200 merged, so is there another dependency?

Cheers,

Michael


---

Attachment


---

Comment by hivert created at 2009-03-28 18:47:43

Oups !!! It looks like Nicolas last review requirement was simply syntactically wrong. He required to write
`res = [None] * subword.length()` where he meant  `res = [None] * len(subword)`. The bad think is that no one of use take care to even launch the tests. Shame on us !!!

The re-sumbmitted patch should work. 

Cheers,

Florent


---

Comment by mabshoff created at 2009-04-03 00:57:17

Resolution: fixed


---

Comment by mabshoff created at 2009-04-03 00:57:17

Merged in Sage 3.4.1.rc0.

Cheers,

Michael
