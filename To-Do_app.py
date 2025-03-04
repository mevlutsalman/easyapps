# Basit To-Do Uygulaması

# Yapılacaklar listesi
todo_list = []

# Fonksiyonlar
def display_todos():
    if len(todo_list) == 0:
        print("Yapılacak bir şey yok!")
    else:
        print("\nYapılacaklar Listesi:")
        for index, todo in enumerate(todo_list, 1):
            print(f"{index}. {todo}")

def add_todo():
    todo_item = input("Eklemek istediğiniz öğeyi yazın: ")
    todo_list.append(todo_item)
    print(f"'{todo_item}' listeye eklendi.")

def remove_todo():
    display_todos()
    try:
        todo_index = int(input("Silmek istediğiniz öğenin numarasını girin: "))
        if 1 <= todo_index <= len(todo_list):
            removed_item = todo_list.pop(todo_index - 1)
            print(f"'{removed_item}' listeden silindi.")
        else:
            print("Geçersiz numara.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def main():
    while True:
        print("\n--- To-Do Uygulaması ---")
        print("1. Yapılacaklar Listesini Görüntüle")
        print("2. Öğe Ekle")
        print("3. Öğe Sil")
        print("4. Çıkış")
        
        choice = input("Seçiminizi yapın (1-4): ")
        
        if choice == '1':
            display_todos()
        elif choice == '2':
            add_todo()
        elif choice == '3':
            remove_todo()
        elif choice == '4':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

# Uygulamayı çalıştırma
if __name__ == "__main__":
    main()
