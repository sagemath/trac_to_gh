# Issue 6122: [with patch, needs review] strip 'nodetex' from docstrings

archive/issues_006122.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nIt bothers me that when you ask for a docstring with a 'nodetex' directive, that directive is printed as part of the docstring.  This patch strips it out.\n\nBefore (note the line after \"Docstring:\"):\n\n```\nsage: view?\nBase Class:       <type 'function'>\nString Form:   <function view at 0x102a230>\nNamespace:        Interactive\nFile:             /Applications/sage/local/lib/python2.5/site-packages/sage/misc/latex.py\nDefinition:       view(objects, title='SAGE', debug=False, sep='', tiny=False, **kwds)\nDocstring:\n    nodetex\n        Compute a latex representation of each object in objects, compile,\n        and display typeset. If used from the command line, this requires\n        that latex be installed.\n```\n\n\nAfter:\n\n```\nsage: view?\nBase Class:       <type 'function'>\nString Form:   <function view at 0x102b770>\nNamespace:        Interactive\nFile:             /Applications/sage/local/lib/python2.5/site-packages/sage/misc/latex.py\nDefinition:       view(objects, title='SAGE', debug=False, sep='', tiny=False, pdflatex=None, **kwds)\nDocstring:\n    \n        Compute a latex representation of each object in objects, compile,\n        and display typeset. If used from the command line, this requires\n        that latex be installed.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6122\n\n",
    "created_at": "2009-05-23T20:00:22Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, needs review] strip 'nodetex' from docstrings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6122",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

It bothers me that when you ask for a docstring with a 'nodetex' directive, that directive is printed as part of the docstring.  This patch strips it out.

Before (note the line after "Docstring:"):

```
sage: view?
Base Class:       <type 'function'>
String Form:   <function view at 0x102a230>
Namespace:        Interactive
File:             /Applications/sage/local/lib/python2.5/site-packages/sage/misc/latex.py
Definition:       view(objects, title='SAGE', debug=False, sep='', tiny=False, **kwds)
Docstring:
    nodetex
        Compute a latex representation of each object in objects, compile,
        and display typeset. If used from the command line, this requires
        that latex be installed.
```


After:

```
sage: view?
Base Class:       <type 'function'>
String Form:   <function view at 0x102b770>
Namespace:        Interactive
File:             /Applications/sage/local/lib/python2.5/site-packages/sage/misc/latex.py
Definition:       view(objects, title='SAGE', debug=False, sep='', tiny=False, pdflatex=None, **kwds)
Docstring:
    
        Compute a latex representation of each object in objects, compile,
        and display typeset. If used from the command line, this requires
        that latex be installed.
```


Issue created by migration from https://trac.sagemath.org/ticket/6122





---

archive/issue_comments_048827.json:
```json
{
    "body": "Attachment [no-nodetex.patch](tarball://root/attachments/some-uuid/ticket6122/no-nodetex.patch) by @rbeezer created at 2009-05-31 00:49:15\n\nApplies cleanly to 4.0, works as advertised at command-line and in the notebook.\n\nPasses  sage -t -rand sage/misc/sagedoc.py\n\nIt would be nice if these directives were cleaned out prior to building the PDF and HTML versions of the documentation.  This patch seems to only apply to the \"interactive\" documentation.   I'm still seeing nodetex directives in the PDF anyway, and in a sense they are worse, as they lead off a line and then the real beginning follows with no line break (as it used to look in the ASCII versions).  \n\nPositive review.",
    "created_at": "2009-05-31T00:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6122#issuecomment-48827",
    "user": "https://github.com/rbeezer"
}
```

Attachment [no-nodetex.patch](tarball://root/attachments/some-uuid/ticket6122/no-nodetex.patch) by @rbeezer created at 2009-05-31 00:49:15

Applies cleanly to 4.0, works as advertised at command-line and in the notebook.

Passes  sage -t -rand sage/misc/sagedoc.py

It would be nice if these directives were cleaned out prior to building the PDF and HTML versions of the documentation.  This patch seems to only apply to the "interactive" documentation.   I'm still seeing nodetex directives in the PDF anyway, and in a sense they are worse, as they lead off a line and then the real beginning follows with no line break (as it used to look in the ASCII versions).  

Positive review.



---

archive/issue_comments_048828.json:
```json
{
    "body": "> It would be nice if these directives were cleaned out prior to building the PDF and HTML versions of the documentation.\n\nSee #6166.",
    "created_at": "2009-05-31T04:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6122#issuecomment-48828",
    "user": "https://github.com/jhpalmieri"
}
```

> It would be nice if these directives were cleaned out prior to building the PDF and HTML versions of the documentation.

See #6166.



---

archive/issue_events_006372.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-01T05:04:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6122",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6122#event-6372"
}
```



---

archive/issue_comments_048829.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T05:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6122#issuecomment-48829",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_048830.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T05:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6122#issuecomment-48830",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.1.alpha0.
