import pickle

with open('creativity.pickle', 'rb') as f:
    all_data = pickle.load(f)

html_code = "<center><table border=1><tr><b><td>Doodle</td><td>Theme</td><td>Dataset</td><td>Comments</td><td>Scores</td></b></tr>"

data_points = sorted([(url, data) for (url, data) in all_data.items()], key=lambda x: (' '.join(x[1][0][0]), x[1][0][1]))
for url, data in data_points:
    assert data[0][0] == data[1][0]
    themes = '; '.join(data[0][0])
    assert data[0][1] == data[1][1]
    dataset = data[0][1]
    comments = '<br><br>'.join([x[2] for x in data])
    scores = '<br><br>'.join([str(x[3]) for x in data])
    row_data = "<td><img src='%s'></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>" % (url, themes, dataset, comments, scores)
    html_code += "<tr>%s</tr>" % row_data

html_code += "</table></center>"

with open('index.html', 'w') as f:
    f.write(html_code)
