from Fetcher.Fetcher import Fetcher
from Parser.Parser import Parser

fetch = Fetcher()
filename, data = fetch.run()
print(data.keys())
par = Parser(data=data)
print(par.parse_regions())