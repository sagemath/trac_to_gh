# Issue 7123: cryptanalysis of the shift cipher

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-10-05 15:56:07

Assignee: somebody

CC:  rbeezer

As the subject says.


---

Comment by rbeezer created at 2009-10-07 05:11:54

Hi Minh,

I'll try to give this a proper review soon.  Two thoughts - one I had before I saw this.

1.  Is there any infrastructure planned for frequency tables - ie perhaps given an alphabet and a language, a dictionary from "letters" to their probabilities in that language?  I could see this being veryuseful for some of the cryptanalysis, especially of the classical ciphers.

2.  Could you build on the exhaustive search in this patch, together with frequency information, to rank more likely keys first, and present more likely decipherments first?

Rob


---

Comment by mvngu created at 2009-10-08 15:27:22

The `trac_7123-clean-up.patch` does the following clean up on the file `sage/monoids/string_monoid_element.py`:

 1. Remove trailing white spaces.
 1. Adjust the module so it conforms to Python coding conventions.
 1. Use the functional form of raising exceptions so that the module more closely conform to Python 3.x.
 1. Remove the unused import statements
 {{{
import operator
from sage.structure.element import MonoidElement
 }}}


---

Comment by mvngu created at 2009-10-08 15:27:22

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2009-10-08 16:30:37

Replying to [comment:2 rbeezer]:
> 1.  Is there any infrastructure planned for frequency tables - ie perhaps given an alphabet and a language, a dictionary from "letters" to their probabilities in that language?  I could see this being veryuseful for some of the cryptanalysis, especially of the classical ciphers.
Frequency distribution is already implemented for the following alphabets: `AlphabeticStrings`, `BinaryStrings`, `HexadecimalStrings`, `OctalStrings`, `Radix64Strings`. The relevant method is `frequency_distribution()` in the class `StringMonoidElement` of the module `sage/monoids/string_monoid_element.py`. Here is an example:

```
[mvngu`@`sage sage-4.1.2.rc0-7123-shift]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: A = AlphabeticStrings()
sage: M = A.encoding("abcd")
sage: M.frequency_distribution()
Discrete probability space defined by {A: 0.250000000000000, C: 0.250000000000000, B: 0.250000000000000, D: 0.250000000000000}
```

As you can see, the default behaviour is to return the string representation of a frequency distribution. This can be difficult to parse, especially if one wants to do further processing with the returned distribution.
| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |




> 2.  Could you build on the exhaustive search in this patch, together with frequency information, to rank more likely keys first, and present more likely decipherments first?
Is there a way to determine likely keys? One way I can think of is to use an existing frequency distribution table T of the letters of the English alphabet. Given the frequency distribution of the ciphertext, sort the ciphertext letters in non-descending order in terms of probability values. Do the same sorting for the table T. Then map the ciphertext letter with the highest probability to its counterpart in T, etc. Can use the frequency table from the text:

 * Robert Edward Lewand. "Cryptological Mathematics". The Mathematical Association of America, 2000, p.36.

The same table can also be found on [wikipedia](http://en.wikipedia.org/wiki/Letter_frequencies). For digrams, trigrams, etc., one can use the US Army's field manual at

http://www.umich.edu/~umich/fm-34-40-2/


---

Comment by mvngu created at 2009-10-08 19:43:55

The patch `trac_7123-shift.patch` implements the following features for cryptanalysis of the shift cipher:

 1. In the class `StringMonoidElement` of the module `sage/monoids/string_monoid_element.py`, change the function `frequency_distribution()` so that it returns a dictionary of probability distribution. Up until this change, the default behaviour has been to return the string representation of the said distribution, which can be difficult to parse if one intends to parse that distribution for useful statistics. The behaviour of `frequency_distribution()` now is to return a dictionary that is easier to parse than previously.
 1. Add the method `characteristic_frequency()` to the module `sage/monoids/string_monoid.py` to return the relative frequencies of all letters of the English alphabet.
 1. The method `brute_force()` for the class `ShiftCryptosystem` to perform exhaustive key search. I have no idea how to order the possible keys by likelihood of being the key closest to the real key. A promising algorithm is via the chi-square statistic as presented at

 http://starbase.trincoll.edu/~crypto/historical/caesar.html

 Would you consider that OK to implement?


---

Comment by mvngu created at 2009-10-08 19:43:55

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2009-10-09 01:35:32

Replying to [comment:5 mvngu]:

Minh,

That's pretty much exactly what I had in mind.  And I'd forgotten to mention the Army Field Manual.  ;-)

