import os


def main():
    print("Консольный файловый менеджер. Для выхода введите 'exit'")

    while True:
        try:
            cwd = os.getcwd()
            command = input(f"\n[{cwd}]> ").strip()
            if not command:
                continue

            parts = command.split()
            cmd = parts[0].lower()

            if cmd == "exit":
                print("Выход из программы")
                break
            elif cmd == "pwd":
                print(cwd)
            elif cmd == "cd":
                if len(parts) < 2:
                    print("Ошибка: укажите директорию")
                    continue
                path = parts[1]
                try:
                    os.chdir(path)
                except Exception as e:
                    print(f"Ошибка: {str(e)}")

            elif cmd == "touch":
                if len(parts) < 2:
                    print("Ошибка: укажите имя файла")
                    continue
                filename = parts[1]
                try:
                    with open(filename, 'a'):
                        os.utime(filename, None)
                except Exception as e:
                    print(f"Ошибка: {str(e)}")

            elif cmd == "cat":
                if len(parts) < 2:
                    print("Ошибка: укажите имя файла")
                    continue
                filename = parts[1]
                try:
                    with open(filename, 'r') as f:
                        print(f.read())
                except Exception as e:
                    print(f"Ошибка: {str(e)}")

            elif cmd == "ls":
                try:
                    for item in os.listdir():
                        print(item)
                except Exception as e:
                    print(f"Ошибка: {str(e)}")

            elif cmd == "rm":
                if len(parts) < 2:
                    print("Ошибка: укажите имя файла")
                    continue
                filename = parts[1]
                try:
                    os.remove(filename)
                except Exception as e:
                    print(f"Ошибка: {str(e)}")

            else:
                print(f"Неизвестная команда: {cmd}")

        except KeyboardInterrupt:
            print("\nВыход из программы")
            break


if __name__ == "__main__":
    main()