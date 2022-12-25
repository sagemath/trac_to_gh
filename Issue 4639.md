# Issue 4639: bad memory leak with exponentiation

archive/issues_004639.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @robertwb\n\nI think that the following example speaks for itself. (This was on an x86, 32 bit, running Ubuntu.)\n\nAlso, I believe that these examples had no problems in sage 3.0.2.\n\n\n```\nbober@bober:~/math/tests$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.2, Release Date: 2008-11-20                         |\n| Type notebook() for the GUI, and license() for information.        |\nsage: get_memory_usage()\n114.5546875\nsage: for z in xrange(10000):\n   ...:     a = 3^i\n   ...:     \nsage: get_memory_usage()\n121.4375\nsage: for z in xrange(10000):\n    a = 3^CC.0\n   ...:     \nsage: get_memory_usage()\n128.96484375\nsage: for z in xrange(10000):\n    a = 3.0^CC.0\n   ...:     \nsage: get_memory_usage()\n187.36328125\nsage: var('t')\nt\nsage: for z in xrange(10000):\n    a = 3.0^t\n   ....:     \nsage: get_memory_usage()\n231.4609375\nsage: #But, integer^integer is OK:\nsage: for z in xrange(10000):\n    a = 3^3\n   ....:     \nsage: get_memory_usage\n<function get_memory_usage at 0x8415f0c>\nsage: get_memory_usage()\n231.58984375\nsage: for z in xrange(10000):\n    a = 3^3\n   ....:     \nsage: get_memory_usage()\n231.58984375\nsage: for z in xrange(10000):\n    a = 3.0^CC.0\n   ....:     \nsaget_memory_usage()\n290.1640625\nsage: for z in xrange(10000):\n    a = CC.0^CC.0\n   ....:     \nsage: get_memory_usage()\n290.1640625\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4639\n\n",
    "created_at": "2008-11-27T19:06:08Z",
    "labels": [
        "component: basic arithmetic",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "bad memory leak with exponentiation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4639",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```
Assignee: somebody

CC:  @robertwb

I think that the following example speaks for itself. (This was on an x86, 32 bit, running Ubuntu.)

Also, I believe that these examples had no problems in sage 3.0.2.


```
bober@bober:~/math/tests$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2, Release Date: 2008-11-20                         |
| Type notebook() for the GUI, and license() for information.        |
sage: get_memory_usage()
114.5546875
sage: for z in xrange(10000):
   ...:     a = 3^i
   ...:     
sage: get_memory_usage()
121.4375
sage: for z in xrange(10000):
    a = 3^CC.0
   ...:     
sage: get_memory_usage()
128.96484375
sage: for z in xrange(10000):
    a = 3.0^CC.0
   ...:     
sage: get_memory_usage()
187.36328125
sage: var('t')
t
sage: for z in xrange(10000):
    a = 3.0^t
   ....:     
sage: get_memory_usage()
231.4609375
sage: #But, integer^integer is OK:
sage: for z in xrange(10000):
    a = 3^3
   ....:     
sage: get_memory_usage
<function get_memory_usage at 0x8415f0c>
sage: get_memory_usage()
231.58984375
sage: for z in xrange(10000):
    a = 3^3
   ....:     
sage: get_memory_usage()
231.58984375
sage: for z in xrange(10000):
    a = 3.0^CC.0
   ....:     
saget_memory_usage()
290.1640625
sage: for z in xrange(10000):
    a = CC.0^CC.0
   ....:     
sage: get_memory_usage()
290.1640625
```


Issue created by migration from https://trac.sagemath.org/ticket/4639





---

