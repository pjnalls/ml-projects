import sys
import torch

text = sys.argv[2]
# print(text)
# sys.stdout.flush()
# TODO: Fix argument weights_only erroring when True
model = torch.load('models/model.pth', weights_only=False)
result = model.predict(text)
print(result)
# sys.stdout.flush()
