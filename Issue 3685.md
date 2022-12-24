# Issue 3685: make damned sure that "import sage.all" doesn't import ipython

archive/issues_003685.json:
```json
{
    "body": "Assignee: cwitty\n\nMake sure that doing this does not import ipython:\n\n\n```\nteragon-2:~ was$ sage -python\nPython 2.5.2 (r252:60911, Jul 10 2008, 00:31:06) \n[GCC 4.0.1 (Apple Inc. build 5465)] on darwin\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n>>> import sage.all\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3685\n\n",
    "created_at": "2008-07-20T14:49:23Z",
    "labels": [
        "misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "make damned sure that \"import sage.all\" doesn't import ipython",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3685",
    "user": "@williamstein"
}
```
Assignee: cwitty

Make sure that doing this does not import ipython:


```
teragon-2:~ was$ sage -python
Python 2.5.2 (r252:60911, Jul 10 2008, 00:31:06) 
[GCC 4.0.1 (Apple Inc. build 5465)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sage.all
```


Issue created by migration from https://trac.sagemath.org/ticket/3685





---

archive/issue_comments_026108.json:
```json
{
    "body": "Here is how Ondrej Certik verifies that sage.all was importing ipython in sage-3.0.5:\n\n```\nI don't want to have anything in common with ipython, but sage invokes\nit on import sage.all, as can be checked easily:\n\nondra@fuji:~/ext/sage$ . local/bin/sage-env\nondra@fuji:~/ext/sage$ python\nPython 2.5.2 (r252:60911, Jul 11 2008, 05:28:36)\n[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n>>> import sage.all\n>>>\n\nThen apply this patch:\n\n--- /tmp/genutils.py    2008-07-20 16:33:15.000000000 +0200\n+++ local/lib/python2.5/site-packages/IPython/genutils.py       2008-07-20\n16:33:26.553433732 +0200\n@@ -54,6 +54,7 @@\n        if not hasattr(stream,'write') or not hasattr(stream,'flush'):\n            stream = fallback\n        self.stream = stream\n+        stop\n        self._swrite = stream.write\n        self.flush = stream.flush\n\n\n\nand:\n\nondra@fuji:~/ext/sage$ python\nPython 2.5.2 (r252:60911, Jul 11 2008, 05:28:36)\n[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n>>> import sage.all\nTraceback (most recent call last):\n File \"<stdin>\", line 1, in <module>\n File \"/home/ondra/ext/sage/local/lib/python2.5/site-packages/sage/all.py\",\nline 58, in <module>\n   from sage.misc.all       import *         # takes a while\n File \"/home/ondra/ext/sage/local/lib/python2.5/site-packages/sage/misc/all.py\",\nline 15, in <module>\n   from sage_timeit_class import timeit\n File \"sage_timeit_class.pyx\", line 3, in sage.misc.sage_timeit_class\n(sage/misc/sage_timeit_class.c:485)\n File \"/home/ondra/ext/sage/local/lib/python2.5/site-packages/sage/misc/sage_timeit.py\",\nline 12, in <module>\n   import timeit as timeit_, time, math, preparser, interpreter\n File \"/home/ondra/ext/sage/local/lib/python2.5/site-packages/sage/misc/interpreter.py\",\nline 108, in <module>\n   from IPython.iplib import InteractiveShell\n File \"/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/__init__.py\",\nline 57, in <module>\n   __import__(name,glob,loc,[])\n File \"/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/ipstruct.py\",\nline 22, in <module>\n   from IPython.genutils import list2dict2\n File \"/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/genutils.py\",\nline 95, in <module>\n   Term = IOTerm()\n File \"/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/genutils.py\",\nline 90, in __init__\n   self.cin  = IOStream(cin,sys.stdin)\n File \"/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/genutils.py\",\nline 57, in __init__\n   stop\nNameError: global name 'stop' is not defined\n```\n",
    "created_at": "2008-07-20T14:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26108",
    "user": "@williamstein"
}
```

Here is how Ondrej Certik verifies that sage.all was importing ipython in sage-3.0.5:

```
I don't want to have anything in common with ipython, but sage invokes
it on import sage.all, as can be checked easily:

ondra@fuji:~/ext/sage$ . local/bin/sage-env
ondra@fuji:~/ext/sage$ python
Python 2.5.2 (r252:60911, Jul 11 2008, 05:28:36)
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sage.all
>>>

Then apply this patch:

--- /tmp/genutils.py    2008-07-20 16:33:15.000000000 +0200
+++ local/lib/python2.5/site-packages/IPython/genutils.py       2008-07-20
16:33:26.553433732 +0200
@@ -54,6 +54,7 @@
        if not hasattr(stream,'write') or not hasattr(stream,'flush'):
            stream = fallback
        self.stream = stream
+        stop
        self._swrite = stream.write
        self.flush = stream.flush



and:

ondra@fuji:~/ext/sage$ python
Python 2.5.2 (r252:60911, Jul 11 2008, 05:28:36)
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sage.all
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/sage/all.py",
line 58, in <module>
   from sage.misc.all       import *         # takes a while
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/sage/misc/all.py",
line 15, in <module>
   from sage_timeit_class import timeit
 File "sage_timeit_class.pyx", line 3, in sage.misc.sage_timeit_class
(sage/misc/sage_timeit_class.c:485)
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/sage/misc/sage_timeit.py",
line 12, in <module>
   import timeit as timeit_, time, math, preparser, interpreter
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/sage/misc/interpreter.py",
line 108, in <module>
   from IPython.iplib import InteractiveShell
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/__init__.py",
line 57, in <module>
   __import__(name,glob,loc,[])
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/ipstruct.py",
line 22, in <module>
   from IPython.genutils import list2dict2
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/genutils.py",
line 95, in <module>
   Term = IOTerm()
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/genutils.py",
line 90, in __init__
   self.cin  = IOStream(cin,sys.stdin)
 File "/home/ondra/ext/sage/local/lib/python2.5/site-packages/IPython/genutils.py",
line 57, in __init__
   stop
NameError: global name 'stop' is not defined
```




---

archive/issue_comments_026109.json:
```json
{
    "body": "I think this shouldn't go into 3.0.6 since it could introduce bugs, as it touches several files.\nThat said, it's a smallish patch I made in 30 minutes.  So it's not crazy complicated.  It's just dangerous.",
    "created_at": "2008-07-20T15:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26109",
    "user": "@williamstein"
}
```

I think this shouldn't go into 3.0.6 since it could introduce bugs, as it touches several files.
That said, it's a smallish patch I made in 30 minutes.  So it's not crazy complicated.  It's just dangerous.



---

archive/issue_comments_026110.json:
```json
{
    "body": "Attachment [sage-3685.patch](tarball://root/attachments/some-uuid/ticket3685/sage-3685.patch) by @mwhansen created at 2008-08-04 09:01:54\n\nThis patch causes some problems on my machine.\n\n1) Sage segfaults at exit.\n\n2) When doing sage -t, I get the following problem for every file:\n\n```\nsage -t  devel/sage-combinat/sage/combinat/root_system/all.pyTraceback (most recent call last):\n  File \"/opt/sage/tmp/.doctest_all.py\", line 2, in <module>\n    from sage.all_cmdline import *; \n  File \"/opt/sage/local/lib/python2.5/site-packages/sage/all_cmdline.py\", line 14, in <module>\n    from sage.all import *\n  File \"/opt/sage/local/lib/python2.5/site-packages/sage/all.py\", line 72, in <module>\n    from sage.rings.all      import *\n  File \"/opt/sage/local/lib/python2.5/site-packages/sage/rings/all.py\", line 94, in <module>\n    from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,\n  File \"/opt/sage/local/lib/python2.5/site-packages/sage/rings/qqbar.py\", line 1163, in <module>\n    QQxy = QQ['x', 'y']\n  File \"ring.pyx\", line 146, in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:1851)\n  File \"/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py\", line 303, in PolynomialRing\n    R = _multi_variate(base_ring, names, n, sparse, order)        \n  File \"/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py\", line 409, in _multi_variate\n    from sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular\n```\n",
    "created_at": "2008-08-04T09:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26110",
    "user": "@mwhansen"
}
```

Attachment [sage-3685.patch](tarball://root/attachments/some-uuid/ticket3685/sage-3685.patch) by @mwhansen created at 2008-08-04 09:01:54

This patch causes some problems on my machine.

1) Sage segfaults at exit.

2) When doing sage -t, I get the following problem for every file:

```
sage -t  devel/sage-combinat/sage/combinat/root_system/all.pyTraceback (most recent call last):
  File "/opt/sage/tmp/.doctest_all.py", line 2, in <module>
    from sage.all_cmdline import *; 
  File "/opt/sage/local/lib/python2.5/site-packages/sage/all_cmdline.py", line 14, in <module>
    from sage.all import *
  File "/opt/sage/local/lib/python2.5/site-packages/sage/all.py", line 72, in <module>
    from sage.rings.all      import *
  File "/opt/sage/local/lib/python2.5/site-packages/sage/rings/all.py", line 94, in <module>
    from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,
  File "/opt/sage/local/lib/python2.5/site-packages/sage/rings/qqbar.py", line 1163, in <module>
    QQxy = QQ['x', 'y']
  File "ring.pyx", line 146, in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:1851)
  File "/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py", line 303, in PolynomialRing
    R = _multi_variate(base_ring, names, n, sparse, order)        
  File "/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py", line 409, in _multi_variate
    from sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular
