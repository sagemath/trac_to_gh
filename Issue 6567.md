# Issue 6567: function to test whether or not some integer is a primitive root modulo n

archive/issues_006567.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman\n\nKeywords: primitive roots\n\nCurrently, the function `primitive_root()` finds a primitive root modulo n. Ticket #6467 proposes to find all primitive roots modulo a fixed n. We should also implement a function to determine whether or not some integer is a primitive root modulo n. A good way is to do this without first having to generate all primitive roots mod n.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6567\n\n",
    "created_at": "2009-07-20T12:11:43Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.8",
    "title": "function to test whether or not some integer is a primitive root modulo n",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6567",
    "user": "mvngu"
}
```
Assignee: @williamstein

CC:  @kcrisman

Keywords: primitive roots

Currently, the function `primitive_root()` finds a primitive root modulo n. Ticket #6467 proposes to find all primitive roots modulo a fixed n. We should also implement a function to determine whether or not some integer is a primitive root modulo n. A good way is to do this without first having to generate all primitive roots mod n.

Issue created by migration from https://trac.sagemath.org/ticket/6567





---

archive/issue_comments_053565.json:
```json
{
    "body": "Review anyone?",
    "created_at": "2012-10-17T08:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53565",
    "user": "@roed314"
}
```

Review anyone?



---

archive/issue_comments_053566.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-10-17T08:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53566",
    "user": "@roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053567.json:
```json
{
    "body": "There is a problem in the docstring:\n\n\n```\nTraceback (most recent call last):\n  File \"/dev/shm/sage_testdir/integer_mod_10415.py\", line 3096, in <module>\n    runner=runner)\n  File \"/dev/shm/sage/local/bin/sagedoctest.py\", line 54, in testmod_returning_runner\n    runner=runner)\n  File \"/dev/shm/sage/local/bin/ncadoctest.py\", line 1819, in testmod_returning_runner\n    for test in finder.find(m, name, globs=globs, extraglobs=extraglobs):\n  File \"/dev/shm/sage/local/bin/ncadoctest.py\", line 839, in find\n    self._find(tests, obj, name, module, source_lines, globs, {})\n  File \"/dev/shm/sage/local/bin/ncadoctest.py\", line 893, in _find\n    globs, seen)\n  File \"/dev/shm/sage/local/bin/ncadoctest.py\", line 881, in _find\n    test = self._get_test(obj, name, module, globs, source_lines)\n  File \"/dev/shm/sage/local/bin/ncadoctest.py\", line 965, in _get_test\n    filename, lineno)\n  File \"/dev/shm/sage/local/bin/ncadoctest.py\", line 594, in get_doctest\n    return DocTest(self.get_examples(string, name), globs,\n  File \"/dev/shm/sage/local/bin/ncadoctest.py\", line 608, in get_examples\n    return [x for x in self.parse(string, name)\n  File \"/dev/shm/sage/local/bin/ncadoctest.py\", line 570, in parse\n    self._parse_example(m, name, lineno)\n  File \"/dev/shm/sage/local/bin/ncadoctest.py\", line 628, in _parse_example\n    self._check_prompt_blank(source_lines, indent, name, lineno)\n  File \"/dev/shm/sage/local/bin/ncadoctest.py\", line 715, in _check_prompt_blank\n    line[indent:indent+3], line))\nValueError: line 27 of the docstring for __main__.example_32 lacks blank after ...: '            ....:     for k in range(Integer(1),Integer(4)):'\n```\n",
    "created_at": "2012-11-18T20:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53567",
    "user": "@saraedum"
}
```

There is a problem in the docstring:


```
Traceback (most recent call last):
  File "/dev/shm/sage_testdir/integer_mod_10415.py", line 3096, in <module>
    runner=runner)
  File "/dev/shm/sage/local/bin/sagedoctest.py", line 54, in testmod_returning_runner
    runner=runner)
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 1819, in testmod_returning_runner
    for test in finder.find(m, name, globs=globs, extraglobs=extraglobs):
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 839, in find
    self._find(tests, obj, name, module, source_lines, globs, {})
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 893, in _find
    globs, seen)
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 881, in _find
    test = self._get_test(obj, name, module, globs, source_lines)
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 965, in _get_test
    filename, lineno)
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 594, in get_doctest
    return DocTest(self.get_examples(string, name), globs,
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 608, in get_examples
    return [x for x in self.parse(string, name)
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 570, in parse
    self._parse_example(m, name, lineno)
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 628, in _parse_example
    self._check_prompt_blank(source_lines, indent, name, lineno)
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 715, in _check_prompt_blank
    line[indent:indent+3], line))
