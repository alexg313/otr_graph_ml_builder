import unittest
from grapher import ObjectTree
import pandas as pd
import cv2

df_path = '/Users/ap/Documents/OTR/git/Graph-Convolution-on-Structured-Documents/data/object_map.csv'
img_path = '/Users/ap/Documents/OTR/git/Graph-Convolution-on-Structured-Documents/data/deskew.jpg'


# validation dataframe
df_val = pd.read_csv(df_path)
df_val = df_val[['xmin', 'ymin', 'xmax', 'ymax', 'Object', 'label']]

img_val = cv2.imread(img_path, 0)


class ObjectTree_readTest(unittest.TestCase):
    def test_empty(self):

        # test dataframe
        df = pd.read_csv(df_path)
        img = cv2.imread(img_path, 0)

        # test
        c = ObjectTree(label_column='label')
        c.read(df, img)
        df, img = c.df, c.img

        self.assertSequenceEqual(list(df.columns), list(df_val.columns))