The chi-square statistic does look like a likely candidate.  I'd also thought of taking the sum of the squared differences between the two distributions (the candidate decrypt frequency vs. the characteristic frequency).  Something makes me think that they may be equivalent, or one is clearly superior, but I don't have a reference, nor have I checked.  If they are different, then implementing both and testing one versus the other could be a good project for a user.  In any event, I think I'd code a choice of the function that "scores" each candidate decrypt, either with a default keyword, or in the extreme, an option to pass in your own function (assuming two arguments, the decrypt and the characteristic frequency).

OK, a bit brief, but I'm trying to beat the Sage infrastructure cutover in 25 minutes.  ;-)

Rob


---

Comment by rbeezer created at 2009-10-10 06:15:45

Hi Minh,

Finally have a chance to comment carefully on the various ways to measure the distributions.

1.  For a chi-square used for goodness-of-fit between distributions see Hogg and Tannis, Probbilit and Stastical Inference, 6th Ed., Section 8.4.  Use the actual counts of each letter in a candidate decipher and call these "observed."  Then multiply frequences from `frequency_distribution()` times the length of the message.  Call these theoretical counts the "expected" and carry them as non-integers, even if we know they should be integral.  Then the statistic is the sum over all the letters of

`(observed - expected)^2/expected`

I would use the keyword "chisquare" for this.

2.  The sum of squared differences should probably be computed as the sum over all letters using counts, not frequencies, ie

`(observed - expected)^2`

This is equivalent in this case to the coefficient of determination, or more informally "r-squared."  Another name is "residual sum of squares."

3.  Not at all clear to me how [SavHar99] justifies the use of their expression and naming it a chi-square statistic.  If anything, it looks to me like a noncentral chisquare statistic.  But it may do a good job of "scoring" candidate decipherments.  Can you be sure if they mean to square just the numerator of each term (`FD^2/CD`), or square the whole fraction (`FD/CF`)?

Rob


---

Comment by mvngu created at 2009-10-10 13:15:50

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2009-10-10 14:28:41

Replying to [comment:7 rbeezer]:
> 1.  For a chi-square used for goodness-of-fit between distributions see Hogg and Tannis, Probbilit and Stastical Inference, 6th Ed., Section 8.4.  Use the actual counts of each letter in a candidate decipher and call these "observed."

Let's call these actual counts the "character count".





> Then multiply frequences from `frequency_distribution()` times the length of the message.  

There are two types of frequencies. The characteristic frequency distribution (or characteristic frequency, for short) of an alphabet is the expected frequency probability distribution for that alphabet. The book by Beker and Piper 1982 contains a table describing this probability distribution. The book by Lewand 2000 also contains such a table. The frequency distribution of a message `M` (or frequency distribution, for short) gives the ratio `R` of character occurrences over message length:

```
R = (number of occurrences of a character) / (message length)
```

The characteristic frequency can be thought of as the expected probability, while the frequency distribution is the observed probability.





> Call these theoretical counts the "expected" and carry them as non-integers, even if we know they should be integral.
 
With the above distinction between characteristic frequency (of an alphabet) and frequency distribution (of a message), I interpret the theoretical counts you mention here as the result of multiplying each probability value in the characteristic frequency by the message length. For example:

```
sage: A = AlphabeticStrings()
sage: M = A.encoding("abcabf")
sage: L = len(M); L
6
sage: CF = A.characteristic_frequency()
sage: sorted(CF.items())

[('A', 0.0820000000000000),
 ('B', 0.0150000000000000),
 ('C', 0.0280000000000000),
 ('D', 0.0430000000000000),
 ('E', 0.127000000000000),
 ('F', 0.0220000000000000),
 ('G', 0.0200000000000000),
 ('H', 0.0610000000000000),
 ('I', 0.0700000000000000),
 ('J', 0.00200000000000000),
 ('K', 0.00800000000000000),
 ('L', 0.0400000000000000),
 ('M', 0.0240000000000000),
 ('N', 0.0670000000000000),
 ('O', 0.0750000000000000),
 ('P', 0.0190000000000000),
 ('Q', 0.00100000000000000),
 ('R', 0.0600000000000000),
 ('S', 0.0630000000000000),
 ('T', 0.0910000000000000),
 ('U', 0.0280000000000000),
 ('V', 0.0100000000000000),
 ('W', 0.0230000000000000),
 ('X', 0.00100000000000000),
 ('Y', 0.0200000000000000),
 ('Z', 0.00100000000000000)]
sage: keys = CF.keys()
sage: for k in keys:
....:     CF[k] *= L
....:     
sage: sorted(CF.items())

[('A', 0.492000000000000),
 ('B', 0.0900000000000000),
 ('C', 0.168000000000000),
 ('D', 0.258000000000000),
 ('E', 0.762000000000000),
 ('F', 0.132000000000000),
 ('G', 0.120000000000000),
 ('H', 0.366000000000000),
 ('I', 0.420000000000000),
 ('J', 0.0120000000000000),
 ('K', 0.0480000000000000),
 ('L', 0.240000000000000),
 ('M', 0.144000000000000),
 ('N', 0.402000000000000),
 ('O', 0.450000000000000),
 ('P', 0.114000000000000),
 ('Q', 0.00600000000000000),
 ('R', 0.360000000000000),
 ('S', 0.378000000000000),
 ('T', 0.546000000000000),
 ('U', 0.168000000000000),
 ('V', 0.0600000000000000),
 ('W', 0.138000000000000),
 ('X', 0.00600000000000000),
 ('Y', 0.120000000000000),
 ('Z', 0.00600000000000000)]
```


