# Issue 7387: gnutls not building on OpenSolaris (x86)

Issue created by migration from https://trac.sagemath.org/ticket/7387

Original creator: drkirkby

Original creation time: 2009-11-04 00:48:18

Assignee: drkirkby

CC:  drkirkby

There is an issue with the gnutls when trying to build 2
.2.1.p4 on OpenSolaris. Strangely, the same problem does not occur on Solaris 10 on SPARC. The linker is finding two copies of the _gcrypt_ and _gpg-error_ libraries. One set are from Sun and reside in /usr/lib and the second set are in the SAGE_LOCAL/lib, and are included in Sage. 

 == What does work - building gnutils independent of Sage ==

It's important to note that if that .spkg file is built outside of Sage directory structure, with none of the Sage environment variables set, so it builds fine except SAGE_LOCAL to something that is not empty (just to stop the spkg-install script exiting). The following will work:


```
$ cp gnutls-2.2.1.p4.spkg /tmp
$ cd /tmp
$ gtar xfj gnutls-2.2.1.p4.spkg
$ cd gnutls-2.2.1.p4
$ export SAGE_LOCAL=/tmp
$ ./spkg-install
$ ls /tmp/lib
libgnutls-extra.la           libgnutls-openssl.so.26
libgnutls-extra.so           libgnutls-openssl.so.26.1.2
libgnutls-extra.so.26        libgnutls.so
libgnutls-extra.so.26.1.2    libgnutls.so.26
libgnutls.la                 libgnutls.so.26.1.2
libgnutls-openssl.la         pkgconfig
libgnutls-openssl.so

```


In this case, gnutls is using all the libraries supplied by Sun, and none included in Sage. If 'ldd' is used to find the dependances of the libraries built in /tmp/lib, one finds many libraries, but which include these two:

 * /usr/lib/libgcrypt.so.11
 * /usr/lib/libgpg-error.so.0

The gcrypt and gpg-error libraries are included in Sage too, but are not used in this in the above example. 


 == What will not work (building as part of Sage) ==

When one attempts to build gnutls inside the Sage source tree, with all the environment variables set, so it all goes wrong. The lines in bold show the most important hint as to what is wrong. 

*ld: fatal: recording name conflict: file `/export/home/drkirkby/sage-4.2/local/lib/libgpg-error.so' and file `/usr/lib/libgpg-error.so' provide identical dependency names: libgpg-error.so.0  (possible multiple inclusion of the same file)*

Here is a larger section of the error message. I've attached 'config.log' 


