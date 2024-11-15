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
	numpy1 = t1.numpy()
	print("numpy1:", numpy1)
	print("type:", type(numpy1))
#######################################
numpy2 = np.array([[1, 2, 3], [4, 5, 6]])

tensor1 = torch.tensor(numpy2)
print("dtype:", tensor1.dtype)