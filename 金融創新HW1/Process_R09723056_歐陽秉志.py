{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from scipy import stats\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from tqdm import tqdm\n",
    "import mplfinance as mpf\n",
    "import time\n",
    "import matplotlib as mlt\n",
    "from talib import abstract\n",
    "from datetime import datetime\n",
    "\n",
    "def percentile(series):\n",
    "        t = series.iloc[-1]\n",
    "        p = stats.percentileofscore(series, t, kind='strict')    \n",
    "        return p\n",
    "\n",
    "\n",
    "def trending(series):\n",
    "    y = series.values.reshape(-1,1)\n",
    "    x = np.array(range(1, series.shape[0] + 1)).reshape(-1,1)\n",
    "    \n",
    "    lm = LinearRegression()\n",
    "    lm.fit(x,y)\n",
    "    \n",
    "    if lm.coef_ > 0:\n",
    "        return 1\n",
    "    elif lm.coef_ == 0:\n",
    "        return 0\n",
    "    else:\n",
    "        return -1\n",
    "\n",
    "\n",
    "def dataprocess(df):\n",
    "    tall = df['Open'].combine(df['Close'],np.maximum)\n",
    "    short = df['Close'].combine(df['Open'],np.minimum)\n",
    "\n",
    "\n",
    "    df['Upper_shadow'] = df['High']-tall\n",
    "    df['Lower_shadow'] = short-df['Low']\n",
    "    df['Realbody'] = df['Close']-df['Open']\n",
    "    df['Direction'] = np.sign(df['Realbody'])\n",
    "    \n",
    "    df['Upper_per'] = df['Upper_shadow'].rolling(50).apply(percentile, raw=False)\n",
    "    df['Lower_per'] = df['Lower_shadow'].rolling(50).apply(percentile, raw=False)\n",
    "    df['Realbody_per'] = df['Realbody'].rolling(50).apply(percentile, raw=False)\n",
    "    \n",
    "    df['Trend7'] = df['Close'].rolling(7).apply(trending, raw=False)\n",
    "    df['Trend8'] = df['Close'].rolling(8).apply(trending, raw=False)\n",
    "    df['Trend9'] = df['Close'].rolling(9).apply(trending, raw=False)\n",
    "    \n",
    "    print(df[100:110])\n",
    "    \n",
    "    df['Eveningstar'] = 0\n",
    "    df['Bullishengulfing'] = 0\n",
    "    df['None'] = 0\n",
    "    \n",
    "    return df\n"
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
