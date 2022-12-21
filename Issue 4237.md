# Issue 4237: magma -- finite field matrix conversions

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-02 16:29:16

Assignee: was


```
2) Converting matrices (over finite fields) is very slow for the dimensions
I'm interested in (the smallest dimension is 10000x10000) because it each
element is converted individually. Also, the conversion eats a lot of RAM due
to the large string that is created.
```


Reported by Martin Albrecht


---

Comment by was created at 2008-10-02 16:29:48

Changing status from new to assigned.


---

Comment by malb created at 2008-12-11 10:16:08

> Which base field are you working over?  GF(2)?  GF(997^1000,'a')?

I am particularly interrested in GF(2) but other finite fields should behave the same. To reproduce:


```
sage: A = random_matrix(GF(2),10^4,10^4)
sage: Am = magma(A) # watch the RAM consumption
```



---

Comment by was created at 2008-12-12 00:08:33

Which version of magma are you using and on which operating system?  I think there is a major bug in Magma-2.14 on OS X where it takes a vast amount of memory to parse any input above a certain threshhold (that threshhold is maybe 1000x1000 matrices).  Doing the same computation on sage.math (Linux) and it takes almost no memory.  There's not much I can do about that, except complain to Magma. 

William


---

Comment by malb created at 2008-12-12 00:23:55

I think something can be done:


```
sage: A = random_matrix(GF(2),2*10^4,2*10^4)
sage: AM = magma(A)
```


This will create a *huge* string in memory (in the Sage process), write that to disk and then read the file into Magma. We could at least write the strings in smaller chunks to disk to avoid the RAM consumption on the Sage side.

Btw. Magma crashes on me on sage.math:


```
before (last 100 chars): home/was/s/data/extcode//magma/latex/latex.m is compiled for newer version than current executable
```



---

Comment by was created at 2008-12-12 02:14:53

> Btw. Magma crashes on me on sage.math: 

That's because I installed a newer magma for myself locally, and it overwrites the .sig files, so the system-wide magma doesn't work.  I deleted them and recreated them with the old version.  If you use your own copy of sage this won't be an issue.


---

Comment by was created at 2008-12-12 03:16:19

Regarding your example

```
sage: A = random_matrix(GF(2),2*10^4,2*10^4)
```

I don't think there is any way to reasonably expect to use pexpect or a file to convert that matrix to Magma quickly using anything like is currently done in Sage or like you suggest even.  Just doing A.str() takes nearly 2GB and takes about the same amount of RAM as A._magma_init_(magma):

```
sage: A = random_matrix(GF(2),2*10^4,2*10^4)
sage: time s = A._magma_init_(magma)
pCPU times: user 203.00 s, sys: 7.73 s, total: 210.73 s
Wall time: 211.47 s
sage: get_memory_usage()
1274.81640625
sage: len(s)
800000011

Versus

sage: A = random_matrix(GF(2),2*10^4,2*10^4)
sage: b = str(A)
sage: b = A.str()
sage: get_memory_usage()
1273.48828125
sage: len(b)
800039999
```


Writing to a file as we go would reduce memory usage at any given moment, but will take as long or longer -- which means several minutes -- which seems unacceptable.   

The optimal solution for your application would be to write a Sage function that writes to file a mod-2 matrix in a single packed binary format, and a Magma function that reads that file and makes a matrix.  As far as I can tell, the *ONLY* way to turn a string into anything of any use in Magma is to use the function StringToInteger, which fortunately has a version that takes a base:

```
> StringToInteger("af",16);
175
```


In all cases, it would be immensely useful for this if there were a Sage function like this:


```
sage: A = random_matrix(GF(2),2*10^4,2*10^4)
sage: n = A._as_packed_integer()
```


The output would be an integer that has `2*10<sup>4*2*10</sup>4` digits in base 2, or 

```
2*10^4*2*10^4/4 = 100000000 = 10^8
```

digits in base 16.   Computing the base-16 string representation of such a massive number in Sage takes about a half second:

```
sage: b = 2*10^4*2*10^4
sage: s = ZZ.random_element(x=0,y=2^b)
sage: time len(s.str(16))
CPU times: user 0.45 s, sys: 0.18 s, total: 0.63 s
```

Memory usage for storing the number and *also* the string representation is about 111MB, which is reasonable (much better than several GB, which is the current situation). 

