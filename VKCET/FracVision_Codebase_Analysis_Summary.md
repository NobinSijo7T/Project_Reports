# FracVision codebase analysis summary

## Project identity

The inspected project is **FracVision**, version 0.1.0: a multimodal X-ray fracture-analysis research prototype.

## Directory structure

- `backend/`: FastAPI application, routes, Pydantic schemas, startup lifecycle, pipeline state, and SQLAlchemy models.
- `frontend/`: Next.js 16 application with analyze, compare, history, results, about, overlay, and result-panel components.
- `model/data/`: FracAtlas and GRAZPEDWRI-DX adapters, COCO/YOLO/VOC parsers, preprocessing, augmentation, splits, and serial pairing.
- `model/models/`: DINOv2 extractor/classifier, RT-DETRv2 detector, MedSAM segmentor, Mamba longitudinal model, and disabled recovery stub.
- `model/inference/`: single-image pipeline and serial X-ray comparator.
- `model/training/`: classifier, detector, MedSAM/Mamba-related training entry points.
- `model/evaluation/`: detection, segmentation, classification, and report evaluation utilities.
- `tests/`: unit and integration tests for preprocessing, adapters, models, and API behavior.
- `docker/` and frontend Dockerfile: CPU/GPU deployment definitions.

## Technology stack

Python 3.11+, PyTorch, torchvision, timm, transformers, OpenCV, Pillow, NumPy, pydicom, SimpleITK, MONAI, FastAPI, Pydantic, SQLAlchemy, SQLite/PostgreSQL-compatible `DATABASE_URL`, Next.js 16.3.3, React 19.2.8, TypeScript, Tailwind CSS 4, pytest, and Docker Compose.

## Implemented modules and workflows

1. Browser upload → FastAPI validation → temporary file → preprocessing/QC.
2. RT-DETRv2 detection → highest-confidence fracture box selection.
3. MedSAM box-prompted segmentation when a checkpoint is loaded.
4. DINOv2 CLS/patch extraction → multilabel classifier probabilities.
5. Typed `PredictionResponse` serialization → database history persistence → frontend overlay/result rendering.
6. Serial comparison using optional registration, DINOv2 cosine similarity, pixel metrics, and mask Dice/IoU.
7. Longitudinal feature sequence → Mamba-style healing-stage logits and sequence representation.

## Data and models

The code supports FracAtlas and GRAZPEDWRI-DX. The supplied workspace contains no actual dataset files or trained checkpoint weights; only `.gitkeep` files exist in the dataset/checkpoint directories. The recovery-time module is deliberately disabled because verified time-to-union and censoring labels are unavailable.

## API inventory

- `GET /api/health`
- `GET /api/models`
- `POST /api/predict`
- `GET /api/history`
- `POST /api/compare`
- FastAPI docs at `/api/docs`, `/api/redoc`, and `/api/openapi.json`

## Persistence

SQLAlchemy models define `patients`, `imaging_studies`, `predictions`, `healing_comparisons`, and `model_versions`. Uploaded image bytes are not persisted by the prediction route; prediction summaries and de-identified metadata are persisted under an `anonymous-upload` patient timeline.

## Safety and validation

The API enforces a 50 MB upload limit, accepts JPEG/PNG/DICOM suffixes for prediction, checks pipeline readiness, uses Pydantic confidence constraints, records stage errors, and attaches a mandatory non-clinical disclaimer. CORS is configuration-driven. Authentication and authorization are not implemented in the inspected code.

## Incomplete or unavailable features

- Local dataset artifacts: unavailable.
- Trained checkpoints: unavailable.
- Recovery-time supervised training: disabled/stub only.
- Numeric benchmark/evaluation report: unavailable.
- Clinical validation: unavailable and explicitly disclaimed.
- Frontend dependency installation: unavailable in the current workspace (`next` command not found).
