# Issue 5060: setup.py dependency checking detects unexpected dependencies

archive/issues_005060.json:
```json
{
    "body": "Assignee: mabshoff\n\nusing sage 3.2.3, I'm trying to build a new module with a .pxd file containing this line\n\n```\n #include \"gmp.h\"\n```\n\nnote that the line is commented. The build fails with the following traceback\n\n```\n sage -b\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nTraceback (most recent call last):\n  File \"setup.py\", line 503, in <module>\n    queue = compile_command_list(ext_modules, deps)\n  File \"setup.py\", line 463, in compile_command_list\n    dep_file, dep_time = deps.newest_dep(f)\n  File \"setup.py\", line 378, in newest_dep\n    for f in self.all_deps(filename):\n  File \"setup.py\", line 361, in all_deps\n    deps.update(self.all_deps(f, path))\n  File \"setup.py\", line 359, in all_deps\n    for f in self.immediate_deps(filename):\n  File \"setup.py\", line 341, in immediate_deps\n    self._deps[filename] = self.parse_deps(filename)\n  File \"setup.py\", line 331, in parse_deps\n    raise IOError, \"could not find dependency %s included in %s.\"%(path, filename)\nIOError: could not find dependency gmp.h included in sage/geometry/cdd.pxd.\nsage: There was an error installing modified sage library code.\n```\n\n\nThere is probably a problem with the regexp on line 228 of [setup.py](http://www.sagemath.org/hg/sage-main/file/b0aa7ef45b3c/setup.py). One can reprouce the bug with this snipet\n\n```\ndep_regex = re.compile(r'^ *(?:cimport +(\\S+))|(?:from +(\\S+) *cimport)|(?:include *[\\'\"]([^\\'\"]+)[\\'\"])', re.M)\nm.groups()for m in dep_regex.finditer('#include \"gmp.h\"'):                      \n    m.groups()                                                        \n```\n\nwhich results in\n\n```\n(None, None, 'gmp.h')\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5060\n\n",
    "created_at": "2009-01-23T00:26:01Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "setup.py dependency checking detects unexpected dependencies",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5060",
    "user": "https://trac.sagemath.org/admin/accounts/users/sbarthelemy"
}
```
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



Issue created by migration from https://trac.sagemath.org/ticket/5060





---

archive/issue_comments_038467.json:
```json
{
    "body": "I think that modifying the regex like this (adding two `'^'` characters) will fix the problem.  (It fixes the above test case, but I don't have time to do a real test, or submit a real patch, right now.)\n\n```\nr'^ *(?:cimport +(\\S+))|^(?:from +(\\S+) *cimport)|^(?:include *[\\'\"]([^\\'\"]+)[\\'\"])'\n```\n",
    "created_at": "2009-01-23T00:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5060#issuecomment-38467",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I think that modifying the regex like this (adding two `'^'` characters) will fix the problem.  (It fixes the above test case, but I don't have time to do a real test, or submit a real patch, right now.)

```
r'^ *(?:cimport +(\S+))|^(?:from +(\S+) *cimport)|^(?:include *[\'"]([^\'"]+)[\'"])'
```




---

archive/issue_comments_038468.json:
```json
{
    "body": "some more thoughts\n\n1. the include keyword is deprecated [cython doc](http://docs.cython.org/docs/language_basics.html?highlight=include#the-include-statement), \n\n2. the current regexp misses other cython patterns that involve dependancies:\n\n```\ncimport mod1, mod2\n```\n\nand\n\n```\ncdef extern from \"toto.h\":\n    ....\n```\n\nHere is a first attempt to fix this, \n\n```\nimport re\ndep_regex = re.compile(r'^ *(?:(?:(?:(?:include)|(?:cdef +extern + from)) +[\\'\"]([^\\'\"]+)[\\'\"])|(?:from +(\\w+) *cimport)|(?:cimport +([^ \\t\\n\\r\\f\\v,]+)(?: *, *([^ \\t\\n\\r\\f\\v,]+))*))',  re.MULTILINE)\n\nteststr = \"\"\"include \"yes1.h\"\ninclude \"yes2.h\" \n include \"yes3.h\"\n include 'yes4.h'\n#include \"no5.h\"\n # include \"no6.h\"\ncimport yes7\n cimport yes8 \n#cimport no9\n# cimport no10\nfrom yes11 cimport toto\nfrom yes12 cimport toto as tata\n#from no13 cimport toto as tata\ncdef extern from \"yes14.h\"\ncimport yes15 , yes15b\ncimport yes16, yes16b\ncimport yes17, yes17b , yes17c\n\n\"\"\"\n\nprint 'toto'\nfor m in dep_regex.finditer(teststr):\n    print m.groups()\n```\n\n\nHowever, for some reason, it doesn't catch yes14.h nor yes17b. So this is not yet functional (nor elegant). Any suggestion is welcome.",
    "created_at": "2009-01-23T03:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5060#issuecomment-38468",
    "user": "https://trac.sagemath.org/admin/accounts/users/sbarthelemy"
}
```

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

archive/issue_events_011661.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T07:56:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5060#event-11661"
}
```



---

archive/issue_comments_038469.json:
```json
{
    "body": "Attachment [5060-deps.patch](tarball://root/attachments/some-uuid/ticket5060/5060-deps.patch) by @robertwb created at 2009-01-23 13:16:08\n\nThe original bug was due to the fact that \"^ *\" was only required for the first grouping. \n\nGiven that more than one module could be cimported in a single statement, it took an extra loop in the parsing code as well.",
    "created_at": "2009-01-23T13:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5060#issuecomment-38469",
    "user": "https://github.com/robertwb"
}
```

Attachment [5060-deps.patch](tarball://root/attachments/some-uuid/ticket5060/5060-deps.patch) by @robertwb created at 2009-01-23 13:16:08

The original bug was due to the fact that "^ *" was only required for the first grouping. 

Given that more than one module could be cimported in a single statement, it took an extra loop in the parsing code as well.



---

archive/issue_comments_038470.json:
```json
{
    "body": "This looks good. Man, that is one serious regular expression.",
    "created_at": "2009-01-24T13:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5060#issuecomment-38470",
    "user": "https://github.com/craigcitro"
}
```

This looks good. Man, that is one serious regular expression.



---

archive/issue_comments_038471.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T18:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5060#issuecomment-38471",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2

Cheers,

Michael



---

archive/issue_comments_038472.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T18:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5060#issuecomment-38472",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_011662.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T18:06:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5060#event-11662"
}
```



---

archive/issue_comments_038473.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-01-26T13:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5060#issuecomment-38473",
    "user": "https://trac.sagemath.org/admin/accounts/users/sbarthelemy"
}
```

Changing status from closed to reopened.



---

archive/issue_events_011663.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/sbarthelemy",
    "created_at": "2009-01-26T13:50:37Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5060#event-11663"
}
```



---

archive/issue_comments_038474.json:
```json
{
    "body": "Hello, \n\nreading the code, I see another problem if ones has the following line in its .pyx:\n\n```\ncimport mod#mycomment\n```\n\nI such a case, we'll look for a dependency mod#mycomment.pxd instead of mod.pxd.\n\nOtherwise, the patch solves the aforementioned problems.\n\nCheers",
    "created_at": "2009-01-26T13:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5060#issuecomment-38474",
    "user": "https://trac.sagemath.org/admin/accounts/users/sbarthelemy"
}
```

Hello, 

reading the code, I see another problem if ones has the following line in its .pyx:

```
cimport mod#mycomment
```

I such a case, we'll look for a dependency mod#mycomment.pxd instead of mod.pxd.

Otherwise, the patch solves the aforementioned problems.

Cheers



---

archive/issue_comments_038475.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-01-26T13:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5060#issuecomment-38475",
    "user": "https://trac.sagemath.org/admin/accounts/users/sbarthelemy"
}
```

