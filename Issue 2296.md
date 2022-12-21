# Issue 2296: setup.py -- another issue with cython dependency checking

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-24 20:11:43

Assignee: cwitty

I've attached a patch that might fix the following problem:

```
>
> > Installing c_lib
> > scons: `install' is up to date.
> > Traceback (most recent call last):
> >   File "setup.py", line 1217, in <module>
> >     deps = create_deps(ext_modules)
> >   File "setup.py", line 1208, in create_deps
> >     deps_graph(deps, f, visited)
> >   File "setup.py", line 1175, in deps_graph
> >     this_deps = search_all_includes(f)
> >   File "setup.py", line 1099, in search_all_includes
> >     S = open(filename).readlines()
> > IOError: [Errno 2] No such file or directory: 'sage-main/sage/modules/
> > free_module_element.pyx'
> > sage: There was an error installing modified sage library code.
>
> > ERROR installing SAGE
>
> Hi,
>
> that is cause by #2180. There is a patch for it, but the short
> solution is to touch the pyrex file in question. Then everything is
> back to normal.
>
> Cheers,
>
> Michael

Burcin did pop up in IRC a little while ago and reported the same
error. Neither touching the file, not a "sage -ba" nor applying the
patch from #2180 fixes the problem, so I am fresh out of ideas. It
only seems to happen on updates, i.e. in the other cases I saw the
issue a touching of a single file was sufficient. So there is maybe
more than one bug lurking in that code. Since I have been unable to
reproduce the harder problem yet any input (or even better solution)
is welcome :)
```




---

Attachment

Please check out #2295 by burcin, which seems to nail the real culprit, i.e. the symlink problem.

Cheers,

Michael


---

Comment by was created at 2008-02-24 20:19:34

#2295 is better.  This is invalid.


---

Comment by was created at 2008-02-24 20:19:34

Resolution: invalid
