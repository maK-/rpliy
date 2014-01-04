<html>

<pre>
*List of Python Package Dependencies*
        -web.py (http://webpy.org )                                            apt-get install python-webpy
        -pygame (http://www.pygame.org/news.html)                              apt-get install python-pygame
        -ID3 (http://id3-py.sourceforge.net/)
        -Python MySQLDB (http://mysql-python.sourceforge.net/MySQLdb.html)     apt-get install python-mysqldb


---Run Commands---

./rpliy.py -q   (Runs without scanning dir for mp3's and default database.)
./rpliy.py [DIR] (scans [DIR] for mp3's and adds to database.)

</pre>
<pre>
---Simple Usage Example---

1. Connect raspberry pi to network (via wireless or ethernet)
2. plug in your usb containing mp3s
3. mount -t vfat /dev/sda1 /media/myusb
4. python rpliy.py /media/myusb
5. Plug the raspberry pi into speakers
6. Connect to the local address on your network via a phone or laptop
7. Add songs to your jukebox & play them!



---Demo Images---
</pre>
<h3>1. Initial bootup of app</h3>
<img src="SPAM1.png" width="683" height="384">
<br/>
<h3>2. Mp3's scanned off device and added to database.</h3>
<img src="SPAM2.png" width="683" height="384">
<br/>
<h3>3. Minimalist home screen search/playlist</h3>
<img src="SPAM3.png" width="683" height="384">
<br />
<h3>4. Simple Playlist controls play/pause/skip/stop</h3>
<img src="SPAM4.png" width="683" height="384">
<br />
<h3>5. Search through song database</h3>
<img src="SPAM5.png" width="683" height="384">
<br />
<h3>6. Select songs to add via ajax</h3>
<img src="SPAM6.png" width="683" height="384">
<br />
<h3>7. Basic controls</h3>
<img src="SPAM7.png" width="683" height="384">
<br />
</html>

