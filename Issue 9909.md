# Issue 9909: Longest path

archive/issues_009909.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  fidelbarrera mvngu\n\nThis method computes a longest path in a graph/digraph... This ticket has to be coordinated with #9698.\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9910\n\n",
    "created_at": "2010-09-14T19:18:22Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Longest path",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9909",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  fidelbarrera mvngu

This method computes a longest path in a graph/digraph... This ticket has to be coordinated with #9698.

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9910





---

archive/issue_comments_098398.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-14T19:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98398",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098399.json:
```json
{
    "body": "Attachment [trac_9910.2.patch](tarball://root/attachments/some-uuid/ticket9910/trac_9910.2.patch) by @nathanncohen created at 2010-10-20 12:16:05\n\nsorry for the two version, they're both the same `^^;`\n\nNathann",
    "created_at": "2010-10-20T12:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98399",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9910.2.patch](tarball://root/attachments/some-uuid/ticket9910/trac_9910.2.patch) by @nathanncohen created at 2010-10-20 12:16:05

sorry for the two version, they're both the same `^^;`

Nathann



---

archive/issue_comments_098400.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-26T17:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98400",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_098401.json:
```json
{
    "body": "Updated !\n\nNathann",
    "created_at": "2010-11-26T20:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98401",
    "user": "https://github.com/nathanncohen"
}
```

Updated !

Nathann



---

archive/issue_comments_098402.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-26T20:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98402",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098403.json:
```json
{
    "body": "Attachment [trac_9910.patch](tarball://root/attachments/some-uuid/ticket9910/trac_9910.patch) by @nathanncohen created at 2010-11-26 20:49:19",
    "created_at": "2010-11-26T20:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98403",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9910.patch](tarball://root/attachments/some-uuid/ticket9910/trac_9910.patch) by @nathanncohen created at 2010-11-26 20:49:19



---

archive/issue_comments_098404.json:
```json
{
    "body": "Attachment [trac-9910_reviewer.patch](tarball://root/attachments/some-uuid/ticket9910/trac-9910_reviewer.patch) by mvngu created at 2010-11-27 19:24:52\n\nI'm OK with most of your patch. But here are some general comments:\n\n* I don't quite understand this documentation:\n\n```\n        - ``s`` (vertex) -- forces the source of the path. Set to               \n          ``None`` by default.                                                  \n                                                                                \n        - ``t`` (vertex) -- forces the destination of the path. Set to          \n          ``None`` by default.\n```\n\n What do you mean by \"forces\", etc. You need to elaborate here.\n\n* The following code block\n\n```\n            if self._directed:\n                from sage.graphs.all import DiGraph\n                return [0, DiGraph()] if weighted else DiGraph()\n            else:\n                from sage.graphs.all import Graph\n                return [0, Graph()] if weighted else Graph()\n```\n\n is equivalent to\n\n```\n            if self._directed:\n                from sage.graphs.all import DiGraph\n                return [0, DiGraph()] if weighted else DiGraph()\n            from sage.graphs.all import Graph\n            return [0, Graph()] if weighted else Graph()\n```\n\n\n* You really need to start seriously writing Python code that conforms to Python coding conventions (wherever possible); see [PEP 8](http://www.python.org/dev/peps/pep-0008/) for more information.\n\nMost of the above issues are fixed in my reviewer patch.",
    "created_at": "2010-11-27T19:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98404",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac-9910_reviewer.patch](tarball://root/attachments/some-uuid/ticket9910/trac-9910_reviewer.patch) by mvngu created at 2010-11-27 19:24:52

I'm OK with most of your patch. But here are some general comments:

* I don't quite understand this documentation:

```
        - ``s`` (vertex) -- forces the source of the path. Set to               
          ``None`` by default.                                                  
                                                                                
        - ``t`` (vertex) -- forces the destination of the path. Set to          
          ``None`` by default.
```

 What do you mean by "forces", etc. You need to elaborate here.

* The following code block

```
            if self._directed:
                from sage.graphs.all import DiGraph
                return [0, DiGraph()] if weighted else DiGraph()
            else:
                from sage.graphs.all import Graph
                return [0, Graph()] if weighted else Graph()
```

 is equivalent to

```
            if self._directed:
                from sage.graphs.all import DiGraph
                return [0, DiGraph()] if weighted else DiGraph()
            from sage.graphs.all import Graph
            return [0, Graph()] if weighted else Graph()
```


* You really need to start seriously writing Python code that conforms to Python coding conventions (wherever possible); see [PEP 8](http://www.python.org/dev/peps/pep-0008/) for more information.

Most of the above issues are fixed in my reviewer patch.



---

archive/issue_comments_098405.json:
```json
{
    "body": "Hello !!!\n\nHere is a patch to import on top of your, to fix the documentation. These options are just a way for the user to compute the \"longest path leaving from s\", or the \"longest path ending in t\", or the \"longest s-t-path\"\n\nAbout the if/else, I knew it was not useful but I let it stay anyway thinking it would be easier to understand the code. When I look at it from afar, I like to see a If/Else with return lines at the end of both, which ensures the method ends because of this part of the code (and I like to preserve symmetry when there is no reason not to `^^;`). That's just me, if you think it's better without the \"else\", then let it be.\n\nI am really sorry you had to waste time fixing my spaces and long lines. I know I never paid attention to spaces, but I will from now on, and I thought I was wary enough of long lines, which is clearly untrue. I also thought I had learned not to write ``x == None`` too... `:-/`\n\nHere is the slight fix in the documentation you asked. If it suits you, the ticket is good to go.\n\nThank you for your precious help, once again !\n\nNathann",
    "created_at": "2010-11-27T21:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98405",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!!

Here is a patch to import on top of your, to fix the documentation. These options are just a way for the user to compute the "longest path leaving from s", or the "longest path ending in t", or the "longest s-t-path"

About the if/else, I knew it was not useful but I let it stay anyway thinking it would be easier to understand the code. When I look at it from afar, I like to see a If/Else with return lines at the end of both, which ensures the method ends because of this part of the code (and I like to preserve symmetry when there is no reason not to `^^;`). That's just me, if you think it's better without the "else", then let it be.

I am really sorry you had to waste time fixing my spaces and long lines. I know I never paid attention to spaces, but I will from now on, and I thought I was wary enough of long lines, which is clearly untrue. I also thought I had learned not to write ``x == None`` too... `:-/`

Here is the slight fix in the documentation you asked. If it suits you, the ticket is good to go.

Thank you for your precious help, once again !

Nathann



---

archive/issue_comments_098406.json:
```json
{
    "body": "Replying to [comment:8 ncohen]:\n> Here is a patch to import on top of your, to fix the documentation. These options are just a way for the user to compute the \"longest path leaving from s\", or the \"longest path ending in t\", or the \"longest s-t-path\"\n\nYour improved documentation is certainly very clear to me. But note a typo in the following:\n\n\n```\n4384\t          returns the longest path starting at ``s``). Thie argument is Set to \n```\n\n\nI think you mean \"The\" instead of \"Thie\". And two more in these lines:\n\n\n```\n4388\t        - ``s`` (vertex) -- forces the destination of the path (the method then \n4389\t          returns the longest path ending at ``s``). Thie argument is Set to \n```\n\n\nI think you mean the above to be about the argument \"t\", as opposed to repeating the documentation for the argument \"s\". If you fix these, then the ticket is good to go.\n\n\n\n\n> About the if/else, I knew it was not useful but I let it stay anyway thinking it would be easier to understand the code. When I look at it from afar, I like to see a If/Else with return lines at the end of both, which ensures the method ends because of this part of the code (and I like to preserve symmetry when there is no reason not to `^^;`). That's just me, if you think it's better without the \"else\", then let it be.\n\nIn many cases, removing the redundant \"else\" can result in faster code than if you leave in the \"else\". Here's a sample profiling session:\n\n```python\nsage: # define functions whose runtime are to be compared\nsage: def con_else(n):\n....:     if n & 1:\n....:         2 * n\n....:         return\n....:     else:\n....:         n + 1\n....:         return\n....:     \nsage: def con_no_else(n):\n....:     if n & 1:\n....:         2 * n\n....:         return\n....:     n + 1\n....:     return\n....: \nsage:\nsage: # get runtime samples for the above functions\nsage: %timeit con_else(100)\n625 loops, best of 3: 781 ns per loop\nsage: %timeit con_else(100)\n625 loops, best of 3: 787 ns per loop\nsage: %timeit con_else(100)\n625 loops, best of 3: 795 ns per loop\nsage: %timeit con_else(100)\n625 loops, best of 3: 785 ns per loop\nsage: %timeit con_else(100)\n625 loops, best of 3: 781 ns per loop\nsage: %timeit con_else(100)\n625 loops, best of 3: 792 ns per loop\nsage: %timeit con_else(100)\n625 loops, best of 3: 784 ns per loop\nsage: %timeit con_else(100)\n625 loops, best of 3: 798 ns per loop\nsage: %timeit con_else(100)\n625 loops, best of 3: 784 ns per loop\nsage: %timeit con_else(100)\n625 loops, best of 3: 766 ns per loop\nsage: T1even = [781, 787, 795, 785, 781, 792, 784, 798, 784, 766]\nsage:\nsage: %timeit con_else(101)\n625 loops, best of 3: 771 ns per loop\nsage: %timeit con_else(101)\n625 loops, best of 3: 769 ns per loop\nsage: %timeit con_else(101)\n625 loops, best of 3: 771 ns per loop\nsage: %timeit con_else(101)\n625 loops, best of 3: 768 ns per loop\nsage: %timeit con_else(101)\n625 loops, best of 3: 772 ns per loop\nsage: %timeit con_else(101)\n625 loops, best of 3: 766 ns per loop\nsage: %timeit con_else(101)\n625 loops, best of 3: 772 ns per loop\nsage: %timeit con_else(101)\n625 loops, best of 3: 768 ns per loop\nsage: %timeit con_else(101)\n625 loops, best of 3: 769 ns per loop\nsage: %timeit con_else(101)\n625 loops, best of 3: 774 ns per loop\nsage: T1odd = [771, 769, 771, 768, 772, 766, 772, 768, 769, 774]\nsage:\nsage: %timeit con_no_else(100)\n625 loops, best of 3: 661 ns per loop\nsage: %timeit con_no_else(100)\n625 loops, best of 3: 667 ns per loop\nsage: %timeit con_no_else(100)\n625 loops, best of 3: 669 ns per loop\nsage: %timeit con_no_else(100)\n625 loops, best of 3: 667 ns per loop\nsage: %timeit con_no_else(100)\n625 loops, best of 3: 669 ns per loop\nsage: %timeit con_no_else(100)\n625 loops, best of 3: 661 ns per loop\nsage: %timeit con_no_else(100)\n625 loops, best of 3: 666 ns per loop\nsage: %timeit con_no_else(100)\n625 loops, best of 3: 674 ns per loop\nsage: %timeit con_no_else(100)\n625 loops, best of 3: 667 ns per loop\nsage: %timeit con_no_else(100)\n625 loops, best of 3: 664 ns per loop\nsage: T2even = [661, 667, 669, 667, 669, 661, 666, 674, 667]\nsage:\nsage: %timeit con_no_else(101)\n625 loops, best of 3: 680 ns per loop\nsage: %timeit con_no_else(101)\n625 loops, best of 3: 677 ns per loop\nsage: %timeit con_no_else(101)\n625 loops, best of 3: 680 ns per loop\nsage: %timeit con_no_else(101)\n625 loops, best of 3: 685 ns per loop\nsage: %timeit con_no_else(101)\n625 loops, best of 3: 679 ns per loop\nsage: %timeit con_no_else(101)\n625 loops, best of 3: 677 ns per loop\nsage: %timeit con_no_else(101)\n625 loops, best of 3: 678 ns per loop\nsage: %timeit con_no_else(101)\n625 loops, best of 3: 679 ns per loop\nsage: %timeit con_no_else(101)\n625 loops, best of 3: 685 ns per loop\nsage: %timeit con_no_else(101)\n625 loops, best of 3: 675 ns per loop\nsage: T2odd = [680, 677, 680, 685, 679, 677, 678, 679, 685, 675]\nsage:\nsage: # And now a comparison of the average runtime\nsage: RR(sum(T1even) / len(T1even))\n785.300000000000\nsage: RR(sum(T2even) / len(T2even))\n666.777777777778\nsage: RR(sum(T1odd) / len(T1odd))\n770.000000000000\nsage: RR(sum(T2odd) / len(T2odd))\n679.500000000000\n```\n\n\n\n\n\n> I am really sorry you had to waste time fixing my spaces and long lines. I know I never paid attention to spaces, but I will from now on, and I thought I was wary enough of long lines, which is clearly untrue. I also thought I had learned not to write ``x == None`` too... `:-/`\n\nI care about your code and how fast it runs. That's why I suggested that you use \"is not\" or \"is\" when you do a comparison with \"None\", because in that case the comparison is faster than if you used \"!=\" or \"=\".\n\n\n\n\n\n> Here is the slight fix in the documentation you asked. If it suits you, the ticket is good to go.\n> \n> Thank you for your precious help, once again !\n\nDon't take my comments above the wrong way. Had I not cared about your code and how fast you can make it run, I wouldn't bother reading your patches and suggest where you can improve the runtime of your code. There are many tricks in Python programming that can result in fast code without having to use Cython. I just want to share with you any tricks I know. As regards coding conventions, many programming languages have them and people who program in such a language would more or less adhere to the corresponding coding conventions. Remember that conventions are guidelines that many if not most experienced programmers find to result in readable, maintainable, and elegant looking code. This means that in some cases, it makes sense to break a convention. In case you are uncertain about whether to follow a convention or not, you need to use your judgement.",
    "created_at": "2010-11-27T22:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98406",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:8 ncohen]:
