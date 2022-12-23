# Issue 6758: visibility.c in libgcrypt attempts to return value from void function.

Issue created by migration from https://trac.sagemath.org/ticket/6758

Original creator: drkirkby

Original creation time: 2009-08-16 03:44:32

Assignee: somebody

CC:  mvngu drkirkby

I tried to use the Sun compiler to build Sage. Since it's more fussy that gcc, it is showing as an *error* 


```

Making all in src
make[4]: Entering directory `/export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/build/libgcrypt-1.4.3.p1/src/src'
source='visibility.c' object='libgcrypt_la-visibility.lo' libtool=yes \
DEPDIR=.deps depmode=none /bin/bash ../depcomp \
/bin/bash ../libtool --tag=CC   --mode=compile /opt/sunstudio12.1/bin/cc -DHAVE_CONFIG_H -I. -I..   -I/export/home/drkirkby/sage/suncc/sage-4.1.1/local/include -I/export/home/drkirkby/sage/suncc/sage-4.1.1/local/include -g -c -o libgcrypt_la-visibility.lo `test -f 'visibility.c' || echo './'`visibility.c
mkdir .libs
 /opt/sunstudio12.1/bin/cc -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sage/suncc/sage-4.1.1/local/include -I/export/home/drkirkby/sage/suncc/sage-4.1.1/local/include -g -c visibility.c  -KPIC -DPIC -o .libs/libgcrypt_la-visibility.o
"visibility.c", line 702: void function cannot return value
"visibility.c", line 851: void function cannot return value
cc: acomp failed for visibility.c
```

The dodgy bits of code are:

```
void
gcry_md_hash_buffer (int algo, void *digest,
                     const void *buffer, size_t length)
{
  return _gcry_md_hash_buffer (algo, digest, buffer, length);
}
```

and 

```
void
gcry_ac_io_init_va (gcry_ac_io_t *ac_io, gcry_ac_io_mode_t mode,
                    gcry_ac_io_type_t type, va_list ap)
{
  return _gcry_ac_io_init_va (ac_io, mode, type, ap);
}
```

The Sun compiler will not accept this, and so exits, aborting the build of Sage. 

Note there are license issues with libgcrypt too - it is GPL 3. See #6757

Dave 


---

Comment by drkirkby created at 2009-08-16 11:58:15

By looking at the latest source code for libgcrypt this code has been changed. It would appear the intension was to just execute the functions _gcry_md_hash_buffer and _gcry_ac_io_init_va, but not return their value. Here are the relevant functions from the latest release (1.4.4):

```
void
gcry_ac_io_init_va (gcry_ac_io_t *ac_io, gcry_ac_io_mode_t mode,
                    gcry_ac_io_type_t type, va_list ap)
{
  _gcry_ac_io_init_va (ac_io, mode, type, ap);
}
```


The code for function gcry_md_hash_buffer has changed a little more, but it is obvious the intension here two was to execute _gcry_md_hash_buffer and not return the value. 


```

void
gcry_md_hash_buffer (int algo, void *digest,
                     const void *buffer, size_t length)
{
  if (!fips_is_operational ())
    {
      (void)fips_not_operational ();
      fips_signal_error ("called in non-operational state");
    }
  _gcry_md_hash_buffer (algo, digest, buffer, length);
}

```


So I removed the 'return' from the code in Sage, and made a patch. Since this is just buggy code, and not-Solaris specific, I've made the patch on all platforms. It is only seen on Solaris with the Sun compiler, as the Sun compiler is more fussy than gcc. 

See: http://sage.math.washington.edu/home/kirkby/Solaris-fixes/libgcrypt-1.4.3.p2/ 


Sinve there are some license issues here, I have not updated the package. This code currently in Sage is GPL3 - see #6757

Dave


---

Comment by mvngu created at 2009-09-02 05:14:01

After uncompressing the spkg

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/libgcrypt-1.4.3.p2/libgcrypt-1.4.3.p2.spkg

I see that it contains two copies of libgcrypt: one in the src (version 1.4.0) directory and another copy in src/libgcrypt-1.4.3. Any reason why we need two different versions in the spkg?


---

Comment by mvngu created at 2009-09-17 22:49:47

This needs work as the updated libgcrypt spkg is seriously messed up --- it has two different versions of libgcrypt.


---

Comment by mvngu created at 2009-09-18 02:05:48

An updated spkg is up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/libgcrypt-1.4.3.p2.spkg

This package incorporates David Kirkby's changes in 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/libgcrypt-1.4.3.p2/libgcrypt-1.4.3.p2.spkg

but leaves out the fixes for the dodgy bits of code since these have been fixed in libgcrypt 1.4.3. I deleted the patches/ directory. Changes have been committed in David's name.


---

Comment by drkirkby created at 2009-09-27 22:51:43

Minh

Something is wrong here. Your revised version will not build with the Sun compiler. It gives the errors:


```
"visibility.c", line 702: void function cannot return value
"visibility.c", line 851: void function cannot return value
```


as it does not contain my fixes. (I appreciate I screwed up the package first). 

I believe the best solution is to forget about 1.4.3.p2 entirely, and produce a 1.4.4. Despite the web site saying 1.4.4 is GPL3, the code clearly has a GPL2 'COPYING' file. 


Dave


---

Comment by drkirkby created at 2009-09-28 01:21:33

#7045 has an update to the 1.4.4 release. No changes to the source were necessary for this to build with Sun Studio 12.1


---

Comment by mvngu created at 2009-09-28 01:23:19

Replying to [comment:6 drkirkby]:
> Something is wrong here. Your revised version will not build with the Sun compiler. It gives the errors:
> 

```
"visibility.c", line 702: void function cannot return value
"visibility.c", line 851: void function cannot return value
```

> 
> as it does not contain my fixes. 

Greatly appreciated that you caught this issue!





> (I appreciate I screwed up the package first). 

I believe you didn't mess up the package. It was messed up even before the start of the 4.x series.





> I believe the best solution is to forget about 1.4.3.p2 entirely, and produce a 1.4.4. Despite the web site saying 1.4.4 is GPL3, the code clearly has a GPL2 'COPYING' file. 

Yes, that sounds reasonable. I usually go for the license file in the source tarball myself and also check on the project website.


---

Comment by mvngu created at 2009-09-28 01:36:43

Resolution: wontfix


---

Comment by mvngu created at 2009-09-28 01:36:43

We should upgrade to libgcrypt 1.4.4 and not worry about libgcrypt 1.4.3 any longer. See ticket #7045 for this.
