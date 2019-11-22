import requests

def main():
#Q1 & Q2  
  printPageInfo("http://icarus.cs.weber.edu/~dweidman/CS2705HTMLLab.html")
#Q3 & Q4
  printPageInfo("http://icarus.cs.weber.edu/~dweidman/CS2705HTMLLab2.html")
  
# Q5 – What is difference between the HEAD command and the GET command?
#   The HEAD command only retrieves information contained the website's HTML head tag
#   (meta data, title, etc). However, the GET command get all information available 
#   from the website.

# Q6 – Why do you think the HEAD command tells you the Content-Type?
#   I can see the HEAD command being used to check basic information; knowing
#   the content type could be a useful overview of a webpage.

# Q7 - What differences did you notice between the two web pages?
#   Different date modifieds, different content lengths, different html code,
#   different etags.

####################################################
# Gets and prints the info for the specified webpage
####################################################
def printPageInfo(address):
    dashBar = "{:-^70}"
    print(("\n{: ^50}\n" + dashBar).format("Info for " + address, '-'))

    r = requests.get(address)
# Status code
    print("Status code is:", r.status_code, "\n")
# Complete header
    print("Headers of the website are:", r.headers, "\n")    
# Content encoding
    print("Content encoding:", r.headers['Content-Encoding'],"\n")
# Length of the content of the heading
    print("Content length:", r.headers['Content-Length'], "\n")
# Date the page was last modified
    print("Last modified date:", r.headers['Last-Modified'], "\n")
# # Current date
    print("Current date", r.headers['Date'])
# # Server type and version
    print("Server type and version:", r.headers['Server'], "\n")
# # HTML coding of the webpage
    print("HTML code of the websited is:\n", r.text, "\n")

main()