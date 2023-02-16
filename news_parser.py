import newspaper
import sys

from newspaper import Article
from datetime import datetime



# source file containing xml 
source_file_path= ""


#file path to write result to
result_file_path = ""

# file mode append or write 
mode ="";

# take input from commandline
sys_arg_len = len(sys.argv)


# take in  source_file path
if (sys_arg_len >= 4) : 
    source_file_path = sys.argv[1]
    result_file_path = sys.argv[2]
    mode = sys.argv[3]
else:
    print("failed")
    exit()


#set up file
if (mode == "0"):
    f = open(result_file_path, "w")
else:
    f = open(result_file_path, "a")
    
r = open(source_file_path,"r")

doc = r.read()
print("finish read")

news_limit = 500
count = 0 
starting_pos = 0 
# count continuous network error so that we would not stuck in a while loop
continuous_error = 0 

starting_pos = doc.find("<loc>",starting_pos)
while starting_pos != -1:
    until = doc.find ("</loc>",starting_pos)
    if until == -1 :
        print("error")
        exit()

    url = ""
    for i in range(starting_pos+5,until):
        url += doc[i]
    
    if url == "":
        print("error")
        exit()

    print(url)

    #create article
    article = Article (url)

    #download, beware network error
    try:
        article.download()
    except:
        continuous_error =+1
        
        # too many continous error, drop now 
        if continuous_error == 10:
            print ("ME skippp")
            continuous_error = 0 

            #set new starting pos 
            starting_pos = until +6
            starting_pos = doc.find("<loc>",starting_pos)


        continue

    

    # Parse and NLP magic
    # print (article.html)
    try:
        article.parse()
    except:
        continuous_error +=1
        
         # too many continous error, drop now 
        if continuous_error == 10:
            print ("ME skippp")
            continuous_error = 0 

            #set new starting pos 
            starting_pos = until +6
            starting_pos = doc.find("<loc>",starting_pos)

        continue
    
    #write to file
    f.write("<news>\n")
    f.write("<pr>url: "+article.source_url+"\n")
    
    try:
        f.write("<pr>Date: "+article.publish_date.strftime('%m/%d/%Y')+"\n")
    except:
        print("This article has no date")

    f.write("<pr>title: "+article.title+"\n")
    f.write("<pr>body: "+article.text+"\n")
    f.write("</news>\n")
    
    #set new starting pos 
    starting_pos = until +6
    starting_pos = doc.find("<loc>",starting_pos)

    #count and check limit 
    count+=1
    if count >= news_limit:
        break