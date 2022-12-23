# Issue 9729: Moving the discrete fourier interact from wiki into the library.

archive/issues_009729.json:
```json
{
    "body": "Assignee: itolkov, jason\n\nCC:  mhampton\n\nMoving the discrete Fourier interact from the wiki into the library. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9729\n\n",
    "created_at": "2010-08-11T21:38:23Z",
    "labels": [
        "interact",
        "minor",
        "enhancement"
    ],
    "title": "Moving the discrete fourier interact from wiki into the library.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9729",
    "user": "punchagan"
}
```
Assignee: itolkov, jason

CC:  mhampton

Moving the discrete Fourier interact from the wiki into the library. 

Issue created by migration from https://trac.sagemath.org/ticket/9729





---

archive/issue_comments_095091.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-12T04:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9729#issuecomment-95091",
    "user": "punchagan"
}
```

Attachment



---

archive/issue_comments_095092.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-12T04:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9729#issuecomment-95092",
    "user": "punchagan"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095093.json:
```json
{
    "body": "This apparently depends on #9728.",
    "created_at": "2010-09-21T20:05:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9729#issuecomment-95093",
    "user": "kcrisman"
}
```

This apparently depends on #9728.



---

archive/issue_comments_095094.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-11-18T11:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9729#issuecomment-95094",
    "user": "pang"
}
```

Attachment



---

archive/issue_comments_095095.json:
```json
{
    "body": "Attachment\n\nThe data from the FFT seems very difficult to read, in my opinion. From the documentation of Fourier.fft:\n\n```\n    The packing of the result is \"standard\": If A = fft(a, n), then A[0]\n    contains the zero-frequency term, A[1:n/2+1] contains the\n    positive-frequency terms, and A[n/2+1:] contains the negative-frequency\n    terms, in order of decreasingly negative frequency. So for an 8-point\n    transform, the frequencies of the result are [ 0, 1, 2, 3, 4, -3, -2, -1]\n```\n\n\nThis suggests that the second half of the array should go before the first half. Also, for many common examples all but a few Fourier coefficients are zero, and it could help visualize them if we plot only the non-zero ones. \n\nThe labels on the x axis do not correspond to the coefficients, but this can be fixed.\n\nAlso, I think a bar plot is more adequate than a line plot. You can compare the result of the original code and the proposed changes in the attached png files.\n\nLast but not least, abs(myfft[j])==abs(my_fft[-j]) for all real functions, so if only real functions are going to be used, we should only plot one half: what was the intention? \n\nI suggest something along the lines of:\n\n\n```\ndef plot_bars(ls, lenght = 1):\n    return (sum(polygon2d([(x-lenght/2,0),(x+lenght/2,0),\n                           (x+lenght/2,y),(x-lenght/2,y)])\n               for x,y in ls) +\n           sum(line2d([(x-lenght/2,0),(x+lenght/2,0),\n                       (x+lenght/2,y),(x-lenght/2,y),(x-lenght/2,0)], \n                      rgbcolor=(0,0,0))\n               for x,y in ls))\n\nimport scipy.fftpack as Fourier\nvar('x')\n@interact\ndef discrete_fourier(f = input_box(default=sum([sin(k*x) for k in range(1,5,2)])), \n                     treshold = slider(0,0.1,0.01,0.01)):\n    pbegin = -float(pi)\n    pend = float(pi)\n    html(\"<h3>Function plot and its discrete Fourier transform</h3>\")\n    show(plot(f, pbegin, pend, plot_points = 512), figsize = [4,3])\n    f_vals = [f(ind) for ind in srange(pbegin, pend,(pend-pbegin)/512.0)]\n    my_fft = Fourier.fft(f_vals)\n    ls = ([(j, abs(my_fft[j])) for j in range(-floor(L/2)+1,floor(L/2)+1)])\n    M = max(v for j,v in ls)\n    max_index = max(j for j in range(L) if ls[j][1] > treshold*M)\n    min_index = min(j for j in range(L) if ls[j][1] > treshold*M)\n    show(plot_bars(ls[max(min_index-5,0):min(max_index+5,L)]), figsize = [4,3])\n\n```\n\n\nNote: \"scale\" no longer works, but if you like the suggestions, it shouldn't be hard to recover.",
    "created_at": "2010-11-18T11:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9729#issuecomment-95095",
    "user": "pang"
}
```

Attachment

The data from the FFT seems very difficult to read, in my opinion. From the documentation of Fourier.fft:

```
    The packing of the result is "standard": If A = fft(a, n), then A[0]
    contains the zero-frequency term, A[1:n/2+1] contains the
    positive-frequency terms, and A[n/2+1:] contains the negative-frequency
    terms, in order of decreasingly negative frequency. So for an 8-point
    transform, the frequencies of the result are [ 0, 1, 2, 3, 4, -3, -2, -1]
```


This suggests that the second half of the array should go before the first half. Also, for many common examples all but a few Fourier coefficients are zero, and it could help visualize them if we plot only the non-zero ones. 

The labels on the x axis do not correspond to the coefficients, but this can be fixed.

Also, I think a bar plot is more adequate than a line plot. You can compare the result of the original code and the proposed changes in the attached png files.

Last but not least, abs(myfft[j])==abs(my_fft[-j]) for all real functions, so if only real functions are going to be used, we should only plot one half: what was the intention? 

I suggest something along the lines of:


```
def plot_bars(ls, lenght = 1):
    return (sum(polygon2d([(x-lenght/2,0),(x+lenght/2,0),
                           (x+lenght/2,y),(x-lenght/2,y)])
               for x,y in ls) +
           sum(line2d([(x-lenght/2,0),(x+lenght/2,0),
                       (x+lenght/2,y),(x-lenght/2,y),(x-lenght/2,0)], 
                      rgbcolor=(0,0,0))
               for x,y in ls))

