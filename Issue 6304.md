# Issue 6304: intermittent crash in bernmm (4.0.2.rc0)

Issue created by migration from https://trac.sagemath.org/ticket/6304

Original creator: dmharvey

Original creation time: 2009-06-15 19:04:21

Assignee: tbd


```
bsd$ uname -a
Darwin bsd.local 9.7.0 Darwin Kernel Version 9.7.0: Tue Mar 31 22:52:17 PDT 2009; root:xnu-1228.12.14~1/RELEASE_I386 i386

~/sage-4.0.2.rc0
bsd$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: w = bernoulli(100000, algorithm="bernmm", num_threads=8)
sage: w = bernoulli(100000, algorithm="bernmm", num_threads=8)
/Users/dmharvey/sage-4.0.2.rc0/local/bin/sage-sage: line 198: 62412 Illegal instruction     sage-ipython "$@" -i
| Sage Version 4.0.2.rc0, Release Date: 2009-06-15                   |
| Type notebook() for the GUI, and license() for information.        |
~/sage-4.0.2.rc0
bsd$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: w = bernoulli(100000, algorithm="bernmm", num_threads=8)
sage: w = bernoulli(100000, algorithm="bernmm", num_threads=8)
sage: w = bernoulli(100000, algorithm="bernmm", num_threads=8)
sage: w = bernoulli(100000, algorithm="bernmm", num_threads=8)
sage: w = bernoulli(100000, algorithm="bernmm", num_threads=8)
sage: w = bernoulli(100000, algorithm="bernmm", num_threads=8)
/Users/dmharvey/sage-4.0.2.rc0/local/bin/sage-sage: line 198: 62473 Illegal instruction     sage-ipython "$@" -i
```

| Sage Version 4.0.2.rc0, Release Date: 2009-06-15                   |
| Type notebook() for the GUI, and license() for information.        |


---

Comment by dmharvey created at 2009-06-15 20:46:59

I can reproduce this from outside Sage, on the same machine, building bernmm directly against GMP and NTL, using only two threads.

gdb says the crash happens somewhere inside GMP, during one of the large XGCD operations.


---

Comment by dmharvey created at 2009-06-15 21:46:51

I've been trying to debug this for almost three hours, and I have absolutely no idea what is going wrong.

I can't reproduce the error on any other systems. Only seems to happen on OSX 10.5.


---

Comment by was created at 2009-06-19 13:23:01

> I can't reproduce the error on any other systems. Only seems to happen on OSX 10.5. 

I would be OK with the following:

  * if somebody tries to use the bernmm algorithm on OS X 10.5, then it gives a warning and falls back to the single threaded PARI version.

  * on OS X 10.5 the default algorithm never uses bernmm.

 -- William


---

Comment by was created at 2009-06-19 13:23:01

Changing component from algebra to combinatorics.


---

Comment by was created at 2009-06-19 13:23:01

Changing assignee from tbd to mhansen.


---

Comment by dmharvey created at 2009-06-19 13:37:46

William,

I got the feeling while trying to debug that it could be a compiler issue. The gcc version is 4.0.1 on that box. I've read online that newer versions of XCode for leopard also include gcc 4.2.1, but it's not switched on by default. I couldn't find it on that machine. Would it be possible to try installing apple's newer xcode/gcc to see if that helps?

david


---

Comment by was created at 2009-06-20 10:56:02

> Would it be possible to try installing apple's newer xcode/gcc to see if that helps? 

That's a very good idea.  What happens on your laptop (I assume you can't replicate the issue). 

Anyway, I can't do anything admin-wise on that box until August when I back in Seattle.


---

Comment by dmharvey created at 2009-06-20 20:41:01

Hmmm, no. I can make it fail on my OS 10.4.11 laptop too.


---

Comment by dmharvey created at 2009-06-22 15:55:42

I tried on my wife's laptop which is OS 10.5.7. I switched over to apple's gcc 4.2.1, but I cannot build sage 4.0.2, I get


```
cc1: error: unrecognized command line option "-Wno-long-double"
```


while building python-2.5.4.p1.


---

Comment by was created at 2009-08-15 22:24:30


```

On Sat, Aug 15, 2009 at 9:52 AM, William Stein<wstein@gmail.com> wrote:
> On Sat, Aug 15, 2009 at 9:42 AM, David Harvey<dmharvey@cims.nyu.edu> wrote:
>>
>> On Aug 15, 2009, at 12:40 PM, William Stein wrote:
>>
>>> On Sat, Aug 15, 2009 at 9:33 AM, David Harvey<dmharvey@cims.nyu.edu>
>>> wrote:
>>>>
>>>> On Aug 15, 2009, at 12:28 PM, William Stein wrote:
>>>>
>>>>> gcc version 4.0.1 (Apple Inc. build 5493)
>>>>
>>>> but still gcc 4.0.1?
>>>>
>>>> Try "man gcc_select"?
>>>
>>> Yes.  So just for clarification, the bug happens with all builds of
>>> GCC 4.0.1, but can be got around by switching to GCC 4.2.x?
>>
>> I don't know. My guess is that there is a bug in the threading support in
>> gcc 4.0.1, but of course it could also be a bug in my code. I spent several
>> hours debugging one day and found nothing. From memory I then tried to build
>> sage using gcc 4.2.x (?) on 10.5 but was not successful, and then I got
>> distracted by other things....
>>
>
> OK, thanks for the clarification.  You do in fact clearly explain this
> at http://trac.sagemath.org/sage_trac/ticket/6304/.  At least it
> crashes instead of giving wrong answers.
>
> There is no gcc_select command with that name on OS X.  I switched to
> gcc-4.2.1 just by changing two symlinks in /usr/bin/.   (For gcc and
> g++.)   I'll try building Sage on that box with that compiler now.
>

I completely built with the latest gcc-4.2.1, and bernmm test still fails.   I've updated the ticket accordingly.  I think the right thig to do at this point is to make using bernmm off by default for OS X 10.5 intel, and put a remark in the docstring that it will sometimes crash sage with an illegal instruction error, and that using the latest XCode with either GCC 4.0.1 or 4.2.1 does not fix the problem.    Robust multithreaded programming is hard. 
```



