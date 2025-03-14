import os
from keras.datasets import mnist

# disable log, maybe need rebuild tensorflow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

print('mnist: ', mnist)

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.ndim)
print(train_images.shape)
print(train_images.dtype)

# show 4th digit in train image
# digit=train_images[1]

# import matplotlib.pyplot as plt
# plt.imshow(digit, cmap=plt.cm.binary)
# plt.show()

# img_slice=train_images[10:100]
img_slice=train_images[0:1, 20:, 20:]
print(img_slice, img_slice.shape)



