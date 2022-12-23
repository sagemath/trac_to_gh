# Issue 5104: setup.py dependency checking issues

archive/issues_005104.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  sbarthelemy robertwb\n\nIn addition to the problems fixed on trac #5060, we also have the following, reported by `sbarthelemy`:\n\nHello,\n\nreading the code, I see another problem if ones has the following line in its `.pyx`:\n\n`cimport mod#mycomment`\n\nIn such a case, we'll look for a dependency `mod#mycomment.pxd` instead of `mod.pxd`.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5104\n\n",
    "created_at": "2009-01-26T16:47:03Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "title": "setup.py dependency checking issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5104",
    "user": "craigcitro"
}
```
Assignee: mabshoff

CC:  sbarthelemy robertwb

In addition to the problems fixed on trac #5060, we also have the following, reported by `sbarthelemy`:

Hello,

reading the code, I see another problem if ones has the following line in its `.pyx`:

`cimport mod#mycomment`

In such a case, we'll look for a dependency `mod#mycomment.pxd` instead of `mod.pxd`.



Issue created by migration from https://trac.sagemath.org/ticket/5104





---

archive/issue_comments_038972.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-01-26T16:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5104#issuecomment-38972",
    "user": "mhansen"
}
```

Resolution: duplicate



---

archive/issue_comments_038973.json:
```json
{
    "body": "I beat you to it Craig :-)\n\nThis is a duplicate of #5103.",
    "created_at": "2009-01-26T16:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5104#issuecomment-38973",
    "user": "mhansen"
}
```

I beat you to it Craig :-)

This is a duplicate of #5103.



---

archive/issue_comments_038974.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2009-01-26T16:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5104#issuecomment-38974",
    "user": "craigcitro"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_038975.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-01-26T16:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5104#issuecomment-38975",
    "user": "craigcitro"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_038976.json:
```json
{
    "body": "Oops -- Mike and I made tickets at the same time; apparently we closed each other's tickets at the same time, too. \n\nWe'll keep this one open.",
    "created_at": "2009-01-26T16:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5104#issuecomment-38976",
    "user": "craigcitro"
}
```

Oops -- Mike and I made tickets at the same time; apparently we closed each other's tickets at the same time, too. 

We'll keep this one open.



---

archive/issue_comments_038977.json:
```json
{
    "body": "This also seems like a worthwhile fix to be in 3.3\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T08:48:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5104#issuecomment-38977",
    "user": "mabshoff"
}
```

This also seems like a worthwhile fix to be in 3.3

Cheers,

Michael



---

archive/issue_comments_038978.json:
```json
{
    "body": "Positive review & good catch.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T09:23:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5104#issuecomment-38978",
    "user": "mabshoff"
}
```

Positive review & good catch.

Cheers,

Michael



---

archive/issue_comments_038979.json:
```json
{
    "body": "Arrg, this code actually does introduce a problem since `\\w` does not include the directory separator `/`. Hence:\n\n```\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nTraceback (most recent call last):\n  File \"setup.py\", line 510, in <module>\n    queue = compile_command_list(ext_modules, deps)\n  File \"setup.py\", line 470, in compile_command_list\n    dep_file, dep_time = deps.newest_dep(f)\n  File \"setup.py\", line 385, in newest_dep\n    for f in self.all_deps(filename):\n  File \"setup.py\", line 366, in all_deps\n    for f in self.immediate_deps(filename):\n  File \"setup.py\", line 348, in immediate_deps\n    self._deps[filename] = self.parse_deps(filename)\n  File \"setup.py\", line 338, in parse_deps\n    raise IOError, \"could not find dependency %s included in %s.\"%(path, filename)\nIOError: could not find dependency sage/finance/sage.pxd included in sage/finance/time_series.pyx.\nsage: There was an error installing modified sage library code.\n```\n\n\nSorry for the hasty review :(\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T09:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5104#issuecomment-38979",
    "user": "mabshoff"
}
```

Arrg, this code actually does introduce a problem since `\w` does not include the directory separator `/`. Hence:

```
Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Traceback (most recent call last):
  File "setup.py", line 510, in <module>
    queue = compile_command_list(ext_modules, deps)
  File "setup.py", line 470, in compile_command_list
    dep_file, dep_time = deps.newest_dep(f)
  File "setup.py", line 385, in newest_dep
    for f in self.all_deps(filename):
  File "setup.py", line 366, in all_deps
    for f in self.immediate_deps(filename):
  File "setup.py", line 348, in immediate_deps
    self._deps[filename] = self.parse_deps(filename)
  File "setup.py", line 338, in parse_deps
    raise IOError, "could not find dependency %s included in %s."%(path, filename)
IOError: could not find dependency sage/finance/sage.pxd included in sage/finance/time_series.pyx.
sage: There was an error installing modified sage library code.
```


Sorry for the hasty review :(

Cheers,

Michael



---

archive/issue_comments_038980.json:
```json
{
    "body": "I am cleaning up the 3.3 milestone. If a patch with positive review is put up to this ticket on time it might make it into 3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T05:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5104#issuecomment-38980",
    "user": "mabshoff"
}
```

I am cleaning up the 3.3 milestone. If a patch with positive review is put up to this ticket on time it might make it into 3.3.

Cheers,

Michael



---

archive/issue_comments_038981.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-17T10:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5104#issuecomment-38981",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_038982.json:
```json
{
    "body": "Updated the patch.",
    "created_at": "2009-02-17T10:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5104#issuecomment-38982",
    "user": "robertwb"
}
```

Updated the patch.



---

archive/issue_comments_038983.json:
```json
{
    "body": "Looks good to me. The complete Sage library dependency tree is parse successfully and also builds from scratch.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T13:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5104#issuecomment-38983",
    "user": "mabshoff"
}
```

Looks good to me. The complete Sage library dependency tree is parse successfully and also builds from scratch.

Cheers,

Michael



---

archive/issue_comments_038984.json:
```json
{
    "body": "Merged in Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T13:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5104#issuecomment-38984",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc3.

Cheers,

Michael



---

archive/issue_comments_038985.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T13:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5104#issuecomment-38985",
    "user": "mabshoff"
}
```

Resolution: fixed