> Here is a patch to import on top of your, to fix the documentation. These options are just a way for the user to compute the "longest path leaving from s", or the "longest path ending in t", or the "longest s-t-path"

Your improved documentation is certainly very clear to me. But note a typo in the following:


```
4384	          returns the longest path starting at ``s``). Thie argument is Set to 
```


I think you mean "The" instead of "Thie". And two more in these lines:


```
4388	        - ``s`` (vertex) -- forces the destination of the path (the method then 
4389	          returns the longest path ending at ``s``). Thie argument is Set to 
```


I think you mean the above to be about the argument "t", as opposed to repeating the documentation for the argument "s". If you fix these, then the ticket is good to go.




> About the if/else, I knew it was not useful but I let it stay anyway thinking it would be easier to understand the code. When I look at it from afar, I like to see a If/Else with return lines at the end of both, which ensures the method ends because of this part of the code (and I like to preserve symmetry when there is no reason not to `^^;`). That's just me, if you think it's better without the "else", then let it be.

In many cases, removing the redundant "else" can result in faster code than if you leave in the "else". Here's a sample profiling session:

```python
sage: # define functions whose runtime are to be compared
sage: def con_else(n):
....:     if n & 1:
....:         2 * n
....:         return
....:     else:
....:         n + 1
....:         return
....:     
sage: def con_no_else(n):
....:     if n & 1:
....:         2 * n
....:         return
....:     n + 1
....:     return
....: 
sage:
sage: # get runtime samples for the above functions
sage: %timeit con_else(100)
625 loops, best of 3: 781 ns per loop
sage: %timeit con_else(100)
625 loops, best of 3: 787 ns per loop
sage: %timeit con_else(100)
625 loops, best of 3: 795 ns per loop
sage: %timeit con_else(100)
625 loops, best of 3: 785 ns per loop
sage: %timeit con_else(100)
625 loops, best of 3: 781 ns per loop
sage: %timeit con_else(100)
625 loops, best of 3: 792 ns per loop
sage: %timeit con_else(100)
625 loops, best of 3: 784 ns per loop
sage: %timeit con_else(100)
625 loops, best of 3: 798 ns per loop
sage: %timeit con_else(100)
625 loops, best of 3: 784 ns per loop
sage: %timeit con_else(100)
625 loops, best of 3: 766 ns per loop
sage: T1even = [781, 787, 795, 785, 781, 792, 784, 798, 784, 766]
sage:
sage: %timeit con_else(101)
625 loops, best of 3: 771 ns per loop
sage: %timeit con_else(101)
625 loops, best of 3: 769 ns per loop
sage: %timeit con_else(101)
625 loops, best of 3: 771 ns per loop
sage: %timeit con_else(101)
625 loops, best of 3: 768 ns per loop
sage: %timeit con_else(101)
625 loops, best of 3: 772 ns per loop
sage: %timeit con_else(101)
625 loops, best of 3: 766 ns per loop
sage: %timeit con_else(101)
625 loops, best of 3: 772 ns per loop
sage: %timeit con_else(101)
625 loops, best of 3: 768 ns per loop
sage: %timeit con_else(101)
625 loops, best of 3: 769 ns per loop
sage: %timeit con_else(101)
625 loops, best of 3: 774 ns per loop
sage: T1odd = [771, 769, 771, 768, 772, 766, 772, 768, 769, 774]
sage:
sage: %timeit con_no_else(100)
625 loops, best of 3: 661 ns per loop
sage: %timeit con_no_else(100)
625 loops, best of 3: 667 ns per loop
sage: %timeit con_no_else(100)
625 loops, best of 3: 669 ns per loop
sage: %timeit con_no_else(100)
625 loops, best of 3: 667 ns per loop
sage: %timeit con_no_else(100)
625 loops, best of 3: 669 ns per loop
sage: %timeit con_no_else(100)
625 loops, best of 3: 661 ns per loop
sage: %timeit con_no_else(100)
625 loops, best of 3: 666 ns per loop
sage: %timeit con_no_else(100)
625 loops, best of 3: 674 ns per loop
sage: %timeit con_no_else(100)
625 loops, best of 3: 667 ns per loop
sage: %timeit con_no_else(100)
625 loops, best of 3: 664 ns per loop
sage: T2even = [661, 667, 669, 667, 669, 661, 666, 674, 667]
sage:
sage: %timeit con_no_else(101)
625 loops, best of 3: 680 ns per loop
sage: %timeit con_no_else(101)
625 loops, best of 3: 677 ns per loop
sage: %timeit con_no_else(101)
625 loops, best of 3: 680 ns per loop
sage: %timeit con_no_else(101)
625 loops, best of 3: 685 ns per loop
sage: %timeit con_no_else(101)
625 loops, best of 3: 679 ns per loop
sage: %timeit con_no_else(101)
625 loops, best of 3: 677 ns per loop
sage: %timeit con_no_else(101)
625 loops, best of 3: 678 ns per loop
sage: %timeit con_no_else(101)
625 loops, best of 3: 679 ns per loop
sage: %timeit con_no_else(101)
625 loops, best of 3: 685 ns per loop
sage: %timeit con_no_else(101)
625 loops, best of 3: 675 ns per loop
sage: T2odd = [680, 677, 680, 685, 679, 677, 678, 679, 685, 675]
sage:
sage: # And now a comparison of the average runtime
sage: RR(sum(T1even) / len(T1even))
785.300000000000
sage: RR(sum(T2even) / len(T2even))
666.777777777778
sage: RR(sum(T1odd) / len(T1odd))
770.000000000000
sage: RR(sum(T2odd) / len(T2odd))
679.500000000000
```





