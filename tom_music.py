import librosa
import soundfile as sf

def change_pitch(audio_path, semitones, output_path):
    # Carrega o arquivo de áudio
    audio, sr = librosa.load(audio_path)

    # Transpõe o tom
    transposed_audio = librosa.effects.pitch_shift(audio, sr=sr, n_steps=semitones)

    # Salva o áudio transposto
    sf.write(output_path, transposed_audio, sr)

if __name__ == "__main__":
    # Caminho para o arquivo de áudio de entrada
    input_audio_path = input("Digite o caminho para o arquivo de áudio de entrada: ")

    # Tom de transposição em semitons (número positivo para subir, negativo para descer)
    semitones = float(input("Digite o número de semitons para transpor (positivo para subir, negativo para descer): "))

    # Caminho para salvar o arquivo de áudio transposto
    output_audio_path = input("Digite o caminho para salvar o arquivo de áudio transposto: ")

    # Transpõe o tom da música e salva o arquivo
    change_pitch(input_audio_path, semitones, output_audio_path)

    print("Transposição concluída com sucesso!"
)