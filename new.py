import pickle

filename = 'resumeScreener.pkl'
# pickle.dump(model, open(filename, 'wb'))
 
# some time later...
 
# load the model from disk
# loaded_model = pickle.load(open(filename, 'rb'))

# print(loaded_model)

with open('filename', 'rb') as f:
    x = pickle.load(f)
    print(x)