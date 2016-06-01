import re
import time
import md5
from selenium import webdriver
from selenium.webdriver.common.by import By
class Posts(object):
    def __init__(self):
        '''
        self.title = []
        self.author = []
        self.comments = []
        self.timestamp = []
        self.hash_title_author = {}
        self.hash_author = {}
        '''
        self.hash = {'title':0, 'author':1, 'comments':2, 'timestamp':3, 'hash_title_author':4, 'hash_author':5}
        self.data = [[],[],[],[],{},{}]
    def addPost(self, title, author, comments):
        hash_t_a = md5.new(title+author).digest()
        if hash_t_a in self.data[self.hash[hash_title_author]]:
            print 'Duplicated title & author found'
            title = title+'(dup)'
            hash_t_a = md5.new(title+author).digest()
        self.data[self.hash['title']].append(title)
        self.data[self.hash['author']].append(author)
        self.data[self.hash['comments']].append(re.search('[0-9]*',comments))
        self.data[self.hash['timestamp']].append(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
        self.data[self.hash['hash_title_author']][hash_t_a] = len(title)-1
        if author in hash_author:
            self.data[self.hash['hash_author']][author].append(len(title)-1)
        else:
            self.data[self.hash['hash_author']][author] = [len(title)-1]
    def save(self):
        with open('log.txt', 'w') as f:
            cata = len(self.data)
            records = len(self.data[0])
            f.write(str(records)+'\n')
            for j in self.data:
                if type(j) is list:
                    for i in list(enumerate(j)):
                        f.write(i+'\n')
                elif type(j) is dict:
                    for key, value in j.iteritems():
                        f.write(key+':'+value))

    def load(self):
        with open('log.txt', 'r') as f:
            records = int(f.readline().strip('\n'))
            for j in xrange(len(self.data)):
                if type(self.data[j]) is list:
                    for i in xrange(records):
                        self.data[j].append(f.readline().strip('\n'))
                elif type(self.data[j]) is dict:
                    for i in xrange(records):
                        key, value = re.split(':', f.readline().strip('\n'))
                        self.data[j][key] = int(value)

class Reddit(object):
    def __init__(self):
        url = 'https://www.reddit.com/r/churning/'
        self.driver = webdriver.Chrome('../chromedriver2.21')
        self.driver.get(url)
    def getElementByClassName(self, driver, n):
        try:
            return driver.find_elements(By.CLASS_NAME, n)
        except BaseException:
            print 'Load one more time...'
            time.sleep(5)
            return driver.find_elements(By.CLASS_NAME, n)
        except Exception:
            print 'No such a CLASS_NAME!'
            return None
    def getElementById(self, driver, id):
        try:
            return driver.find_element_by_id(id)
        except BaseException:
            print 'Load one more time...'
            time.sleep(5)
            return driver.find_element_by_id(id)
        except Exception:
            print 'No such an ID'
            return None
    def getList(self):
        siteTable = self.getElementById(self.driver, 'siteTable')
        sitePosts = self.getElementByClassName(self.driver, 'may-blank')
        for i in sitePosts:
            print i.text
    def done(self):
        print 'Done'
        self.driver.quit()

a = Reddit()
print a.getList()
a.done()
