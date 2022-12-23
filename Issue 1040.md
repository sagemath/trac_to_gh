# Issue 1040: bug in new ring extension constructor

Issue created by migration from https://trac.sagemath.org/ticket/1040

Original creator: was

Original creation time: 2007-10-31 18:14:03

Assignee: was

Now that we allow notation such as

```
QQ[2^(1/3)]
```

to create a number field, the following is totally wrong and
needs to be fixed ASAP:


```
sage: K.<a> = QQ[2^(1/3)]
sage: K
Univariate Polynomial Ring in a over Rational Field
sage: parent(a)
Univariate Polynomial Ring in a over Rational Field
```



---

Comment by was created at 2007-11-01 07:20:03

More:

This is because the preparser is written stupidly in this case:


```
sage: K.<a> = QQ[2^(1/3)]
sage: preparse('K.<a> = QQ[2^(1/3)]')
'K = QQ["a"]; (a,) = K._first_ngens(Integer(1))'
```


I think this is what *should* happen:

```
sage: K.<a> = QQ[2^(1/3)]
sage: preparse('K.<a> = QQ[2^(1/3)]')
'K = QQ["2^(1/3)"]; (a,) = K._first_ngens(Integer(1))'
```


The previous behavior should only happen in the case when nothing is between brackets, as a sort of short cut:

```
sage: K.<a> = QQ[2^(1/3)]
sage: preparse('K.<a> = QQ[]')
'K = QQ["a"]; (a,) = K._first_ngens(Integer(1))'
```



---

Comment by ncalexan created at 2007-11-03 20:10:37

Changing assignee from was to ncalexan.


---

Attachment


---

Comment by was created at 2007-11-03 23:43:20

Resolution: fixed
