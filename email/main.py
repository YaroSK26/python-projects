import smtplib
import requests

response = requests.get("https://api.kanye.rest")
quote = response.json()["quote"]

my_email = "your email"
password = "your password"
message = "Hello, this is a test email"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    # connection.sendmail(from_addr=my_email, to_addrs="receiver email", msg=f"Subject:Hello\n\n{message}")
    connection.sendmail(from_addr=my_email, to_addrs="receiver email", msg=quote.encode("utf-8"))