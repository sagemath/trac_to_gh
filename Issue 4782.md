# Issue 4782: construction of some relative quadratic extensions is SERIOUSLY FRICKIN's FOO-bar'd

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-13 03:48:49

Assignee: was

Try this carefully with your finger on kill -9:

```
sage: NumberField(x^2 + 79*x - 60, 'a').extension(x^2 - 69*x + 38,'b')
```


On sage.math top shows pretty quickly over 6.9GB memory usage!

```
15392 was       25   0 8219m 6.9g  21m R  100 10.9   0:53.76 sage-ipython                                                    
```


The discriminants aren't very big:

```
sage: R.<x> = QQ[]
sage: disc(x^2 + 79*x-60)
6481
sage: disc(x^2 - 69*x + 38)
4609
```


Same behavior with Proof false:


```
sage: proof.all(False)
sage: NumberField(x^2 + 79*x - 60, 'a').extension(x^2 - 69*x + 38,'b')
...hell....
```


Giving both polys at once (which maybe use polcompositum) works:

```
sage: NumberField([x^2 + 79*x-60, x^2 - 69*x + 38], 'a')

  ***   Warning: insufficient precision for fundamental units, not given.
Number Field in a0 with defining polynomial x^2 + 79*x - 60 over its base field
```


Basically there is something very wrong with how we make relative fields... probably because of something very very wrong in the core of pari itself (and it's relative number fields). 


---

Comment by ncalexan created at 2008-12-17 15:32:15

Verify this is a PARI bug and submit it.  I've been amazed at how fast the PARI group addresses bugs!  I haven't seen this particular one, BTW.


---

Comment by was created at 2009-01-22 00:50:11

I just tried this on sage.math with sage-3.3.alpha0:

```
  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+ 
5160 wstein    20   0 61.7g  43g  21m R  102 34.4   2:48.35 sage-ipython
```


Oh my frickin' god?!  That's nuts.


---

Comment by ncalexan created at 2009-01-22 18:34:56

This is a pari bug, fixed in svn already:


```
mero:pari-svn ncalexan$ ./gp
                                          GP/PARI CALCULATOR Version 2.4.3 (development svn-11539)
                                              i386 running darwin (ix86 kernel) 32-bit version
                                          compiled: Jan 22 2009, gcc-4.0.1 (Apple Inc. build 5484)
                                             (readline not compiled in, extended help enabled)

                                                   Copyright (C) 2000-2008 The PARI Group

PARI/GP is free software, covered by the GNU General Public License, and comes WITHOUT ANY WARRANTY WHATSOEVER.

Type ? for help, \q to quit.
Type ?12 for how to get moral (and possibly technical) support.

parisize = 4000000, primelimit = 500000
? nffactor(nfinit(y^2 + 79*y - 60), x^2 - 69*x + 38)
%1 = 
[x^2 - 69*x + 38 1]
```



---

Comment by ncalexan created at 2009-01-22 18:40:41

And here is gp svn running on sage.math:


```
/scratch/nca/pari-svn $ ./gp
            GP/PARI CALCULATOR Version 2.4.3 (development svn-11539)
               amd64 running linux (x86-64 kernel) 64-bit version
            compiled: Jan 22 2009, gcc-4.2.4 (Ubuntu 4.2.4-1ubuntu3)
                 (readline v5.2 enabled, extended help enabled)

                     Copyright (C) 2000-2008 The PARI Group

PARI/GP is free software, covered by the GNU General Public License, and comes
WITHOUT ANY WARRANTY WHATSOEVER.

Type ? for help, \q to quit.
Type ?12 for how to get moral (and possibly technical) support.

parisize = 8000000, primelimit = 500000

? nffactor(nfinit(y^2 + 79*y - 60), x^2 - 69*x + 38)
%1 =
[x^2 - 69*x + 38 1]
```



---

Comment by ncalexan created at 2009-01-22 19:45:14

After discussion at SD12, mabs, craigcitro, and ncalexan are going to try to update pari to unstable/trunk.


---

Comment by was created at 2009-02-20 05:19:51

I just checked and the stated problem (for this ticket) is gone in 3.3.rc2 some I'm closing this.  (I tested on both sage.math and OS X)


```
sage: NumberField(x^2 + 79*x - 60, 'a').extension(x^2 - 69*x + 38,'b')
Number Field in b with defining polynomial x^2 - 69*x + 38 over its base field
```



---

Comment by was created at 2009-02-20 05:19:51

Resolution: fixed


---

Comment by ncalexan created at 2009-02-20 05:23:26

The problem is *not* gone, it's just hidden by #5231.  Creation is lazy now: it doesn't actually call pari, which will still fail.  This will be fixed when we upgrade to pari-svn.  I suggest this ticket be re-opened.


---

Comment by was created at 2009-02-20 05:31:58

Nick -- post an example that illustrates things not working.  Because I can't find one. 


```
sage: K = NumberField(x^2 + 79*x - 60, 'a').extension(x^2 - 69*x + 38,'b')
sage: K._pari[try every possible function even class groups]
<works fine>
```



---

Comment by mabshoff created at 2009-02-20 07:03:47

I just ran into Sage eating *122 GB* in the random ring test:

```
sage -t -long devel/sage/sage/rings/tests.py
```

Specifically

```
18203 mabshoff  25  5  122g 2.0g  23m R  100  1.6  4:00.82 /scratch/mabshoff/sage-3.3.rc3/local/bin/python /
```

So this is a problem, hence I will reopen it :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 07:03:47

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-02-20 07:03:47

Resolution changed from fixed to 


---

Comment by mabshoff created at 2009-02-20 07:09:20

Ok, I also just hit this, which might be completely unrelated:

```
sage -t -long "devel/sage/sage/rings/tests.py"              
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/rings/tests.py", line 251:
    sage: sage.rings.tests.test_random_arith(trials=1000)   # long time (5 seconds?)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.rc3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.rc3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.rc3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_12[3]>", line 1, in <module>
        sage.rings.tests.test_random_arith(trials=Integer(1000))   # long time (5 seconds?)###line 251:
    sage: sage.rings.tests.test_random_arith(trials=1000)   # long time (5 seconds?)
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/rings/tests.py", line 255, in test_random_arith
        for x in random_rings(level):
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/rings/tests.py", line 209, in random_rings
        yield random.choice(v)[0]()
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/rings/tests.py", line 131, in relative_number_field
        K = K.extension(f,var)
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 2616, in extension
        return NumberField_relative(self, poly, str(name), check=check, embedding=embedding)
      File "/scratch/mabshoff/sage-3.3.rc3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_rel.py", line 276, in __init__
        raise ValueError, "defining polynomial (%s) must be irreducible"%polynomial
    ValueError: defining polynomial (x^2 + 3*x - 20) must be irreducible
**********************************************************************
```

But the ring random test seems to flush out issues :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 08:29:50

Remember to turn on relative number field in the ring tester once this spkg has made it - see #4779.

Cheers,

Michael


---

Comment by davidloeffler created at 2009-07-21 08:16:36

Changing component from number theory to number fields.


---

Comment by jdemeyer created at 2010-10-10 21:26:38

Can we close this ticket in the light of #9343?


---

Comment by jdemeyer created at 2010-10-10 21:26:38

Changing status from new to needs_review.


---

Comment by lftabera created at 2010-11-23 22:36:56

I cannot reproduce the problem with sage 4.6 on debian linux 32 bits. I just get the relative field and looks ok.

Does anyone still experience issues?


---

Comment by robertwb created at 2010-12-04 19:40:27

Resolution: worksforme
