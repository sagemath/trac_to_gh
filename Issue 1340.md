# Issue 1340: %cython seriously broken

archive/issues_001340.json:
```json
{
    "body": "Assignee: robertwb\n\nTry this from the notebook:\n\n\n```\n%cython\n\ndef foo(e,f):\n  return e*f\n```\n\n\nand you'll get:\n\n\n```\nTraceback (most recent call last):    \n  File \"/home/malb/SAGE/local/lib/python2.5/site-packages/sage/server/support.py\", line 303, in cython_import_all\n    create_local_c_file=create_local_c_file)\n  File \"/home/malb/SAGE/local/lib/python2.5/site-packages/sage/server/support.py\", line 284, in cython_import\n    create_local_c_file=create_local_c_file)\n  File \"/home/malb/SAGE/local/lib/python2.5/site-packages/sage/misc/cython.py\", line 220, in cython\n    raise RuntimeError, \"Error converting %s to C:\\n%s\\n%s\"%(filename, log, err)\nRuntimeError: Error converting /home/malb/Texte/Talks/20071129 - SAGE - Paris/sage_notebook/worksheets/admin/2/code/sage47.spyx to C:\n\nCython (http://cython.org) is a compiler for code written in the\nCython language.  Cython is based on Pyrex by Greg Ewing.\n\nUsage: cython [options] sourcefile.pyx ...\n\nOptions:\n  -v, --version                  Display version number of cython compiler\n  -l, --create-listing           Write error messages to a listing file\n  -I, --include-dir <directory>  Search for include files in named directory\n                                 (multiply include directories are allowed).\n  -o, --output-file <filename>   Specify name of generated C file\n  -p, --embed-positions          If specified, the positions in Cython files of each\n                                 function definition is embedded in its docstring.\n  -z, --pre-import <module>      If specified, assume undeclared names in this \n                                 module. Emulates the behavior of putting \n                                 \"from <module> import *\" at the top of the file. \n  --incref-local-binop           Force local an extra incref on local variables before\n                                 performing any binary operations.\n  -D, --no-docstrings            Remove docstrings.\n  -a, --annotate                 Produce an colorized version of the source.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1340\n\n",
    "created_at": "2007-11-29T13:27:45Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "%cython seriously broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1340",
    "user": "malb"
}
```
Assignee: robertwb

Try this from the notebook:


```
%cython

def foo(e,f):
  return e*f
```


and you'll get:


```
Traceback (most recent call last):    
  File "/home/malb/SAGE/local/lib/python2.5/site-packages/sage/server/support.py", line 303, in cython_import_all
    create_local_c_file=create_local_c_file)
  File "/home/malb/SAGE/local/lib/python2.5/site-packages/sage/server/support.py", line 284, in cython_import
    create_local_c_file=create_local_c_file)
  File "/home/malb/SAGE/local/lib/python2.5/site-packages/sage/misc/cython.py", line 220, in cython
    raise RuntimeError, "Error converting %s to C:\n%s\n%s"%(filename, log, err)
RuntimeError: Error converting /home/malb/Texte/Talks/20071129 - SAGE - Paris/sage_notebook/worksheets/admin/2/code/sage47.spyx to C:

Cython (http://cython.org) is a compiler for code written in the
Cython language.  Cython is based on Pyrex by Greg Ewing.

Usage: cython [options] sourcefile.pyx ...

Options:
  -v, --version                  Display version number of cython compiler
  -l, --create-listing           Write error messages to a listing file
  -I, --include-dir <directory>  Search for include files in named directory
                                 (multiply include directories are allowed).
  -o, --output-file <filename>   Specify name of generated C file
  -p, --embed-positions          If specified, the positions in Cython files of each
                                 function definition is embedded in its docstring.
  -z, --pre-import <module>      If specified, assume undeclared names in this 
                                 module. Emulates the behavior of putting 
                                 "from <module> import *" at the top of the file. 
  --incref-local-binop           Force local an extra incref on local variables before
                                 performing any binary operations.
  -D, --no-docstrings            Remove docstrings.
  -a, --annotate                 Produce an colorized version of the source.
```


Issue created by migration from https://trac.sagemath.org/ticket/1340





---

archive/issue_comments_008593.json:
```json
{
    "body": "I cannot replicate this at all.   %cython works fine for me in sage-2.8.14, at least on osx.  and definitely works fine in 2.8.13 in linux.  And there has been no change to related code that I can think of.\n\n\n```\n raise RuntimeError, \"Error converting %s to C:\\n%s\\n%s\"%(filename, log, err)\n```\n\n\nWhat's with the C: -- looks suspicious.",
    "created_at": "2007-11-29T14:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1340#issuecomment-8593",
    "user": "was"
}
```

I cannot replicate this at all.   %cython works fine for me in sage-2.8.14, at least on osx.  and definitely works fine in 2.8.13 in linux.  And there has been no change to related code that I can think of.


```
 raise RuntimeError, "Error converting %s to C:\n%s\n%s"%(filename, log, err)
```


What's with the C: -- looks suspicious.



---

archive/issue_comments_008594.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-11-29T14:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1340#issuecomment-8594",
    "user": "malb"
}
```

Resolution: invalid



---

archive/issue_comments_008595.json:
```json
{
    "body": "> What's with the C: -- looks suspicious.\n\nIt's not the driver letter C but, \"convert to C\" ... and then colon to show what when wrong.\n\nAnyway, I'll invalidate it for now.",
    "created_at": "2007-11-29T14:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1340#issuecomment-8595",
    "user": "malb"
}
```

> What's with the C: -- looks suspicious.

It's not the driver letter C but, "convert to C" ... and then colon to show what when wrong.

Anyway, I'll invalidate it for now.



---

archive/issue_comments_008596.json:
```json
{
    "body": "The problem actually is, that %cython doesn't work well with directory names containing spaces.",
    "created_at": "2007-11-29T14:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1340#issuecomment-8596",
    "user": "malb"
}
```

The problem actually is, that %cython doesn't work well with directory names containing spaces.



---

archive/issue_comments_008597.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-11-29T14:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1340#issuecomment-8597",
    "user": "malb"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_008598.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2007-11-29T14:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1340#issuecomment-8598",
    "user": "malb"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_008599.json:
```json
{
    "body": "Attachment [1340-cython-spaces.patch](tarball://root/attachments/some-uuid/ticket1340/1340-cython-spaces.patch) by robertwb created at 2007-12-02 09:52:26",
    "created_at": "2007-12-02T09:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1340#issuecomment-8599",
    "user": "robertwb"
}
```

Attachment [1340-cython-spaces.patch](tarball://root/attachments/some-uuid/ticket1340/1340-cython-spaces.patch) by robertwb created at 2007-12-02 09:52:26



---

archive/issue_comments_008600.json:
```json
{
    "body": "Looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-14T04:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1340#issuecomment-8600",
    "user": "mabshoff"
}
```

Looks good to me.

Cheers,

Michael



---

archive/issue_comments_008601.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-14T05:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1340#issuecomment-8601",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008602.json:
```json
{
    "body": "Merged in 2.9.alpha7.",
    "created_at": "2007-12-14T05:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1340#issuecomment-8602",
    "user": "mabshoff"
}
```

Merged in 2.9.alpha7.
