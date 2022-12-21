# Issue 5357: typos in library file; Sage 3.3

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-02-24 08:08:58

Assignee: tba

CC:  mhansen

A bunch of typos found in Sage 3.3 library files, in particular files under the following directories:


 * sage/algebras
 * sage/calculus
 * sage/coding
 * sage/combinat
 * sage/crypto
 * sage/databases

The typos are fairly trivial to review.


---

Comment by mvngu created at 2009-02-24 08:09:58

fixed typos in files under sage/algebras


---

Attachment

fixed typos in files under sage/calculus


---

Attachment

fixed typos in files under sage/coding


---

Attachment

fixed typos in files under sage/combinat; part 1


---

Comment by mvngu created at 2009-02-24 08:11:44

fixed typos in files under sage/combinat; part 2


---

Attachment

fixed typos in files under sage/crypto


---

Comment by mvngu created at 2009-02-24 08:12:26

fixed typos in files under sage/databases


---

Attachment


---

Comment by mabshoff created at 2009-02-24 12:57:05

Hi Minh,

the timing of these patches is rather unfortunate since they are against the old codebase without the ReST patches. Since that patches have preference about anything else two thing can happen:

 * Mike Hansen integrates the fixes into the ReST patch set
 * someone will need to rebase these patches for Sage 3.4.1.

Cheers,

Michael


---

Comment by mvngu created at 2009-02-24 23:24:49

Replying to [comment:2 mabshoff]:
> Hi Minh,
> 
> the timing of these patches is rather unfortunate since they are against
> the old codebase without the ReST patches. Since that patches have
> preference about anything else two thing can happen:
> 
>  * Mike Hansen integrates the fixes into the ReST patch set
>  * someone will need to rebase these patches for Sage 3.4.1.
No problem. Leave the attached fixes as is and don't integrate them into 3.4. I don't want to further delay the ReSTification of the documentation and hence the release of 3.4 with that beautifully formatted standard documentation. I'll try to rebase the above patches for 3.4.1.


---

Comment by mhansen created at 2009-02-24 23:25:49

Actually, I can take care of it as I had already made a number of the SAGE -> Sage changes.


---

Attachment

Looks good to me.  I made a rebased trac_5357.patch.


---

Comment by mhansen created at 2009-02-28 17:25:02

(Just merge trac_5357.patch)


---

Comment by mabshoff created at 2009-02-28 22:32:40

Merged in Sage 3.4.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-28 22:32:40

Resolution: fixed
