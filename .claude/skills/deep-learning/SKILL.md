---
name: deep-learning
description: Deep learning and neural networks from first principles. Use for any ML, neural net, PyTorch, transformer, LLM internals, training loop, backprop, CNN, RNN or fine-tuning question or build, including audio and TTS model work.
---

# Deep learning and neural networks

Vendored references (read the file you need, do not load the whole tree):
- `refs/nn-zero-to-hero/` (MIT, Karpathy): lecture notes for micrograd (backprop), makemore (bigram to MLP to BatchNorm to WaveNet), GPT and the tokenizer. Start at `lectures/`.
- `refs/LLMs-from-scratch/` (Apache 2.0, Raschka): GPT built chapter by chapter in PyTorch. `ch02` data and tokens, `ch03` attention, `ch04` GPT model, `ch05` pretraining, `ch06` classification fine-tune, `ch07` instruction fine-tune, `appendix-A` PyTorch intro, `appendix-E` LoRA, `reasoning-from-scratch/` reasoning models.
- On demand, `./fetch-more.sh d2l` (Dive into Deep Learning, CC BY-SA, covers CNNs, RNNs, attention, optimization, vision, NLP) or `./fetch-more.sh fastbook` (fast.ai book, notebooks, practical top down).

## How to work
1. Name the task: classification, sequence, generation, audio, vision. Pick the smallest model that fits (linear or small MLP before a transformer).
2. Build the data pipeline and a baseline first. Overfit one tiny batch to prove the loop works.
3. Track loss on train and validation. Check shapes at every layer. Normalize inputs. Start Adam at 3e-4.
4. Debug in this order: data, shapes, loss function, learning rate, initialization (loss at step 0 should be about ln(classes)), then architecture.
5. Explain with the lecture's own derivation; cite the file you used.

## Notes for this repo
Voice work here uses pretrained Kokoro (ONNX) and pyworld. Training or fine-tuning a TTS or voice model needs a GPU and data we do not have in this container; use these references to reason about it, not to promise it.
