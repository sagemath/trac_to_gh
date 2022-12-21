# Issue 2822: Invalid read in libgroebner.so [picked up by valgrinding catalogue.py]

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-04-06 06:26:30

Assignee: malb

CC:  burcin polybori

Valgrind says:

```
==28038== Invalid read of size 4
==28038==    at 0x152C3A90: (within /scratch/mabshoff/release-cycle/sage-3.0.alpha1/local/lib/libgroebner.so)
==28038==    by 0x4FEEB8C: exit (in /lib/libc-2.3.6.so)
==28038==  Address 0x5566450 is not stack'd, malloc'd or (recently) free'd
```

This seems to be cause by either the new PolyBoRi.spkg or its interface.

The component for this bug is debatable.

Cheers,

Michael


---

Comment by malb created at 2008-04-07 13:16:22

stripped valgrind session for Sage 3.0.alpha2 + PolyBoRi with SAGE_DEBUG


---

Attachment

After rebuilding PolyBoRi with debugging options (export SAGE_DEBUG=1) I don't get this invalid read anymore. I've attached a the valgrind log for a simple session.

It might be worth noting that almost all alleged memleaks are due to one call. It might make sense to ask Michael and Alexander about that one.


---

Comment by malb created at 2008-04-07 14:11:22

For the record: We don't know yet if it is "our" wrapper fault or an internal PolyBoRi fault.


---

Comment by malb created at 2008-04-07 14:11:22

Changing keywords from "" to "polybori".


---

Comment by PolyBoRi created at 2008-04-07 14:16:58

You can also disable the NDEBUG flag in PolyBoRi,
scons CPPDEFINES=""
to get lots of assertions checked.


---

Comment by PolyBoRi created at 2008-04-08 05:53:03

