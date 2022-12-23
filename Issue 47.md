# Issue 47: make it easy to turn off preparser

archive/issues_000047.json:
```json
{
    "body": "Assignee: somebody\n\nIt's \"from sage.all import *\".  But then I'm being dumb, since that\njust turns the preparser back on. \n\nThe preparser in SAGE is activated in misc/interpreter.py in this line:\n\n# Rebind this to be the new IPython prefilter:\nInteractiveShell.prefilter = sage_prefilter\n\nIf you comment that one line out, then restart SAGE (with sage -br) you'll \nget a SAGE that has no preparsing at all by default.  Yet all the library\ncode\nshould work fine and you have the sage library functions available by\ndefault.\n\nThat sounds reasonable. I undid the preparser.py change and commented out the\nsuggested line in interpreter.py. With a few basic tests everything seems OK.\n\nI guess the default int is now a Python int, but that is okay for what I'm working on\nright now. \n\nThanks for sorting this out.\n\nIssue created by migration from https://trac.sagemath.org/ticket/47\n\n",
    "created_at": "2006-09-13T09:26:37Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "title": "make it easy to turn off preparser",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/47",
    "user": "anonymous"
}
```
Assignee: somebody

It's "from sage.all import *".  But then I'm being dumb, since that
just turns the preparser back on. 

The preparser in SAGE is activated in misc/interpreter.py in this line:

# Rebind this to be the new IPython prefilter:
InteractiveShell.prefilter = sage_prefilter

If you comment that one line out, then restart SAGE (with sage -br) you'll 
get a SAGE that has no preparsing at all by default.  Yet all the library
code
should work fine and you have the sage library functions available by
default.

That sounds reasonable. I undid the preparser.py change and commented out the
suggested line in interpreter.py. With a few basic tests everything seems OK.

I guess the default int is now a Python int, but that is okay for what I'm working on
right now. 

Thanks for sorting this out.

Issue created by migration from https://trac.sagemath.org/ticket/47





---

archive/issue_comments_000276.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T07:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/47",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/47#issuecomment-276",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_000277.json:
```json
{
    "body": "This has been possible for a while now:\n\n```\nsage: preparser(False)\nsage: 2^2\n0\nsage: preparser(True)\nsage: 2^2\n4\n```\n\nHence I am closing the ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T07:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/47",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/47#issuecomment-277",
    "user": "mabshoff"
}
```

This has been possible for a while now:

```
sage: preparser(False)
sage: 2^2
0
sage: preparser(True)
sage: 2^2
4
```

Hence I am closing the ticket.

Cheers,

Michael
