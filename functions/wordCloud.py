import re
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def make_wordCloud(text,outputPath,show=True):
    text = re.sub(r'==.*?==+', '', text)
    text = text.replace('\n', '')
    
    # Generate word cloud
    wordcloud = WordCloud(width= 3000, 
                          height = 2000, 
                          random_state=1, 
                          background_color='black', 
                          colormap='Pastel1', 
                          collocations=False, 
                          stopwords = STOPWORDS).generate(text)
    # Set figure size
    plt.figure(figsize=(40, 30))
    if(show):
      # Display image
      plt.imshow(wordcloud) 
    
    # -----No axis details needed

    plt.axis("off");

    # -----------SAVE TO PATH

    print('Saving image to ' + str(outputPath))
    exists = os.path.isfile(outputPath)
    if exists:
        os.remove(outputPath)


    plt.savefig(outputPath)
    plt.close()

    print('Done \n') 
