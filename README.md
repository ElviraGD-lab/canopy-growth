# canopy-growth

**Canopy Growth from Repeated Airborne LiDAR** — how fast the forest grows, measured from the
free national LiDAR surveys of Spain (PNOA), with an honest statement of where the old surveys
do not allow it.

> **Status: early development.** The repository is set up (step 3.0 of the plan). Nothing is
> computed yet; the first release with a DOI follows when the base passes its tests.

Part of the **Pajares** project — three open tools for forests and power lines in Spain:
`canopy-growth`, `storm-forest-damage`, `powerline-treefall-risk`.

## What it gives

- A map of **canopy height growth in m/yr with an interval** (20–30 m cells); separately —
  regrowth in line corridors, corridor edges and undisturbed forest.
- A **passport of every survey strip**: usable, corrected or excluded — and why.
- A **report on where the numbers can be trusted**.
- For non-programmers — a **QGIS plugin**: draw an area, press "Calculate"; the plugin downloads
  the PNOA tiles itself. For technical users — a Python package and command line.

## What it does not promise

- The growth of an individual tree.
- A replacement for companies' own corridor flights (15–25 points/m²).
- The cause of growth.
- A forecast beyond continuing the measured rate.

## Where it is tested

| Site | Why |
|---|---|
| Puerto de Pajares (pilot), ETRS89 / UTM 30N (EPSG:25830), X 270 000–278 000, Y 4 759 000–4 767 000 | Atlantic mountain forest, two survey series on both sides of the pass |
| Galicia | eucalyptus, leaf-off survey — blind transfer |
| A Mediterranean site | other climate — blind transfer |

## How the results are checked

Every step writes a number that can fail, and the pass/fail thresholds are committed in
`config/acceptance.yaml` **before** any result is computed. Checks include a known-answer test,
a noise estimate from two surveys close in time, stable surfaces (roads, roofs, rock), and the
National Forest Inventory tables.

## Install (development)

```bash
conda env create -f environment.yml
conda activate canopy-growth
pip install -e . --no-deps
pytest
```

## Data

No LiDAR data is stored in this repository; the code downloads PNOA tiles itself.
PNOA data: "PNOA cedido por © Instituto Geográfico Nacional" (CC BY 4.0, scne.es).

## Licence

- Code — [Apache-2.0](LICENSE).
- Documentation and derived data — [CC BY 4.0](LICENSE-docs).
- The QGIS plugin (when added) — GPL v2 or later, as QGIS requires.

## Citation

See [`CITATION.cff`](CITATION.cff) or the "Cite this repository" button on GitHub. Each release
will have its own DOI on Zenodo.

## Support and contributing

Questions, bugs and ideas — [GitHub Issues](https://github.com/ElviraGD-lab/canopy-growth/issues).
See [CONTRIBUTING.md](CONTRIBUTING.md).

## Author

Elvira Gayanova — geodetic engineer, Asturias, Spain.
