# Issue 1945: [with patch] improve reference manual formatting

archive/issues_001945.json:
```json
{
    "body": "Assignee: tba\n\nI've gone through and made some changes to improve the formatting of the reference manual.  Here are my commit comments:\n\n```\nMany changes to improve the refman.\n1) Change SAGE->\\sage many places\n2) LaTeXify lots of math, literal strings, filenames, URLs, etc.\n3) fix typos, adjust content in other minor ways\n```\n\nand\n\n```\nMiscellaneous changes to make the reference manual prettier.\n1) Override python.sty so that list environments (itemize, etc.) inside\nfuncdesc environments work better.\n2) Change SAGE->Sage several places.\n3) Fix problem where sage.crypto.mq files were added to refman\n\"the old way\".\n4) Fix typos, adjust content in minor ways.\n5) Improve reference manual autogeneration:\n  a) only recognize \"sage:\" as doctest at the beginning of a line\n  b) only remove \"EXAMPLES:\" if it's the only thing on the line\n  c) start parsing \"INPUT:\" and \"OUTPUT:\" sections (so now you can\n     include LaTeX markup)\n  d) make parsing more flexible (authors can be separated by \"*\" as well\n     as \"--\", for example)\n  e) skip Cython file-location in module and class docstrings\n  f) if __init__ method has a docstring, put it in the refman\n  g) if a class includes a non-method, don't put it in the refman\n  h) if a module docstring includes \"nodoctest\", replace it with\n     useful text\n  i) work even when -f (\"force\") argument is not given\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1945\n\n",
    "created_at": "2008-01-27T01:04:41Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch] improve reference manual formatting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1945",
    "user": "cwitty"
}
```
Assignee: tba

I've gone through and made some changes to improve the formatting of the reference manual.  Here are my commit comments:

```
Many changes to improve the refman.
1) Change SAGE->\sage many places
2) LaTeXify lots of math, literal strings, filenames, URLs, etc.
3) fix typos, adjust content in other minor ways
```

and

```
Miscellaneous changes to make the reference manual prettier.
1) Override python.sty so that list environments (itemize, etc.) inside
funcdesc environments work better.
2) Change SAGE->Sage several places.
3) Fix problem where sage.crypto.mq files were added to refman
"the old way".
4) Fix typos, adjust content in minor ways.
5) Improve reference manual autogeneration:
  a) only recognize "sage:" as doctest at the beginning of a line
  b) only remove "EXAMPLES:" if it's the only thing on the line
  c) start parsing "INPUT:" and "OUTPUT:" sections (so now you can
     include LaTeX markup)
  d) make parsing more flexible (authors can be separated by "*" as well
     as "--", for example)
  e) skip Cython file-location in module and class docstrings
  f) if __init__ method has a docstring, put it in the refman
  g) if a class includes a non-method, don't put it in the refman
  h) if a module docstring includes "nodoctest", replace it with
     useful text
  i) work even when -f ("force") argument is not given
```


Issue created by migration from https://trac.sagemath.org/ticket/1945





---

archive/issue_comments_012345.json:
```json
{
    "body": "Attachment [trac-1945-doc.patch](tarball://root/attachments/some-uuid/ticket1945/trac-1945-doc.patch) by cwitty created at 2008-01-27 01:06:38\n\nThe hg_doc part of the patch",
    "created_at": "2008-01-27T01:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1945#issuecomment-12345",
    "user": "cwitty"
}
```

Attachment [trac-1945-doc.patch](tarball://root/attachments/some-uuid/ticket1945/trac-1945-doc.patch) by cwitty created at 2008-01-27 01:06:38

The hg_doc part of the patch



---

archive/issue_comments_012346.json:
```json
{
    "body": "Attachment [trac-1945-sage.patch](tarball://root/attachments/some-uuid/ticket1945/trac-1945-sage.patch) by cwitty created at 2008-01-27 01:07:23\n\nThe hg_sage part of the patch",
    "created_at": "2008-01-27T01:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1945#issuecomment-12346",
    "user": "cwitty"
}
```

Attachment [trac-1945-sage.patch](tarball://root/attachments/some-uuid/ticket1945/trac-1945-sage.patch) by cwitty created at 2008-01-27 01:07:23

The hg_sage part of the patch



---

archive/issue_comments_012347.json:
```json
{
    "body": "I have verified that testall passes with this patch.",
    "created_at": "2008-01-27T01:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1945#issuecomment-12347",
    "user": "cwitty"
}
```

I have verified that testall passes with this patch.



---

archive/issue_comments_012348.json:
```json
{
    "body": "Jason reviewed the changes to calculus.py; he says:\n\n```\n Okay, I've got to go, but I agree with all of your changes to calculus.py.\n (with the above exceptions :)\n```\n\nwhere \"the above exceptions\" are:\n\n```\nOne change: \n sage/calculus/calculus.py: line 1510\n with respect to $x$.\n (instead of \"with respect to $n$.\"\n```\n\nand\n\n```\n<jason> cwitty: in calculus.py, you changed .arguments() to .args().  Both seem to work.  Why the change?\n<jason> line 4440\n<cwitty> Because it's the doctest for .args(); if I don't make the change, then the doctest isn't testing the right thing.\n<jason> Especially since the docs to the function talk about .arguments()\n<cwitty> Oops; looks like more things should be changed then.\n<jason> oh, I didn't see that from the patch.\n<cwitty> (Or the whole .args() method should be replaced with \"args = arguments\".)\n<jason> That's my vote.  No code duplication then.\n```\n",
    "created_at": "2008-01-27T01:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1945#issuecomment-12348",
    "user": "cwitty"
}
```

Jason reviewed the changes to calculus.py; he says:

```
 Okay, I've got to go, but I agree with all of your changes to calculus.py.
 (with the above exceptions :)
```

where "the above exceptions" are:

```
One change: 
 sage/calculus/calculus.py: line 1510
 with respect to $x$.
 (instead of "with respect to $n$."
```

and

```
<jason> cwitty: in calculus.py, you changed .arguments() to .args().  Both seem to work.  Why the change?
<jason> line 4440
<cwitty> Because it's the doctest for .args(); if I don't make the change, then the doctest isn't testing the right thing.
<jason> Especially since the docs to the function talk about .arguments()
<cwitty> Oops; looks like more things should be changed then.
<jason> oh, I didn't see that from the patch.
<cwitty> (Or the whole .args() method should be replaced with "args = arguments".)
<jason> That's my vote.  No code duplication then.
```




---

archive/issue_comments_012349.json:
```json
{
    "body": "I didn't go over this with a fine tooth comb, but all changes are minor and seem reasonable.  I say apply.",
    "created_at": "2008-01-27T04:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1945#issuecomment-12349",
    "user": "ncalexan"
}
```

I didn't go over this with a fine tooth comb, but all changes are minor and seem reasonable.  I say apply.



---

archive/issue_comments_012350.json:
```json
{
    "body": "I needed to apply hunk 1 from the safe library patch manually.",
    "created_at": "2008-01-27T05:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1945#issuecomment-12350",
    "user": "mabshoff"
}
```

I needed to apply hunk 1 from the safe library patch manually.



---

archive/issue_comments_012351.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T05:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1945#issuecomment-12351",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012352.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc1",
    "created_at": "2008-01-27T05:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1945#issuecomment-12352",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc1
