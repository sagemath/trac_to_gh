# Issue 7439: optional spkg nauty-24b7.p1  fails to build with sage-4.2.1 and ubuntu 9.10 (gcc-4.4.1)

Issue created by migration from https://trac.sagemath.org/ticket/7439

Original creator: was

Original creation time: 2009-11-12 05:31:22

Assignee: tbd

With gcc version 4.4.1 (Ubuntu 4.4.1-4ubuntu8):


```
...
dreadnaut.c:983: warning: format ‘%lu’ expects type ‘long unsigned int’, but argument 3 has type ‘unsigned int’
dreadnaut.c:985: warning: format ‘%lu’ expects type ‘long unsigned int’, but argument 3 has type ‘unsigned int’
gcc -c -O4 -march=i686  gtools.c
In file included from gtools.c:6:
gtools.h:159: error: conflicting types for ‘getline’
/usr/include/stdio.h:651: note: previous declaration of ‘getline’ was here
gtools.c:375: error: conflicting types for ‘getline’
/usr/include/stdio.h:651: note: previous declaration of ‘getline’ was here
gtools.c: In function ‘gt_abort’:
gtools.c:1835: warning: format not a string literal and no format arguments
make: *** [gtools.o] Error 1
Copying nauty...
cp: cannot stat `addedgeg': No such file or directory
cp: cannot stat `amtog': No such file or directory
cp: cannot stat `biplabg': No such file or directory
cp: cannot stat `catg': No such file or directory
cp: cannot stat `complg': No such file or directory
cp: cannot stat `copyg': No such file or directory
cp: cannot stat `countg': No such file or directory
cp: cannot stat `deledgeg': No such file or directory
cp: cannot stat `directg': No such file or directory
cp: cannot stat `dretog': No such file or directory
cp: cannot stat `genbg': No such file or directory
cp: cannot stat `geng': No such file or directory
cp: cannot stat `genrang': No such file or directory
cp: cannot stat `labelg': No such file or directory
cp: cannot stat `listg': No such file or directory
cp: cannot stat `multig': No such file or directory
cp: cannot stat `newedgeg': No such file or directory
cp: cannot stat `NRswitchg': No such file or directory
cp: cannot stat `pickg': No such file or directory
cp: cannot stat `planarg': No such file or directory
cp: cannot stat `shortg': No such file or directory
cp: cannot stat `showg': No such file or directory

real    0m29.370s
user    0m10.093s
sys     0m18.105s
sage: An error occurred while installing nauty-24b7.p1
```



---

Comment by was created at 2009-11-12 06:30:06


```

I confirmed that this is a problem with the latest nauty 2.4 as well.
I've sent a message to the nauty mailing list.

Thanks,

Jason
```



---

Comment by drkirkby created at 2010-03-13 01:44:29

Using sage 4.3.4.alpha1 on Solaris 10 (SPARC) and don't even get as far as you do on Ununta. Instead I get problems with:


```
nauty-24b7.p1/nauty24b7.tar.gz
nauty-24b7.p1/SPKG.txt
nauty-24b7.p1/license.txt
Finished extraction
****************************************************
Host system
uname -a:
SunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: sparc-sun-solaris2.10
Configured with: ../gcc-4.4.3/configure --prefix=/usr/local/gcc-4.4.3 --with-mpfr=/usr/local/gcc-4.4.3 --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local/gcc-4.4.3 --enable-languages=c,c++,fortran
Thread model: posix
gcc version 4.4.3 (GCC)
****************************************************
./spkg-install: top_level=/export/home/drkirkby/sage-4.3.4.alpha1/spkg/build/nauty-24b7.p1: is not an identifier

real    0m0.011s
user    0m0.003s
sys     0m0.007s
sage: An error occurred while installing nauty-24b7.p1
```



---

Comment by wjlaffin created at 2010-03-29 20:49:50

http://dcsmail.anu.edu.au/pipermail/nauty-list/2009-November/000546.html

shows Brendan's reply to Jason as well as possible work-arounds. 

Using -ansi did not work reporting same problem if put in CFLAGS and gave other errors (below) if put in CC definition:


```
...
gcc -ansi -o genrang -O4  genrang.c nausparse.o \
                gtools.o nautil.o naututil.o naugraph.o rng.o
genrang.c: In function ‘main’:
genrang.c:405: error: storage size of ‘nauty_tz’ isn’t known
make: *** [genrang] Error 1

```


however, his other suggestion, did make a compile work:


```
sed -i 's/getline/readline/g' gtools-h.in
sed -i 's/getline/readline/g' shortg.c
sed -i 's/getline/readline/g' gtools.c
./configure
make
```


I'm not sure how to test that this doesn't brake anything within sage though.


---

Comment by wjlaffin created at 2010-03-30 19:44:07

In a personal email from Brendan McKay (author):

  Version 2.5 has some serious changes and won't be released for a while. An alternative to changing multiple files would be to insert

```
#define getline gtools_getline
}}} 
  into nauty-h.in .


---

Comment by wjlaffin created at 2010-03-30 19:44:07

Changing status from new to needs_work.


---

Comment by zimmerma created at 2010-05-18 07:33:37

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2010-05-18 07:33:37

I confirm the following works (tried with sage-4.4.1 and nauty-24b7.p1.spkg):

```
If you insert
  #define getline nauty_getline
into gtools-h.in after all the #includes in that file, it should compile.
```

Thanks to Brendan McKay for that patch. I have put an updated spkg at
http://www.loria.fr/~zimmerma/nauty-24b7.p1.spkg. Please could someone review it?

Paul


---

Comment by jason created at 2010-05-18 14:09:40

This spkg was horribly out of conformance with the current spkg guidelines.  So I redid the spkg, upgraded to nauty 2.4 (final), and applied the above patch.  The result is here: http://sage.math.washington.edu/home/jason/nauty-24.spkg

Paul, could you in turn review the above spkg?  It works for me on OSX 10.6 and Ubuntu 9.10.


---

Comment by zimmerma created at 2010-05-18 21:39:59

Jason, sorry for the horrible spkg, this was my first spkg... Your new spkg works like a charm
(tested under Fedora 12). I did not run the doctests (do they test optional packages) but the
following did work:

```
sage: graph_list = graphs.nauty_geng("-q 3")
sage: len(graph_list)
4
```

(I've removed my name as author since the new spkg is your work.)


---

Comment by zimmerma created at 2010-05-18 21:39:59

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-05-18 21:46:53

Replying to [comment:7 zimmerma]:
> Jason, sorry for the horrible spkg, this was my first spkg... Your new spkg works like a charm

Oh, I thought it was my fault, as I did the original nauty spkg, and there weren't nice guidelines back then.


> (tested under Fedora 12). I did not run the doctests (do they test optional packages) 

Yes, but I don't know if there are any #optional doctests for nauty in the sage library.

but the
> following did work:
> {{{
> sage: graph_list = graphs.nauty_geng("-q 3")
> sage: len(graph_list)
> 4
> }}}

Great!


---

Comment by mhansen created at 2010-06-07 05:06:40

Resolution: fixed
