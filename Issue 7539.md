# Issue 7539: primes.p0.spkg with "prime_sieve.c" functionality

archive/issues_007539.json:
```json
{
    "body": "Assignee: ohanar\n\nCC:  kevin.stueve robertwb was victor leif dimpase\n\nThis ticket was split away from #7013:\n\nLet's create a \"primes.p0.spkg\" (better names appreciated ...) which provides the \"prime_sieve.c\" code/functionality from T. Oliveira e Silva as a library.\n\nPrimary goal: The function \"primes_interval()\" from \"prime_sieve.c\" is accessible from a dynamic library \"libprimes.so\" resp. \"libprimes.dylib\" (resp. \"libprimes.dll\" if Cygwin is in our scope), which in turn compiles (and works correctly ...) on the platforms Sage supports, to be a part of future versions of Sage.\n\nSecondary goal: This spkg also provides (i.e. contains) certain precomputed tables from Kevin Stueve (which in a Sage installation will be installed under \"data/prime_pi_tables/\").\n\nTertiary goal: Provide the LMO code/functionality from Victor Miller in the same way, too. (Eventually outside the scope of this ticket, so potentially another follow-up ticket.)\n\nMaintainers till end 2010: Andrew Rohana, Georg S. Weber\n\nIssue created by migration from https://trac.sagemath.org/ticket/7539\n\n",
    "created_at": "2009-11-26T21:48:06Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "primes.p0.spkg with \"prime_sieve.c\" functionality",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7539",
    "user": "GeorgSWeber"
}
```
Assignee: ohanar

CC:  kevin.stueve robertwb was victor leif dimpase

This ticket was split away from #7013:

Let's create a "primes.p0.spkg" (better names appreciated ...) which provides the "prime_sieve.c" code/functionality from T. Oliveira e Silva as a library.

Primary goal: The function "primes_interval()" from "prime_sieve.c" is accessible from a dynamic library "libprimes.so" resp. "libprimes.dylib" (resp. "libprimes.dll" if Cygwin is in our scope), which in turn compiles (and works correctly ...) on the platforms Sage supports, to be a part of future versions of Sage.

Secondary goal: This spkg also provides (i.e. contains) certain precomputed tables from Kevin Stueve (which in a Sage installation will be installed under "data/prime_pi_tables/").

Tertiary goal: Provide the LMO code/functionality from Victor Miller in the same way, too. (Eventually outside the scope of this ticket, so potentially another follow-up ticket.)

Maintainers till end 2010: Andrew Rohana, Georg S. Weber

Issue created by migration from https://trac.sagemath.org/ticket/7539





---

archive/issue_comments_063947.json:
```json
{
    "body": "It is appropriate to give credit to the sources I used in making the tables of offsets between prime_pi and a logarithmic integral approximation.  I used an asymptotic approximation to the logarithmic integral provided by Fredrik Johansson and the tables of prime_pi from http://www.primefan.ru/stuff/primes/table.html.  And the idea of combining a table of values of prime_pi and sieving for fast computation of the prime_pi was provided by the nth prime page at http://primes.utm.edu/nthprime/\n\nThe primefan tables are extensive, and are from a combined effort of several individuals, including Andrey V. Kulsha, Anatoly F. Selevich, and Tom\u00e1s Oliveira e Silva.  It is likely that the total computation time required to generate these tables was many processor years.\n\nAs processor time (for the developer), hard-drive storage (for the client), and Internet bandwidth (for the client) become cheaper and more available, I would like to see published tables of prime_pi to expand (and to see resources put toward such computation).  It would be nice for the number of values in the prime_pi tables in Sage to increase every few years as the computation of the tables becomes easier for the developer and the download and storage of the tables becomes easier for the client.  Maybe several table sizes could be offered.  A standard table could be the default for most users, but for those who are studying the distribution of prime numbers and desire speed over extra storage space on their hard-drive (and for bragging rights for Sage), larger tables could be offered.  A web-service could even be offered to query a very large table of values of the prime counting function (the additional sieving could be done either on the server or client).  Of course, it would be very important to have redundancy in such large calculations (the generation of the prime_pi tables), as there have been incorrect values of the prime counting function published several times in the past.\n\nKevin Stueve",
    "created_at": "2009-11-27T07:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63947",
    "user": "kevin.stueve"
}
```

It is appropriate to give credit to the sources I used in making the tables of offsets between prime_pi and a logarithmic integral approximation.  I used an asymptotic approximation to the logarithmic integral provided by Fredrik Johansson and the tables of prime_pi from http://www.primefan.ru/stuff/primes/table.html.  And the idea of combining a table of values of prime_pi and sieving for fast computation of the prime_pi was provided by the nth prime page at http://primes.utm.edu/nthprime/

The primefan tables are extensive, and are from a combined effort of several individuals, including Andrey V. Kulsha, Anatoly F. Selevich, and Tomás Oliveira e Silva.  It is likely that the total computation time required to generate these tables was many processor years.

As processor time (for the developer), hard-drive storage (for the client), and Internet bandwidth (for the client) become cheaper and more available, I would like to see published tables of prime_pi to expand (and to see resources put toward such computation).  It would be nice for the number of values in the prime_pi tables in Sage to increase every few years as the computation of the tables becomes easier for the developer and the download and storage of the tables becomes easier for the client.  Maybe several table sizes could be offered.  A standard table could be the default for most users, but for those who are studying the distribution of prime numbers and desire speed over extra storage space on their hard-drive (and for bragging rights for Sage), larger tables could be offered.  A web-service could even be offered to query a very large table of values of the prime counting function (the additional sieving could be done either on the server or client).  Of course, it would be very important to have redundancy in such large calculations (the generation of the prime_pi tables), as there have been incorrect values of the prime counting function published several times in the past.

Kevin Stueve



---

