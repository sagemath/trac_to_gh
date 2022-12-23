# Issue 8469: add "Number Theory and the RSA Public Key Cryptosystem" to "Sage HOWTOs"

Issue created by migration from https://trac.sagemath.org/ticket/8469

Original creator: mvngu

Original creation time: 2010-03-07 02:25:47

Assignee: mvngu

CC:  malb

Keywords: RSA, public-key cryptosystem

Add the document [Number Theory and the RSA Public Key Cryptosystem](http://sites.google.com/site/nguyenminh2/numtheory-crypto-sage.pdf) to the documentation category "Sage HOWTOs". The original proposal can be found on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc).


---

Comment by mvngu created at 2010-03-10 06:00:14

Changing status from new to needs_review.


---

Comment by mjordan7 created at 2010-05-04 06:32:55

Looks good and builds fine. Nice job!
~Mark


---

Comment by pang created at 2010-05-12 15:36:03

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

Attachment


---

Comment by mvngu created at 2010-05-15 04:11:38

Replying to [comment:5 pang]:
> If this is reasonable to you, I'll be glad to write a patch, of course.

That would be nice. Thank you.





>  * A missing space was generating a minor problem with latex. I attach a patch only for that

Your patch looks OK to me.



Also, could you put your real name in the "Reviewer(s):" field? That way, it makes it easier to credit you for your contribution.


---

Attachment

The last patch includes the previous one (I can't find a wat to delete it).


---

Attachment

Only the last patch is needed. Sorry for the noise.


---

Attachment

based on Sage 4.5.2.rc0


---

Attachment

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
 1. Someone needs to sign off on [attachment:trac_8469-review-rebased.patch]. This is pang's original patch together with some typo fixes by me. I'm happy with pang's content. But someone other than myself needs to go over the fixes I included in this updated patch.


---

Comment by davidloeffler created at 2010-12-31 17:24:29

Apply trac_8469-rsa.patch, trac_8469-review-rebased.patch

(for patchbot)


---

Comment by mariah created at 2011-05-23 20:15:48

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

Comment by mariah created at 2011-05-23 20:15:48

Changing status from needs_review to needs_work.


---

Comment by rbeezer created at 2011-08-22 04:52:33

This all looks very good.  I have posted a rebase of the main patch, it was just a matter of getting the table of contents aligned with new additions.

The "Menezes" citation appears twice, it seems to be in the bibliography for the Lie group stuff, so that needs to be removed.

The RSA bibliography appears as a section of its own at the same level as the different topics.  Maybe it should just be added directly into the new file of RSA material at the end?  (In other words, not in its own file that is included at a level I think is one too high.)

I am at Bug Days 32 and this is on the list of priority tickets.  I can make a patch rearranging the bibliography or I can review a change.  If there is interest, please respond and let me know which approach to take.

Rob


---

Comment by rbeezer created at 2011-08-22 04:52:33

Changing status from needs_work to needs_info.


---

Attachment


---

Attachment


---

Comment by rbeezer created at 2011-08-23 17:56:28

Changing status from needs_info to needs_review.


---

Comment by rbeezer created at 2011-08-23 17:56:28

Forgot to post the rebased patch.  That is fixed.

"rebase" patch:  removes RSA bibliography file from top-level.  Reviewer should check that there is no "bibliography.html" at the same level as the four or five other tutorial files.  Still fixes rebasing problem.

"bibliography" patch:  moves RSA bibliography to the end of the actual tutorial file.  Removed duplicate citation from the Lie group bibliography file.


---

Comment by malb created at 2011-08-23 19:31:24

I read the patches and skimmed the produced HTML which suffices for me to give a positive review.


---

Comment by malb created at 2011-08-23 19:31:24

Changing status from needs_review to positive_review.


---

Comment by was created at 2011-08-24 23:44:59

Changing keywords from "RSA, public-key cryptosystem" to "RSA, public-key cryptosystem, sd32".


---

Comment by leif created at 2011-09-12 19:35:15

Resolution: fixed
