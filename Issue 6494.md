# Issue 6494: sage should *never* ever import numpy by default on startup.  Yet again it does!

archive/issues_006494.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @williamstein @jasongrout @robertwb\n\n\n```\n.bash-3.2$ ./sage -startuptime |grep numpy\n           decorators_numpy: 0.000 (IPython.testing)\n             numpy: 0.073 (complex_plot)\n              numpy.__config__: 0.000 (numpy)\n              version: 0.000 (numpy)\n              _import_tools: 0.000 (numpy)\n              add_newdocs: 0.047 (numpy)\n                numpy.version: 0.000 (lib)\n                 numpy.core.numeric: 0.018 (type_check)\n                  multiarray: 0.002 (numpy.core.numeric)\n                  umath: 0.001 (numpy.core.numeric)\n                   numpy.core.multiarray: 0.000 (umath)\n                  _internal: 0.001 (numpy.core.numeric)\n                  numerictypes: 0.002 (numpy.core.numeric)\n                  _sort: 0.000 (numpy.core.numeric)\n                  numeric: 0.004 (numpy.core.numeric)\n                  defmatrix: 0.001 (numpy.core.numeric)\n                  defchararray: 0.000 (numpy.core.numeric)\n                  records: 0.001 (numpy.core.numeric)\n                  memmap: 0.000 (numpy.core.numeric)\n                  scalarmath: 0.001 (numpy.core.numeric)\n                   numpy.core.umath: 0.000 (scalarmath)\n                  numpy.testing: 0.004 (numpy.core.numeric)\n                   decorators: 0.000 (numpy.testing)\n                   utils: 0.003 (numpy.testing)\n                   numpytest: 0.000 (numpy.testing)\n                 numpy.core.numerictypes: 0.000 (index_tricks)\n                  numpy.core.fromnumeric: 0.000 (function_base)\n                  numpy.lib.shape_base: 0.000 (function_base)\n                  numpy.lib.twodim_base: 0.000 (function_base)\n                 numpy.core.defmatrix: 0.000 (index_tricks)\n                 numpy.lib.type_check: 0.000 (scimath)\n                 numpy.core: 0.000 (polynomial)\n                 numpy.lib.getlimits: 0.001 (polynomial)\n                  machar: 0.000 (numpy.lib.getlimits)\n                 numpy.lib.function_base: 0.000 (polynomial)\n                 numpy.linalg: 0.002 (polynomial)\n                  linalg: 0.001 (numpy.linalg)\n                   numpy.lib: 0.000 (linalg)\n                  numpy.lib.utils: 0.000 (format)\n               numpy.lib._compiled_base: 0.000 (add_newdocs)\n               numpy.lib.index_tricks: 0.000 (add_newdocs)\n              testing: 0.000 (numpy)\n              core: 0.000 (numpy)\n              fft: 0.002 (numpy)\n              mtrand: 0.015 (numpy)\n              ctypeslib: 0.001 (numpy)\n               numpy.core._internal: 0.000 (ctypeslib)\n              ma: 0.006 (numpy)\n0.073 numpy (complex_plot)\n```\n\n\nI think this is because of the new complex_plot module, which I think I positively reviewed, so this is my fault.  To resolve this ticket, make that import sufficiently lazy.  Also, make a doctest that verifies that numpy is not imported when Sage starts up.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6494\n\n",
    "created_at": "2009-07-09T04:20:56Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage should *never* ever import numpy by default on startup.  Yet again it does!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6494",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

CC:  @williamstein @jasongrout @robertwb


```
.bash-3.2$ ./sage -startuptime |grep numpy
           decorators_numpy: 0.000 (IPython.testing)
             numpy: 0.073 (complex_plot)
              numpy.__config__: 0.000 (numpy)
              version: 0.000 (numpy)
              _import_tools: 0.000 (numpy)
              add_newdocs: 0.047 (numpy)
                numpy.version: 0.000 (lib)
                 numpy.core.numeric: 0.018 (type_check)
                  multiarray: 0.002 (numpy.core.numeric)
                  umath: 0.001 (numpy.core.numeric)
                   numpy.core.multiarray: 0.000 (umath)
                  _internal: 0.001 (numpy.core.numeric)
                  numerictypes: 0.002 (numpy.core.numeric)
                  _sort: 0.000 (numpy.core.numeric)
                  numeric: 0.004 (numpy.core.numeric)
                  defmatrix: 0.001 (numpy.core.numeric)
                  defchararray: 0.000 (numpy.core.numeric)
                  records: 0.001 (numpy.core.numeric)
                  memmap: 0.000 (numpy.core.numeric)
                  scalarmath: 0.001 (numpy.core.numeric)
                   numpy.core.umath: 0.000 (scalarmath)
                  numpy.testing: 0.004 (numpy.core.numeric)
                   decorators: 0.000 (numpy.testing)
                   utils: 0.003 (numpy.testing)
                   numpytest: 0.000 (numpy.testing)
                 numpy.core.numerictypes: 0.000 (index_tricks)
                  numpy.core.fromnumeric: 0.000 (function_base)
                  numpy.lib.shape_base: 0.000 (function_base)
                  numpy.lib.twodim_base: 0.000 (function_base)
                 numpy.core.defmatrix: 0.000 (index_tricks)
                 numpy.lib.type_check: 0.000 (scimath)
                 numpy.core: 0.000 (polynomial)
                 numpy.lib.getlimits: 0.001 (polynomial)
                  machar: 0.000 (numpy.lib.getlimits)
                 numpy.lib.function_base: 0.000 (polynomial)
                 numpy.linalg: 0.002 (polynomial)
                  linalg: 0.001 (numpy.linalg)
                   numpy.lib: 0.000 (linalg)
                  numpy.lib.utils: 0.000 (format)
               numpy.lib._compiled_base: 0.000 (add_newdocs)
               numpy.lib.index_tricks: 0.000 (add_newdocs)
              testing: 0.000 (numpy)
              core: 0.000 (numpy)
              fft: 0.002 (numpy)
              mtrand: 0.015 (numpy)
              ctypeslib: 0.001 (numpy)
               numpy.core._internal: 0.000 (ctypeslib)
              ma: 0.006 (numpy)
0.073 numpy (complex_plot)
```


