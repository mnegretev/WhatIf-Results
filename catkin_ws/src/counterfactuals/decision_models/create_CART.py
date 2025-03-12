import sys
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
#from sklearn.neural_network import MLPClassifier
import pickle
import time
import statistics

def main(input_subdir, output_subdir):
    print("input_subdir received:", input_subdir, flush=True)
    print("output_subdir received:", output_subdir, flush=True)    
        
    model = DecisionTreeClassifier(max_depth=6)

    print("Fold 10: ", flush = True)    
    # Load data files
    data = pd.read_csv("train_fold_10.csv")
    data.drop(columns=["latent_collision"], inplace=True)        
    X_train = data.drop(['action'], axis = 1)
    y_train = data['action']
        
    print("X_train.head ", X_train.head(), flush = True)
    print("X_train.info ", X_train.info(), flush = True)
    print("X_train.describe ", X_train.describe(), flush = True)
    print("X_train ", X_train.shape, flush = True)          

    model.fit(X_train, y_train) 

    filename = output_subdir + "CART_10.cart"
    pickle.dump(model, open(filename, 'wb'))  
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 create_CART.py <input_subdir> <output_subdir>")
        sys.exit(1)
    input_subdir = sys.argv[1]
    output_subdir = sys.argv[2]    
    main(input_subdir, output_subdir)


