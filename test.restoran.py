def create_booking(name: str, people: int) -> dict:
    if not name or not name.strip():
        raise ValueError("Имя клиента не может быть пустым")

    if people < 1:
        raise ValueError("Количество людей должно быть больше 0")

    return {"name": name.strip(), "people": people}

def calculate_price(people: int, hour: float) -> float:
    base_price = 1000 if hour < 18.0 else 1500
    return float(base_price * people)