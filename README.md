# SiteScraper

This repository contains the following methods:

## 'yt_vedio()'
This method uses Selenium and Firefox web driver to scrape YouTube videos' title, views, and upload time from a given URL. It returns a dictionary with keys 'title', 'views', and 'when', and corresponding values.

## 'yt_vedio_comment()'
This method uses Selenium and Firefox web driver to scrape YouTube comments' text, likes, and time posted from a given URL. It returns a Pandas DataFrame with columns 'comment_text', 'likes', and 'comment_time', and corresponding values.

To use these methods, you will need to have Python 3 installed, along with the following libraries: pandas, selenium, and geckodriver-autoinstaller.

To install the required libraries, you can use pip:


pip install pandas selenium geckodriver-autoinstaller


To run the methods, you will need to import the SiteScraper module and create an instance of the 'yt_vedio' or 'yt_vedio_comment' class:


import SiteScraper as ss

# create an instance of yt_vedio class
```

import SiteScraper as ss
import pandas as pd 
df = ss.yt_vedio()
new_data = df.yt_vedios_data('https://www.youtube.com/@campusx-official/videos')
dataframe = pd.DataFrame(new_data)
dataframe.to_csv('campusx.csv', index=False)

```

# create an instance of yt_vedio_comment class


```

import SiteScraper as ss
import pandas as pd 
df = ss.yt_vedio_comment()
new_data = df.yt_vedio_comment('https://www.youtube.com/watch?v=xxxxxxxx')
dataframe = pd.DataFrame(new_data)
dataframe.to_csv('youtube_comments.csv', index=False)

```



Note that you will need to replace the URL with the actual YouTube URL that you want to scrape.
New methods will be commited for twitter and reddit 
#  Note this is for running SiteScraper in google colab : 
```

#run this command in the cell 
!apt-get update
!apt-get install chromium  chromium-driver
!pip install selenium

```
```

%%shell

# Add debian buster
cat > /etc/apt/sources.list.d/debian.list <<'EOF'
deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster.gpg] http://deb.debian.org/debian buster main
deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster-updates.gpg] http://deb.debian.org/debian buster-updates main
deb [arch=amd64 signed-by=/usr/share/keyrings/debian-security-buster.gpg] http://deb.debian.org/debian-security buster/updates main
EOF

# Add keys
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DCC9EFBF77E11517
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 648ACFD622F3D138
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 112695A0E562B32A

apt-key export 77E11517 | gpg --dearmour -o /usr/share/keyrings/debian-buster.gpg
apt-key export 22F3D138 | gpg --dearmour -o /usr/share/keyrings/debian-buster-updates.gpg
apt-key export E562B32A | gpg --dearmour -o /usr/share/keyrings/debian-security-buster.gpg

# Prefer debian repo for chromium* packages only
# Note the double-blank lines between entries
cat > /etc/apt/preferences.d/chromium.pref << 'EOF'
Package: *
Pin: release a=eoan
Pin-Priority: 500


Package: *
Pin: origin "deb.debian.org"
Pin-Priority: 300


Package: chromium*
Pin: origin "deb.debian.org"
Pin-Priority: 700
EOF

```
