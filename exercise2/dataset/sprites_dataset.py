import random

<<<<<<< HEAD
import torch
=======
>>>>>>> 7a1d79814df4e5dcf930aa4e7c51ab4be33cdc4d
from torch.utils.data import Dataset

import numpy as np
from .helpers import set_seed

class SpritesDataset(Dataset):
    def __init__(self, 
            transform,
            sfilename='exercise2/data/sprites.npy', 
            lfilename='exercise2/data/labels.npy', 
            num_samples=40000,
            seed=1,
        ):
        self.images = np.load(sfilename)
        labels = np.load(lfilename)
        self.labels = np.argmax(labels, axis=1) 

        # Reduce dataset size
        if num_samples:
            set_seed(seed=seed)
            sampled_indeces = random.sample(range(len(self.images)), num_samples)
            self.images = self.images[sampled_indeces]
            self.labels = self.labels[sampled_indeces]


        self.transform = transform
       
                
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        image = self.images[idx]
        label = self.labels[idx]
        if self.transform:
            image = self.transform(image)
        return image, label

  