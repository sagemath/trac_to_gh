# Issue 4148: Upgrade to givaro-3.2.13rc1

Issue created by migration from https://trac.sagemath.org/ticket/4148

Original creator: cpernet

Original creation time: 2008-09-19 00:39:53

Assignee: cpernet

Upgrade the givaro spkg to upstream version 3.2.13rc1.
This is required for the resolution of ticket #4147 and is therefore a defect.


---

Comment by cpernet created at 2008-09-19 00:42:01

The proposed spkg is here:
[http://sage.math.washington.edu/home/pernet/givaro-3.2.13rc1.spkg](http://sage.math.washington.edu/home/pernet/givaro-3.2.13rc1.spkg)

Already succesfully tested on sage.math and on my x86_32 Linux box.


---

Comment by cpernet created at 2008-09-19 01:26:15

I have a pb compiling givaro on PPC-OSX, because endianness parameter __BYTE_ORDER is not defined there. I am working on it.


---

Comment by cpernet created at 2008-09-19 02:33:30

I changed the endianess detection in Givaro, which fixed the problem.
The new spkg is here:

[http://sage.math.washington.edu/home/pernet/givaro-3.2.13rc2.spkg](http://sage.math.washington.edu/home/pernet/givaro-3.2.13rc2.spkg)


---

Comment by mabshoff created at 2008-09-20 01:47:31

Spkg looks good to me. I added some code to touch the extensions linked against Givaro so they are automatically rebuild when doing a "sage -b". The updated spkg is in

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha0/givaro-3.2.13rc1.spkg

Positive review, but I am doing some more build testing to be sure the spkg actually works.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-20 02:01:54

Hhm, this spkg blows up on OSX 10.4 PPC as well as OSX 10.5 Intel with

```
Making install in rational
/bin/sh ../../../libtool --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I. -I../../.. -I../../..   -I../../../src/kernel/integer -I../../../src/kernel -I../../../src/kernel/system -I../../../src/kernel/memory   -I/Users/mabshoff/sage-3.1.2.rc2/local//include  -fPIC -I"/Users/mabshoff/sage-3.1.2.rc2/local/include" -MT givratcstor.lo -MD -MP -MF .deps/givratcstor.Tpo -c -o givratcstor.lo givratcstor.C
 g++ -DHAVE_CONFIG_H -I. -I../../.. -I../../.. -I../../../src/kernel/integer -I../../../src/kernel -I../../../src/kernel/system -I../../../src/kernel/memory -I/Users/mabshoff/sage-3.1.2.rc2/local//include -fPIC -I/Users/mabshoff/sage-3.1.2.rc2/local/include -MT givratcstor.lo -MD -MP -MF .deps/givratcstor.Tpo -c givratcstor.C  -fno-common -DPIC -o .libs/givratcstor.o
givratcstor.C:45: error: declaration of ‘uint64 ieee::mantissa’
givratcstor.C:42: error: conflicts with previous declaration ‘uint64 ieee::mantissa’
givratcstor.C:46: error: declaration of ‘uint64 ieee::exponent’
givratcstor.C:41: error: conflicts with previous declaration ‘uint64 ieee::exponent’
givratcstor.C:47: error: declaration of ‘uint64 ieee::negative’
givratcstor.C:40: error: conflicts with previous declaration ‘uint64 ieee::negative’
make[5]: *** [givratcstor.lo] Error 1
make[4]: *** [install-recursive] Error 1
make[3]: *** [install-recursive] Error 1
make[2]: *** [install-recursive] Error 1
Error installing givaro
```

Please make sure to base this spkg off the one I link above by the same name as yours.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-20 02:05:48

Ok, the problem boils down to byte order detection being broken on OSX it seems:

```
#if     __BYTE_ORDER == __BIG_ENDIAN
            uint64 negative:1;
            uint64 exponent:11;
            uint64 mantissa:52;
#endif                          /* Big endian.  */
#if     __BYTE_ORDER == __LITTLE_ENDIAN
            uint64 mantissa:52;
            uint64 exponent:11;
            uint64 negative:1;
#endif                          /* Little endian.  */
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-09-20 02:15:56

Ooops, as Clement just pointed out to me I picked the wrong spkg. The one at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha0/givaro-3.2.13rc2.spkg

based on his spkg has the extension rebuild fix and builds fine for me and passes doctests on various platforms from OSX, Linux in various flavors and Solaris. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-20 02:17:08

This is rc2 :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-20 02:46:16

Merged in Sage 3.1.3.alpha0


---

Comment by mabshoff created at 2008-09-20 02:46:16

Resolution: fixed
