import news
import weather
import quote

# delimiters
f = open('email_accumulator.html', 'r')
s_accumulator = f.read()
f.close()

s_end = '</div>\n</body>\n</html>\n'


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
s_accumulator += '<h1>Blacksburg Weather</h1>\n'
s_accumulator += '<li>Today: ' + str(weather.weather_data['mon_high']) + '/' + str(weather.weather_data['mon_low']) + u'\N{DEGREE SIGN}F. ' + weather.weather_data['summary'] + '. ' + 'Wind: ' + weather.weather_data['wind'] + '. Precip: ' + weather.weather_data['precip'] + '. Sunrise: ' + weather.weather_data['sunrise'] + '. Sunset: ' + weather.weather_data['sunset'] + '.</li>\n'
s_accumulator += '<li>Tuesday: ' + str(weather.weather_data['tues_high']) + '/' + str(weather.weather_data['tues_low']) + u'\N{DEGREE SIGN}F, ' + str(weather.weather_data['tues_conditions']) + '</li>\n'
s_accumulator += '<li>Wednesday: ' + str(weather.weather_data['wed_high']) + '/' + str(weather.weather_data['wed_low']) + u'\N{DEGREE SIGN}F, ' + str(weather.weather_data['wed_conditions']) + '</li>\n'
s_accumulator += '<li>Thursday: ' + str(weather.weather_data['thurs_high']) + '/' + str(weather.weather_data['thurs_low']) + u'\N{DEGREE SIGN}F, ' + str(weather.weather_data['thurs_conditions']) + '</li>\n'
s_accumulator += '<li>Friday: ' + str(weather.weather_data['fri_high']) + '/' + str(weather.weather_data['fri_low']) + u'\N{DEGREE SIGN}F, ' + str(weather.weather_data['fri_conditions']) + '</li>\n'


s_accumulator += '</div>'
s_accumulator += '<hr style="width:90%">\n'

# Quote of the week
s_accumulator += '<h1>Quote of the Week</h1>\n'
s_accumulator += '<p>"' + quote.quote_data['quote'] + '" -' + quote.quote_data['author'] + '</p>' if quote.quote_data['quote'] != 'QUOTE_ERROR' else '<p>Quote error :(</p>'

# full email var used in email sender
full_email = s_accumulator + s_end
# writing to file just to keep
f = open("full_email.html", "w")
f.write(s_accumulator)
f.write(s_end)
f.close()