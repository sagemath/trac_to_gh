# Issue 2419: Gap interface and resultant destroy the Singular interface on some machines

Issue created by migration from https://trac.sagemath.org/ticket/2419

Original creator: SimonKing

Original creation time: 2008-03-07 08:10:10

Assignee: was

CC:  wdj was

Keywords: gap singular resultant

I consider the following bug critical, because it completely corrupts the Singular interface. However, it seems that the error only occurs on very few machines - so far, only one other person can reproduce the bug - see discussions at http://groups.google.com/group/sage-support/browse_thread/thread/5006f9a839723e27?hl=en

Creating a univariate polynomial ring R over the rationals, computing the resultant of two polynomials in that ring and using the gap interface for the Integers makes the singular interface fail on R (on some machines). To be precise:

```
sage: R.<x> = QQ[]
sage: f = x^3 + x + 1;  g = x^3 - x - 1
sage: r = f.resultant(g)
sage: gap(ZZ)
Integers
sage: singular(R).typeof()    # this should yield 'ring' !
print(sage8);
sage: singular(R).name()   # this is correct ...
'sage0'
sage: singular('sage0')   # ... hence, this should return a ring - but it doesn't
print(sage9);
sage: singular('sage0')
print(sage10);
sage: singular('sage0')
print(sage11);
```


Note that computing the resultant is important. If i replace it with, say, `singular(R)`, then the error does not occur. Also, if `gap(ZZ)` is done _before_ computing the resultant, the error does not occur.

David Joyner observed that on both machines showing that error, there is an rpm based Linux. However, i know a machine with the same Linux that does not show that error.
Again, see http://groups.google.com/group/sage-support/browse_thread/thread/5006f9a839723e27?hl=en



---

Comment by SimonKing created at 2008-03-08 22:41:14

Replying to [ticket:2419 SimonKing]:
> I consider the following bug critical, because it completely corrupts the Singular interface. However, it seems that the error only occurs on very few machines ...

Meanwhile, i found a very similar error that even occurs on sage.math with sage 2.10.2:

```
sage: R.<x> = QQ[] 
sage: f = x^3 + x + 1;  g = x^3 - x - 1 
sage:  r = f.resultant(g) 
sage: gap(ZZ) 
Integers 
sage: singular(R) 

sage: singular(R) 
//   characteristic : 0 
//   number of vars : 1 
//        block   1 : ordering lp 
//                  : names    x 
//        block   2 : ordering C 
sage: singular(R).typeof() 

sage: singular(R).typeof() 

sage: singular(R).name() 
'sage0' 
sage: singular('sage0') 

sage: singular('sage0') 

```

So, after computing resultant and calling gap, the first singular(R) has empty output, but the second (and following) display a ring. Calling typeof on that ring repeatedly has empty output. And although `sage0` is the name of singular(R), calling singular('sage0') has empty output.

I hope this is sufficiently reproducible for tracking down the problem.


---

Comment by SimonKing created at 2008-03-12 08:58:54

Replying to [comment:2 SimonKing]:

I was just trying the above example that used to fail on sage.math with sage-2.10.2

It works on sage.math with sage-2.10.3!! So, many thanks to the person who did (accidentally?) fix the bug.

Now i am looking forward to test it on my machine, but this will take a while.


---

Comment by SimonKing created at 2008-03-12 12:50:27

Replying to [comment:3 SimonKing]:
>
> Now i am looking forward to test it on my machine, but this will take a while.

Although the problem vanished on sage.math, it is still present on my machine. Is there anyone out there who can reproduce it?


---

Comment by wdj created at 2008-03-12 13:38:15

This is what I get on an amd64 ubuntu 7.10:

wdj`@`wooster:~/wdj/sagefiles/sage-2.10.3$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.3, Release Date: 2008-03-11                      |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: R.<x> = QQ[]
sage: sage: f = x^3 + x + 1;  g = x^3 - x - 1
sage: sage: r = f.resultant(g)
sage: sage: gap(ZZ)
Integers
sage: Integers
<function IntegerModRing at 0xf95ed8>
sage: sage: singular(R).typeof()
print(sage8);
sage: singular(R).name()
'sage0'
sage: singular('sage0')
print(sage9);
sage: singular('sage0')
print(sage10);
sage: singular('sage0')
print(sage11);
sage: singular(R)

//   number of vars : 1
//        block   1 : ordering lp
//                  : names    x
//        block   2 : ordering C
sage: singular(R).typeof()
print(sage12);
sage: singular(R).name()
'sage0'
sage: singular(R).name()
'sage0'
sage: singular('sage0')
print(sage13);
sage:


---

Comment by wdj created at 2008-03-12 13:38:57

Sorry, forgot the wikiformatting, so reposted:


```
wdj@wooster:~/wdj/sagefiles/sage-2.10.3$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.3, Release Date: 2008-03-11                      |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: R.<x> = QQ[]
sage: sage: f = x^3 + x + 1;  g = x^3 - x - 1
sage: sage: r = f.resultant(g)
sage: sage: gap(ZZ)
Integers
sage: Integers
<function IntegerModRing at 0xf95ed8>
sage: sage: singular(R).typeof()
print(sage8);
sage: singular(R).name()
'sage0'
sage: singular('sage0')
print(sage9);
sage: singular('sage0')
print(sage10);
sage: singular('sage0')
print(sage11);
sage: singular(R)

//   number of vars : 1
//        block   1 : ordering lp
//                  : names    x
//        block   2 : ordering C
sage: singular(R).typeof()
print(sage12);
sage: singular(R).name()
'sage0'
sage: singular(R).name()
'sage0'
sage: singular('sage0')
print(sage13);
sage:                              
```



---

Comment by SimonKing created at 2008-03-12 13:49:21

Replying to [comment:6 wdj]:

Exactly the same happens on my machine, with AMD Athlon 64 and openSUSE 10.2.

Something different happens on sage.math, but it is still nonsense:

```
sage: R.<x> = QQ[]
sage: f = x^3 + x + 1;  g = x^3 - x - 1
sage: r = f.resultant(g)
sage: gap(ZZ)
Integers
sage: singular(R).typeof()

sage: singular(R).name()
'sage0'
sage: singular('sage0')

sage: singular('sage0')

sage: singular(R)

//   characteristic : 0
//   number of vars : 1
//        block   1 : ordering lp
//                  : names    x
//        block   2 : ordering C
```


Hence, singular('sage0') and singular(R).typeof() have no visible output.


---

Comment by was created at 2008-03-12 14:50:11


```
perhaps you noticed that i had found a version of the weird bug
"resultant+gap+singular=nonsense" even on sage.math, as i reported in
ticket #2419.

That was for sage-2.10.2; but the problem has vanished for sage-2.10.3 --
at least on sage.math, i am curious what will happen on my machine. [[it survives there]]

Do you have any idea how the problem was fixed (or whom i should ask)?
```



---

Comment by SimonKing created at 2008-03-12 15:15:57

