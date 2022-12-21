# Issue 8177: element_wrapper.py: Sage 4.3.2.alpha1 segfault on Mac OS X 10.6.2

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-02-03 18:45:01

Assignee: tbd

CC:  nthiery mvngu hivert

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/7754a347b837fad6) and also [reported here](http://groups.google.com/group/sage-devel/browse_thread/thread/7c920d26ddad3345):

```
> built fine on mac 10.6.2 but one failure for sage -testall :

> The following tests failed:

>        sage -t  "devel/sage/sage/structure/element_wrapper.py" # Segfault

I get the same result on bsd.math (Mac OS X 10.6.2). Doing a verbose
long doctest, I get:

Trying:
    Integer(1) < l11###line 213:_sage_    >>> 1 < l11
Expecting:
    False

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------ 
```



---

Comment by was created at 2010-02-04 12:22:02

Here is a complete self-contained session that illustrates the problem:

```
wstein`@`bsd:~/build/sage-4.3.2.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: class MyElement(ElementWrapper): __lt__ = ElementWrapper._lt_by_value
....:
sage: a = MyElement(1, parent = ZZ)
sage: 1 < a
| Sage Version 4.3.2.rc0, Release Date: 2010-02-03                   |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

wstein`@`bsd:~/build/sage-4.3.2.rc0$
```



---

Comment by was created at 2010-02-04 12:22:02

Changing priority from major to blocker.


---

Comment by was created at 2010-02-04 12:23:15

Oh, and here is the traceback:

```
sage: 1 < a                                                                 

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_INVALID_ADDRESS at address: 0x0000000000000000
0x000000010164f04d in __gmpz_cmp ()
(gdb) bt
#0  0x000000010164f04d in __gmpz_cmp ()
#1  0x0000000103ab178d in __pyx_f_4sage_5rings_7integer_7Integer__cmp_c_impl (__pyx_v_left=0x1097f81b0, __pyx_v_right=0x10caade10) at sage/rings/integer.c:7334
#2  0x0000000102317afc in __pyx_f_4sage_9structure_7element_7Element__richcmp_c_impl (__pyx_v_left=0x1097f81b0, __pyx_v_right=0x10caade10, __pyx_v_op=0) at sage/structure/element.c:7177
#3  0x0000000102349553 in __pyx_f_4sage_9structure_7element_7Element__richcmp (__pyx_v_left=0x1097f81b0, __pyx_v_right=0x10caade10, __pyx_v_op=0) at sage/structure/element.c:6917
#4  0x0000000103aae77b in __pyx_pf_4sage_5rings_7integer_7Integer___richcmp__ (__pyx_v_left=<value temporarily unavailable, due to optimizations>, __pyx_v_right=<value temporarily unavailable, due to optimizations>, __pyx_v_op=<value temporarily unavailable, due to optimizations>) at sage/rings/integer.c:7293
#5  0x000000010004e15c in try_rich_compare ()
#6  0x000000010004faff in PyObject_RichCompare ()
#7  0x00000001000af100 in PyEval_EvalFrameEx ()
#8  0x00000001000b3e70 in PyEval_EvalCodeEx ()
...
```



---

Comment by craigcitro created at 2010-02-05 17:56:58

As mentioned in one of the sage-devel threads linked above, the issue here is that `ZZ` assumes that if it's the parent of some `x`, then `x` is of type `sage.rings.integer.Integer`. (Similar assumptions are made all over.) It turns out that this popping up only on OSX was a weird artifact of compiler details/how memory is initialized/the alignment of the planets, as explained in the sage-devel thread.

I'm waiting for Nicolas to weigh in on what he thinks should happen with the `ElementWrapper` code -- he's probably the most appropriate person to spin a patch. (Nicolas, I'm adding you in the cc.)


---

Attachment


---

Comment by hivert created at 2010-02-06 09:24:20

Hi there !

I uploaded a patch where a replaced `ZZ` as a parent to `Sets().example("facade")` which is much closer to a meaningfull parent. It should hide the segfault problem which is actually a problem in Integer. However, I don't have access to a Max OS machine so please tell me if it doesn't work.

Cheers,

Florent


---

Comment by hivert created at 2010-02-06 09:24:20

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-02-06 10:31:58

Replying to [comment:1 was]:
> Here is a complete self-contained session that illustrates the problem:
> {{{
> wstein`@`bsd:~/build/sage-4.3.2.rc0$ ./sage
> ----------------------------------------------------------------------
> | Sage Version 4.3.2.rc0, Release Date: 2010-02-03                   |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> **********************************************************************
> *                                                                    *
> * Warning: this is a prerelease version, and it may be unstable.     *
> *                                                                    *
> **********************************************************************
> sage: class MyElement(ElementWrapper): __lt__ = ElementWrapper._lt_by_value
> ....:
> sage: a = MyElement(1, parent = ZZ)
> sage: 1 < a

Just for the record, could someone post the result of this more self contained example?

```
   sage: class F(Element):
    ....:     pass
    ....:
    sage: x = F(ZZ)
    sage: 1 < x
    False
```



---

Comment by nthiery created at 2010-02-06 12:16:45

Changing priority from blocker to major.


---

Comment by nthiery created at 2010-02-06 12:16:45

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2010-02-06 12:16:45

I have worked further on Florent's patch, and made a separate ticket for it: #8200.
I have removed the blocker priority on this, and set it on #8200. I leave this ticket open, since the issue is still there. I let the experts decide whether this should be a won't fix or not.


---

Comment by wdj created at 2010-02-06 12:42:15

For me, this patch fixed the segfault but still failed:


```
jeeves:sage-4.3.2.rc0 wdj$ ./sage -t  "devel/sage/sage/structure/element_wrapper.py" # Segfault
sage -t  "devel/sage/sage/structure/element_wrapper.py"     
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.2.rc0/devel/sage/sage/structure/element_wrapper.py", line 213:
    sage: 1 < l11
Expected:
    False
Got:
    True
**********************************************************************
1 items had failures:
   1 of  14 in __main__.example_8
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/wdj/.sage//tmp/.doctest_element_wrapper.py
         [2.3 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/structure/element_wrapper.py"
```

This is on sage-4.3.2.rc0 and mac 10.6.2.


---

Comment by nthiery created at 2010-02-06 13:08:34

Replying to [comment:7 wdj]:
> For me, this patch fixed the segfault but still failed:

Could you please try with the patch on #8200? It should be fixed in principle. Thanks!


---

Comment by wdj created at 2010-02-06 13:23:06

Replying to [comment:8 nthiery]:
> Replying to [comment:7 wdj]:
> > For me, this patch fixed the segfault but still failed:
> 
> Could you please try with the patch on #8200? It should be fixed in principle. Thanks!

I'm running sage -testall on #8200 now (the above single doctest passes though).

Does this new ticket mean you want Minh to make this as wontfix/invalid/duplicate and close it?


---

Comment by nthiery created at 2010-02-06 13:33:12

Replying to [comment:9 wdj]:
> Does this new ticket mean you want Minh to make this as wontfix/invalid/duplicate and close it?

No, it means that, with #8200, I have done my part at fixing my improper usage of ZZ. But the issue that such an improper usage can cause a segfault is still there, and I leave to the experts the decision of whether to fix it now, leave it to later, or resolve it as wontfix.

I personally vote -1 for making it a wontfix.


---

Comment by hivert created at 2010-02-07 10:20:01

> No, it means that, with #8200, I have done my part at fixing my improper usage of ZZ. But the issue that such an improper usage can cause a segfault is still there, and I leave to the experts the decision of whether to fix it now, leave it to later, or resolve it as wontfix.
> 
> I personally vote -1 for making it a wontfix.

I strongly second Nicolas -1. 

Moreover, if the segfault is not removed the invariant 

```
    x.parent() == ZZ <==> x.class == Integer
```

must be clearly stated with a _big warning_ in the doc. My opinion is that the segfault must be left only if there is a very large performance penalty fixing it.
By the way is this invariant an equivalence ? As far as I understood the segfault only came because we where breaking the `==>` part. 

Cheers,

Florent

By the way, I've removed myself as author since I won't be hacking in integers (my work in integrated in #8200).


---

Comment by roed created at 2013-03-28 23:00:39

Changing component from doctest to documentation.


---

Comment by mhansen created at 2013-07-22 15:19:59

Resolution: invalid


---

Comment by mhansen created at 2013-07-22 15:19:59

I think we can mark this as invalid as of 5.10:


```
sage: class MyElement(ElementWrapper): __lt__ = ElementWrapper._lt_by_value
sage: a = MyElement(ZZ, 1)
sage: 1 < a
False
sage: a < 1
False
```



---

Comment by nthiery created at 2013-07-24 10:56:39

I looked at the code of Integer._rich_cmp, and indeed it now tests that the right hand side is indeed in the Integer class which fixes the issue.

In an ideal world, we would have added a regression test, but oh well, let's move on.
