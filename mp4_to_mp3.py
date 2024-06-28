import ffmpeg

def convert_to_mp3(input_file, output_file):
    probe = ffmpeg.probe(input_file)
    audio_streams = [stream for stream in probe['streams'] if stream['codec_type'] == 'audio']
    
    if not audio_streams:
        print("O arquivo de entrada não contém uma faixa de áudio.")
        return

    (
        ffmpeg.input(input_file)
        .output(output_file, format='mp3')
        .run()
    )

if __name__ == "__main__":
    input_file_path = input("Digite o caminho para o arquivo MP4 de entrada: ")
    output_file_path = input("Digite o caminho para salvar o arquivo MP3 de saída: ")

    convert_to_mp3(input_file_path, output_file_path)

    print("Conversão concluída com sucesso!")
