import re
import time
import md5
from selenium import webdriver
from selenium.webdriver.common.by import By
class Posts(object):
    def __init__(self):
        self.title = []
        self.author = []
        self.comments = []
        self.timestamp = []
        self.hash_title_author = {}
        self.hash_author = {}
    def addPost(self, title, author, comments):
        hash_t_a = md5.new(title+author).digest()
        if hash_t_a in self.hash_title_author:
            print 'Duplicated title & author found'
            title = title+'(dup)'
            hash_t_a = md5.new(title+author).digest()
        self.title.append(title)
        self.author.append(author)
        self.comments.append(int(re.search('[0-9]*',comments)))
        self.timestamp.append(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
        self.hash_title_author[hash_t_a] = len(title)-1
        if author in hash_author:
            self.hash_author[author].append(len(title)-1)
        else:
            self.hash_author[author] = [len(title)-1]
    def save(self):
        with open('log.txt', 'w') as f:
            f.write(str(len(title))+'\n')
            #f.write('title\n')
            for i in self.title:
                f.write(i+'\n')
            #f.write('author\n')
            for i in self.author:
                f.write(i+'\n')
            #f.write('comments\n')
            for i in self.comments:
                f.write(str(i)+'\n')
            #f.write('timestamp')
            for i in self.timestamp:
                f.write(i+'\n')
            #f.write('hash_title_author\n')
            for key, value in self.hash_title_author.iteritems():
                f.write(key+':'+str(value))
            #f.write('hash_author\n')
            for key, value in self.hash_author.iteritems():
                f.write(key+':'+str(value))
    def load(self):
        with open('log.txt', 'r') as f:
            records = int(f.readline().replace('\n', ''))
            self.title = []
            for i in xrange(records):
                self.title.append(f.readline().strip('\n'))
            self.author = []
            for i in xrange(records):
                self.author.append(f.readline().strip('\n'))
            self.comments = []
            for i in xrange(records):
                self.comments.append(int(f.readline().strip('\n')))
            self.timestamp = []
            for i in xrange(records):
                self.timestamp.append(f.readline().strip('\n'))
            self.hash_title_author = {}
            for i in xrange(records):
                key, value = re.split(':', f.readline().strip('\n'))
                self.hash_title_author[key] = int(value)
            self.hash_author = {}
            for i in xrange(records):
                key, value = re.split(':', f.readline().strip('\n'))
                self.hash_author[key] = int(value)
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
