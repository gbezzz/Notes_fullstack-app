from django.core.mail import send_mail


def send_daily_email():
    send_mail(
        "Daily Update",
        "This is your daily update email.",
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )
