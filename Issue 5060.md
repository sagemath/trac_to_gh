# Issue 5060: setup.py dependency checking detects unexpected dependencies

Issue created by migration from Trac.

Original creator: sbarthelemy

Original creation time: 2009-01-23 00:26:01

Assignee: mabshoff

using sage 3.2.3, I'm trying to build a new module with a .pxd file containing this line

```
 #include "gmp.h"
```

note that the line is commented. The build fails with the following traceback

```
 sage -b

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Traceback (most recent call last):
  File "setup.py", line 503, in <module>
    queue = compile_command_list(ext_modules, deps)
  File "setup.py", line 463, in compile_command_list
    dep_file, dep_time = deps.newest_dep(f)
  File "setup.py", line 378, in newest_dep
    for f in self.all_deps(filename):
  File "setup.py", line 361, in all_deps
    deps.update(self.all_deps(f, path))
  File "setup.py", line 359, in all_deps
    for f in self.immediate_deps(filename):
  File "setup.py", line 341, in immediate_deps
    self._deps[filename] = self.parse_deps(filename)
  File "setup.py", line 331, in parse_deps
    raise IOError, "could not find dependency %s included in %s."%(path, filename)
IOError: could not find dependency gmp.h included in sage/geometry/cdd.pxd.
sage: There was an error installing modified sage library code.
```


There is probably a problem with the regexp on line 228 of [setup.py](http://www.sagemath.org/hg/sage-main/file/b0aa7ef45b3c/setup.py). One can reprouce the bug with this snipet

```
dep_regex = re.compile(r'^ *(?:cimport +(\S+))|(?:from +(\S+) *cimport)|(?:include *[\'"]([^\'"]+)[\'"])', re.M)
m.groups()for m in dep_regex.finditer('#include "gmp.h"'):                      
    m.groups()                                                        
```

which results in

```
(None, None, 'gmp.h')
```




---

Comment by cwitty created at 2009-01-23 00:51:58

I think that modifying the regex like this (adding two `'^'` characters) will fix the problem.  (It fixes the above test case, but I don't have time to do a real test, or submit a real patch, right now.)

```
r'^ *(?:cimport +(\S+))|^(?:from +(\S+) *cimport)|^(?:include *[\'"]([^\'"]+)[\'"])'
```



---

Comment by sbarthelemy created at 2009-01-23 03:45:06

some more thoughts

1. the include keyword is deprecated [cython doc](http://docs.cython.org/docs/language_basics.html?highlight=include#the-include-statement), 

2. the current regexp misses other cython patterns that involve dependancies:

```
cimport mod1, mod2
```

and

```
cdef extern from "toto.h":
    ....
```

Here is a first attempt to fix this, 

```
import re
dep_regex = re.compile(r'^ *(?:(?:(?:(?:include)|(?:cdef +extern + from)) +[\'"]([^\'"]+)[\'"])|(?:from +(\w+) *cimport)|(?:cimport +([^ \t\n\r\f\v,]+)(?: *, *([^ \t\n\r\f\v,]+))*))',  re.MULTILINE)

teststr = """include "yes1.h"
include "yes2.h" 
 include "yes3.h"
 include 'yes4.h'
#include "no5.h"
 # include "no6.h"
cimport yes7
 cimport yes8 
#cimport no9
# cimport no10
from yes11 cimport toto
from yes12 cimport toto as tata
#from no13 cimport toto as tata
cdef extern from "yes14.h"
cimport yes15 , yes15b
cimport yes16, yes16b
cimport yes17, yes17b , yes17c

"""

print 'toto'
for m in dep_regex.finditer(teststr):
    print m.groups()
```


However, for some reason, it doesn't catch yes14.h nor yes17b. So this is not yet functional (nor elegant). Any suggestion is welcome.


---

Attachment

The original bug was due to the fact that "^ *" was only required for the first grouping. 

Given that more than one module could be cimported in a single statement, it took an extra loop in the parsing code as well.


---

Comment by craigcitro created at 2009-01-24 13:17:23

This looks good. Man, that is one serious regular expression.


---

Comment by mabshoff created at 2009-01-24 18:06:29

Merged in Sage 3.3.alpha2

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 18:06:29

Resolution: fixed


---

Comment by sbarthelemy created at 2009-01-26 13:50:37

Changing status from closed to reopened.


---

Comment by sbarthelemy created at 2009-01-26 13:50:37

Hello, 

reading the code, I see another problem if ones has the following line in its .pyx:

```
cimport mod#mycomment
```

I such a case, we'll look for a dependency mod#mycomment.pxd instead of mod.pxd.

Otherwise, the patch solves the aforementioned problems.

Cheers


---

Comment by sbarthelemy created at 2009-01-26 13:50:37

Resolution changed from fixed to 


---

Comment by mhansen created at 2009-01-26 16:45:05

Please do not reopen closed tickets -- it makes things much more difficult for Michael.  Instead, just open a new one. 

I've opened #5103 for this.


---

Comment by mhansen created at 2009-01-26 16:45:05

Resolution: fixed


---

Comment by craigcitro created at 2009-01-26 16:47:54

Actually, I'm going to reclose this ticket, since the original issues reported are fixed, and I've opened #5104 for this new issue.


---

Comment by craigcitro created at 2009-01-26 16:48:52

Oops. Mike, I'm closing your ticket as a dupe, since I spent more time reformatting the text in mine. `:P`
