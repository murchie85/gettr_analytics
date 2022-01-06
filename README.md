# Gettr Analytics
  
![](pics/head.png)  
*Image wordmap generated from Gettr Trend data*


### About
  
This is a repo with some tools for parsing out data from Gettr, currently i'm using the `gogettr` lib to pull the data, though if this depreciates it's easy enough to replicate with requests (that's what they do, as the site has public endpoints.)  


### What is Gettr
  
From what I can see its like a cancel free Twitter that is gaining in hype, hence this repo. 

**Wikipedia** Definition (take from it what you will...)

```
Gettr (stylized GETTR) is a social media platform and microblogging site founded by Jason Miller, a former Donald Trump aide. Miller said Getter is "for everyone across the political spectrum" to come together and have debates as per the First Amendment. He also stated it was designed to be "cancel-free."[5]. It was officially launched on July 4, 2021. Its user interface and feature set have been described as very similar to those of Twitter.  
```  

## Setting up client
  
Note, I use `gg`, as shorthand for the client object.  

```
from gogettr import PublicClient

# API client
gg = PublicClient()
```

## Get Trends Usage
  
The trends call returns an iterator, which I wrap into a list of Dicts (dict keys can vary).  

```
trends = getTrends(gg,printOut=True)
```  

## Get word cloud   
  
Feed it any text string, in this case its the text returned from trends.
   
It does all the regex and print on its side. 
  
Second parm, is just where you want to print the image too.  

```
make_wordCloud(trends, 'report/wordCloud.png')
```  

## Reference Dict

The API creators didn't generate a reference dicts for the API fields (weird), anyway I will build up the dict as I figure them out. 
  
If you are uncomfortable with this, I suggest building from scratching using requets like they did.  

```
udate       
_t          = I think this means type (post, update etc)
cdate
activity
_id
action
acl
txt
utgs
prevsrc
previmg
vis
ttl
dsc
uid
txt_lang
translates
lkbpst
cm
shbpst
vfpst
uinf
```
