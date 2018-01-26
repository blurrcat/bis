
## Development

### Testing

By default, tests are run without migrations for reasons:
* sometimes we want to test before generating migration files
* speedup tests

You can enable migrations in tests by adding the `--migrations` flag:

    pytest --migrations

When `make test`, the test database is recreated with migrations on.
