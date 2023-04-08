# Copyright 2023 The oryx Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module for optimizers in Oryx."""
from oryx.experimental.optimizers.optix import adam
from oryx.experimental.optimizers.optix import gradient_descent
from oryx.experimental.optimizers.optix import noisy_sgd
from oryx.experimental.optimizers.optix import optimize
from oryx.experimental.optimizers.optix import rmsprop
from oryx.experimental.optimizers.optix import sgd
