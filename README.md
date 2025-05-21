# 🚀 OpenEdge-LLM
### LLMs Anywhere—From Data Center to ESP32

OpenEdge-LLM bundles everything you need to build a modern, multimodal assistant. Train models, compile them for any device, and serve them with a sleek Next.js front-end—all from one repo.

#### Why You'll Love It
- **Edge-to-Cloud** deployment from GPUs to sub‑1W microcontrollers
- **Multimodal** ingestion of text, images and sensor data
- **One-Click Demo** to show off your smart home or factory assistant

## Project Layers and Technologies

| Layer                     | Technologies                                                                 | What it Builds                                                                      |
| ------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Data Ingestion & ETL**  | Apache Beam (Spark for back-fills, Dask for interactive notebooks)           | Ingest JSON from MQTT/REST/camera; land as Parquet in MinIO object store.           |
| **Dataset & Feature Store** | DataHub/LakeFS, Qdrant/Faiss                                                 | Versioned corpora; vector store updated by Beam.                                    |
| **Intent + RAG Backend**  | PyTorch (BERT intent head), HuggingFace Transformers, custom RAG retriever   | Route "turn on lights" vs free-form Q-A; pull context docs.                         |
| **Model Training**        | PyTorch + DeepSpeed-ZeRO-3/4, JAX pjit, TensorFlow/Keras                     | Finetune open models (e.g., Llama-3-8B) with LoRA; light models for edge.           |
| **Compilation**           | TVM, TensorRT-LLM, TFLite Micro & CMSIS-NN                                   | Single `export.py` for Jetson, GPU server, ESP32/Cortex-M.                          |
| **Serving**               | NVIDIA Triton Server, vLLM, µTVM on ESP32                                    | Triton ensemble (RAG ➜ LLM ➜ post-processor); vLLM for CPU; µTVM on device.       |
| **Front-end & APIs**      | FastAPI + Next.js (Vercel)                                                   | Ask “Did I leave the stove on?” → assistant fuses camera frame + sensor logs.       |
| **DevOps**                | Docker-Compose, Helm, GitHub Actions, Prometheus/Grafana                     | CI builds Triton image, runs TVM tuning jobs on push to main.                       |

## Why it Rocks

*   **Versatility**: Demonstrates cloud-class LLM capabilities alongside inference on < 1 W microcontrollers from a single repository.
*   **Interoperability**: Showcases practical application and interchange between Beam, Spark, and Dask, plus a wide array of model compilers.
*   **Demo-Friendly**: Enables tangible demonstrations, such as interacting with a smart home setup locally, even without internet connectivity.

## Quick Demo

1. Spin up the stack:
   ```sh
   docker-compose -f devops/docker-compose.yml up --build
   ```
2. Start the APIs:
   ```sh
   uvicorn frontend/backend/main:app --reload
   ```
3. Open [http://localhost:3000](http://localhost:3000) and start chatting.

**Example Conversation**
```
You: "Did I leave the lights on?"
Assistant: "Nope. Last sensor reading shows all lights off."
```

## Key Resources Utilized

*   TensorRT-LLM: Open-sourced kernels & paged KV cache.
*   vLLM: High-throughput text generation server.
*   NVIDIA Triton Inference Server: Monthly releases with ensemble graphs & GPU/CPU back-ends.

## Project Structure

```
- data_ingestion/
- feature_store/
- intent_rag_backend/
- model_training/
- compilation/
- serving/
- frontend/
    - backend/
    - web/
- devops/
```

## Getting Started

OpenEdge-LLM is designed for rapid prototyping and real-world deployment. Here’s how to get up and running:

### 1. Clone the Repository
```sh
git clone https://github.com/your-org/open-edge-llm.git
cd open-edge-llm
```

### 2. Configure Environment
Copy the provided `.env.example` to `.env` and fill in your secrets as needed:
```sh
cp devops/.env.example devops/.env
```

### 3. Launch Core Services (Dev)
Spin up the backend, frontend, and supporting services with Docker Compose:
```sh
docker-compose -f devops/docker-compose.yml up --build
```

### 4. Data Ingestion
- Run the MQTT listener to receive live sensor data:
  ```sh
  python data_ingestion/mqtt_listener.py
  ```
- Upload a file to MinIO object storage:
  ```sh
  python data_ingestion/minio_upload.py
  ```
- Process Parquet data interactively with Dask:
  ```sh
  python data_ingestion/dask_notebook.py
  ```
- Run Apache Beam pipeline for ETL:
  ```sh
  python data_ingestion/beam_pipeline.py
  ```

### 5. Feature Store
- Initialize LakeFS repository and branch for versioned corpora:
  ```sh
  python feature_store/lakefs_setup.py
  ```
- Build and search a FAISS vector index:
  ```sh
  python feature_store/faiss_index.py
  ```
- Use Qdrant vector store for fast similarity search:
  ```sh
  python feature_store/vector_store.py
  ```

### 6. Intent + RAG Backend
- Run robust intent classification and routing:
  ```sh
  python intent_rag_backend/intent_router.py
  ```
- Run RAG question-answering:
  ```sh
  python intent_rag_backend/rag_qa.py
  ```
- Run summarization:
  ```sh
  python intent_rag_backend/summarizer.py
  ```

### 7. Model Training
- Finetune LLMs with LoRA or DeepSpeed:
  ```sh
  python model_training/finetune.py
  python model_training/lora_finetune.py
  ```
- Run text generation and translation:
  ```sh
  python model_training/text_generation.py
  python model_training/translation.py
  ```

### 8. Compilation for All Targets
- TVM autotune for Jetson:
  ```sh
  python compilation/tvm_autotune.py
  ```
- Export to TFLite Micro for ESP32:
  ```sh
  python compilation/tflite_micro_export.py
  ```
- Export to CMSIS-NN for Cortex-M:
  ```sh
  python compilation/cmsis_nn_export.py
  ```
- Export all artifacts:
  ```sh
  python compilation/export.py
  ```

### 9. Serving
- Run batch and streaming LLM serving:
  ```sh
  python serving/batch_llm.py
  python serving/streaming_llm.py
  ```
- Run post-processing and Triton ensemble simulation:
  ```sh
  python serving/post_processor.py
  python serving/triton_ensemble.py
  ```

### 10. Frontend & APIs
- Start FastAPI backend (health, file/image upload, RAG API):
  ```sh
  uvicorn frontend/backend/main:app --reload
  uvicorn frontend/backend/file_api:app --reload
  uvicorn frontend/backend/image_api:app --reload
  uvicorn frontend/backend/rag_api:app --reload
  ```
- Visit [http://localhost:3000](http://localhost:3000) for the Next.js UI.

### 11. DevOps, CI/CD & Monitoring
- GitHub Actions: Automated tests and builds on push to main.
- Helm: Deploy to Kubernetes with `devops/Chart.yaml`.
- Prometheus/Grafana: Monitoring with `devops/prometheus.yml`.

---

## Why OpenEdge-LLM is a Game Changer

- **Edge-to-Cloud**: Run LLMs on both GPU servers and microcontrollers (<1W) from the same repo.
- **Multimodal**: Ingest and reason over text, images, and sensor data.
- **Plug-and-Play**: Modular, extensible, and ready for real-world smart home, industrial, or research use.
- **Interoperable**: Mix Apache Beam, Spark, Dask, and every major model compiler in one workflow.
- **Demo-Ready**: Show off local, offline AI—ask your house questions, get answers, even with no internet.
