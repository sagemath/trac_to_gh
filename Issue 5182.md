# Issue 5182: Strange Symmetrica segfault

Issue created by migration from https://trac.sagemath.org/ticket/5182

Original creator: jbandlow

Original creation time: 2009-02-04 22:49:42

Assignee: mhansen

CC:  jbandlow sage-combinat

Keywords: symmetrica

This is from sagenb running sage 3.3.alpha3:


```
sage: dd = { Partition([1]) : 1 } ; ee = { Partition([1]) : int(1) } ; s = SFASchur(QQ)
sage: (s._from_dict(dd), s._from_dict(ee)) # This is fine
(s[1], s[1])
sage: 1 * s._from_dict(dd) # This is fine
s[1]
sage: 1 * s._from_dict(ee) # This fails
Exception exceptions.TypeError: 'cannot convert a (= 1) to OP' in
'sage.libs.symmetrica.symmetrica._op_schur_general_dict' ignored
function: mult(1) 
python: �73x��
Connection to localhost closed.
```



This is a low priority for me, since the obvious workaround is not to put 'int's in this kind of dictionary, but I wanted to report it.


---

Comment by jbandlow created at 2010-05-06 14:03:25

Changing priority from minor to major.


---

Comment by jbandlow created at 2010-05-06 14:03:25

Replying to [ticket:5182 jbandlow]:
> This is from sagenb running sage 3.3.alpha3:
> 
> {{{
> sage: dd = { Partition([1]) : 1 } ; ee = { Partition([1]) : int(1) } ; s = SFASchur(QQ)
> sage: (s._from_dict(dd), s._from_dict(ee)) # This is fine
> (s[1], s[1])
> sage: 1 * s._from_dict(dd) # This is fine
> s[1]
> sage: 1 * s._from_dict(ee) # This fails
> Exception exceptions.TypeError: 'cannot convert a (= 1) to OP' in
> 'sage.libs.symmetrica.symmetrica._op_schur_general_dict' ignored
> function: mult(1) 
> python: �73x��
> Connection to localhost closed.
> }}}
> 
> 
> This is a low priority for me, since the obvious workaround is not to put 'int's in this kind of dictionary, but I wanted to report it.

Update in sage-4.4.  This bug can occur without using private methods.

```
sage: sage: s = SymmetricFunctions(QQ).schur()
sage: sage: s.sum_of_terms([ (Partition([i]), i) for i in range(3) ])
s[1] + 2*s[2]
sage: sage: s.sum_of_terms([ (Partition([i]), i) for i in range(3) ]) * 1
Exception TypeError: 'cannot convert a (= 1) to OP' in 'sage.libs.symmetrica.symmetrica._op_schur_general_dict' ignored
function: mult_bruch(2) not definied for object type:
kind of object is empty-object
python: function: mult_bruch(2) not definied for object type:
: Operation not permitted
```


This is a segfault and exits sage.


---

Comment by jbandlow created at 2011-03-14 18:59:44

These errors do not occur with sage 4.6.2.


---

Comment by mhansen created at 2011-03-14 21:43:05

Resolution: invalid