archive/issue_comments_063948.json:
```json
{
    "body": "Leif Leonhardy sent some very useful contributions over the past days.  Following is our correspondence.\n----\n*Friday December 4, 2009:\nHi Kevin,\n\nI've made some changes to [your version of] TOS's prime_sieve.c, making\nit more portable and removing the 4-byte pointer constraint (i.e. fixing\nyour \"-m64\" problem).\n\nThe original version also contains an overflow bug on large intervals\n(>=2^36).\n(Another overflow still occurs [very] near to 2^64, because the sum of\n[the muted] main_base and numbers_per_segment might [or will] exceed 64\nbits.)\nFor use with Sage, the modulo-64* limitation on the intervals' bounds\nshould be removed, too (easy, but it didn't disturb me yet ;-) ).\nI also fixed your parameter handling and output of the result.\n\nIf you intend to build a library rather than a stand-alone program the\nmemory management should be rewritten (and globals removed). Running\nmany sieving threads on multi-core CPUs doesn't make much sense because\nmemory (consumption and traffic) is the bottleneck; the sieving primes\nlists (\"main_lists\") can't be shared among tasks (TOS's optimization\nis a \"sequential\" one in that sense).\n\nNote that TOS's implementation, as he stated, was created mainly for\nillustration purposes - \"simple but serious\" - and wasn't intended (and\ndoesn't claim) to be \"fully optimized\" or optimal in all aspects.\n\nThe default values for sieve (segment) and bucket size were appropriate\nin 2002; for contemporary hardware, both should be increased. I got best\nresults with the (currently) maximal bucket size of 64KB, and sieve\nsegment sizes of 256KB and 1MB on an Intel Pentium 4 Prescott (1MB L2\ncache) and Intel Core2 with 6MB L2 cache per core-pair (e.g. E8400,\nQ9x50), respectively. Also, native code (\"-m64\"**) runs faster on x86_64\nplatforms, even with u32 as the sieve basetype; using 64- rather than\n32-bit words for the sieve has probably greater effect on platforms like\nSPARC64, I guess. (Compile with \"-DSIEVE_BASETYPE_U64\" to get that.)\n\nI've attached your version of prime_sieve.c (\"Silva.c.orig\", 09/04/09),\ntoo, since I'm not sure I fetched the latest. The first diff contains a\n(working) subset of the changes I made, the second contains all changes.\nA ChangeLog (and adaption of TOS's \"#if 0\" test code) is in the\npipeline... :/\n\nHave fun,\n-Leif\n\n----\n\n*My reply, December 4th 2009\nSounds great\n[...]\n\nOn a Macbook pro, I have found that dualthreaded (simply calling TOS\ntwice for two adjacent intervals) is about 1.71 times faster.  I hope\nthat it might be possible to improve that.\n[...]\nKevin Stueve\n----\n*From Leif, December 4th 2009\nHi again,\n\nI've just found another little 64bit-pointer bug in get_memory(),\nthe attached diff contains only that patch.\n\n-Leif\n----\n*From Leif, December 5th, 2009\nHi Kevin,\n\nI've fixed the modulo-64 (or modulo-128 for 64-bit sieve words)\nrestriction on interval bounds (by enlarging the sieved interval and\nsubtracting the \"extra\" primes found if necessary);\nupper_bound==lower_bound is allowed now, too.\n[Adapting the Python code is up to you ;-)]\n\nThe majority of \"#ifdef SIEVE_BASETYPE_U64\"s has also been removed in\nfavour of conditional macros and constants defined at the beginning.\n\n-Leif\n\nP.S.: By \"many sieving threads\" (currently: processes) I meant more than\n2 or 4; but even with only few instances the processor's cache(s) might\nbegin thrashing and we might run out of physical RAM; the behaviour can\ndepend on not only the specific hardware but compile-time parameters\n(and does of course depend on the interval's lower bound), too.\n[Even small intervals above 4e18 require ~0.8GB (per process), intervals\nnear 2^64 approx. 1.6GB. In worst case the machine starts swapping and\nmultiple processes run slower, taking more time than a single would have\ntaken. If I could get rid of the megs of sieving primes, I'd use the\nhundreds of cores on modern GPUs. :-) ]",
    "created_at": "2009-12-06T06:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63948",
    "user": "kevin.stueve"
}
```

Leif Leonhardy sent some very useful contributions over the past days.  Following is our correspondence.
----
*Friday December 4, 2009:
Hi Kevin,

I've made some changes to [your version of] TOS's prime_sieve.c, making
it more portable and removing the 4-byte pointer constraint (i.e. fixing
your "-m64" problem).

The original version also contains an overflow bug on large intervals
(>=2^36).
(Another overflow still occurs [very] near to 2^64, because the sum of
[the muted] main_base and numbers_per_segment might [or will] exceed 64
bits.)
For use with Sage, the modulo-64* limitation on the intervals' bounds
should be removed, too (easy, but it didn't disturb me yet ;-) ).
I also fixed your parameter handling and output of the result.

If you intend to build a library rather than a stand-alone program the
memory management should be rewritten (and globals removed). Running
many sieving threads on multi-core CPUs doesn't make much sense because
memory (consumption and traffic) is the bottleneck; the sieving primes
lists ("main_lists") can't be shared among tasks (TOS's optimization
is a "sequential" one in that sense).

Note that TOS's implementation, as he stated, was created mainly for
illustration purposes - "simple but serious" - and wasn't intended (and
doesn't claim) to be "fully optimized" or optimal in all aspects.

The default values for sieve (segment) and bucket size were appropriate
in 2002; for contemporary hardware, both should be increased. I got best
results with the (currently) maximal bucket size of 64KB, and sieve
segment sizes of 256KB and 1MB on an Intel Pentium 4 Prescott (1MB L2
cache) and Intel Core2 with 6MB L2 cache per core-pair (e.g. E8400,
Q9x50), respectively. Also, native code ("-m64"**) runs faster on x86_64
platforms, even with u32 as the sieve basetype; using 64- rather than
32-bit words for the sieve has probably greater effect on platforms like
SPARC64, I guess. (Compile with "-DSIEVE_BASETYPE_U64" to get that.)

I've attached your version of prime_sieve.c ("Silva.c.orig", 09/04/09),
too, since I'm not sure I fetched the latest. The first diff contains a
(working) subset of the changes I made, the second contains all changes.
A ChangeLog (and adaption of TOS's "#if 0" test code) is in the
pipeline... :/

Have fun,
-Leif

----

*My reply, December 4th 2009
Sounds great
[...]

On a Macbook pro, I have found that dualthreaded (simply calling TOS
twice for two adjacent intervals) is about 1.71 times faster.  I hope
that it might be possible to improve that.
[...]
Kevin Stueve
----
*From Leif, December 4th 2009
Hi again,

I've just found another little 64bit-pointer bug in get_memory(),
the attached diff contains only that patch.

-Leif
----
*From Leif, December 5th, 2009
Hi Kevin,

I've fixed the modulo-64 (or modulo-128 for 64-bit sieve words)
restriction on interval bounds (by enlarging the sieved interval and
subtracting the "extra" primes found if necessary);
upper_bound==lower_bound is allowed now, too.
[Adapting the Python code is up to you ;-)]

