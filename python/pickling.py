import pickle

d = dict(name="Randy", age=37, role="QA")

with open('dumps.txt', 'wb') as f:
    pickle.dump(d, f)

with open('/Users/yunpengli/PycharmProjects/yaamnotes/dumps.txt', 'rb') as f:
    nd = pickle.load(f)

print(nd)