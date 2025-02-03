import time

def read_numbers_from_file(filename):
    """Lee números desde un archivo y maneja errores."""
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Error: '{line.strip()}' no es un número válido.")
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    return numbers

def mean(numbers):
    """Calcula la media de una lista de números."""
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calcula la mediana de una lista de números."""
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    return (numbers[mid] if n % 2 != 0 else (numbers[mid - 1] + numbers[mid]) / 2)

def mode(numbers):
    """Calcula la moda de una lista de números."""
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    return [num for num, freq in frequency.items() if freq == max_freq]

def variance(numbers, mean_value):
    """Calcula la varianza de una lista de números."""
    return sum((x - mean_value) ** 2 for x in numbers) / len(numbers)

def std_dev(variance_value):
    """Calcula la desviación estándar."""
    return variance_value ** 0.5

def compute_statistics(filename):
    """Función principal para calcular estadísticas descriptivas."""
    start_time = time.time()
    numbers = read_numbers_from_file(filename)
    
    if not numbers:
        print("No se pudieron procesar los datos correctamente.")
        return
    
    mean_value = mean(numbers)
    median_value = median(numbers)
    mode_value = mode(numbers)
    variance_value = variance(numbers, mean_value)
    std_dev_value = std_dev(variance_value)
    elapsed_time = time.time() - start_time
    
    result = (
        f"Media: {mean_value}\n"
        f"Mediana: {median_value}\n"
        f"Moda: {mode_value}\n"
        f"Varianza: {variance_value}\n"
        f"Desviación estándar: {std_dev_value}\n"
        f"Tiempo de ejecución: {elapsed_time} segundos\n"
    )
    
    print(result)
    with open("StatisticsResults.txt", "w", encoding='utf-8') as output_file:
        output_file.write(result)
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py fileWithData.txt")
    else:
        compute_statistics(sys.argv[1])