Writing our massive base-16 string to a file takes about 0.5 seconds.

```
sage: time open('foo','w').write(t)
CPU times: user 0.00 s, sys: 0.56 s, total: 0.56 s
Wall time: 0.56 s
```


Reading it into Magma takes about 2.5 seconds:

```
sage: magma.eval('time A := Read("foo");')
'Time: 2.260'
```


Incidentally, Python is literally ALMOST TEN TIMES faster at reading in a file that Magma!!

```
sage: time k = open('foo').read()
CPU times: user 0.00 s, sys: 0.28 s, total: 0.28 s
```


Anyway, now that we have that string in Magma, we convert it to an integer, which takes 3.36 seconds:

```
sage: magma.eval('time n := StringToInteger(A, 16);')
'Time: 3.360'
```


Incidentally, the same operation in Sage is over twice as faster:

```
sage: time k = ZZ(t, base=16)
CPU times: user 1.14 s, sys: 0.25 s, total: 1.39 s
Wall time: 1.39 s
```


OK, so the one remaining step is to convert that big integer in Magma into a boolean matrix in Magma.  This is probably going to be the killer bottleneck.  ...
In fact, I'm totally stumped about how to turn a packed integer that corresponds to a matrix over GF(2) into anything useful.  There seems to be no "bitwise or" on integers, no way to get the ith bit of an integer, nothing!  All I can think to do is "mod 2" and divide by 2 repeatedly, but dividing by 2 is very expensive.

There is the command StringToIntegerSequence, but it stupidly only works with numbers in base 10, making it utterly and completely useless. 

I'm stumped.


---

Comment by was created at 2008-12-12 05:12:30

For the record using `StringToIntegerSequence` on 0/1 integers, I can transfer 4*10^8 zeros and ones from Sage to Magma in 102 seconds, where the time is totally dominated by Magma's StringToIntegerSequence command.

```
sage: time open('/home/was/foo','w').write('1 '*10^8)
CPU time: 1.58 s,  Wall time: 1.58 s
sage: %magma
sage: time a := Read("/home/was/foo");
sage: time b := StringToIntegerSequence(a);
Time: 4.180
Time: 18.910
sage: time open('/home/was/foo','w').write('1 '*(2*10^4*2*10^4))
CPU time: 6.38 s,  Wall time: 6.37 s
sage: %magma
sage: time a := Read("/home/was/foo");
sage: time b := StringToIntegerSequence(a);
Time: 17.410
Time: 79.150
sage: 17.4 + 79.15 + 6.37
102.920000000000
```


Incidentally, I estimate that it would take 326 seconds (isntead of 79 seconds) to do the same thing Sage's `StringToIntegerSequence` does in pure Python:

```
sage: v = '1 '*(2*10^3*2*10^3)
sage: time z =[int(a) for a in v.split()]
CPU time: 3.13 s,  Wall time: 3.26 s
```

One would have to use Cython or something to beat that, though it doesn't matter for what we're doing. 

Back to our story.  So if we use the Magma parser itself to read in a boolean vector of length 4*10^8, I estimate it will take 384 seconds just for reading, which is about 4 times as long as above, so StringToIntegerSequence beats using the parser. 

```
sage: n = 10^7
sage: s = ('v := Vector(GF(2),%s,%s);'%(n, [1]*n)).replace(' ', '')
sage: time open('/home/was/foo','w').write(s)
Time: CPU 0.12 s, Wall: 0.13 s
sage: time magma.eval('load "/home/was/foo";')
'Loading "/home/was/foo"'
CPU time: 0.00 s,  Wall time: 9.60 s
sage: n = 2*10^7
sage: s = ('v := Vector(GF(2),%s,%s);'%(n, [1]*n)).replace(' ', '')
sage: time open('/home/was/foo','w').write(s)
Time: CPU 0.23 s, Wall: 0.23 s
sage: time magma.eval('load "/home/was/foo";')
'Loading "/home/was/foo"'
CPU time: 0.00 s,  Wall time: 18.72 s
sage: 4*10^8/10^7 * 9.6
384.000000000000
```


Interestingly, just using the Magma parser to read in a sequence of 1's in decimal without putting `Vector(GF(2), n, ...)` around the sequence takes WAY longer, i.e., I estimate it would take about 40,000 seconds (!):