ValueError: line 27 of the docstring for __main__.example_32 lacks blank after ...: '            ....:     for k in range(Integer(1),Integer(4)):'
```




---

archive/issue_comments_053568.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-11-18T20:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53568",
    "user": "@saraedum"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_053569.json:
```json
{
    "body": "The doctesting error was due to depending on syntax only valid after #12415.  Since I don't want to wait on that, I've updated the doctest (and also marked the dependency correctly).",
    "created_at": "2013-02-27T01:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53569",
    "user": "@roed314"
}
```

The doctesting error was due to depending on syntax only valid after #12415.  Since I don't want to wait on that, I've updated the doctest (and also marked the dependency correctly).



---

archive/issue_comments_053570.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-02-27T01:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53570",
    "user": "@roed314"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053571.json:
```json
{
    "body": "\n```\n# self**(p**k*(p-1)//q) = 1 for some q \n```\n\nShould that be `k-1`?  I'd also put it \"# now self...\" just to make it clear\n\nEverything else looks nice.  I feel like I want to check the logic for numbers divisible by 2, 3, or 5 but where start > 5 a little more closely (getting late here) but if someone else does that first that is fine.",
    "created_at": "2013-02-27T04:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53571",
    "user": "@kcrisman"
}
```


```
# self**(p**k*(p-1)//q) = 1 for some q 
```

Should that be `k-1`?  I'd also put it "# now self..." just to make it clear

Everything else looks nice.  I feel like I want to check the logic for numbers divisible by 2, 3, or 5 but where start > 5 a little more closely (getting late here) but if someone else does that first that is fine.



---

archive/issue_comments_053572.json:
```json
{
    "body": "Attachment [6567.patch](tarball://root/attachments/some-uuid/ticket6567/6567.patch) by @roed314 created at 2013-02-27 11:36:46",
    "created_at": "2013-02-27T11:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53572",
    "user": "@roed314"
}
```

Attachment [6567.patch](tarball://root/attachments/some-uuid/ticket6567/6567.patch) by @roed314 created at 2013-02-27 11:36:46



---

archive/issue_comments_053573.json:
```json
{
    "body": "I'm not quite sure what you meant by the \"# now self...\" but I made some change along those lines.  I'm also not sure why patchbot was giving me a failure in applying.  Hopefully the new patch won't have the same problem.",
    "created_at": "2013-02-27T11:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53573",
    "user": "@roed314"
}
```

I'm not quite sure what you meant by the "# now self..." but I made some change along those lines.  I'm also not sure why patchbot was giving me a failure in applying.  Hopefully the new patch won't have the same problem.



---

archive/issue_comments_053574.json:
```json
{
    "body": "Attachment [6567_2.patch](tarball://root/attachments/some-uuid/ticket6567/6567_2.patch) by @haikona created at 2013-02-28 23:36:01\n\nFixes single line in self.is_primitive_root() to make compatible with new 12116.patch",
    "created_at": "2013-02-28T23:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53574",
    "user": "@haikona"
}
```

Attachment [6567_2.patch](tarball://root/attachments/some-uuid/ticket6567/6567_2.patch) by @haikona created at 2013-02-28 23:36:01

Fixes single line in self.is_primitive_root() to make compatible with new 12116.patch



---

archive/issue_comments_053575.json:
```json
{
    "body": "Patch applies, but with the (proposed) change to #12116 - swapping the order integers returned by `perfect_power()` so that `(a^b).perfect_power()` returns `(a,b)` and not `(b,a)` - the code breaks on perfect powers or twice perfect powers. A simple single line change fixes this; I've uploaded a new patch with this fix. Line 1485 goes from\n\n```\nk, p = odd.perfect_power() \n```\n\nto\n\n```\np, k = odd.perfect_power() \n```\n\nEverything else is good.",
    "created_at": "2013-02-28T23:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53575",
    "user": "@haikona"
}
```

Patch applies, but with the (proposed) change to #12116 - swapping the order integers returned by `perfect_power()` so that `(a^b).perfect_power()` returns `(a,b)` and not `(b,a)` - the code breaks on perfect powers or twice perfect powers. A simple single line change fixes this; I've uploaded a new patch with this fix. Line 1485 goes from

```
k, p = odd.perfect_power() 
```

to

```
p, k = odd.perfect_power() 
```

Everything else is good.



---

archive/issue_comments_053576.json:
```json
{
    "body": "Fine with me.",
    "created_at": "2013-03-01T01:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53576",
    "user": "@roed314"
}
```

Fine with me.



---

archive/issue_comments_053577.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-01T01:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53577",
    "user": "@roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053578.json:
```json
{
    "body": "Please clarify which patch(es) must be applied.",
    "created_at": "2013-03-04T07:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53578",
    "user": "@jdemeyer"
}
```

Please clarify which patch(es) must be applied.



---

archive/issue_comments_053579.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-03-06T10:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6567#issuecomment-53579",
    "user": "@jdemeyer"
}
```

Resolution: fixed
