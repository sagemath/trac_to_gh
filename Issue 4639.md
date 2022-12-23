# Issue 4639: bad memory leak with exponentiation

Issue created by migration from https://trac.sagemath.org/ticket/4639

Original creator: bober

Original creation time: 2008-11-27 19:06:08

Assignee: somebody

CC:  robertwb

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



---

Comment by mabshoff created at 2008-11-27 19:23:22

This is indeed a grave bug.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-27 19:23:22

Changing priority from critical to blocker.


---

Comment by mabshoff created at 2008-11-28 02:31:09

Hmm, 

Burcin and I have been looking at code he has been writing and there seems to be a caching issue with the coercion system. Now, I don't want to outright blame coercion here without any hard evidence, but the timing (3.0.2 to now) suggests that it could be involved here. So let's add robertwb to the CC and see if he can come up with anything. I will collect some evidence and hopefully someone else will take over.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-28 02:40:00

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

Comment by burcin created at 2008-11-28 02:51:49

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

Comment by mabshoff created at 2008-11-28 21:35:49

This ticket might also cause #4631.

Cheers,

Michael


---

Comment by robertwb created at 2008-12-02 12:04:38

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

Comment by mabshoff created at 2008-12-02 15:49:34

Hi Robert,

do you want me to valgrind here or are you already on top of this?

Cheers,

Michael


---

Comment by robertwb created at 2008-12-02 19:50:02

I think I can dig further, this is just as far as I got last night. It's probably a caching, not malloc, issue.


---

Attachment

this fixes the leak in coerce, not in exponentiation


---

Comment by robertwb created at 2008-12-02 22:25:40

Better caching for homsets fixes the leak for coercion.


---

Comment by mabshoff created at 2008-12-02 22:43:51

Maybe we should move the problem with exponentiation to another ticket if it proves difficult to fix so we can get the coercion fix in. I am doctesting this now, but I will hold on a merge until we have gotten #3623 and #4276 in.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-03 00:05:29

The patch RobertWB posted does pass doctesting.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-03 01:16:00

#4683 might be a dupe of this ticket.

Cheers,

Michael


---

Comment by was created at 2008-12-06 22:33:04

I've read the patch and give it a positive review.  But the patch doesn't resolve the ticket, as Robert points out.   So after applying the patch, I guess you have to open a new ticket?  Or???  

Anyway -- don't just randomly close this ticket after applying the patch...


---

Comment by mabshoff created at 2008-12-08 11:26:01

I have deleted the patch and moved it to its own ticket at #4740 since it does not fix the original problem reported. 

Cheers,

Michael


---

Comment by robertwb created at 2008-12-14 05:51:51

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

Comment by robertwb created at 2008-12-14 05:55:52

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

Comment by robertwb created at 2008-12-14 06:30:52

I am almost sure the above is what's going wrong, and it gets invoked by __call__. 

guppy gives a total of 40420 bytes on these runs... and nothing new after repeated runs (despite get_memory_usage going up and up). However, the memory still goes up. Mabshoff, could you valgrind this and see if anything suspicious comes up? Perhaps up the loop to 100000, or diff the run from Python with that from Cython, to make it more clear where the error is...


---

Comment by mabshoff created at 2008-12-14 06:33:26

Will do. Any news on the pickle failure for #4740?

Cheers,

Michael


---

Comment by robertwb created at 2008-12-14 09:01:29

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

Comment by robertwb created at 2008-12-14 11:28:24

Install cython-0.10.3.spkg at http://sage.math.washington.edu/home/robertwb/cython/ , which contains a fix to http://trac.cython.org/cython_trac/ticket/162 and I think is the underlying cause here (and probably elsewhere).


---

Comment by mabshoff created at 2008-12-14 15:53:39

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

Comment by mabshoff created at 2008-12-14 17:41:59

For the record: The cython.spkg upgrade to 0.10.3 is #4798.

Cheers,

Michael


---

Comment by robertwb created at 2008-12-15 18:30:57

This is the bug that will never die... I'll keep looking at that last case.


---

Comment by mabshoff created at 2008-12-15 18:43:17

If there ever was a blocker for 3.2.2 :)

Cheers,

Michael


---

Comment by SimonKing created at 2008-12-16 13:16:29

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

Attachment

I believe I have located and resolved the issue. After tracing through all kinds of coercion and homset code, and reading tons of Cython code looking for memory leaks, it turns out that this was caused by all Parents ever created being cached due to old debugging code. (Wow, wish I'd looked there first! :)

Some old, unnecessary code has been removed from the generic __call__ method as well.


---

Comment by mabshoff created at 2008-12-16 20:35:59

Nice! I am testing away at the moment :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-16 20:38:31

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

Comment by mabshoff created at 2008-12-17 03:28:13

Positive review for 4639-parent-memleak.patch - w00t

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-17 14:01:23

Merged in Sage 3.2.2.rc1


---

Comment by mabshoff created at 2008-12-17 14:01:23

Resolution: fixed
