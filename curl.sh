#!/bin/sh

curl http://$OLLAMA_HOST/api/generate -d '{
  "model": "llama3.1",
  "prompt": "Why is the sky blue?"
}'