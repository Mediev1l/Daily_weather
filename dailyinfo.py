from forecast import weather, mail, mail_list
from datetime import date


weather = weather.WeatherApi()
mail = mail.SendMail()
today = date.today()
formated = today.strftime('%d/%m/%Y')

subject = 'Daily forecast'

message =f"""\
Pogoda na dzień {formated}

Prognoza na dzisiejszy dzień: {weather.day_forecast()}.
Prognoza na dzisiejszą noc: {weather.night_forecast()}.

Temperatura minimalna to {weather.temp_min()} a maksymalna {weather.temp_max()}.
Odczuwalna temperatura od {weather.real_feel_min()} do {weather.real_feel_max()}."""


for email in mail_list.mails:
    mail.send_mail(email, subject, message)