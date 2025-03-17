def calculate_average(numbers):
    try:
        if not isinstance(numbers, list):
            raise TypeError("Input harus berupa list")
        
        total = sum(numbers)
        average = total / len(numbers)
        return average

    except TypeError as e:
        return f"Error: {e}"
    except ZeroDivisionError:
        return "Error: List tidak boleh kosong"
    except Exception as e:
        return f"Error: Terjadi kesalahan - {e}"

# Contoh penggunaan
print(calculate_average([5, 5, 7, 8]))  # Input benar
print(calculate_average("5,5,7,8"))      # Input salah (string)
print(calculate_average(5))              # Input salah (intege