Replying to [comment:8 was]:
> perhaps you noticed that i had found a version of the weird bug
> "resultant+gap+singular=nonsense" even on sage.math, as i reported in
> ticket #2419.
> 
> That was for sage-2.10.2; but the problem has vanished for sage-2.10.3 --
> at least on sage.math, i am curious what will happen on my machine. [This is the Trac macro *it survives there* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#it survives there-macro)
> 
> Do you have any idea how the problem was fixed (or whom i should ask)?

That was my message off trac to William. Apparently i was too optimistic: What i posted above _did_ (and still does) happen on sage.math _after_ writing my message to William. 

Hopefully it is reproducible for you.


---

Attachment


---

Comment by was created at 2008-03-12 15:33:16

Changing priority from critical to blocker.


---

Comment by wdj created at 2008-03-12 16:19:58

The patch sage-2419-singular_synch.patch did not apply cleanly against my version
of 2.10.3 using the command 
hg_doc.apply("/home/wdj/wdj/sagefiles/sage-2419-singular_synch.patch")


---

Comment by was created at 2008-03-12 16:28:57

> The patch sage-2419-singular_synch.patch did not apply cleanly 
> against my version of 2.10.3 using the command
> hg_doc.apply("/home/wdj/wdj/sagefiles/sage-2419-singular_synch.patch")

Agh!  hg_doc??  Why are you using hg_doc?


---

Comment by SimonKing created at 2008-03-12 18:03:17

Hi William!

The patch applies cleanly, and it solves the problem on my machine!

So, many thanks for the great job!

On sage-support you mentioned that the patch would slow down the interface considerably. Is there a way to know when synchronization is really needed? Perhaps, if the synchronization would not be done before _each_ command, it were faster.


---

Comment by was created at 2008-03-12 18:08:38

> On sage-support you mentioned that the patch would slow down the 
> interface considerably. Is there a way to know when synchronization 

30% isn't so bad, and it's only a LATENCY issue really, i.e., if you
do 

```
  singular('something that takes some actual time on the singular side')
```

then it makes almost no difference.  

> is really needed? Perhaps, if the synchronization would not be done 
> before each command, it were faster.

But then it wouldn't always work, which defeats the whole purpose, which
is "rock solid robustness".

 -- William


---

Comment by was created at 2008-03-12 18:11:51

Just to be clear: that "30%" refers only to the extra time if you do almost nothing in singular.eval('...').  If you actually do something that takes time, then the overhead of synchronizing should be way less.  Also, the 30% is for maxima.  I didn't benchmark the singular overhead yet.


---

Comment by SimonKing created at 2008-03-12 18:18:37

Replying to [comment:16 was]:
> Just to be clear: that "30%" refers only to the extra time if you do almost nothing in singular.eval('...').  If you actually do something that takes time, then the overhead of synchronizing should be way less.  Also, the 30% is for maxima.  I didn't benchmark the singular overhead yet.  

Thank you for the explanation! 

Since the problem vanishes with the patch (at least for me), I give a positive review, although you may know better than i if further and more extensive tests are needed.


---

Comment by SimonKing created at 2008-03-12 18:21:07

Replying to [comment:15 was]:
> > is really needed? Perhaps, if the synchronization would not be done 
> > before each command, it were faster.
> 
> But then it wouldn't always work, which defeats the whole purpose, which
> is "rock solid robustness".

What i meant was: Is there a _fast_ test that tells us whether or not the interface needs synchronization? If the test is faster than actually doing the synchronization, it would be faster and still rock solid.


---

Comment by mabshoff created at 2008-03-12 19:45:25

Merged in Sage 2.10.4.alpha0


---

Comment by mabshoff created at 2008-03-12 19:45:25

Resolution: fixed


---

Comment by was created at 2008-03-12 19:47:46

Changing status from closed to reopened.


---

Comment by was created at 2008-03-12 19:47:46

Wow, this was a 15-minute test patch, not a finished solution.
It should be have been rejected based on lack of doctests if nothing
else.  Anyways, reopened.


---

Comment by was created at 2008-03-12 19:47:46

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-03-12 19:53:19

ok, for the record: I reverted the patch in my tree, i.e. once doctests are added and the patch has been given a positive review it needs to be reapplied.

Cheers,

Michael


---

Comment by SimonKing created at 2008-03-12 19:58:14

Replying to [comment:21 mabshoff]:
> ok, for the record: I reverted the patch in my tree, i.e. once doctests are added and the patch has been given a positive review it needs to be reapplied.

Sorry that i confused you by using the notion "positive review" in my post. What i meant was "positive feedback, since the original problem was solved", where "positive feedback" means that it appears to go in a good direction.


---

Comment by wdj created at 2008-03-12 22:51:11

Oops. The hg_doc was stupid. With hg_sage.apply, it applies cleanly and fixes the problem.
Passes sage -testall.


---

Comment by SimonKing created at 2008-03-13 09:55:18

Hi!

Since my premature hooray was causing some trouble, i try to excuse with a few doc tests: See the patch that i am about to attach, which should be applied after William's patch. Also i have a couple of questions/remarks.

Questions/Remarks:
 * Example for _crash_msg: I don't know if that example is platform dependent, since i use os.kill(singular.pid(),9) -- probably you know a more elegant way to kill singular on purpose. Also, it fails on `sage -t` because the error message "Singular crashed -- automatically restarting." is considered as output. 
   - I'd like to show the error message to the user, but i don't want that `sage -t` expects it as output. How can i do so?
 * I didn't find out what _expect_expr is supposed to do. Similarly to what is done in _synchronize, I tried without success:

```
sage: singular._sendstr('2+3;')
sage: singular._expect_expr(timeout=0.5)
}}} 
 * Also i don't find a reasonable example for _interrupt.


---

Comment by SimonKing created at 2008-03-13 09:56:18

Adding some doctests to singular synchronization. To be applied after William's patch


---

Attachment

I found that bug since doc tests for my patch from #2420 failed. Thus i expected that William's synchronization patch would fix #2420 as well, but it didn't -- see my comments there.

I'll try to boil down the new problem, but i suspect that a synchronization will be needed for the gap interface as well.


---

Comment by SimonKing created at 2008-03-20 12:46:38

Hi!

So far, there was no feedback on my doc-tests, and no explanation about what _expect_expr is supposed to do. 

Concerning testing: I used Williams patch for extensive computations in a program that makes (small) use of the gap interface and _heavy_ use of the singular interface. It didn't crash, which indicates that it may work. 

I am not sure: Is this enough for giving a "positive review pending; more doctests needed"?


---

Comment by was created at 2008-03-20 23:44:06

> I am not sure: Is this enough for giving a "positive review 
> pending; more doctests needed"? 

Yes.  Given how the patch is written if it works in practice it
is definitely worth including in Sage.  

I can't work on this now unfortunately due to lack of time.


---

Comment by SimonKing created at 2008-04-08 07:49:36

Sorry, i have not been at work for a while. According to William's remark, i give a "positive review pending; more doctests needed". However, i could only provide more doctests if someone tells me about the use of _expect_expr. Also, i don't know how to deal with printed output in a doctest -- this concerns my example for _crash_msg.


---

Comment by mabshoff created at 2008-04-18 20:32:20

This *really* ought to be looked at. It seems ready.

Cheers,

Michael


---

Attachment

apply *all three* patches in order.


---

Comment by was created at 2008-04-20 19:52:44

It said "[positive review pending; more doctests needed]", so I wrote more doctests and did the
refactoring suggested in my comments.   So now -- [with patch; needs review]


---

Comment by mhansen created at 2008-04-20 20:01:33

Applies and passes tests against 3.0alpha5.  Looks good to me.


---

Comment by mabshoff created at 2008-04-21 00:41:55

Merged all three patches in Sage 3.0.rc1


---

Comment by mabshoff created at 2008-04-21 00:41:55

Resolution: fixed


---

Comment by mabshoff created at 2008-04-21 01:17:23

Mmh, after merging this patch I see:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.rc1$ ./sage -t  devel/sage/sage/interfaces/expect.py
sage -t  devel/sage/sage/interfaces/expect.py               **********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/tmp/expect.py", line 835:
    sage: singular('2+3')
Expected:
    Singular crashed -- automatically restarting.
    5
Got:
    5
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/tmp/expect.py", line 860:
    sage: R.<x> = QQ[]; f = x^3 + x + 1;  g = x^3 - x - 1; r = f.resultant(g); gap(ZZ); singular(R)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_17[2]>", line 1, in <module>
        R = QQ['x']; (x,) = R._first_ngens(Integer(1)); f = x**Integer(3) + x + Integer(1);  g = x**Integer(3) - x - Integer(1); r = f.resultant(g); gap(ZZ); singular(R)###line 860:
    sage: R.<x> = QQ[]; f = x^3 + x + 1;  g = x^3 - x - 1; r = f.resultant(g); gap(ZZ); singular(R)
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 288, in resultant
        return resultant_func(self, other, variable)
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 438, in resultant_func
        rt = self._singular_().resultant(other._singular_(), variable._singular_())
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 282, in _singular_
        return _singular_func(self, singular, have_ring, force)
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 334, in _singular_func
        self.parent()._singular_(singular,force=force).set_ring() #this is expensive
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 174, in _singular_
        return self._singular_init_(singular, force)
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 217, in _singular_init_
        self.__singular = singular.ring(self.characteristic(), _vars, order=order, check=False)
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 681, in ring
        R = self('%s,%s,%s'%(char, vars, order), 'ring')
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 502, in __call__
        return SingularElement(self, type, x, False)
      File "/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 825, in __init__
        raise TypeError, x
    TypeError: End Of File (EOF) in read_nonblocking(). Braindead platform.
    <pexpect.spawn instance at 0x2abf554371b8>
    version: 2.0 ($Revision: 1.151 $)
    command: /scratch/mabshoff/release-cycle/sage-3.0.rc1/local/bin/Singular
    args: ['/scratch/mabshoff/release-cycle/sage-3.0.rc1/local/bin/Singular', '-t', '--ticks-per-sec', '1000']
    patterns:
        >
    buffer (last 100 chars):
    before (last 100 chars): ring sage4=0,x,lp;

    after: <class 'pexpect.EOF'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 1
    pid: 19207
    child_fd: 3
    timeout: None
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 1000
    searchwindowsize: None
    delaybeforesend: 0
    Singular crashed executing ring sage4=0,x,lp;
**********************************************************************
2 items had failures:
   1 of   7 in __main__.example_16
   1 of   3 in __main__.example_17
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.rc1/tmp/.doctest_expect.py
         [7.5 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/interfaces/expect.py
Total time for all tests: 7.5 seconds
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.rc1$   
```


Thoughts?

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-04-21 02:16:25

Merged sage-2419-followup.patch in Sage 3.0.rc1