The majority of "#ifdef SIEVE_BASETYPE_U64"s has also been removed in
favour of conditional macros and constants defined at the beginning.

-Leif

P.S.: By "many sieving threads" (currently: processes) I meant more than
2 or 4; but even with only few instances the processor's cache(s) might
begin thrashing and we might run out of physical RAM; the behaviour can
depend on not only the specific hardware but compile-time parameters
(and does of course depend on the interval's lower bound), too.
[Even small intervals above 4e18 require ~0.8GB (per process), intervals
near 2^64 approx. 1.6GB. In worst case the machine starts swapping and
multiple processes run slower, taking more time than a single would have
taken. If I could get rid of the megs of sieving primes, I'd use the
hundreds of cores on modern GPUs. :-) ]



---

archive/issue_comments_063949.json:
```json
{
    "body": "Provided by Leif Leonhardy in his first email",
    "created_at": "2009-12-06T06:30:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63949",
    "user": "kevin.stueve"
}
```

Provided by Leif Leonhardy in his first email



---

archive/issue_comments_063950.json:
```json
{
    "body": "Attachment [Silva.c.additional.diff](tarball://root/attachments/some-uuid/ticket7539/Silva.c.additional.diff) by kevin.stueve created at 2009-12-06 06:31:04\n\nProvided by Leif Leonhardy in his second email",
    "created_at": "2009-12-06T06:31:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63950",
    "user": "kevin.stueve"
}
```

