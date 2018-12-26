import numpy as np
import pickle

with open('hp.pickle', 'rb') as f:
    data = pickle.load(f)


output = "<html><body><center><table border=1>"

classes = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'l', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

for k, v in data.items():
    np_arr = np.array(v)
    top_k_args = np_arr.argsort()[-10:][::-1]
    top_k_vals = np_arr[top_k_args]
    distro = "<br>".join(["<b>%s</b> = %.2f&#37;" % (classes[arg], val * 100.0) for arg, val in zip(top_k_args, top_k_vals)])
    output += "<tr><td><img src='%s'></td><td>%s</td></tr>" % (k, distro)

output += "</table></body></center></html>"

with open('index.html', 'w') as f:
    f.write(output)
