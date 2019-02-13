import csv
from collections import Counter

urls = []
themes = []
words = []
answers = []
workers = []
f = open('final.csv')
csv_f = csv.reader(f)
for i, row in enumerate(csv_f):
    if i == 0:
        continue
    urls.extend(row[27:32])
    themes.extend(row[32:37])
    words.extend(row[37:42])
    answers.extend(row[45:50])
    workers.extend([row[15], row[15], row[15], row[15], row[15]])

all_data = {}
for url, word, theme, answer, worker in zip(urls, words, themes, answers, workers):
    if url in all_data:
        assert all_data[url]['word'] == word
        assert all_data[url]['theme'] == theme
        all_data[url]['answers'].append(answer.lower())
        all_data[url]['workers'].append(worker)
    else:
        all_data[url] = {
            'word': word.lower(),
            'theme': theme,
            'answers': [answer.lower()],
            'workers': [worker]
        }

all_data = [(url, data) for url, data in all_data.items()]
all_data.sort(key=lambda x: sum([ans == x[1]['word'] for ans in x[1]['answers']]), reverse=True)
all_workers = []
unique_workers = {}
for d in all_data:
    for answer, worker in zip(d[1]['answers'], d[1]['workers']):
        if worker in unique_workers:
            unique_workers[worker].append(answer == d[1]['word'])
        else:
            unique_workers[worker] = [answer == d[1]['word']]
    all_workers.extend(d[1]['workers'])

for k, v in unique_workers.items():
    print("%s = %d / %d" % (k, sum(v), len(v)))

html_code = "<center><table border=1><tr><b><td>Doodle</td><td>Theme</td><td>Word</td><td>Score</td><td>Answers</td></b></tr>"

for (url, data) in all_data:
    answer_worker = '<br>'.join(["<b>%s = %s</b>" % (w, ans) if ans == data['word'] else "%s = %s" % (w, ans) for w, ans in zip(data['workers'], data['answers'])])
    row_data = "<td><img src='%s'></td><td>%s</td><td>%s</td><td>%d / 5</td><td>%s</td>" % (url, data['theme'], data['word'], sum([ans == data['word'] for ans in data['answers']]), answer_worker)
    html_code += "<tr>%s</tr>" % row_data

html_code += "</table></center>"

with open('index.html', 'w') as f:
    f.write(html_code)
