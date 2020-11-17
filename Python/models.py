from tensorflow.keras import Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, LSTM
from tensorflow.keras.optimizers import Adam


def final():
    nb_actions = 10
    nb_obs = 11
    model = Sequential()
    # model.add(Dense(nb_obs, input_shape=(11)))
    model.add(Flatten(input_shape=(1,11)))
    model.add(Dense(nb_obs, input_shape=(11,)))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(nb_actions, input_shape=(10,), activation='sigmoid'))
    return model

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

def custom_intermediary(input_shape):
    nb_actions = 10
    nb_obs = 11
    activation = 'relu'
    final_activation = 'sigmoid'
    model = Sequential()
    # model.add(Dense(nb_obs, input_shape=(11)))
    model.add(Flatten(input_shape=(1,11)))
    model.add(Dense(nb_obs, input_shape=(11,)))
    model.add(Dense(input_shape[0], activation=activation))
    model.add(Dense(input_shape[1], activation=activation))
    model.add(Dense(input_shape[2], activation=activation))
    model.add(Dense(nb_actions, input_shape=(10,), activation=final_activation))
    return model

def equalised_weight(neuron_count):
    nb_actions = 10
    nb_obs = 11
    model = Sequential()
    # model.add(Dense(nb_obs, input_shape=(11)))
    model.add(Flatten(input_shape=(1,11)))
    model.add(Dense(nb_obs, input_shape=(11,)))
    model.add(Dense(neuron_count, activation='sigmoid'))
    model.add(Dense(neuron_count, activation='relu'))
    model.add(Dense(neuron_count, activation='relu'))
    model.add(Dense(nb_actions, input_shape=(10,), activation='relu'))
    return model

def convex(neuron_count, activation, final_activation): # smol large smol
    nb_actions = 10
    nb_obs = 11
    model = Sequential()
    # model.add(Dense(nb_obs, input_shape=(11)))
    model.add(Flatten(input_shape=(1,11)))
    model.add(Dense(nb_obs, input_shape=(11,)))
    model.add(Dense(8, activation=activation))
    model.add(Dense(12, activation=activation))
    model.add(Dense(8, activation=activation))
    model.add(Dense(nb_actions, input_shape=(10,), activation=final_activation))
    return model

def concave(neuron_count, activation, final_activation): # large smol large
    nb_actions = 10
    nb_obs = 11
    model = Sequential()
    # model.add(Dense(nb_obs, input_shape=(11)))
    model.add(Flatten(input_shape=(1,11)))
    model.add(Dense(nb_obs, input_shape=(11,)))
    model.add(Dense(12, activation=activation))
    model.add(Dense(3, activation=activation))
    model.add(Dense(12, activation=activation))
    model.add(Dense(nb_actions, input_shape=(10,), activation=final_activation))
    return model

def less_layers(neuron_count, activation, final_activation):
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
    model.add(Dense(neuron_count, activation=activation))
    model.add(LSTM(8))
    model.add(Dense(neuron_count, activation=activation))
    model.add(Dense(nb_actions, input_shape=(10,), activation=final_activation))
    return model