Multiplying each probability value in the frequency distribution by the message length would result in the counts of character occurrences:

```
sage: char_counts = M.character_count()
sage: sorted(char_counts.items())
[(A, 2), (B, 2), (C, 1), (F, 1)]
sage: FD = M.frequency_distribution()
sage: sorted(FD.items())

[(A, 0.333333333333333),
 (B, 0.333333333333333),
 (C, 0.166666666666667),
 (F, 0.166666666666667)]
sage: keys = FD.keys()
sage: for k in keys:
....:     FD[k] *= L
....:     
sage: sorted(FD.items())

[(A, 2.00000000000000),
 (B, 2.00000000000000),
 (C, 1.00000000000000),
 (F, 1.00000000000000)]
sage: sorted(char_counts.items())
[(A, 2), (B, 2), (C, 1), (F, 1)]
```






>  Then the statistic is the sum over all the letters of
> 
> `(observed - expected)^2/expected`

This agrees with Pearson's chi-square test at

http://en.wikipedia.org/wiki/Goodness_of_fit





> I would use the keyword "chisquare" for this.

No problem.





> 2.  The sum of squared differences should probably be computed as the sum over all letters using counts, not frequencies, ie
> 
> `(observed - expected)^2`

No problem.





> This is equivalent in this case to the coefficient of determination, or more informally "r-squared."  Another name is "residual sum of squares."
> 
> 3.  Not at all clear to me how [SavHar99] justifies the use of their expression and naming it a chi-square statistic.  If anything, it looks to me like a noncentral chisquare statistic.  But it may do a good job of "scoring" candidate decipherments.  Can you be sure if they mean to square just the numerator of each term (`FD^2/CD`), or square the whole fraction (`FD/CF`)?
The description at

http://starbase.trincoll.edu/~crypto/historical/caesar.html

is mostly textual and ambiguous. I would implement the above statistics you suggested as they are much more concrete and well specified, instead of spending time teasing out the "right" formula from the textual description.


---

Comment by rbeezer created at 2009-10-10 18:49:08

Minh,

Perfect.  I've been reading through the patches, but I'll put them through a full review once the changes are done.

Rob


---

Comment by mvngu created at 2009-10-11 00:36:59

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2009-10-11 07:00:37

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2009-10-11 07:00:37


