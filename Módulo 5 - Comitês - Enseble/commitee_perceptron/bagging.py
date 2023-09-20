import numpy as np

class Bagging:
    # Função para contar ocorrências e obter a classe com maior votação
    def majority_vote(self, column):
        counts = np.bincount(column)
        return np.argmax(counts)
    
    # Criando uma subdivisao nos dados com repetição
    def subsample(self, dataset, dataset_labels, ratio=1.0):
        n_sample = round(len(dataset) * ratio)
        indices = np.random.choice(len(dataset), n_sample, replace=True)
        sample = dataset[indices]
        sample_labels = dataset_labels[indices]
        
        return sample, sample_labels
        