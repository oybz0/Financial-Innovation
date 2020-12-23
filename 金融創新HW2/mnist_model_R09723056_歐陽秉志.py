{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "469/469 [==============================] - 70s 150ms/step - loss: 0.4405 - accuracy: 0.8533 - val_loss: 0.1541 - val_accuracy: 0.9519\n",
      "LSTM test accuracy: 0.9519000053405762\n",
      "WARNING:tensorflow:From <ipython-input-1-f40c502246f3>:67: Sequential.predict_classes (from tensorflow.python.keras.engine.sequential) is deprecated and will be removed after 2021-01-01.\n",
      "Instructions for updating:\n",
      "Please use instead:* `np.argmax(model.predict(x), axis=-1)`,   if your model does multi-class classification   (e.g. if it uses a `softmax` last-layer activation).* `(model.predict(x) > 0.5).astype(\"int32\")`,   if your model does binary classification   (e.g. if it uses a `sigmoid` last-layer activation).\n",
      "[[5811    1    9    3    8    8   30    7   27   19]\n",
      " [   2 6610   53    7    6    7    9   14   23   11]\n",
      " [  33   18 5788   21   22    6    9   28   25    8]\n",
      " [  16   12  138 5751    1   66    2   29  105   11]\n",
      " [  14    7   17    1 5565    6   58   33   31  110]\n",
      " [  62   11   22   30   14 5102  114   20   40    6]\n",
      " [  29    4    5    1   34   17 5820    0    7    1]\n",
      " [   9   15   89   40   11    1    0 6040   21   39]\n",
      " [  42   31   37   87   16  129   27    3 5465   14]\n",
      " [  81    8    2   40  136   56    6  195  183 5242]] \n",
      "\n",
      " [[ 967    1    1    0    1    3    3    2    1    1]\n",
      " [   0 1118    6    0    0    3    2    1    5    0]\n",
      " [   5    1 1006    3    4    2    4    5    2    0]\n",
      " [   0    1   21  959    0    9    0    6   11    3]\n",
      " [   3    2    1    0  926    0   14    4    8   24]\n",
      " [  10    0    2   11    2  847   15    2    3    0]\n",
      " [   7    2    0    0    9    5  933    0    2    0]\n",
      " [   0    5   20   15    0    0    0  975    7    6]\n",
      " [  15    1    4   21    3   33    4    0  892    1]\n",
      " [   9    4    0    5   20    9    2   23   41  896]]\n",
      "Model: \"sequential_1\"\n",
      "_________________________________________________________________\n",
      "Layer (type)                 Output Shape              Param #   \n",
      "=================================================================\n",
      "conv2d (Conv2D)              (None, 28, 28, 16)        416       \n",
      "_________________________________________________________________\n",
      "max_pooling2d (MaxPooling2D) (None, 14, 14, 16)        0         \n",
      "_________________________________________________________________\n",
      "conv2d_1 (Conv2D)            (None, 14, 14, 36)        14436     \n",
      "_________________________________________________________________\n",
      "max_pooling2d_1 (MaxPooling2 (None, 7, 7, 36)          0         \n",
      "_________________________________________________________________\n",
      "dropout (Dropout)            (None, 7, 7, 36)          0         \n",
      "_________________________________________________________________\n",
      "flatten (Flatten)            (None, 1764)              0         \n",
      "_________________________________________________________________\n",
      "dense_1 (Dense)              (None, 256)               451840    \n",
      "_________________________________________________________________\n",
      "dropout_1 (Dropout)          (None, 256)               0         \n",
      "_________________________________________________________________\n",
      "dense_2 (Dense)              (None, 10)                2570      \n",
      "=================================================================\n",
      "Total params: 469,262\n",
      "Trainable params: 469,262\n",
      "Non-trainable params: 0\n",
      "_________________________________________________________________\n",
      "938/938 [==============================] - 60s 64ms/step - loss: 0.1959 - accuracy: 0.9384 - val_loss: 0.0439 - val_accuracy: 0.9856\n",
      "CNN test accuracy: 0.9855999946594238\n",
      "[[5875    1    8    1    1    2   13    0   16    6]\n",
      " [   1 6656   22   13    5    2    3   13   25    2]\n",
      " [   2    6 5846   44    3    0    1   28   24    4]\n",
      " [   1    0    8 6070    0   13    0   18   15    6]\n",
      " [   3    9    7    0 5776    0   13    3    7   24]\n",
      " [   1    0    3   26    0 5360   10    0   19    2]\n",
      " [  10    6    3    2    2   16 5849    0   30    0]\n",
      " [   1    7   13    7   10    0    0 6192   12   23]\n",
      " [   1   10   12   14   11   17    2    5 5764   15]\n",
      " [   8    6    0   30   21   19    1   25   25 5814]] \n",
      "\n",
      " [[ 972    0    1    0    0    0    3    1    3    0]\n",
      " [   0 1125    0    4    0    0    1    1    4    0]\n",
      " [   0    1 1016    6    0    0    0    7    2    0]\n",
      " [   0    0    3 1000    0    2    0    3    2    0]\n",
      " [   0    0    2    0  968    0    4    1    2    5]\n",
      " [   1    0    0    8    0  882    1    0    0    0]\n",
      " [   4    3    0    1    1    5  940    0    4    0]\n",
      " [   0    1    5    1    0    0    0 1014    2    5]\n",
      " [   2    0    1    2    2    2    0    2  962    1]\n",
      " [   2    3    0    5    8    5    0    4    5  977]]\n"
     ]
    }
   ],
   "source": [
    "import keras\n",
    "from keras.models import Sequential, load_model\n",
    "from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D, Activation\n",
    "from keras.layers import LSTM\n",
    "from keras.utils import np_utils\n",
    "from keras.datasets import mnist\n",
    "from keras.optimizers import Adam\n",
    "import pandas as pd\n",
    "from sklearn.metrics import confusion_matrix\n",
    "\n",
    "def CNN_dataprocess(x_train, x_test, y_train, y_test):\n",
    "    #reshape the mnist data\n",
    "    x_train = x_train.reshape(-1, 28, 28, 1)/255\n",
    "    x_test = x_test.reshape(-1, 28, 28, 1)/255\n",
    "    x_train = x_train.astype('float32')\n",
    "    x_test = x_test.astype('float32')\n",
    "    y_train = np_utils.to_categorical(y_train)\n",
    "    y_test = np_utils.to_categorical(y_test)\n",
    "    return (x_train, x_test, y_train, y_test)\n",
    "\n",
    "def LSTM_dataprocess(x_train, x_test, y_train, y_test, n_step, n_input, n_classes):\n",
    "    #reshape the mnist data\n",
    "    x_train = x_train.reshape(-1, n_step, n_input)\n",
    "    x_test = x_test.reshape(-1, n_step, n_input)\n",
    "    x_train = x_train.astype('float32')/255\n",
    "    x_test = x_test.astype('float32')/255\n",
    "    \n",
    "    y_train = keras.utils.to_categorical(y_train, n_classes)\n",
    "    y_test = keras.utils.to_categorical(y_test, n_classes)\n",
    "    return (x_train, x_test, y_train, y_test)\n",
    "\n",
    "def CNN_model():\n",
    "    #build the model\n",
    "    model = Sequential()\n",
    "    #Layer 1\n",
    "    model.add(Conv2D(filters=16,kernel_size=(5,5),padding='same',input_shape=(28,28,1),activation='relu'))  \n",
    "    #Max-Pool 1\n",
    "    model.add(MaxPool2D(pool_size=(2,2)))\n",
    "    #Layer 2\n",
    "    model.add(Conv2D(filters=36,kernel_size=(5,5),padding='same',input_shape=(28,28,1),activation='relu'))  \n",
    "    #Max-Pool 2\n",
    "    model.add(MaxPool2D(pool_size=(2,2)))\n",
    "    #Add dropout layer\n",
    "    model.add(Dropout(0.25))  \n",
    "    model.add(Flatten())\n",
    "    model.add(Dense(256, activation='relu'))\n",
    "    model.add(Dropout(0.5))\n",
    "    model.add(Dense(10, activation='softmax'))\n",
    "    model.summary()\n",
    "    return model\n",
    "\n",
    "def LSTM_model(n_input, n_step, n_hidden, n_classes):\n",
    "    #build the model\n",
    "    model = Sequential()\n",
    "    model.add(LSTM(n_hidden, batch_input_shape=(None, n_step, n_input), unroll=True))\n",
    "    model.add(Dense(n_classes))\n",
    "    model.add(Activation('softmax'))\n",
    "    return model\n",
    "\n",
    "def train(model, x_train, y_train, x_test, y_test, learning_rate, epochs, batch_size):\n",
    "    adam = Adam(lr=learning_rate)\n",
    "    model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])\n",
    "    model.fit(x_train, y_train,batch_size=batch_size, epochs=epochs,verbose=1, validation_data=(x_test, y_test))\n",
    "\n",
    "def result(x_train, x_test, y_train, y_test, model):\n",
    "    #Get prediction y, both train and test\n",
    "    train_pred = model.predict_classes(x_train)\n",
    "    test_pred = model.predict_classes(x_test)\n",
    "    \n",
    "    #Get true y, both train and test\n",
    "    train_label = y_train\n",
    "    test_label =  y_test\n",
    "    \n",
    "    #Confusion matrix\n",
    "    train_result_cm = confusion_matrix(train_label, train_pred, labels=range(10))\n",
    "    test_result_cm = confusion_matrix(test_label, test_pred, labels=range(10))\n",
    "    print(train_result_cm, '\\n'*2, test_result_cm)\n",
    "\n",
    "\n",
    "def mnist_cnn_main():\n",
    "    # training parameters\n",
    "    learning_rate = 0.001\n",
    "    epochs = 1\n",
    "    batch_size = 64\n",
    "    \n",
    "    (x_train, y_train), (x_test, y_test) = mnist.load_data()\n",
    "    x_train, x_test, y_train_1, y_test_1 = CNN_dataprocess(x_train, x_test, y_train, y_test)\n",
    "\n",
    "    model = CNN_model()\n",
    "    train(model, x_train, y_train_1, x_test, y_test_1, learning_rate, epochs, batch_size)\n",
    "    scores = model.evaluate(x_test, y_test_1, verbose=0)\n",
    "    print('CNN test accuracy:', scores[1])\n",
    "    result(x_train, x_test, y_train, y_test, model)\n",
    "\n",
    "def mnist_lstm_main():\n",
    "    # training parameters\n",
    "    learning_rate = 0.001\n",
    "    epochs = 1\n",
    "    batch_size = 128\n",
    "\n",
    "    # model parameters\n",
    "    n_input = 28\n",
    "    n_step = 28\n",
    "    n_hidden = 256\n",
    "    n_classes = 10\n",
    "\n",
    "    (x_train, y_train), (x_test, y_test) = mnist.load_data()\n",
    "    x_train, x_test, y_train_1, y_test_1 = LSTM_dataprocess(x_train, x_test, y_train, y_test, n_step, n_input, n_classes)\n",
    "\n",
    "    model = LSTM_model(n_input, n_step, n_hidden, n_classes)\n",
    "    train(model, x_train, y_train_1, x_test, y_test_1, learning_rate, epochs, batch_size)\n",
    "    scores = model.evaluate(x_test, y_test_1, verbose=0)\n",
    "    print('LSTM test accuracy:', scores[1])\n",
    "    result(x_train, x_test, y_train, y_test, model)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    mnist_lstm_main()\n",
    "    \n",
    "    mnist_cnn_main()"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
