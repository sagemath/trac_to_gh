# Issue 7013: prime_pi and nth_prime

Issue created by migration from Trac.

Original creator: kevin.stueve

Original creation time: 2009-09-25 10:26:36

Assignee: kevin.stueve

CC:  was robertwb georgsweber kevin.stueve ohanar victor leif

Keywords: primes, sieve, table,LMO

Computes the prime counting and nth prime function.  This is my first Sage contribution.


---

Comment by kevin.stueve created at 2009-09-25 10:33:05

Replying to [ticket:7013 kevin.stueve]:
> Computes the prime counting and nth prime function.  This is my first Sage contribution.
7013 is a prime number.  What are the odds of that, 11%?


---

Comment by GeorgSWeber created at 2009-09-27 06:49:31

Hi Kevin,

you posted a *.lzma-compressed file. On my Mac, neither 7-zip installs out of the box (seems to be MS Windows-only, see http://www.7-zip.org/), nor do I intend to install DarwinPorts or Fink, which contain packages to unpack such files, nor did I find some standalone *.dmg for OS X by googling some minutes around. So I'm unable to unpack this file on my computer.

Sorry, but that's a problem of your patch, not of my system installation. Patches in trac are supposed to be created by hg/mercurial and to apply seamlessly to Sage, or you should provide a link (!) to some file in *.spkg format, or both. Did you read the respective parts of the "Sage Programming Guide", by the way?

From what you write in the sage-devel thread ("Be sure to use the -m32 option when compiling the c code ...") it seems that (some C part of) your code lacks anyway build scripts that work "out of the box" on each of the platforms supported by Sage. For a start, have a look at the "Cliquer.spkg" already in Sage, or at the "Frobby.spkg", not yet in Sage due to build problems on Solaris (see trac ticket #6416), in case your C code is rather "external" to the Sage library.

On the other hand, if your code is intended to "go directly into the Sage library", you need anyway to tell the then-necessary Cython bridge how to compile your code correctly (see module_list.py). And probably some database integration, if I understand correctly what you want to do.

Better still, drop the necessity of "-m32" by using, in your code, fixed-sized C types like "uint32_t" from (ISO/ANSI C99) stdlib.h (wich exists even for msvc, although provided by third parties), and not plain "int"/"long"/... if your algorithm depends on that. But without being able to even have a single look at your code, I'll stop here.

And please, please, don't post MB-sized compressed files into trac itself, but rather post links to some accessible webspace instead. I did that myself for one of my first patches for Sage, and got pretty washed my head (see trac ticket #4857, if you want to), the file itself being erased from trac by the admin almost immediately ... (the reason is that trac is best used "text-based", and any compressed blob has to remain in there for eternity, which is bad for both size-archive-backup issues, and performance).

Heads up! ;-)


Cheers,
Georg


---

Comment by robertwb created at 2009-09-27 07:24:14

I figured since I've talked to you about this I could at least take a pass at refereeing your code, but was unable to decompress and look at it as well...

FYI, I posted the attached file at http://sage.math.washington.edu/home/robertwb/tmp/KevinStueve.tar.lzma and removed it from trac.


---

Comment by kevin.stueve created at 2009-09-27 10:13:51

Replying to [ticket:7013 kevin.stueve]:
> Computes the prime counting and nth prime function.  This is my first Sage contribution.
> 
> http://sage.math.washington.edu/home/robertwb/tmp/KevinStueve.tar.lzma


---

Comment by kevin.stueve created at 2009-09-27 10:53:43

GeorgSWeber, I don't currently use Windows.  I made the lzma file on Ubuntu.  I am currently unable to single-handedly make build scripts for my code, because I don't have access to systems with every possible operating system on which Sage might be run.  Someone with access to different environments could help with the build script for their platform.

Note: On 64bit Ubuntu on an Acer I get the following with Silva's code without using -m32 and installing special packages for 32bit mode.  Can anyone see how to make this better?
static void *get_memory(u32 size)
{
 u32 m;

 line 100:m = (u32)malloc(size + 255); // this assumes that
sizeof(void *) = sizeof(u32)
 line 101:if((void *)m == NULL)
   exit(1);
 m = (m + 255) & ~255;
 line 104:return (void *)m; // pointer aligned on a 256 byte boundary
}

~/Documents/Silva$ bash compile
Silva.c: In function ‘get_memory’:
Silva.c:100: warning: cast from pointer to integer of different size
Silva.c:101: warning: cast to pointer from integer of different size
Silva.c:104: warning: cast to pointer from integer of different size
~/Documents/Silva$ ./Silva
Segmentation fault

Please note that the Silva c and LMO c code work fine without any special compiler options or libraries on a MacBookPro.  The Silva c code works on 64bit Ubuntu when the proper -m32 compiler option is specified and a library is installed that allows 32 bit mode (just Google the error you get without it).  The LMO c code on 64 bit Ubuntu I believe requires the -m32 flag and additional libraries for 32 bit mode.

Currently, my Python code calls Silva's code and the LMO code from the command line using the subprocess module.

Kevin Stueve


---

Comment by GeorgSWeber created at 2009-09-27 14:50:39

Hi Kevin,

I won't be able to respond on a daily basis because I'm quite busy right now. But concerning the above code snippet, one might use the ANSI C99 type "uintptr_t" instead, since you obviously want to cast pointer values to integer values back and forth. (I can't judge right now, whether you really must do this, but that's another topic.)

Using "uintptr_t" would also very benefical in light of portability to native Windows 64bit. Sage will not be able to support this platform (well, any Windows platform) for a while, but it is a goal definitely on the road map.

Since on 64 bit platforms (e.g. on OS X 10.6, Ubuntu, Fedora, Suse, ...) we need to build Sage with "-m64", and it is not a good idea to mix "-m32" and "-m64", we should try hard to smooth this out of the code itself.

Cheers, Georg


---

Comment by was created at 2009-09-28 19:19:21

The code here implements what is the worlds fastest general purpose prime_pi for a practical range of numbers -- it's much faster than Mathematica, or anything else available in general purpose software.  However, it is really mainly a first very rough draft, in that it still hardcodes explicitly paths, etc., and will need to be completely gone over by an experienced Sage developer.  That said, all the really *hard work* that requires specialized knowledge about number theory has already been done.  What's left is a lot of work that requires basically nothing except a good knowledge of Python and Sage.


---

Comment by was created at 2009-09-28 19:21:15

And Kevin is willing that somebody who does the above gets to be co-author of this code.


---

Comment by GeorgSWeber created at 2009-09-28 20:40:49

Silva's code states explicitly (line 25):

```
//
// Assumptions: pointers have 4 bytes, gcc compiler
//
```

(the first of which is plainly wrong on 64-bit systems), and has a one-line "compile" shell script as build system. The LMO code seems to have been blessed with some early version of autotools, oh well. The "optimized Legendre code from Andrew Ohana" seems to be missing. All these C code "command line programs" should go into a separate spkg. (At least this is what I learned from Michael Abshoff.)

I assume that the "800 lines of code" William refers to in the fifth (or so) post to the sage-devel thread "are" the file "clean_prime_pi.py". I agree that one should look over it line-by-line (e.g. line 145 is *not* safe w.r.t. endian-ness), but I there's a bit more work to do ...


---

Comment by kevin.stueve created at 2009-09-30 02:46:52

Andrew Ohana's prime_pi is the one currently in Sage.  Yes, clean_prime_pi.py is the code to look at.  The other files in the zip are earlier versions of my code (including me experimenting with single/dual core etc).
By line 145 did you mean
    byte3=inputfile.read(1)      in the get_table_pi function?
Note that the get_table_pi function in its current state is designed only for when Li(x)-pi(x) (which is positive for all x<10**316 (see http://en.wikipedia.org/wiki/Skewes%27_number and the included article link (Patrick Demichel. The prime counting function and related subjects) that I just fixed so it wasn't a dead link), so we don't need to worry about storing negatives) fits in three bytes base 256, so if larger values are desired, the table must be expanded to use four bytes in such cases.  Li(x)-pi(x) exceeds 256**3 somewhere between 10**17 and 10**18 (see http://en.wikipedia.org/wiki/Prime-counting_function).
I look forward to seeing how the code is improved and made more safe/clean/robust.


---

Comment by GeorgSWeber created at 2009-10-06 22:02:56

Hi Kevin,

to continue, we firstly need some fundamental design decisions.

As I understand it (please correct me, if I'm wrong), your code resp. its functionality depends on C code written by T. Oliveira e Silva. (BTW, I like the original name "prime_sieve.c" as given on "http://www.ieeta.pt/~tos/software/prime_sieve.html" better than "Silva.c".) This is only one rather small C file, but nevertheless --- Sage is written in Python/Cython, not C. Currently, you compile this C code into an executable, which is called more or less directly from the command line (piping input and output). To include this C code (resp. its functionality) into Sage, I see (at least) four options:

1.) Keep the interfacing via commandline call --- this would mean that we need to stick this code into its own spkg

2.) Make a shared/dynamic library out of the C code, sitting in/installed by its own spkg, and write a small Cython wrapper, that links this library in --- interfacing is no longer done via command line, but via function call

3.) Write a small Cython wrapper, in order to interface via function call, and stick the bulk of the C code into the corresponding Cython extension (via "module_list.py" magic) as an external C file

4.) Rewrite it completely in Cython

Once this decision is made for the prime sieve C code of T. Oliveira e Silva, it has to be made again for the Lagarias-Miller-Odlyzko "lmonew" parts from Victor Miller, which also are written in plain C. If a new spkg is created at all, it also could be placed there (either as another standalone executable to be compiled, or as another library). But one could use a step-by-step approach, leaving "lmonew" out in the first shot, and include it back only later, as an update.

All four options are valid. The main decision is, whether we want to create a new Sage spkg out of (parts of) the C code (options 1 and 2), or not (options 3 and 4). I definitely think William should make this decision (he has started and supervised this prime_pi stuff, and is the Sage BDFL anyway) --- poke him about that.

Cheers, Georg


---

Comment by ohanar created at 2009-11-23 10:05:42

I have posted a patch, the prime tables need to be placed in SAGE_ROOT/data/prime_pi_tables, I have them at [http://sage.math.washington.edu/home/ohanar/prime_pi/prime_pi_tables.tar](http://sage.math.washington.edu/home/ohanar/prime_pi/prime_pi_tables.tar)

A few things that need to be resolved still:

1.) I have not been able to fix the LMO code to compile across platforms (currently not included in the patch), we need to decide whether we want to include this code or cap at `10**16`.

2.) The li_approx file is still included, Kevin I am not sure what method is being used in it, but if we can use the sage Li function, that would be preferable.

3.) The Silva code has been renamed back to prime_sieve.c, it has compiled across all platforms I have tested, but definitely more testing is needed for it. Also, it is presently in sage.functions, it would be more useful (and better placed) as a library, the code included can easily be extended to replace prime_range, if someone wants to do this, or can point me to a good reference as to how to create one, let me know.

4.) The docstrings and header content need to be worked on, if anyone has any comments on this, let me know, I have mainly focused on getting the code to run, so I will complete try to fill this out later on.

Take care,
Andrew


---

Attachment

Rough first patch


---

Comment by GeorgSWeber created at 2009-11-24 22:45:27

I'm glad that things are moving on!

Technically, there are various open points, e.g. the line 105 of the modified da Silva code

```
m = (unsigned long) malloc(size + 255); // this assumes that sizeof(void *) = sizeof(u32) 
```

still looks suspicious to me w.r.t. 64bit platforms, since there, sizeof(void *) usually is sizeof(u64). It might be benefical to do something like

```
m = calloc(size/(64*sizeof(void *)), 64*sizeof(void *))
```

and we haven't even discussed the memory leakage question yet, since all this "bucket" memory is never explicitly freed again ... (important if we want to use the code as a library). Let alone "exit 1;" (line 107) in case of memory shortage being suboptimal in a Sage subroutine.

OTOH, having read the "rough first patch", and thinking about it, I guess we can't avoid creating a new spkg. It would be the optimal solution anyway, no doubt about that, but currently I have no idea how the data/prime_pi_tables/ could be handled otherwise in any clean way. (Of course we could stick them too under sage/functions/, including them into "Manifest.in", and so on, but I see this as a last resort only before this work comes to a halt.) Last, but not least, the spkg way is "the" way to make a library out of the da Silva "prime_sieve" functionality. How to create such a library/spkg? It's probably easiest I just do it and say "look and see", before trying to explain it in lengthy terms.

William recently has set up quite strict rules for the inclusion of new spkgs, especially that there are to be individuals that are willing to maintain these for the next one to two years, say. I cannot do that alone, but might volunteer to be part of a team doing it. Anybody joining to form a tag team? Let me know.

Cheers,
Georg


---

Comment by kevin.stueve created at 2009-11-25 03:28:14

Write-up of project


---

Attachment

Andrew (ohanar),

I obtained the li_approx code via a personal communication (email) from Fredrik Johansson, owner of the mpmath project.  It computes an approximation to the logarithmic integral using an asymptotic series.  You can also find it described at

http://en.wikipedia.org/wiki/Logarithmic_integral_function#Asymptotic_expansion

I first used the Sage Li function, but switched to this one because it is orders of magnitude faster.  The Sage Li function spends unnecessary cycles calculating Li out to many decimal places.  For this application, we can stop at the decimal point, because we only need an approximation.  Note that the calculation of an exact value of li would probably use the series representation of li rather than the asymptotic series.

http://en.wikipedia.org/wiki/Logarithmic_integral_function#Series_representation

For large computations, the difference in time between Li and li_approx is negligible compared to the total computation time.  However, for small computations, the saved time could be the limiting factor in the time complexity of this algorithm.  This is especially apparent when generating the tables.  Because speed is one of the most important factors in this program, I strongly advocate keeping li_approx rather than using Sage's exact Li.  IMHO,the simplicity of calling a preexisting library function simply does not outweigh the time trade-off of using the asymptotic series.  If anything, I would want some sort of fast li_approx to be made a permanent part of the Sage function library, as it would be useful for number theory research.  If using exist parts of the Sage library is desired over using new code, it might be possible to optimize small prime_pi calculations to not depend on li, but I see this as very unnecessary extra work.

If the sage-devel team decides that they want to use Li for its simplicity over the asymptotic series provided by Fredrik Johansson (actually in any case), I would like to stress the importance of using the same prime_pi approximation function (whether li_exact or li_approx) when generating the tables and when using them.  It is absolutely critical that every detail, including but not limited to rounding versus truncating and what the last included term of the series is is exactly the same in both calculations (generating the table and using it).

For everyone involved I would like to mention to be careful about confusing the logarithmic integral and offset logarithmic integral.

For everyone to read, here is a link to my writeup (I also created an attachment):

http://www.wstein.org/projects/stueve.pdf

After the code is added to Sage, I intend to submit the paper (most likely with revisions/additions) for publication.  As Andrew is taking part in the development of the code and sharing authorship, I believe it would be appropriate for myself, Andrew Ohana, and William Stein to share authorship of both the code added to Sage and the paper submitted for publication.

Kevin Stueve


---

Comment by ohanar created at 2009-11-25 21:45:33

Kevin,

I agree that the built in Li function is slower, my tests:

Built in Li:

```
sage: timeit('prime_pi(10**16)')
625 loops, best of 3: 809 µs per loop
sage: time prime_pi(10**16-10**10)
CPU times: user 56.95 s, sys: 0.42 s, total: 57.37 s
Wall time: 57.41 s
279238071526960
```


Using li_approx:

```
sage: timeit('prime_pi(10**16)')
625 loops, best of 3: 22.3 µs per loop
sage: time prime_pi(10**16-10**10)
CPU times: user 57.10 s, sys: 0.40 s, total: 57.50 s
Wall time: 57.54 s
279238071948684
```


I don't know if the li_approx is necessary, while for certain values we have a magnitude of difference in complexity, we still are running fast enough, and the values where time actually matters changing to Li has little effect. We would need to fix the offset, but that shouldn't change the runtime noticeably. If you still want to use a li_approx, I would suggest creating a li module, and include arbitrary digit precision.



George,

 
I am not very familiar with C, I know that on most platforms `sizeof(long) == sizeof(void *)`, but I don't believe this is true on all platforms, so we might want to check the declaration of `m` as well. I'm unsure what your comment on the tables was all about, to me SAGE_ROOT/data seemed to be the most appropriate place to put them. Given my relatively limited knowledge of C, I would be hesitant to join a maintenance team, but placing prime_sieve into a spkg is clearly ideal, so if I am needed I can join (although, I don't know how much help I would be).

Take care,
Andrew


---

Comment by kevin.stueve created at 2009-11-26 02:27:26

Andrew,

First of all, great work on the patch Andrew.  You have done good work, and it is nice to have the code in Cython now.  I am glad to share this project with you.  I am looking forward to working more

But I have an issue with removing the fast Li approximation.

The use of fast Li approximation function for this program is absolutely essential.  I am very strongly opposed to switching out the Li approximation for the slower built-in exact Li as it will severely impact its average case time complexity.

You say that the cases where Li's speed matter do not affect average case time complexity.  Computing average case time complexity is difficult because it requires that you define a probability distribution over the possible inputs.

If the probability distribution is uniform, meaning that any input is just as likely, then most of the input will be large numbers.  For an average large value of x (say a random 12 digit number), the li calculation takes up a very negligible fraction of the total computation time of prime_pi.

I believe that a uniform distribution in the logarithmic domain is a more accurate model of input probabilities.  In modeling average case time complexity, I would assume that 1, 2, 3, 4, ..etc digit numbers have equal probabilities of being input in the program.

For small values of x (say only a few digits long), the li calculation could represent the majority of the calculation time (where only minimal or no sieving is needed).

When average case time complexity is modeled using the more realistic logarithmic model, the performance of prime_pi on smaller values is not negligible, and could represent a significant fraction of expected input.

I see no logical reason to take code that has been painstakingly optimized for speed and make it up to 40 times slower for a significant percentage of its expected input.

After this prime_pi and nth_prime are formally added to Sage, I would like to create a graph of its performance for a set of random 1, 2, 3, 4... etc digit numbers (and compare the performance to other implementations of the prime counting function).  I really, really don't want the section of the graph representing numbers less than 5 digits to be up to 40 times slower than it could have been because of an unfounded prejudice against the asymptotic series for the logarithmic integral (which was written by an expert in coding arithmetic functions and is well documented and known by the mathematics community).

Math/Programming is war.  Every cycle of speed is fought for.  Don't give it up.

Why would I want to use arbitrary precision arithmetic to calculate an approximation that is desired to be as fast as possible (maybe you are just advocating that the desired accuracy be a parameter)?  I don't believe that the asymptotic series lends itself to error analysis or arbitrary precision.  It is simply a fast way to calculate an approximation.  And I think that the asymptotic series is preferable here to the series representation (with specified precision) because of speed issues.

If I am going to make a Li module, with the exact li, an arbitrary precision li, a specified precision li, and a fast asymptotic series li, then I am going to need some assistance from someone who has more experience than myself at making Sage patches (any takers?).

A would also like to mention track ticket 7017 at this time (prime range problem).  Ticket 7017 should help making plots of prime_pi.

Sincerely,
your friend,
Kevin Stueve


---

Comment by kevin.stueve created at 2009-11-26 08:10:14

I noticed on line 506 of "sage/functions/prime_pi.pyx" in the patch that prime_pi(x) is capped at x=2**61 (2.30584301 × 10**18).  This is okay if the LMO code is used for the largest values of x.  However, without the LMO code being called in such cases, the table/sieving prime_pi will start to return incorrect values as soon as the li(x)-pi(x) values don't fit within three bytes (somewhere between 10**17 and 10**18, see my above post on this issue I made two months ago).
The options are:
-cap the allowed values of x so that li(x)-pi(x) will never exceed three bytes of space
 -modify the table to allow more than three bytes of storage when necessary
 -incorporate the LMO code for large values of x


---

Comment by robertwb created at 2009-11-26 08:19:08

There should be no need to assume that sizeof(long) == sizeof(void*), and I think the code should be fixed to remove this assumption. However, I agree with Kevin that the optimized approximation to li is worth keeping and using, and we don't have to make a whole Li module to get this patch in.


---

Comment by kevin.stueve created at 2009-11-26 19:34:11

Andrew,

I would again like to praise you for your great work on this program.  You have done a good job at converting the code from Python to Cython (which improves the speed of the non-c parts of the program), improving the style of the code, and integrating table/sieving prime_pi and nth prime with the rest of Sage in a patch.

The parallel processing code I implemented has been removed.

I think it would be very well worth the effort to re-implement parallel processing code.  Dual core processors are common today.  Quad and greater numbers of cores are becoming more common.  As it is becoming harder to make components on a silicon chip smaller and faster (clock-rate), the semiconductor industry has partially responded by making more cores per chip.  It is reasonable to assume that in the foreseeable future this trend will continue and many more cores will be available than are now.

I believe that the almost 2-times speedup offered by parallel processing on dual core machines is worth the extra coding effort.  This is even more true for quad and greater numbers of cores.  Companies spend great amounts of money and time to make their programs just 10% faster.  An algorithm which is trivially parallelizable such as sieving is rare.  Every such opportunity for improvement should be given the utmost attention.

In any project it is important to look toward the future and what technology will be available.  Let's look at the future of multi-core processors.

"Intel's researchers have produced a research prototype 80-core chip that uses less energy than a quad-core processor and has teraflop performance capabilities.
It expects to be able to produce a chip with 80 cores in five to eight years."
Intel builds 80-core chip
EE Times, Jan. 16, 2007
http://www.eetimes.com/news/latest/showArticle.jhtml;?articleID=196901229

"Chinese researchers have unveiled details of Godson-3, a scalable microprocessor with four cores (work in parallel) that they hope will bring personal computing to most ordinary people in China by 2010, with an eight-core version in development."
A Chinese Challenge to Intel
Technology Review, Sep. 1, 2008
http://www.technologyreview.com/Infotech/21322/?a=f

"Intel Larrabee to have 32 cores, ship in 2010"
May 15th, 2009
http://blogs.zdnet.com/gadgetreviews/?p=4336

The opportunity to almost double or quadruple the speed of a program is enough to implement multiprocessing.  But when Intel's road-map includes a 32 core chip in 2010 and an 80 core chip a few years away, it becomes absolutely ridiculous not to implement multiprocessing.

I spent a lot of time and effort optimizing the use of multiprocessing.  I did benchmarking to determine at what point the time savings from multiprocessing outweighs the overhead needed.  This is time sacrificed that I could have spent doing many other things.

Now I find that my multiprocessing code has been removed.  It is not my responsibility to put it back in.  I already put it in once.

Let me remind you that the purpose of this project is the fastest possible implementation of the prime counting function.  Let's not miss a large factor of difference (that will grow exponentially as the years go by) from neglecting a few lines of trivial multiprocessing code.

Sincerely,
your friend,
Kevin Stueve


---

Comment by GeorgSWeber created at 2009-11-26 21:17:35

I'll try to cool down things by addressing several independent issues in independent messages.


---

Comment by GeorgSWeber created at 2009-11-26 21:53:58

Let's start to create a "primes.p0.spkg" (better names appreciated ...) which provides the "prime_sieve.c" code/functionality as a library.

Primary goal: The function "primes_interval()" is accessible from a dynamic library "libprimes.so" resp. "libprimes.dll", which in turn compiles (and works) on the platforms Sage supports, and actually is being a part of some future version of Sage.

Secondary goal: This spkg also provides some precomputed tables (which in a Sage installation will be installed under "data/prime_pi_tables/").

Tertiary goal: Provide the LMO code/functionality from Victor Miller in the same way, too. 

I opened up a new ticket for this, #7539. The work on that ticket #7539 is more or less an exercise in software engineering, and does hardly interfere with the remaining work on this ticket here.


---

Comment by GeorgSWeber created at 2009-11-26 21:57:48

My comment from two months ago about an endianness issue (... (e.g. line 145 is *not* safe w.r.t. endian-ness) ...) now seems to me as being nonsense. Just forget about that.


---

Comment by GeorgSWeber created at 2009-11-26 22:09:45

I'd vote to change the tables (and the algorithms) such that each entry is four Bytes (instead of three) in size. The uncompressed tables currently are 3 MB, probably they would grow to 4 MB by this change. So what. They could be read out as u32 values on the mainstream platforms, and on platforms with the other endianness, the speed-regression would be marginal.

The big gain is that (as I understand it) we don't need to cap at 10^^16, but only (far?!?) later, if the LMO code is not available.


---

Comment by GeorgSWeber created at 2009-11-26 22:11:04

Oops, 10**16, not 1016 ... it seems not all characters are allowed.


---

Comment by GeorgSWeber created at 2009-11-26 22:16:59

To answer one other question:

Where does the content from "data/" come from? Well, each subdirectory there is copied over from some spkg, e.g. the "data/extcode/" subdirectory from the "extcode-4.3.alpha0.spkg".

So we need to decide from which spkg the tables shall be copied to "data/prime_pi_tables/", and I think the spkg at #7539 is a good place for that. I don't know of any other "good" place; I certainly consider the Sage library itself as a being a bad place for that.


---

Comment by GeorgSWeber created at 2009-11-26 22:26:10

I admit I haven't looked at the "parallel processing" parts of the code. But my feeling is we should proceed step-by-step now, i.e. integrate into Sage some first version, and after that, (re-)add functionality/goodies that had to be postponed in the course of doing so.

For now, AFAIK, postponed topics are the integration (as a choice) of the Legendre code from Andrew, the LMO code, and the parallel processing ability.


---

Comment by GeorgSWeber created at 2009-11-26 22:37:16

Finally, I admit myself to post one off-topic message.

My diploma thesis from 1997 was about the Odlyzko bounds for algebraic number fields. A main part dealt with the so-called "explicit formulae", see e.g. chapters three and four in S. Patterson, "An introduction to the Riemann zeta-function", Cambridge studies in advanced mathematics; 14.

Until I read your writeup, I didn't knew about the What is Riemann's Hypothesis? (Draft) 
from Barry Mazur and William --- the fourth version of the formulations of the RH (in their counting) is intimately related to the "explicit formulae" and their applications.
And of course to Li, prime counting, and so on ...


---

Comment by kevin.stueve created at 2009-11-27 08:16:02

Replying to [comment:27 GeorgSWeber]:
> I admit I haven't looked at the "parallel processing" parts of the code. But my feeling is we should proceed step-by-step now, i.e. integrate into Sage some first version, and after that, (re-)add functionality/goodies that had to be postponed in the course of doing so.
> 
> For now, AFAIK, postponed topics are the integration (as a choice) of the Legendre code from Andrew, the LMO code, and the parallel processing ability.

One piece of functionality that I would like to suggest (either for myself or anyone else interested in it) to add after everything else is done is a cache of previous results used to optimize later calculations (instead of just the previous result as is the case now).  For example if you calculate the nth prime (and obtain x), a later calculation of the (n-10)-th prime, or of prime_pi(x+205) would use this result to reduce the necessary calculation.  The cache might be some sort of tree where you can obtain a nearby previously calculated value.  It would be necessary to keep a queue of the order that cached values were used, so that the oldest could be thrown out when the alloted storage is consumed and a new value is to be stored in the queue.  It would probably be a good idea to have some way of not caching many values that are excessively close together, so it might be necessary to keeps track of the statistics of how close together the values in the cache are to determine when it is worth it to cache a value. Maybe this cache could even be stored to disk.

Kevin Stueve


---

Comment by kevin.stueve created at 2009-11-27 11:33:27

Replying to [comment:27 GeorgSWeber]:
> I admit I haven't looked at the "parallel processing" parts of the code. But my feeling is we should proceed step-by-step now, i.e. integrate into Sage some first version, and after that, (re-)add functionality/goodies that had to be postponed in the course of doing so.
> 
> For now, AFAIK, postponed topics are the integration (as a choice) of the Legendre code from Andrew, the LMO code, and the parallel processing ability.

Another possible improvement after everything else is done is making every table query not require file io.  Perhaps the first time one of the table files is queried, that entire table could be loaded into RAM as an array.  I don't think the several MB of RAM needed would be excessive.

Kevin Stueve


---

Comment by kevin.stueve created at 2009-11-27 12:07:56

Replying to [comment:28 GeorgSWeber]:
> Finally, I admit myself to post one off-topic message.
> 
> My diploma thesis from 1997 was about the Odlyzko bounds for algebraic number fields. A main part dealt with the so-called "explicit formulae", see e.g. chapters three and four in S. Patterson, "An introduction to the Riemann zeta-function", Cambridge studies in advanced mathematics; 14.
> 
> Until I read your writeup, I didn't knew about the What is Riemann's Hypothesis? (Draft) 
> from Barry Mazur and William --- the fourth version of the formulations of the RH (in their counting) is intimately related to the "explicit formulae" and their applications.
> And of course to Li, prime counting, and so on ...

Thanks!  I just purchased that book from Amazon.  What does the 14 represent?  Is it a page number?  Do you have an electronic copy of your 1997 thesis?  I did a Google search and wasn't able to find it.

Kevin Stueve


---

Comment by robertwb created at 2009-11-27 22:26:11

Perhaps it could be viewed as an enhancement, but if we packed the tables into 4-byte chunks it would probably compress nearly as small, and we could use memory mapped numpy arrays. This would both be a cleaner interface to the table, and gracefully handle caching issues, etc. transparently.


---

Comment by kevin.stueve created at 2009-12-26 03:18:18

I think that in the final version, we should give the user the option of using either is_prime or is_pseudo_prime.  is_pseudo_prime may be faster, and is believed to always be valid (for numbers in our range), but because its validity is not proven, the user should be able to choose is_prime.

Kevin Stueve


---

Comment by leif created at 2010-01-12 16:48:05

Do we have a supreme court decision whether to use Li() or Li_approx() (of course for the generation *and* the look-up)?

What about the width of the stored offsets?
32 bits for all tables or just for those where the deviation from pi() exceeds 24 bits?

-Leif


---

Comment by kevin.stueve created at 2010-01-13 12:32:22

I would suggest using an approximation to R(x), the Riemann prime counting function described at http://mathworld.wolfram.com/RiemannPrimeCountingFunction.html, if a fast approximation (R_approx()) can be written (perhaps a Taylor or asymptotic series?), and li_approx otherwise.  The 10% or so storage savings should be worthwhile, especially if larger tables will become available.  Alternatively, some sort of a piecewise shifted li_approx fit could be used (meaning we start with li_approx and shift it by a pre-calculated amount in different intervals), probably obtaining accuracy similar to R() or R_approx().  I agree with the always 32 bit suggestion, as this should not affect the compression considerably, and will make the code simpler.  Another space optimization to consider, especially with denser tables, is storing the number of primes in an interval (or the offset from an estimate of this from Li() or R()) instead of the prime counting function.  This may also save 10% or so in storage.  Storing the number of primes in bins is what Andrew Booker does on the UTM "nth prime page".


Kevin Stueve


---

Comment by leif created at 2010-01-13 18:06:12

I would not even bother storing 16-byte pairs of (n,pi(n)), or preferably (n,nth_prime) because it is injective, in plain (uncompressed) binary format.
The whole range up to 2<sup>64</sup> at steps of 10<sup>9</sup> fits on a (DL-)DVD, and sieving a whole interval (worst case) with 10<sup>9</sup> primes today takes at most a few minutes. (With a step size of 10<sup>10</sup>, the table would fit on a CD, 10<sup>11</sup> would be about 65MB and so on. The tables should compress well for shipping because of the monotonicity.)

But we are yet far away from having such dense (and complete) tables, though I expect (wishful thinking?) the 64-bit range to be fully sieved within the next 5-10 years.
Regarding that, it would at my opinion be better to use a format that allows the tables to be successively updated (i.e. extended) with "arbitrary" intermediate values, until they one day are complete (and can be indexed directly rather than binary-searched).

As Kevin stated, harddisks get larger and cheaper, bandwidth continuously grows... Since the tables should be optional anyway (and they are still quite small), I think we shouldn't be too much concerned about file sizes. [Admins, take mercy on me...]

Of course we could support (and provide) both types of tables and let the user choose which one is more appropriate to him (or her).

-Leif


---

Comment by kevin.stueve created at 2010-01-28 08:27:47


```
First some timings:
from math import log

timeit( 'Li(10**15)')
125 loops, best of 3: 7.34 ms per loop

#R from http://wstein.org/rh/rh/code/code.sage
timeit('R(10**15)') #with prec 100
625 loops, best of 3: 218 µs per loop

timeit('li_approx(10**15)')
625 loops, best of 3: 200 µs per loop

timeit( 'log(10**15)')
625 loops, best of 3: 10.7 µs per loop

I have some email correspondence to relay below.  Thank you so much
to everyone who contributed below.  Every suggestion and idea was
incredibly valuable!

Sincerely,
Kevin Stueve

"The equation 13 [http://mathworld.wolfram.com/RiemannPrimeCountingFunction.html](http://mathworld.wolfram.com/RiemannPrimeCountingFunction.html)
you mentioned is PROBABLY wrong: check Andrey V. Kulsha'
post of 11/18/2008 entitled "On the explicit formula for the Prime-counting
function pi(x)" on the NMBRTHRY`@`LISTSERV.NODAK.EDU list. To me, it seems
far better to compress the pi(x) data using simply pi(x)=li(x)-e(x). Instead
of storing pi(x) you would store the (positive) value of e(x) rounded to the
nearest integer. Note that li(x) can be computed easily and that e(x) should
be of the order of sqrt(x). Replacing li(x) by R(x) would not help much,
because the error term could be either positive or negative (one more bit).
Using a few zeros of the zeta function could reduce the error term, but my
experience is that it would take much more time to compute the approximation
(it would be necessary to evaluate $li(x^rho)$ accurately, and also
pi(sqrt(x)), pi(cbrt(x)), etc.)." TOS (Tomás Oliveira e Silva, http://www.ieeta.pt/~tos/index.html)
(My experiments lead me to believe that storing R (sometimes called Ri)
offsets will save at least 6% (with .tar.bz2) in table size over li
offsets (with .tar.bz2).)

"lzma gives sometimes significantly better compression than bzip" TOS
Unfortunately, lzma is not part of Sage.

"I see a potential problem with the approach described above [storing li(x) offsets]. What if li(x)
evaluates to INTEGER.4999999999 or to INTEGER.500000001? Can it be assured
that the same evaluation on a different architecture/compiler/operating system
gives exactly the same result? This problem would be amplified in R(x) and
some zeros of the zeta function are used. Assuming that the error of evaluating
li(x) is smaller than, say, 0.1, the above problems can be solved by storing
the rounded value of e(x) AND storing also the last two bits of pi(x), i.e.,
storing  4 * round(e(x)) + (pi(x) mod 4)."  TOS
(One of the li (approximation) implementations we are considering is a fast asymptotic series, which
is truncated when the terms stop decreasing.  I am now fearful that a slight machine
difference could cause an extra term or one less term to be included
causing the value to unacceptably change.)

"Knowing the last bit of pi(x) is enough if the floating point error
  is smaller than 0.5 (round to the nearest even or to the nearest odd
  integer, respectively if pi(x) mod 2 = 0 or pi(x) mod 2 = 1)" TOS

"If many pi(x) values are present in the database, why not split it in
  reasonably sized chunks and then encode the data in a differential form?
  I.e., store x1 and pi(x1), then store x2-x1 and pi(x2)-pi(x1), etc.
  Note that pi(x2)-pi(x1) would be close to (x2-x1)/log(x2), so the difference
  between the two should be stored instead (together with the last bit of
  pi(x2)). This may perhaps give smaller correction terms than using
  R(x) or more sofisticated approximations. The price to pay would be that
  the database entries would depend on all previous one of the same chunk.
  The advantages: with suitable modifications it could also be used to
  compress pi2(x) data, and the required computations are very simple." TOS
(This [differential coding in reasonably sized chunks] is a much better idea
than the tree structure I was suggesting.  I believe AB's index idea is equivalent
to having chunks.  However, we don't need to store
the values of x if the spacing is preset.  I tried storing the offsets between
pi(x2)-pi(x1) and (x2-x1)/log(x2).  With tar.bz2 compression, the table space
was less than 0.55% more than storing offsets between pi(x2)-pi(x1) and 
R(x2)-R(x1)!  Within small intervals, the PNT (prime number theorem) estimate
is nearly identical to R (what great insight from TOS!).  The PNT estimate can be
calculated 18 times faster than li_approx or R, and 685 times faster than Sage's
Li.  If any sort of analytic approximation is going to be used for Sage's
prime_pi tables, it is the method described above!!!!!, along with the parity bit
of pi(x2)-pi(x1) to guard against potential machine dependent rounding issues.
I tried taking diffs of the above described offsets (i.e. one more order of differences than TOS suggested), and under tar.bz2, the table
space increased.  That the method TOS described could easily be extended to
twin primes is an extra bonus.)

"One of these days I will dump my entire pi(x) and pi2(x) database in a
  ASCII format and then I will let you know where you can fetch it. It has
  many more entries than those available on my web site." TOS
I can't wait!

"As it happens, I have been thinking for a while about updating the nth
prime page to reflect the capabilities of modern hardware, but have
been too lazy to do the computations myself.  I'll describe what I
have in mind; let me know if you or others in the group might be
interested in pursuing it. " AB (Andrew Booker, 
http://www.maths.bris.ac.uk/people/faculty/maarb/)

"In an ideal world, the spacing of entries around a number x in the
precomputed table should be proportional to sqrt(x), since that is the
minimum running time of the sieve of Eratosthenes.  Thus, for a table
that works up to 10^18, one would want table entries spaced every 10^9
at least.  In fact the obvious choice would be to store a table of
pi(t_n), where t_n is the nth triangular number n(n+1)/2.  That would
give an algorithm that runs in best possible time when using the sieve
of Eratosthenes.  (To be clear on this point, there are faster
algorithms than the standard sieve for primality testing a short
interval; e.g., Galway's algorithm runs in time O(x^{1/3}), and for
very short intervals one would prefer to use a standalone primality
test on each number in the interval.  However, I think that the above
strategy coupled with a heavily optimized standard sieve would be the
ideal tradeoff of running time and table storage in practice.)  This
would mean storing on the order of 1.4*10^9 numbers, which is nothing
for a modern hard drive (though obviously too much to distribute with
sage; I'm thinking more of the nth prime page where it would be stored
centrally on a server)." AB
(I like the idea of storing triangular, square, and oblong numbers so that
the computation time increases smoothly and so variants of Landau's third
problem, Legendre's conjecture can be easily studied.  However I think that
storing multiples of powers of ten is the most practical option, because lots
of analysis will only need equally spaced values of the prime counting function.
I would like to see both types of tables.  Larger tables can be used at the nth
prime page and in the online version of Sage, as well as possibly being shipped
on optical media.)

"This has other advantages as well.  For instance, it obviates the need
to compute Li(x) for compression; with a regularly spaced table like
pi(t_n), one gets the same compression simply by storing differences
between consecutive values, plus an index at the beginning for faster
searching.  (Even better is to store second differences.  In fact
that's what I did for the original nth prime page; there the bulk of
the table consists of 2-byte integers, even though the numbers go up
to 10^12.)" AB
(Yes, when the difference between the number of primes in one block and
the next is stored instead of the number of primes in a block, the space
used is less than 4% more than TOS's PNT offset idea (taking a diff of a
higher order hurts compression).  However, I did not
take into account the cost of storing the parity bits in TOS's PNT offset idea
in my analysis.  An extra bit for a million table entries should add 125,000
bytes of virtually incompressible data, making AB's second order difference
idea preferable, at least as far as my vote goes.  It is so amazing that out of all the possible algorithms to calculate pi(x), the fastest is to use an exponentially
large table of values calculated with brute force sieving.  Even more amazing
is that out of all the analytic approximations and formulas, the best way to
compress that table of values of pi(x) seems to be simply storing differences.
Yes, there are probably ways to only store parity bits when an offset is very
near a rounding point, but that would involve significant coding effort and
the risk of a coding error or misunderstanding of how floating point arithmetic
works causing incorrect errors would be absolutely unacceptable in my opinion.
Absolutely, the first priority of this project is to not return false values.  All else,
running times, table space, input ranges are negotiable.)

"Anyway, I propose a project to compute pi(t_n) for all t_n up to
10^18.  Unfortunately that means sieving up to 10^18, which is not
easy.  But it's certainly possible, since it has been done already by
TOS et al.  In fact it could probably be done in less than a year on a
cluster of reasonable size.  You could then take whatever fraction of
the values you wanted for distribution with sage (and again I think
that storing second differences would give compression nearly as good
as the Li(x) trick, but with only integer arithmetic).  What do you
think?" AB
I can't wait for tables to be available for that interval and much larger ones.
A 100 million core exaflop computer may be available by 2018!

Following is an email exchange between Victor Miller and Hugh Montgomery
regarding the distribution of the remainder pi(x) - Li(x) that was forwarded to me.

victor miller wrote:

    Hugh, Do you know of results about the distribution of the remainder pi(x) - Li(x) (assuming RH)?  In particular if one wanted to store remainders like this for various random values of x if one knew the distribution (which I would expect is certainly not uniform) then one could use various data compression techniques that depend on knowing the distribution to save at least a constant factor.

    Victor

    PS. One could of course try to throw in a few terms corresponding to the first few zeros of zeta(s) but I would think that, in practical terms, you might not gain very much.

Dear Victor:

   Unconditionally one cannot say much about this error term, because we don't even
know its order of magnitude.  Assume RH.  Then pi - li does not have a limiting distribution
because its general size is growing.  So consider

                                         pi(x) - Li(x)
                                      ------------------- .
                                      x^{1/2}/log x

This will generally lie between -1.25 and -0.75, but even this does not have a limiting
distribution.  The point is that its wobbles become slower and slower, so that
for any given order of magnitude, the quantity is almost constant.  What is needed
is an exponential change of variable.  Put

                                      f(y) = (psi(e^y) - e^y)/e^{y/2}.

Aurel Wintner showed that (on RH) this has a limiting distribution.  If one wanted
to use data to get an idea of this distribution, it would be difficult to get very many
independent data points, due to the exponential increase of the argument.  If one assumes
that the ordinates gamma > 0 of the zeros of zeta(s) are linearly independent over the
rationals, then the terms e^{i*gamma*y} act like independent random variables, and
one can develop approximations to the distribution function of f.  The distribution function
is even, its density is everywhere positive, and tends to zero rapidly (almost doubly-
exponentially) at infinity.  For each gamma > 0, let X_gamma be a random variable
uniformly distributed on [0,1], and suppose that the X_gamma are independent.  Then
the limiting distribution of f (assuming RH & the linear independence of the gamma)
is the same as for the random variable

                                 2 sum_{gamma > 0} (sin 2*Pi*X_gamma)/|rho| .

Here rho = 1/2+i*gamma.  One could sample this variable at random points to
develop an approximation to the distribution function of f.

                                                      Cheers,
                                                                   Hugh
```



---

Comment by kevin.stueve created at 2010-01-28 08:30:04

I'm sorry that that's so hard to read.  How do I clean it up?


---

Comment by leif created at 2010-01-28 19:42:25

*For those who can't rotate their wide-screen display: * ;-)

First some timings:

```
from math import log

timeit( 'Li(10**15)')
125 loops, best of 3: 7.34 ms per loop

#R from http://wstein.org/rh/rh/code/code.sage
timeit('R(10**15)') #with prec 100
625 loops, best of 3: 218 µs per loop

timeit('li_approx(10**15)')
625 loops, best of 3: 200 µs per loop

timeit( 'log(10**15)')
625 loops, best of 3: 10.7 µs per loop
```

I have some email correspondence to relay below.  Thank you so much
to everyone who contributed below.  Every suggestion and idea was
incredibly valuable!

Sincerely,
Kevin Stueve


  "The equation 13 [http://mathworld.wolfram.com/RiemannPrimeCountingFunction.html](http://mathworld.wolfram.com/RiemannPrimeCountingFunction.html)
  you mentioned is PROBABLY wrong: check Andrey V. Kulsha's post of 11/18/2008 entitled ''"On the explicit formula for the Prime-counting
  function pi(x)"'' on the !NMBRTHRY`@`LISTSERV.NODAK.EDU list (http://listserv.nodak.edu/cgi-bin/wa.exe?A2=ind0811&L=nmbrthry&T=0&F=&S=&P=839). To me, it seems
  far better to compress the pi(x) data using simply pi(x)=li(x)-e(x). Instead
  of storing pi(x) you would store the (positive) value of e(x) rounded to the
  nearest integer. Note that li(x) can be computed easily and that e(x) should
  be of the order of sqrt(x). Replacing li(x) by R(x) would not help much,
  because the error term could be either positive or negative (one more bit).
  Using a few zeros of the zeta function could reduce the error term, but my
  experience is that it would take much more time to compute the approximation
  (it would be necessary to evaluate li(x<sup>rho</sup>) accurately, and also
  pi(sqrt(x)), pi(cbrt(x)), etc.)."

  TOS (Tomás Oliveira e Silva, http://www.ieeta.pt/~tos/index.html)

(My experiments lead me to believe that storing R (sometimes called Ri)
offsets will save at least 6% (with .tar.bz2) in table size over li
offsets (with .tar.bz2).)


  "lzma gives sometimes significantly better compression than bzip"

  TOS

Unfortunately, lzma is not part of Sage.


  "I see a potential problem with the approach described above [storing li(x) offsets]. What if li(x)
  evaluates to INTEGER.4999999999 or to INTEGER.500000001? Can it be assured
  that the same evaluation on a different architecture/compiler/operating system
  gives exactly the same result? This problem would be amplified in R(x) and
  some zeros of the zeta function are used. Assuming that the error of evaluating
  li(x) is smaller than, say, 0.1, the above problems can be solved by storing
  the rounded value of e(x) AND storing also the last two bits of pi(x), i.e.,
  storing  4 * round(e(x)) + (pi(x) mod 4)."

  TOS

(One of the li (approximation) implementations we are considering is a fast asymptotic series, which
is truncated when the terms stop decreasing.  I am now fearful that a slight machine
difference could cause an extra term or one less term to be included
causing the value to unacceptably change.)

  "Knowing the last bit of pi(x) is enough if the floating point error
  is smaller than 0.5 (round to the nearest even or to the nearest odd
  integer, respectively if pi(x) mod 2 = 0 or pi(x) mod 2 = 1)"

  TOS

  "If many pi(x) values are present in the database, why not split it in
  reasonably sized chunks and then encode the data in a differential form?
  I.e., store x1 and pi(x1), then store x2-x1 and pi(x2)-pi(x1), etc.
  Note that pi(x2)-pi(x1) would be close to (x2-x1)/log(x2), so the difference
  between the two should be stored instead (together with the last bit of
  pi(x2)). This may perhaps give smaller correction terms than using
  R(x) or more sofisticated approximations. The price to pay would be that
  the database entries would depend on all previous one of the same chunk.
  The advantages: with suitable modifications it could also be used to
  compress pi2(x) data, and the required computations are very simple."

  TOS

(This [differential coding in reasonably sized chunks] is a much better idea
than the tree structure I was suggesting.  I believe AB's index idea is equivalent
to having chunks.  However, we don't need to store
the values of x if the spacing is preset.  I tried storing the offsets between
pi(x2)-pi(x1) and (x2-x1)/log(x2).  With tar.bz2 compression, the table space
was less than 0.55% more than storing offsets between pi(x2)-pi(x1) and 
R(x2)-R(x1)!  Within small intervals, the PNT (prime number theorem) estimate
is nearly identical to R (what great insight from TOS!).  The PNT estimate can be
calculated 18 times faster than li_approx or R, and 685 times faster than Sage's
Li.  If any sort of analytic approximation is going to be used for Sage's
prime_pi tables, it is the method described above!!!!!, along with the parity bit
of pi(x2)-pi(x1) to guard against potential machine dependent rounding issues.
I tried taking diffs of the above described offsets (i.e. one more order of
differences than TOS suggested), and under tar.bz2, the table space increased.
That the method TOS described could easily be extended to twin primes is an extra bonus.)


  "One of these days I will dump my entire pi(x) and pi2(x) database in a
  ASCII format and then I will let you know where you can fetch it. It has
  many more entries than those available on my web site."

  TOS

I can't wait!


  "As it happens, I have been thinking for a while about updating the nth
  prime page to reflect the capabilities of modern hardware, but have
  been too lazy to do the computations myself.  I'll describe what I
  have in mind; let me know if you or others in the group might be
  interested in pursuing it. "

  AB (Andrew Booker, http://www.maths.bris.ac.uk/people/faculty/maarb/)

  "In an ideal world, the spacing of entries around a number x in the
  precomputed table should be proportional to sqrt(x), since that is the
  minimum running time of the sieve of Eratosthenes.  Thus, for a table
  that works up to 10<sup>18</sup>, one would want table entries spaced every 10<sup>9</sup>
  at least.  In fact the obvious choice would be to store a table of
  pi(t<sub>n</sub>), where t<sub>n</sub> is the nth triangular number n(n+1)/2.  That would
  give an algorithm that runs in best possible time when using the sieve
  of Eratosthenes.  (To be clear on this point, there are faster
  algorithms than the standard sieve for primality testing a short
  interval; e.g., Galway's algorithm runs in time O(x<sup>1/3</sup>), and for
  very short intervals one would prefer to use a standalone primality
  test on each number in the interval.  However, I think that the above
  strategy coupled with a heavily optimized standard sieve would be the
  ideal tradeoff of running time and table storage in practice.)  This
  would mean storing on the order of 1.4*10<sup>9</sup> numbers, which is nothing
  for a modern hard drive (though obviously too much to distribute with
  sage; I'm thinking more of the nth prime page where it would be stored
  centrally on a server)."

  AB

(I like the idea of storing triangular, square, and oblong numbers so that
the computation time increases smoothly and so variants of Landau's third
problem, Legendre's conjecture can be easily studied.  However I think that
storing multiples of powers of ten is the most practical option, because lots
of analysis will only need equally spaced values of the prime counting function.
I would like to see both types of tables.  Larger tables can be used at the nth
prime page and in the online version of Sage, as well as possibly being shipped
on optical media.)


  "This has other advantages as well.  For instance, it obviates the need
  to compute Li(x) for compression; with a regularly spaced table like
  pi(t<sub>n</sub>), one gets the same compression simply by storing differences
  between consecutive values, plus an index at the beginning for faster
  searching.  (Even better is to store second differences.  In fact
  that's what I did for the original nth prime page; there the bulk of
  the table consists of 2-byte integers, even though the numbers go up
  to 10<sup>12</sup>.)"

  AB

(Yes, when the difference between the number of primes in one block and
the next is stored instead of the number of primes in a block, the space
used is less than 4% more than TOS's PNT offset idea (taking a diff of a
higher order hurts compression).  However, I did not
take into account the cost of storing the parity bits in TOS's PNT offset idea
in my analysis.  An extra bit for a million table entries should add 125,000
bytes of virtually incompressible data, making AB's second order difference
idea preferable, at least as far as my vote goes.  It is so amazing that out of all
the possible algorithms to calculate pi(x), the fastest is to use an exponentially
large table of values calculated with brute force sieving.  Even more amazing
is that out of all the analytic approximations and formulas, the best way to
compress that table of values of pi(x) seems to be simply storing differences.
Yes, there are probably ways to only store parity bits when an offset is very
near a rounding point, but that would involve significant coding effort and
the risk of a coding error or misunderstanding of how floating point arithmetic
works causing incorrect errors would be absolutely unacceptable in my opinion.
Absolutely, the first priority of this project is to not return false values.
All else, running times, table space, input ranges are negotiable.)


  "Anyway, I propose a project to compute pi(t<sub>n</sub>) for all t<sub>n</sub> up to
  10<sup>18</sup>.  Unfortunately that means sieving up to 10<sup>18</sup>, which is not
  easy.  But it's certainly possible, since it has been done already by
  TOS et al.  In fact it could probably be done in less than a year on a
  cluster of reasonable size.  You could then take whatever fraction of
  the values you wanted for distribution with sage (and again I think
  that storing second differences would give compression nearly as good
  as the Li(x) trick, but with only integer arithmetic).  What do you
  think?"

  AB

I can't wait for tables to be available for that interval and much larger ones.
A 100 million core exaflop computer may be available by 2018!


Following is an email exchange between Victor Miller and Hugh Montgomery
regarding the distribution of the remainder pi(x) - Li(x) that was forwarded to me.

Victor Miller wrote:

  Hugh, Do you know of results about the distribution of the remainder pi(x) - Li(x) (assuming RH)?
  In particular if one wanted to store remainders like this for various random values of x if one
  knew the distribution (which I would expect is certainly not uniform) then one could use various
  data compression techniques that depend on knowing the distribution to save at least a constant factor.

  Victor

  PS. One could of course try to throw in a few terms corresponding to the first few zeros of zeta(s)
  but I would think that, in practical terms, you might not gain very much.

Hugh Montgomery replied:

  Dear Victor:

  Unconditionally one cannot say much about this error term, because we don't even
  know its order of magnitude.  Assume RH.  Then pi - li does not have a limiting distribution
  because its general size is growing.  So consider

                         ( pi(x) - Li(x) ) / ( x<sup>1/2</sup>/log x )

  This will generally lie between -1.25 and -0.75, but even this does not have a limiting
  distribution.  The point is that its wobbles become slower and slower, so that
  for any given order of magnitude, the quantity is almost constant.  What is needed
  is an exponential change of variable.  Put

                         f(y) = (psi(e<sup>y</sup>) - e<sup>y</sup>)/e<sup>y/2</sup>.

  Aurel Wintner showed that (on RH) this has a limiting distribution.  If one wanted
  to use data to get an idea of this distribution, it would be difficult to get very many
  independent data points, due to the exponential increase of the argument.  If one assumes
  that the ordinates gamma > 0 of the zeros of zeta(s) are linearly independent over the
  rationals, then the terms e<sup>i*gamma*y</sup> act like independent random variables, and
  one can develop approximations to the distribution function of f.  The distribution function
  is even, its density is everywhere positive, and tends to zero rapidly (almost doubly-
  exponentially) at infinity.  For each gamma > 0, let X<sub>gamma</sub> be a random variable
  uniformly distributed on ![0,1], and suppose that the X<sub>gamma</sub> are independent.  Then
  the limiting distribution of f (assuming RH & the linear independence of the gamma)
  is the same as for the random variable

                                 2 SUM,,gamma > 0,, (sin 2*Pi*X<sub>gamma</sub>)/|rho| .

  Here rho = 1/2+i*gamma.  One could sample this variable at random points to
  develop an approximation to the distribution function of f.

  Cheers,
  Hugh

*All content by Kevin*, just reformatted by me.
Editing recently posted comments is *really* missing in trac.

-Leif


---

Comment by kevin.stueve created at 2010-02-04 04:10:28

I have an idea to use MD5 hash to detect machine rounding differences in the table compression, which combines several of our ideas. Store offsets/differences/whatever (either for values, intervals, or whatever the method is) without regard for rounding errors or storing parity bits. But store the MD5 hash of either the entire table, or chunks of it. Do a one time unpacking of either the entire table or chunks of it, and at this time, compare the stored MD5 hash against the MD5 hash of the unpacked table. It is not necessary for the hash to be cryptographically secure, because we are only checking file integrity. If the MD5 hash values do not match, display a fatal error message, describing that the system has unexpected floating point properties, and that a (larger) table that does not depend on floating point needs to be downloaded, with instructions/link (or perhaps tries to download it automatically, with permission to access the Internet). Even if this idea doesn't make it into Sage's production prime_pi, it would be useful for a demo of the compression that would result from using the Riemann correction terms (see #8135).  For an idea of the compression possible, see Patrick Demichel's "The prime counting function and related subjects" (link at bottom of wikipedia's Skewes' number page).

Kevin Stueve


---

Comment by kevin.stueve created at 2010-02-08 03:48:40

I think that whatever sort of table is used, it needs to have a header that specifies the format.  That way if we change the table format, what table is present can easily be detected.  Perhaps a descriptive filename would be sufficient.


---

Comment by leif created at 2010-02-08 04:20:11

Replying to [comment:44 kevin.stueve]:
> I think that whatever sort of table is used, it needs to have a header that specifies the format.

Yes. For any sort of _binary_ file, I was thinking of just reserving the first 1024 bytes, which should be enough space for various information.
Such _fixed-size_ header can easily be [partially] skipped if the program does not implement the latest file [header] format version.
We could even use this convention for text files, and start each file with a zero-terminated short ASCII string, s.t. 

```
user`@`machine~/somewhere$ head some_file_of_unknown_format
```

gives a machine- *and* human-understandable brief description (at least of its type and file format version).


---

Comment by leif created at 2010-02-08 04:30:06

Of course this fixed size of the header is simply added anywhere we compute file offsets into the real data.


---

Comment by kevin.stueve created at 2010-03-22 02:06:47

I updated our prime counting code to use denser tables from TOS, TRN, and Kulsha, and an updated version of TOS's prime_sieve.c from Leif.  Consider my Python code still a rough draft.  I haven't tested it.  It would be nice to see this code get finalized, polished, peer reviewed, and implemented in the online version of Sage and also provided as an optional package for the downloaded version of Sage.

Right now the interval [1e14,1e15] has spacing 1e10.  It would be nice, and not too difficult to sieve this interval with prime_sieve.c on Sagemath with spacing 1e9.  This would be good to compare against Andrew Booker's new data he is going to calculate.
http://sage.math.washington.edu/home/kstueve/uploads/March21_2010/TableBasedPrimePi.zip

Kevin Stueve


---

Comment by leif created at 2010-03-22 14:58:26

Replying to [comment:47 kevin.stueve]:
> I updated our prime counting code to use denser tables from TOS, TRN, and Kulsha, and an updated version of TOS's prime_sieve.c from Leif.

Note that this version of `prime_sieve.c` is outdated (and btw, it should be called `prime_pi_sieve_tos.c`).

I hope I can provide a slightly polished version of the latest (Jan 2010, with optimizations, all overflow conditions I'm aware of - see #7539 - fixed) within this week.


> Right now the interval [1e14,1e15] has spacing 1e10.  It would be nice, and not too difficult to sieve this interval with prime_sieve.c on Sagemath with spacing 1e9.  This would be good to compare against Andrew Booker's new data he is going to calculate.

Regarding the current density in other ranges, I'd consider this rather a waste of time and space; even with - nowadays suboptimal - LMO, it takes only a few seconds to compute pi(x) in that range.

Above 10<sup>19</sup> we have a spacing of 10<sup>16</sup>, which is far too sparse; I'm currently computing pi(N*10<sup>15</sup>) for N>10000 (hopefully up to N=18446, i.e. 2<sup>64</sup>, but this will take months...).


> http://sage.math.washington.edu/home/kstueve/uploads/March21_2010/TableBasedPrimePi.zip

*Please* separate the data from the code... ;-)


-Leif


---

Comment by leif created at 2010-03-22 15:01:53

(Unintended modification of description reverted; trac... 8/ )


---

Comment by kevin.stueve created at 2010-03-22 23:09:57

Replying to [comment:48 leif]:
> Replying to [comment:47 kevin.stueve]:
> > I updated our prime counting code to use denser tables from TOS, TRN, and Kulsha, and an updated version of TOS's prime_sieve.c from Leif.
> 
> Note that this version of `prime_sieve.c` is outdated (and btw, it should be called `prime_pi_sieve_tos.c`).
> 
> I hope I can provide a slightly polished version of the latest (Jan 2010, with optimizations, all overflow conditions I'm aware of - see #7539 - fixed) within this week.
I thought that I included your latest version.  Maybe I messed up.  =)  Please add a descriptive docstring with authors and changes to your new post.  Thanks again for your work.  =)
> 
> 
> > Right now the interval [1e14,1e15] has spacing 1e10.  It would be nice, and not too difficult to sieve this interval with prime_sieve.c on Sagemath with spacing 1e9.  This would be good to compare against Andrew Booker's new data he is going to calculate.
> 
> Regarding the current density in other ranges, I'd consider this rather a waste of time and space; even with - nowadays suboptimal - LMO, it takes only a few seconds to compute pi(x) in that range.
I disagree with you on that point. 1e14(1e9)1e15 would be very useful. Personally I would like much denser data. =)
> 
> Above 10<sup>19</sup> we have a spacing of 10<sup>16</sup>, which is far too sparse; I'm currently computing pi(N*10<sup>15</sup>) for N>10000 (hopefully up to N=18446, i.e. 2<sup>64</sup>, but this will take months...).
If you can tell me where the program is, I would like to sieve 1e14(1e9)1e15.  Why not store much denser data than 1e19(1e15)2<sup>64</sup>?  Why not store 1e19(1e9)2<sup>64</sup>?  Why not start at 0 (it would only add a fraction to the computation time) and fill a 1TB drive with the densest counts possible?  If the cost of the sieving is the bottleneck, requiring months of computer time, it might be worthwhile to invest in even larger storage media.  The data in my latest upload were the results of a decade of work of TRN and 350 years of computation time by TOS, including time on Kracken, one of the fastest supercomputers in the world.  Every time you want denser data, you have to sieve your entire interval again.  If expensive supercomputer time and months or years of computation are involved, I think it makes much more sense to invest a fraction of your computation cost in larger storage, and then store denser counts than you would ever think anyone would need.
> 
> 
> > http://sage.math.washington.edu/home/kstueve/uploads/March21_2010/TableBasedPrimePi.zip
> 
> *Please* separate the data from the code... ;-)
> 
> 
> -Leif


