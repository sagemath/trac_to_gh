# Issue 8469: add "Number Theory and the RSA Public Key Cryptosystem" to "Sage HOWTOs"

archive/issues_008469.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @malb\n\nKeywords: RSA, public-key cryptosystem\n\nAdd the document [Number Theory and the RSA Public Key Cryptosystem](http://sites.google.com/site/nguyenminh2/numtheory-crypto-sage.pdf) to the documentation category \"Sage HOWTOs\". The original proposal can be found on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8469\n\n",
    "created_at": "2010-03-07T02:25:47Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "add \"Number Theory and the RSA Public Key Cryptosystem\" to \"Sage HOWTOs\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8469",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  @malb

Keywords: RSA, public-key cryptosystem

Add the document [Number Theory and the RSA Public Key Cryptosystem](http://sites.google.com/site/nguyenminh2/numtheory-crypto-sage.pdf) to the documentation category "Sage HOWTOs". The original proposal can be found on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc).

Issue created by migration from https://trac.sagemath.org/ticket/8469





---

archive/issue_comments_076147.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-10T06:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76147",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076148.json:
```json
{
    "body": "Looks good and builds fine. Nice job!\n~Mark",
    "created_at": "2010-05-04T06:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76148",
    "user": "https://trac.sagemath.org/admin/accounts/users/mjordan7"
}
```

Looks good and builds fine. Nice job!
~Mark



---

archive/issue_comments_076149.json:
```json
{
    "body": "Two comments: \n* In this tutorial, euler_phi(n) is called several times. The whole security of RSA lies in the fact that euler_phi takes a long time if you don't know the factorization. I'd suggest using a variable:\n\n\n```\nphi = (p-1)*(q-1)\n```\n\n\nWhen I've taught about RSA, I've used big primes:\n\n\n```\np = next_prime(randint(10^100,10^101))\nq = next_prime(randint(10^100,10^101))\n```\n\n\nand euler_phi would take for ever, of course. If this is reasonable to you, I'll be glad to write a patch, of course.\n\n* A missing space was generating a minor problem with latex. I attach a patch only for that, waiting for your opinions on the first item.",
    "created_at": "2010-05-12T15:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76149",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```

Two comments: 
* In this tutorial, euler_phi(n) is called several times. The whole security of RSA lies in the fact that euler_phi takes a long time if you don't know the factorization. I'd suggest using a variable:


```
phi = (p-1)*(q-1)
```


When I've taught about RSA, I've used big primes:


```
p = next_prime(randint(10^100,10^101))
q = next_prime(randint(10^100,10^101))
```


and euler_phi would take for ever, of course. If this is reasonable to you, I'll be glad to write a patch, of course.

* A missing space was generating a minor problem with latex. I attach a patch only for that, waiting for your opinions on the first item.



---

archive/issue_comments_076150.json:
```json
{
    "body": "Attachment [trac_8469_add_a_space.patch](tarball://root/attachments/some-uuid/ticket8469/trac_8469_add_a_space.patch) by pang created at 2010-05-12 15:37:58",
    "created_at": "2010-05-12T15:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76150",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```

Attachment [trac_8469_add_a_space.patch](tarball://root/attachments/some-uuid/ticket8469/trac_8469_add_a_space.patch) by pang created at 2010-05-12 15:37:58



---

archive/issue_comments_076151.json:
```json
{
    "body": "Replying to [comment:5 pang]:\n> If this is reasonable to you, I'll be glad to write a patch, of course.\n\nThat would be nice. Thank you.\n\n\n\n\n\n>  * A missing space was generating a minor problem with latex. I attach a patch only for that\n\nYour patch looks OK to me.\n\n\n\nAlso, could you put your real name in the \"Reviewer(s):\" field? That way, it makes it easier to credit you for your contribution.",
    "created_at": "2010-05-15T04:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76151",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:5 pang]:
> If this is reasonable to you, I'll be glad to write a patch, of course.

That would be nice. Thank you.





>  * A missing space was generating a minor problem with latex. I attach a patch only for that

Your patch looks OK to me.



Also, could you put your real name in the "Reviewer(s):" field? That way, it makes it easier to credit you for your contribution.



---

archive/issue_comments_076152.json:
```json
{
    "body": "Attachment [trac_8469_review.patch](tarball://root/attachments/some-uuid/ticket8469/trac_8469_review.patch) by pang created at 2010-05-15 22:47:28\n\nThe last patch includes the previous one (I can't find a wat to delete it).",
    "created_at": "2010-05-15T22:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76152",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```

Attachment [trac_8469_review.patch](tarball://root/attachments/some-uuid/ticket8469/trac_8469_review.patch) by pang created at 2010-05-15 22:47:28

The last patch includes the previous one (I can't find a wat to delete it).



---

archive/issue_comments_076153.json:
```json
{
    "body": "Attachment [trac_8469_review_final.patch](tarball://root/attachments/some-uuid/ticket8469/trac_8469_review_final.patch) by pang created at 2010-05-16 18:56:27\n\nOnly the last patch is needed. Sorry for the noise.",
    "created_at": "2010-05-16T18:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76153",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```

Attachment [trac_8469_review_final.patch](tarball://root/attachments/some-uuid/ticket8469/trac_8469_review_final.patch) by pang created at 2010-05-16 18:56:27

Only the last patch is needed. Sorry for the noise.



---

archive/issue_comments_076154.json:
```json
{
    "body": "Attachment [trac_8469-rsa.patch](tarball://root/attachments/some-uuid/ticket8469/trac_8469-rsa.patch) by mvngu created at 2010-08-03 12:07:44\n\nbased on Sage 4.5.2.rc0",
    "created_at": "2010-08-03T12:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76154",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8469-rsa.patch](tarball://root/attachments/some-uuid/ticket8469/trac_8469-rsa.patch) by mvngu created at 2010-08-03 12:07:44

based on Sage 4.5.2.rc0



---

archive/issue_comments_076155.json:
```json
{
    "body": "Attachment [trac_8469-review-rebased.patch](tarball://root/attachments/some-uuid/ticket8469/trac_8469-review-rebased.patch) by mvngu created at 2010-08-03 12:13:50\n\nWhen applying the previous version of my patch on top of Sage 4.5.2.rc0, I got the following failure:\n\n```sh\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8469/trac_8469-rsa.patch && hg qpush \nadding trac_8469-rsa.patch to series file\napplying trac_8469-rsa.patch\npatching file doc/en/thematic_tutorials/index.rst\nHunk #1 FAILED at 13\n1 out of 1 hunks FAILED -- saving rejects to file doc/en/thematic_tutorials/index.rst.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_8469-rsa.patch\n```\n\nI have rebased my patch against Sage 4.5.2.rc0 in order to resolve the above failure.\n\n\n\nThe content of pang's patch [attachment:trac_8469_review_final.patch] is mostly OK, but the way the patch itself is structured is frowned upon. From the way it looks, I guess that the patch was put together by concatenating many patches together into one file. That's not how you should put patches together. Use Mercurial queue to concatenate patches into one patch. I have done this and uploaded an updated version of pang's patch, which also fixes some typos found in his original patch. For reference, here are the fixed typos:\n\n```diff\n--- a/doc/en/thematic_tutorials/numtheory_rsa.rst\n+++ b/doc/en/thematic_tutorials/numtheory_rsa.rst\n@@ -295,8 +295,8 @@\n pseudo-random integer uniformly distributed within the closed interval\n `[0, n-1]`.  \n \n-We can compute the value `\\varphi(n)` calling the sage function\n-``euler_phi(n)``, but for arbitrary large prime numbers `p` and `q`,\n+We can compute the value `\\varphi(n)` by calling the sage function\n+``euler_phi(n)``, but for arbitrarily large prime numbers `p` and `q`,\n this can take an enormous amount of time. Indeed, the private key\n can be quickly deduced from the public key once you know `\\varphi(n)`,\n so it is an important part of the security of the RSA cryptosystem that\n```\n\nPang's updated patch and the typo fixes are all rolled into one patch. See the ticket description for instructions on applying the relevant patches.\n\n\n\nFor ticket to be closed, the following must happen:\n\n1. Someone needs to sign off on [attachment:trac_8469-rsa.patch]. This is my patch, so it requires a reviewer other than myself.\n2. Someone needs to sign off on [attachment:trac_8469-review-rebased.patch]. This is pang's original patch together with some typo fixes by me. I'm happy with pang's content. But someone other than myself needs to go over the fixes I included in this updated patch.",
    "created_at": "2010-08-03T12:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76155",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8469-review-rebased.patch](tarball://root/attachments/some-uuid/ticket8469/trac_8469-review-rebased.patch) by mvngu created at 2010-08-03 12:13:50

When applying the previous version of my patch on top of Sage 4.5.2.rc0, I got the following failure:

```sh
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8469/trac_8469-rsa.patch && hg qpush 
adding trac_8469-rsa.patch to series file
applying trac_8469-rsa.patch
patching file doc/en/thematic_tutorials/index.rst
Hunk #1 FAILED at 13
1 out of 1 hunks FAILED -- saving rejects to file doc/en/thematic_tutorials/index.rst.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8469-rsa.patch
```

I have rebased my patch against Sage 4.5.2.rc0 in order to resolve the above failure.



The content of pang's patch [attachment:trac_8469_review_final.patch] is mostly OK, but the way the patch itself is structured is frowned upon. From the way it looks, I guess that the patch was put together by concatenating many patches together into one file. That's not how you should put patches together. Use Mercurial queue to concatenate patches into one patch. I have done this and uploaded an updated version of pang's patch, which also fixes some typos found in his original patch. For reference, here are the fixed typos:

```diff
--- a/doc/en/thematic_tutorials/numtheory_rsa.rst
+++ b/doc/en/thematic_tutorials/numtheory_rsa.rst
@@ -295,8 +295,8 @@
 pseudo-random integer uniformly distributed within the closed interval
 `[0, n-1]`.  
 
-We can compute the value `\varphi(n)` calling the sage function
-``euler_phi(n)``, but for arbitrary large prime numbers `p` and `q`,
+We can compute the value `\varphi(n)` by calling the sage function
+``euler_phi(n)``, but for arbitrarily large prime numbers `p` and `q`,
 this can take an enormous amount of time. Indeed, the private key
 can be quickly deduced from the public key once you know `\varphi(n)`,
 so it is an important part of the security of the RSA cryptosystem that
```

Pang's updated patch and the typo fixes are all rolled into one patch. See the ticket description for instructions on applying the relevant patches.



For ticket to be closed, the following must happen:

1. Someone needs to sign off on [attachment:trac_8469-rsa.patch]. This is my patch, so it requires a reviewer other than myself.
2. Someone needs to sign off on [attachment:trac_8469-review-rebased.patch]. This is pang's original patch together with some typo fixes by me. I'm happy with pang's content. But someone other than myself needs to go over the fixes I included in this updated patch.



---

archive/issue_comments_076156.json:
```json
{
    "body": "Apply trac_8469-rsa.patch, trac_8469-review-rebased.patch\n\n(for patchbot)",
    "created_at": "2010-12-31T17:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76156",
    "user": "https://github.com/loefflerd"
}
```

Apply trac_8469-rsa.patch, trac_8469-review-rebased.patch

(for patchbot)



---

archive/issue_comments_076157.json:
```json
{
    "body": "I suspect that this patch needs to be rebased.  When I tried to apply [attachment:trac_8469-rsa.patch] to sage-4.7.rc3 I got\n\n\n\n```\nsage: hg_sage.apply(\"/home/mariah/trac_8469-rsa.patch\")\ncd \"/home/mariah/sage/sage-4.7.rc3-x86_64-Linux-core2-fc-review-8469/devel/sage\" && hg status\ncd \"/home/mariah/sage/sage-4.7.rc3-x86_64-Linux-core2-fc-review-8469/devel/sage\" && hg status\ncd \"/home/mariah/sage/sage-4.7.rc3-x86_64-Linux-core2-fc-review-8469/devel/sage\" && hg import   \"/home/mariah/trac_8469-rsa.patch\"\napplying /home/mariah/trac_8469-rsa.patch\npatching file doc/en/thematic_tutorials/index.rst\nHunk #1 FAILED at 16\n1 out of 1 hunks FAILED -- saving rejects to file doc/en/thematic_tutorials/index.rst.rej\nabort: patch failed to apply\nsage:\n```\n",
    "created_at": "2011-05-23T20:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76157",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

I suspect that this patch needs to be rebased.  When I tried to apply [attachment:trac_8469-rsa.patch] to sage-4.7.rc3 I got



```
sage: hg_sage.apply("/home/mariah/trac_8469-rsa.patch")
cd "/home/mariah/sage/sage-4.7.rc3-x86_64-Linux-core2-fc-review-8469/devel/sage" && hg status
cd "/home/mariah/sage/sage-4.7.rc3-x86_64-Linux-core2-fc-review-8469/devel/sage" && hg status
cd "/home/mariah/sage/sage-4.7.rc3-x86_64-Linux-core2-fc-review-8469/devel/sage" && hg import   "/home/mariah/trac_8469-rsa.patch"
applying /home/mariah/trac_8469-rsa.patch
patching file doc/en/thematic_tutorials/index.rst
Hunk #1 FAILED at 16
1 out of 1 hunks FAILED -- saving rejects to file doc/en/thematic_tutorials/index.rst.rej
abort: patch failed to apply
sage:
```




---

archive/issue_comments_076158.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-05-23T20:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76158",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076159.json:
```json
{
    "body": "This all looks very good.  I have posted a rebase of the main patch, it was just a matter of getting the table of contents aligned with new additions.\n\nThe \"Menezes\" citation appears twice, it seems to be in the bibliography for the Lie group stuff, so that needs to be removed.\n\nThe RSA bibliography appears as a section of its own at the same level as the different topics.  Maybe it should just be added directly into the new file of RSA material at the end?  (In other words, not in its own file that is included at a level I think is one too high.)\n\nI am at Bug Days 32 and this is on the list of priority tickets.  I can make a patch rearranging the bibliography or I can review a change.  If there is interest, please respond and let me know which approach to take.\n\nRob",
    "created_at": "2011-08-22T04:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76159",
    "user": "https://github.com/rbeezer"
}
```

This all looks very good.  I have posted a rebase of the main patch, it was just a matter of getting the table of contents aligned with new additions.

The "Menezes" citation appears twice, it seems to be in the bibliography for the Lie group stuff, so that needs to be removed.

The RSA bibliography appears as a section of its own at the same level as the different topics.  Maybe it should just be added directly into the new file of RSA material at the end?  (In other words, not in its own file that is included at a level I think is one too high.)

I am at Bug Days 32 and this is on the list of priority tickets.  I can make a patch rearranging the bibliography or I can review a change.  If there is interest, please respond and let me know which approach to take.

Rob



---

archive/issue_comments_076160.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-08-22T04:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76160",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_076161.json:
```json
{
    "body": "Attachment [trac_8469-rsa-rebase.patch](tarball://root/attachments/some-uuid/ticket8469/trac_8469-rsa-rebase.patch) by @rbeezer created at 2011-08-23 17:52:45",
    "created_at": "2011-08-23T17:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76161",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_8469-rsa-rebase.patch](tarball://root/attachments/some-uuid/ticket8469/trac_8469-rsa-rebase.patch) by @rbeezer created at 2011-08-23 17:52:45



---

archive/issue_comments_076162.json:
```json
{
    "body": "Attachment [trac_8469-rsa-bibliography.patch](tarball://root/attachments/some-uuid/ticket8469/trac_8469-rsa-bibliography.patch) by @rbeezer created at 2011-08-23 17:52:56",
    "created_at": "2011-08-23T17:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76162",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_8469-rsa-bibliography.patch](tarball://root/attachments/some-uuid/ticket8469/trac_8469-rsa-bibliography.patch) by @rbeezer created at 2011-08-23 17:52:56



---

archive/issue_comments_076163.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-08-23T17:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76163",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_076164.json:
```json
{
    "body": "Forgot to post the rebased patch.  That is fixed.\n\n\"rebase\" patch:  removes RSA bibliography file from top-level.  Reviewer should check that there is no \"bibliography.html\" at the same level as the four or five other tutorial files.  Still fixes rebasing problem.\n\n\"bibliography\" patch:  moves RSA bibliography to the end of the actual tutorial file.  Removed duplicate citation from the Lie group bibliography file.",
    "created_at": "2011-08-23T17:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76164",
    "user": "https://github.com/rbeezer"
}
```

Forgot to post the rebased patch.  That is fixed.

"rebase" patch:  removes RSA bibliography file from top-level.  Reviewer should check that there is no "bibliography.html" at the same level as the four or five other tutorial files.  Still fixes rebasing problem.

"bibliography" patch:  moves RSA bibliography to the end of the actual tutorial file.  Removed duplicate citation from the Lie group bibliography file.



---

archive/issue_comments_076165.json:
```json
{
    "body": "I read the patches and skimmed the produced HTML which suffices for me to give a positive review.",
    "created_at": "2011-08-23T19:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76165",
    "user": "https://github.com/malb"
}
```

I read the patches and skimmed the produced HTML which suffices for me to give a positive review.



---

archive/issue_comments_076166.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-23T19:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76166",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076167.json:
```json
{
    "body": "Changing keywords from \"RSA, public-key cryptosystem\" to \"RSA, public-key cryptosystem, sd32\".",
    "created_at": "2011-08-24T23:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76167",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "RSA, public-key cryptosystem" to "RSA, public-key cryptosystem, sd32".



---

archive/issue_comments_076168.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-12T19:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8469#issuecomment-76168",
    "user": "https://github.com/nexttime"
}
```

Resolution: fixed
