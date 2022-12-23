# Issue 4896: fill in missing magma --> sage conversions

Issue created by migration from https://trac.sagemath.org/ticket/4896

Original creator: was

Original creation time: 2008-12-31 02:33:36

Assignee: was

Make it so all the following work:

```
sage: magma(QQ['x,y'].0).sage()
```


Note that a huge number of sage-->magma conversions for ring elements now work.  To find examples where the converse doesn't work, use this script:


```
sage: for R in sage.rings.tests.random_rings(): print R, magma(R.random_element()).sage()
```

after applying #4779.

When the above loop runs for "a while" without crashing (after applying #4779), then this ticket can be closed.


---

Comment by mabshoff created at 2009-01-02 07:07:58

No patch, i.e. better luck in 3.4 :)

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-23 02:43:29

Changing type from defect to enhancement.


---

Comment by jdemeyer created at 2015-06-23 13:49:26

Changing component from interfaces to interfaces: optional.


---

Comment by chapoton created at 2018-06-23 08:08:24

Got

```
Multivariate Polynomial Ring in x0, x1, x2, x3, x4, x5, x6, x7 over Ring of integers modulo 30768  File "<string>", line 1
    Residue class ring of integers modulo Integer(30768)['x0, x1, x2, x3, x4, x5, x6, x7'.replace('$.', 'x').replace('.', '')](dict([ ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x2'), Integer('0x0'), Integer('0x0'), Integer('0x0') ), Integer(17090) ), ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x2'), Integer('0x0'), Integer('0x0') ), Integer(8615) ), ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x1'), Integer('0x0'), Integer('0x0'), Integer('0x1'), Integer('0x0') ), Integer(24187) ), ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x1'), Integer('0x0'), Integer('0x0'), Integer('0x0') ), Integer(5374) ), ( ( Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0'), Integer('0x0') ), Integer(27378) ) ]))
                ^
SyntaxError: invalid syntax
```

and

```
Univariate Polynomial Ring in x over Ring of integers modulo 11908  File "<string>", line 1
    Residue class ring of integers modulo 11908['x'.replace('$.', 'x').replace('.', '')]([ 9823, 11770, 6616 ])
                ^
SyntaxError: invalid syntax
```



---

Comment by chapoton created at 2018-06-23 12:19:59

Comes from

```
sage: R=Zmod(137)
sage: magma(R)
Residue class ring of integers modulo 137
sage: magma(R).sage()
  File "<string>", line 1
    Residue class ring of integers modulo Integer(137)
                ^
SyntaxError: invalid syntax
```



---

Comment by chapoton created at 2018-06-23 12:20:34

Changing keywords from "" to "magma".


---

Comment by chapoton created at 2018-06-23 14:34:34

New commits:


---

Comment by git created at 2018-06-23 14:38:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2018-06-23 15:26:25

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2018-06-24 11:25:14

branch was moved to #25640


---

Comment by vdelecroix created at 2018-08-03 19:20:18

update milestone 8.3 -> 8.4
