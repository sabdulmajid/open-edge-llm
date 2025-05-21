# Serving

NVIDIA Triton Server hosts TensorRT engines; vLLM handles pure-CPU batched text; ESP32 flashes the µTVM binary. Triton ensemble graph: RAG retriever ➜ LLM ➜ post-processor.