archive/issue_comments_034826.json:
```json
{
    "body": "This is indeed a grave bug.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T19:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34826",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is indeed a grave bug.

Cheers,

Michael



---

archive/issue_comments_034827.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2008-11-27T19:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34827",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_034828.json:
```json
{
    "body": "Hmm, \n\nBurcin and I have been looking at code he has been writing and there seems to be a caching issue with the coercion system. Now, I don't want to outright blame coercion here without any hard evidence, but the timing (3.0.2 to now) suggests that it could be involved here. So let's add robertwb to the CC and see if he can come up with anything. I will collect some evidence and hopefully someone else will take over.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T02:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34828",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, 

Burcin and I have been looking at code he has been writing and there seems to be a caching issue with the coercion system. Now, I don't want to outright blame coercion here without any hard evidence, but the timing (3.0.2 to now) suggests that it could be involved here. So let's add robertwb to the CC and see if he can come up with anything. I will collect some evidence and hopefully someone else will take over.

Cheers,

Michael



---

archive/issue_comments_034829.json:
```json
{
    "body": "Burcin about his code, not the problem reported here:\n\n```\n[6:36pm] burcin: hmm.. I think I found the problem..\n[6:36pm] burcin: still vague though\n[6:36pm] mabshoff: burcin: I CCed RobertWB on that existing leak ticket with the exponentiation and hopefully he will just post a one line patch.\n[6:36pm] mabshoff: Ok \n[6:36pm] burcin: I was being a good coercion user and called .coerce()\n[6:36pm] burcin: if I just use the __call__ on the parent, things work much much faster\n[6:36pm] mabshoff: And it doesn't leak?\n[6:37pm] burcin: I am guessing that the leak also goes away.. because this example ate more than 2gb memory with the leak\n[6:37pm] mabshoff: yeah\n```\n",
    "created_at": "2008-11-28T02:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34829",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Burcin about his code, not the problem reported here:

```
[6:36pm] burcin: hmm.. I think I found the problem..
[6:36pm] burcin: still vague though
[6:36pm] mabshoff: burcin: I CCed RobertWB on that existing leak ticket with the exponentiation and hopefully he will just post a one line patch.
[6:36pm] mabshoff: Ok 
[6:36pm] burcin: I was being a good coercion user and called .coerce()
[6:36pm] burcin: if I just use the __call__ on the parent, things work much much faster
[6:36pm] mabshoff: And it doesn't leak?
[6:37pm] burcin: I am guessing that the leak also goes away.. because this example ate more than 2gb memory with the leak
[6:37pm] mabshoff: yeah
```




---

archive/issue_comments_034830.json:
```json
{
    "body": "Here is my leak:\n\n\n```\nsage: F = GF(13)\nsage: get_memory_usage()\n708.02734375\nsage: for _ in xrange(10000):\n....:     t = F.coerce(F(234234))\n....:     \nsage: get_memory_usage()\n728.15234375\nsage: for _ in xrange(100000):\n    t = F.coerce(F(234234))\n....:     \nsage: get_memory_usage()\n932.3125\nsage: for _ in xrange(100000):\n    t = F.coerce(F(234234))\n....:     \nsage: get_memory_usage()\n1136.35546875\n```\n",
    "created_at": "2008-11-28T02:51:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34830",
    "user": "https://github.com/burcin"
}
```

Here is my leak:


```
sage: F = GF(13)
sage: get_memory_usage()
708.02734375
sage: for _ in xrange(10000):
....:     t = F.coerce(F(234234))
....:     
sage: get_memory_usage()
728.15234375
sage: for _ in xrange(100000):
    t = F.coerce(F(234234))
....:     
sage: get_memory_usage()
932.3125
sage: for _ in xrange(100000):
    t = F.coerce(F(234234))
....:     
sage: get_memory_usage()
1136.35546875
```




---

archive/issue_comments_034831.json:
```json
{
    "body": "This ticket might also cause #4631.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T21:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34831",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This ticket might also cause #4631.

Cheers,

Michael



---

archive/issue_comments_034832.json:
```json
{
    "body": "Here's the bug: \n\n\n```\nsage: sage: get_memory_usage()\n'465M'\nsage: for _ in xrange(10000): t = Hom(QQ, QQ)\n....: \nsage: sage: get_memory_usage()\n'476M'\nsage: Hom(QQ, QQ) is Hom(QQ, QQ)\nFalse\n```\n",
    "created_at": "2008-12-02T12:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34832",
    "user": "https://github.com/robertwb"
}
```

Here's the bug: 


```
sage: sage: get_memory_usage()
'465M'
sage: for _ in xrange(10000): t = Hom(QQ, QQ)
....: 
sage: sage: get_memory_usage()
'476M'
sage: Hom(QQ, QQ) is Hom(QQ, QQ)
False
```




---

archive/issue_comments_034833.json:
```json
{
    "body": "Hi Robert,\n\ndo you want me to valgrind here or are you already on top of this?\n\nCheers,\n\nMichael",
    "created_at": "2008-12-02T15:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34833",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Robert,

do you want me to valgrind here or are you already on top of this?

Cheers,

Michael



---

archive/issue_comments_034834.json:
```json
{
    "body": "I think I can dig further, this is just as far as I got last night. It's probably a caching, not malloc, issue.",
    "created_at": "2008-12-02T19:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34834",
    "user": "https://github.com/robertwb"
}
```

I think I can dig further, this is just as far as I got last night. It's probably a caching, not malloc, issue.



---

archive/issue_comments_034835.json:
```json
{
    "body": "Attachment [4639-coerce-leak.patch](tarball://root/attachments/some-uuid/ticket4639/4639-coerce-leak.patch) by @robertwb created at 2008-12-02 22:25:18\n\nthis fixes the leak in coerce, not in exponentiation",
    "created_at": "2008-12-02T22:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34835",
    "user": "https://github.com/robertwb"
}
```

Attachment [4639-coerce-leak.patch](tarball://root/attachments/some-uuid/ticket4639/4639-coerce-leak.patch) by @robertwb created at 2008-12-02 22:25:18

this fixes the leak in coerce, not in exponentiation



---

archive/issue_comments_034836.json:
```json
{
    "body": "Better caching for homsets fixes the leak for coercion.",
    "created_at": "2008-12-02T22:25:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34836",
    "user": "https://github.com/robertwb"
}
```

Better caching for homsets fixes the leak for coercion.



---

archive/issue_comments_034837.json:
```json
{
    "body": "Maybe we should move the problem with exponentiation to another ticket if it proves difficult to fix so we can get the coercion fix in. I am doctesting this now, but I will hold on a merge until we have gotten #3623 and #4276 in.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-02T22:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34837",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Maybe we should move the problem with exponentiation to another ticket if it proves difficult to fix so we can get the coercion fix in. I am doctesting this now, but I will hold on a merge until we have gotten #3623 and #4276 in.

Cheers,

Michael



---

archive/issue_comments_034838.json:
```json
{
    "body": "The patch RobertWB posted does pass doctesting.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-03T00:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34838",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch RobertWB posted does pass doctesting.

Cheers,

Michael



---

archive/issue_comments_034839.json:
```json
{
    "body": "#4683 might be a dupe of this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-03T01:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34839",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

#4683 might be a dupe of this ticket.

Cheers,

Michael



---

archive/issue_comments_034840.json:
```json
{
    "body": "I've read the patch and give it a positive review.  But the patch doesn't resolve the ticket, as Robert points out.   So after applying the patch, I guess you have to open a new ticket?  Or???  \n\nAnyway -- don't just randomly close this ticket after applying the patch...",
    "created_at": "2008-12-06T22:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34840",
    "user": "https://github.com/williamstein"
}
```

I've read the patch and give it a positive review.  But the patch doesn't resolve the ticket, as Robert points out.   So after applying the patch, I guess you have to open a new ticket?  Or???  

Anyway -- don't just randomly close this ticket after applying the patch...



---

archive/issue_comments_034841.json:
```json
{
    "body": "I have deleted the patch and moved it to its own ticket at #4740 since it does not fix the original problem reported. \n\nCheers,\n\nMichael",
    "created_at": "2008-12-08T11:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34841",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I have deleted the patch and moved it to its own ticket at #4740 since it does not fix the original problem reported. 

Cheers,

Michael



---

archive/issue_comments_034842.json:
```json
{
    "body": "An interesting test point: \n\n\n```\nclass TestParent(Parent):\n    def __init__(self):\n        self._populate_coercion_lists_()\n    def _has_coerce_map_from_(self, X):\n        return True\n    def _element_constructor_(self, x):\n        raise TypeError\n```\n\n\nNow this leaks\n\n\n```\n%python\n\nfrom sage.all import get_memory_usage\n\ndef test(R, S):\n    mor = S.convert_map_from(R)\n    print get_memory_usage()\n    for i in range(10000):\n        try:\n            mor = S.convert_map_from(R)\n            a = mor._call_(R.gen())\n        except:\n            pass\n    print get_memory_usage()\n```\n\n\nBut this doesn't \n\n\n```\n%cython\n\nfrom sage.all import get_memory_usage\n\ndef test(R, S):\n    mor = S.convert_map_from(R)\n    print get_memory_usage()\n    for i in range(10000):\n        try:\n            mor = S.convert_map_from(R)\n            a = mor._call_(R.gen())\n        except:\n            pass\n    print get_memory_usage()\n```\n\n\nThe *only* difference here is Python vs. Cython (leaking in the Python case).",
    "created_at": "2008-12-14T05:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34842",
    "user": "https://github.com/robertwb"
}
```

An interesting test point: 


```
class TestParent(Parent):
    def __init__(self):
        self._populate_coercion_lists_()
    def _has_coerce_map_from_(self, X):
        return True
    def _element_constructor_(self, x):
        raise TypeError
```


Now this leaks


```
%python

from sage.all import get_memory_usage

def test(R, S):
    mor = S.convert_map_from(R)
    print get_memory_usage()
    for i in range(10000):
        try:
            mor = S.convert_map_from(R)
            a = mor._call_(R.gen())
        except:
            pass
    print get_memory_usage()
```


But this doesn't 


```
%cython

from sage.all import get_memory_usage

def test(R, S):
    mor = S.convert_map_from(R)
    print get_memory_usage()
    for i in range(10000):
        try:
            mor = S.convert_map_from(R)
            a = mor._call_(R.gen())
        except:
            pass
    print get_memory_usage()
```


The *only* difference here is Python vs. Cython (leaking in the Python case).



---

archive/issue_comments_034843.json:
```json
{
    "body": "And running \n\n\n```\ntest(TestParent(), ZZ['x']) # python\n638M\n640M\n```\n\n\n\n\n```\ntest(TestParent(), ZZ['x']) # cython\n640M\n640M\n```\n\n\nIt feels like something is getting cached in an exception.",
    "created_at": "2008-12-14T05:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34843",
    "user": "https://github.com/robertwb"
}
```

And running 


```
test(TestParent(), ZZ['x']) # python
638M
640M
```




```
test(TestParent(), ZZ['x']) # cython
640M
640M
```


It feels like something is getting cached in an exception.



---

archive/issue_comments_034844.json:
```json
{
    "body": "I am almost sure the above is what's going wrong, and it gets invoked by __call__. \n\nguppy gives a total of 40420 bytes on these runs... and nothing new after repeated runs (despite get_memory_usage going up and up). However, the memory still goes up. Mabshoff, could you valgrind this and see if anything suspicious comes up? Perhaps up the loop to 100000, or diff the run from Python with that from Cython, to make it more clear where the error is...",
    "created_at": "2008-12-14T06:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34844",
    "user": "https://github.com/robertwb"
}
```

I am almost sure the above is what's going wrong, and it gets invoked by __call__. 

guppy gives a total of 40420 bytes on these runs... and nothing new after repeated runs (despite get_memory_usage going up and up). However, the memory still goes up. Mabshoff, could you valgrind this and see if anything suspicious comes up? Perhaps up the loop to 100000, or diff the run from Python with that from Cython, to make it more clear where the error is...



---

archive/issue_comments_034845.json:
```json
{
    "body": "Will do. Any news on the pickle failure for #4740?\n\nCheers,\n\nMichael",
    "created_at": "2008-12-14T06:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34845",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Will do. Any news on the pickle failure for #4740?

Cheers,

Michael



---

archive/issue_comments_034846.json:
```json
{
    "body": "This is a Cython error, not a coercion error. When something is returned from within a try block, it appears the (cached) exception is not released. \n\n\n```\n%cython\ndef foo():\n    try:\n        return None\n    except:\n        pass\n```\n\n\n\n```\n%python\ndef test():\n    print get_memory_usage()\n    for i in range(100000):\n        try:\n            foo()\n            raise TypeError\n        except TypeError:\n            pass\n    print get_memory_usage()\n```\n\n\nNow `test()` will leak.",
    "created_at": "2008-12-14T09:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34846",
    "user": "https://github.com/robertwb"
}
```

This is a Cython error, not a coercion error. When something is returned from within a try block, it appears the (cached) exception is not released. 


```
%cython
def foo():
    try:
        return None
    except:
        pass
```



```
%python
def test():
    print get_memory_usage()
    for i in range(100000):
        try:
            foo()
            raise TypeError
        except TypeError:
            pass
    print get_memory_usage()
```


Now `test()` will leak.



---

archive/issue_comments_034847.json:
```json
{
    "body": "Install cython-0.10.3.spkg at http://sage.math.washington.edu/home/robertwb/cython/ , which contains a fix to http://trac.cython.org/cython_trac/ticket/162 and I think is the underlying cause here (and probably elsewhere).",
    "created_at": "2008-12-14T11:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34847",
    "user": "https://github.com/robertwb"
}
```

Install cython-0.10.3.spkg at http://sage.math.washington.edu/home/robertwb/cython/ , which contains a fix to http://trac.cython.org/cython_trac/ticket/162 and I think is the underlying cause here (and probably elsewhere).



---

archive/issue_comments_034848.json:
```json
{
    "body": "The new Cython.spkg reduces the leak significantly:\nWithout:\n\n```\nsage: get_memory_usage()\n417.98828125\nsage: for z in xrange(10000):\n....:     a = 3.0^CC.0\n....:     \nsage: get_memory_usage()\n509.26171875\n```\n\nWith:\n\n```\nsage: get_memory_usage()\n416.19140625\nsage: \nsage: for z in xrange(10000):\n....:     a = 3.0^CC.0\n....:     \nsage: get_memory_usage()\n437.97265625\n```\n\nBut unfortunately it doesn't fix it completely:\n\n```\nsage: get_memory_usage()\n416.19140625\nsage: \nsage: for z in xrange(10000):\n....:     a = 3.0^CC.0\n....:     \nsage: get_memory_usage()\n437.97265625\nsage: for z in xrange(10000):\n    a = 3.0^CC.0\n....:     \nsage: get_memory_usage()\n459.99609375\n```\n\nConsequently I will split the Cython.spkg from this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-14T15:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34848",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The new Cython.spkg reduces the leak significantly:
Without:

```
sage: get_memory_usage()
417.98828125
sage: for z in xrange(10000):
....:     a = 3.0^CC.0
....:     
sage: get_memory_usage()
509.26171875
```

With:

```
sage: get_memory_usage()
416.19140625
sage: 
sage: for z in xrange(10000):
....:     a = 3.0^CC.0
....:     
sage: get_memory_usage()
437.97265625
```

But unfortunately it doesn't fix it completely:

```
sage: get_memory_usage()
416.19140625
sage: 
sage: for z in xrange(10000):
....:     a = 3.0^CC.0
....:     
sage: get_memory_usage()
437.97265625
sage: for z in xrange(10000):
    a = 3.0^CC.0
....:     
sage: get_memory_usage()
459.99609375
```

Consequently I will split the Cython.spkg from this ticket.

Cheers,

Michael



---

archive/issue_comments_034849.json:
```json
{
    "body": "For the record: The cython.spkg upgrade to 0.10.3 is #4798.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-14T17:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34849",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: The cython.spkg upgrade to 0.10.3 is #4798.

Cheers,

Michael



---

archive/issue_comments_034850.json:
```json
{
    "body": "This is the bug that will never die... I'll keep looking at that last case.",
    "created_at": "2008-12-15T18:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34850",
    "user": "https://github.com/robertwb"
}
```

This is the bug that will never die... I'll keep looking at that last case.



---

archive/issue_comments_034851.json:
```json
{
    "body": "If there ever was a blocker for 3.2.2 :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-15T18:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34851",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

If there ever was a blocker for 3.2.2 :)

Cheers,

Michael



---

archive/issue_comments_034852.json:
```json
{
    "body": "Another data point.\n\nI took the example from #4683 (Michael, it was argued that #4683 is a duplicate).\n\n```\nsage: get_memory_usage()\n704.5390625\nsage: v = [CDF(i)^2 for n in range(50000)]\nsage: get_memory_usage()\n803.67578125\n...\nsage: get_memory_usage()\n1093.203125\nsage: del v\nsage: get_memory_usage()\n1093.203125\nsage: v = [CDF(i)^2 for n in range(50000)]\nsage: get_memory_usage()\n1183.86328125\nsage: del v\nsage: get_memory_usage()\n1183.86328125\nsage: v=1\nsage: get_memory_usage()\n1183.86328125\n...\nsage: v = [CDF(i)^2 for n in range(50000)]\nsage: get_memory_usage()\n1279.55078125\nsage: w = deepcopy(v)\nsage: get_memory_usage()\n1295.18359375\nsage: del w\nsage: get_memory_usage()\n1295.18359375\n```\n\n\nTherefore it seems to me that the problem is not exponentiation but a failure in deallocation.",
    "created_at": "2008-12-16T13:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34852",
    "user": "https://github.com/simon-king-jena"
}
```

Another data point.

I took the example from #4683 (Michael, it was argued that #4683 is a duplicate).

```
sage: get_memory_usage()
704.5390625
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
803.67578125
...
sage: get_memory_usage()
1093.203125
sage: del v
sage: get_memory_usage()
1093.203125
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
1183.86328125
sage: del v
sage: get_memory_usage()
1183.86328125
sage: v=1
sage: get_memory_usage()
1183.86328125
...
sage: v = [CDF(i)^2 for n in range(50000)]
sage: get_memory_usage()
1279.55078125
sage: w = deepcopy(v)
sage: get_memory_usage()
1295.18359375
sage: del w
sage: get_memory_usage()
1295.18359375
```


Therefore it seems to me that the problem is not exponentiation but a failure in deallocation.



---

archive/issue_comments_034853.json:
```json
{
    "body": "Attachment [4639-parent-memleak.patch](tarball://root/attachments/some-uuid/ticket4639/4639-parent-memleak.patch) by @robertwb created at 2008-12-16 20:29:23\n\nI believe I have located and resolved the issue. After tracing through all kinds of coercion and homset code, and reading tons of Cython code looking for memory leaks, it turns out that this was caused by all Parents ever created being cached due to old debugging code. (Wow, wish I'd looked there first! :)\n\nSome old, unnecessary code has been removed from the generic __call__ method as well.",
    "created_at": "2008-12-16T20:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34853",
    "user": "https://github.com/robertwb"
}
```

Attachment [4639-parent-memleak.patch](tarball://root/attachments/some-uuid/ticket4639/4639-parent-memleak.patch) by @robertwb created at 2008-12-16 20:29:23

I believe I have located and resolved the issue. After tracing through all kinds of coercion and homset code, and reading tons of Cython code looking for memory leaks, it turns out that this was caused by all Parents ever created being cached due to old debugging code. (Wow, wish I'd looked there first! :)

Some old, unnecessary code has been removed from the generic __call__ method as well.



---

archive/issue_comments_034854.json:
```json
{
    "body": "Nice! I am testing away at the moment :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-16T20:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34854",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice! I am testing away at the moment :)

Cheers,

Michael



---

archive/issue_comments_034855.json:
```json
{
    "body": "This does indeed fix the issue for me:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: get_memory_usage()\n416.21484375\nsage: for z in xrange(10000):\n....:     a = 3.0^CC.0\n....:     \nsage: get_memory_usage()\n416.21484375\nsage: for z in xrange(10000):\n    a = 3.0^CC.0\n....:     \nsage: get_memory_usage()\n416.21484375\n```\n\nDoctesting now ...\n| Sage Version 3.2.2.rc0, Release Date: 2008-12-15                   |\n| Type notebook() for the GUI, and license() for information.        |\nCheers,\n\nMichael",
    "created_at": "2008-12-16T20:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34855",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This does indeed fix the issue for me:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: get_memory_usage()
416.21484375
sage: for z in xrange(10000):
....:     a = 3.0^CC.0
....:     
sage: get_memory_usage()
416.21484375
sage: for z in xrange(10000):
    a = 3.0^CC.0
....:     
sage: get_memory_usage()
416.21484375
```

Doctesting now ...
| Sage Version 3.2.2.rc0, Release Date: 2008-12-15                   |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael



---

archive/issue_comments_034856.json:
```json
{
    "body": "Positive review for 4639-parent-memleak.patch - w00t\n\nCheers,\n\nMichael",
    "created_at": "2008-12-17T03:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34856",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review for 4639-parent-memleak.patch - w00t

Cheers,

Michael



---

archive/issue_events_004886.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-12-17T14:01:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4639#event-4886"
}
```



---

archive/issue_comments_034857.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc1",
    "created_at": "2008-12-17T14:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34857",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.rc1



---

archive/issue_comments_034858.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-17T14:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4639",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4639#issuecomment-34858",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
