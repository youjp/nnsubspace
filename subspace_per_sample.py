from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

import nnsubspace.visual.subspaceplot as subspaceplot
from nnsubspace.nndataset.dataset import Dataset
from nnsubspace.nnmodel.model import NNModel
from nnsubspace.nnsubspace.subspace import NNSubspace

dataset_name = 'cifar10'

dataset_ = Dataset(dataset=dataset_name)
model_ = NNModel(dataset=dataset_name, model_id='0')

for i_sample, x in enumerate(dataset_.x_test[0:5000]):
    x = np.expand_dims(x, axis=0)
    y = model_.model.predict(x)
    if y.max() < 0.7:
        print('sample {}'.format(i_sample))
        dataset_.decode_predictions(y)
        dataset_.decode_predictions(dataset_.y_test[i_sample])

        subspaceplot.imshow(np.squeeze(x + dataset_.x_train_mean), figsize=(2, 2))

        AS = NNSubspace(model=model_.model, x=x, x_train_mean=dataset_.x_train_mean)

        AS.sampling_setup(num_gradient_mc=600,
                          num_rs_mc=600,
                          seed=7,
                          bool_clip=True,
                          sigma=2 / 255,
                          num_eigenvalue=20)
        AS.run()

# Test single sample
# i_sample = 259
# x = dataset_.x_test[i_sample]
# x = np.expand_dims(x, axis=0)
# y = model_.model.predict(x)
# print('sample {}'.format(i_sample))
# dataset_.decode_predictions(y)
# dataset_.decode_predictions(dataset_.y_test[i_sample])
#
# subspaceplot.imshow(np.squeeze(x + dataset_.x_train_mean), figsize=(2, 2))
#
# AS = NNSubspace(model=model_.model, x=x, x_train_mean=dataset_.x_train_mean)
#
# AS.sampling_setup(num_gradient_mc=667,
#                  num_rs_mc=50000,
#                  seed=7,
#                  bool_clip=True,
#                  sigma=50 / 255,
#                  num_eigenvalue=20)
# AS.run()
