from fuzzywuzzy import fuzz
from fuzzywuzzy import process

test = fuzz.token_sort_ratio("Barista", "Bar Staff")
print(test)

