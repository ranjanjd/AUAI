{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# AUAI -Day4b Deep Learning Demos\n",
    "https://machinelearningmastery.com/multi-class-classification-tutorial-keras-deep-learning-library/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sklearn\n",
    "import numpy\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn import datasets\n",
    "\n",
    "from keras.models import Sequential\n",
    "from keras.layers import Dense\n",
    "from keras.wrappers.scikit_learn import KerasClassifier\n",
    "from keras.utils import np_utils\n",
    "from sklearn.model_selection import cross_val_score\n",
    "from sklearn.model_selection import KFold\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.pipeline import Pipeline\n",
    "\n",
    "iris = datasets.load_iris()\n",
    "X = iris.data[:, :4]  # we only take the first two features.\n",
    "y = iris.target\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.333)\n",
    "#print(len(X_train), len(X_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# fix random seed for reproducibility\n",
    "seed = 7\n",
    "numpy.random.seed(seed)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# encode class values as integers\n",
    "encoder = LabelEncoder()\n",
    "encoder.fit(y)\n",
    "encoded_y = encoder.transform(y)\n",
    "# convert integers to dummy variables (i.e. one hot encoded)\n",
    "dummy_y = np_utils.to_categorical(encoded_y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Define The Neural Network Model\n",
    "4 inputs -> [8 hidden nodes] -> 3 outputs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# define baseline model\n",
    "def baseline_model():\n",
    "\t# create model\n",
    "\tmodel = Sequential()\n",
    "\tmodel.add(Dense(8, input_dim=4, activation='relu'))\n",
    "\tmodel.add(Dense(3, activation='softmax'))\n",
    "\t# Compile model\n",
    "\tmodel.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])\n",
    "\treturn model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5, verbose=0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Evaluate The Model with k-Fold Cross Validation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "kfold = KFold(n_splits=10, shuffle=True, random_state=seed)"
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
      "Baseline: 97.33% (4.42%)\n"
     ]
    }
   ],
   "source": [
    "results = cross_val_score(estimator, X, dummy_y, cv=kfold)\n",
    "print(\"Baseline: %.2f%% (%.2f%%)\" % (results.mean()*100, results.std()*100))"
   ]
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
