# Comandos usados no Coleb para o Desafio de Projeto de Redes Neurais

### Importanto pacote Kaggle e fazendo o upload do DataBase


!pip install kaggle


!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json


!kaggle competitions download -c dogs-vs-cats


- Extraindo o conjunto de dados compactado

from zipfile import ZipFile

dataset = '/content/dogs-vs-cats.zip'

with ZipFile(dataset, 'r') as zip:
  zip.extractall()
  print('Dataset extraido')


- Extraindo o conjunto de dados compactado

from zipfile import ZipFile

dataset = '/content/train.zip'

with ZipFile(dataset, 'r') as zip:
  zip.extractall()
  print('Dataset extraido')

- Contando o número de arquivos na pasta train
import os
path, dirs, files = next(os.walk('/content/train'))
file_count = len(files)
print('Number of images: ', file_count)


- Imprimindo o nome das imagens

file_names = os.listdir('/content/train')
print(file_names)


- Importando dependencias

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from sklearn.model_selection import train_test_split
from google.colab.patches import cv2_imshow 


### Exibindo as imagens de cães e gatos

- Exibindo imagem de cachorro

img = mpimg.imread('/content/train/dog.3788.jpg')
imgplt = plt.imshow(img)
plt.show()

- Exibindo imagem de gato
img = mpimg.imread('/content/train/cat.11763.jpg')
imgplt = plt.imshow(img)
plt.show()


- Os arquivos possuem o mesmo nome?
file_names = os.listdir('/content/train/')

for i in range(5):

  name = file_names[i] 
  print(name[0:3])


- Quantidade de imagens de gatos e de cachorros.

file_names = os.listdir('/content/train/')

dog_count = 0
cat_count = 0

for img_file in file_names:

  name = img_file[0:3]

  if name == 'dog':
    dog_count += 1

  else:
    cat_count += 1

print('Number of dog images =', dog_count)
print('Number of cat images =', cat_count)


### Redimensionando todas as imagens

- Criando um diretório para imagens redimensionadas

os.mkdir('/content/image resized')

- Redimencionando

original_folder = '/content/train/'
resized_folder = '/content/image resized/'

for i in range(2000):

  filename = os.listdir(original_folder)[i]
  img_path = original_folder+filename

  img = Image.open(img_path)
  img = img.resize((224, 224))
  img = img.convert('RGB')

  newImgPath = resized_folder+filename
  img.save(newImgPath)

  - Exibindo imagem de cachorro redimencionada

img = mpimg.imread('/content/image resized/dog.3788.jpg')
imgplt = plt.imshow(img)
plt.show()


- Exibindo imagem de gato redimencionada

img = mpimg.imread('/content/image resized/cat.11763.jpg')
imgplt = plt.imshow(img)
plt.show()

### Criação de rótulos para imagens redimensionadas de cães e gatos

Cat --> 0

Dog --> 1


- Criando um loop for para atribuir rótulos
filenames = os.listdir('/content/image resized/')


labels = []

for i in range(2000):

  file_name = filenames[i]
  label = file_name[0:3]

  if label == 'dog':
    labels.append(1)

  else:
    labels.append(0)


print(filenames[0:5])
print(len(filenames))


print(labels[0:5])
print(len(labels))


- Contando as imagens de cães e gatos de 2000 imagens

values, counts = np.unique(labels, return_counts=True)
print(values)
print(counts)



### Convertendo todas as imagens redimensionadas em matrizes numpy

import cv2
import glob


image_directory = '/content/image resized/'
image_extension = ['png', 'jpg']

files = []

[files.extend(glob.glob(image_directory + '*.' + e)) for e in image_extension]

dog_cat_images = np.asarray([cv2.imread(file) for file in files])



- Exibindo matriz Dog/Cat

print(dog_cat_images)


type(dog_cat_images)


- Pegando as labels em forma de lista e converter para um numpy array

- Criando duas variaveis X e Y por ser mais conveniente

X = dog_cat_images
Y = np.asarray(labels)


- Divisão de teste de trem

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)


- Verificar o formato das imagens

print(X.shape, X_train.shape, X_test.shape)


1600 --> training images

400 --> test images


- Escalando os dados

X_train_scaled = X_train/255

X_test_scaled = X_test/255


print(X_train_scaled)


### Construindo a Rede Neural

import tensorflow as tf
import tensorflow_hub as hub


mobilenet_model = 'https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4'

pretrained_model = hub.KerasLayer(mobilenet_model, input_shape=(224,224,3), trainable=False)


num_of_classes = 2

model = tf.keras.Sequential([
    
    pretrained_model,
    tf.keras.layers.Dense(num_of_classes)

])

model.summary()



model.compile(
    optimizer = 'adam',
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics = ['acc']
)


score, acc = model.evaluate(X_test_scaled, Y_test)
print('Test Loss =', score)
print('Test Accuracy =', acc)


### Sistema Preditivo

- Testando imagem dog.jpg
input_image_path = input('Path of the image to be predicted: ')

input_image = cv2.imread(input_image_path)

cv2_imshow(input_image)

input_image_resize = cv2.resize(input_image, (224,224))

input_image_scaled = input_image_resize/255

image_reshaped = np.reshape(input_image_scaled, [1,224,224,3])

input_prediction = model.predict(image_reshaped)

print(input_prediction)

input_pred_label = np.argmax(input_prediction)

print(input_pred_label)

if input_pred_label == 0:
  print('Isso é um gato.')

else:
  print('Isso é um cachorro.')


- Testando imagem 02

input_image_path = input('Path of the image to be predicted: ')

input_image = cv2.imread(input_image_path)

cv2_imshow(input_image)

input_image_resize = cv2.resize(input_image, (224,224))

input_image_scaled = input_image_resize/255

image_reshaped = np.reshape(input_image_scaled, [1,224,224,3])

input_prediction = model.predict(image_reshaped)

print(input_prediction)

input_pred_label = np.argmax(input_prediction)

print(input_pred_label)

if input_pred_label == 0:
  print('A imagem representa um cachorro.')

else:
  print('A imagem representa um gato.')