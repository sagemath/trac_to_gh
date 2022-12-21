# Issue 4731: Repeated computation involving Maxima is getting slower and slower

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2008-12-06 23:18:40

Assignee: burcin

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


---

Comment by mabshoff created at 2008-12-07 06:04:59

Changing assignee from burcin to mabshoff.


---

Comment by mabshoff created at 2008-12-07 06:04:59

Changing component from calculus to performance.


---

Comment by SimonKing created at 2009-07-27 08:17:43

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

Comment by mvngu created at 2009-07-27 08:18:17

See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/863e59ba164590c5) thread for a simple example of such memory leaks.


---

Comment by mvngu created at 2009-08-03 23:46:31

Here's a [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/cacc0b6dd40f7624) thread related to timeit getting slower and slower with each call.


---

Comment by was created at 2009-08-24 15:51:46

I have verified that #6818 *does* fix this problem:


---

Comment by mvngu created at 2009-08-25 01:18:12

Closing this as a duplicate of #6818.


---

Comment by mvngu created at 2009-08-25 01:18:12

Resolution: duplicate
