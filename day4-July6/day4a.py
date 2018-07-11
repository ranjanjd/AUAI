{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# AUAI -Day4a Machine Learning Demos\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sklearn\n",
    "import numpy as np\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn import datasets\n",
    "import time\n",
    "iris = datasets.load_iris()\n",
    "X = iris.data[:, :4]  # we only take the first two features.\n",
    "y = iris.target\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.333)\n",
    "#print(len(X_train), len(X_test))\n",
    "def print_accuracy(f):\n",
    "    print(\"Accuracy = {0}%\".format(100*np.sum(f(X_test) == y_test)/len(y_test)))\n",
    "    time.sleep(0.5) # to let the print get out before any progress bars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy = 96.0%\n"
     ]
    }
   ],
   "source": [
    "#KNN: k-nearest neighbors\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "knn = KNeighborsClassifier()\n",
    "knn.fit(X_train, y_train)\n",
    "print_accuracy(knn.predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy = 98.0%\n"
     ]
    }
   ],
   "source": [
    "#SVM: Support vector machine with a linear kernel\n",
    "from sklearn.svm import SVC\n",
    "svc_linear = SVC(kernel='linear', probability=True)\n",
    "svc_linear.fit(X_train, y_train)\n",
    "print_accuracy(svc_linear.predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy = 92.0%\n"
     ]
    }
   ],
   "source": [
    "#DT: Decision tree\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "linear_lr = LogisticRegression()\n",
    "linear_lr.fit(X_train, y_train)\n",
    "print_accuracy(linear_lr.predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy = 94.0%\n"
     ]
    }
   ],
   "source": [
    "#RF: Random forest\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "rforest = RandomForestClassifier(n_estimators=100, max_depth=None, min_samples_split=2, random_state=0)\n",
    "rforest.fit(X_train, y_train)\n",
    "print_accuracy(rforest.predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy = 96.0%\n"
     ]
    }
   ],
   "source": [
    "#NN: Neural network (MLP)\n",
    "from sklearn.neural_network import MLPClassifier\n",
    "nn = MLPClassifier(solver='lbfgs', alpha=1e-1, hidden_layer_sizes=(5, 2), random_state=0)\n",
    "nn.fit(X_train, y_train)\n",
    "print_accuracy(nn.predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
