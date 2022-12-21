# Issue 5980: In sage-3.4.2.final on 32 bits there is a failure in prime_pi()

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2009-05-04 16:45:28

Assignee: mabshoff


```

On May 4, 9:07 am, Jaap Spies <j.sp...`@`hccnet.nl> wrote:
> > mabshoff wrote:
>> > > Hello folks,

<SNIP>

>> > > Please build, test and report issues as usual.
> >
> > On Fedora 9, 32 bit upgraded from alpha0 -> rc0-> sage-3.4.2
> > and on Fedora 10, 32 bit upgraded from rc0 I get tons
> > of failures with prime_pi, e.g.:
> >
> > sage -t  "devel/sage/sage/functions/prime_pi.pyx"
> > **********************************************************************
> > File "/home/jaap/Download/sage-3.4.2.rc0/devel/sage/sage/functions/prime_pi.pyx", line 74:
> >      sage: prime_pi(7)
> > Exception raised:
> >      Traceback (most recent call last):
> >        File "/home/jaap/Download/sage-3.4.2.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
> >          self.run_one_example(test, example, filename, compileflags)
> >        File "/home/jaap/Download/sage-3.4.2.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
> >          OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
> >        File "/home/jaap/Download/sage-3.4.2.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
> >          compileflags, 1) in test.globs
> >        File "<doctest __main__.example_3[2]>", line 1, in <module>
> >          prime_pi(Integer(7))###line 74:
> >      sage: prime_pi(7)
> >        File "prime_pi.pyx", line 175, in sage.functions.prime_pi.PrimePi.__call__ (sage/functions/prime_pi.c:1101)
> >      NotImplementedError: computation of prime_pi() greater 2**40 not implemented
> > 
Arrg, this is cause by Integer(2**40) on 32 bit systems being "0" in
Cython. I didn't use any long representation of 2^40 to avoid running
into 32 vs. 64 bit issues. Oh well, please open a ticket, I guess
there will be another "final" 3.4.2 tarball :(

> > Jaap

Cheers,

Michael
```



---

Comment by mabshoff created at 2009-05-04 16:49:01

Resolution: duplicate


---

Comment by mabshoff created at 2009-05-04 16:49:01

Ahh, I looked at the timeline to make sure there wasn't a ticket already, but Jaap did open this more or less at the same time. And he beat me to it, but since I attached a workaround patch to #5981 I am closing this one as a dupe ;)

Cheers,

Michael
