# Issue 8478: Programming tutorial page seems incorrect

Issue created by migration from https://trac.sagemath.org/ticket/8478

Original creator: lesshaste

Original creation time: 2010-03-07 20:11:17

Assignee: mvngu

The section Standalone Python/Sage Scripts at http://www.sagemath.org/doc/tutorial/programming.html#section-loadattach seems to have two problems (profuse apologies if these are actually user errors).

1) #!/usr/bin/env sage -python   doesn't work in linux as shebang can't take two arguments. One simple workaround is to use #!/path_to_sage -python
2) The script itself seems broken. Testing it using sage 4.3.3

./factor 2006

works as expected.

But ./factor "32*x^5-1"  gives
Traceback (most recent call last):
  File "./factor", line 11, in <module>
    print factor(sage_eval(sys.argv[1]))
  File "/opt/sage-4.3.3-linux-32bit-ubuntu_9.10-i686-Linux/local/lib/python2.6/site-packages/sage/misc/sage_eval.py", line 199, in sage_eval
    return eval(source, sage.all.__dict__, locals)
  File "<string>", line 1, in <module>
NameError: name 'x' is not defined


---

Comment by wjp created at 2010-03-07 20:40:39

A better way of handling the `#!` problem might be to use `#!/usr/bin/env sage-python`.


---

Comment by edgimar created at 2011-08-08 22:01:50

Here's a version which should work correctly (at least with sage 5.8):



```/usr/bin/env sage

import sys
from sage.all import *

if len(sys.argv) != 2:
    print "Usage: %s <n>"%sys.argv[0]
    print "Outputs the prime factorization of n."
    sys.exit(1)
    
try:
    e = sage_eval(sys.argv[1])
except NameError:
    e = symbolic_expression(sys.argv[1])

print factor(e)

```



---

Comment by kcrisman created at 2013-08-02 15:57:45

See also [this commit](https://bitbucket.org/edgimar/sage-main/commits/8f2d381fae7eb0e8de92ecab9f12f4b1d3ef951e) on bitbucket.
