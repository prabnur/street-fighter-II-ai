from tensorflow.keras import Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, LSTM
from tensorflow.keras.optimizers import Adam

def vanilla(neuron_count, activation, final_activation):
    nb_actions = 10
    nb_obs = 11
    model = Sequential()
    # model.add(Dense(nb_obs, input_shape=(11)))
    model.add(Flatten(input_shape=(1,11)))
    model.add(Dense(nb_obs, input_shape=(11,)))
    model.add(Dense(neuron_count, activation=activation))
    model.add(Dense(neuron_count, activation=activation))
    model.add(Dense(neuron_count, activation=activation))
    model.add(Dense(nb_actions, input_shape=(10,), activation=final_activation))
    return model

def convex(neuron_count, activation, final_activation): # smol large smol
    nb_actions = 10
    nb_obs = 11
    model = Sequential()
    # model.add(Dense(nb_obs, input_shape=(11)))
    model.add(Flatten(input_shape=(1,11)))
    model.add(Dense(nb_obs, input_shape=(11,)))
    model.add(Dense(neuron_count-6, activation=activation))
    model.add(Dense(neuron_count+4, activation=activation))
    model.add(Dense(neuron_count-6, activation=activation))
    model.add(Dense(nb_actions, input_shape=(10,), activation=final_activation))
    return model

def concave(neuron_count, activation, final_activation): # large smol large
    nb_actions = 10
    nb_obs = 11
    model = Sequential()
    # model.add(Dense(nb_obs, input_shape=(11)))
    model.add(Flatten(input_shape=(1,11)))
    model.add(Dense(nb_obs, input_shape=(11,)))
    model.add(Dense(neuron_count, activation=activation))
    model.add(Dense(neuron_count-6, activation=activation))
    model.add(Dense(neuron_count, activation=activation))
    model.add(Dense(nb_actions, input_shape=(10,), activation=final_activation))
    return model

def less_layer(neuron_count, activation, final_activation):
    nb_actions = 10
    nb_obs = 11
    model = Sequential()
    # model.add(Dense(nb_obs, input_shape=(11)))
    model.add(Flatten(input_shape=(1,11)))
    model.add(Dense(nb_obs, input_shape=(11,)))
    model.add(Dense(neuron_count, activation=activation))
    model.add(Dense(nb_actions, input_shape=(10,), activation=final_activation))
    return model

# Needs to be configured!
def lstm(neuron_count, activation, final_activation):
    nb_actions = 10
    nb_obs = 11
    model = Sequential()
    # model.add(Dense(nb_obs, input_shape=(11)))
    model.add(Flatten(input_shape=(1,11)))
    model.add(Dense(nb_obs, input_shape=(11,)))
    model.add()
    model.add(Dense(neuron_count, activation=activation))
    model.add(Dense(nb_actions, input_shape=(10,), activation=final_activation))
    return model
