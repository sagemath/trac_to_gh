# Issue 3557: Preparser bug: doctest failes when "..." is first expected output

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-07-06 01:39:11

Assignee: was

With 

```
         EXAMPLES:
             sage: G = DirichletGroup(3) 
             sage: e = G.0
             sage: e.gauss_sum_numerical()
             ...e-16 + 1.7320508075...*I
```

the doctesting framework complains about:

```
sage -t -long devel/sage/sage/modular/dirichlet.py          Traceback (most recent call last):
  File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/.doctest_dirichlet.py", line 1206, in <module>
    globs=globals())
  File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 1814, in testmod
    for test in finder.find(m, name, globs=globs, extraglobs=extraglobs):
  File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 839, in find
    self._find(tests, obj, name, module, source_lines, globs, {})
  File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 893, in _find
    globs, seen)
  File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 881, in _find
    test = self._get_test(obj, name, module, globs, source_lines)
  File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 965, in _get_test
    filename, lineno)
  File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 594, in get_doctest
    return DocTest(self.get_examples(string, name), globs,
  File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 608, in get_examples
    return [x for x in self.parse(string, name)
  File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 570, in parse
    self._parse_example(m, name, lineno)
  File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 628, in _parse_example
    self._check_prompt_blank(source_lines, indent, name, lineno)
  File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 715, in _check_prompt_blank
    line[indent:indent+3], line))
ValueError: line 24 of the docstring for __main__.example_23 lacks blank after ...: "            ...e-Integer(16) + RealNumber('1.7320508075E')llipsis*I"

	 [2.5 s]
exit code: 1024
```

According to wstein this is a bug in the preparser.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 08:57:36

Invalid since:

```
[01:54am] mabshoff: Are we invalidating the "..." ticket or might there be a long term fix?
[01:54am] wstein: mabshoff -- I say invalidate.
[01:54am] wstein: doctest output should never start with ...
[01:54am] mabshoff: ok
[01:55am] wstein: since ... means "line continuation/indent"
[01:55am] mabshoff: Ok, I see the problem there.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 08:57:36

Resolution: invalid
