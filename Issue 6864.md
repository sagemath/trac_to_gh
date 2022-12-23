# Issue 6864: Stop Sage tests from saving things to hard drive

Issue created by migration from https://trac.sagemath.org/ticket/6864

Original creator: kcrisman

Original creation time: 2009-09-02 14:19:01

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


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by jhpalmieri created at 2009-09-02 17:16:34

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

Comment by kcrisman created at 2009-09-02 17:42:38

Another one is in calculus/calculus.py, line 1200 

```
(p1+p2).save()
```

in a long differential equations example.  This is the one labeled sage0.png above.

I think that leaves only sage2.png to be found.  This is a single point, and it's not clear if it comes from plotting or elsewhere. 

Notwithstanding that some optional doctests also save...


---

Comment by jhpalmieri created at 2009-09-02 19:01:48

Replying to [comment:3 kcrisman]:
>
> I think that leaves only sage2.png to be found.  This is a single point, and it's not clear if it comes from plotting or elsewhere. 

It's from `visualize_structure` in sage.matrix.matrix2.


---

Comment by jhpalmieri created at 2009-09-02 20:26:44

Changing assignee from tba to tbd.


---

Comment by jhpalmieri created at 2009-09-02 20:26:44

Changing component from documentation to doctest.


---

Comment by jhpalmieri created at 2009-09-02 20:26:44

Here's a patch.  I couldn't figure out how to fix the one in database.py, so it is now "not tested".


---

Attachment

Great!  Thanks.   This passes all relevant doctests and nothing appears in my home directory.  I think not testing that example will be okay.


---

Comment by mvngu created at 2009-09-16 04:02:30

Merged `trac_6864-SAGETMP.patch`.


---

Comment by mvngu created at 2009-09-16 04:02:30

Resolution: fixed


---

Comment by jhpalmieri created at 2009-09-29 03:01:06

See #7059 for a followup.
