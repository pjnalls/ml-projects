# ================================================
# Initialize Environment
# ================================================
import retro
import torch
from torch import nn
from torchvision import transforms as T
from PIL import Image
import numpy as np
from pathlib import Path
from collections import deque
import random, datetime, os

# Gym is an OpenAI toolkit for RL
import gym
from gym.spaces import Box
from gym.wrappers import FrameStack

# SNES Emulator for OpenAI Gym
from nes_py.wrappers import JoypadSpace

gym_super_mario_world = retro.make('SuperMarioWorld-Snes', 'DonutPlains1.state')

from tensordict import TensorDict
from torchrl.data import TensorDictReplayBuffer, LazyTensorDictReplayBuffer

# if gym.__version__ < '0.26':
#     env = retro.make('SuperMarioWorld-Snes', 'DonutPlains1.state', new_step_api=True)
# else:
#     env = retro.make('SuperMarioWorld-Snes', 'DonutPlains1.state', render_mode='rgb_array')
env = JoypadSpace(gym_super_mario_world, [['right'], ['right', 'A']])

env.reset()

next_state, reward, done, trunc, info = env.step(action = 0)
print(f"{next_state.shape},\n {reward},\n {done},\n {info}")