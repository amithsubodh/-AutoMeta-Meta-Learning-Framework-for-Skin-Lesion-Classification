import sklearn, inspect
from sklearn.manifold import TSNE
print("✅ scikit-learn:", sklearn.__version__)
print("TSNE accepts:", list(inspect.signature(TSNE).parameters.keys()))