# Issue 6864: Stop Sage tests from saving things to hard drive

archive/issues_006864.json:
```json
{
    "body": "Assignee: tba\n\nAs far as I can tell, there are several objects that are saved when you run sage -t.  One example is \n\n```\n    sage: from pylab import *\n    sage: t = arange(0.0, 2.0, 0.01)\n    sage: s = sin(2*pi*t)\n    sage: P = plot(t, s, linewidth=1.0)\n    sage: xl = xlabel('time (s)')\n    sage: yl = ylabel('voltage (mV)')\n    sage: t = title('About as simple as it gets, folks')\n    sage: grid(True)\n    sage: savefig('sage.png')\n```\n\nin sage/plot/plot.py.  However, there are others, which are unfortunately not anywhere near as easy to find, since they don't have a goofy caption.\n\nThis one seems to do it right:\n\n```\nsage: text(\"sage\", (0,0), rgbcolor=(0,0,0)).save(SAGE_TMP + 'a.pdf')\n```\n\nwhich is in the sage/plot/text.py, I think.  \n\nI'm not sure what else there is for sure, but I get at the very least the graphics which are attached.  If you recognize them, post it here.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6864\n\n",
    "created_at": "2009-09-02T14:19:01Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Stop Sage tests from saving things to hard drive",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6864",
    "user": "kcrisman"
}
```
Assignee: tba

As far as I can tell, there are several objects that are saved when you run sage -t.  One example is 

```
    sage: from pylab import *
    sage: t = arange(0.0, 2.0, 0.01)
    sage: s = sin(2*pi*t)
    sage: P = plot(t, s, linewidth=1.0)
    sage: xl = xlabel('time (s)')
    sage: yl = ylabel('voltage (mV)')
    sage: t = title('About as simple as it gets, folks')
    sage: grid(True)
    sage: savefig('sage.png')
```

in sage/plot/plot.py.  However, there are others, which are unfortunately not anywhere near as easy to find, since they don't have a goofy caption.

This one seems to do it right:

```
sage: text("sage", (0,0), rgbcolor=(0,0,0)).save(SAGE_TMP + 'a.pdf')
```

which is in the sage/plot/text.py, I think.  

I'm not sure what else there is for sure, but I get at the very least the graphics which are attached.  If you recognize them, post it here.

Issue created by migration from https://trac.sagemath.org/ticket/6864





---

archive/issue_comments_056644.json:
```json
{
    "body": "Attachment [sage.png](tarball://root/attachments/some-uuid/ticket6864/sage.png) by kcrisman created at 2009-09-02 14:19:17",
    "created_at": "2009-09-02T14:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6864#issuecomment-56644",
    "user": "kcrisman"
}
```

Attachment [sage.png](tarball://root/attachments/some-uuid/ticket6864/sage.png) by kcrisman created at 2009-09-02 14:19:17



---

archive/issue_comments_056645.json:
```json
{
    "body": "Attachment [sage0.png](tarball://root/attachments/some-uuid/ticket6864/sage0.png) by kcrisman created at 2009-09-02 14:19:29",
    "created_at": "2009-09-02T14:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6864#issuecomment-56645",
    "user": "kcrisman"
}
```

Attachment [sage0.png](tarball://root/attachments/some-uuid/ticket6864/sage0.png) by kcrisman created at 2009-09-02 14:19:29



---

archive/issue_comments_056646.json:
```json
{
    "body": "Attachment [0.png](tarball://root/attachments/some-uuid/ticket6864/0.png) by kcrisman created at 2009-09-02 14:19:58",
    "created_at": "2009-09-02T14:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6864#issuecomment-56646",
    "user": "kcrisman"
}
```

Attachment [0.png](tarball://root/attachments/some-uuid/ticket6864/0.png) by kcrisman created at 2009-09-02 14:19:58



---

archive/issue_comments_056647.json:
```json
{
    "body": "Attachment [zz.png](tarball://root/attachments/some-uuid/ticket6864/zz.png) by kcrisman created at 2009-09-02 14:23:08",
    "created_at": "2009-09-02T14:23:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6864#issuecomment-56647",
    "user": "kcrisman"
}
```

Attachment [zz.png](tarball://root/attachments/some-uuid/ticket6864/zz.png) by kcrisman created at 2009-09-02 14:23:08



---

archive/issue_comments_056648.json:
```json
{
    "body": "This ticket is a good idea.  Here are some things I've found:\n\nThe file 'zz.png' is from sage.misc.latex, the function `png`.  By the way, in that same file, the function `_run_latex_` saves its output to a temporary directory like this:\n\n```\n        sage: from sage.misc.latex import _run_latex_, _latex_file_\n        sage: from sage.misc.misc import tmp_dir\n        sage: base = tmp_dir()\n        sage: file = os.path.join(base, \"temp.tex\")\n        sage: O = open(file, 'w')\n        sage: O.write(_latex_file_([ZZ[x], RR])); O.close()\n        sage: _run_latex_(file) # random - depends on whether latex is installed\n        'dvi'\n```\n\nIn the class `ode_solver` in sage.gsl.ode, a file \"sage.png\" is produced: \n\n```\n         By default T.plot_solution() plots the y_0, to plot general y_i use\n         sage: T.plot_solution(i=0, filename='sage.png')\n         sage: T.plot_solution(i=1, filename='sage.png')\n         sage: T.plot_solution(i=2, filename='sage.png')\n```\n\nThis gets overwritten by the \"as simple as it gets\" example, though.\n\n`_import_worksheet_sws` in sage.server.notebook.notebook: produces the file \"tmp.sws\".  (Note that the file is exported and then imported again, so if we change the path name, it needs to be done in both places.)\n\nIn sage.structure.sage_object, we get sage.png and test.sobj, both in the function `save`.\n\n\"0.png\" seems to come from sage.databases.database, in the function `_apply_plot`, maybe.\n\nI'll try to track down the others later.",
    "created_at": "2009-09-02T17:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6864#issuecomment-56648",
    "user": "jhpalmieri"
}
```

This ticket is a good idea.  Here are some things I've found:

The file 'zz.png' is from sage.misc.latex, the function `png`.  By the way, in that same file, the function `_run_latex_` saves its output to a temporary directory like this:

```
        sage: from sage.misc.latex import _run_latex_, _latex_file_
        sage: from sage.misc.misc import tmp_dir
        sage: base = tmp_dir()
        sage: file = os.path.join(base, "temp.tex")
        sage: O = open(file, 'w')
        sage: O.write(_latex_file_([ZZ[x], RR])); O.close()
        sage: _run_latex_(file) # random - depends on whether latex is installed
        'dvi'
