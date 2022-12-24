# Issue 8937: Implementation of AES with different key sizes

archive/issues_008937.json:
```json
{
    "body": "Assignee: mvngu\n\nKeywords: AES\n\nThis class implements the full Advanced Encryption Standard, as described in \n\nhttp://csrc.nist.gov/publications/fips/fips197/fips-197.pdf \n\nIt includes encryption with a 128 bit plaintext block, and keys of either 128, 196 or 256 bits, which are the only block and key sizes allowed by the standard.  It includes decryption by either the Inverse Cipher method, or the Equivalent Inverse Cipher method.  There are also methods to print out all the intermediate steps in either an encryption or decryption.\n\nThe various \"layers\": mixcolumns, shiftrows, subbytes and their inverses, are available to the user for experimentation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8937\n\n",
    "created_at": "2010-05-09T05:00:43Z",
    "labels": [
        "cryptography",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-feature",
    "title": "Implementation of AES with different key sizes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8937",
    "user": "amca01"
}
```
Assignee: mvngu

Keywords: AES

This class implements the full Advanced Encryption Standard, as described in 

http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf 

It includes encryption with a 128 bit plaintext block, and keys of either 128, 196 or 256 bits, which are the only block and key sizes allowed by the standard.  It includes decryption by either the Inverse Cipher method, or the Equivalent Inverse Cipher method.  There are also methods to print out all the intermediate steps in either an encryption or decryption.

The various "layers": mixcolumns, shiftrows, subbytes and their inverses, are available to the user for experimentation.

Issue created by migration from https://trac.sagemath.org/ticket/8937





---

archive/issue_comments_082290.json:
```json
{
    "body": "Implementation of AES with different key sizes",
    "created_at": "2010-05-09T23:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8937#issuecomment-82290",
    "user": "amca01"
}
```

Implementation of AES with different key sizes



---

archive/issue_comments_082291.json:
```json
{
    "body": "Changing assignee from mvngu to amca01.",
    "created_at": "2010-05-11T22:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8937#issuecomment-82291",
    "user": "amca01"
}
```

Changing assignee from mvngu to amca01.



---

archive/issue_comments_082292.json:
```json
{
    "body": "Attachment [aes.sage](tarball://root/attachments/some-uuid/ticket8937/aes.sage) by amca01 created at 2010-05-11 22:38:14",
    "created_at": "2010-05-11T22:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8937#issuecomment-82292",
    "user": "amca01"
}
```

Attachment [aes.sage](tarball://root/attachments/some-uuid/ticket8937/aes.sage) by amca01 created at 2010-05-11 22:38:14



---

archive/issue_comments_082293.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2011-06-12T15:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8937#issuecomment-82293",
    "user": "kini"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_082294.json:
```json
{
    "body": "On lines 12 and 13 of your file, you say that this is already implemented in Sage. May I ask what the benefit of your code is over the current implementation, then?\n\nBy the way, if you would like to contribute code to Sage, please generate a patch file against the Mercurial repository in `$SAGE_ROOT/devel/sage/` . The code should be either added to an existing `.py` or `.pyx` file, or in a new `.py` or `.pyx` file, somewhere in `$SAGE_ROOT/devel/sage`, rather than in a `.sage` file.\n\nI also notice that there is another version of `aes.sage` that you uploaded to the wiki page [TracTickets](TracTickets) (in fact that's how I came across this ticket). Can that one be ignored/deleted? It's older than the one you've uploaded to this ticket.",
    "created_at": "2011-06-12T15:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8937#issuecomment-82294",
    "user": "kini"
}
```

On lines 12 and 13 of your file, you say that this is already implemented in Sage. May I ask what the benefit of your code is over the current implementation, then?

By the way, if you would like to contribute code to Sage, please generate a patch file against the Mercurial repository in `$SAGE_ROOT/devel/sage/` . The code should be either added to an existing `.py` or `.pyx` file, or in a new `.py` or `.pyx` file, somewhere in `$SAGE_ROOT/devel/sage`, rather than in a `.sage` file.

I also notice that there is another version of `aes.sage` that you uploaded to the wiki page [TracTickets](TracTickets) (in fact that's how I came across this ticket). Can that one be ignored/deleted? It's older than the one you've uploaded to this ticket.



---

archive/issue_comments_082295.json:
```json
{
    "body": "Replying to [comment:2 kini]:\n> On lines 12 and 13 of your file, you say that this is already implemented in Sage. May I ask what the benefit of your code is over the current implementation, then?\n> \n> By the way, if you would like to contribute code to Sage, please generate a patch file against the Mercurial repository in `$SAGE_ROOT/devel/sage/` . The code should be either added to an existing `.py` or `.pyx` file, or in a new `.py` or `.pyx` file, somewhere in `$SAGE_ROOT/devel/sage`, rather than in a `.sage` file.\n> \n> I also notice that there is another version of `aes.sage` that you uploaded to the wiki page [TracTickets](TracTickets) (in fact that's how I came across this ticket). Can that one be ignored/deleted? It's older than the one you've uploaded to this ticket.\n\nThe main difference is that AES, as currently implemented in Martin Albrecht's SR class, is that AES is there treated as one of a number of cryptosystems with different parameters.  My implementation is much closer to the ISO standard in design, and allows the user to experiment with all aspects of the AES.",
    "created_at": "2011-06-13T02:06:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8937#issuecomment-82295",
    "user": "amca01"
}
```

Replying to [comment:2 kini]:
> On lines 12 and 13 of your file, you say that this is already implemented in Sage. May I ask what the benefit of your code is over the current implementation, then?
> 
> By the way, if you would like to contribute code to Sage, please generate a patch file against the Mercurial repository in `$SAGE_ROOT/devel/sage/` . The code should be either added to an existing `.py` or `.pyx` file, or in a new `.py` or `.pyx` file, somewhere in `$SAGE_ROOT/devel/sage`, rather than in a `.sage` file.
> 
> I also notice that there is another version of `aes.sage` that you uploaded to the wiki page [TracTickets](TracTickets) (in fact that's how I came across this ticket). Can that one be ignored/deleted? It's older than the one you've uploaded to this ticket.

The main difference is that AES, as currently implemented in Martin Albrecht's SR class, is that AES is there treated as one of a number of cryptosystems with different parameters.  My implementation is much closer to the ISO standard in design, and allows the user to experiment with all aspects of the AES.
