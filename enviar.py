# encoding: utf-8

#pip install python-simplemail
import simplemail

def enviar(destino, sub, msg=""):
    e=simplemail.Email(
        smtp_server='smtp.gmail.com:587',
        smtp_user='nome_usuario',
        smtp_password='sua_senha',
        use_tls='True',
        from_address='email_de_envio@gmail.com',
        to_address=destino,
        subject=sub,
        message=msg).send()


enviar('destinatario@gmail.com','ENVIADO COM PYTHON', 'QUEIJO EH BOM, JUJUBA EH MELHOR AINDA')
print('enviado com sucesso!')