```

In the class `ode_solver` in sage.gsl.ode, a file "sage.png" is produced: 

```
         By default T.plot_solution() plots the y_0, to plot general y_i use
         sage: T.plot_solution(i=0, filename='sage.png')
         sage: T.plot_solution(i=1, filename='sage.png')
         sage: T.plot_solution(i=2, filename='sage.png')
```

This gets overwritten by the "as simple as it gets" example, though.

`_import_worksheet_sws` in sage.server.notebook.notebook: produces the file "tmp.sws".  (Note that the file is exported and then imported again, so if we change the path name, it needs to be done in both places.)

In sage.structure.sage_object, we get sage.png and test.sobj, both in the function `save`.

"0.png" seems to come from sage.databases.database, in the function `_apply_plot`, maybe.

I'll try to track down the others later.



---

archive/issue_comments_056649.json:
```json
{
    "body": "Another one is in calculus/calculus.py, line 1200 \n\n```\n(p1+p2).save()\n```\n\nin a long differential equations example.  This is the one labeled sage0.png above.\n\nI think that leaves only sage2.png to be found.  This is a single point, and it's not clear if it comes from plotting or elsewhere. \n\nNotwithstanding that some optional doctests also save...",
    "created_at": "2009-09-02T17:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6864#issuecomment-56649",
    "user": "kcrisman"
}
```

Another one is in calculus/calculus.py, line 1200 

```
(p1+p2).save()
```

in a long differential equations example.  This is the one labeled sage0.png above.

I think that leaves only sage2.png to be found.  This is a single point, and it's not clear if it comes from plotting or elsewhere. 

Notwithstanding that some optional doctests also save...



---

archive/issue_comments_056650.json:
```json
{
    "body": "Replying to [comment:3 kcrisman]:\n>\n> I think that leaves only sage2.png to be found.  This is a single point, and it's not clear if it comes from plotting or elsewhere. \n\nIt's from `visualize_structure` in sage.matrix.matrix2.",
    "created_at": "2009-09-02T19:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6864#issuecomment-56650",
    "user": "jhpalmieri"
}
```

Replying to [comment:3 kcrisman]:
>
> I think that leaves only sage2.png to be found.  This is a single point, and it's not clear if it comes from plotting or elsewhere. 

It's from `visualize_structure` in sage.matrix.matrix2.



---

archive/issue_comments_056651.json:
```json
{
    "body": "Changing assignee from tba to tbd.",
    "created_at": "2009-09-02T20:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6864#issuecomment-56651",
    "user": "jhpalmieri"
}
```

Changing assignee from tba to tbd.



---

archive/issue_comments_056652.json:
```json
{
    "body": "Changing component from documentation to doctest.",
    "created_at": "2009-09-02T20:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6864#issuecomment-56652",
    "user": "jhpalmieri"
}
```

Changing component from documentation to doctest.



---

archive/issue_comments_056653.json:
```json
{
    "body": "Here's a patch.  I couldn't figure out how to fix the one in database.py, so it is now \"not tested\".",
    "created_at": "2009-09-02T20:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6864#issuecomment-56653",
    "user": "jhpalmieri"
}
```

Here's a patch.  I couldn't figure out how to fix the one in database.py, so it is now "not tested".



---

archive/issue_comments_056654.json:
```json
{
    "body": "Attachment [trac_6864-SAGETMP.patch](tarball://root/attachments/some-uuid/ticket6864/trac_6864-SAGETMP.patch) by kcrisman created at 2009-09-14 21:18:33\n\nGreat!  Thanks.   This passes all relevant doctests and nothing appears in my home directory.  I think not testing that example will be okay.",
    "created_at": "2009-09-14T21:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6864#issuecomment-56654",
    "user": "kcrisman"
}
```

Attachment [trac_6864-SAGETMP.patch](tarball://root/attachments/some-uuid/ticket6864/trac_6864-SAGETMP.patch) by kcrisman created at 2009-09-14 21:18:33

Great!  Thanks.   This passes all relevant doctests and nothing appears in my home directory.  I think not testing that example will be okay.



---

archive/issue_comments_056655.json:
```json
{
    "body": "Merged `trac_6864-SAGETMP.patch`.",
    "created_at": "2009-09-16T04:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6864#issuecomment-56655",
    "user": "mvngu"
}
```

Merged `trac_6864-SAGETMP.patch`.



---

archive/issue_comments_056656.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-16T04:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6864#issuecomment-56656",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056657.json:
```json
{
    "body": "See #7059 for a followup.",
    "created_at": "2009-09-29T03:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6864#issuecomment-56657",
    "user": "jhpalmieri"
}
```

See #7059 for a followup.
