import smtplib
from time import sleep
from email.message import EmailMessage
import imghdr
import threading


class EmailSender:
    def __init__(self, origin_email, email_password):
        self.origin_email = origin_email
        self.email_password = email_password

    def set_content(self, subject, your_email, contact_list, email_content):
        self.mail = EmailMessage()
        self.mail['Subject'] = subject
        message = email_content
        self.mail['From'] = your_email
        self.mail['To'] = ', '.join(contact_list)
        self.mail.add_header('Content-Type', 'text/html')
        self.mail.set_payload(message.encode('utf-8'))

    def attach_image(self, image_list):
        for image in image_list:
            with open(image, 'rb') as arquivo:
                data = arquivo.read()
                image_extension = imghdr.what(arquivo.name)
                file_name = arquivo.name
                self.mail.add_attachment(data, maintype='image', subtype=image_extension, filename=file_name)

    def send_email(self, time_to_sleep):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
            email.login(user=self.origin_email, password=self.email_password)
            email.send_message(self.mail)
            sleep(time_to_sleep)


def leiadinheiro(mensagem):
    while True:
        valor = input(mensagem)
        if ',' in valor:
            valor = valor.replace(',', '.')
        qtd_pontos = valor.count('.')
        if (qtd_pontos == 0 or qtd_pontos == 1) and valor.replace('.', '').isnumeric():
            valor = float(valor)
            break
        else:
            print(f'"{valor}" é um valor incorreto! ')
    return valor


def dinheiro_formatado(n):
    try:
        n = float(n)
    except:
        return None
    else:
        return f'{n:.2f}'.replace('.', ',')


def enviar_email_simplificado(msg, contatos):
    with open('senha_e_email.txt', 'r', encoding='utf-8') as senha_e_email:
        dados = senha_e_email.read().split('\n')
    print(dados)

    var_email = EmailSender(dados[0], dados[1])
    var_email.set_content('Cotação do dólar', dados[0], contatos, msg)
    var_email.send_email(60)
