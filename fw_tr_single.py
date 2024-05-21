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
#base_directory = "/data/BEA-Base/train-114"
base_directory = "/data/BEA-Base/train-114/001"

# 存储已完成转录的结果
completed_transcriptions = []

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
                # 获取音频文件的id（去掉扩展名）
                audio_id = os.path.splitext(filename)[0]
                
                # 进行音频转录
                segments, info = model.transcribe(file_path, beam_size=5, language='hu')
                print(f"Transcribing {file_path}:")
                
                # 将转录结果保存到相应的.txt文件中
                output_path = os.path.join("/data/faster-whisper/BEA-Base/train/001", f"{audio_id}.txt")
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    for segment in segments:
                        output_file.write("[%.2fs -> %.2fs] %s\n" % (segment.start, segment.end, segment.text))
                
                # 记录已完成的转录结果
                completed_transcriptions.append(f"{audio_id}: {len(list(segments))} segments")
                
# 输出已完成的结果
print("已完成的转录结果:")
for result in completed_transcriptions:
    print(result)

