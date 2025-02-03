import time

def read_numbers_from_file(filename):
    """Lee números desde un archivo y maneja errores."""
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    numbers.append(int(line.strip()))
                except ValueError:
                    print(f"Error: '{line.strip()}' no es un número válido.")
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    return numbers

def decimal_to_binary(n):
    """Convierte un número decimal a binario usando algoritmos básicos."""
    binary = ""
    if n == 0:
        return "0"
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def decimal_to_hexadecimal(n):
    """Convierte un número decimal a hexadecimal usando algoritmos básicos."""
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    if n == 0:
        return "0"
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n //= 16
    return hexadecimal

def convert_numbers(filename):
    """Función principal para convertir números de un archivo a binario y hexadecimal."""
    start_time = time.time()
    numbers = read_numbers_from_file(filename)
    
    if not numbers:
        print("No se pudieron procesar los datos correctamente.")
        return
    
    results = []
    for num in numbers:
        results.append(f"Decimal: {num} | Binario: {decimal_to_binary(num)} | Hexadecimal: {decimal_to_hexadecimal(num)}")
    
    elapsed_time = time.time() - start_time
    results.append(f"Tiempo de ejecución: {elapsed_time} segundos")
    
    result_text = "\n".join(results)
    print(result_text)
    
    with open("ConvertionResults.txt", "w", encoding='utf-8') as output_file:
        output_file.write(result_text)
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py fileWithData.txt")
    else:
        convert_numbers(sys.argv[1])
