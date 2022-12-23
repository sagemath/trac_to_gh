# Issue 5833: Update libgcrypt to 1.4.4

Issue created by migration from https://trac.sagemath.org/ticket/5833

Original creator: mabshoff

Original creation time: 2009-04-20 06:51:28

Assignee: mabshoff

The latest upstream release is at

 ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-1.4.4.tar.bz2

The following is from the release notes:

```
The GNU project is pleased to announce the availability of Libgcrypt
version 1.4.4.

Libgcrypt is a general purpose library of cryptographic building
blocks.  It is originally based on code used by GnuPG.  It does not
provide any implementation of OpenPGP or other protocols.  Thorough
understanding of applied cryptography is required to use Libgcrypt.

Noteworthy changes in version 1.4.4:

 * Publish GCRY_MODULE_ID_USER and GCRY_MODULE_ID_USER_LAST constants.
   This functionality has been in Libgcrypt since 1.3.0. 

 * MD5 may now be used in non-enforced fips mode.

 * Fixed HMAC for SHA-384 and SHA-512 with keys longer than 64 bytes.

 * In fips mode, RSA keys are now generated using the X9.31 algorithm
   and DSA keys using the FIPS 186-2 algorithm.

 * The transient-key flag is now also supported for DSA key
   generation.  DSA domain parameters may be given as well.
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-04-20 06:51:39

Changing status from new to assigned.


---

Comment by mvngu created at 2009-10-01 06:26:17

Resolution: duplicate


---

Comment by mvngu created at 2009-10-01 06:26:17

Closing this as a duplicate of #7045.
