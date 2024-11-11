import smtplib

sender_email = "sender@gmail.com"
sender_password = "12345Pass!"

connection = smtplib.SMTP("smtp.gmail.com")
# --- Make the connection secure
connection.starttls()
# --- login
connection.login(user=sender_email, password=sender_password)
# --- Send message
connection.send_message(
    from_addr=sender_email, 
    to_addrs="recipient@mailservice.com", 
    msg="Subject:Hello\n\nThe Message"
)
# --- Close the connection
connection.close()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender_email, password=sender_password)
    connection.send_message(
        from_addr=sender_email, 
        to_addrs="recipient@mailservice.com", 
        msg="Subject:Hello\n\nThe Message"
    )
