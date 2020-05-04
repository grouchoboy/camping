## Quickstart

To get started with Camping you need to have installed `Docker` and `docker
compose`.

1. Build the Docker images, and run the database migrations.

```bash
make build
make init
```

2. Run the development server for Camping.

```bash
make run
```

Your development instance of Camping will be running on
[localhost:8000](http://localhost:8000). `make run` runs the development server of
Django, alternative you can enter to the container shell and run the
server yourself.

```bash
make runshell
bin/run-dev.sh
```

If you want to change the assets, js and css files, you have to compile
them with the `watch` option.

```bash
make frontend-watch
```

## Documentation

The project uses [mkdocs](https://www.mkdocs.org/) for the
documentation. The source is under the `docs` folder. To build it run
`make docs-build`.
