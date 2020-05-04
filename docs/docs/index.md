# Camping documentation

## What is Camping?

Camping is a clone of Basecamp. Is does not have any aspiration to be a
real product. I began to program Camping mainly for learn CSS. I borrow
some features of basecamp and try to implement its UI with plain CSS.

## Stack

Camping is build with Python and Django as a web framework. It is a
classic server side rendered web application, but it uses
[Turbolinks](https://github.com/turbolinks/turbolinks) to get some of
the goodies of an SPA with the programmer productibity of a SSR
application. For the styles Camping uses plain CSS.

As a package manager for python packages I'm using [poetry](https://python-poetry.org/)
to get reproducible installations.

## Application Organization

Django encourages
[applications](https://docs.djangoproject.com/en/3.0/ref/applications/)
as a way to organize your projects. But at the begining can be
challenging know where will be the boundings between the different
bussines contexts. I like to begin with a single `core` app and when
necessary extract the applications.

## Roadmap

The roadmap besides features could have things to try. The are not in
any specific order.

### Add support for users

Currently Camping does not have the idea of users. With users, each of
those will have its own home to create projects. At the moment I don't
have plans for collaboration between users, but maybe in the future I
will reconsider the idea.

### Add type hints anotations.

Add type hints annotations in the code and check for errors with
[mypy](http://mypy-lang.org/).

