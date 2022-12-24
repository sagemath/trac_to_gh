# Issue 8478: Programming tutorial page seems incorrect

archive/issues_008478.json:
```json
{
    "body": "Assignee: mvngu\n\nThe section Standalone Python/Sage Scripts at http://www.sagemath.org/doc/tutorial/programming.html#section-loadattach seems to have two problems (profuse apologies if these are actually user errors).\n\n1) #!/usr/bin/env sage -python   doesn't work in linux as shebang can't take two arguments. One simple workaround is to use #!/path_to_sage -python\n2) The script itself seems broken. Testing it using sage 4.3.3\n\n./factor 2006\n\nworks as expected.\n\nBut ./factor \"32*x^5-1\"  gives\nTraceback (most recent call last):\n  File \"./factor\", line 11, in <module>\n    print factor(sage_eval(sys.argv[1]))\n  File \"/opt/sage-4.3.3-linux-32bit-ubuntu_9.10-i686-Linux/local/lib/python2.6/site-packages/sage/misc/sage_eval.py\", line 199, in sage_eval\n    return eval(source, sage.all.__dict__, locals)\n  File \"<string>\", line 1, in <module>\nNameError: name 'x' is not defined\n\nIssue created by migration from https://trac.sagemath.org/ticket/8478\n\n",
    "created_at": "2010-03-07T20:11:17Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "Programming tutorial page seems incorrect",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8478",
    "user": "lesshaste"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/8478





---

archive/issue_comments_076413.json:
```json
{
    "body": "A better way of handling the `#!` problem might be to use `#!/usr/bin/env sage-python`.",
    "created_at": "2010-03-07T20:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8478#issuecomment-76413",
    "user": "@wjp"
}
```

A better way of handling the `#!` problem might be to use `#!/usr/bin/env sage-python`.



---

archive/issue_comments_076414.json:
```json
{
    "body": "Here's a version which should work correctly (at least with sage 5.8):\n\n\n\n```/usr/bin/env sage\n\nimport sys\nfrom sage.all import *\n\nif len(sys.argv) != 2:\n    print \"Usage: %s <n>\"%sys.argv[0]\n    print \"Outputs the prime factorization of n.\"\n    sys.exit(1)\n    \ntry:\n    e = sage_eval(sys.argv[1])\nexcept NameError:\n    e = symbolic_expression(sys.argv[1])\n\nprint factor(e)\n\n```\n",
    "created_at": "2011-08-08T22:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8478#issuecomment-76414",
    "user": "edgimar"
}
```

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

archive/issue_comments_076415.json:
```json
{
    "body": "See also [this commit](https://bitbucket.org/edgimar/sage-main/commits/8f2d381fae7eb0e8de92ecab9f12f4b1d3ef951e) on bitbucket.",
    "created_at": "2013-08-02T15:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8478#issuecomment-76415",
    "user": "@kcrisman"
}
```

See also [this commit](https://bitbucket.org/edgimar/sage-main/commits/8f2d381fae7eb0e8de92ecab9f12f4b1d3ef951e) on bitbucket.
