# 寄送 Email 的程式
# 準備訊息物件設定
from email.message import EmailMessage
msg=EmailMessage()
msg["From"]="寄件人"
msg["To"]="收件人"
msg["Subject"]="主旨"

# 寄送純文字的內容
# msg.set_content("測試看看")

# 寄送比較多樣式的內容(html)
msg.add_alternative("<h1>恭喜您<h1>成功發送此郵件", subtype="html")

# 連線到 SMTP Server ,驗證寄件人身分並發送郵件
import smtplib
# 到網路上搜尋 gmail smtp server 或是 yahoo smtp server
server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("帳號", "密碼")
server.send_message(msg)
server.close()