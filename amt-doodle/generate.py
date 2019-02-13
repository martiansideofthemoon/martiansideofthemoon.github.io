import csv
import operator

urls = []
themes = []
words = []
answers = []
f = open('final.csv')
csv_f = csv.reader(f)
for i, row in enumerate(csv_f):
    if i == 0:
        continue
    urls.extend(row[27:32])
    themes.extend(row[32:37])
    words.extend(row[37:42])
    answers.extend(row[45:50])

all_data = {}
for url, word, theme, answer in zip(urls, words, themes, answers):
    if url in all_data:
        assert all_data[url]['word'] == word
        assert all_data[url]['theme'] == theme
        all_data[url]['answers'].append(answer.lower())
    else:
        all_data[url] = {
            'word': word.lower(),
            'theme': theme,
            'answers': [answer.lower()]
        }

all_data = [(url, data) for url, data in all_data.items()]
all_data.sort(key=lambda x: sum([ans == x[1]['word'] for ans in x[1]['answers']]), reverse=True)

html_code = "<center><table border=1><tr><b><td>Doodle</td><td>Theme</td><td>Word</td><td>Score</td><td>Answers</td></b></tr>"

for (url, data) in all_data:
    row_data = "<td><img src='%s'></td><td>%s</td><td>%s</td><td>%d / 5</td><td>%s</td>" % (url, data['theme'], data['word'], sum([ans == data['word'] for ans in data['answers']]), ', '.join(data['answers']))
    html_code += "<tr>%s</tr>" % row_data

html_code += "</table></center>"

with open('index.html', 'w') as f:
    f.write(html_code)
