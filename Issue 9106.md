# Issue 9106: Wrong sphinx markup in UniqueRepresentation

Issue created by migration from https://trac.sagemath.org/ticket/9106

Original creator: hivert

Original creation time: 2010-05-31 19:06:21

Assignee: hivert

There are some missing "::"


---

Comment by hivert created at 2010-05-31 19:18:06

Changing status from new to needs_review.


---

Comment by hivert created at 2010-06-02 09:16:51

Changing keywords from "" to "UniqueRepresentation".


---

Comment by hivert created at 2010-06-02 09:16:51

Review went on sage-combinat queue. E-mail from Nicolas

```
Réciproquement, j'ai poussé un patch de revue pour #9106. S'il est ok
pour toi, tu peux fusionner et exporter sur trac, et zou.
```

Review patch merged an positively reviewed.


---

Attachment


---

Attachment

Sorry for uploading the wrong patch, I clic too fast...


---

Comment by hivert created at 2010-06-02 09:21:22

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-05 22:49:44

Resolution: fixed


---

Comment by mvngu created at 2010-06-24 18:02:54

The patch `trac_9106-UniqueRep_sphinx_fix-fh.patch` results in a failure to build the PDF version of the reference manual. See #9331 for a follow-up to this issue.
