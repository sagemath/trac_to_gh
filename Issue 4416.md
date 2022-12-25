# Issue 4416: Sage 3.2.a2: optional doctest failure in sage/rings/arith.py

archive/issues_004416.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ ./sage -t -long -optional devel/sage/sage/rings/arith.py\nsage -t -long -optional devel/sage/sage/rings/arith.py      Traceback (most recent call last):\n  File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/.doctest_arith.py\", line 2453, in <module>\n    globs=globals())\n  File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 1814, in testmod\n    for test in finder.find(m, name, globs=globs, extraglobs=extraglobs):\n  File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 839, in find\n    self._find(tests, obj, name, module, source_lines, globs, {})\n  File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 893, in _find\n    globs, seen)\n  File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 881, in _find\n    test = self._get_test(obj, name, module, globs, source_lines)\n  File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 965, in _get_test\n    filename, lineno)\n  File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 594, in get_doctest\n    return DocTest(self.get_examples(string, name), globs,\n  File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 608, in get_examples\n    return [x for x in self.parse(string, name)\n  File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 570, in parse\n    self._parse_example(m, name, lineno)\n  File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 640, in _parse_example\n    lineno + len(source_lines))\n  File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py\", line 726, in _check_prefix\n    (lineno+i+1, name, line))\nValueError: line 51 of the docstring for __main__.example_2 has inconsistent leading whitespace: \"    \\\\note{If $n>50000$ then algorithm = 'gp' is used instead of\"\n\n\t [2.3 s]\nexit code: 1024\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4416\n\n",
    "created_at": "2008-11-01T01:11:29Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Sage 3.2.a2: optional doctest failure in sage/rings/arith.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4416",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ ./sage -t -long -optional devel/sage/sage/rings/arith.py
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


Issue created by migration from https://trac.sagemath.org/ticket/4416





---

archive/issue_comments_032417.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-01T01:11:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4416#issuecomment-32417",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032418.json:
```json
{
    "body": "Attachment [trac_4416.patch](tarball://root/attachments/some-uuid/ticket4416/trac_4416.patch) by mabshoff created at 2008-11-01 01:13:25",
    "created_at": "2008-11-01T01:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4416#issuecomment-32418",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4416.patch](tarball://root/attachments/some-uuid/ticket4416/trac_4416.patch) by mabshoff created at 2008-11-01 01:13:25



---

archive/issue_comments_032419.json:
```json
{
    "body": "Patch looks good. Probably also makes the docstring more readable ...",
    "created_at": "2008-11-01T22:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4416#issuecomment-32419",
    "user": "https://github.com/craigcitro"
}
```

Patch looks good. Probably also makes the docstring more readable ...



---

archive/issue_comments_032420.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-02T00:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4416#issuecomment-32420",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032421.json:
```json
{
    "body": "Merged in Sage 3.2.alpha3",
    "created_at": "2008-11-02T00:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4416#issuecomment-32421",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha3



---

archive/issue_events_004661.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-02T00:48:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4416",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4416#event-4661"
}
```
