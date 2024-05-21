from faster_whisper import WhisperModel

model_size = "/data/asr_large_model/whisper_model/faster-whisper-large-v2"

# Run on GPU with FP16
model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
#model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("/data/BEA-Base/train-114/001/bea_001_m_41_stm_0370.wav", beam_size=5, language='hu')


for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