```
sage: n = 10^5
sage: time s = ('v := %s;'%[1]*n).replace(' ', '')
sage: time open('/home/was/foo','w').write(s)
Time: CPU 0.02 s, Wall: 0.02 s
Time: CPU 0.01 s, Wall: 0.01 s
sage: time magma.eval('load "/home/was/foo";')
'Loading "/home/was/foo"'
CPU time: 0.00 s,  Wall time: 10.08 s
sage: 4*10^8/10^5 * 10.08
40320.0000000000
```

I tried the above several times -- it is just shockingly slow. 

Some other weirdness:

 * It takes magma 123 times as long to parse the hex integer literal version of `3<sup>(10</sup>6)` than the base-10 integer literal version of that number!!!  Also, using StringToInteger takes over 100 times longer than just using the load command on an assignment.  I'm trying a bunch of different variations... and the winner is:

```
21:08 < wstein> If you do "v := 0x<big hex string>;" in Magma it is insanely slow.
21:08 < wstein> If you do "v := <big decimal string>;" it is fast (like sage)
21:08 < wstein> If you do "v := StringToInteger(<big decimal string>)" it is insansely slow.
21:09 < wstein> If you do "v := StringToInteger(0x<big hex string>, 16)" it is very fast, just like sage.
21:09 < wstein> So the last option is good :)
```



---

Comment by was created at 2008-12-12 08:36:25

The first attached patch makes conversion to Magma for matrix_modn_dense twice as fast as before, and somewhat more memory efficient. 

BEFORE:

```
age:  w = random_matrix(GF(97),2000)
sage: time m = magma(w)
CPU times: user 3.00 s, sys: 0.46 s, total: 3.47 s
Wall time: 7.46 s
```


AFTER:

```
sage: w = random_matrix(GF(97),2000)
sage: time m = magma(w)
CPU times: user 1.08 s, sys: 0.19 s, total: 1.27 s
Wall time: 3.22 s
```


This does not apply to matrices over GF(2), which still require more special code to be faster. 

This patch also fixes a free that should be a sage_free, and speeds up the list method for matrices mod n.


---

Attachment

matrices modn for n odd.


---

Comment by malb created at 2008-12-12 14:45:03

`trac_4237_part1.patch` assumes that we always store the entries as positive integers. Is this a sensible assumption?


---

Comment by was created at 2008-12-12 18:26:45

> trac_4237_part1.patch assumes that we always store the entries as positive integers. 
> Is this a sensible assumption? 

Yes.  All entries are stored as numbers between 0 and p-1.  See, e.g., code like this in the __init__ method:

```
                if PY_TYPE_CHECK_EXACT(x, int):
                    tmp = (<long>x) % p
                    v[j] = tmp + (tmp<0)*p
```


William


---

Comment by was created at 2008-12-12 19:31:37

The second patch adds support for much faster conversions of matrices over GF(2) to Magma.  Now sage can convert your 10000x10000 GF(2) matrix in about 45 seconds, instead of the 149 seconds it used to take (so over 3 times faster).  The intermediate memory usage is also better on the Sage side.

BEFORE:

```
sage: w = random_matrix(GF(2),10000)
sage: time k = w._magma_init_(magma)
CPU times: user 49.64 s, sys: 2.20 s, total: 51.84 s
Wall time: 52.75 s
sage: time a = magma(k)
CPU times: user 1.94 s, sys: 2.69 s, total: 4.63 s
Wall time: 97.84 s
sage: 52 + 97
149
```


AFTER:

```
sage: w = random_matrix(GF(2),10000)
sage: time k = w._magma_init_(magma)
CPU times: user 1.22 s, sys: 0.63 s, total: 1.85 s
Wall time: 1.85 s
sage: time a = magma(k)
CPU times: user 1.70 s, sys: 2.30 s, total: 4.00 s
Wall time: 44.15 s
```


Now the time is totally dominated by the time Magma spends in the function StringToIntegerSequence.

I tried the 2*10^4 example.  With the new code, Sage does create a 5GB string in memory, then writes it to a 763MB file:

```
was`@`sage:~/.sage/temp/sage/22977/interface$ ls -lh
total 764M
-rw-r--r-- 1 was was 763M 2008-12-12 11:12 tmp22977
```

