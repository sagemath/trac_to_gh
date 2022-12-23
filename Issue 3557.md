# Issue 3557: Preparser bug: doctest failes when "..." is first expected output

archive/issues_003557.json:
```json
{
    "body": "Assignee: was\n\nWith \n\n```\n         EXAMPLES:\n             sage: G = DirichletGroup(3) \n             sage: e = G.0\n             sage: e.gauss_sum_numerical()\n             ...e-16 + 1.7320508075...*I\n```\n\nthe doctesting framework complains about:\n\n```\nsage -t -long devel/sage/sage/modular/dirichlet.py          Traceback (most recent call last):\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/.doctest_dirichlet.py\", line 1206, in <module>\n    globs=globals())\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py\", line 1814, in testmod\n    for test in finder.find(m, name, globs=globs, extraglobs=extraglobs):\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py\", line 839, in find\n    self._find(tests, obj, name, module, source_lines, globs, {})\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py\", line 893, in _find\n    globs, seen)\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py\", line 881, in _find\n    test = self._get_test(obj, name, module, globs, source_lines)\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py\", line 965, in _get_test\n    filename, lineno)\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py\", line 594, in get_doctest\n    return DocTest(self.get_examples(string, name), globs,\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py\", line 608, in get_examples\n    return [x for x in self.parse(string, name)\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py\", line 570, in parse\n    self._parse_example(m, name, lineno)\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py\", line 628, in _parse_example\n    self._check_prompt_blank(source_lines, indent, name, lineno)\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py\", line 715, in _check_prompt_blank\n    line[indent:indent+3], line))\nValueError: line 24 of the docstring for __main__.example_23 lacks blank after ...: \"            ...e-Integer(16) + RealNumber('1.7320508075E')llipsis*I\"\n\n\t [2.5 s]\nexit code: 1024\n```\n\nAccording to wstein this is a bug in the preparser.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3557\n\n",
    "created_at": "2008-07-06T01:39:11Z",
    "labels": [
        "doctest coverage",
        "critical",
        "bug"
    ],
    "title": "Preparser bug: doctest failes when \"...\" is first expected output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3557",
    "user": "mabshoff"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/3557





---

archive/issue_comments_025148.json:
```json
{
    "body": "Invalid since:\n\n```\n[01:54am] mabshoff: Are we invalidating the \"...\" ticket or might there be a long term fix?\n[01:54am] wstein: mabshoff -- I say invalidate.\n[01:54am] wstein: doctest output should never start with ...\n[01:54am] mabshoff: ok\n[01:55am] wstein: since ... means \"line continuation/indent\"\n[01:55am] mabshoff: Ok, I see the problem there.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T08:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3557#issuecomment-25148",
    "user": "mabshoff"
}
```

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

archive/issue_comments_025149.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-07-06T08:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3557",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3557#issuecomment-25149",
    "user": "mabshoff"
}
```

Resolution: invalid
