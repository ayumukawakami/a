from PIL import Image
import imagehash

hash_1a = imagehash.average_hash(Image.open('cat.jpg'))
hash_1p = imagehash.phash(Image.open('cat.jpg'))
hash_1d = imagehash.dhash(Image.open('cat.jpg'))
hash_1w = imagehash.whash(Image.open('cat.jpg'))

hash_2a = imagehash.average_hash(Image.open('paprika-966290_640.jpg'))
hash_2p = imagehash.phash(Image.open('paprika-966290_640.jpg'))
hash_2d = imagehash.dhash(Image.open('paprika-966290_640.jpg'))
hash_2w = imagehash.whash(Image.open('paprika-966290_640.jpg'))

a=0x95c86eb7a174614b
b=0xa53bda84706b0eda
print('ahash : ', hash_2a-hash_1a)
print('phash : ', hash_2p)
print('dhash : ', hash_1p)
print('whash : ', a-b)

