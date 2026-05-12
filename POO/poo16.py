# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, message) -> None:
        self.message = message

    @abstractmethod
    def send(self) -> bool: ...

class NotificationEmail(Notification):
    def send(self) -> bool:
        print("Email: sending:", self.message)
        return True

class NotificationSMS(Notification):
    def send(self) -> bool:
        print("SMS: sending:", self.message)
        return True

# n = NotificationEmail("Testing Notification")
# n.send()

def notify(notification: Notification):
    notification_sent = notification.send()

    if notification_sent:
        print("Sent Notification")
    else:
        print("Not Sent Notification")

notification_email = NotificationEmail("E-mail")
notify(notification_email)

notification_sms = NotificationSMS("SMS")
notify(notification_sms)