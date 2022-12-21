# Issue 7235: os x readme file is misleading

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-17 19:43:21

Assignee: tbd


```
>> There is definitely no way the 10.6 OS X binary will work on OS X
>> 10.4, and I would find it highly unlikely that it would work on 10.5
>> either.  If the readme says that, it is very misleading (I think the
>> readme is  refering to the source code).
>
> The ReadMe says that.

I see it says:

**
  These binaries are only for OS X 10.4 or 10.5.  They will not work on OS X 10.3. 
**

However, that's simply wrong, since the binaries are only for the platform listed in the name of the dmg.  Argh.  That needs to be changed.  (I was thinking of a different README file when I wrote my response.)    Thanks for the bug report.

William
```



---

Comment by was created at 2009-10-18 01:36:42

We might say: "These binaries are only for the OS X version that is indicated by the
package .dmg name.
They generally will not work on any other OS X version (unless
explicitly stated otherwise)."


---

Comment by GeorgSWeber created at 2009-10-23 21:00:58

See ticket #5296 for related work on the age-worn OS X Readme.


---

Comment by GeorgSWeber created at 2009-10-24 19:36:20

See also this thread on sage-support about naming conventions:

http://groups.google.com/group/sage-support/browse_thread/thread/4c6fc409f60053f4#

BTW, on the Sage download page side-by-side with the Mac binaries (.dmg's), there is a README.txt file reading:

```
NOTE: the OS X 10.4 binary works fine on OS X 10.5. 
```

One might put more information there, too.


---

Attachment

I changed the line as suggested by Georg Weber.  I agree with his suggestion.


---

Comment by was created at 2009-11-11 19:12:51

Changing status from new to needs_review.


---

Comment by was created at 2009-11-11 19:12:51

I think I can just give this a positive review, since I just put what GeorgSWeber suggested in the README.


---

Comment by was created at 2009-11-11 19:13:17

Changing status from needs_review to positive_review.


---

Comment by GeorgSWeber created at 2009-11-11 19:37:18

I must admit I'm a bit flattered. However, I'm not the author of the one-line change suggested and incorporated in the new file, as one can see in the change history's first entry.

On the other hand, we *do* agree on what to do, so I confirm that the issue at hand has a positive review.  :-)


---

Comment by mhansen created at 2009-11-12 06:07:17

Resolution: fixed
