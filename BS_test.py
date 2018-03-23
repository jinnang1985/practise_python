#example from freecodecamp.org 

class Scraper_BS:

#import libraries
  import urllib2
  from bs4 import BeautifulSoup

  elem_id = 0
  lobby_addr = []
  new_dict={}
  #specify the url
  prefix = "www.etuovi.com"
  main_page = 'https://www.etuovi.com/myytavat-asunnot/tulokset?haku=M1235650663&rd=50'
  nextfix = 'https://www.etuovi.com/myytavat-asunnot'

  def scrape(self):

    while True:

      #query website and return the html to variable page
      print(self.main_page)
      page = self.urllib2.urlopen(self.main_page)

      #parse the page into BeautifulSoup
      soup = self.BeautifulSoup(page, 'html.parser')
      print type(soup)

      result_box = soup.find_all('section', attrs={'class':'results list'})
      print type(result_box)

      #print(result_box)
      for elem in result_box:
        house_box = elem.find_all('li', attrs={'class':'residental'})
        print type(house_box)
      #print (house_box)
        for elem2 in house_box:
          address_box = elem2.find('div', attrs={'class':'address'})
          address = address_box.find('strong')
          area    = address_box.find('span')
          retr_link = elem2.a["href"]
          refn_link = retr_link.replace("..", "")
          refn_link = self.prefix + refn_link
          size_box = elem2.find('div', attrs={'class':'size'})
          size     = size_box.span.string
          price_box = elem2.find('div', attrs={'class':'price'})
          price     = price_box.span.string
          year_box = elem2.find('div', attrs={'class':'year'})
          if year_box.span == None :
            year = "9999"
          else :
            year = year_box.span.string

          self.elem_id += 1
          case    = {'id':self.elem_id, 'address':address.string, 'area':area.string, 'link':refn_link, 'price':price, 'size':size, 'year':year}
          self.lobby_addr.append(case)

#for elem in result_box:
      nextpage = result_box[0].find('li', attrs={'class':'next'})
      if nextpage.em == None:
        nextlink = nextpage.a['href']
        nextlink = nextlink.replace('.', '')
        self.main_page= self.nextfix + nextlink
        # main_page.format()
      else:
        break

    ################################
    ##organize list
    for di in self.lobby_addr:
      self.new_dict[di['id']]={}
      for k in di.keys():
        if k =='id': continue
        self.new_dict[di['id']][k]=di[k]

    ###############################
## find specific
  def export(self):

    print(self.new_dict.keys())

    import os, csv
    os.chdir("/home/jinnang/ENV/bin")
    with open("lobbying.csv", "w") as toWrite:
      writer = csv.writer(toWrite, delimiter=",")
      writer.writerow(["name", "link", "price", "size", "year"])
      for a in self.new_dict.keys():
        writer.writerow([self.new_dict[a]["address"].encode("utf-8"), self.new_dict[a]["link"].encode("utf-8"), self.new_dict[a]["price"].encode("utf-8"), self.new_dict[a]["size"].encode("utf-8"),self.new_dict[a]["year"].encode("utf-8")])

###################################################


myclass = Scraper_BS()
myclass.scrape()
myclass.export()

