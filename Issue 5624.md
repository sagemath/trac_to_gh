# Issue 5624: matrices cache their hash, which causes subtle bugs when moving objects between 32/64 bit

Issue created by migration from https://trac.sagemath.org/ticket/5624

Original creator: was

Original creation time: 2009-03-28 15:17:37

Assignee: cwitty


```
On Sat, Mar 28, 2009 at 6:26 AM, Jason Bandlow <...> wrote:
>> I'm guessing this is a subtle 32 versus 64-bit issue involving
>> pickling and assumptions made somewhere in the combinat or other sage
>> code involving 32/64-bit.  The notebook is 64-bit and I bet your
>> computer is 32-bit.
>>
>> By the way, this works on the notebook in the context of your session above:
>>
>> for a, b in M.iteritems():
>>     if a == key: print b
>>
>
> Thanks William!  This does seem likely to be the problem.  I'll do more
> investigation when I get a chance and see if I can find out precisely
> where the problem is.

I know of one place in sage where objects cache their hash for efficiency reasons (e.g., I think Sage matrices do). I hadn't thought about the fact that pickling, moving to an object to a platform where the hashes are different, and unpickling, would result in the subtle issue above, but that makes sense.   Here is an example:

On a 32-bit platform do this:

sage: a = matrix(ZZ,2,[1,-2,4,1993938292]); a.set_immutable(); b = {a:5}; save(b,'/Users/wstein/b.sobj')

Then load b on a 64-bit platform (e.g. ,sage.math):

sage: a = matrix(ZZ,2,[1,-2,4,1993938292]); a.set_immutable(); b = load('b.sobj'); b[a]
boom! KeyError ...
sage: sage: b.keys()[0] == a
True

The fix here is that right before pickling the cached hash of the matrix should be deleted.

I don't know any other places in Sage that do the above.  
```



---

Comment by cwitty created at 2009-03-28 16:41:34

`CombinatorialObject` (and hence also its many subclasses) does this; see `__hash__` at line 769 of sage/combinat/combinat.py
