# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:36:42 2023

@author: Erfan Dehghan
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

metaInformation = yf.Ticker("Meta")
metaDataframe = metaInformation.history(period = "10y")
metaDataframe.to_csv("metaData.CSV")
#print(metaDataframe)
metaNullNumber = metaDataframe["Close"].isna().sum()
print(f"metaData close-price culomn has {metaNullNumber} null values")
metaDuplicateNumber = metaDataframe.duplicated().sum()
print(f"metaDataFrame has {metaDuplicateNumber} duplicated rows")

def metaNormalization(metaDataframe):
    metaNormalData = (metaDataframe["Close"] - metaDataframe["Close"].mean())/np.std(metaDataframe["Close"])
    plt.plot(metaNormalData - metaNormalData.shift(1))
    plt.title("meta close price normalized data")
    plt.show()
metaNormalization(metaDataframe)

def metaPlot(metaDataframe):
    plt.plot(metaDataframe['Close'])
    plt.title("meta close-price per time chart")
    plt.xlabel('time')
    plt.ylabel('close price')
    plt.show()
metaPlot(metaDataframe)
    
def metaStatistics(metaDataframe):
    mean = metaDataframe['Close'].mean()
    median = metaDataframe['Close'].median()   
    mode = metaDataframe['Close'].mode()
    variance = metaDataframe['Close'].var()
    print("meta close-price mean:", mean)
    print("meta close-price median:", median)
    print("meta close-price mode:", mode)
    print("meta close-price variance:", variance)
metaStatistics(metaDataframe)

print(metaDataframe["Close"].describe())

def metaCorr(metaDataframe):
    new = metaDataframe[metaDataframe.columns.drop(['Dividends'])]
    new = new[new.columns.drop(['Volume'])]
    metaCorrMatrix = new.corr(method='pearson')
    plt.figure(figsize=(10, 8))
    plt.imshow(metaCorrMatrix, cmap='coolwarm', interpolation='nearest')
    plt.title('meta cross-correlation matrix')
    plt.xticks(range(len(metaCorrMatrix.columns)), metaCorrMatrix.columns, rotation=90)
    plt.yticks(range(len(metaCorrMatrix.columns)), metaCorrMatrix.columns)
    plt.colorbar()
    plt.show()
metaCorr(metaDataframe)

def metaEMAPlot(metaDataframe):
    plt.plot(metaDataframe['Close'])
    plt.plot(metaDataframe['Close'].ewm(span=30, adjust=False).mean(), color="r")
    plt.plot(metaDataframe['Close'].ewm(span=90, adjust=False).mean(), color="g", linestyle="--")
    A, B = (np.polyfit(metaDataframe.reset_index().index, metaDataframe.Close, 1))
    plt.plot(np.array(metaDataframe.index), np.array(A*metaDataframe.reset_index().index + B))
    plt.title("meta EMA close-price per time chart")
    plt.xlabel('time')
    plt.ylabel('close price')
    plt.legend(["real data", "monthly EMA ind.", "seasonly EMA ind.", "trendLine"])
    plt.show()
metaEMAPlot(metaDataframe)

def metaSeason(metaDataframe):
    metaDataframe['month'] = metaDataframe.index.month
    metaDataframe['year'] = metaDataframe.index.year
    average_price = metaDataframe.groupby(['year', 'month'])['Close'].mean()
    average_price = average_price.unstack()
    average_price.plot(figsize=(15,8))
    plt.title('seasonality analysis of meta close prices')
    plt.xlabel('year')
    plt.ylabel('average close price')
    plt.legend(title='month',loc="upper right")
    plt.show()
metaSeason(metaDataframe)


#####################################################################
goldInformation = yf.Ticker("Gold")
goldDataframe = (goldInformation.history(period = "10y"))
goldDataframe.to_csv("goldData.CSV")
#print(goldDataframe)
goldNullNumber = goldDataframe["Close"].isna().sum()
print(f"goldData close-price culomn has {goldNullNumber} null values")
goldDuplicateNumber = goldDataframe.duplicated().sum()
print(f"goldDataFrame has {goldDuplicateNumber} duplicated rows")

def goldNormalization(goldDataframe):
    goldNormalData = (goldDataframe["Close"] - goldDataframe["Close"].mean())/np.std(goldDataframe["Close"])
    plt.plot(goldNormalData - goldNormalData.shift(1))
    plt.title("gold close price normalized data")
    plt.show()
goldNormalization(goldDataframe)


def goldPlot(goldDataframe):
    plt.plot(goldDataframe['Close'])
    plt.title("gold close-price per time chart")
    plt.xlabel('time')
    plt.ylabel('close price')
    plt.show()
goldPlot(goldDataframe)

def goldStatistics(goldDataframe):
    mean = goldDataframe['Close'].mean()
    median = goldDataframe['Close'].median()   
    mode = goldDataframe['Close'].mode()
    variance = goldDataframe['Close'].var()
    print("gold close-price mean:", mean)
    print("gold close-price median:", median)
    print("gold close-price mode:", mode)
    print("gold close-price variance:", variance)
goldStatistics(goldDataframe)

print(goldDataframe["Close"].describe())

def goldCorr(goldDataframe):
    new = goldDataframe[goldDataframe.columns.drop(['Dividends'])]
    new = new[new.columns.drop(['Volume'])]
    goldCorrMatrix = new.corr(method='pearson')
    plt.figure(figsize=(10, 8))
    plt.imshow(goldCorrMatrix, cmap='coolwarm', interpolation='nearest')
    plt.title('gold cross-correlation matrix')
    plt.xticks(range(len(goldCorrMatrix.columns)), goldCorrMatrix.columns, rotation=90)
    plt.yticks(range(len(goldCorrMatrix.columns)), goldCorrMatrix.columns)
    plt.colorbar()
    plt.show()
goldCorr(goldDataframe)

def goldEMAPlot(goldDataframe):
    plt.plot(goldDataframe['Close'])
    plt.plot(goldDataframe['Close'].ewm(span=30, adjust=False).mean(), color="r")
    plt.plot(goldDataframe['Close'].ewm(span=90, adjust=False).mean(), color="g", linestyle="--")
    A, B = (np.polyfit(goldDataframe.reset_index().index, goldDataframe.Close, 1))
    plt.plot(np.array(goldDataframe.index), np.array(A*goldDataframe.reset_index().index + B))
    plt.title("gold EMA close-price per time chart")
    plt.xlabel('time')
    plt.ylabel('close price')
    plt.legend(["real data", "monthly EMA ind.", "seasonly EMA ind.", "trendLine"])
    plt.show()
goldEMAPlot(goldDataframe)

def goldSeason(goldDataframe):
    goldDataframe['month'] = goldDataframe.index.month
    goldDataframe['year'] = goldDataframe.index.year
    average_price = goldDataframe.groupby(['year', 'month'])['Close'].mean()
    average_price = average_price.unstack()
    average_price.plot(figsize=(15,8))
    plt.title('seasonality analysis of gold close prices')
    plt.xlabel('year')
    plt.ylabel('average close price')
    plt.legend(title='month',loc="upper right")
    plt.show()
goldSeason(goldDataframe)