Attachment [Silva.c.additional.diff](tarball://root/attachments/some-uuid/ticket7539/Silva.c.additional.diff) by kevin.stueve created at 2009-12-06 06:31:04

Provided by Leif Leonhardy in his second email



---

archive/issue_comments_063951.json:
```json
{
    "body": "Provided by Leif Leonhardy in his third email",
    "created_at": "2009-12-06T06:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63951",
    "user": "kevin.stueve"
}
```

Provided by Leif Leonhardy in his third email



---

archive/issue_comments_063952.json:
```json
{
    "body": "Attachment [Silva.c.orig](tarball://root/attachments/some-uuid/ticket7539/Silva.c.orig) by mvngu created at 2009-12-24 15:27:50\n\noriginal version of Silva.c",
    "created_at": "2009-12-24T15:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63952",
    "user": "mvngu"
}
```

Attachment [Silva.c.orig](tarball://root/attachments/some-uuid/ticket7539/Silva.c.orig) by mvngu created at 2009-12-24 15:27:50

original version of Silva.c



---

archive/issue_comments_063953.json:
```json
{
    "body": "From IRC:\n\n```\n06:44 < mvngu> The attachments look like a mess to me.\n06:45 < SageWWW> They are supposedly diffs\n06:45 < mvngu> I downloaded the first attachment, uncompressed it, and can't \n               work out which patches to apply in which order.\n06:49 < SageWWW> \"The first diff contains a (working) subset of the changes I \n                 made, the second contains all changes.\"Leif\n06:50 < SageWWW> That is in his first email.  And he also included the original\n06:51 < mvngu> So Silva.c.orig is the original version. And Silva.c is the \n               newer version with all changes in the diff's?\n06:51 < SageWWW> Perhaps.  It would be easier to tell if Leif added himself to \n                 the authors section of the updated code\n06:53 < mvngu> The diff's don't look like standard diff formats. At least when \n               I apply them with the command \"patch\", they failed to apply.\n06:56 < SageWWW> It is extra confusing that Andrew Ohana and Leif Leonhardy \n                 both made their own updated version of Kevin Stueve's updated \n                 version of Oliviera e Silva's code.\n06:56 < mvngu> I think if you diff Silva.c.orig against Silva.c, you get the \n               differences in the newer version (which is Silva.c).\n```\n\nThe attachments look confusing to me. So I have attached what I think is the sequence of patches to apply on top of the original C code version `Silva.c.orig`. Starting from `Silva.c.orig`, apply the three patches in this order:\n\n1. `01_Silva.patch`\n2. `02_Silva.patch`\n3. `03_Silva.patch`\n\nAfter applying the above three patches on top of `Silva.c.orig`, you get the file `Silva.c`. I hope my attachments would resolve some of the confusion.",
    "created_at": "2009-12-24T15:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63953",
    "user": "mvngu"
}
```

From IRC:

```
06:44 < mvngu> The attachments look like a mess to me.
06:45 < SageWWW> They are supposedly diffs
06:45 < mvngu> I downloaded the first attachment, uncompressed it, and can't 
               work out which patches to apply in which order.
06:49 < SageWWW> "The first diff contains a (working) subset of the changes I 
                 made, the second contains all changes."Leif
06:50 < SageWWW> That is in his first email.  And he also included the original
06:51 < mvngu> So Silva.c.orig is the original version. And Silva.c is the 
               newer version with all changes in the diff's?
06:51 < SageWWW> Perhaps.  It would be easier to tell if Leif added himself to 
                 the authors section of the updated code
06:53 < mvngu> The diff's don't look like standard diff formats. At least when 
               I apply them with the command "patch", they failed to apply.
06:56 < SageWWW> It is extra confusing that Andrew Ohana and Leif Leonhardy 
                 both made their own updated version of Kevin Stueve's updated 
                 version of Oliviera e Silva's code.
06:56 < mvngu> I think if you diff Silva.c.orig against Silva.c, you get the 
               differences in the newer version (which is Silva.c).
```

The attachments look confusing to me. So I have attached what I think is the sequence of patches to apply on top of the original C code version `Silva.c.orig`. Starting from `Silva.c.orig`, apply the three patches in this order:

1. `01_Silva.patch`
2. `02_Silva.patch`
3. `03_Silva.patch`

After applying the above three patches on top of `Silva.c.orig`, you get the file `Silva.c`. I hope my attachments would resolve some of the confusion.



---

archive/issue_comments_063954.json:
```json
{
    "body": "Attachment [01_Silva.patch](tarball://root/attachments/some-uuid/ticket7539/01_Silva.patch) by mvngu created at 2009-12-24 16:24:04\n\nfirst patch of Leif_attachment1.zip, i.e. Silva.c.diff0",
    "created_at": "2009-12-24T16:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63954",
    "user": "mvngu"
}
```

Attachment [01_Silva.patch](tarball://root/attachments/some-uuid/ticket7539/01_Silva.patch) by mvngu created at 2009-12-24 16:24:04

first patch of Leif_attachment1.zip, i.e. Silva.c.diff0



---

archive/issue_comments_063955.json:
```json
{
    "body": "Leif_attachment1.zip, patch Silva.c.diff: apply all changes in Silva.c.diff that are not in Silva.c.diff0",
    "created_at": "2009-12-24T16:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63955",
    "user": "mvngu"
}
```

Leif_attachment1.zip, patch Silva.c.diff: apply all changes in Silva.c.diff that are not in Silva.c.diff0



---

archive/issue_comments_063956.json:
```json
{
    "body": "Attachment [02_Silva.patch](tarball://root/attachments/some-uuid/ticket7539/02_Silva.patch) by mvngu created at 2009-12-24 16:24:51\n\nadd changes from Silva.c.additional.diff",
    "created_at": "2009-12-24T16:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63956",
    "user": "mvngu"
}
```

Attachment [02_Silva.patch](tarball://root/attachments/some-uuid/ticket7539/02_Silva.patch) by mvngu created at 2009-12-24 16:24:51

add changes from Silva.c.additional.diff



---

archive/issue_comments_063957.json:
```json
{
    "body": "Attachment [04_Silva.patch](tarball://root/attachments/some-uuid/ticket7539/04_Silva.patch) by mvngu created at 2009-12-24 16:25:07\n\nadd changes from Silva.c.bounds-restriction-removed.diff",
    "created_at": "2009-12-24T16:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63957",
    "user": "mvngu"
}
```

Attachment [04_Silva.patch](tarball://root/attachments/some-uuid/ticket7539/04_Silva.patch) by mvngu created at 2009-12-24 16:25:07

add changes from Silva.c.bounds-restriction-removed.diff



---

archive/issue_comments_063958.json:
```json
{
    "body": "Attachment [Silva.c](tarball://root/attachments/some-uuid/ticket7539/Silva.c) by mvngu created at 2009-12-24 16:25:43\n\nversion of Silva.c after applying the previous 4 patches",
    "created_at": "2009-12-24T16:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63958",
    "user": "mvngu"
}
```

Attachment [Silva.c](tarball://root/attachments/some-uuid/ticket7539/Silva.c) by mvngu created at 2009-12-24 16:25:43

version of Silva.c after applying the previous 4 patches



---

archive/issue_comments_063959.json:
```json
{
    "body": "From IRC:\n\n```\n07:57 < SageWWW> mvngu, what do you think Leif meant by a working subset of \n                 changes?\n08:02 < mvngu> SageWWW: I think it's removing the 4-byte pointer constraint. \n               The working changes in the first diff now also work for 8-byte \n               pointers.\n08:03 < SageWWW> It is still confusing.  Leif provided 4 patches total.\n08:03 < mvngu> I know. You could ask for clarification on the ticket. \n08:03 < mvngu> Do you have an account on the trac server?\n08:04 < SageWWW> I think you should modify your comment on the trac server to \n                 specifically state which of Leif's files corresponds to which \n                 of yours\n08:04 < SageWWW> kevin.stueve\n08:04 < mvngu> Let me modify the patches I have attached. Hang on...\n```\n\nI have deleted the previous 3 patches. In their place I attached 4 patches which correspond to the diff's contained in the attachments kevin.stueve. Starting from Silva.c.orig, apply the 4 patches in this order:\n\n1. `01_Silva.patch`\n2. `02_Silva.patch`\n3. `03_Silva.patch`\n4. `04_Silva.patch`\n \nAfter applying the above four patches on top of Silva.c.orig, you get the file Silva.c. I hope my attachments would resolve some of the confusion.",
    "created_at": "2009-12-24T16:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63959",
    "user": "mvngu"
}
```

From IRC:

```
07:57 < SageWWW> mvngu, what do you think Leif meant by a working subset of 
                 changes?
08:02 < mvngu> SageWWW: I think it's removing the 4-byte pointer constraint. 
               The working changes in the first diff now also work for 8-byte 
               pointers.
08:03 < SageWWW> It is still confusing.  Leif provided 4 patches total.
08:03 < mvngu> I know. You could ask for clarification on the ticket. 
08:03 < mvngu> Do you have an account on the trac server?
08:04 < SageWWW> I think you should modify your comment on the trac server to 
                 specifically state which of Leif's files corresponds to which 
                 of yours
08:04 < SageWWW> kevin.stueve
08:04 < mvngu> Let me modify the patches I have attached. Hang on...
```

I have deleted the previous 3 patches. In their place I attached 4 patches which correspond to the diff's contained in the attachments kevin.stueve. Starting from Silva.c.orig, apply the 4 patches in this order:

1. `01_Silva.patch`
2. `02_Silva.patch`
3. `03_Silva.patch`
4. `04_Silva.patch`
 
After applying the above four patches on top of Silva.c.orig, you get the file Silva.c. I hope my attachments would resolve some of the confusion.



---

archive/issue_comments_063960.json:
```json
{
    "body": "\n```\n08:57 < mvngu> So starting from Silva.c.orig, I applied Silva.c.diff0 which is \n               the same as 01_Silva.patch.\n08:59 < mvngu> Call the file with 01_Silva.patch applied \"Silva.c\".\n08:59 < mvngu> I then do a diff of Silva.c against the version of Silva.c in \n               Leif_attachment1.zip.\n09:00 < mvngu> That produce the patch file 02_Silva.patch.\n```\n",
    "created_at": "2009-12-24T17:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63960",
    "user": "mvngu"
}
```


```
08:57 < mvngu> So starting from Silva.c.orig, I applied Silva.c.diff0 which is 
               the same as 01_Silva.patch.
08:59 < mvngu> Call the file with 01_Silva.patch applied "Silva.c".
08:59 < mvngu> I then do a diff of Silva.c against the version of Silva.c in 
               Leif_attachment1.zip.
09:00 < mvngu> That produce the patch file 02_Silva.patch.
```




---

archive/issue_comments_063961.json:
```json
{
    "body": "One of the aspects of TOS's prime_sieve.c is that it has an initialization phase for an interval.  I'm not sure if the code already does this, but we should make sure to think about not repeating initialization more than needed.  Leif, I think you understand TOS's prime_sieve.c code better than me, what do you think?\n\nKevin Stueve",
    "created_at": "2009-12-26T03:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63961",
    "user": "kevin.stueve"
}
```

One of the aspects of TOS's prime_sieve.c is that it has an initialization phase for an interval.  I'm not sure if the code already does this, but we should make sure to think about not repeating initialization more than needed.  Leif, I think you understand TOS's prime_sieve.c code better than me, what do you think?

Kevin Stueve



---

archive/issue_comments_063962.json:
```json
{
    "body": "WARNING: Do not use the current version of \"Silva.c\" to count primes in intervals beyond approx. 18302910352e9 (assuming a sieve segment size of 2MB, i.e. _sieve_bits_log2_=24; with lower segment sizes, overflows occur later).\n\nUnfortunately, these early overflows do not lead to run-time errors (e.g. segmentation faults) but unsuspiciously wrong results.\n[\"Obvious\" (run-time) errors do occur much later due to other overflow conditions.]\n\nNote also that you currently must not use 1 as the interval's upper bound or (little worse) 2 as its lower bound, because prime counts will be wrong by one (1 is treated as prime while 2 is not).\n\nNevertheless, Happy New Decade...\n\n-Leif",
    "created_at": "2010-01-02T13:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63962",
    "user": "leif"
}
```

WARNING: Do not use the current version of "Silva.c" to count primes in intervals beyond approx. 18302910352e9 (assuming a sieve segment size of 2MB, i.e. _sieve_bits_log2_=24; with lower segment sizes, overflows occur later).

Unfortunately, these early overflows do not lead to run-time errors (e.g. segmentation faults) but unsuspiciously wrong results.
["Obvious" (run-time) errors do occur much later due to other overflow conditions.]

Note also that you currently must not use 1 as the interval's upper bound or (little worse) 2 as its lower bound, because prime counts will be wrong by one (1 is treated as prime while 2 is not).

Nevertheless, Happy New Decade...

-Leif



---

archive/issue_comments_063963.json:
```json
{
    "body": "I think I've now fixed all overflow conditions (I did find yet another one) such that it works up to 2<sup>64</sup>-1 under all circumstances.\n\nGoing to clean up the code and then perhaps release a final *stand-alone* version...\n\nThere's currently some overflow checking overhead which could be reduced for \"safe\" intervals but I'll most probably not remove it before writing a library version (which will be optimized for other special cases, too).\n\nAnyway, the improved version is faster than the original... :)",
    "created_at": "2010-01-05T15:32:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63963",
    "user": "leif"
}
```

I think I've now fixed all overflow conditions (I did find yet another one) such that it works up to 2<sup>64</sup>-1 under all circumstances.

Going to clean up the code and then perhaps release a final *stand-alone* version...

There's currently some overflow checking overhead which could be reduced for "safe" intervals but I'll most probably not remove it before writing a library version (which will be optimized for other special cases, too).

Anyway, the improved version is faster than the original... :)



---

archive/issue_comments_063964.json:
```json
{
    "body": "An initial portable version of LMOnew/findn runs on x86_64 in 64-bit native mode.\n\nNow going to extend its domain further up to 2<sup>64</sup>-1...\n\n[It could be helpful to have confirmed values of pi(x) between 1844e16 and 2<sup>64</sup>. Anyone?]\n\n-Leif",
    "created_at": "2010-01-10T17:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63964",
    "user": "leif"
}
```

An initial portable version of LMOnew/findn runs on x86_64 in 64-bit native mode.

Now going to extend its domain further up to 2<sup>64</sup>-1...

[It could be helpful to have confirmed values of pi(x) between 1844e16 and 2<sup>64</sup>. Anyone?]

-Leif



---

archive/issue_comments_063965.json:
```json
{
    "body": "Thomas R. Nicely's table of pi(x) at http://sage.math.washington.edu/home/kstueve/T_R_NICELY/ has a granularity of 1e10 up to 2e16.  So you really only need values between 2e16 and 2<sup>64</sup>.\nKevin Stueve",
    "created_at": "2010-01-10T21:18:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63965",
    "user": "kevin.stueve"
}
```

Thomas R. Nicely's table of pi(x) at http://sage.math.washington.edu/home/kstueve/T_R_NICELY/ has a granularity of 1e10 up to 2e16.  So you really only need values between 2e16 and 2<sup>64</sup>.
Kevin Stueve



---

archive/issue_comments_063966.json:
```json
{
    "body": "Correction: 1e10 or better",
    "created_at": "2010-01-10T21:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63966",
    "user": "kevin.stueve"
}
```

Correction: 1e10 or better



---

archive/issue_comments_063967.json:
```json
{
    "body": "Replying to [comment:12 kevin.stueve]:\n> So you really only need values between 2e16 and 2<sup>64</sup>.\n\nOnly? There was no decimal point missing in 1844... ;-)",
    "created_at": "2010-01-11T00:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63967",
    "user": "leif"
}
```

Replying to [comment:12 kevin.stueve]:
> So you really only need values between 2e16 and 2<sup>64</sup>.

Only? There was no decimal point missing in 1844... ;-)



---

archive/issue_comments_063968.json:
```json
{
    "body": "Sorry.  Right now you have the values:\n\n\n\nx                          pi(x)\n\n\n18440 00000 00000 00000 : 425 50425 77541 37607\n\n18446 74407 37095 51616 : 425 65628 40352 17743 \n\n18450 00000 00000 00000 : 425 72967 93423 72554\n\n\nfrom http://www.primefan.ru/stuff/primes/table.html and http://www.ieeta.pt/~tos/bib/5.4.pdf.\n\nYou could sieve part of this interval for more values.  You could contact one of the authors of one of the variants of combinatorial method asking for other values (Such as Gourdon, TOS, etc).\n\nAnother possibility is using a O(x<sup>1/2</sup> log(x)) algorithm that computes the parity (even or odd) of the prime counting function, for a limited amount of verification of values of the prime counting function.  This algorithm is described by Terence Tao and others at the polymath project at http://michaelnielsen.org/polymath1/index.php?title=Prime_counting_function\nand by Henri Lifchitz at\nhttp://web.archive.org/web/20070325064748/http://ourworld.compuserve.com/homepages/hlifchitz/Henri/us/ParPius.htm\n\n\n\nGourdon, an author of a variant of the combinatorial prime_pi method links to this page at http://numbers.computation.free.fr/Constants/Primes/countingPrimes.html, however Gourdon's link to Henri Lifchitz's page is dead and you have to use the wayback machine.  At Lifchitz's page is his paper on calculating the parity of prime_pi and a program that works up to (unfortunately only) 1e19, and seems to be a little slow.\n\n\n\nGourdon has a pix program released at http://numbers.computation.free.fr/Constants/Primes/Pix/contributepixtable.html that he used for his distributed pix project.  I'm not sure what range is allowed, how long computation takes, or if the code is open source.  But it *might* work for you.  There is also a table of 7702/9001 values of pi(x) computed in the range 1000e14 -> 10000e14 available from Gourdon's pix project at http://numbers.computation.free.fr/Constants/Primes/Pix/resultstable.php.  Not the range you were asking for, but still worth noting.  Take this data and program with a grain of salt- although Gourdon is surely a better programmer and mathematician than myself, he had to halt his pix program when he found his code was off by one in the global checks for prime_pi(10<sup>23</sup>)\n\n\n\nTOS will probably release more values of prime_pi up to 4e18 after his Golbach conjecture verification project is complete, but since these aren't in the range you need, I would recommend contacting Gourdon or TOS directly asking for values for verification.\n\n\n\nKevin Stueve",
    "created_at": "2010-01-11T02:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63968",
    "user": "kevin.stueve"
}
```

Sorry.  Right now you have the values:



x                          pi(x)


18440 00000 00000 00000 : 425 50425 77541 37607

18446 74407 37095 51616 : 425 65628 40352 17743 

18450 00000 00000 00000 : 425 72967 93423 72554


from http://www.primefan.ru/stuff/primes/table.html and http://www.ieeta.pt/~tos/bib/5.4.pdf.

You could sieve part of this interval for more values.  You could contact one of the authors of one of the variants of combinatorial method asking for other values (Such as Gourdon, TOS, etc).

Another possibility is using a O(x<sup>1/2</sup> log(x)) algorithm that computes the parity (even or odd) of the prime counting function, for a limited amount of verification of values of the prime counting function.  This algorithm is described by Terence Tao and others at the polymath project at http://michaelnielsen.org/polymath1/index.php?title=Prime_counting_function
and by Henri Lifchitz at
http://web.archive.org/web/20070325064748/http://ourworld.compuserve.com/homepages/hlifchitz/Henri/us/ParPius.htm



Gourdon, an author of a variant of the combinatorial prime_pi method links to this page at http://numbers.computation.free.fr/Constants/Primes/countingPrimes.html, however Gourdon's link to Henri Lifchitz's page is dead and you have to use the wayback machine.  At Lifchitz's page is his paper on calculating the parity of prime_pi and a program that works up to (unfortunately only) 1e19, and seems to be a little slow.



Gourdon has a pix program released at http://numbers.computation.free.fr/Constants/Primes/Pix/contributepixtable.html that he used for his distributed pix project.  I'm not sure what range is allowed, how long computation takes, or if the code is open source.  But it *might* work for you.  There is also a table of 7702/9001 values of pi(x) computed in the range 1000e14 -> 10000e14 available from Gourdon's pix project at http://numbers.computation.free.fr/Constants/Primes/Pix/resultstable.php.  Not the range you were asking for, but still worth noting.  Take this data and program with a grain of salt- although Gourdon is surely a better programmer and mathematician than myself, he had to halt his pix program when he found his code was off by one in the global checks for prime_pi(10<sup>23</sup>)



TOS will probably release more values of prime_pi up to 4e18 after his Golbach conjecture verification project is complete, but since these aren't in the range you need, I would recommend contacting Gourdon or TOS directly asking for values for verification.



Kevin Stueve



---

archive/issue_comments_063969.json:
```json
{
    "body": "Replying to [comment:11 leif]:\n> Now going to extend its domain further up to 2<sup>64</sup>-1...\n\n\n\n```\n\tpi(10000000000000000000)=234057667276344607\t# ok\n\tpi(10000100000000000000)=234059953037027338     # ok (sieved)\n\tpi(10001000000000000000)=234080524854508201\n\tpi(10002000000000000000)=234103382381000184\n\tpi(10003000000000000000)=234126239852389526\n\tpi(10004000000000000000)=234149097272730775\n\tpi(10005000000000000000)=234171954644081388\n\tpi(10006000000000000000)=234194811963658747\n\tpi(10007000000000000000)=234217669226973010\n\tpi(10008000000000000000)=234240526435037954\n\tpi(10009000000000000000)=234263383594121363\n\tpi(10010000000000000000)=234286240703110411\t# ok\n\tpi(18440000000000000000)=425504257754137607\t# ok\n\tpi(18441000000000000000)=425526800039801658\n\tpi(18442000000000000000)=425549342293840481\n\tpi(18443000000000000000)=425571884521908383\n\tpi(18444000000000000000)=425594426720237587\n\tpi(18445000000000000000)=425616968892901351\n\tpi(18446000000000000000)=425639511036514638\n\tpi(18446100000000000000)=425641765249620069\n\tpi(18446200000000000000)=425644019461402605\n\tpi(18446300000000000000)=425646273676018091\n\tpi(18446400000000000000)=425648527886817884\n\tpi(18446500000000000000)=425650782098479434\n\tpi(18446600000000000000)=425653036308859193\n\tpi(18446700000000000000)=425655290520421050\n\tpi(18446744073709551615)=425656284035217743\t# ok\n\n```\n\n\nHappy validating... ;-)\n\n*\"You just need a computer with a pentium or equivalent chip, turning on windows 95, 98 or NT. ...\"* [Xavier Gourdon about his \"fastpix11\"]\n\n(Still cleaning up the code.)\n\n-Leif",
    "created_at": "2010-01-15T04:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63969",
    "user": "leif"
}
```

Replying to [comment:11 leif]:
> Now going to extend its domain further up to 2<sup>64</sup>-1...



```
	pi(10000000000000000000)=234057667276344607	# ok
	pi(10000100000000000000)=234059953037027338     # ok (sieved)
	pi(10001000000000000000)=234080524854508201
	pi(10002000000000000000)=234103382381000184
	pi(10003000000000000000)=234126239852389526
	pi(10004000000000000000)=234149097272730775
	pi(10005000000000000000)=234171954644081388
	pi(10006000000000000000)=234194811963658747
	pi(10007000000000000000)=234217669226973010
	pi(10008000000000000000)=234240526435037954
	pi(10009000000000000000)=234263383594121363
	pi(10010000000000000000)=234286240703110411	# ok
	pi(18440000000000000000)=425504257754137607	# ok
	pi(18441000000000000000)=425526800039801658
	pi(18442000000000000000)=425549342293840481
	pi(18443000000000000000)=425571884521908383
	pi(18444000000000000000)=425594426720237587
	pi(18445000000000000000)=425616968892901351
	pi(18446000000000000000)=425639511036514638
	pi(18446100000000000000)=425641765249620069
	pi(18446200000000000000)=425644019461402605
	pi(18446300000000000000)=425646273676018091
	pi(18446400000000000000)=425648527886817884
	pi(18446500000000000000)=425650782098479434
	pi(18446600000000000000)=425653036308859193
	pi(18446700000000000000)=425655290520421050
	pi(18446744073709551615)=425656284035217743	# ok

```


Happy validating... ;-)

*"You just need a computer with a pentium or equivalent chip, turning on windows 95, 98 or NT. ..."* [Xavier Gourdon about his "fastpix11"]

(Still cleaning up the code.)

-Leif



---

archive/issue_comments_063970.json:
```json
{
    "body": "Important update:\n\"WARNING! The data for x = 6.5402\u00b710<sup>15</sup> and for x = 6.6808\u00b710<sup>15</sup> was incorrect before February 21, 2010.\"\nhttp://www.primefan.ru/stuff/primes/table.html\n\nWe need to check our data.",
    "created_at": "2010-03-03T11:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63970",
    "user": "kevin.stueve"
}
```

Important update:
"WARNING! The data for x = 6.5402·10<sup>15</sup> and for x = 6.6808·10<sup>15</sup> was incorrect before February 21, 2010."
http://www.primefan.ru/stuff/primes/table.html

We need to check our data.



---

archive/issue_comments_063971.json:
```json
{
    "body": "Considering that Kevin decided to go with primesieve over Silva's \"prime_sieve.c\", I think that it is appropriate to use this ticket to discuss the primesieve spkg (since the functionality is simply a superset of \"prime_sieve.c\").\n\nI've created an initial spkg, although for the moment implicitly assumes that gcc >= version 4.2.",
    "created_at": "2012-01-05T01:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63971",
    "user": "ohanar"
}
```

Considering that Kevin decided to go with primesieve over Silva's "prime_sieve.c", I think that it is appropriate to use this ticket to discuss the primesieve spkg (since the functionality is simply a superset of "prime_sieve.c").

I've created an initial spkg, although for the moment implicitly assumes that gcc >= version 4.2.



---

archive/issue_comments_063972.json:
```json
{
    "body": "I've worked on this a little, and have posted an updated spkg. Unfortunately there are some major issues with primesieve on big endian systems. I have added a patch that stops the vast majority of the segfaults, however, there is still the occasional segfault. Even without segfaulting, the library gives very incorrect values on big endian systems.\n\nI've also posted a few patches, one that provides a cython wrapper, and a couple that sets up the package as either standard or optional. All of these were based off of 5.0.prealpha1, so they may have some fuzz factors to them (especially the later two).",
    "created_at": "2012-01-22T15:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63972",
    "user": "ohanar"
}
```

I've worked on this a little, and have posted an updated spkg. Unfortunately there are some major issues with primesieve on big endian systems. I have added a patch that stops the vast majority of the segfaults, however, there is still the occasional segfault. Even without segfaulting, the library gives very incorrect values on big endian systems.

I've also posted a few patches, one that provides a cython wrapper, and a couple that sets up the package as either standard or optional. All of these were based off of 5.0.prealpha1, so they may have some fuzz factors to them (especially the later two).



---

archive/issue_comments_063973.json:
```json
{
    "body": "Attachment [primesieve-sage-root.patch](tarball://root/attachments/some-uuid/ticket7539/primesieve-sage-root.patch) by walki created at 2013-09-09 12:33:41\n\nIntegrates primesieve-4.4.spkg into sagemath",
    "created_at": "2013-09-09T12:33:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63973",
    "user": "walki"
}
```

Attachment [primesieve-sage-root.patch](tarball://root/attachments/some-uuid/ticket7539/primesieve-sage-root.patch) by walki created at 2013-09-09 12:33:41

Integrates primesieve-4.4.spkg into sagemath



---

archive/issue_comments_063974.json:
```json
{
    "body": "Attachment [primesieve-sage-main.patch](tarball://root/attachments/some-uuid/ticket7539/primesieve-sage-main.patch) by walki created at 2013-09-09 12:34:37\n\nInitial primesieve patch",
    "created_at": "2013-09-09T12:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63974",
    "user": "walki"
}
```

Attachment [primesieve-sage-main.patch](tarball://root/attachments/some-uuid/ticket7539/primesieve-sage-main.patch) by walki created at 2013-09-09 12:34:37

Initial primesieve patch



---

archive/issue_comments_063975.json:
```json
{
    "body": "I have attached the two patches 'primesieve-sage-root.patch' and '02_primesieve-sage-main.patch' to this ticket, the corresponding spkg package can be downloaded from https://primesieve.googlecode.com/files/primesieve-4.4.spkg. These patches integrate primesieve-4.4 into sage-5.12.beta4. The patches include a Cython wrapper around the ParallelPrimeSieve C++ API (by default single-threaded due to #12690) and improvements to the prime_range() and primes_first_n() functions. These patches were written by Andrew Ohana and myself.\n\nRegards,\n\nKim Walisch",
    "created_at": "2013-09-09T13:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63975",
    "user": "walki"
}
```

I have attached the two patches 'primesieve-sage-root.patch' and '02_primesieve-sage-main.patch' to this ticket, the corresponding spkg package can be downloaded from https://primesieve.googlecode.com/files/primesieve-4.4.spkg. These patches integrate primesieve-4.4 into sage-5.12.beta4. The patches include a Cython wrapper around the ParallelPrimeSieve C++ API (by default single-threaded due to #12690) and improvements to the prime_range() and primes_first_n() functions. These patches were written by Andrew Ohana and myself.

Regards,

Kim Walisch



---

archive/issue_comments_063976.json:
```json
{
    "body": "The previous version had indentation errors in the file fast_arith.pyx.",
    "created_at": "2013-09-09T19:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63976",
    "user": "walki"
}
```

The previous version had indentation errors in the file fast_arith.pyx.



---

archive/issue_comments_063977.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-09-10T03:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63977",
    "user": "ohanar"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063978.json:
```json
{
    "body": "Attachment [02_primesieve-sage-main.patch](tarball://root/attachments/some-uuid/ticket7539/02_primesieve-sage-main.patch) by ohanar created at 2013-09-10 03:42:57\n\nI've reviewed this code while Kim was writing it, so other than the following questions/concerns, it has a positive review from me.\n\n1. What is our policy with licencing files in the Sage library. This patch adds two files which are marked as BSD licensed, is this ok? (given that the Sage library as a whole is GPL licensed)\n2. What is the current policy on adding new standard SPKGs? At some point it was decided that all new SPKGs had to be optional before they were made standard, but this requirement has been repeatedly ignored.\n3. Would it make sense stripping out the directory src/src/apps/gui? This would reduce the size of the spkg by over half.\n\nP.S. Kim, would you please update the list of developers on trac's homepage so people know who you are.",
    "created_at": "2013-09-10T03:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63978",
    "user": "ohanar"
}
```

Attachment [02_primesieve-sage-main.patch](tarball://root/attachments/some-uuid/ticket7539/02_primesieve-sage-main.patch) by ohanar created at 2013-09-10 03:42:57

I've reviewed this code while Kim was writing it, so other than the following questions/concerns, it has a positive review from me.

1. What is our policy with licencing files in the Sage library. This patch adds two files which are marked as BSD licensed, is this ok? (given that the Sage library as a whole is GPL licensed)
2. What is the current policy on adding new standard SPKGs? At some point it was decided that all new SPKGs had to be optional before they were made standard, but this requirement has been repeatedly ignored.
3. Would it make sense stripping out the directory src/src/apps/gui? This would reduce the size of the spkg by over half.

P.S. Kim, would you please update the list of developers on trac's homepage so people know who you are.



---

archive/issue_comments_063979.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2013-09-10T03:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63979",
    "user": "ohanar"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_063980.json:
```json
{
    "body": "> 1. This patch adds two files which are marked as BSD licensed, is this ok? ...\n\n\nNo, it cannot be BSD licensed as primesieve.pyx includes Sage headers that are GPL licensed. I relicensed the primesieve.pyx and primesieve.pxd files to GPL. The corresponding patch is 03_primesieve-sage-main.patch.\n\n\n\n> 2. What is the current policy on adding new standard SPKGs? ...\n\n\nSlightly off topic: primesieve is highly portable, its Makefile is Posix compatible and primesieve builds without any issues on Linux, Mac OS X, BSD and Cygwin and runs on both little and big endian CPUs. Also primesieve has no dependencies on other libraries.\n\n\n\n> 3. Would it make sense stripping out the directory src/src/apps/gui? This would reduce the size of the spkg by over half.\n\n\nYes, this makes sense. On the other hand the size of the compressed spkg package is only 120 kilobytes and removing this directory makes packaging new primesieve releases a little more difficult.",
    "created_at": "2013-09-10T08:37:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63980",
    "user": "walki"
}
```

> 1. This patch adds two files which are marked as BSD licensed, is this ok? ...


No, it cannot be BSD licensed as primesieve.pyx includes Sage headers that are GPL licensed. I relicensed the primesieve.pyx and primesieve.pxd files to GPL. The corresponding patch is 03_primesieve-sage-main.patch.



> 2. What is the current policy on adding new standard SPKGs? ...


Slightly off topic: primesieve is highly portable, its Makefile is Posix compatible and primesieve builds without any issues on Linux, Mac OS X, BSD and Cygwin and runs on both little and big endian CPUs. Also primesieve has no dependencies on other libraries.



> 3. Would it make sense stripping out the directory src/src/apps/gui? This would reduce the size of the spkg by over half.


Yes, this makes sense. On the other hand the size of the compressed spkg package is only 120 kilobytes and removing this directory makes packaging new primesieve releases a little more difficult.



---

archive/issue_comments_063981.json:
```json
{
    "body": "Same as 02_primesieve-sage-main.patch but uses GPL instead of BSD license.",
    "created_at": "2013-09-10T08:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63981",
    "user": "walki"
}
```

Same as 02_primesieve-sage-main.patch but uses GPL instead of BSD license.



---

archive/issue_comments_063982.json:
```json
{
    "body": "Attachment [03_primesieve-sage-main.patch](tarball://root/attachments/some-uuid/ticket7539/03_primesieve-sage-main.patch) by vbraun_spam created at 2014-01-30 21:20:52",
    "created_at": "2014-01-30T21:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63982",
    "user": "vbraun_spam"
}
```

Attachment [03_primesieve-sage-main.patch](tarball://root/attachments/some-uuid/ticket7539/03_primesieve-sage-main.patch) by vbraun_spam created at 2014-01-30 21:20:52



---

archive/issue_comments_063983.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2021-12-02T00:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63983",
    "user": "mkoeppe"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_063984.json:
```json
{
    "body": "Happening now in #25009.",
    "created_at": "2021-12-02T00:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63984",
    "user": "mkoeppe"
}
```

Happening now in #25009.



---

archive/issue_comments_063985.json:
```json
{
    "body": "Collective apologies to Kim Walisch for allowing this to bitrot.\nBut primecount spkg is coming up on #25009.",
    "created_at": "2021-12-02T11:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63985",
    "user": "dimpase"
}
```

Collective apologies to Kim Walisch for allowing this to bitrot.
But primecount spkg is coming up on #25009.



---

archive/issue_comments_063986.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-12-02T11:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63986",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063987.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-12-03T18:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7539#issuecomment-63987",
    "user": "mkoeppe"
}
```

Resolution: invalid
