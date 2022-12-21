# Issue 1169: NTL cache-friendly FFT routines

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-11-14 14:48:16

Assignee: somebody

CC:  vbraun

I've written a more cache-friendly version of NTL's FFT routines. This may speed up NTL's polynomial arithmetic for polynomials of very high degree (e.g. > 100000) with small coefficients. For example I get a speedup of about 2x on sage.math.

BEFORE INCLUDING IN SAGE, someone needs to write some automatic tuning code, otherwise it might GREATLY SLOW DOWN arithmetic for small polynomials, which would be very stupid. See my website for code and more details:

http://math.harvard.edu/~dmharvey/code/ntl-fft/



---

Comment by mabshoff created at 2008-11-28 08:54:42

David,

what is the status here? It seems that your website does contain the code.

Cheers,

Michael


---

Comment by dmharvey created at 2008-11-28 13:31:28

Yes it does, but it doesn't have tuning code and I don't have time to work on it now. Without proper tuning it is just as likely to make things slower.


---

Comment by jpflori created at 2013-10-09 09:15:50

Changing status from new to needs_review.


---

Comment by jpflori created at 2013-10-09 09:15:50

I think this code has been integrated (somehow) into NTL 6.0.
So #14876 should supercede this.


---

Comment by jpflori created at 2013-12-31 12:24:33

NTL 6.0.0 is on its way.


---

Comment by jpflori created at 2013-12-31 12:24:33

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-01-04 02:22:13

Resolution: duplicate
