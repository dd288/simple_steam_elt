"""

"""

from yoyo import step

__depends__ = {'20240424_01_pM8l1'}

steps = [
    step(
	"""
	 INSERT INTO steam."steam.topgames" (
       	 appid INT,
       	 name VARCHAR (50),
       	 developer VARCHAR (50),
       	 positive INT,
       	 negative INT,
       	 price VARCHAR (50),
       	 ccu INT
    	)
	"""
)
]
