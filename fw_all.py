import os
from faster_whisper import WhisperModel

model_size = "/data/asr_large_model/whisper_model/faster-whisper-large-v2"

# Run on GPU with FP16
model = WhisperModel(model_size, device="cuda", compute_type="float16")

# 或者在GPU上使用INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# 或者在CPU上使用INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

# 指定BEA-Base目录的路径
base_directory = "/data/BEA-Base/train-114"

# 遍历每个子文件夹
for folder in os.listdir(base_directory):
    folder_path = os.path.join(base_directory, folder)
    
    # 检查子文件夹是否存在并且是一个目录
    if os.path.isdir(folder_path):
        # 遍历子文件夹中的所有文件
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # 检查文件是否以.wav结尾
            if filename.endswith(".wav"):
                # 进行音频转录
                segments, info = model.transcribe(file_path, beam_size=5, language='hu')
                print(f"Transcribing {file_path}:")
                for segment in segments:
                    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

