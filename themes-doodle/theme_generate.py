import csv
from collections import Counter


for k in range(1, 6):
    urls = []
    correct_themes = []
    all_themes = []
    words = []
    f = open('t%d_final.csv' % k)
    csv_f = csv.reader(f)
    for i, row in enumerate(csv_f):
        if i == 0:
            continue
        urls.extend(row[0:5])
        correct_themes.extend(row[5:10])
        words.extend(row[10:15])
        all_themes.extend([row[15:25], row[25:35], row[35:45], row[45:55], row[55:65]])

    html_code = "<center><table border=1><tr><b><td>Doodle</td><td>Word</td><td>Themes</td></b></tr>"

    for url, word, correct, at in zip(urls, words, correct_themes, all_themes):
        assert correct == at[0]
        theme_data = "<b>%s</b><br>" % at[0] + '<br>'.join([x for x in at[1:]])
        row_data = "<td><img src='%s'></td><td>%s</td><td>%s</td>" % (url, word, theme_data)
        html_code += "<tr>%s</tr>" % row_data

    html_code += "</table></center>"

    with open('t%d/index.html' % k, 'w') as f:
        f.write(html_code)