```
gcc -std=gnu99 -shared -Wl,-h -Wl,libgnutls.so.26 -o .libs/libgnutls.so.26.1.2
  .libs/gnutls_record.o .libs/gnutls_compress.o .libs/debug.o .libs/gnutls_cip
her.o .libs/gnutls_buffers.o .libs/gnutls_handshake.o .libs/gnutls_num.o .libs
/gnutls_errors.o .libs/gnutls_algorithms.o .libs/gnutls_dh.o .libs/gnutls_kx.o
 .libs/gnutls_priority.o .libs/gnutls_hash_int.o .libs/gnutls_cipher_int.o .li
bs/gnutls_compress_int.o .libs/gnutls_session.o .libs/gnutls_db.o .libs/x509_b
64.o .libs/auth_anon.o .libs/gnutls_extensions.o .libs/gnutls_auth.o .libs/gnu
tls_v2_compat.o .libs/gnutls_datum.o .libs/auth_rsa.o .libs/gnutls_session_pac
k.o .libs/gnutls_mpi.o .libs/gnutls_pk.o .libs/gnutls_cert.o .libs/gnutls_glob
al.o .libs/gnutls_constate.o .libs/gnutls_anon_cred.o .libs/pkix_asn1_tab.o .l
ibs/gnutls_asn1_tab.o .libs/gnutls_mem.o .libs/auth_cert.o .libs/gnutls_ui.o .
libs/gnutls_sig.o .libs/auth_dhe.o .libs/gnutls_dh_primes.o .libs/ext_max_reco
rd.o .libs/gnutls_alert.o .libs/gnutls_str.o .libs/gnutls_state.o .libs/gnutls
_x509.o .libs/ext_cert_type.o .libs/gnutls_rsa_export.o .libs/auth_rsa_export.
o .libs/ext_server_name.o .libs/auth_dh_common.o .libs/gnutls_helper.o .libs/e
xt_inner_application.o .libs/gnutls_extra_hooks.o .libs/gnutls_supplemental.o 
.libs/ext_srp.o .libs/gnutls_srp.o .libs/auth_srp.o .libs/auth_srp_passwd.o .l
ibs/auth_srp_sb64.o .libs/auth_srp_rsa.o .libs/auth_psk.o .libs/auth_psk_passw
d.o .libs/gnutls_psk.o .libs/auth_dhe_psk.o -Wl,-z -Wl,allextract ../lgl/.libs
/liblgnu.a x509/.libs/libgnutls_x509.a -Wl,-z -Wl,defaultextract  -R/export/ho
me/drkirkby/sage-4.2/local/lib -R/export/home/drkirkby/sage-4.2/local/lib -L/u
sr/lib -ltasn1 -L/export/home/drkirkby/sage-4.2/local/lib /export/home/drkirkb
y/sage-4.2/local/lib/libgcrypt.so /export/home/drkirkby/sage-4.2/local/lib/lib
gpg-error.so -lz -lgcrypt -lgpg-error -lnsl -lsocket -lc 
ld: fatal: recording name conflict: file `/export/home/drkirkby/sage-4.2/local
/lib/libgcrypt.so' and file `/usr/lib/libgcrypt.so' provide identical dependen
cy names: libgcrypt.so.11  (possible multiple inclusion of the same file)
ld: fatal: recording name conflict: file `/export/home/drkirkby/sage-4.2/local
/lib/libgpg-error.so' and file `/usr/lib/libgpg-error.so' provide identical de
pendency names: libgpg-error.so.0  (possible multiple inclusion of the same fi
le)
ld: fatal: file processing errors. No output written to .libs/libgnutls.so.26.
1.2
collect2: ld returned 1 exit status
make[5]: *** [libgnutls.la] Error 1
make[5]: Leaving directory `/export/home/drkirkby/sage-4.2/spkg/build/gnutls-2
.2.1.p4/src/lib'
```



 == A hack that will work ==

I expect this would cause other problems, and is certainly not the right way to address this, but if the following files are removed 

 * SAGE_LOCAL/include/gcrypt-module.h 
 * SAGE_LOCAL/include/gpg-error.h
 * SAGE_LOCAL/include/gcrypt.h
 * SAGE_LOCAL/lib/libgcrypt*
 * SAGE_LOCAL/lib/libgpg*

before one attempts to build gnutls, so the build will work. 



---

Attachment

config.log file generated by the 'configure' script.


---

Comment by jsp created at 2010-01-01 18:32:57

Working on Open Solaris 09/06 x86 in VirtualBox the build of gnutls
succeeded after a rebuild of libgpg and libcrypt in 64 bit mode.

I had to change the spkg-install files accordingly.

Jaap


---

Comment by jsp created at 2010-01-04 15:36:11

I made a new spkg such that it builds on Open Solaris with SAGE64="yes"

libgpg and libcrypt built with 64 bit.

See: http://boxen.math.washington.edu/home/jsp/ports/gnutls-2.2.1.p5.spkg



```
real	1m46.089s
user	0m49.128s
sys	1m12.507s
Successfully installed gnutls-2.2.1.p5
Now cleaning up tmp files.
rm: cannot remove directory `/export/home/jaap/Downloads/sage-4.3.1.alpha0/spkg/build/gnutls-2.2.1.p5': Invalid argument
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing gnutls-2.2.1.p5.spkg
jaap@opensolaris:~/Downloads/sage-4.3.1.alpha0$ 

```



Jaap


---

Comment by jsp created at 2010-01-04 15:36:11

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-04 21:45:45

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-04 21:45:45

That fixes the problem. 

It probably worth saying in future that the change will add the compiler option -m64 on any platform - it is not just Solaris. The problem with the original implementation is someone decided to limit it to OSX. The change makes it work on any platform. 

But I'm not going to ask you to change it - just a minor point for the future. 

Dave


---

Comment by rlm created at 2010-01-13 05:56:41

Resolution: fixed
