# Issue 4638: Sage 3.2->3.2.a2 upgrade failure

Issue created by migration from https://trac.sagemath.org/ticket/4638

Original creator: mabshoff

Original creation time: 2008-11-27 08:25:56

Assignee: was

Do the following: 

 * build Sage 3.2
 * install the updates scripts.spkg: sage -i http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/sage-3.2.1.alpha2/spkg/standard/sage_scripts-3.2.1.alpha2
 * upgrade to Sage 3.2.a2: ./sage -i http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/sage-3.2.1.alpha2/

Things go boom (due to a dependency bug in setup.py - it has been fixed in 3.2.1.alpha1, but somehow that setup.py is not used):

```
Building sage/matrix/action.pyx because it depends on sage/structure/parent.pxd.
Traceback (most recent call last):
  File "setup.py", line 486, in <module>
    queue = compile_command_list(ext_modules, deps)
  File "setup.py", line 456, in compile_command_list
    dep_file, dep_time = deps.newest_dep(f)
  File "setup.py", line 371, in newest_dep
    for f in self.all_deps(filename):
  File "setup.py", line 354, in all_deps
    deps.update(self.all_deps(f, path))
  File "setup.py", line 352, in all_deps
    for f in self.immediate_deps(filename):
  File "setup.py", line 334, in immediate_deps
    self._deps[filename] = self.parse_deps(filename)
  File "setup.py", line 290, in parse_deps
    f = open(filename)
IOError: [Errno 2] No such file or directory: 'sage/rings/mpfr.pxi'
sage: There was an error installing modified sage library code.
```



Then sage-3.2.1.alpha0.spkg as well as the doc.spkg are missing. Deleting the Cython cache and a sage -ba gets you a working Sage again.

But make is unhappy:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.final$ make
cd spkg && ./install all 2>&1 | tee -a ../install.log
/bin/ls: doc-*.spkg: No such file or directory
/bin/ls: examples-*.spkg: No such file or directory
/bin/ls: sage-*.spkg: No such file or directory
make[1]: Entering directory `/scratch/mabshoff/release-cycle/sage-3.2.final/spkg'
standard/deps:310: warning: overriding commands for target `installed/'
standard/deps:177: warning: ignoring old commands for target `installed/'
standard/deps:366: warning: overriding commands for target `installed/'
standard/deps:310: warning: ignoring old commands for target `installed/'
standard/deps:370: warning: overriding commands for target `installed/'
standard/deps:366: warning: ignoring old commands for target `installed/'
make[1]: Circular installed/ <- installed/ dependency dropped.
make[1]: Circular installed/ <- installed/ dependency dropped.
make[1]: Nothing to be done for `all'.
make[1]: Leaving directory `/scratch/mabshoff/release-cycle/sage-3.2.final/spkg'

real	0m0.008s
user	0m0.004s
sys	0m0.004s
To install gap, gp, singular, etc., scripts
in a standard bin directory, start sage and
type something like
   sage: install_scripts('/usr/local/bin')
at the SAGE command prompt.
```

Doing another

 * ./sage -i http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/sage-3.2.1.alpha2/

replaces the missing spkgs and everything is fine.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-01 09:19:34

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-12-01 09:19:34

This might become a problem when running -upgrade from 3.2 to 3.2.1, but we will see. For now reassign it to 3.2.1. Once we have tested the 3.2 upgrade to 3.2.1.final we will see if we have to do anything special here.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-01 09:19:34

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-12-02 05:34:21

Resolution: wontfix


---

Comment by mabshoff created at 2008-12-02 05:34:21

wontfix since this was unsupported anyway. Upgrades from 3.2 to 3.2.1 are working.

Cheers,

Michael
