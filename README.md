# Port Scanner
A demonstration of how you might build a Port Scanner for KS4 and KS5 pupils.

## Introduction
This code should be reasonably straightforward for pupils that have a basic understanding of Python and reinforces basic programming constructs such as selection and iteration.

## Demonstating in class
I have tested this on Python 3.1X with MacOS and Windows, but you do need access to the command line interface (CLI) so it may be a question of demonstrating it to pupils rather than them running it themselves.

The easiest way to open up a port like HTTP (80) is to run Python's simple web server by typing in the following:
```
python3 -m http.server 80
```

## Packages Used
We will be using:
* [socket](https://docs.python.org/3/library/socket.html) 

The socket library is a part of the standard library, you already have it, so no need to install it.