```
22:11 < rbeezer> found the problem - you are decrypting/shifting too much
22:12 < rbeezer> try this - change     AlphShifted = self.enciphering(key, Alph)
22:12 < rbeezer> to  AlphShifted = self.enciphering(0, Alph)
22:22 -!- homerj [n=homerj`@`207-255-12-114-dhcp.jst.pa.atlanticbb.net] has left #sage-devel ["Leaving"]
22:41 < rbeezer> mvngu: any luck?
23:00 < mvngu> rbeezer: I'm not convinced about the change.
23:01 < rbeezer> mvngu: Ideally, I think you want   RMk = [(OM[AlphShifted[StrAlph.index(e)]] - EA[e])**2 / EA[e] for e in StrAlph]
23:01 < rbeezer> to read more like:  RMk = [(OM[e] - EA[e])**2 / EA[e] for e in StrAlph]
23:01 < rbeezer> but when I made this change, the indices of OM and EM were different types and I got errors
23:02 < mvngu> rbeezer: That's what I thought, and originally implemented for the method at http://starbase.trincoll.edu/~crypto/historical/caesar.html
23:03 < rbeezer> changing the statement before  (key -> 0)  was just a hack to negate the whole shifting in AlphShifted
23:03 < rbeezer> With  key->0  I was getting good results with short test phrases
23:05 < mvngu> rbeezer: Have you looked at the formula for RMk? See the formula at http://sage.math.washington.edu/home/mvngu/reference-7123-shift/sage/crypto/classical.html#sage.crypto.classical.ShiftCryptosystem.rank_by_chi_square  I was following that formula.
23:06 < mvngu> In particular, this formula  http://sage.math.washington.edu/home/mvngu/reference-7123-shift/_images/math/d8a2fd0995ed8152cfa73a6e16fcab0ef367a993.png
23:06 < rbeezer> mvngu: the formula in that doc shouldn't have the +k, I think
23:07 < rbeezer> mvngu: the starbase stuff is using the +k to decrypt, I think
23:07 < rbeezer> mvngu: while you have the brute_force output as an input to your routine, so the decryption has already happened
23:08 < rbeezer> the starbase stuff is not complete enough, or careful enough, to give me any confidence
23:09 < mvngu> rbeezer: What's "starbase stuff"?
23:09 < rbeezer> did you test my original hackish change?
23:09 < mvngu> rbeezer: "*="
23:09 < mvngu> ?
23:09 < rbeezer> the link at starbase.trincoll.edu  ;-)
23:10 < mvngu> rbeezer: testing your change now...
23:14 < williamstein> I made a lot of progress on the notebook "rewrite" today...
23:14 < williamstein> and finally those VirtualBox machines are working!
23:14 < williamstein> There are also now 8949 sagenb.org users.
23:15 < williamstein> Only 51 more to 9000.
23:18 < mvngu> rbeezer: Your change certainly gives better results now. See my transcript at http://sage.math.washington.edu/home/mvngu/chi-square-rbeezer-hack.txt
23:19 -!- wormsxulla [i=chatzill`@`unaffiliated/wormsxulla] has quit [Read error: 110 (Connection timed out)]
23:19 -!- wormsxulla_ [i=chatzill`@`unaffiliated/wormsxulla] has joined #sage-devel
23:19 -!- wormsxulla_ is now known as wormsxulla
23:19 < rbeezer> mvngu: that's what I was seeing
23:19 < mvngu> rbeezer: Now for a text file...
23:20 < rbeezer> mvngu: your strings from brute_force() have already been shifted, you just want the one whose letter distribution most closely matches that of English
23:21 < rbeezer> but right now OM and EM are indexed by letters versus one-character stings, or somthing like that
23:21 < rbeezer> s/strings/stings/
23:23 < mvngu> rbeezer: Result from using a file... Looks good. See transcript at http://sage.pastebin.com/m6e4d8df4
23:24 < rbeezer> yep, that's it - the Pearson chi-square should give good results for short and long messages

```



---

Comment by mvngu created at 2009-10-11 08:29:33

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2009-10-12 05:49:22


```
22:43 < rbeezer> mvngu: but I did have one suggestion - the first paragraph of
                 each ranking method
22:43 < mvngu> rbeezer: Fire away your suggestion.
22:43 < rbeezer> calls FM the frequency for an encrypted message, when what you
                 are really doing is getting a pile of candidate decrypted
22:44 < rbeezer> messages from the brute_force() method and analyzing their
                 freguencies
22:44 < rbeezer> You want the key that makes a decrypt with frequencey most
                 like english
22:45 < rbeezer> So maybe before FM you say it is for a "decrypted" or
                 "candidate decrypted" message
22:46 -!- Serica [i=815dcecd`@`gateway/web/freenode/x-awudwwybpvbxuikl] has quit 
          [Ping timeout: 180 seconds]
22:47 < mvngu> rbeezer: That sounds logical; I'll put it in now.
22:47 < rbeezer> Or you can wait until I do a full review and take care of 
                 everything at once
22:47 < mvngu> rbeezer: OK. Let's work on the Mercurial issue now.
```



---

Comment by mvngu created at 2009-10-12 19:05:41

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2009-10-13 01:47:22

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2009-10-13 05:16:33

Changing status from needs_review to needs_work.


---

Comment by rbeezer created at 2009-10-13 05:16:33

Hi Minh,

This is looking real good.  Just some details and questions:

