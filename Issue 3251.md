# Issue 3251: plot level is really weird -- points, etc., are difficult to control whether they are above or below other plot elements

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-18 03:29:42

Assignee: was

CC:  jason kcrisman


```
On Sat, May 10, 2008 at 9:35 AM, Hector Villafuerte <hectorvd`@`gmail.com> wrote:
>
> On Sat, May 10, 2008 at 9:14 AM, louie <loufervillegas`@`hotmail.com> wrote:
>>
>> I made a custom polar grid based on circles and lines and then plotted
>> some points but the points appeared behind the grid. I tried the
>> documentation on these primitives and also show() but nothing on the
>> subject.
>
>
> I was sure that it depended on the order of the plots when adding
> them... but it doesn't work for me here, since p1+p0 gives the same
> result as p0+p1:
>
> sage: p0 = polar_plot(lambda t: 1, 0, 2*pi, thickness=5)
> sage: p1 = sum([point( [cos(k), sin(k)], pointsize=70, rgbcolor='red')
> for k in srange(0,2*pi,pi/4)])
> sage: (p1+p0).show(aspect_ratio=1)
> sage: (p0+p1).show(aspect_ratio=1)
>
> Some of the more knowledgeable users might want to comment on this.
> Best,
> --
>  Hector

I don't know of any way to fix this at present.   It was in Alex Clemesha's
original implementation of plotting, and he never fixed it.  Somebody will
likely have to spend some time understanding why Sage's "plotting using
matplotlib" organizers overlaps in such a weird way and fix it.  If anybody
already has, please speak up.

```



---

Comment by AlexGhitza created at 2009-01-22 18:28:48

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2011-06-02 03:36:48

#6249 is related, though apparently slightly different.
