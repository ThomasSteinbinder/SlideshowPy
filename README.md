# SlideshowPy
Python script to start a slideshow using OpenCV

### Usage in commandline

```
slideshow.py -d <directory> -w <width> -h <height> -t <time>

-d    The directory where the images will be taken from                                         default   ./
-w    The width, the images will be sized to (preferable the screen width)                      default   640
-h    The height, the images will be sized to (preferable the screen height)                    default   480
-t    The time in milliseconds, a single image will be shown before the next one fades in.      default   2000
      (Plus the time, it takes to load and resize the next image)
```
