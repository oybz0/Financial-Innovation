{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'dataprocess' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-8b5b738e1aa2>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     37\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     38\u001b[0m \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'data.csv'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 39\u001b[0;31m \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdataprocess\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     40\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     41\u001b[0m \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msignal\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'dataprocess' is not defined"
     ]
    }
   ],
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
    "def graph(df,signal):\n",
    "    df_adj = df.iloc[:10,0:5]\n",
    "    df_adj['Date'] = pd.to_datetime(df_adj['Date'])\n",
    "    df_adj.set_index(['Date'], inplace=True)\n",
    "    mpf.plot(df_adj, type='candle', style='binance', title=signal)\n",
    "\n",
    "\n",
    "def graphresult(df):\n",
    "    for idx in tqdm(df.index):\n",
    "        start = idx-9\n",
    "        end = idx\n",
    "        if start >= 0:\n",
    "            data = df.loc[start:end]\n",
    "            if eveningstar(data):\n",
    "                graph(data,'eveningstar')\n",
    "                break\n",
    "                \n",
    "    for idx in tqdm(df.index):\n",
    "        start = idx-9\n",
    "        end = idx\n",
    "        if start >= 0:\n",
    "            data = df.loc[start:end]\n",
    "            if bullishengulfing(data):\n",
    "                graph(data,'bullishengulfing')\n",
    "                break\n",
    "\n",
    "df = pd.read_csv('data.csv')\n",
    "df = dataprocess(df)\n",
    "\n",
    "df = signal(df)\n",
    "\n",
    "counts(df)\n",
    "\n",
    "graphresult(df)"
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
