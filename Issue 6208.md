# Issue 6208: [with patch, needs review] Improving gap interface by pre-compiling certain regular expressions

Issue created by migration from https://trac.sagemath.org/ticket/6208

Original creator: SimonKing

Original creation time: 2009-06-04 11:54:06

Assignee: SimonKing

Keywords: gap interface expect regular expression

At http://groups.google.com/group/sage-support/browse_thread/thread/657ef562de60fc6a
Jerome pointed out that the built in comparison of permutation groups sometimes is rather sluggish compared with comparison of their lists of elements.

While trying to find a reason, I found that the method ``_execute_line`` of the gap interface makes a non-optimal use of regular expressions: One and the same pattern is compiled over and over again.

I did not succeed to solve the poster's original concern. But at least I could speed up the gap interface.

Without the patch, I had

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: G=SymmetricGroup(7)
sage: time L=[X for X in G if X.order()==2]
CPU times: user 10.19 s, sys: 2.12 s, total: 12.31 s
Wall time: 15.48 s
```

| Sage Version 4.0, Release Date: 2009-05-29                         |
| Type notebook() for the GUI, and license() for information.        |
With the patch, I have

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: expect-devel
sage: G=SymmetricGroup(7)
sage: time L=[X for X in G if X.order()==2]
CPU times: user 4.02 s, sys: 0.17 s, total: 4.19 s
Wall time: 6.13 s
```

| Sage Version 4.0, Release Date: 2009-05-29                         |
| Type notebook() for the GUI, and license() for information.        |
__How does the patch work?__

The method ``_execute_line`` contains a ``while`` loop. In the loop, the expect interface is called, searching for one long and one short pattern.

Without my patch, ``expect`` would compile the two patterns over and over again. With my patch, the patterns will be compiled _once_ (I think the ``_start`` method is an appropriate place), stored as attributes, and then ``expect_list`` is called without the need to re-compile the patterns.

Here is another evidence that it works. Without the patch:

```
sage: gap._start()
sage: prun gap._execute_line('b:=1;')

         3258 function calls (3243 primitive calls) in 0.015 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       26    0.001    0.000    0.010    0.000 sre_compile.py:501(compile)
       26    0.001    0.000    0.002    0.000 sre_compile.py:367(_compile_info)
       26    0.001    0.000    0.003    0.000 sre_parse.py:385(_parse)
        7    0.001    0.000    0.001    0.000 sre_compile.py:213(_optimize_charset)
       15    0.001    0.000    0.001    0.000 {select.select}
        1    0.001    0.001    0.001    0.001 {method 'clear' of 'dict' objects}
        8    0.001    0.000    0.003    0.000 pexpect.py:914(expect_list)
      186    0.001    0.000    0.001    0.000 sre_parse.py:188(__next)
       83    0.001    0.000    0.011    0.000 re.py:227(_compile)
    36/31    0.001    0.000    0.001    0.000 sre_parse.py:146(getwidth)
    31/26    0.000    0.000    0.002    0.000 sre_compile.py:38(_compile)
      657    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        8    0.000    0.000    0.012    0.001 pexpect.py:815(compile_pattern_list)
       26    0.000    0.000    0.004    0.000 sre_parse.py:669(parse)
      156    0.000    0.000    0.001    0.000 sre_parse.py:207(get)
  656/651    0.000    0.000    0.000    0.000 {len}
...
```


With the patch:

```
sage: gap._start()
sage: prun gap._execute_line('b:=1;')
         478 function calls in 0.006 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       15    0.004    0.000    0.004    0.000 {select.select}
        8    0.001    0.000    0.005    0.001 pexpect.py:914(expect_list)
       15    0.000    0.000    0.004    0.000 pexpect.py:498(read_nonblocking)
      188    0.000    0.000    0.000    0.000 {built-in method search}
       15    0.000    0.000    0.000    0.000 {posix.read}
        1    0.000    0.000    0.006    0.006 gap.py:573(_execute_line)
       15    0.000    0.000    0.000    0.000 pexpect.py:739(isalive)
       30    0.000    0.000    0.000    0.000 {posix.waitpid}
        1    0.000    0.000    0.000    0.000 sre_compile.py:367(_compile_info)
        1    0.000    0.000    0.000    0.000 sre_compile.py:501(compile)
        2    0.000    0.000    0.000    0.000 {posix.write}
        2    0.000    0.000    0.000    0.000 re.py:227(_compile)
        2    0.000    0.000    0.000    0.000 pexpect.py:656(send)
        1    0.000    0.000    0.000    0.000 sre_parse.py:385(_parse)
       32    0.000    0.000    0.000    0.000 {built-in method start}
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
       25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        2    0.000    0.000    0.000    0.000 pexpect.py:815(compile_pattern_list)
        1    0.000    0.000    0.000    0.000 sre_parse.py:146(getwidth)
       15    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        2    0.000    0.000    0.004    0.002 pexpect.py:855(expect)
        8    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
        5    0.000    0.000    0.000    0.000 sre_parse.py:188(__next)
       15    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        1    0.000    0.000    0.000    0.000 sre_parse.py:669(parse)
        2    0.000    0.000    0.000    0.000 {time.sleep}
        1    0.000    0.000    0.000    0.000 sre_compile.py:486(_code)
       20    0.000    0.000    0.000    0.000 {len}
...
```


Now I am curious what ``select.select`` refers to. But I think the improvement is clear.


---

Attachment

Improved performance of the gap interface by pre-compiling regular expressions


---

Comment by SimonKing created at 2009-06-04 12:15:33

Concerning the timings, one cautious remark:

I _did_ have the good timing with my patch. But later, I tried again, and it was not as good (though still faster than without the patch).

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: expect-devel
sage: G=SymmetricGroup(7)
sage: time L=[X for X in G if X.order()==2]
CPU times: user 8.50 s, sys: 1.88 s, total: 10.39 s
Wall time: 13.05 s
```

| Sage Version 4.0, Release Date: 2009-05-29                         |
| Type notebook() for the GUI, and license() for information.        |
Perhaps someone can explain why this happens. It seems that this is a bad benchmark test.

So, I would appreciate a better (more stable) example.


---

Comment by SimonKing created at 2009-06-04 12:30:30

Replying to [comment:1 SimonKing]:
> So, I would appreciate a better (more stable) example.

Perhaps the one below. Since there is no caching involved, one can do ``timeit`` and gets more reliable times. Moreover, it uses the interface more directly.

Without the patch:

```
sage: G=SymmetricGroup(7)
sage: g=G._gap_()
sage: l=g.Elements()
sage: timeit ("L=[gap.eval(l.name()+'[%d]^2'%(i)) for i in range(1,7.factorial()+1)]")
5 loops, best of 3: 3.18 s per loop
```


With the patch:

```
sage: G=SymmetricGroup(7)
sage: g=G._gap_()
sage: l=g.Elements()
tsage: timeit ("L=[gap.eval(l.name()+'[%d]^2'%(i)) for i in range(1,7.factorial()+1]")
5 loops, best of 3: 1.93 s per loop
```



---

Comment by mhansen created at 2009-06-04 19:28:12

Resolution: fixed


---

Comment by mhansen created at 2009-06-04 19:28:12

Looks good to me.  I had actually been meaning to do this as well.

Merged in 4.0.1.rc1.


---

Comment by mvngu created at 2009-06-06 22:15:42

The milestone for this one should be Sage 4.0.1. Unfortunately, it's still stuck at Sage 4.0.2. Someone with admin priviledges on trac might know how to do that.


---

Comment by craigcitro created at 2009-06-07 21:44:19

Just correcting the milestone (since it was already merged).
