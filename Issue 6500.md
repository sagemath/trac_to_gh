# Issue 6500: Improve reference manual coverage for polynomial rings

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-07-09 14:39:15

Assignee: tba

CC:  jhpalmieri mvngu

As of 4.1.rc1 very few of the polynomial ring classes are in the reference manual; even the basic constructor function is missing. 


---

Comment by davidloeffler created at 2009-07-09 14:54:53

The patch I've just uploaded Sphinxifies the docstrings of several modules in sage/rings/polynomial, and adds them to the reference manual.

(CCed to jhpalmieri and mvngu, as I know you have both contributed a great deal to improving the documentation in the past.)


---

Comment by mvngu created at 2009-07-09 15:08:18

Hi David,

Just a comment before I review your patch. Can you put your name on the patch? That way, you are identified as the patch's author and it makes it easy to credit you on release notes and release tours. Also, can you put in a commit message in your patch? A commit message should have the ticket number in it. I usually put the ticket number in front of any commit message I write. The template I follow is:

trac #n: <put commit message here>


---

Attachment

Well spotted -- I have uploaded another patch (overwriting the previous one) that has my username and a commit message on it. Thanks for the quick response.


---

Comment by davidloeffler created at 2009-07-10 14:29:22

apply over previous patch


---

Attachment

Here's another patch in the same vein, covering multivariate polynomial rings.


---

Comment by jhpalmieri created at 2009-07-20 02:31:13

Source code looks good and the documentation looks good.  I'm attaching a referee's patch which looks large, but the large majority of which contains repetitions of two changes: "EXAMPLE::" --> "EXAMPLES::" and ".::" --> ". ::" (a period followed by :: produces ".:" in the Sphinx documentation, while if you insert a space, no colons are printed).  Of the other changes, I think the only one worth mentioning is that I changed instances of the "param" command used in polynomial_singular_interface.py to INPUT blocks, for consistency with the rest of the documentation.

I don't think my patch needs much review, but I'll keep this marked as "needs review".  davidloeffler's two patches get positive reviews from me; if my patch is okay, the whole thing gets a positive review.


---

Attachment

apply over previous patches


---

Comment by jhpalmieri created at 2009-07-20 02:34:50

Changing type from defect to enhancement.


---

Comment by davidloeffler created at 2009-07-20 08:12:21

John's patch looks fine to me -- it applies without problems, the documentation builds without errors, and the formatting fixes all look sensible.


---

Comment by mvngu created at 2009-07-20 13:49:51

Resolution: fixed
