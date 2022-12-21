# Issue 4416: Sage 3.2.a2: optional doctest failure in sage/rings/arith.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-01 01:11:29

Assignee: mabshoff


```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ ./sage -t -long -optional devel/sage/sage/rings/arith.py
sage -t -long -optional devel/sage/sage/rings/arith.py      Traceback (most recent call last):
  File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/.doctest_arith.py", line 2453, in <module>
    globs=globals())
  File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1814, in testmod
    for test in finder.find(m, name, globs=globs, extraglobs=extraglobs):
  File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 839, in find
    self._find(tests, obj, name, module, source_lines, globs, {})
  File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 893, in _find
    globs, seen)
  File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 881, in _find
    test = self._get_test(obj, name, module, globs, source_lines)
  File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 965, in _get_test
    filename, lineno)
  File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 594, in get_doctest
    return DocTest(self.get_examples(string, name), globs,
  File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 608, in get_examples
    return [x for x in self.parse(string, name)
  File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 570, in parse
    self._parse_example(m, name, lineno)
  File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 640, in _parse_example
    lineno + len(source_lines))
  File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 726, in _check_prefix
    (lineno+i+1, name, line))
ValueError: line 51 of the docstring for __main__.example_2 has inconsistent leading whitespace: "    \\note{If $n>50000$ then algorithm = 'gp' is used instead of"

	 [2.3 s]
exit code: 1024
```



---

Comment by mabshoff created at 2008-11-01 01:11:47

Changing status from new to assigned.


---

Attachment


---

Comment by craigcitro created at 2008-11-01 22:54:32

Patch looks good. Probably also makes the docstring more readable ...


---

Comment by mabshoff created at 2008-11-02 00:48:22

Resolution: fixed


---

Comment by mabshoff created at 2008-11-02 00:48:22

Merged in Sage 3.2.alpha3