---

Comment by dmharvey created at 2009-08-16 13:37:31

I am trying to debug again on my laptop (core 2 duo, 2 cores, mac os 10.4.11). If I build bernmm standalone using GMP 4.3.1 + NTL 5.4.2 with default configure options, I can get the test suite to fail quite regularly (bus error) with `./bernmm-test --rational 40000 8`. Interestingly, if I configure GMP 4.3.1 with recommended "maximum debuggability options" (`--disable-shared --enable-assert --enable-alloca=debug --build=none CFLAGS="-m64 -g"`), I can't get it to crash any more.


---

Comment by dmharvey created at 2009-08-16 13:53:37

Now I tried compiling GMP with `--disable-shared --enable-assert --enable-alloca=debug CFLAGS="-g -O2 -pedantic -m64 -mtune=k8"` (the latter is the default CFLAGS plus "-g"), and there seem to be no crashes. This suggests the problem is not in the GMP assembly code.


---

Comment by dmharvey created at 2009-08-16 14:03:03

Tried again, this time removing `--disable-shared`. Still doesn't crash.


---

Comment by dmharvey created at 2009-08-16 15:12:18

Now making progress.... on sage.math, if I run bernmm-test under valgrind, even for n = 4 and one thread, I get all kind of invalid read errors.


---

Comment by dmharvey created at 2009-08-16 16:36:15

Actually no progress at all. I discovered after another hour that valgrind even reports invalid read errors for a simple program that computes "2+2" using GMP. I have no idea what to make of this.


---

Comment by dmharvey created at 2009-08-16 16:58:52

Moving back to my laptop, if I compile GMP without the `--enable-alloca=debug` option, the crashes reappear.


---

Comment by dmharvey created at 2009-08-16 19:22:57

Finally got somewhere.

It appears to be a stack overflow issue. It occurs inside GMP's xgcd function. The default stack size for new threads is 8 MB on sage.math but apparently only 512 KB on OSX. If I increase the thread stack size inside bernmm, the crashes stop happening.

I wrote a test program (below) that calls `mpz_invert` for a given input size using a given thread stack size. (The `mpz_invert` call is what seems to be causing the problems in bernmm.) I found that for stack size = 512 KB, GMP doesn't have any problems, but if I bump it down to only 448 KB, it starts crashing for inputs of 2800 limbs and above. This is around about the largest size that is used in bernmm for computing B(40000), which is the value of k where problems seem to start occurring. So if bernmm is only using a few 10's of KB of stack, it could push GMP over the limit.

I haven't tried any of this with MPIR, but given that it uses a similar quasi-linear XGCD algorithm, it wouldn't surprise me that the cause is the same.

This is not so easy to address. A band-aid solution is to make bernmm use a bigger stack. The real issue is whether it is reasonable for GMP to require so much stack space for the XGCD operation (or conversely whether the default stack size on OSX is too small). I will ask on the GMP mailing list about this.


```
#include <limits.h>
#include <stdio.h>
#include <gmp.h>
#include <pthread.h>


void*
worker (void* arg)
{
  size_t n = * (size_t*) arg;

  mpz_t a, b;
  mpz_init (a);
  mpz_init (b);

  /* try to invert a random number modulo B^n + 1 */
  mpz_random (a, n);
  mpz_set_ui (b, 1);
  mpz_mul_2exp (b, b, n * GMP_NUMB_BITS);
  mpz_add_ui (b, b, 1);
  mpz_invert (a, a, b);

  mpz_clear (b);
  mpz_clear (a);
}

int
main (int argc, char* argv[])
{
  if (argc < 3)
    {
      printf ("syntax: test <n> <stacksize>\n");
      return 0;
    }

  size_t n = atol (argv[1]);
  size_t old_stacksize;
  size_t new_stacksize = atol (argv[2]);

  pthread_attr_t attr;
  pthread_attr_init (&attr);

  pthread_attr_getstacksize (&attr, &old_stacksize);
  printf ("old stacksize = %ld\n", old_stacksize);

  int retval = pthread_attr_setstacksize (&attr, new_stacksize);
  if (retval != 0)
    {
      printf ("PTHREAD_STACK_MIN = %ld\n", PTHREAD_STACK_MIN);
      printf ("pthread_attr_setstacksize call failed with size = %ld\n",
              new_stacksize);
      return 0;
    }

  pthread_t thread;
  pthread_create (&thread, &attr, worker, &n);
  pthread_join (thread, NULL);

  pthread_attr_destroy (&attr);

  return 0;
}
```



---

Attachment


---

Comment by dmharvey created at 2009-08-20 15:00:10

I have released bernmm 1.1 which addresses this issue, by providing a THREAD_STACK_SIZE compile-time option. See attached patch.

This doesn't address the underlying issue (that in my opinion, GMP/MPIR uses too much stack space by default for XGCD), but it will have to do for the moment.


---

Comment by mhansen created at 2009-10-03 06:13:23

This changed fixed things for me.  I'm going to go ahead and give it a positive review.


---

Comment by mhansen created at 2009-10-15 07:13:44

Resolution: fixed
