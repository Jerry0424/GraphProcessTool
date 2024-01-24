import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def extract_cloud_features(gray_image, threshold=200):
    _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
    return binary_image

def create_cloud_model(binary_image):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y = np.nonzero(binary_image)
    z = np.random.uniform(low=0, high=1, size=x.shape[0])
    ax.scatter(x, y, z)
    plt.show()
    return fig

# 主程序
image_path = './inputImage/image2.png'
preprocessed_image = preprocess_image(image_path)
cloud_features = extract_cloud_features(preprocessed_image)
cloud_model = create_cloud_model(cloud_features)

# 将模型保存到文件
cloud_model.savefig('./outputImage/image3.png')
