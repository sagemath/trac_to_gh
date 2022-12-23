# Issue 4974: make sage.libs.pari.gen._normalize_slice a miscellaneous function for dealing with slices

Issue created by migration from https://trac.sagemath.org/ticket/4974

Original creator: jason

Original creation time: 2009-01-14 10:27:30

Assignee: craigcitro

CC:  jason

Also, it would be good to optimize it if possible.


```
[04:21] <craigcitro> yeah, file a ticket for that and assign it to me.
[04:21] <jason-> (couldn't get cimport to work...)
[04:22] <craigcitro> well, the pari gen.pyx probably wasn't the best place for that function
[04:22] <craigcitro> so it needs to be moved anyway
```




---

Comment by craigcitro created at 2009-01-14 10:52:45

patch not necessarily ready for review yet.


---

Comment by craigcitro created at 2009-01-14 11:54:02

I think this is good to go.


---

Comment by craigcitro created at 2009-01-14 11:54:02

Changing status from new to assigned.


---

Comment by ylchapuy created at 2009-01-14 13:33:44

Some questions/remarks.
Shouldn't the following always be true ? (at least this is what I understand from the docstring)

```python
normalize_slice( s , size_list) == range(size_list)[s.start:s.stop:s.step]
```


If no (which is the case actually) this looks quite incoherent to me;
if yes, is there a reason not to rewrite this fonction as a one liner?


---

Comment by ylchapuy created at 2009-01-14 13:47:54

forget the one liner thing it's obviously a bad idea


---

Comment by craigcitro created at 2009-01-14 18:15:31

Wait, so disregarding whether or not we'd want to implement things that way -- are you still saying there are cases where that isn't true?


---

Comment by jason created at 2009-01-14 18:23:02

There is an inconsistency with standard python:


```
[12:12] <jason-> sage.misc.misc_c.normalize_slice(slice(2,None,-1),3)
[12:12] <jason-> gives me 2
[12:12] <jason-> but 
[12:12] <jason-> sage: range(3)[2::-1]
[12:12] <jason-> [2, 1, 0]
```



---

Comment by craigcitro created at 2009-01-14 18:25:02

Jason Grout just brought up an example in IRC where exactly that would happen. Here's a case:


```
sage: range(3)[2::-1]
[2, 1, 0]
```


`normalize_slice` will *not* return that, since it interprets a missing `stop` to be equal to `size`. This isn't documented as part of the Python semantics, but I think we should switch it to behave the same way regardless. (Also, it'll be easy to implement.)

This is now `needs work` until I change this.


---

Comment by craigcitro created at 2009-01-14 18:30:15

Another case brought up by Jason Grout:


```
sage: range(5)[-6:]
[0, 1, 2, 3, 4]
```



---

Comment by ylchapuy created at 2009-01-14 19:36:04

and another one from the docstring...

```
sage: range(20)[5:8:-1]
[]
```



---

Attachment

apply normalize_size.patch on top of previous patch.  This corrects all errors pointed out above and I believe is faster and simpler as well.


---

Comment by ylchapuy created at 2009-01-14 23:01:44

A lot better, but there are still bugs.

I would recommand to try something like this to test extensively:


```python
def safe_norm(i,j,k,l):
    try:
        return sage.misc.misc_c.normalize_slice(slice(i,j,k),l)
    except ValueError:
        return "error"

def safe_range(i,j,k,l):
    try:
        return range(l)[i:j:k]
    except ValueError:
        return "error"

d=[-5,-4,-3,-2,-1,0,-1,-2,-3,-4,-5,None]
ld=len(d)-1
for r in xrange(500):
    i=d[randint(0,ld)]
    j=d[randint(0,ld)]
    k=d[randint(0,ld)]
    l=randint(-8,8)
    r1=safe_norm(i,j,k,l)
    r2=safe_range(i,j,k,l)
    if not r1==r2:
        print i,j,k,l,r1,r2
```



---

Comment by ylchapuy created at 2009-01-15 01:43:01

draft for the future patch


---

Attachment

I have no clean install of sage to do the real patch, but I hope it helps...


---

Comment by jason created at 2009-01-15 04:17:56

ylchapuy: nice.  I like how you avoided the redundant comparisons in my code.  

In scanning through your code, it has a few places where the stuff following the +=size lines should be taken out of the body of the if statement and placed after the if statement instead.


---

Comment by jason created at 2009-01-15 04:40:23

Okay, I think this makes all of this work redundant.  Equivalent functionality (and mostly equivalent or faster times) are found in the implementation:


```
range(*s.indices(size))
```


where s is the slice, size is the size of list.


---

Comment by jason created at 2009-01-15 04:43:31

There are several nice things about the above.  First, python handles all of the weird corner cases so that everything is consistent.  Second, you can use xrange to get an iterator over the indices instead of the list.  Third, you avoid one more function call.


---

Comment by craigcitro created at 2009-01-15 04:46:57

And fourth, it does more error checking than we were doing (dealing with unnecessarily large size, etc) ...

I think we should do this. One question: should we keep all our doctests? It's like documentation for how you can use slices, which doesn't seem to appear elsewhere. :)


---

Attachment


---

Comment by craigcitro created at 2009-01-15 05:53:21

What Jason says above is exactly right -- there's no point trying to outdo Python, because it already is quite fast, and does all this for us. Plus, we can't miss corner cases this way. 

Ultimately, things could get faster with nice Cython support for slices. This isn't wildly pressing, but it should be easy to implement.

Apply only the newest `trac-4974.patch`. This patch simply removes `normalize_slice`.

We should make a note about using this for slices somewhere -- apparently, `range(*s.indices(size))` is a standard Python idiom (it's in *Python in a Nutshell*), so we should use it more.


---

Comment by jason created at 2009-01-15 06:10:26

+1 to the code cruft removal and adoption of standard python constructs.  I'm opening another ticket to add information about slices to the developer guide.

This patch applies and doctests pass in the file.


---

Comment by mabshoff created at 2009-01-18 15:49:40

Resolution: fixed


---

Comment by mabshoff created at 2009-01-18 15:49:40

Merge trac-4974.patch in Sage 3.3.alpha0
