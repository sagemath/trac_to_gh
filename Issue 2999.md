# Issue 2999: Some packages don't respect the CC environment variable

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-04-22 16:42:08

Assignee: mabshoff

CC:  mjo

Packages which seem to not honor CC environment variable (they use "gcc"):


```
flint-1.06.p2
atlas-3.8.1.p1
f2c-20070816.p0
symmetrica-2.0.p2
polybori-0.3.1.p1
rubiks-20070912.p5
zn_poly-0.8.p0
sage-3.0.rc1
gap-4.4.10.p7 // guava3.4
tachyon-0.98beta.p5
palp-1.1.p1
```



---

Comment by PolyBoRi created at 2008-04-22 21:07:20

For PolyBoRi see the patch for the custom.py file. Feel free to add additional Variables there

Good Night,
  Alexander


---

Comment by PolyBoRi created at 2008-04-22 21:18:19

CC/CXX patch


---

Attachment


---

Comment by mabshoff created at 2008-04-26 10:45:37

Changing status from new to assigned.


---

Comment by mvngu created at 2009-07-14 07:58:54

Ticket #6437 has an updated spkg so that polybori can be built under Solaris.


---

Comment by ddrake created at 2009-09-16 23:11:27

There are other spkgs which also fail to respect CC: from [http://groups.google.com/group/sage-devel/msg/a9192a6b51a74d22 this thread](http://groups.google.com/group/sage-devel/msg/a9192a6b51a74d22 this thread), I see the following spkgs which are not listed above:

> * cliquer-1.2
>
> * symmetrica-2.0.p4
>
> * ratpoints-2.1.2.p2


---

Comment by mvngu created at 2009-09-16 23:13:25

Cliquer should respect the CC environment variable now. See ticket #6681.


---

Comment by mjo created at 2012-02-25 21:05:29

The f2c package is fixed at #7027, so I've removed it from the list.


---

Comment by mjo created at 2012-02-25 21:17:13

symmetrica fixed at #10719, so removing that too.


---

Comment by mjo created at 2012-02-25 21:19:04

flint and zn_poly have their own tickets at #7024 and #12433 respectively, so there's no need to duplicate them here.


---

Comment by mjo created at 2012-02-25 22:33:59

Polybori also respects `$CC` now, although I can't pin down the ticket where it went from doesn't-work-at-all to something else.


---

Comment by mjo created at 2012-02-25 22:45:41

Tachyon should have been fixed by #9379 and #10681. Waiting on #7069 to confirm on Solaris.


---

Comment by mjo created at 2012-02-25 22:52:25

And gap was fixed at #2575 and #4161...


---

Comment by mjo created at 2012-02-25 22:55:56

Rubiks fixed at #7036.


---

Comment by mjo created at 2012-02-25 23:16:22

Working on palp at #7071.


---

Comment by vbraun created at 2012-02-26 19:39:01

ATLAS supports CC since atlas-3.8.3.p18.


---

Comment by mjo created at 2012-02-27 14:07:33

Ok, atlas was fixed in #10226 and we have a ticket for the sage library at #12443. I replaced the initial list for review.


---

Comment by mjo created at 2012-02-27 14:07:33

Changing status from new to needs_review.


---

Comment by ohanar created at 2012-02-27 17:55:46

Changing status from needs_review to positive_review.


---

Comment by ohanar created at 2012-02-27 17:55:46

Yup, there are plenty of tickets regarding all of these packages -- some from me with the clang port, some from David Kirby with the Sun CC port.


---

Comment by mjo created at 2012-02-27 18:02:42

Thanks, I did the same thing with the `$CXX` ticket at #3000.


---

Comment by AlexanderDreyer created at 2012-02-28 09:06:50

Replying to [comment:9 mjo]:
> Polybori also respects `$CC` now, although I can't pin down the ticket where it went from doesn't-work-at-all to something else.
That was #6437 as mentioned above.


---

Comment by jdemeyer created at 2012-03-04 21:25:51

Resolution: duplicate


---

Comment by leif created at 2012-03-17 02:25:11

Replying to [comment:16 ohanar]:
> Yup, there are plenty of tickets regarding all of these packages -- some from me with the clang port, some from David Kirby with the Sun CC port.

AFAIK at least ratpoints doesn't [yet] have its own ticket; I would have left this ticket open as a meta-ticket until all issues (or spkgs) have really been fixed.


---

Comment by leif created at 2012-03-17 10:41:21

Replying to [comment:11 mjo]:
> And gap was fixed at #2575 and #4161...

Aha.  I knew `CC` was "intentionally" unset in GAP's `spkg-install` for a long time (which was annoying anyway), but *now* I still get:

```
gcc version 4.6.3 (GCC) 
****************************************************
*WARNING*: Unsetting CC since that tends to break GAP building
*WARNING*: Unsetting CXX since that tends to break GAP building
checking build system type... x86_64-unknown-linux-gnu
checking host system type... x86_64-unknown-linux-gnu
checking target system type... x86_64-unknown-linux-gnu
checking for gcc... gcc
checking for C compiler default output file name... 
configure: error: C compiler cannot create executables
See `config.log' for more details.
Configuration of GAP failed.

real	0m0.793s
user	0m0.160s
sys	0m0.050s
************************************************************************
Error installing package gap-4.4.12.p6
************************************************************************
```


So if there's been an issue with `CC` and `CXX` set, it might have been *fixed upstream* (I believe so), but it *isn't fixed in Sage*.

[The problem here simply is that the "default" `gcc`, which is 4.4.3, doesn't understand some of the options I pass in `CFLAGS`.  GCC 4.6.3, specified in `CC`, of course _does_ understand them.]


---

Comment by leif created at 2012-03-17 15:02:52

Replying to [comment:20 leif]:
> Replying to [comment:16 ohanar]:
> > Yup, there are plenty of tickets regarding all of these packages -- some from me with the clang port, some from David Kirby with the Sun CC port.
> 
> AFAIK at least ratpoints doesn't [yet] have its own ticket [...]

This (ratpoints) is now #12682 (*needing review*).
