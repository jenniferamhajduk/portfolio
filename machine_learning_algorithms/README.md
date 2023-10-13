# Algorithms for Creative AI - Please note that this repository is a work in progress!

Welcome to this high-level intro to Generative AI algorithms. I created this repository to be an educational tour of algorithms that power Generative AI applications. While this is not aimed at beginners, everyone can benefit from learning a little bit more every day.

# Tools

I will include a list of tools that I used to run the examples:

- [Visual Studio Code](https://code.visualstudio.com/download)
- [Jupyter Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [SKLearn](https://scikit-learn.org/stable/index.html)
- [NumPy](https://numpy.org/)
- [PyTorch](https://pytorch.org/)
- [Google Colab](https://colab.research.google.com)

## Data Representation

Computers cannot see, smell or feel the world around them. We can, however, abstract these sense into data so that a machine can perform predictions or generate new content. The data representation lesson talks about how we do this and gives a simple example that you can run on your own. We do a manual example and then turn to tools that are much better at it than we are.

## Neural Networks

At the heart of generative AI are multi-layer perceptrons, more commonly known as neural networks. One of the important concepts behind neural networks are that they introduce non-linearity to predictions through the use of Activation Functions. If we were to take a simple function that add 2 to any number, as the input number increases, adding 2 to that number would result in just a larger number. Activation Functions are more complicated in that they do not lead to predictions that increase with the input data. There are other parts of Neural Networks that are great to learn about as well. Variations of neural networks power AI algorithms and they are relatively good at it. The following algorithms are neural networks with the specific purpose of generating content.

## Recurrent Neural Networks

Recurrent Neural Networks are used with time series data. They are used with sequential data. Fully connected RNNs connect the outputs of each neuron to the input of each neuron. This is one of the unique things about RNNs, that they allow the output of neurons to affect the input of neurons. Recurrent neural netowrks are often illustrated as "unfolding" as time goes on. Each "fold" may appear as a "layer" typically seen in other types of Artificial Neural Networks but, in fact, is simply a fully connected RNN at different time steps. The variants (there are many) of RNNs that are commonly used within generative tasks are Long Short Term Memory and Gated Recurrent Units. 
RNNs can be used for a variety of tasks including NLP.

## Autoencoders

Autoencoders work in an interesting way. We talked a bit about data representation above so lets talk about dimensionality. Input data can be highly dimensional. This means that the data has a high number of features relative to the sample size. There can be a host of issues with high dimensional data, including algorithmic complexity, overfitting, and data sparsity. So, we want to be careful to pick out the most important features of the data. Autoencoders take input data and reduce the dimensionality of the data with a process called encoding. Then, they attempt to decode the low dimensional representation of the data to reproduce the original input. The samples folder will be empty. The dataset used can be found [here](https://www.kaggle.com/datasets/fournierp/captcha-version-2-images)

## Generative Adversarial Networks (GAN)

These are my favoritive generative algorithms. They are actually composed of two neural networks, a generator and discriminator and these two networks play a game to refine the generated content. The generator learns how to recreate the input data and the discriminator has to try to distinguish between the generated data and the real input data. Very cool! These algorithms are known fo producing high quality image and video content.

## Transformers

Transformers use something called attention in order to capture contextual relationships between data. Hello ChatGPT...also known a a Generative PreTrained Transformer. Using attention mechanisms is a way for applications such a chatbots to "understand" what you are saying and respond in kind. Transformers are used commonly in Natural Language Processing (NLP). It is not easy for algorithms to understand how we communicate. Certain words can carry multiple meanings depending on context and positioning in a sentence. Single words can be sentences. There are also quirks to any language like idioms, expressions, etc. Attention mechanisms allow transformers to focus in on the important words in input. Transformers take context into consideration when processing language. This allow the algorithm to choose the the right words to respond with in a chat application.
