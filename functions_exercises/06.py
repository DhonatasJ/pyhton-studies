from datetime import datetime

def convert(horario24h, datetime):
    horario12h = datetime.strptime(horario24h, "%H:%M").strftime("%I:%M %p")
    return horario12h

horario24h = input("Informe a hora formato 24h, EX: 00:00 ")
result = convert(horario24h, datetime)
print(result)