```




---

archive/issue_comments_026111.json:
```json
{
    "body": "Mike said:\n> 1) Sage segfaults at exit.\n> 2) When doing sage -t, I get the following problem for every file: \n\nMike, (1) what is your system?  (2) Can you do \"sage -ba\" and try again?\n\n -- William",
    "created_at": "2008-08-13T07:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26111",
    "user": "@williamstein"
}
```

Mike said:
> 1) Sage segfaults at exit.
> 2) When doing sage -t, I get the following problem for every file: 

Mike, (1) what is your system?  (2) Can you do "sage -ba" and try again?

 -- William



---

archive/issue_comments_026112.json:
```json
{
    "body": "I just tried it out and got none of the problems described above.  \n\n'import sage.all' doesn't import IPython as desired.  I'm not putting up a positive review because of the problems described above, but I would be nice to have feedback on this\n\nI'm on OS X 10.5 with this patch applied against 3.1.4.",
    "created_at": "2008-10-23T21:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26112",
    "user": "anakha"
}
```

I just tried it out and got none of the problems described above.  

'import sage.all' doesn't import IPython as desired.  I'm not putting up a positive review because of the problems described above, but I would be nice to have feedback on this

I'm on OS X 10.5 with this patch applied against 3.1.4.



---

archive/issue_comments_026113.json:
```json
{
    "body": "If we've released for months and months (8 months!) without fixing this, it doesn't make sense to keep it as a blocker.",
    "created_at": "2009-06-15T23:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26113",
    "user": "@williamstein"
}
```

If we've released for months and months (8 months!) without fixing this, it doesn't make sense to keep it as a blocker.



---

archive/issue_comments_026114.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2009-06-15T23:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26114",
    "user": "@williamstein"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_026115.json:
```json
{
    "body": "Attachment [trac_3685.patch](tarball://root/attachments/some-uuid/ticket3685/trac_3685.patch) by @mwhansen created at 2013-07-22 14:22:45",
    "created_at": "2013-07-22T14:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26115",
    "user": "@mwhansen"
}
```

Attachment [trac_3685.patch](tarball://root/attachments/some-uuid/ticket3685/trac_3685.patch) by @mwhansen created at 2013-07-22 14:22:45



---

archive/issue_comments_026116.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-07-22T14:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26116",
    "user": "@mwhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_026117.json:
```json
{
    "body": "This is much easier now with the new IPython.\n\nApply trac_3685.patch",
    "created_at": "2013-07-22T14:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26117",
    "user": "@mwhansen"
}
```

This is much easier now with the new IPython.

Apply trac_3685.patch



---

archive/issue_comments_026118.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-08-21T16:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26118",
    "user": "@fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_026119.json:
```json
{
    "body": "it seems that the doctest fails on 5.12.beta2, so the patch needs work",
    "created_at": "2013-08-21T16:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26119",
    "user": "@fchapoton"
}
```

it seems that the doctest fails on 5.12.beta2, so the patch needs work



---

archive/issue_comments_026120.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-08-25T16:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26120",
    "user": "@fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_026121.json:
```json
{
    "body": "Changing keywords from \"\" to \"startup time and imports\".",
    "created_at": "2013-08-25T16:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26121",
    "user": "@fchapoton"
}
```

Changing keywords from "" to "startup time and imports".



---

archive/issue_comments_026122.json:
```json
{
    "body": "Attachment [trac_3685_remove_tab.patch](tarball://root/attachments/some-uuid/ticket3685/trac_3685_remove_tab.patch) by @fchapoton created at 2013-08-25 16:14:57\n\nI have found the problem, it seems ! Here is the patch solving the issue.\n\nNeeds review !",
    "created_at": "2013-08-25T16:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26122",
    "user": "@fchapoton"
}
```

Attachment [trac_3685_remove_tab.patch](tarball://root/attachments/some-uuid/ticket3685/trac_3685_remove_tab.patch) by @fchapoton created at 2013-08-25 16:14:57

I have found the problem, it seems ! Here is the patch solving the issue.

Needs review !



---

archive/issue_comments_026123.json:
```json
{
    "body": "arggg, that breaks everything... Back to need work.. :(",
    "created_at": "2013-08-25T19:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26123",
    "user": "@fchapoton"
}
```

arggg, that breaks everything... Back to need work.. :(



---

archive/issue_comments_026124.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-08-25T19:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26124",
    "user": "@fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_026125.json:
```json
{
    "body": "I am not able to sort things out.\n\nIt seems that the import of IPython occurs because of the line\n\n```\nfrom IPython.core.formatters import PlainTextFormatter\n```\n\nin \"sage.misc.displayhook\"\n\nIs there a way to avoid this IPython import ?",
    "created_at": "2013-08-25T19:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26125",
    "user": "@fchapoton"
}
```

I am not able to sort things out.

It seems that the import of IPython occurs because of the line

```
from IPython.core.formatters import PlainTextFormatter
```

in "sage.misc.displayhook"

Is there a way to avoid this IPython import ?



---

archive/issue_comments_026126.json:
```json
{
    "body": "#18726 took care of this and also added a doctest for it.\n\nOutdated, should close",
    "created_at": "2021-09-07T08:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26126",
    "user": "@mkoeppe"
}
```

#18726 took care of this and also added a doctest for it.

Outdated, should close



---

archive/issue_comments_026127.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-09-07T08:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26127",
    "user": "@mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_026128.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-09-07T08:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26128",
    "user": "@fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_026129.json:
```json
{
    "body": "ok",
    "created_at": "2021-09-07T08:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26129",
    "user": "@fchapoton"
}
```

ok



---

archive/issue_comments_026130.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-09-10T04:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3685",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3685#issuecomment-26130",
    "user": "@mkoeppe"
}
```

Resolution: invalid
