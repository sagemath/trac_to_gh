# Issue 487: problem with the is_principal method for fractional ideals in a number field.

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-24 05:29:07

Assignee: was

The Problem has been reported by Kevin McGown at http://groups.google.com/group/sage-forum/t/a8a6efc565e36339

In SAGE 2.8 it seems there is a problem with the is_principal method
for fractional ideals in a number field.  In the code below I create
the same ideal in two different ways and obtain two different answers
from is_principal (True and False). 


```
sage: K = QuadraticField(-119,'a')
sage: P2 = K.ideal([2]).factor()[0][0]
sage: I = P2^5
sage: a = K.0
sage: J = K.ideal([1/2*a+3/2])
sage: I==J
True
sage: I.is_principal()
False
sage: J.is_principal()
True
```


Kevin also suggested a fix:

```
I believe the problem is with the following line in the is_principal()
method:

if len (self.gens()) <= 1:

Instead it should read:

if len (self.gens_reduced()) <= 1:

Not 100% sure, but I thought I would bring it to your attention.

- Kevin
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-08-27 07:14:16

Another suggestion from Kevin:

```
Hello everyone,

I think my fix above was incorrect.  The relevant file is:
/sage-2.8.2-i386-Darwin/local/lib/python2.5/site-packages/sage/rings/
number_field/number_field_ideal.py

I think the problem is with the following line:
self.__is_principal = (len(v[0]) == 0) ## i.e., v[0] is the zero
vector

This above code gets 1 for the length of the zero vector.  I replaced
it with this line:
self.__is_principal = (v[0] == "[0]~")

I don't know if this is the best way to do it, but it seemed to fix
the problem for me.

- Kevin 
```



---

Comment by was created at 2007-09-06 09:19:23

Resolution: fixed


---

Comment by was created at 2007-09-06 09:19:23

The actual fix was a bit more complicated than described above, though the above was very helpful.
This is definitely fixed in sage > 2.8.3.5.
