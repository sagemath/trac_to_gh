# Issue 2767: error in elem.matrix(F) and elem.norm(F) for F == elem.parent() a number field

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-04-02 04:54:31

Assignee: was

CC:  ncalexan

Keywords: number field norm matrix


```
sage: F.<z> = CyclotomicField(5)
sage: F.<z> = CyclotomicField(5)
sage: t = 3*z^3 + 4*z^2 + 2
sage: t.norm()
251
sage: t.norm(F)
2
sage: t.matrix(F)
[2]
```



---

Comment by craigcitro created at 2008-04-02 07:22:21

`ncalexan` and `wstein` looked at this for a few minutes, and discovered that the root cause was that my "fix" for #1083 really only worked in the case that the absolute extension was of degree 2. (Sloppy testing on my part.) So, I'm fixing this.

The bug is really in `sage/rings/number_field/maps.py`, around line 122. We are given an absolute polynomial, and we want to convert it into a relative polynomial. However, in this case, we want to return a polynomial of degree 0 in the generator for L/K. So if our original element is represented by the absolute polynomial a<sub>n</sub>x<sup>n</sup> + ... + a<sub>1</sub>x + a<sub>0</sub> , and our extension is defined by `x-m`, for `m` an element of K (note that one cannot currently define a relative extension by a non-monic polynomial), then we want to return a<sub>n</sub>m<sup>n</sup> + ... + a<sub>1</sub>m + a<sub>0</sub>. Now `m` is just `-1*L.pari_rnf()[0][0]`, so we just evaluate our polynomial there. This will always give us a constant polynomial that's exactly what we want.

If there's some case that I'm not thinking of here, let me know. I've tested it on various degrees, and with relative polynomials other than just `x-a`, and it works in every case I could come up with.


---

Comment by craigcitro created at 2008-04-02 07:22:21

Changing assignee from was to craigcitro.


---

Comment by craigcitro created at 2008-04-02 07:22:21

Changing status from new to assigned.


---

Attachment


---

Comment by ncalexan created at 2008-04-03 04:14:09

Does this handle fields with unusual defining polynomials, such as F = L.extension(2*x - L.gen())?  I don't think it will.

Nick


---

Comment by ncalexan created at 2008-04-03 04:20:59

After discussion on IRC, reviewed positive:


```
craigcitro: hey ncalexan -- did you see i posted a patch for the thing you were looking at last night?
[9:11pm] ncalexan: craigcitro: yes, I just commented on it.  I don't think it will handle polys like 2*x - a, will you check?
[9:12pm] craigcitro: you're right -- but you can't create an extension with such a poly
[9:12pm] craigcitro: (i checked it when i was looking at it)
[9:12pm] ncalexan: Someday I hope to address that, but okay.
[9:12pm] craigcitro: nod
[9:12pm] ncalexan: Comment on the patch, then I'll review positive.
[9:13pm] ncalexan: Actually, wait -- what about x - 2*a?
[9:13pm] craigcitro: that works fine
[9:13pm] craigcitro: i checked those
[9:13pm] ncalexan: You're assuming that x = rel gen when you look at f(rel gen), right?
[9:13pm] craigcitro: then i tried 2*x - a
[9:13pm] craigcitro: and discovered it didn't work
[9:14pm] craigcitro: if the rel poly is x-foo
[9:14pm] ncalexan: Well, there's a test with x - a/2.
[9:14pm] craigcitro: i just plug foo in.
[9:14pm] ncalexan: Okay.  I'll review positive.
```



---

Comment by mabshoff created at 2008-04-03 08:51:40

Doctests pass for me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-03 08:51:56

Merged in Sage 3.0.alpha1


---

Comment by mabshoff created at 2008-04-03 08:51:56

Resolution: fixed
