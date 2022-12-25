# Issue 438: cython -v prints standard help text

archive/issues_000438.json:
```json
{
    "body": "Assignee: @williamstein\n\nInstead of some version number I get\n\n[mabshoff`@`m940 sage-2.8.1]$ cython -v\nCython (http://cython.org) is a compiler for code written in the\nCython language.  Cython is based on Pyrex by Greg Ewing.\n\nUsage: cython [options] sourcefile.pyx ...\n\nOptions:\n  -v, --version                  Display version number of cython compiler\n  -l, --create-listing           Write error messages to a listing file\n  -I, --include-dir <directory>  Search for include files in named directory\n                                 (multiply include directories are allowed).\n  -o, --output-file <filename>   Specify name of generated C file\n  -p, --embed-positions          If specified, the positions in Cython files of each\n                                 function definition is embedded in its docstring.\n  -z, --pre-import <module>      If specified, assume undeclared names in this\nmodule. Emulates the behavior of putting\n                                 \"from <module> import *\" at the top of the file.\n\nIssue created by migration from https://trac.sagemath.org/ticket/438\n\n",
    "created_at": "2007-08-18T17:52:27Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "cython -v prints standard help text",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/438",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

Instead of some version number I get

[mabshoff`@`m940 sage-2.8.1]$ cython -v
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

Issue created by migration from https://trac.sagemath.org/ticket/438





---

archive/issue_events_001078.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-29T21:11:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/438",
    "milestone": "sage-2.9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/438#event-1078"
}
```



---

archive/issue_comments_002183.json:
```json
{
    "body": "I will report this to the Cython dev mailing list.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-29T21:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/438#issuecomment-2183",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I will report this to the Cython dev mailing list.

Cheers,

Michael



---

archive/issue_comments_002184.json:
```json
{
    "body": "I never reported this to the cython-devel list, but somebody else did this week and it ought to be fixed soon then.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T01:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/438#issuecomment-2184",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I never reported this to the cython-devel list, but somebody else did this week and it ought to be fixed soon then.

Cheers,

Michael



---

archive/issue_comments_002185.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2008-02-16T01:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/438#issuecomment-2185",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_events_001079.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2008-02-23T06:36:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/438",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/438#event-1079"
}
```



---

archive/issue_comments_002186.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-23T06:36:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/438#issuecomment-2186",
    "user": "https://github.com/robertwb"
}
```

Resolution: fixed
