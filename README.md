# bat-rises
a simple tool for fetching files from a remote directory
## usage

#### setup
You need to configure the _conf.ini_ before running the program.<br>
The default values point to empty files inside the program folder tree<br>
so without configuration the program does nothing.<br>

#### create logs 
` bat-rises.py clogs `<br>
the program initially logs all the _"last modified"_ dates of the remote files.<br>
it does this when *logs.json* does not exist.<br>
**clogs** argument lets you create them manually.<br>

#### get files from the remote location
` python bat-rises.py pull `
#### upload files to remote location
` python bat-rises.py push `