> I am really sorry you had to waste time fixing my spaces and long lines. I know I never paid attention to spaces, but I will from now on, and I thought I was wary enough of long lines, which is clearly untrue. I also thought I had learned not to write ``x == None`` too... `:-/`

I care about your code and how fast it runs. That's why I suggested that you use "is not" or "is" when you do a comparison with "None", because in that case the comparison is faster than if you used "!=" or "=".





> Here is the slight fix in the documentation you asked. If it suits you, the ticket is good to go.
> 
> Thank you for your precious help, once again !

Don't take my comments above the wrong way. Had I not cared about your code and how fast you can make it run, I wouldn't bother reading your patches and suggest where you can improve the runtime of your code. There are many tricks in Python programming that can result in fast code without having to use Cython. I just want to share with you any tricks I know. As regards coding conventions, many programming languages have them and people who program in such a language would more or less adhere to the corresponding coding conventions. Remember that conventions are guidelines that many if not most experienced programmers find to result in readable, maintainable, and elegant looking code. This means that in some cases, it makes sense to break a convention. In case you are uncertain about whether to follow a convention or not, you need to use your judgement.



---

archive/issue_comments_098407.json:
```json
{
    "body": "Replying to [comment:9 mvngu]:\n> Replying to [comment:8 ncohen]:\n> Your improved documentation is certainly very clear to me. But note a typo in the following:\n\nFixed in the updated patch !\n\n> Don't take my comments above the wrong way.\n\nBy now I have understood that both your patience and attention to details are about boundless. It makes me all the more eager to learn from you !\n\nNathann",
    "created_at": "2010-11-28T08:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98407",
    "user": "https://github.com/nathanncohen"
}
```