1.  In the first paragraph of the doc string for `characteristic_frequency()` you talk about plaintext and ciphertext.  Not sure somebody looking at this monoid code will be doing crypto.  Could you make the description more confined to properties of the monoid - just describe it as a property of letters in English usage?  The distinction with the `frequency_distribution()` is very good, so retain that.

2.  Does `frequency_distribution()` need documentation on its inputs?  And should you change the nature of the output?  Perhaps you should stick to returning a probability space, and then just call `function()` on it as needed to get the dictionary you want.  Maybe somebody else will want to get something different from the probability distribution and want the more general object?  In any event, the first line of the docstring doesn't match the behavior.

3.  Looked like there were some stray commented-out code statements in the cryptanalysis code?  Maybe you could review those and take out any that might be misleading.

4.  You probably don't need to give me credit for the chi-square and squared-differences stuff, they are pretty standard measures of differences.  I also found the [SavHar99] reference more misleading than helpful.

5.  On to affine cipher......

Rob


---

Comment by mvngu created at 2009-10-13 05:35:50

Replying to [comment:17 rbeezer]:
> This is looking real good.  Just some details and questions:

I'm now addressing your comments.


---

Attachment

based on Sage 4.1.2.rc0 and #7010


---

Attachment

apply on top of previous


---

Comment by mvngu created at 2009-10-13 22:01:07

Replying to [comment:17 rbeezer]:
> 1.  In the first paragraph of the doc string for `characteristic_frequency()` you talk about plaintext and ciphertext.  Not sure somebody looking at this monoid code will be doing crypto.  Could you make the description more confined to properties of the monoid - just describe it as a property of letters in English usage?  The distinction with the `frequency_distribution()` is very good, so retain that.

Done. The documentation for `characteristic_frequency()` has been re-written to describe properties of a monoid. No more mentions of plaintext or ciphertext. I have also made a slight coding change to that function to increase its readability.





> 2.  Does `frequency_distribution()` need documentation on its inputs?  

Done. I have documented the parameters of the method `frequency_distribution()` and provided an example illustrating how to use the key word "length".





> And should you change the nature of the output?  Perhaps you should stick to returning a probability space, and then just call `function()` on it as needed to get the dictionary you want.  Maybe somebody else will want to get something different from the probability distribution and want the more general object?  In any event, the first line of the docstring doesn't match the behavior.

Done. The method `frequency_distribution()` now returns a probability space. In order to get the frequency probability distribution, use `frequency_distribution().function()`.





> 3.  Looked like there were some stray commented-out code statements in the cryptanalysis code?  Maybe you could review those and take out any that might be misleading.

Fixed.





> 4.  You probably don't need to give me credit for the chi-square and squared-differences stuff, they are pretty standard measures of differences.  I also found the [SavHar99] reference more misleading than helpful.

Fixed. I now only reference the Wikipedia articles on the Pearson chi-square test, and the residual sum of squares measure.


---

Comment by mvngu created at 2009-10-13 22:01:07

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2009-10-14 06:27:29

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2009-10-14 06:27:29

Minh,

Looks real good.

Builds, passes all tests, documentation is a model everybody should look at.

Positive review.

Rob


---

Comment by rbeezer created at 2009-10-14 06:27:29

Changing keywords from "" to "cryptanalysis shift".


---

Comment by mhansen created at 2009-10-19 07:17:35

Changing status from positive_review to needs_work.


---

Attachment

This doesn't work after the changes in #7198.


---

Comment by mhansen created at 2009-10-19 07:17:52

I've attached a patch which fixes the issue.


---

Comment by mhansen created at 2009-10-19 07:17:52

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2009-10-19 08:31:06

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2009-10-19 08:31:06

The patch `trac_7123-iter.patch` looks good. Doctesting the whole Sage library, the only failure I got is the following:

```
sage -t -long devel/sage/sage/modules/vector_double_dense.pyx
**********************************************************************
File "/scratch/mvngu/sage-4.2.alpha0-sage.math/devel/sage-main/sage/modules/vector_double_dense.pyx", line 663:
    sage: v.stats_kurtosis()
Expected:
    -1.23
Got:
    doctest:106: SyntaxWarning: assertion is always true, perhaps remove parentheses?
    -1.23
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_29
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_vector_double_dense.py
         [2.5 s]
```

This doctest passed on a second try.


---

Comment by mhansen created at 2009-10-19 13:31:50

Since #7198 was backed out, I only merged trac_7123-clean-up.patch and trac_7123-shift.patch.


---

Comment by mhansen created at 2009-10-19 13:31:50

Resolution: fixed
