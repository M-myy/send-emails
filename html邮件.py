import smtplib
from email.mime.text import MIMEText
from email.header import Header

recipient_addr = []  #收件人地址
f = open('mail.db')    #读取文件，载入邮箱
recipient_addr = f.read().split('\n')
f.close()

smtp_obj = smtplib.SMTP_SSL('smtp.qq.com',465)  #发件人邮箱中的SMTP服务器,默认端口是25
smtp_obj.login('**********@qq.com','***************')  #邮箱账号、密码（授权码）
#smtp_obj.set_debuglevel(1)

mail_body = '''
    <script>
        alert("hahhahh")
    </script>
    <h5>一封信,title</h5>
    <p>
        这是一份html的测试邮件,正文
    </p>
    <h5>2.来自HTML</h5>
    <p>
        test
    </p>
'''

#设置邮箱信息
msg = MIMEText(mail_body,'html','utf-8')  #内容，正文，utf-8
msg['From'] = Header('来自我的问候','utf-8')  #发送者
msg['To'] = Header('for you','utf-8')  #接收者
msg['Subject'] = Header('一封信')  #主题

#发送
smtp_obj.sendmail('*******@qq.com',recipient_addr,msg.as_string())
