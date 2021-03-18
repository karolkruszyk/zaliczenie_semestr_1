def get_disk_size():
    size = int(input("Podaj deklarowany rozmiar dysku (GB): "))
    real_size = size * 1000 * 1000 * 1000
    real_size = real_size / 1024 / 1024 / 1024
    return real_size


real_disk_size = get_disk_size()
print("Realny rozmiar dysku:",round(real_disk_size, 2), "GB")
