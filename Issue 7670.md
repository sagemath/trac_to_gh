# Issue 7670: notebook -- evidently only the first 6 characters are significant???

Issue created by migration from https://trac.sagemath.org/ticket/7670

Original creator: was

Original creation time: 2009-12-12 00:22:38

Assignee: was


```
Hi,

There is a password issue with sage notebook account. Please read below:

Sameer

On Fri, Dec 11, 2009 at 1:22 PM, Sameer Regmi <> wrote:
> On Fri, Dec 11, 2009 at 1:16 PM, Ondrej Certik <> wrote:
>> On Fri, Dec 11, 2009 at 1:12 PM, Sameer <> wrote:
>>> Hi I have found a weird issue with FEMhub online lab account. Let's
>>> say my password is "nevada". Then whenever I enter any text (in
>>> password field) with nevada as the prefix it will login. That means if
>>> I enter nevada123 (or whatever as the suffix) it will
>>> login.
>>
>> Seems like a bug in the Sage notebook. Could you please try to verify
>> this against sagenb.org and if the problem is in there as well,
>> could you please report it to the sage notebook list?
>
> Exactly! Its the bug in Sage notebook. The issue is there in sagenb.org too.
> I even can login with "nevad" if the password is of nevada. I am
> reporting to sage notebook list
>
> Sameer
```



---

Comment by mpatel created at 2009-12-12 17:02:33

Could the problem be `sagenb.notebook.user.User`'s use of [crypt](http://docs.python.org/library/crypt.html):

```python
>>> import crypt
>>> crypt.crypt('abcdefgh', 'aa')
'aaHHlPHAM4sjs'
>>> crypt.crypt('abcdefghi', 'aa')
'aaHHlPHAM4sjs'
```

?


---

Comment by mpatel created at 2009-12-12 19:19:13

But [crypt](http://docs.python.org/library/crypt.html) supports whatever the OS's underlying [crypt(3)](http://www.kernel.org/doc/man-pages/online/pages/man3/crypt.3.html) supports.  We could instead do, e.g.,

```python
import crypt as c, random as r
salt = repr(r.random())[2:]
'77551456940940877'
c.crypt('abcdefgh', '$6$' + salt + '$')
'$6$7755145694094087$uW0RGjvJG3I.BDFKIAieUTPZkD4IGI6b8RtLt1fZ9czR0TefjriLwRGPItgPyZogDFsy.YorN24v2GM4YrBwK0'
c.crypt('abcdefghi', '$6$' + salt + '$')
'$6$7755145694094087$txEQuYAJlZ.042gqmPTeLSczXBv1sI6kSjzpbmU7o89rh.Tk7qUGHhLHtL1GIrVXmUdFrQBuIefktTTptuEq31'
```

If Linux and Mac OS X, at least, both support SHA-512, I suggest we use it by default.  Should we generate each user's pseudo-random "salt" --- [used to avoid clustering](http://stackoverflow.com/questions/536584/non-random-salt-for-password-hashes) --- differently than above?


---

Comment by kcrisman created at 2014-09-17 02:15:33

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-09-17 02:15:33

I cannot replicate this, and it is so old I am going to ask to close this.


---

Comment by kcrisman created at 2014-09-17 02:15:40

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-09-18 17:58:47

Resolution: invalid