Resolution changed from fixed to 



---

archive/issue_events_011664.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-01-26T16:45:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5060#event-11664"
}
```



---

archive/issue_comments_038476.json:
```json
{
    "body": "Please do not reopen closed tickets -- it makes things much more difficult for Michael.  Instead, just open a new one. \n\nI've opened #5103 for this.",
    "created_at": "2009-01-26T16:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5060#issuecomment-38476",
    "user": "https://github.com/mwhansen"
}
```

Please do not reopen closed tickets -- it makes things much more difficult for Michael.  Instead, just open a new one. 

I've opened #5103 for this.



---

archive/issue_comments_038477.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-26T16:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5060#issuecomment-38477",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_038478.json:
```json
{
    "body": "Actually, I'm going to reclose this ticket, since the original issues reported are fixed, and I've opened #5104 for this new issue.",
    "created_at": "2009-01-26T16:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5060#issuecomment-38478",
    "user": "https://github.com/craigcitro"
}
```

Actually, I'm going to reclose this ticket, since the original issues reported are fixed, and I've opened #5104 for this new issue.



---

archive/issue_comments_038479.json:
```json
{
    "body": "Oops. Mike, I'm closing your ticket as a dupe, since I spent more time reformatting the text in mine. `:P`",
    "created_at": "2009-01-26T16:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5060#issuecomment-38479",
    "user": "https://github.com/craigcitro"
}
```

Oops. Mike, I'm closing your ticket as a dupe, since I spent more time reformatting the text in mine. `:P`
