# Resource located at /api/books

## 1. Server-side rendering

    - C => POST /api/books/create/ (GET /api/books/create for HTML of the form)
    - R => GET /api/books/ or GET /api/books/2/
    - U => POST /api/books/2/ (GET /api/books/create for HTML of the form)
    - D => POST /api/books/2/ (GET /api/books/create for HTML of the form)

## 2. RESTful API:

    - C         => POST     /api/books/
    - R all     => GET      /api/books/
    - R details => GET      /api/books/2/
    - U         => PUT      /api/books/2/
    - D         => DELETE   /api/books/2/