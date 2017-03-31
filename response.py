import os
FILE = 'response.html'

class Response:
  def __init__(self):
    self.file = os.open(os.curdir + os.sep + FILE, os.O_RDWR|os.O_CREAT)
    os.ftruncate(self.file, 0)
    os.lseek(self.file, 0, os.SEEK_SET)
    os.write(self.file,
"""
<head>
  <title>Head</title>
</head>
<body>
  <h1> Body: </h1>
  <ol>
  </ol>
</body>
"""
    )
    
  def up(self,time):
    os.lseek(self.file, -14, os.SEEK_END)
    os.write(self.file, "  <li>" + time +
"""</li>
  </ol>
</body>
"""
)

