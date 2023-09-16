from django.test import TestCase
# from pyspark import SparkConf, SparkContext

# Create your tests here.
import requests 

bok = requests.get('https://www.gutenberg.org/cache/epub/28885/pg28885.txt').text
# fil = open('./alice.txt','w')
# fil.write(bok)
# fil.close()
type(bok)