Replying to [comment:9 mvngu]:
> Replying to [comment:8 ncohen]:
> Your improved documentation is certainly very clear to me. But note a typo in the following:

Fixed in the updated patch !

> Don't take my comments above the wrong way.

By now I have understood that both your patience and attention to details are about boundless. It makes me all the more eager to learn from you !

Nathann



---

archive/issue_comments_098408.json:
```json
{
    "body": "Attachment [trac_9910-fixing_documentation.patch](tarball://root/attachments/some-uuid/ticket9910/trac_9910-fixing_documentation.patch) by mvngu created at 2010-11-29 08:46:33",
    "created_at": "2010-11-29T08:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98408",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_9910-fixing_documentation.patch](tarball://root/attachments/some-uuid/ticket9910/trac_9910-fixing_documentation.patch) by mvngu created at 2010-11-29 08:46:33



---

archive/issue_comments_098409.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-29T08:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98409",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098410.json:
```json
{
    "body": "This is a comment from an outsider, so it may not make much sense: you mention in the docstring that this problem is NP-hard, and I agree there doesn't seem to be an algorithm that is polinomial in the number of edges, but:\n\nIn the paper \n\nhttp://dutta.csc.ncsu.edu/csc791_spring07/wrap/circuits_johnson.pdf\n\nthere is an algorithm to list all elementary circuits in a graph that is linear in the number of circuits. This algorithm is implemented in version 1.4 of networkx:\n\nhttps://networkx.lanl.gov/trac/ticket/394\n\nIs the situation for paths instead of circuits much different? Is a MILP algorithm better than listing all elementary paths by a Johnson-like algorithm and finding the max lenght? Maybe MILP is better in practice but is it in theory?",
    "created_at": "2010-12-31T16:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98410",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```

This is a comment from an outsider, so it may not make much sense: you mention in the docstring that this problem is NP-hard, and I agree there doesn't seem to be an algorithm that is polinomial in the number of edges, but:

In the paper 

http://dutta.csc.ncsu.edu/csc791_spring07/wrap/circuits_johnson.pdf

there is an algorithm to list all elementary circuits in a graph that is linear in the number of circuits. This algorithm is implemented in version 1.4 of networkx:

https://networkx.lanl.gov/trac/ticket/394

Is the situation for paths instead of circuits much different? Is a MILP algorithm better than listing all elementary paths by a Johnson-like algorithm and finding the max lenght? Maybe MILP is better in practice but is it in theory?



---

archive/issue_comments_098411.json:
```json
{
    "body": "Hello !\n\n> Is the situation for paths instead of circuits much different?\n\nThe situation for directed graphs is not different at all : by just replacing each undirected edge by two edges, on in each direction, you transform one problem into the other. Besides, your algorithms shouldn't make much more operations than necessary because of the transformation.\n\n>  Is a MILP algorithm better than listing all elementary paths by a Johnson-like algorithm and finding the max lenght? Maybe MILP is better in practice but is it in theory?\n\nLet me first begin by saying that I can not *stand* complexity theory. I mean -- I like the theory, some of its conjectures, it sometimes says interesting things, and even though it is most of the times for bad reasons (see *) it motivates people to do research on maths, which is perfectly nice.\n\nThis being said, many recent results and directions of research in complexity have forgotten practice a long time ago. They are still interesting results, they are still analysis of what our modelling of \"what is an efficient algorith\" is, (*) but there is a point where this modelling is not representative of the reality anymore (at which point we are expected to adapt our theory).\nSo in theory, no there are no differences between those two algorithms. Well, perhaps there is one : it is very hard to analyse the runtime of a specific linear program, especially when it makes use of many heuristics hidden in the LP solvers (and CPLEX and GLPK may behave very differently on the same instance, even though they are given the same formulations). On the other hand, I suspect it should be possible to produce graphs for which listing all the paths before finding one of maximum length (usually you would need to enumerat them all to be sure you found the best one, but if you happen to find a hamiltonian path at some point you needn't press further) takes an exponential time.\nWhich means I can not prove the LP is faster than the complete enumeration. Of course -- nothing more than that -- it is probably possible to do it anyway, my ignorance hopefully being a personnal drama :-D\n\nTo answer further, there is an heuristic added to the Longest Path method in Sage. It works by randomly extending paths, for as long as possible, with some other healthy rules to go back in the exploration if bad choices have been made. It isn't the algorithm you mentionned, but it is a good way to get an idea of their relative performances without having to implement the actual enumeration.\n\nLet me also add that if you were willing to implement this enumeration (and then again, I of course have no proof LP is better. Especially when we can put complexity analysis to death by saying -- \"we are just interested in practical instances\", which can not be defined. That's precisely where a simple programming trick can divide the running time by 100 even though Theory does not see the difference), using the NetworkX implementation would be a very bad choice, considering it is written in Python. I had to write an enumeration algorithm in Cython for the graph methods subgraph_search*, and the Python version I had written previously was just .... not working. I didn't say \"slow\", I said that the running time of the SAME algorithm was comparatively so large that it wasn't even worthy of being used for small instances. Yeah, there again they both have the same asymptotic complexity. Python is extremely slow for complete enumerations, so you really want to save running time by writing low-level code as soon as possible :-)\n\nIn the end, one thing to remember : I have no way to prove one is better than the other, but I suspect it is (LP is actually enumerating all the solutions -- with many heuristics -- but it is able to say very early \"I do not need to search further in this direction, because reasons that have no graph-theoretic meaning (the relaxed version of my LP) tell me there will be no solution this way). LP are very nice because they are easy to write, but it is very hard to know how efficient they are in practice. And complete enumeration in Python is often a waste of time :-)\n\nNote for myself : if I want to lead my war against complexity further, I first need to study it much more :-)\n\nHappy new year !\n\nNathann",
    "created_at": "2011-01-01T11:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98411",
    "user": "https://github.com/nathanncohen"
}
```

Hello !

> Is the situation for paths instead of circuits much different?

The situation for directed graphs is not different at all : by just replacing each undirected edge by two edges, on in each direction, you transform one problem into the other. Besides, your algorithms shouldn't make much more operations than necessary because of the transformation.

>  Is a MILP algorithm better than listing all elementary paths by a Johnson-like algorithm and finding the max lenght? Maybe MILP is better in practice but is it in theory?

Let me first begin by saying that I can not *stand* complexity theory. I mean -- I like the theory, some of its conjectures, it sometimes says interesting things, and even though it is most of the times for bad reasons (see *) it motivates people to do research on maths, which is perfectly nice.

This being said, many recent results and directions of research in complexity have forgotten practice a long time ago. They are still interesting results, they are still analysis of what our modelling of "what is an efficient algorith" is, (*) but there is a point where this modelling is not representative of the reality anymore (at which point we are expected to adapt our theory).
So in theory, no there are no differences between those two algorithms. Well, perhaps there is one : it is very hard to analyse the runtime of a specific linear program, especially when it makes use of many heuristics hidden in the LP solvers (and CPLEX and GLPK may behave very differently on the same instance, even though they are given the same formulations). On the other hand, I suspect it should be possible to produce graphs for which listing all the paths before finding one of maximum length (usually you would need to enumerat them all to be sure you found the best one, but if you happen to find a hamiltonian path at some point you needn't press further) takes an exponential time.
Which means I can not prove the LP is faster than the complete enumeration. Of course -- nothing more than that -- it is probably possible to do it anyway, my ignorance hopefully being a personnal drama :-D

To answer further, there is an heuristic added to the Longest Path method in Sage. It works by randomly extending paths, for as long as possible, with some other healthy rules to go back in the exploration if bad choices have been made. It isn't the algorithm you mentionned, but it is a good way to get an idea of their relative performances without having to implement the actual enumeration.

Let me also add that if you were willing to implement this enumeration (and then again, I of course have no proof LP is better. Especially when we can put complexity analysis to death by saying -- "we are just interested in practical instances", which can not be defined. That's precisely where a simple programming trick can divide the running time by 100 even though Theory does not see the difference), using the NetworkX implementation would be a very bad choice, considering it is written in Python. I had to write an enumeration algorithm in Cython for the graph methods subgraph_search*, and the Python version I had written previously was just .... not working. I didn't say "slow", I said that the running time of the SAME algorithm was comparatively so large that it wasn't even worthy of being used for small instances. Yeah, there again they both have the same asymptotic complexity. Python is extremely slow for complete enumerations, so you really want to save running time by writing low-level code as soon as possible :-)

In the end, one thing to remember : I have no way to prove one is better than the other, but I suspect it is (LP is actually enumerating all the solutions -- with many heuristics -- but it is able to say very early "I do not need to search further in this direction, because reasons that have no graph-theoretic meaning (the relaxed version of my LP) tell me there will be no solution this way). LP are very nice because they are easy to write, but it is very hard to know how efficient they are in practice. And complete enumeration in Python is often a waste of time :-)

Note for myself : if I want to lead my war against complexity further, I first need to study it much more :-)

Happy new year !

Nathann



---

archive/issue_events_010036.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-12T06:33:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9909#event-10036"
}
```



---

archive/issue_comments_098412.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-12T06:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9909#issuecomment-98412",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
