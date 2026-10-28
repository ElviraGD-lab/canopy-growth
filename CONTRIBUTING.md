# Contributing

Thank you for your interest in `canopy-growth`.

- **Questions, bugs, ideas:** open an issue on GitHub. For a bug, please give the PNOA tile
  names, the command you ran and the full error message.
- **Code changes:** open an issue first, so we can agree on the approach; then a pull request
  from a branch. Every pull request must keep the tests passing (`pytest`).
- **Thresholds:** values in `config/acceptance.yaml` are not changed after a result has been
  seen; a change needs a reason recorded in the repository.
- **Data:** never commit LiDAR files, rasters or keys; the code downloads PNOA tiles itself.

## Development setup

```bash
conda env create -f environment.yml
conda activate canopy-growth
pip install -e . --no-deps
pytest
```
