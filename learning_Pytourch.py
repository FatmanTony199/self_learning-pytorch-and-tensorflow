import torch
import numpy as np
a = torch.tensor([[1, 2], [3, 4], [5, 6]])
print(a)
################################################
a = torch.tensor([[1, 2], [3, 4], [5, 6]], dtype=torch.float64)
print(a)
##############################################
a = torch.zeros([2, 2])
print(a)
##########################################
a = torch.ones([2, 2])
print(a)
#########################################
if torch.cuda.is_available():
	cuda0 = torch.device('cuda', 1)
	t1 = torch.tensor([[1, 2], [3, 4], [5, 6]], dtype=torch.float64, device=cuda0)