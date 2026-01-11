# Text_Summarizer# TextSummarizer USing Huggingface

### Workflows 

1. Config.yaml
2. Params.yaml
3. Config entity
4. Configuration Manager
5. Update the components- Data Ingestion,Data Transformation, Model Trainer
6. Create our Pipeline-- Training Pipeline,PRediction Pipeline
7. Front end-- Api's, Training APi's, Batch Prtediction API's


Hardware Requirements & Model Loading

This project uses the Pegasus transformer model for text summarization. The full Pegasus model is very large (~2.3 GB) and may require substantial RAM to load and run. On CPU-only machines with limited memory, loading the model may fail with errors like:

DefaultCPUAllocator: not enough memory


Recommendations for running successfully:

Use a smaller transformer model for testing (e.g., t5-small or distilbart-cnn-12-6).

Reduce the training batch size (per_device_train_batch_size = 1).

Use a GPU if available.

For memory-efficient loading, you can use load_in_8bit=True or device_map="auto" when calling from_pretrained.

These adjustments allow the pipeline to run end-to-end on most machines without running out of memory.