Mabshoff wrote in sage-devel, that this happens in every sage session.
Does this mean, it even happens, if PolyBoRi isn't used at all.
So it must be some global code.
In libgroebner itself there exist almost no global things, except
some call
static base_generator_type generator(static_cast<unsigned int>(std::time(0)));
(which indeed hasn't been implemented in 0.1).


---

Comment by malb created at 2008-04-08 10:30:26

Replying to [comment:4 PolyBoRi]:
> Mabshoff wrote in sage-devel, that this happens in every sage session.
> Does this mean, it even happens, if PolyBoRi isn't used at all.
> So it must be some global code.
> In libgroebner itself there exist almost no global things, except
> some call
> static base_generator_type generator(static_cast<unsigned int>(std::time(0)));
> (which indeed hasn't been implemented in 0.1).

Yes, afaik it happens even when no PolyBoRi functionality is used so it ought to be global code. Also, in the cleaned up valgrind log, we have:


```
==8421== 16 bytes in 1 blocks are indirectly lost in loss record 63 of 2,800
==8421==    at 0x4A07809: operator new(unsigned long) (vg_replace_malloc.c:230)
==8421==    by 0x1E409188: polybori::get_ordering(int) (pbori_order.h:84)
==8421==    by 0x1E4070E6: polybori::BoolePolyRing::BoolePolyRing(unsigned, int, bool) (BoolePolyRing.cc:187)
==8421==    by 0x1E9FA733: __static_initialization_and_destruction_0(int, int) (BooleEnv.cc:85)
==8421==    by 0x1EA9C8E1: (within /usr/local/sage-3.0.alpha2/local/lib/libgroebner.so)
==8421==    by 0x1E9769C2: (within /usr/local/sage-3.0.alpha2/local/lib/libgroebner.so)
==8421==    by 0x1E0C0C6D: (within /usr/local/sage-3.0.alpha2/devel/sage-main/build/sage/rings/polynomial/pbori.so)
```


several times and the number of lost bytes increases. So we seem to initialise PolyBoRi several times, maybe?


---

Comment by cwitty created at 2008-04-09 17:42:19

When I tried valgrind on this, I got a slightly different record.  I don't know if the new information is meaningful or just random.

```
==27941== Invalid read of size 4
==27941==    at 0xA1BFE98: (within /home/cwitty/sage-3.0.alpha2/local/lib/libgroebner.so)
==27941==    by 0x40B6F13: exit (in /lib/i686/cmov/libc-2.7.so)
==27941==    by 0x80E7DB1: handle_system_exit (pythonrun.c:1618)
==27941==    by 0x80E7FA4: PyErr_PrintEx (pythonrun.c:1062)
==27941==    by 0x80E8848: PyRun_SimpleFileExFlags (pythonrun.c:976)
==27941==    by 0x80592B4: Py_Main (main.c:523)
==27941==    by 0x8058771: main (python.c:23)
==27941==  Address 0x448b7e4 is 4 bytes inside a block of size 16 free'd
==27941==    at 0x40242EC: operator delete(void*) (vg_replace_malloc.c:342)
==27941==    by 0x9FFA877: boost::detail::sp_counted_impl_p<polybori::CDynamicOrder<polybori::LexOrder> >::~sp_counted_impl_p() (in /home/cwitty/sage-3.0.alpha2/local/lib/libpolybori.so)
==27941==    by 0x9F15D04: boost::detail::sp_counted_base::destroy() (sp_counted_base_gcc_x86.hpp:126)
==27941==    by 0x9FFE16F: (within /home/cwitty/sage-3.0.alpha2/local/lib/libpolybori.so)
==27941==    by 0x40B6F13: exit (in /lib/i686/cmov/libc-2.7.so)
==27941==    by 0x80E7DB1: handle_system_exit (pythonrun.c:1618)
==27941==    by 0x80E7FA4: PyErr_PrintEx (pythonrun.c:1062)
==27941==    by 0x80E8848: PyRun_SimpleFileExFlags (pythonrun.c:976)
==27941==    by 0x80592B4: Py_Main (main.c:523)
==27941==    by 0x8058771: main (python.c:23)
```



---

Comment by mabshoff created at 2008-04-09 17:55:58

Hi Carl,

I thing the above is very useful. It clearly implicates some destructor, which supports the theory that we initialize some global data structure more than once. I would also recommend that we turn on debug symbols for PolyBoRi per default until further notice. There is no performance penalty and only some overhead for increased RAM use.

Cheers,

Michael


---

Comment by PolyBoRi created at 2008-04-10 06:14:06

except the random generator, I can't remember of anything static in libgroebner.
So I would be really interested, of some stack trace in libgroebner.

The trace log of libpolybori indicates, that the destruction of
static BooleEnv::active_ring
affected.

The trace log also indicates, that there happens something in libgroebner accessing it, after its destruction.
But I don't know of global code except that random generator (which doesn't do anything with polynomials).
I am not so very experienced with this low level stuff, but is it possible, that libpolybori and libgroebner both try to destruct BooleEnv::active_ring.

Maybe it would help just linking them together in one common shared library (as we do with our python module).


---

Attachment

Thanks to Alexander we provide a fixed CCuddCore.h.
I hope, that will fix the invalid reads (at least it should fix the leaks).


---

Comment by mabshoff created at 2008-04-11 20:09:16

Ok, I have finally tracked this down to us linking all three libraries dynamically. Switching to static linking fixes the issue after making sure that we use -fPIC:

```
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/mabshoff
/release-cycle/sage-3.0.alpha2/local/include/cudd -I/scratch/mabshoff/release-cycle/sage-
3.0.alpha2/local/include/polybori -I/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/include
/polybori/groebner -I/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local//include -I/scratch
/mabshoff/release-cycle/sage-3.0.alpha2/local//include/csage -I/scratch/mabshoff/release-
cycle/sage-3.0.alpha2/devel//sage/sage/ext -I/scratch/mabshoff/release-cycle/sage-3.0.alpha2
/local/include/python2.5 -c sage/rings/polynomial/pbori.cpp -o build/temp.linux-x86_64-2.5
/sage/rings/polynomial/pbori.o -w -w
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for 
C++ 
g++ -pthread -shared build/temp.linux-x86_64-2.5/sage/rings/polynomial/pbori.o -L/scratch
/mabshoff/release-cycle/sage-3.0.alpha2/local//lib -lcsage -lpolybori -lpboriCudd -lgroebner 
-lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/rings/polynomial/pbori.so
/usr/bin/ld: /scratch/mabshoff/release-cycle/sage-3.0.alpha2/local
//lib/libpolybori.a(BoolePolyRing.o): relocation R_X86_64_32 against `a local symbol' can not be 
used when making a shared object; recompile with -fPIC
/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local//lib/libpolybori.a: could not read 
symbols: Bad value
collect2: ld returned 1 exit status
error: command 'g++' failed with exit status 1
sage: There was an error installing modified sage library code.
```

I also replaced CCuddCore.h with the new version provided by Alexander and it does fix some of the memory leaks. There are more of them, but that will be a new ticket.

The new spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha4/polybori-0.3.1.p1.spkg

To test it build it, then 

touch devel/sage/sage/rings/polynomial/pbori.pyx

And to a `sage -b`

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-11 20:09:47

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-11 20:09:47

Changing assignee from malb to mabshoff.


---

Comment by malb created at 2008-04-11 21:52:02

*Review*
 - builds fine under Debian/Linux
 - after rebuilding `pbori.pyx` no more SIGSEGVs
 - I say apply.


---

Comment by mabshoff created at 2008-04-11 22:09:01

Merged in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-11 22:09:01

Resolution: fixed


---

Comment by PolyBoRi created at 2008-04-12 23:07:13

New version, cleaner code


---

Attachment

Hi everybody,
I've added a new (somehow cleaner) version of CCuddCore.h. Maybe that fixes some of the remaining leaks.

Regards
  Alexander Dreyer