Then Sage frees all that memory.  Then Magma reads in the string to memory, which 
takes over 5GB again (not surprisingly):

```
23012 was       25   0 5772m 5.1g 2796 R  100  8.0   2:41.25 magma.exe.x86_6            
```

Converts that to a string over integers (which also takes a lot of RAM), then creates a mod-2 matrix. 

It would in theory be possible to do this via a series of chunks as you suggest, but support for that does not exist in the Magma/Sage interface (or any interface) at all, and would probably be particular hard to get right when Magma isn't even running locally (I think now one could have the magma run on a different machine and that 763MB file above would get copied via scp, maybe...)

If only Magma had any support WHATEVER for bit manipulation.  Then we could send the whole data over as a single integer or other format and extract it.  But Magma doesn't.  At present it seems that by far the fastest way to get a mod-2 matrix over to Magma is to do what I've implemented in patch 2, which is pretty bad memory-wise in the limit.  It does complete your 2*10^4 example on sage.math in 192 seconds, which is an improvement:

```
sage: A = random_matrix(GF(2),2*10^4,2*10^4)
sage: time B = magma(A)
CPU times: user 16.28 s, sys: 14.38 s, total: 30.65 s
Wall time: 192.45 s
```


Anyway, for something more memory efficient, what I just wrote could be the base case. Maybe you could try sending a big matrix over GF(2) to magma by breaking it into smaller matrices, sending each of those (with the new code I just wrote), then reassembling the result in Magma.  Can magma do things like stack matrices (like Sage's A.stack)?


---

Attachment

patch2 doesn't apply against my 3.2.1. Hunk:


```
--- matrix_mod2_dense.pyx
+++ matrix_mod2_dense.pyx
`@``@` -1136,7 +1136,7 `@``@`
         EXAMPLE:
             sage: A = random_matrix(GF(2),3,3)
             sage: A._magma_init_(magma)                             # optional - magma
-            '_sage_[...]![0,1,0,0,1,1,0,0,0]'
+            'Matrix(GF(2),3,3,StringToIntegerSequence("0 1 0 0 1 1 0 0 0"))'
             sage: A = random_matrix(GF(2),100,100)
             sage: B = random_matrix(GF(2),100,100)
             sage: magma(A*B) == magma(A) * magma(B)                 # optional - magma
```


Do I need 3.2.2.alphaX for this patch?


---

Comment by mabshoff created at 2008-12-15 16:52:24

I am seeing one doctest failure with this patch on sage.math:

```
sage -t -long "devel/sage/sage/matrix/matrix_modn_dense.pyx"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/matrix/matrix_modn_dense.pyx", line 276, in __main__.example_6
Failed example:
    -m###line 554:_sage_    >>> -m
Expected:
    [19 18 17]
    [16 15 14]
    [13 12 11]
Got:
    [ 0 18 17]
    [16 15 14]
    [13 12 11]
**********************************************************************
```

I haven't looked into the cause yet.

Cheers,

Michael


---

Comment by was created at 2008-12-17 01:56:29

A quick comment.  The *new* output you're getting is *right*.  The old output, which is in sage, is wrong.  Somebody (probably me) fixed a bug. The matrix is a matrix modulo 19, so its entries should be normalized between 0 and 18, inclusive. That 19 should be 0, as it is in the output you get now.


---

Comment by was created at 2008-12-17 01:58:20

The doctest that "fails" (by giving correct output) is *not* in the patch I submitted.  In my code I fixed some free's that should be sage_free, and implemented a correct specialized faster list method.  Probably one of those two fixed the bug.


---

Comment by was created at 2008-12-17 02:03:14

OK, I fixed the doctest, then fixed the __neg__ method which had a bug (and has ever since it was written).    This has nothing to do with the sage/magma interface, by the way.  The doctest used to be wrong because of that bug; the new list method I wrote fixed the bug in printing, but didn't fix the actual bug.  Now it's fixed.  The bug was in negation of a number modulo p and forgetting to normalize the result in the range 0 to p-1, inclusive.


---

Attachment


---

Comment by mabshoff created at 2008-12-17 14:50:29

Positive review for all three patches.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-17 15:12:40

Resolution: fixed


---

Comment by mabshoff created at 2008-12-17 15:12:40

Merged all three patches in Sage 3.2.2.rc1