---

Comment by leif created at 2010-03-24 16:40:57

Replying to [comment:50 kevin.stueve]:
> Why not store much denser data than 1e19(1e15)2<sup>64</sup>?  Why not store 1e19(1e9)2<sup>64</sup>?

:D If I was able to _sieve_ such a large interval in reasonable time, I wouldn't mind storing terabytes of data (including more than just pi(x)).

I think the primary goal should be getting denser tables in the whole 64-bit range, s.t. the average time for arbitrary values drops down significantly.
This can be accompanied by sieving "from scratch" while recording more information if we have the resources to do so.
But the current situation is that we have large "holes" in our tables that make the combinatorial method outperform table look-up and sieving by orders of magnitude (though taking even "too long" from a user's perspective, i.e. up to _hours_).

Computing pi(N*10<sup>15</sup>) for N>10000 is just a _first step_, perhaps followed by computing pi(N*10<sup>14</sup>) where these values are missing, and so on, until - _perhaps large-scale distributed_ - _sieving_ the remaining smaller intervals beats individually computing lots of values in them. Anyway, having data points independently computed with other methods is always good, and a prerequisite for validating results computed only once.

-Leif


---

Comment by kevin.stueve created at 2010-04-25 12:39:17

Andrew Ohana Cythonized my last prime counting code post.  I triple quoted the message he sent me on Mar 23

"""Hey,

So I've attached a code, how to get it working (in sage), the prime_sieve.c has the main method separated from the sieve so that we can get an unsigned 64-bit int straight out of it and into cython (huge speedup that bests the multiprocessed python code with a single thread on my machine):

0) I will refer to the sage directory (where the sage command lies) as SAGE_ROOT (as per the sage api)

1) make sure you clone sage and exit, you can do this from within sage by running hg_sage.clone(clone_name), eg

sage: hg_sage.clone('PrimePi')
<clone output>
sage: exit

2) copy your tables (with the same file names) into SAGE_ROOT/data/prime_pi_tables/

3) copy the two files I've attached to SAGE_ROOT/devel/sage/sage/functions/

4) edit SAGE_ROOT/devel/sage/sage/functions/all.py and add the following line after the prime_pi line

from cython_table_based_prime_pi import cython_table_based_prime_pi

we will remove this when the old prime_pi method is removed

5) edit SAGE_ROOT/devel/sage/module_list.py and add the following lines in the sage.functions section

Extension('sage.functions.cython_table_based_prime_pi',
    sources = ['sage/functions/cython_table_based_prime_pi.pyx']),

again we will remove this later on (after testing).

6) run the sage command with the argument -br e.g.

SAGE_ROOT/sage -br

7) you should now be able to use the cython_table_based_prime_pi function from within sage whenever you are in the PrimePi branch (you can switch branches with the hg_sage.switch command).

Hopefully this illustrates how to add code to sage in general, the module_list is not needed for python modules, only for cython modules and multiple cython sources can be used for a single module.

-- Andrew"""

I think that we are ready to make an optional package and installing it in the online version of Sage.  Andrew Ohana's instructions should allow anyone to add the table-based prime counting algorithm along with the densest data available to their copy of Sage.

Kevin Stueve


---

Attachment


---

Attachment

Just for the record:

TOS has published a new prime sieve program, which also incorporates some of my ideas (separate list for sieving primes that have multiples in every sieve segment, combined striking of multiples of the smallest primes).

However, it is rather a rewrite from scratch than an update of his previous one.


---

Attachment

I have posted new table-based prime counting code in table_based_prime_pi_23_July_2011.zip.  In addition to counting primes, this code can also count twin primes, prime triplets, and prime quadruplets.  Since my last contribution, denser tables of the prime counting function and counts of prime constellations have become available (by a factor of 10 in some intervals), decreasing the amount of sieving needed by such a factor.

This code fixes the problems in my original contribution.  The sieve I used in my original contribution was Tomás Oliveira e Silva's prime_sieve.c, which assumed pointers have 4 bytes.  The sieve I use in my new code is Kim Walisch's primesieve.  Primesieve uses portable c++ and uses Oliveira e Silva's algorithm for large x.

Although a lot of work has been done, my code should still be considered a rough draft.  The path to the primesieve package is still hard-coded.  A second person should fix such problems and also go over the code line by line and double-check for off-by-one errors and the like.  I am willing to offer someone who can can get this code in Sage coauthorship of the code.

This code checks for the presence of prime count tables in SAGE_ROOT/data/prime_counting_tables, and if they are not there, instructs the user to download them from http://sage.math.washington.edu/home/kstueve/prime_pi_tables/.

The code communicates with primesieve using the subprocess module and primesievesubprocess.cpp, a file I wrote to allow the code to communicate with primesieve over the command line.  It may be desirable to change this arrangement.  For one thing, primesieve has to do its initialization for every call to table_based_prime_pi.

To build primesievesubprocess.cpp, I put it into the main primesieve folder.  I ran the primesieve make file.  I removed main.o, ParallelPrimeSieve.o, and test,o from the out folder.  I then ran:
g++ primesievesubprocess.cpp out/*.o -o primesievesubprocess

Sincerely,
Kevin Stueve


---

Comment by kevin.stueve created at 2012-01-01 07:58:13

I have uploaded a new version of the table-based prime_pi algorithm to http://sage.math.washington.edu/home/kstueve/prime_pi_tables/table_based_prime_pi_31Dec2011.  The new version has denser tables of prime_pi and prime_pi2 (the twin prime counting function) and higher tables of prime_pi2 than the previous version.  The new version uses a Cython wrapper around primesieve rather than calling primesieve using the subprocess module.  Despite progress made, the code is still not yet complete.  It works on my MacBook Pro (but OpenMP only allows a single thread), but I have been unable to get primesieve to build as a Sage component on the sage.math computer (primesieve is portable c++, I have been able to get primesieve to build on sage.math, just not as a Sage component).  The issue surrounds enabling OpenMP.

I also experimented with compression schemes.  Given a sequence of differences between successive errors of a logarithmic integral approximation (I implemented Ramanujan's formula in double precision, equation 15 at http://mathworld.wolfram.com/LogarithmicIntegral.html), for each difference, given the highest 0 to 4 bits of the difference, by storing the probability that the next bit will be a 1 and providing this probability to an arithmetic coder (I used the arithmetic coder in Matt Mahoney's paq8hp6s), you can decrease the size of the file by 16%.  By using the previous difference to predict the current difference, even more compression may be possible- however hard-coding probabilities for the next bit to be a 1 given the high bits of the current and previous difference will not work-experimentally it is more efficient to allocate the storage to the current difference rather than the previous difference.  Fitting a function such as a multivariate Gaussian to the data may be a solution.

Hopefully the table-based prime_pi will make it into Sage in 2012.

Happy New Year,
Kevin Stueve


---

Comment by ohanar created at 2012-01-01 12:45:44

Hi Kevin,

Could you please update the horribly outdated description with details on how to install your changes. Just to make sure, this is intended at as an optional package for sage, yes? (The size of the database needed is why I am asking).

Looking at your changes, the first thing that jumps out at me is that you are including the source code of primesieve directly within the sage library. Considering that it is a separate piece of software, the best way to do this would be to bundle it within a separate spkg to install to `SAGE_LOCAL`. If you are not familiar with working with spkgs, see http://www.sagemath.org/doc/developer/producing_spkgs.html. If I remember correctly, primesieve doesn't quite work as a library out of the box, so you might have to apply some patches to it make it work as such. Doing this may help you debug the issues you are having with primesieve, however, you can not assume that every user has openmp (it was only introduced in gcc 4.2, and we support back to 4.0.1). I'm not quite sure about the policies for optional packages, but you may be able to require the user to have openmp, in which case the install script should check for it and fail if the computer's cc does not support it.

Secondly, you will need to create an spkg including your tables. These should be installed to `SAGE_DATA`, and the install script should be very simple.

There are some issues with the `PrimePi` class as well, but I need to sleep and look at it again before I can give you any real feedback on it.

Take care,
Andrew


---

Comment by ohanar created at 2012-01-05 01:18:59

fyi, #7539 is the appropriate place for the primesieve spkg. I toyed around today, and created an initial version of such an spkg based on the recently released primesieve-3.4. I'll post it in a few minutes after I update the description for said ticket.

One question for this ticket. In the description you mention the idea of including smaller tables as a standard spkg. This is will be a major uphill battle for you since we try to minimize the rate at which sage is bloating, so if you did manage to win people over, it would be with a database of no more than a couple megabytes. With such a small database, would there be any significant speed improvements relative to the current implementation (or for that matter, the rewrite at #11475)?


---

Attachment


---

Comment by ohanar created at 2012-01-22 15:30:06

I've rebased your patch off of my patches and spkg at #7539. Since #7539 fixes the openmp issues you were having on sage.math, I set your patch to be in parallel (unless, of course, gcc doesn't support openmp, in which case everything is serial).

Patch: attachment:trac7013_rebased.patch