I think this is because of the new complex_plot module, which I think I positively reviewed, so this is my fault.  To resolve this ticket, make that import sufficiently lazy.  Also, make a doctest that verifies that numpy is not imported when Sage starts up.

Issue created by migration from https://trac.sagemath.org/ticket/6494





---

archive/issue_comments_052451.json:
```json
{
    "body": "Attachment [trac_6494.patch](tarball://root/attachments/some-uuid/ticket6494/trac_6494.patch) by @mwhansen created at 2010-08-26 19:31:43",
    "created_at": "2010-08-26T19:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6494#issuecomment-52451",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6494.patch](tarball://root/attachments/some-uuid/ticket6494/trac_6494.patch) by @mwhansen created at 2010-08-26 19:31:43



---

archive/issue_comments_052452.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-26T19:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6494#issuecomment-52452",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_052453.json:
```json
{
    "body": "I don't think you can cimport numpy without causing an import in the module.  Thus, a number of things have to be lazily imported.  This will cause a problem if people do\n\n\n```\nsage: from sage.finance.all import TimeSeries\nsage: isinstance(foo, TimeSeries)\n```\n\n\nsince TimeSeries will be a LazyImport object rather than a class.  I'm not sure the best thing to do, but I've posted a patch anyway.",
    "created_at": "2010-08-26T19:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6494#issuecomment-52453",
    "user": "https://github.com/mwhansen"
}
```

I don't think you can cimport numpy without causing an import in the module.  Thus, a number of things have to be lazily imported.  This will cause a problem if people do


```
sage: from sage.finance.all import TimeSeries
sage: isinstance(foo, TimeSeries)
```


since TimeSeries will be a LazyImport object rather than a class.  I'm not sure the best thing to do, but I've posted a patch anyway.



---

archive/issue_comments_052454.json:
```json
{
    "body": "numpy recently has made great improvements in its import speed, so maybe this isn't quite the issue it used to be?",
    "created_at": "2010-10-02T20:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6494#issuecomment-52454",
    "user": "https://github.com/jasongrout"
}
```

numpy recently has made great improvements in its import speed, so maybe this isn't quite the issue it used to be?



---

archive/issue_comments_052455.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-10-15T12:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6494#issuecomment-52455",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_052456.json:
```json
{
    "body": "I'm not going to judge whether numpy imports are still an issue or not, but in any case the patch needs to be rebased:\n\n```\npatching file sage/calculus/all.py\nHunk #2 succeeded at 16 (offset 1 line).\npatching file sage/finance/all.py\npatching file sage/interfaces/gnuplot.py\npatching file sage/plot/all.py\nHunk #2 FAILED at 21.\n1 out of 2 hunks FAILED -- saving rejects to file sage/plot/all.py.rej\npatching file sage/plot/plot3d/implicit_plot3d.py\nHunk #2 succeeded at 255 (offset 10 lines).\npatching file sage/stats/all.py\npatching file sage/stats/hmm/all.py\n```\n",
    "created_at": "2011-10-15T12:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6494#issuecomment-52456",
    "user": "https://github.com/jdemeyer"
}
```

I'm not going to judge whether numpy imports are still an issue or not, but in any case the patch needs to be rebased:

```
patching file sage/calculus/all.py
Hunk #2 succeeded at 16 (offset 1 line).
patching file sage/finance/all.py
patching file sage/interfaces/gnuplot.py
patching file sage/plot/all.py
Hunk #2 FAILED at 21.
1 out of 2 hunks FAILED -- saving rejects to file sage/plot/all.py.rej
patching file sage/plot/plot3d/implicit_plot3d.py
Hunk #2 succeeded at 255 (offset 10 lines).
patching file sage/stats/all.py
patching file sage/stats/hmm/all.py
```




---

archive/issue_comments_052457.json:
```json
{
    "body": "This ticket is invalid now as all of the changes appearing in it are already in the Sage library.",
    "created_at": "2012-03-28T21:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6494#issuecomment-52457",
    "user": "https://github.com/mwhansen"
}
```

This ticket is invalid now as all of the changes appearing in it are already in the Sage library.



---

archive/issue_comments_052458.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-03-28T21:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6494#issuecomment-52458",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_006732.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2012-03-28T21:09:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6494",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6494#event-6732"
}
```



---

archive/issue_comments_052459.json:
```json
{
    "body": "You shouldn't just close tickets, leave that to the release manager.",
    "created_at": "2012-03-28T22:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6494#issuecomment-52459",
    "user": "https://github.com/jdemeyer"
}
```

You shouldn't just close tickets, leave that to the release manager.
