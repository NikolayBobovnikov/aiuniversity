import gdown
import sys

print(sys.version)


gdown.download(
    "https://storage.googleapis.com/terra_ai/DataSets/tesla.zip", None, quiet=True
)
