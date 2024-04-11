# Changelog

All notable changes to this project will be documented in this file.

## [1.2.0](https://github.com/bigdatabr/deirokay/compare/1.1.1...1.2.0) (2024-04-11)


### Features

* Add "tolerance_%" parameter in Contain statement ([#61](https://github.com/bigdatabr/deirokay/issues/61)) ([d557f4b](https://github.com/bigdatabr/deirokay/commit/d557f4bfdd84b2083f62fe0fc8c1cd6093b4a564))

### [1.1.1](https://github.com/bigdatabr/deirokay/compare/1.1.0...1.1.1) (2024-03-14)


### Bug Fixes

* **statement:** "Contain" report ([8fd0987](https://github.com/bigdatabr/deirokay/commit/8fd098788d8c8cd577ca8b94df10ea39f1e0e284))

## [1.1.0](https://github.com/bigdatabr/deirokay/compare/1.0.1...1.1.0) (2024-01-09)


### Features

* StatisticInInterval statement ([#32](https://github.com/bigdatabr/deirokay/issues/32)) ([86b018d](https://github.com/bigdatabr/deirokay/commit/86b018d482effb4aa5a068ecfffbbeddaad4feab))


### Bug Fixes

* Limit output size to stdout ([a41f31f](https://github.com/bigdatabr/deirokay/commit/a41f31fdc260988da3647e98f24dafb8cf34788a))

### [1.0.1](https://github.com/bigdatabr/deirokay/compare/1.0.0...1.0.1) (2022-10-21)


### Bug Fixes

* Add libpq-dev as required package ([0d508f8](https://github.com/bigdatabr/deirokay/commit/0d508f85d43f8fc247a89f120bdd87e812e4cfd2))

## [1.0.0](https://github.com/bigdatabr/deirokay/compare/0.8.0...1.0.0) (2022-07-21)


### ⚠ BREAKING CHANGES

* ColumnExpression report format
* Remove `verbose` from Contain statement in favor of
`report_limit`. Null values are now valid
* Create `attach_backend` and `get_backend`
* Create support for multibackend resources + refactor

### Features

* Create `attach_backend` and `get_backend` ([37d6e31](https://github.com/bigdatabr/deirokay/commit/37d6e3175a656b03c08b7e29a7ce8a41488dbdf2))
* Create support for multibackend resources + refactor ([8500721](https://github.com/bigdatabr/deirokay/commit/85007214979611672baba398cfc05146067b9dae))
* Dask backend for NotNull stmt ([b3fb691](https://github.com/bigdatabr/deirokay/commit/b3fb6915e2f60c790bdcfaed5fd8eedd92a9b63c))
* Dask backend for RowCount stmt ([a320201](https://github.com/bigdatabr/deirokay/commit/a320201ef4d396e86a22b0c76b6d73bf51bb0143))
* Dask backend for Unique stmt ([e3cdfd6](https://github.com/bigdatabr/deirokay/commit/e3cdfd6fe258fbb6f83a34178f58da5f8fb64f45))
* Implement Dask serialize in all treaters ([e824d78](https://github.com/bigdatabr/deirokay/commit/e824d78053071beadd7b0e8bc42b10ca7595e7e7))
* Improve ColumnExpression and implement Dask ([a02e247](https://github.com/bigdatabr/deirokay/commit/a02e2477aa6fc50b1fd2becb20598070b5a2732c))
* Improve Contain stmt and implement Dask ([effa169](https://github.com/bigdatabr/deirokay/commit/effa1691baed3d52c6f644e3046e6a3f6919c4aa))
* Standardize data readers ([a42e9d3](https://github.com/bigdatabr/deirokay/commit/a42e9d38754a0d9a53c02a2b91b181249912acb4))


### Bug Fixes

* Boolean treater ([22b39b5](https://github.com/bigdatabr/deirokay/commit/22b39b529768e305d180081c3efd7d08825ec562))
* DataTreater `treat` support Iterables + force ([ae84cad](https://github.com/bigdatabr/deirokay/commit/ae84cad56b1f093b0e98c5d56f332f64f8a5039d))
* fix tests for Dask ([40cd1af](https://github.com/bigdatabr/deirokay/commit/40cd1af8cc42f0d07cdc35293a3c805aaf34dbea))
* FutureWarning consistent across repo ([60d5722](https://github.com/bigdatabr/deirokay/commit/60d5722796b71c6ada14094c2322c4c5a92f2e87))
* Missing lazy module usage in typing ([0413433](https://github.com/bigdatabr/deirokay/commit/0413433fb109b69de93255ae39b0cbdc9e1ad78a))
* Remove BaseStatement from statements map ([d7e844c](https://github.com/bigdatabr/deirokay/commit/d7e844ccb4e24a9dc11889203a36b6085d27da02))
* Remove Python3.8-only features ([0bb8dca](https://github.com/bigdatabr/deirokay/commit/0bb8dca0000bc45cad7cc2ebe7b9397b42734e6d))
* Use lru_cache without limits instead of cache ([33f0a14](https://github.com/bigdatabr/deirokay/commit/33f0a1444245e3ab2ba6618db36371ce2e3a02f0))
* Validator behavior for Dask backend ([9379f63](https://github.com/bigdatabr/deirokay/commit/9379f63afccc481ab41e5ac8277cdcfa48580eab))

## [0.8.0](https://github.com/bigdatabr/deirokay/compare/0.7.2...0.8.0) (2022-06-28)


### Features

* Minor changes to exception message ([0e00b38](https://github.com/bigdatabr/deirokay/commit/0e00b3838170135692c359ef476bc0c5c9aad308))
* Rewords list-like alias requirement exception ([e526258](https://github.com/bigdatabr/deirokay/commit/e52625813ee2c57d9d2651521483d26d55c46a04))


### Bug Fixes

* Bug when reading S3 logs with same prefix ([969cc7d](https://github.com/bigdatabr/deirokay/commit/969cc7da11344a696405ec92f761f267d0e340a6)), closes [#37](https://github.com/bigdatabr/deirokay/issues/37)

### [0.7.2](https://github.com/bigdatabr/deirokay/compare/0.7.1...0.7.2) (2022-04-07)


### Bug Fixes

* Deal with pagination in S3 list_objects ([ed5e10e](https://github.com/bigdatabr/deirokay/commit/ed5e10e2a0e4e8ea3fc03ab8b5e2001c4bb222e6))

# Release 0.7.1

2022-02-22

- Fix bugs when profiling entirely null columns


# Release 0.7.0

2022-02-22

- New `ColumnExpression` (`column_expression`) statement to evaluate an expression involving the columns from a scope.
- `data_reader` can now get table from SQL query or file
  - Add `reader_kwargs` and `validator_kwargs` arguments in `DeirokayOperator` (to support feature above)
  - Deprecation warning for `path_to_file` argument in `DeirokayOperator` in favor of `data` (to make API consistent with feature above)


# Release 0.6.0

2021-12-15

- New `deirokay.DTypes.DECIMAL` for exact decimal value representation.
- New `distinct` boolean parameter for `row_count` statement, which
makes it possible to count only distinct values in a given scope.
- General improvements in templates generated by `profile` method of
builtin statements.
- Better logs (stdout) for `deirokay.validate` failed statements.
Now it also prints the scope the statements are applied to and the
provided severity threshold level.


# Release 0.5.2

2021-12-09

- Fix jinja templating for `DeirokayOperator`


# Release 0.5.1

2021-12-09

- Custom Jinja templates also in `DeirokayOperator`


# Release 0.5.0

2021-12-09

- Custom Jinja templates in `Derokay.validate`
- Improve exception error when there is a typo in column names


# Release 0.4.3

2021-12-08

- Fix for setup install


# Release 0.4.2

2021-12-08

- New `contain` statement (`deirokay.statements.Contain`)
- Serialization of DataFrame data into validation documents with `get_dtype_treater` and `get_treater_instance` (from `deirokay.parser`) and `serialize` methods (in Deirokay treaters)
