import news
import weather
import quote
import dog_picture as dp
import datetime as dt

# delimiters
f = open('email_part_1.html', 'r')
s_accumulator = f.read()
f.close()

f = open('email_part_2.html', 'r')
after_dog_image = f.read()
f.close()

s_end = '</div>\n</body>\n</html>\n'


''' Add dog picture '''
dp.get_dog_picture()

s_accumulator += dp.dog_data['url']
s_accumulator += after_dog_image


''' Add News and Weather - accounts for articles not paired with an image'''
news.get_news()
weather.get_weather()
quote.get_quote()

# News
s_accumulator += '<hr style="width:90%">\n'
s_accumulator += '<h1>News This Week</h1>\n'

# first business article
s_accumulator += '<h2><a style="text-decoration: none; color: DarkSlateGray;" href="' + news.business_articles[0][1] + '">' + news.business_articles[0][0] + '</a></h2>\n'
s_accumulator += '<img src="' + news.business_articles[0][2] + '" width="50%"></a>\n' if news.business_articles[0][2] != None else '<p>no image available :(</p>\n'
# second business article
s_accumulator += '<h2><a style="text-decoration: none; color: DarkSlateGray;" href="' + news.business_articles[1][1] + '">' + news.business_articles[1][0] + '</a></h2>\n'
s_accumulator += '<img src="' + news.business_articles[1][2] + '" width="50%"></a>\n' if news.business_articles[1][2] != None else '<p>no image available :(</p>\n'
# third business article
s_accumulator += '<h2><a style="text-decoration: none; color: DarkSlateGray;" href="' + news.business_articles[2][1] + '">' + news.business_articles[2][0] + '</a></h2>\n'
s_accumulator += '<img src="' + news.business_articles[2][2] + '" width="50%"></a>\n' if news.business_articles[2][2] != None else '<p>no image available :(</p>\n'
# first science article
s_accumulator += '<h2><a style="text-decoration: none; color: DarkSlateGray;" href="' + news.science_articles[0][1] + '">' + news.science_articles[0][0] + '</a></h2>\n'
s_accumulator += '<img src="' + news.science_articles[0][2] + '" width="50%"></a>\n' if news.science_articles[0][2] != None else '<p>no image available :(</p>\n'
# second science article
s_accumulator += '<h2><a style="text-decoration: none; color: DarkSlateGray;" href="' + news.science_articles[1][1] + '">' + news.science_articles[1][0] + '</a></h2>\n'
s_accumulator += '<img src="' + news.science_articles[1][2] + '" width="50%"></a>\n' if news.science_articles[1][2] != None else '<p>no image available :(</p>\n'
# third science article
s_accumulator += '<h2><a style="text-decoration: none; color: DarkSlateGray;" href="' + news.science_articles[2][1] + '">' + news.science_articles[2][0] + '</a></h2>\n'
s_accumulator += '<img src="' + news.science_articles[2][2] + '" width="50%"></a>\n' if news.science_articles[2][2] != None else '<p>no image available :(</p>\n'
# end news
s_accumulator += '<hr style="width:90%">\n'
s_accumulator += '<div style="text-align:center; padding-bottom: 20px;">'


# Weather
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
today = dt.datetime.today().weekday()

s_accumulator += '<h1>Blacksburg Weather</h1>\n'
s_accumulator += '<li>Today: ' + str(weather.weather_data['day1_high']) + '/' + str(weather.weather_data['day1_low']) + u'\N{DEGREE SIGN}F. ' + weather.weather_data['summary'] + '. ' + 'Wind: ' + weather.weather_data['wind'] + '. Precip: ' + weather.weather_data['precip'] + '. Sunrise: ' + weather.weather_data['sunrise'] + '. Sunset: ' + weather.weather_data['sunset'] + '.</li>\n'
s_accumulator += '<li>' + days_of_week[(today + 1) % 7] + ': ' + str(weather.weather_data['day2_high']) + '/' + str(weather.weather_data['day2_low']) + u'\N{DEGREE SIGN}F, ' + str(weather.weather_data['day2_conditions']) + '</li>\n'
s_accumulator += '<li>' + days_of_week[(today + 2) % 7] + ': ' + str(weather.weather_data['day3_high']) + '/' + str(weather.weather_data['day3_low']) + u'\N{DEGREE SIGN}F, ' + str(weather.weather_data['day3_conditions']) + '</li>\n'
s_accumulator += '<li>' + days_of_week[(today + 3) % 7] + ': ' + str(weather.weather_data['day4_high']) + '/' + str(weather.weather_data['day4_low']) + u'\N{DEGREE SIGN}F, ' + str(weather.weather_data['day4_conditions']) + '</li>\n'
s_accumulator += '<li>' + days_of_week[(today + 4) % 7] + ': ' + str(weather.weather_data['day5_high']) + '/' + str(weather.weather_data['day5_low']) + u'\N{DEGREE SIGN}F, ' + str(weather.weather_data['day5_conditions']) + '</li>\n'


s_accumulator += '</div>'
s_accumulator += '<hr style="width:90%">\n'

# Quote of the week
s_accumulator += '<h1>Quote of the Week</h1>\n'
s_accumulator += '<p>"' + quote.quote_data['quote'] + '" -' + quote.quote_data['author'] + '</p>' if quote.quote_data['quote'] != 'QUOTE_ERROR' else '<p>Quote error :(</p>'

# full email var used in email sender
full_email = s_accumulator + s_end
# writing to file just to keep
# f = open("full_email.html", "w")
# f.write(s_accumulator)
# f.write(s_end)
# f.close()