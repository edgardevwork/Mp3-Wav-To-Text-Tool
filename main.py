import whisper
import os

# Указываем путь к папке с ffmpeg.exe
ffmpeg_path = r"C:\...\ffmpeg\bin"  # Здесь должна лежать ffmpeg.exe
os.environ["PATH"] += f";{ffmpeg_path}"  # Добавляем к текущей PATH

# 📌 Выбор модели: чем больше модель → тем выше точность, но медленнее работа
# tiny / base   - очень быстро, подходит только для коротких фраз или прототипов
# small         - хороший баланс между скоростью и качеством (~7–9% ошибок на русском)
# medium        - стандарт качества для русского языка (~5–6% ошибок), работает без GPU
# large-v3      - максимальная точность (~4–5% ошибок), требует много памяти CPU/GPU
# large-v3-turbo- быстрее версии large-v3 при почти той же точности
model = whisper.load_model("base") # Или попробуй "base", если нужно ускорить процесс!

# Используем абсолютный путь!
audio_file = r"C:\...\2.mp3"

result = model.transcribe(
    audio_file,
    language="ru",
    verbose=False,
    word_timestamps=False
)

with open("output.txt", "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        f.write(f"[{segment['start']:.2f} - {segment['end']:.2f}] {segment['text'].strip()}\n")

print("Готово!")