
import math


def parse_booking(text):
    try:
        if not isinstance(text, str):
            return None

        if text.count(':') != 1:
            return None

        service, minutes = text.split(':')
        service = service.strip()
        minutes = minutes.strip()

        if not service or not minutes:
            return None

        duration = float(minutes)

        if not math.isfinite(duration) or duration < 0:
            return None

        return service.title(), duration

    except (ValueError, TypeError):
        return None


def duration_average(durations_csv):
    try:
        if not isinstance(durations_csv, str):
            return None

        if not durations_csv.strip():
            return None

        values = [int(r.strip()) for r in durations_csv.split(',')]

        if not values or any(value < 0 for value in values):
            return None

        return sum(values) // len(values)

    except (ValueError, TypeError):
        return None


def payable_bill(text):
    try:
        if not isinstance(text, str):
            return None

        if text.count('|') != 1:
            return None

        bill, discount = text.split('|')
        bill = float(bill.strip())
        discount = float(discount.strip())

        if not math.isfinite(bill) or not math.isfinite(discount):
            return None

        if bill < 0 or discount < 0:
            return None

        total = bill * 1.18 - discount

        return max(total, 0)

    except (ValueError, TypeError):
        return None


def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter service:duration in min (e.g. haircut:45): ")
    result = parse_booking(user_input)
    print("Service and Duration:", result)

    print("\n==== Running duration_average ====")
    user_input = input("Enter durations as CSV (e.g. 30,45,60): ")
    result = duration_average(user_input)
    print("Average Duration:", result)

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 800|100): ")
    result = payable_bill(user_input)
    print("Payable Bill:", result)


if __name__ == "__main__":
    main()
