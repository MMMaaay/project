import os
import os.path
import re
import csv
import codecs
from itertools import chain
import string
import collections
import argparse
import random
import sys
import math

def dot(v1, v2):
    if len(v1) < len(v2):
        return dot(v2, v1)
    else:
        return sum([v1.get(f, 0) * v for f, v in v2.items()])

def increment(v1, v2, scale):
    for f, v in v2.items():
        v1[f] = v1.get(f, 0) + scale * v

def predict(weights, feat):
    return -1. / (1 + math.exp(-dot(weights, feat)))

def verbose_predict(feat, weights, label, fout):
    y_hat = 1 if dot(weights, feat) > 0 else 0
    correct = y_hat == label
    fout.write('label={}, predicted={}, {}\n'.format(label, y_hat, 'correct' if correct else 'wrong'))
    for f, v in sorted(list(feat.items()), key=lambda x: x[1] * weights.get(x[0], 0), reverse=True):
        w = weights.get(f, 0)
        fout.write('f={}, v={}, w={}, v*w={}\n'.format(f, v, w, v * w))
    return y_hat

def evaluate_predictor(examples, predictor):
    return sum([predictor(feat) != label for feat, label in examples]) / float(len(examples))

def learn_predictor(train_examples, valid_examples, learning_rate, num_epochs):
    weights = {}
    for n in range(num_epochs):
        random.shuffle(train_examples)
        for feat, label in train_examples:
            scale = (label - predict(weights, feat)) * learning_rate
            increment(weights, feat, scale)
        predictor = lambda x : 1 if dot(weights, x) > 0 else 0
        train_err = evaluate_predictor(train_examples, predictor)
        valid_err = evaluate_predictor(valid_examples, predictor)
        print('epoch={} train_err={} valid_err={}'.format(n, train_err, valid_err))
    return weights

train_examples = []
valid_examples = []
with open('train.csv', 'r',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    cnt = 0
    for row in f_csv:
        t = []
        ex = {}
        ex['age'] = int(row[0])
        ex['sex'] = int(row[1])
        ex['cp'] = int(row[2])
        ex['trestbps'] = int(row[3])
        ex['chol'] = int(row[4])
        ex['fbs'] = int(row[5])
        ex['restecg'] = int(row[6])
        ex['thalach'] = int(row[7])
        ex['exang'] = int(row[8])
        ex['oldpeak'] = float(row[9])
        ex['slope'] = int(row[10])
        ex['ca'] = int(row[11])
        ex['thal'] = int(row[12])
        t.append(ex)
        t.append(int(row[13]))
        train_examples.append(t)
with open('dev.csv', 'r',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    cnt = 0
    for row in f_csv:
        t = []
        ex = {}
        ex['age'] = int(row[0])
        ex['sex'] = int(row[1])
        ex['cp'] = int(row[2])
        ex['trestbps'] = int(row[3])
        ex['chol'] = int(row[4])
        ex['fbs'] = int(row[5])
        ex['restecg'] = int(row[6])
        ex['thalach'] = int(row[7])
        ex['exang'] = int(row[8])
        ex['oldpeak'] = float(row[9])
        ex['slope'] = int(row[10])
        ex['ca'] = int(row[11])
        ex['thal'] = int(row[12])
        t.append(ex)
        t.append(int(row[13]))
        valid_examples.append(t)
weights = learn_predictor(train_examples, valid_examples, 0.01, 10)

def evaluate_predictor(examples):
    cnt = 0
    for feat, label in examples:
        x = dot(weights, feat)
        res = 0
        if (x>0):
            res = 1
        if (res==label):
            cnt = cnt + 1
    return cnt / float(len(examples))
predictor = lambda ex: 1 if dot(weights, feature_extractor(ex)) > 0 else 0
valid_err = evaluate_predictor(valid_examples)
print(valid_err)