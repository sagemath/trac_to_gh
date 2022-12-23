# Issue 5833: Update libgcrypt to 1.4.4

archive/issues_005833.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe latest upstream release is at\n\n ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-1.4.4.tar.bz2\n\nThe following is from the release notes:\n\n```\nThe GNU project is pleased to announce the availability of Libgcrypt\nversion 1.4.4.\n\nLibgcrypt is a general purpose library of cryptographic building\nblocks.  It is originally based on code used by GnuPG.  It does not\nprovide any implementation of OpenPGP or other protocols.  Thorough\nunderstanding of applied cryptography is required to use Libgcrypt.\n\nNoteworthy changes in version 1.4.4:\n\n * Publish GCRY_MODULE_ID_USER and GCRY_MODULE_ID_USER_LAST constants.\n   This functionality has been in Libgcrypt since 1.3.0. \n\n * MD5 may now be used in non-enforced fips mode.\n\n * Fixed HMAC for SHA-384 and SHA-512 with keys longer than 64 bytes.\n\n * In fips mode, RSA keys are now generated using the X9.31 algorithm\n   and DSA keys using the FIPS 186-2 algorithm.\n\n * The transient-key flag is now also supported for DSA key\n   generation.  DSA domain parameters may be given as well.\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5833\n\n",
    "created_at": "2009-04-20T06:51:28Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "Update libgcrypt to 1.4.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5833",
    "user": "mabshoff"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/5833





---

archive/issue_comments_045845.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-20T06:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5833#issuecomment-45845",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045846.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-01T06:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5833#issuecomment-45846",
    "user": "mvngu"
}
```

Resolution: duplicate



---

archive/issue_comments_045847.json:
```json
{
    "body": "Closing this as a duplicate of #7045.",
    "created_at": "2009-10-01T06:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5833#issuecomment-45847",
    "user": "mvngu"
}
```

Closing this as a duplicate of #7045.
