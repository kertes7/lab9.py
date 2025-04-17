def calculate_cosmic_distance(speed_fraction, time_years):
    return speed_fraction * time_years

def calculate_gravitational_force(mass1, mass2, cosmic_factor=1.0):
    return mass1 * mass2 * cosmic_factor

def calculate_time_dilation(speed_fraction, time_seconds):
    if speed_fraction >= 1:
        raise ValueError("Частка швидкості світла повинна бути меншою за 1.")
    return time_seconds / (1 - speed_fraction)

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Будь ласка, введіть коректне число.")

def main():
    print("🚀 Вітаємо у калькуляторі 'Таємниці Всесвіту'!")
    while True:
        print("\nОберіть розрахунок:")
        print("1. Космічна відстань")
        print("2. Спрощена гравітація")
        print("3. Сповільнення часу")

        choice = input("Ваш вибір (1/2/3): ")

        if choice == "1":
            speed = get_float_input("Введіть частку від швидкості світла (0 < x ≤ 1): ")
            time = get_float_input("Введіть час у роках: ")
            result = calculate_cosmic_distance(speed, time)
            print(f"🌌 Відстань, яку пройде об'єкт: {result:.2f} світлових років.")

        elif choice == "2":
            m1 = get_float_input("Введіть масу першого об'єкта: ")
            m2 = get_float_input("Введіть масу другого об'єкта: ")
            factor = get_float_input("Космічний коефіцієнт (за замовчуванням 1.0): ") or 1.0
            result = calculate_gravitational_force(m1, m2, factor)
            print(f"🪐 Спрощена гравітаційна взаємодія: {result:.2f} умовних одиниць.")

        elif choice == "3":
            speed = get_float_input("Введіть частку швидкості світла (менше 1): ")
            time = get_float_input("Введіть час у секундах: ")
            try:
                result = calculate_time_dilation(speed, time)
                print(f"⏳ Сповільнений час: {result:.2f} секунд.")
            except ValueError as e:
                print(f"⚠️ Помилка: {e}")

        else:
            print("Невірний вибір. Спробуйте знову.")

        again = input("🔁 Бажаєте зробити ще один розрахунок? (так/ні): ").strip().lower()
        if again != "так":
            print("🌠 Дякуємо за використання калькулятора 'Таємниці Всесвіту'! До нових зустрічей!")
            break

if __name__ == "__main__":
    main()
