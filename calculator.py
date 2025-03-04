def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Hata! Sıfıra bölme yapılamaz."
    return x / y

print("Basit Hesap Makinesi")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

while True:
    choice = input("Seçiminizi yapın (1/2/3/4) veya çıkmak için 'q' girin: ")
    
    if choice == 'q':
        print("Hesap makinesi kapatılıyor...")
        break
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Birinci sayıyı girin: "))
        num2 = float(input("İkinci sayıyı girin: "))
        
        if choice == '1':
            print("Sonuç:", add(num1, num2))
        elif choice == '2':
            print("Sonuç:", subtract(num1, num2))
        elif choice == '3':
            print("Sonuç:", multiply(num1, num2))
        elif choice == '4':
            print("Sonuç:", divide(num1, num2))
    else:
        print("Geçersiz giriş! Lütfen 1, 2, 3 veya 4 girin.")
