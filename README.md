# ome2024-ngff-challenge

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]

<!-- SPHINX-START -->

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/ome/ome2024-ngff-challenge/workflows/CI/badge.svg
[actions-link]:             https://github.com/ome/ome2024-ngff-challenge/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/ome2024-ngff-challenge
[conda-link]:               https://github.com/conda-forge/ome2024-ngff-challenge-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/ome/ome2024-ngff-challenge/discussions
[pypi-link]:                https://pypi.org/project/ome2024-ngff-challenge/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/ome2024-ngff-challenge
[pypi-version]:             https://img.shields.io/pypi/v/ome2024-ngff-challenge
[rtd-badge]:                https://readthedocs.org/projects/ome2024-ngff-challenge/badge/?version=latest
[rtd-link]:                 https://ome2024-ngff-challenge.readthedocs.io/en/latest/?badge=latest

<!-- prettier-ignore-end -->

Project planning and material repository for the 2024 challenge to generate 1 PB of OME-Zarr data

## Challenge overview

The high-level goal of the challenge is to generate OME-Zarr data according to a development
version of the specification to drive forward the implementation work and establish a baseline
for the conversion costs that members of the community can expect to incur.

Data generated within the challenge will have:

* all v2 arrays converted to v3, optionally sharding the data
* all .zattrs metadata migrated to `zarr.json["attributes"]["ome"]`
* a top-level `ro-crate-metadata.json` file with minimal metadata (specimen and imaging modality)

## Converting your data

### Getting started

The `dev2/resave.py` script can be used to convert an OME-Zarr 0.4 dataset
that is based on Zarr v2:

```
dev2/resave.py input.zarr output.zarr
```

If you would like to re-run the script with different parameters, you can additionally
set `--output-overwrite` to ignore a previous conversion:

```
dev2/resave.py input.zarr output.zarr --output-overwrite
```

### Writing metadata

The RO-Crate metadata writing code is not currently enabled by default. To generate the
metadata, use:

```
PYTHONPATH=dev3/zarr-crate dev2/resave.py input.zarr ouput.zarr --output-rocrate
```

### Reading/writing remotely

If you would like to avoid downloading and/or upload the Zarr datasets, you can set S3
parameters on the command-line which will then treat the input and/or output datasets
as a prefix within an S3 bucket:

```
dev2/resave.py \
        --input-bucket=BUCKET \
        --input-endpoint=HOST \
        --input-anon \
        input.zarr \
        output.zarr
```

A small example you can try yourself:

```
dev2/resave.py \
        --input-bucket=idr \
        --input-endpoint=https://uk1s3.embassy.ebi.ac.uk \
        --input-anon \
        zarr/v0.4/idr0062A/6001240.zarr \
        /tmp/6001240.zarr
```

### Reading/writing via a script

Another R/W option is to have `resave.py` generate a script which you can execute later.
If you pass `--output-script`, then rather than generate the arrays immediately, a file
named `convert.sh` will be created which can be executed later.

For example, running:

```
dev2/resave.py dev2/input.zarr /tmp/scripts.zarr --output-script
```

produces a dataset with one `zarr.json` file and 3 `convert.sh` scripts:

```
/tmp/scripts.zarr/0/convert.sh
/tmp/scripts.zarr/1/convert.sh
/tmp/scripts.zarr/2/convert.sh
```

Each of the scripts contains a statement of the form:

```
zarrs_reencode --chunk-shape 1,1,275,271 --shard-shape 2,236,275,271 --dimension-names c,z,y,x --validate dev2/input.zarr /tmp/scripts.zarr
```

Running this script will require having installed `zarrs_tools` with:

```
cargo install zarrs_tools
export PATH=$PATH:$HOME/.cargo/bin
```

### Optimizing chunks and shards

Finally, there is not yet a single heuristic for determining the chunk and shard sizes
that will work for all data. Instead, you can use a JSON file to review and manually
optimize the chunking and sharding parameters:

```
dev2/resave.py input.zarr parameters.json --output-write-details
```

This will write a JSON file of the form:

```
[{"shape": [...], "chunks": [...], "shards": [...]}, ...
```

Edits to this file can be read back in using the `output-read-details` flag:

```
dev2/resave.py input.zarr output.zarr --output-read-details=parameters.json
```

Note: Changes to the shape are ignored.


## Related work

The following additional PRs are required to work with the data
created by the scripts in this repository:

 * https://github.com/ome/ome-ngff-validator/pull/36
 * https://github.com/ome/ome-zarr-py/pull/383
 * https://github.com/hms-dbmi/vizarr/pull/172
 * https://github.com/LDeakin/zarrs_tools/issues/8

 Slightly less related but important at the moment:

 * https://github.com/google/neuroglancer/issues/606
 * https://github.com/ome/napari-ome-zarr/pull/112
 * https://github.com/zarr-developers/zarr-python/issues/2029
