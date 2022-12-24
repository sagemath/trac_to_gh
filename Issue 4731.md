# Issue 4731: Repeated computation involving Maxima is getting slower and slower

archive/issues_004731.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: maxima timing repeated computation\n\nIt may happen that a computation does not always take the same time when it is done the first or the tenth time, if Maxima is involved. The example below is short and rather drastic. However, much worse happened to me in some application, when the time dropped by a much bigger factor.\n\nThe strange time-under-repetition behaviour can be triggered by the following short code:\n\n```\nsage: class Foo:\n....:     def __init__(self,n,L):\n....:         self.n = n\n....:         self.l = int(log(n,10))+1\n....:         self.L = [X%n for X in L]\n....:     def __str__(self):\n....:         return \"[\"+\" \".join([str(X).rjust(self.l) for X in self.L])+\"]\"\n....:     def __copy__(self):\n....:         OUT = Foo(self.n,copy(self.L))\n....:         return OUT\n....:     def __mul__(self,r):\n....:         OUT = self.__copy__()\n....:         OUT.L = [(X*r)%OUT.n for X in OUT.L]\n....:         return OUT\n....:\nsage: M=Foo(97,[1,13,100,23098])\nsage: timeit('N=M*13')\n25 loops, best of 3: 9.66 ms per loop\nsage: timeit('N=M*13')\n25 loops, best of 3: 13.3 ms per loop\nsage: timeit('N=M*13')\n25 loops, best of 3: 14.3 ms per loop\nsage: timeit('N=M*13')\n25 loops, best of 3: 12.2 ms per loop\nsage: timeit('N=M*13')\n25 loops, best of 3: 17.3 ms per loop\nsage: timeit('N=M*13')\n25 loops, best of 3: 16 ms per loop\nsage: timeit('N=M*13')\n25 loops, best of 3: 17.8 ms per loop\nsage: timeit('N=M*13')\n25 loops, best of 3: 19.3 ms per loop\nsage: timeit('N=M*13')\n25 loops, best of 3: 20.7 ms per loop\n```\n\n\nSo, on average, the computation becomes slower and slower.\n\nThis strange behaviour is due to the line `self.l = int(log(n,10))+1`. Replacing it by a different (though equivalent) line, we get:\n\n```\nsage: class Foo:\n....:     def __init__(self,n,L):\n....:         self.n = n\n....:         self.l = len(str(n))\n....:         self.L = [X%n for X in L]\n....:     def __str__(self):\n....:         return \"[\"+\" \".join([str(X).rjust(self.l) for X in self.L])+\"]\"\n....:     def __copy__(self):\n....:         OUT = Foo(self.n,copy(self.L))\n....:         return OUT\n....:     def __mul__(self,r):\n....:         OUT = self.__copy__()\n....:         OUT.L = [(X*r)%OUT.n for X in OUT.L]\n....:         return OUT\n....:\nsage: M=Foo(97,[1,13,100,23098])\nsage: timeit('N=M*13')\n625 loops, best of 3: 19.2 \u00c2\u00b5s per loop\nsage: timeit('N=M*13')\n625 loops, best of 3: 19.2 \u00c2\u00b5s per loop\nsage: timeit('N=M*13')\n625 loops, best of 3: 19.2 \u00c2\u00b5s per loop\nsage: timeit('N=M*13')\n625 loops, best of 3: 19.3 \u00c2\u00b5s per loop\nsage: timeit('N=M*13')\n625 loops, best of 3: 19.3 \u00c2\u00b5s per loop\nsage: timeit('N=M*13')\n625 loops, best of 3: 19.3 \u00c2\u00b5s per loop\n```\n\n\nIt is not the point that now it is faster. The point is that now the computation time is constant under repetition.\n\nSorry, I am not sure what \"Component\" I shall assign. Hopefully calculus is ok?\n\nIssue created by migration from https://trac.sagemath.org/ticket/4731\n\n",
    "created_at": "2008-12-06T23:18:40Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Repeated computation involving Maxima is getting slower and slower",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4731",
    "user": "@simon-king-jena"
}
```
Assignee: @burcin

Keywords: maxima timing repeated computation

It may happen that a computation does not always take the same time when it is done the first or the tenth time, if Maxima is involved. The example below is short and rather drastic. However, much worse happened to me in some application, when the time dropped by a much bigger factor.

The strange time-under-repetition behaviour can be triggered by the following short code:

```
sage: class Foo:
....:     def __init__(self,n,L):
....:         self.n = n
....:         self.l = int(log(n,10))+1
....:         self.L = [X%n for X in L]
....:     def __str__(self):
....:         return "["+" ".join([str(X).rjust(self.l) for X in self.L])+"]"
....:     def __copy__(self):
....:         OUT = Foo(self.n,copy(self.L))
....:         return OUT
....:     def __mul__(self,r):
....:         OUT = self.__copy__()
....:         OUT.L = [(X*r)%OUT.n for X in OUT.L]
....:         return OUT
....:
sage: M=Foo(97,[1,13,100,23098])
sage: timeit('N=M*13')
25 loops, best of 3: 9.66 ms per loop
sage: timeit('N=M*13')
25 loops, best of 3: 13.3 ms per loop
sage: timeit('N=M*13')
25 loops, best of 3: 14.3 ms per loop
sage: timeit('N=M*13')
25 loops, best of 3: 12.2 ms per loop
sage: timeit('N=M*13')
25 loops, best of 3: 17.3 ms per loop
sage: timeit('N=M*13')
25 loops, best of 3: 16 ms per loop
sage: timeit('N=M*13')
25 loops, best of 3: 17.8 ms per loop
sage: timeit('N=M*13')
25 loops, best of 3: 19.3 ms per loop
sage: timeit('N=M*13')
25 loops, best of 3: 20.7 ms per loop
```


So, on average, the computation becomes slower and slower.

This strange behaviour is due to the line `self.l = int(log(n,10))+1`. Replacing it by a different (though equivalent) line, we get:

```
sage: class Foo:
....:     def __init__(self,n,L):
....:         self.n = n
....:         self.l = len(str(n))
....:         self.L = [X%n for X in L]
....:     def __str__(self):
....:         return "["+" ".join([str(X).rjust(self.l) for X in self.L])+"]"
....:     def __copy__(self):
....:         OUT = Foo(self.n,copy(self.L))
....:         return OUT
....:     def __mul__(self,r):
....:         OUT = self.__copy__()
....:         OUT.L = [(X*r)%OUT.n for X in OUT.L]
....:         return OUT
....:
sage: M=Foo(97,[1,13,100,23098])
sage: timeit('N=M*13')
625 loops, best of 3: 19.2 Âµs per loop
sage: timeit('N=M*13')
625 loops, best of 3: 19.2 Âµs per loop
sage: timeit('N=M*13')
625 loops, best of 3: 19.2 Âµs per loop
sage: timeit('N=M*13')
625 loops, best of 3: 19.3 Âµs per loop
sage: timeit('N=M*13')
625 loops, best of 3: 19.3 Âµs per loop
sage: timeit('N=M*13')
625 loops, best of 3: 19.3 Âµs per loop
```


It is not the point that now it is faster. The point is that now the computation time is constant under repetition.

Sorry, I am not sure what "Component" I shall assign. Hopefully calculus is ok?

Issue created by migration from https://trac.sagemath.org/ticket/4731





---

archive/issue_comments_035710.json:
```json
{
    "body": "Changing assignee from @burcin to mabshoff.",
    "created_at": "2008-12-07T06:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4731#issuecomment-35710",
    "user": "mabshoff"
}
```

Changing assignee from @burcin to mabshoff.



---

archive/issue_comments_035711.json:
```json
{
    "body": "Changing component from calculus to performance.",
    "created_at": "2008-12-07T06:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4731#issuecomment-35711",
    "user": "mabshoff"
}
```

Changing component from calculus to performance.



---

archive/issue_comments_035712.json:
```json
{
    "body": "At http://groups.google.com/group/sage-devel/browse_thread/thread/863e59ba164590c5 Golam Mortuza Hossain came up with a still much shorter code snipped that is probably related with this ticket:\n\n\n```\nsage: f(x) = function('f',x);\nsage: timeit('bool( f(x) == 0 )')\n5 loops, best of 3: 71.6 ms per loop\nsage: timeit('bool( f(x) == 0 )')\n5 loops, best of 3: 89.1 ms per loop\nsage: timeit('bool( f(x) == 0 )')\n5 loops, best of 3: 101 ms per loop\nsage: timeit('bool( f(x) == 0 )')\n5 loops, best of 3: 127 ms per loop\nsage: timeit('bool( f(x) == 0 )')\n5 loops, best of 3: 159 ms per loop\nsage: timeit('bool( f(x) == 0 )')\n5 loops, best of 3: 231 ms per loop\nsage: timeit('bool( f(x) == 0 )')\n5 loops, best of 3: 305 ms per loop \n```\n\n\nSo, this code should be short enough to clearly point to the source of trouble. Maxima experts, speak up, please!",
    "created_at": "2009-07-27T08:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4731#issuecomment-35712",
    "user": "@simon-king-jena"
}
```

At http://groups.google.com/group/sage-devel/browse_thread/thread/863e59ba164590c5 Golam Mortuza Hossain came up with a still much shorter code snipped that is probably related with this ticket:


```
sage: f(x) = function('f',x);
sage: timeit('bool( f(x) == 0 )')
5 loops, best of 3: 71.6 ms per loop
sage: timeit('bool( f(x) == 0 )')
5 loops, best of 3: 89.1 ms per loop
sage: timeit('bool( f(x) == 0 )')
5 loops, best of 3: 101 ms per loop
sage: timeit('bool( f(x) == 0 )')
5 loops, best of 3: 127 ms per loop
sage: timeit('bool( f(x) == 0 )')
5 loops, best of 3: 159 ms per loop
sage: timeit('bool( f(x) == 0 )')
5 loops, best of 3: 231 ms per loop
sage: timeit('bool( f(x) == 0 )')
5 loops, best of 3: 305 ms per loop 
```


So, this code should be short enough to clearly point to the source of trouble. Maxima experts, speak up, please!



---

archive/issue_comments_035713.json:
```json
{
    "body": "See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/863e59ba164590c5) thread for a simple example of such memory leaks.",
    "created_at": "2009-07-27T08:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4731#issuecomment-35713",
    "user": "mvngu"
}
```

See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/863e59ba164590c5) thread for a simple example of such memory leaks.



---

archive/issue_comments_035714.json:
```json
{
    "body": "Here's a [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/cacc0b6dd40f7624) thread related to timeit getting slower and slower with each call.",
    "created_at": "2009-08-03T23:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4731#issuecomment-35714",
    "user": "mvngu"
}
```

Here's a [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/cacc0b6dd40f7624) thread related to timeit getting slower and slower with each call.



---

archive/issue_comments_035715.json:
```json
{
    "body": "I have verified that #6818 *does* fix this problem:",
    "created_at": "2009-08-24T15:51:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4731#issuecomment-35715",
    "user": "@williamstein"
}
```

I have verified that #6818 *does* fix this problem:



---

archive/issue_comments_035716.json:
```json
{
    "body": "Closing this as a duplicate of #6818.",
    "created_at": "2009-08-25T01:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4731#issuecomment-35716",
    "user": "mvngu"
}
```

Closing this as a duplicate of #6818.



---

archive/issue_comments_035717.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-08-25T01:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4731#issuecomment-35717",
    "user": "mvngu"
}
```

Resolution: duplicate
