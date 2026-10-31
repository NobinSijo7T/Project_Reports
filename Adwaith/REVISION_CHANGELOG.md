# Revision change log — 27 October 2026

Applied to `main.tex` and the Adwaith report wrapper `main_adwaith.tex`.

- Re-examined the supplied implementation, including `codebase/lung-detection/src/dataset.py`, `configs/default.json`, `train.py`, `evaluate.py`, checkpoints, and evaluation outputs.
- Corrected the dataset note to state precisely that the supplied implementation is a lung-detection image classifier, not a GESL power-grid pipeline.
- Retained GESL, `T=128`, `D=24`, 15,000 windows, and stride 10 only as report claims; marked provider, features, preprocessing, window derivation, split, and leakage status as requiring verification.
- Added a dataset configuration summary table distinguishing the unverified GESL claims from the observed X-ray implementation.
- Updated the experimental-results sections to distinguish unrelated X-ray outputs from the absent GESL/TFT/VAE evidence.
- Retained the reported metric values without presenting them as independently verified.

## Verification table

| Item | Evidence inspected | Verification status | Correction made | Outstanding requirements |
|---|---|---|---|---|
| GESL source and configuration | Repository tree; report source; no GESL files found | Requires verification | Marked provider, source, features, preprocessing, windows, split, and leakage as unresolved | Supply authoritative GESL source, data, loader, and preprocessing artifacts |
| Supplied implementation identity | `src/dataset.py`, `configs/default.json`, `train.py`, `evaluate.py` | Verified as unrelated lung-detection classifier | Replaced broad/ambiguous wording with factual implementation description | None for this finding |
| TFT Silhouette 0.684; reconstruction MSE 0.0142 | Report table only; no GESL embeddings or logs | Unverified | Values retained as reported, not independently verified | GESL model outputs, labels, split, and reproducible metric script |
| UMAP trustworthiness 0.965 | Report table only; no projection artifacts or timing logs | Unverified | Value retained as reported | Latent vectors, UMAP parameters, seed, and evaluation output |
| DBSCAN Silhouette 0.718; six clusters; 3.2% noise | Report table/figure only; no DBSCAN labels | Unverified | Values retained as reported | 2D embeddings, labels, distance metric, cluster/noise counts, and calculation |
| Report formatting and consistency | LaTeX source, two-pass compilation, PDF text extraction, and compiler log | Completed | Regenerated 63-page PDF; no fatal errors or overfull-box warnings remain | Visual review of the institution's final submission copy |
