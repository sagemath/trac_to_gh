# Issue 2232: Bug in 'digits' function for Integers

Issue created by migration from https://trac.sagemath.org/ticket/2232

Original creator: vgermrk

Original creation time: 2008-02-20 14:11:38

Assignee: somebody

This works

```
sage: 1.digits(16,'0123456789abcdef')
['1']
sage: 2.digits(16,'0123456789abcdef')
['2']
```

but this don't

```
sage: 0.digits(16,'0123456789abcdef')
[]
```


The problem exists for all bases. The '0'-value is never returned.


---

Comment by malb created at 2008-02-20 16:45:46

I agree that this is a bug since we have symbols to represent zero so we should use them.


---

Comment by robertwb created at 2008-02-20 16:48:06

This might be relevant to #2170 (or the other way around)


---

Comment by jbmohler created at 2008-03-01 16:41:08

I'm supposing that the poster of this bug wants:

```
sage: 0.digits(16,'0123456789abcdef')
['0']
```


I do not like that.  I think one should use str for this (witness 2.10.2's current operation):  

```
sage: 0.str(10)
'0'
sage: f=0.str(10)
sage: [c for c in f]
['0']
```


I don't think that what I suggested is a perfect analog for what may have desired, but I don't like the inconsistency that this desired "fix" introduces for digits.


---

Comment by vgermrk created at 2008-03-02 10:53:47

This example above (base=16) is from the docstring.
You're right that you should use ".str" if you just want to get the string representation of a number in a given base.

But the digits function can do more. It can take any indexable object as source for the digits.
So i think this is really a bug which should be fixed, because this 

```
sage: 0.digits(11,'pleasefixme')
```

should return

```
['p']
```



---

Comment by jbmohler created at 2008-03-03 19:39:38

I see that there is some precedent for agreeing that this is a bug:

```
sage: 0.ndigits()
1
```

Given my opinion that this bug is invalid, I would also want to change ndigits.  While on the subject of digits and ndigits, I think it is really awful that their default bases are not the same.


---

Attachment

The patches fixes the issue and adds a padto-parameter,

see discussion [http://groups.google.com/group/sage-devel/browse_thread/thread/f9d7b5016e237b22](http://groups.google.com/group/sage-devel/browse_thread/thread/f9d7b5016e237b22)


---

Comment by jbmohler created at 2008-04-04 11:18:33

With-out applying and running the code, I have some comments.

 1) I do not like the change in semantics when the digits are passed in.  I think that is way too arbitrary.  Essentially, you are overriding the default to padto when digits are passed in and making it default padto=1.

 2) The "zero = 0" in the snippet below will create a python int with 0 -- it should be a sage int.  Use the_integer_ring._zero_element

```
 
if digits is None: 
    zero = 0           # value for padding 
else: 
    zero = digits[0]   # value for padding 
```


 3) Could you also in this patch change ndigits so it returns 0 for 0?  I think that accurately reflects the will of sage-devel and fits in this patch nicely.

Thanks for coding this patch up!


---

Attachment

the second (additional) patch takes care of jbmohler's remarks.


---

Comment by jbmohler created at 2008-04-04 12:49:58

I applied both patches, checked it out a bit and give a positive review.


---

Comment by mabshoff created at 2008-04-04 18:14:36

Doctests pass. Merged in Sage 3.0.alpha1


---

Comment by mabshoff created at 2008-04-04 18:14:36

Resolution: fixed
