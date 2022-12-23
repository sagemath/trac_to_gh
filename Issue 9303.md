# Issue 9303: dumb (easy-to-fix) mistake in sage notebook js.py file

Issue created by migration from https://trac.sagemath.org/ticket/9303

Original creator: was

Original creation time: 2010-06-22 04:36:02

Assignee: jason, was

Reported by Ralf Hemmecke:


```
Oh, it's a bug. It hit me again... :-(

sagenb-0.8.p2/src/sagenb/sagenb/notebook/js.py

says

try:
   from sage.misc.misc import SAGE_ROOT
   from pkg_resources import Requirement, working_set
   sagenb_path = working_set.find(Requirement.parse('sagenb')).location
   debug_mode = SAGE_ROOT not in os.path.realpath(sagenb_path)
except AttributeError, ImportError:
   debug_mode = False

But according to what I cite below, it should rather be

except (AttributeError, ImportError):

Ralf

http://docs.python.org/tutorial/errors.html

A try statement may have more than one except clause, to specify
handlers for different exceptions. At most one handler will be executed.
Handlers only handle exceptions that occur in the corresponding try
clause, not in other handlers of the same try statement. An except
clause may name multiple exceptions as a parenthesized tuple, for example:

... except (RuntimeError, TypeError, NameError):
...     pass
```



---

Comment by was created at 2010-06-22 04:57:11

Resolution: invalid


---

Comment by was created at 2010-06-22 04:57:11


```
What happens if the bug was fixed before the track ticket was reported? :)

http://boxen.math.washington.edu:8100/rev/65d6838cefd8

Ondrej
```

