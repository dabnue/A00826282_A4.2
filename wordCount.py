import time

def read_words_from_file(filename):
    """Lee palabras desde un archivo y maneja errores."""
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words.extend(line.strip().split())
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    return words

def count_word_frequencies(words):
    """Cuenta la frecuencia de cada palabra en una lista."""
    word_count = {}
    for word in words:
        word = word.lower().strip(".,!?()[]{}:;\"'")  # Normalizar palabras
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

def word_count(filename):
    """Función principal para contar palabras en un archivo."""
    start_time = time.time()
    words = read_words_from_file(filename)
    
    if not words:
        print("No se pudieron procesar los datos correctamente.")
        return
    
    word_frequencies = count_word_frequencies(words)
    elapsed_time = time.time() - start_time
    
    results = [f"{word}: {count}" for word, count in sorted(word_frequencies.items())]
    results.append(f"Tiempo de ejecución: {elapsed_time} segundos")
    
    result_text = "\n".join(results)
    print(result_text)
    
    with open("WordCountResults.txt", "w", encoding='utf-8') as output_file:
        output_file.write(result_text)
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py fileWithData.txt")
    else:
        word_count(sys.argv[1])
