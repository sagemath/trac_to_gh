# Issue 6164: Phan's Mini-AES for educational purposes

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-05-31 04:21:30

Assignee: somebody

CC:  malb

Keywords: Mini-AES, AES, cryptography

To facilitate the learning of cryptography (in particular the Advanced Encryption Standard), it's a good idea to add a class to allow students to explore the working of a block cipher. The goal here is to implement the Mini-AES block cipher of Phan as described in the paper:

 R. C.-W. Phan. Mini advanced encryption standard (mini-AES): a testbed for cryptanalysis students. Cryptologia, 26(4):283--306, 2002.

This is a simplified variant of the AES to be used for cryptography education.


---

Comment by mvngu created at 2009-05-31 04:25:41

I'm CC'ing Martin, as he's the only person I know who might be interested in reviewing this ticket.


---

Comment by malb created at 2009-05-31 12:50:01

Hi, how does the MiniAES compare to the small scale AES variants already in Sage? I guess, they should at least re-use the same building blocks. e.g. there is an S-Box class which might be worth using, some of the functions might do the same etc.


---

Comment by mvngu created at 2009-06-01 01:15:48

Replying to [comment:2 malb]:
> Hi, how does the MiniAES compare to the small scale AES variants already in Sage? 


As you know, Mini-AES was designed as a very small scale variant of the AES. It can be used to teach crypto to computer science students who don't have the necessary maths background to understand finite fields and (basic) abstract algebra. Ideally, such students should have taken at least two courses in basic calculus, and at least two courses in programming. As I see it, Mini-AES and the implementation contained in the patch require "minimum" maths background for crypto students to work through the processes of encryption and decryption. As noted in the paper



C. Cid, S. Murphy, and M. Robshaw. Small scale variants of the AES. In Proceedings of Fast Software Encryption 2005. LNCS 3557, Springer Verlag, 2005.



Mini-AES and the simplified AES variant by Musa, Schaefer, and Wedig have been designed for teaching purposes. On the other hand, the small scale variants of the AES by Cid, Murphy, and Robshaw have been designed as a framework for cryptanalysis and comparing different cryptanalytic techniques that can be brought to bear on the AES or its small scale variants. As I see it, the small scale variants of Cid et al. require far more advanced maths to describe and use. To be fair, the simplified variant by Musa et al. also requires far too much advanced maths than is suitable for someone who requires a basic understanding of how AES works. 



What I want to do with the patch is to implement a variant of the AES that fits in with Neal Koblitz's idea of Kid Krypto, where one should not require too much advanced maths to describe the working of a cryptosystem. Each method of the class `MiniAES` is designed so that a student can follow through the whole processes of encryption and decryption, one step at a time. But the class also has a callable that a student can use to perform encryption or decryption in one step.



> I guess, they should at least re-use the same building blocks. e.g. there is an S-Box class which might be worth using, some of the functions might do the same etc.


Yes. You got me there. I see what I can do to re-use the building blocks in `sage/crypto/mq/sr.py`


---

Comment by malb created at 2009-06-01 09:46:22

Replying to [comment:3 mvngu]:
Thanks for reminding me about the differences between SR and MiniAES. I am not opposed to have the MiniAES in Sage, on the contrary I very much support it. We should have some clear docs somewhere to make sure that users don't get confused about the various AES variants we have. 

> > I guess, they should at least re-use the same building blocks. e.g. there is an S-Box class which might be worth using, some of the functions might do the same etc.
> Yes. You got me there. I see what I can do to re-use the building blocks in `sage/crypto/mq/sr.py`

`mq.SR` does not really make use of the S-Box class (since the S-Box is so structured). Have a look at `mq.SBox` (a weird place for that class, I know), it seems it would be useful for your purposes. Also, this class also gives you difference distribution tables etc. for free.

Btw.   ``\text{GF}(2^4)`` should now be ``\GF{2^4}``.


---

Comment by mvngu created at 2009-06-01 14:02:25

Replying to [comment:4 malb]:
> Replying to [comment:3 mvngu]:
> Thanks for reminding me about the differences between SR and MiniAES. I am not opposed to have the MiniAES in Sage, on the contrary I very much support it. We should have some clear docs somewhere to make sure that users don't get confused about the various AES variants we have. 


I'm on it. I anticipate changing/adding to the documentation of `sage/mq/sr.py` and my patch.



> `mq.SR` does not really make use of the S-Box class (since the S-Box is so structured). Have a look at `mq.SBox` (a weird place for that class, I know), it seems it would be useful for your purposes. Also, this class also gives you difference distribution tables etc. for free.


Thanks for the pointer. And for free courtesy of Martin :-)



> Btw.   ``\text{GF}(2^4)`` should now be ``\GF{2^4}``.


