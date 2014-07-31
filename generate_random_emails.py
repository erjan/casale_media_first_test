import random, string


# generate millions of email domains and output them by date they were added in database
#
#
#
#NOT COMPLETE!
#

#data for generating random email 
domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
alphabet = string.ascii_lowercase
lastnames = ["jack", "john", "mike" ,"myers", "obama","mayor",
             "nixon","virginia", "super", "fly",
             "neo", "liddel", "colonnel", "myles",
             "osman", "baiuly", "signak", "algazi", "ostinpowers"]

firstnames = ["tlc", "london", "keyes", "ava", "lisa", "ann", "brandi", "love", "cassadi", "karmen"]
#data for generating random dates
years = [2001, 1976]
days = [ day for day in range(1,32)]
months = ["august" ,  "october", "june", "july", "september"]


def generate_random_date():    
        random_year = random.choice(years)
        random_day = random.choice(days)
        random_month = random.choice(months)
        #print( ''.join(str(random_day) + " "+ random_month + " "+ str(random_year)))
        return ( ''.join(str(random_day) + " "+ random_month + " "+ str(random_year)))
        
def get_one_random_domain(domains):
        return random.choice(domains)

def get_2_random_chars(alphabet):
    chars = ''
    return ''.join(chars + random.choice(alphabet) for i in range(2))    

def get_random_firstname():
        return random.choice(firstnames)

def get_random_lastname():
        return random.choice(lastnames)

email_date_table = []
date_for_emails_dict = {}
def mailing_table(length):
        
        for i in range(length):
                email = generate_random_email() 
                date = generate_random_date()
                email_date_table.append( [email, date] )                    

def emails_by_date(pairs):
    ret = {}
    for email, date in pairs:
        ret.setdefault(date, []).append(email)
    return ret

def generate_random_email():
            
         one_domain = str(get_one_random_domain(domains))
         lastname = str(get_random_lastname())
         name_or_chars = random.choice([1,2])
         
         if name_or_chars == 1:
                 firstname = str(get_random_firstname())        
                 return (firstname  + "_" + lastname + "@" + one_domain)
         elif name_or_chars == 2:
                 two_chars = str(get_2_random_chars(alphabet))                         
                 return (two_chars  + "_" + lastname + "@" + one_domain)
                
def print_email_date_dict(dictu):
        for key in dictu.keys():
            print(key + " : ")
            print( *dictu[key], sep = '\n')
            print()

def main():
            
    mailing_table(14000)
    dictu = emails_by_date(email_date_table)
    print_email_date_dict(dictu)
    
        
        
        