import scipy.fftpack as Fourier
var('x')
@interact
def discrete_fourier(f = input_box(default=sum([sin(k*x) for k in range(1,5,2)])), 
                     treshold = slider(0,0.1,0.01,0.01)):
    pbegin = -float(pi)
    pend = float(pi)
    html("<h3>Function plot and its discrete Fourier transform</h3>")
    show(plot(f, pbegin, pend, plot_points = 512), figsize = [4,3])
    f_vals = [f(ind) for ind in srange(pbegin, pend,(pend-pbegin)/512.0)]
    my_fft = Fourier.fft(f_vals)
    ls = ([(j, abs(my_fft[j])) for j in range(-floor(L/2)+1,floor(L/2)+1)])
    M = max(v for j,v in ls)
    max_index = max(j for j in range(L) if ls[j][1] > treshold*M)
    min_index = min(j for j in range(L) if ls[j][1] > treshold*M)
    show(plot_bars(ls[max(min_index-5,0):min(max_index+5,L)]), figsize = [4,3])

```


Note: "scale" no longer works, but if you like the suggestions, it shouldn't be hard to recover.



---

archive/issue_comments_095096.json:
```json
{
    "body": "Replying to [comment:3 pang]:\nSorry, forgot to copyandpaste some details\n\n```\ndef plot_bars(ls, lenght = 1):\n    return (sum(polygon2d([(x-lenght/2,0),(x+lenght/2,0),\n                           (x+lenght/2,y),(x-lenght/2,y)])\n               for x,y in ls) +\n           sum(line2d([(x-lenght/2,0),(x+lenght/2,0),\n                       (x+lenght/2,y),(x-lenght/2,y),(x-lenght/2,0)], \n                      rgbcolor=(0,0,0))\n               for x,y in ls))\n\nimport scipy.fftpack as Fourier\nvar('x')\n@interact\ndef discrete_fourier(f = input_box(default=sum([sin(k*x) for k in range(1,5,2)])), \n                     treshold = slider(0,0.1,0.01,0.01)):\n    pbegin = -float(pi)\n    pend = float(pi)\n    html(\"<h3>Function plot and its discrete Fourier transform</h3>\")\n    show(plot(f, pbegin, pend, plot_points = 512), figsize = [4,3])\n    f_vals = [f(x=ind) for ind in srange(pbegin, pend,(pend-pbegin)/512.0)]\n    my_fft = Fourier.fft(f_vals)\n    L = len(my_fft)\n    ls = ([(j, abs(my_fft[j])) for j in range(-floor(L/2)+1,floor(L/2)+1)])\n    M = max(v for j,v in ls)\n    max_index = max(j for j in range(L) if ls[j][1] > treshold*M)\n    min_index = min(j for j in range(L) if ls[j][1] > treshold*M)\n    show(plot_bars(ls[max(min_index-5,0):min(max_index+5,L)]), figsize = [4,3])\n    \n\n\n```\n",
    "created_at": "2010-11-18T11:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9729#issuecomment-95096",
    "user": "pang"
}
```

Replying to [comment:3 pang]:
Sorry, forgot to copyandpaste some details

```
def plot_bars(ls, lenght = 1):
    return (sum(polygon2d([(x-lenght/2,0),(x+lenght/2,0),
                           (x+lenght/2,y),(x-lenght/2,y)])
               for x,y in ls) +
           sum(line2d([(x-lenght/2,0),(x+lenght/2,0),
                       (x+lenght/2,y),(x-lenght/2,y),(x-lenght/2,0)], 
                      rgbcolor=(0,0,0))
               for x,y in ls))

import scipy.fftpack as Fourier
var('x')
@interact
def discrete_fourier(f = input_box(default=sum([sin(k*x) for k in range(1,5,2)])), 
                     treshold = slider(0,0.1,0.01,0.01)):
    pbegin = -float(pi)
    pend = float(pi)
    html("<h3>Function plot and its discrete Fourier transform</h3>")
    show(plot(f, pbegin, pend, plot_points = 512), figsize = [4,3])
    f_vals = [f(x=ind) for ind in srange(pbegin, pend,(pend-pbegin)/512.0)]
    my_fft = Fourier.fft(f_vals)
    L = len(my_fft)
    ls = ([(j, abs(my_fft[j])) for j in range(-floor(L/2)+1,floor(L/2)+1)])
    M = max(v for j,v in ls)
    max_index = max(j for j in range(L) if ls[j][1] > treshold*M)
    min_index = min(j for j in range(L) if ls[j][1] > treshold*M)
    show(plot_bars(ls[max(min_index-5,0):min(max_index+5,L)]), figsize = [4,3])
    


```




---

archive/issue_comments_095097.json:
```json
{
    "body": "Based on pang's comments, looks like maybe this is 'needs work'.",
    "created_at": "2011-06-13T18:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9729#issuecomment-95097",
    "user": "kcrisman"
}
```

Based on pang's comments, looks like maybe this is 'needs work'.



---

archive/issue_comments_095098.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-13T18:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9729#issuecomment-95098",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.