Duly noted.


---

Comment by mvngu created at 2009-06-17 00:16:08

The patch uses the S-box implementation in `sage/crypto/mq/sbox.py` for constructing the S-box of Mini-AES. It also distinguishes Mini-AES from SR, as implemented in `sage/crypto/mq/sr.py`.


---

Comment by malb created at 2009-06-17 20:07:14

*Review Report*

* as mentioned earlier, the module is beautifully documented. This is really nice!
* I am wondering whether it would be better to have a directory `block_cipher` with a file `miniaes.py` inside instead of `block_cipher.py`?
* I guess it would be nice to have a function `sbox` which returns the encryption S-Box for further study?
* AFAIK, we agreed to not use `\leq` but `<=` instead, because our users might not speak LaTeX
* same for `\times`
* why are you more strict wrt types in `__call__` than in `encrypt`?
* `D = \sigma_{K_0} \circ \gamma^{-1} \circ \pi \circ \theta \circ \sigma_{K_1} \circ \gamma^{-1} \circ \pi \circ \sigma_{K_2} ` isn't exactly easily readable, but I guess it looks nice in the reference manual. Maybe there is some compromise though?
* Maybe http://sphinx.pocoo.org/markup/misc.html#dir-tabularcolumns is a good alternative to LaTeX tabular for readability?

Note, that most of the above are recommendations, not requirements. This ticket is much better documented than almost every other module in Sage!


---

Comment by mvngu created at 2009-06-17 20:53:18

Replying to [comment:7 malb]:
> *Review Report*
> * I am wondering whether it would be better to have a directory `block_cipher` with a file `miniaes.py` inside instead of `block_cipher.py`?
That can be arranged.




> * I guess it would be nice to have a function `sbox` which returns the encryption S-Box for further study?
You read my mind. I forgot to add that. Man, it's early in the morning over here :-)




> * AFAIK, we agreed to not use `\leq` but `<=` instead, because our users might not speak LaTeX
> * same for `\times`
Let's leave them in for now and see how users react.




> * why are you more strict wrt types in `__call__` than in `encrypt`?
The methods `encrypt` and `decrypt` are meant to deal with only 16-bit blocks of data, so they're very limited in the length of their input. As their input are matrices over a finite field, I think the structure of the input and output mimics how a student would go through the encryption/decryption by hand. If they rather work with integers than finite field elements, they could use the provided conversion methods.

The callable `__call__` is designed for performing encryption/decryption in one go, operating mainly on binary strings. So once someone is comfortable with how Mini-AES works, they can encrypt binary strings longer than 16 bits in length, which is at present not possible with the `encrypt` and `decrypt` methods. You can think of `__call__` as being there to do Mini-AES encryption/decryption on arbitrary data, while `encrypt` and `decrypt` aid in understanding the corresponding processes on a small scale, i.e. on 16-bit blocks.




> * `D = \sigma_{K_0} \circ \gamma^{-1} \circ \pi \circ \theta \circ \sigma_{K_1} \circ \gamma^{-1} \circ \pi \circ \sigma_{K_2} ` isn't exactly easily readable, but I guess it looks nice in the reference manual. Maybe there is some compromise though?
I'm not sure. It's meant as a specification of the decryption process.




> * Maybe http://sphinx.pocoo.org/markup/misc.html#dir-tabularcolumns is a good alternative to LaTeX tabular for readability?
Sure. Let me try that one for a change.


---

Comment by mvngu created at 2009-06-18 21:23:49

Fixed the following issues raised by malb:
 * Mini-AES is now under the directory `sage/crypto/block_cipher`
 * add the function `sbox()` to return the S-box of MiniAES

I still use LaTeX markup for tables, as the `tabularcolumns` tag of Sphinx doesn't give the effect I want, at least I can't figure out how to do so.


---

Comment by malb created at 2009-06-20 12:49:53

Replying to [comment:8 mvngu]:
> > * AFAIK, we agreed to not use `\leq` but `<=` instead, because our users might not speak LaTeX
> > * same for `\times`
> Let's leave them in for now and see how users react.

It is somewhere in the developer docs that we should expect users to speak LaTeX, so I'd recommend to change that. I'll give the patch a positive review and leave it to your decision to follow this advise or not.


---

Comment by malb created at 2009-06-24 14:27:38

Doctests fail in 4.1.alpha0:


```
sage: maes = MiniAES()
NameError: name 'MiniAES' is not defined
```



---

Comment by mvngu created at 2009-06-24 21:53:30

based on Sage 4.1.alpha0


---

Attachment

Can you try again with the new patch?


---

Comment by malb created at 2009-06-24 22:35:55

Yep that works! positive review again!


---

Comment by boothby created at 2009-06-26 17:45:53

Resolution: fixed
